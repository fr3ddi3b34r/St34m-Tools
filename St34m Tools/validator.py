import os
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from colorama import init, Fore, Style
import datetime
# Renkli çıktıları etkinleştirme
init(autoreset=True)

def auto_login():
    from colorama import Fore, Style

            # accounts.txt dosyasını oluştur
    if not os.path.isfile('accounts.txt'):
             with open("accounts.txt", 'w') as configfile:
                
                print(Fore.GREEN + "accounts.txt oluşturuluyor..."+ Style.RESET_ALL)
                print("accounts.txt oluşturuldu...")
        
    while True:
            try:
                # accounts.txt dosyasını oku ve ilk hesabı al
                with open("accounts.txt", "r") as file:
                    lines = file.readlines()
                    if len(lines) == 0:
                        print(Fore.MAGENTA + "Hesap bulunamadı. Lütfen accounts.txt dosyasını kontrol edin." + Style.RESET_ALL)
                        input(Fore.GREEN + "Hesap eklediyseniz herhangi bir tuşa basın..." + Style.RESET_ALL)
                        continue

                    account = lines[0].strip().split(';')
                    username = account[0].strip()
                    password = account[1].strip()
                    link = account[2].strip()
                    

                    print(Fore.GREEN + "Giriş yapılıyor..."+ Style.RESET_ALL , username )                    # Chrome sürücüsü ayarları
                    chrome_options = webdriver.ChromeOptions()
                    chrome_options.add_argument("--no-sandbox")
                    chrome_options.add_argument("--disable-dev-shm-usage")

                    # ChromeDriver hizmetini başlat
                    driver_service = Service("path/to/chromedriver")

                    # WebDriver'ı başlat
                    driver = webdriver.Chrome(service=driver_service, options=chrome_options)

                    # Sayfa yüklenene kadar beklemeyi etkinleştir
                    driver.implicitly_wait(3)  # 3 saniye boyunca sayfanın yüklenmesini bekler

                    # Siteyi aç
                    driver.get("https://store.steampowered.com/twofactor/manage")

                    # Kullanıcı adı ve şifre alanlarını bulmak için bekle
                    wait = WebDriverWait(driver, 10)
                    username_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="responsive_page_template_content"]/div/div[1]/div/div/div/div[2]/div/form/div[1]/input')))
                    password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="responsive_page_template_content"]/div/div[1]/div/div/div/div[2]/div/form/div[2]/input')))

                    # Kullanıcı adı ve şifreyi gir
                    username_field.send_keys(username)
                    password_field.send_keys(password)

                    # Giriş yap düğmesini bul
                    login_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="responsive_page_template_content"]/div/div[1]/div/div/div/div[2]/div/form/div[4]/button')))

                    # Giriş yap düğmesine tıkla
                    login_button.click()

                    # Yeni sayfada bulunan ilk düğmeye tıkla
                    driver.implicitly_wait(60)  # 3 saniye boyunca sayfanın yüklenmesini bekler
                    button1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email_authenticator_check"]')))
                    button1.click()
                    #
                    print(Fore.GREEN + "Başarıyla giriş yapıldı." + Style.RESET_ALL)
                    # Metin yazıldıktan sonra ikinci düğmeye tıkla
                    driver.implicitly_wait(60)  # 60 saniye boyunca sayfanın yüklenmesini bekler
                    button2 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="account_pulldown"]')))
                    button2.click()
                    # Metin yazıldıktan sonra ikinci düğmeye tıkla
                    driver.implicitly_wait(60)  # 60 saniye boyunca sayfanın yüklenmesini bekler
                    button3 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="account_dropdown"]/div/a[3]')))
                    button3.click()
                                    # Yeni sekme açma
                    driver.execute_script("window.open('', 'new_tab')")
                    # Son açılan sekme tanımlayıcısını al
                    window_handles = driver.window_handles
                    new_tab_handle = window_handles[-1]
                    # Yeni sekme geçişi yap
                    driver.switch_to.window(new_tab_handle)

                    # İstenilen siteye gidin
                    driver.get("https://store.steampowered.com/twofactor/manage")
                     # Kullanıcı adı ve şifre alanlarını bulmak için bekle
                    wait = WebDriverWait(driver, 10)
                    username_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="responsive_page_template_content"]/div/div[1]/div/div/div/div[2]/div/form/div[1]/input')))
                    password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="responsive_page_template_content"]/div/div[1]/div/div/div/div[2]/div/form/div[2]/input')))

                    # Kullanıcı adı ve şifreyi gir
                    username_field.send_keys(username)
                    password_field.send_keys(password)

                    # Giriş yap düğmesini bul
                    login_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="responsive_page_template_content"]/div/div[1]/div/div/div/div[2]/div/form/div[4]/button')))

                    # Giriş yap düğmesine tıkla
                    login_button.click()
                    print(Fore.GREEN + "Hesabın steam guard doğrulaması başarıyla yapıldı." + Style.RESET_ALL)
                    WebDriverWait(driver, 3)
                    # Hesabı unverified_accounts.txt dosyasından sil
                    with open("accounts.txt", "w") as file:
                        for line in lines[1:]:
                            file.write(line)
                    
                    if not os.path.isfile('verified_accounts.txt'):
                            with open("verified_accounts.txt", 'w') as configfile:
                        
                                print(Fore.MAGENTA + "verified_accounts.txt oluşturuluyor..."+ Style.RESET_ALL)
                                print(Fore.GREEN + "verified_accounts.txt oluşturuldu..." + Style.RESET_ALL)
                    #doğrulanan hesapları verified_accounts.txt ye ekle
                    with open("verified_accounts.txt", "a") as file:
                            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                            file.write(f"{current_time};{username};{password};{link}\n")
                            print(Fore.MAGENTA + "Doğrulanan hesap verified_accounts.txt'dosyasına kaydedildi." + Style.RESET_ALL)
                        # Hesap silindikten sonra geriye kaç hesap kaldığını yazdır
                            print(Fore.YELLOW + "Kalan Hesap Sayısı:", len(lines) - 1)
                    
                    #kaldırılcak
                    while True:

                            print(Fore.GREEN + "Giriş bölümüne aktarılıyor..." + Style.RESET_ALL)
                            # WebDriver'ı kapat
                            driver.quit()
                            break
                     #.
            except Exception as e:
                    print(Fore.RED + "Bir hata oluştu: " + str(e) + Style.RESET_ALL)
                    print(Fore.RED + "Hata sebebiyle döngü başa alınıyor..." + Style.RESET_ALL)

if __name__ == "__main__":
    auto_login()