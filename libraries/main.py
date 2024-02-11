from bs4 import BeautifulSoup

from seleniumbase import Driver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

import time, random, sys
from sys import exit

from webScraper import sahibindenLib
from dataWorker import dataWorker

driver = Driver(uc=True)

# Sahibinden.com bağlantısının kurulması ve emir beklenmesi
print("sahibinden.com bağlantısı kuruluyor...")
try:
    sahibindenLib.sahibindenInit(driver)
    print("sahibinden.com bağlantısı kuruldu.")
except Exception as e:
    print("sahibinden.com bağlantısı kurulamadı.")
    print(e)
    sys.exit()


# Örnek bir arama senaryosu
    
# arama sayfasına gidilmesi
sahibindenLib.sahibindenSearch(driver)


sayfaNumarasi = 0 # ilk sayfayı 0 kabul edelim

# filtreleme yapıldıktan sonra sayfanın ekrana yazdırılması
while True:
    try:
        sahibindenLib.sahibindenCaptchaCheck(driver)
        time.sleep(2)
        url = driver.current_url
        sahibindenLib.sahibindenPageSet(driver, url, sayfaNumarasi)
        sahibindenLib.sahibindenPostRecorder(driver)
        sayfaNumarasi += 1

        print(f"{sayfaNumarasi}. sayfa kaydedildi. Güvenlik amaçlı 2 saniye bekleniyor...")
        time.sleep(2)
    except Exception as e:
        print("Bir hata oluştu.")
        print(e)
        break

input("Devam etmek için bir tuşa basın...")

