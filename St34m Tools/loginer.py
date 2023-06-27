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

# Renkli çıktıları etkinleştirme
init(autoreset=True)

print(Fore.YELLOW + "Soru ve önerileriniz için discord üzerinden Eksi#9299 veya khebib#0001'e ulaşabilirsiniz. " + Style.RESET_ALL)


def manual_login():
    while True:
        try:
            # Kullanıcı adı ve şifreyi al
            username = input(Fore.CYAN + "Kullanıcı adınızı girin: " + Style.RESET_ALL)
            password = input(Fore.CYAN + "Şifrenizi girin: " + Style.RESET_ALL)
            
            print(Fore.GREEN + "Giriş yapılıyor..." , username + Style.RESET_ALL)                    # Chrome sürücüsü ayarları
            
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
            driver.get("https://steamcommunity.com/openid/loginform?need_password=1&force=1&goto=%2Fopenid%2Flogin%3Fopenid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.mode%3Dcheckid_setup%26openid.return_to%3Dhttps%253A%252F%252Floginhell.com%252Flogin%252Fsteam%252Fcallback%26openid.realm%3Dhttps%253A%252F%252Floginhell.com%26openid.ns_sreg%3Dhttp%253A%252F%252Fopenid.net%252Fextensions%252Fsreg%252F1.1%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid_mode%3Dcheckid_setup%26nonce%3D22d4b67f8659a2115ee200aa")

            # Kullanıcı adı ve şifre alanlarını bulmak için bekle
            wait = WebDriverWait(driver, 10)
            username_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input')))
            password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input')))

            # Kullanıcı adı ve şifreyi gir
            username_field.send_keys(username)
            password_field.send_keys(password)

            # Giriş yap düğmesini bul
            login_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[4]/button')))

            # Giriş yap düğmesine tıkla
            login_button.click()
            
            

            # Oturum açıldıktan sonra beklemek için uygun bir süre ayarla
            driver.implicitly_wait(60)  # 3 saniye boyunca sayfanın yüklenmesini bekler

            # Oturum açıldıktan sonra yeni sayfaya yönlendirme yapılıyor
            # İlgili sayfada oturum aç düğmesini bulmak için bekleyin
            new_page_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="imageLogin"]')))
            print(Fore.GREEN + "Başarıyla giriş yapıldı." + Style.RESET_ALL)
            # Otomatik olarak oturum aç düğmesine tıkla
            new_page_button.click()


            # Yeni sayfada bulunan ilk düğmeye tıkla
            driver.implicitly_wait(60)  # 3 saniye boyunca sayfanın yüklenmesini bekler
            button1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/header/div/div[2]/div[2]/div/button')))
            button1.click()

            # Açılan pencerede metin kutusunu bul ve "baso" yazısını gönder
            driver.implicitly_wait(60)  # 60 saniye boyunca sayfanın yüklenmesini bekler
            input_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div/div/input')))

            # Metin kutusuna tıkla ve "baso" yazısını gönder
            driver.implicitly_wait(60)  # 60 saniye boyunca sayfanın yüklenmesini bekler
            input_field.click()
            input_field.send_keys("baso")
            print(Fore.GREEN + "Promosyon kodu başarıyla kullanıldı." + Style.RESET_ALL)
            # Metin yazıldıktan sonra ikinci düğmeye tıkla
            driver.implicitly_wait(60)  # 60 saniye boyunca sayfanın yüklenmesini bekler
            button2 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/form/button[1]')))
            button2.click()

            # Son olarak üçüncü düğmeye tıkla
            driver.implicitly_wait(60)  # 60 saniye boyunca sayfanın yüklenmesini bekler
            button3 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div/div/div[1]/i')))
            button3.click()
        # İşlemler tamamlandı, program sonlanmaması için sonsuz bir döngüye girilir
            while True:
                choice = input(Fore.CYAN + "Farklı bir hesaptan giriş yapmak isterseniz --> (E): " + Style.RESET_ALL)
                if choice.upper() == "E":
                    print(Fore.GREEN + "Giriş bölümüne aktarılıyor..." + Style.RESET_ALL)
                    # WebDriver'ı kapat
                    driver.quit()
                    break
                else:
                    print(Fore.RED + 'Geçersiz seçenek. Lütfen tekrar giriş yapmak için "E" seçeneğini girin.' + Style.RESET_ALL)


        except Exception as e:
                print(Fore.RED + "Bir hata oluştu: " + str(e) + Style.RESET_ALL)
                print(Fore.RED + "Hata sebebiyle döngü başa alınıyor..." + Style.RESET_ALL)


