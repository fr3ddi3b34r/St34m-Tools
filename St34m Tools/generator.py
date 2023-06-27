import signal
import sys
import time
from colorama import Fore, init
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from colorama import Fore, Style
# Renkli çıktıları etkinleştirme
init(autoreset=True)

def get_element_text(driver, locator):
    element = WebDriverWait(driver, 60).until(EC.presence_of_element_located(locator))
    return element.text

def write_to_file(username, password, email):
    if not os.path.isfile('accounts.txt'):
        with open("accounts.txt", 'w') as configfile:
            print(Fore.MAGENTA + "accounts.txt oluşturuluyor..."+ Style.RESET_ALL)
            print(Fore.GREEN + "accounts.txt oluşturuldu..." + Style.RESET_ALL)
    with open('accounts.txt', 'a') as file:
            file.write(f"{username};{password};{email}\n")


def main():
    init()
    global driver
    driver = webdriver.Chrome()
    driver.get('https://sage.leodev.xyz/')
    previous_username = None
    previous_password = None
    previous_email = None
    is_info_changed = False
    
    
    while True:
        try:
            # Kullanıcı adı kopyalama
            username_locator = (By.CSS_SELECTOR, 'button[br-track="gen-copy-username"]')
            username = get_element_text(driver, username_locator)

            # Şifre kopyalama
            password_locator = (By.CSS_SELECTOR, 'span.font-semibold.group button[br-track="gen-copy-password"]')
            password_button_element = driver.find_element(*password_locator)
            password = password_button_element.get_attribute('innerHTML')

            # E-posta kopyalama
            email_locator = (By.CSS_SELECTOR, 'button[br-track="gen-copy-email"]')
            email = ""
            while email == "":
                email = get_element_text(driver, email_locator)
                if email == "(loading)":
                    email = ""
                    time.sleep(1)

            if username == previous_username or password == previous_password or email == previous_email:
                if not is_info_changed:
                    print(f"{Fore.CYAN}Bilgiler hala aynı, döngü başa dönüyor...{Fore.RESET}")
                    is_info_changed = False
                continue
            
            write_to_file(username, password, email)
            print(f"{Fore.GREEN}Bilgiler dosyaya yazıldı. Hesap: {Fore.RESET}{username}")
            previous_username = username
            previous_password = password
            previous_email = email
            is_info_changed = True


        except Exception as e:
            print(f"{Fore.RED}Hata alındı{Fore.RESET}")

        time.sleep(5)

    driver.quit()

if __name__ == '__main__':
    main()