def auto_login():
    from colorama import Fore, Style

    choice = input(
        Fore.LIGHTBLUE_EX + "Giriş yapmak için yöntem seçin: " +
        Fore.LIGHTYELLOW_EX + "\n1. " +
        Fore.LIGHTCYAN_EX + "Manuel giriş" +
        Fore.LIGHTYELLOW_EX + "\n2." +
        Fore.LIGHTCYAN_EX + "Otomatik giriş\n" +
        Fore.LIGHTBLUE_EX + "Seçiminiz: " + Style.RESET_ALL
    )


    if choice == "1":
        manual_login()
    elif choice == "2":
            # accounts.txt dosyasını oluştur
            if not os.path.isfile('accounts.txt'):
             with open("accounts.txt", 'w') as configfile:
                
                print(Fore.GREEN + "accounts.txt oluşturuluyor...")
                print("accounts.txt oluşturuldu..." + Style.RESET_ALL)
        
    while True:
            try:
                # accounts.txt dosyasını oku ve ilk hesabı al
                with open("accounts.txt", "r") as file:
                    lines = file.readlines()
                    if len(lines) == 0:
                        print(Fore.MAGENTA + "Hesap bulunamadı. Lütfen accounts.txt dosyasını kontrol edin." + Style.RESET_ALL)
                        input(Fore.GREEN + "Hesap eklediyseniz herhangi bir tuşa basın..." + Style.RESET_ALL)
                        continue

                    account = lines[0].strip().split(";")
                    username = account[0].strip()
                    password = account[1].strip()
                    link = account[2].strip()

                    print(Fore.GREEN + "Giriş yapılıyor..." , username + Style.RESET_ALL)                    # Chrome sürücüsü ayarları
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
                    driver.get("https://steamcommunity.com/openid/loginform?need_password=1&force=1&goto=%2Fopenid%2Flogin%3Fopenid.ns%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%26openid.mode%3Dcheckid_setup%26openid.return_to%3Dhttps%253A%252F%252Floginhell.com%252Flogin%252Fsteam%252Fcallback%26openid.realm%3Dhttps%253A%252F%252Floginhell.com%26openid.ns_sreg%3Dhttp%253A%252F%252Fopenid.net%252Fextensions%252Fsreg%252F1.1%26openid.claimed_id%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid.identity%3Dhttp%253A%252F%252Fspecs.openid.net%252Fauth%252F2.0%252Fidentifier_select%26openid_mode%3Dcheckid_setup%26nonce%3D22d4b67f8659a2115ee200aa")

                    # Kullanıcı adı ve şifre alanlarını bulmak için bekle
                    wait = WebDriverWait(driver, 10)
                    username_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[1]/input')))
                    password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[2]/input')))

                    # Kullanıcı adı ve şifreyi gir
                    username_field.send_keys(username)
                    password_field.send_keys(password)

                    # Giriş yap düğmesini bul
                    login_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="responsive_page_template_content"]/div[1]/div[1]/div/div/div/div[2]/div/form/div[4]/button')))

                    # Giriş yap düğmesine tıkla
                    login_button.click()
                    
                    

                    # Oturum açıldıktan sonra beklemek için uygun bir süre ayarla
                    driver.implicitly_wait(60)  # 3 saniye boyunca sayfanın yüklenmesini bekler

                    # Oturum açıldıktan sonra yeni sayfaya yönlendirme yapılıyor
                    # İlgili sayfada oturum aç düğmesini bulmak için bekleyin
                    new_page_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="imageLogin"]')))
                    print(Fore.GREEN + "Başarıyla giriş yapıldı." + Style.RESET_ALL)
                    # Otomatik olarak oturum aç düğmesine tıkla
                    new_page_button.click()


                    # Yeni sayfada bulunan ilk düğmeye tıkla
                    driver.implicitly_wait(60)  # 3 saniye boyunca sayfanın yüklenmesini bekler
                    button1 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-content"]/header/div/div[2]/div[2]/div/button')))
                    button1.click()

                    # Açılan pencerede metin kutusunu bul ve "baso" yazısını gönder
                    driver.implicitly_wait(60)  # 60 saniye boyunca sayfanın yüklenmesini bekler
                    input_field = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/form/div[2]/div/div/div/input')))

                    # Metin kutusuna tıkla ve "baso" yazısını gönder
                    driver.implicitly_wait(60)  # 60 saniye boyunca sayfanın yüklenmesini bekler
                    input_field.click()
                    input_field.send_keys("baso")
                    print(Fore.GREEN + "Promosyon kodu başarıyla kullanıldı." + Style.RESET_ALL)
                    # Metin yazıldıktan sonra ikinci düğmeye tıkla
                    driver.implicitly_wait(60)  # 60 saniye boyunca sayfanın yüklenmesini bekler
                    button2 = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="__layout"]/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/form/button[1]')))
                    button2.click()
                    
                    # Hesabı accounts.txt dosyasından sil
                    with open("accounts.txt", "w") as file:
                        for line in lines[1:]:
                            file.write(line)
                    
                    if not os.path.isfile('used_accounts.txt'):
                            with open("used_accounts.txt", 'w') as configfile:
                        
                                print(Fore.MAGENTA + "used_accounts.txt oluşturuluyor..."+ Style.RESET_ALL)
                                print(Fore.GREEN + "used_accounts.txt oluşturuldu..." + Style.RESET_ALL)

                    with open("used_accounts.txt", "a") as file:
                            file.write(f"{username};{password};{link}\n")
                            print(Fore.MAGENTA + "Kullanılan hesap used_accounts.txt'dosyasına kaydedildi." + Style.RESET_ALL)
                        # Hesap silindikten sonra geriye kaç hesap kaldığını yazdır
                            print(Fore.YELLOW + "Kalan Hesap Sayısı:", len(lines) - 1)
                    while True:
                        choice = input(Fore.CYAN + "Farklı bir hesaptan giriş yapmak isterseniz --> (E): " + Style.RESET_ALL)
                        if choice.upper() == "E":
                            print(Fore.GREEN + "Giriş bölümüne aktarılıyor..." + Style.RESET_ALL)
                            # WebDriver'ı kapat
                            driver.quit()
                            break
                        else:
                            print(Fore.RED + 'Geçersiz seçenek. Lütfen tekrar giriş yapmak için "E" seçeneğini girin.' + Style.RESET_ALL)

            except Exception as e:
                    print(Fore.RED + "Bir hata oluştu: " + str(e) + Style.RESET_ALL)
                    print(Fore.RED + "Hata sebebiyle döngü başa alınıyor..." + Style.RESET_ALL)

    else:
        print(Fore.RED + "Geçersiz seçenek. Lütfen 1 veya 2 seçeneğini girin." + Style.RESET_ALL)


if __name__ == "__main__":
    auto_login()