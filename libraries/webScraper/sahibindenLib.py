from bs4 import BeautifulSoup
from seleniumbase import Driver
import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time, random, re
from sys import exit

from dataWorker import dataWorker


def sahibindenInit(driver):
    # Birkaç sayfada gezilerek bot koruması aşılmaya çalışılır.
    driver.get("https://www.sahibinden.com")

    sahibindenCaptchaCheck(driver)

    return True

def sahibindenCaptchaSolver(driver):
    try:
        WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='Cloudflare güvenlik görevi içeren pencere öğeleri']")))
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@class='ctp-checkbox-label']"))).click()
        print("Chechbox basıldı.")
    except Exception as e:
        print("Cloudflare Bypass edilemedi.")
        print(e)
        pass

    time.sleep(5)
    WebDriverWait(driver, 20)

    if re.match(r'https://www.sahibinden.com/', driver.current_url):
        print("Bot koruması aşıldı.")
    else:
        print("Bot koruması aşılamadı.")
        print(f'link: {driver.current_url}')
        print("Ekran görüntüsü kaydediliyor.")
        driver.save_screenshot("bot_koruma.png")

# Bu fonksiyon, sayfanın captcha ya dönüşüp dönüşmediğini kontrol eder.
def sahibindenCaptchaCheck(driver):
    if re.match(r'https://secure.sahibinden.com/*', driver.current_url):
        print("Bot koruması tespit edildi.")
        sahibindenCaptchaSolver(driver)
        WebDriverWait(driver, 20)
        return True
    else:
        print("Bot koruması tespit edilmedi.")
        return False
    

def sahibindenSearch(driver, sehir):
    webLink= "https://www.sahibinden.com/satilik-daire"
    driver.get(webLink)
    sahibindenCaptchaCheck(driver)

    # Bu sayfaya girince ekranda "aramanızı kaydedin" uyarısı çıkıyor
    # bu uyarıyı kapatmak için büyük kutucuğun arka planına tıklanır.
    time.sleep(4)
    action = ActionChains(driver)
    action.move_by_offset(0, 0).click().perform()

    # İlanın bulunduğu şehir seçilir.
    il = sehir
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "İl"))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, il))).click()

    # bütün çerezleri engelle
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, "onetrust-reject-all-handler"))).click()
    time.sleep(1)
    # son olarak "ara" butonuna tıklanır.
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".search-submit"))).click()

# Çağırıldığında, sadece bulunduğu sayfadaki ilanları konsola yazdırır.
def sahibindenPostRecorder(driver):

    current_url= driver.current_url
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    titles_raw = soup.find_all(class_="classifiedTitle")
    specs_raw = soup.find_all(class_="searchResultsAttributeValue")
    price_raw = soup.find_all(class_="classified-price-container")
    dates_raw = soup.find_all(class_="searchResultsDateValue")
    districts_raw = soup.find_all(class_="searchResultsLocationValue")

    titles = []
    h_refs = []

    specs = [sp.getText().strip() for sp in specs_raw]
    rooms = specs[1::2]
    square_meters = specs[0::2]
    prices = [pr.getText().strip() for pr in price_raw]
    dates = [dt.getText().strip().replace("\n\n", " ") for dt in dates_raw]
    districts = [BeautifulSoup(str(ds), 'html.parser').get_text(separator='-').replace('/n', '-').replace(' / ', '-').strip() for ds in districts_raw]


    for tt in titles_raw:
        titles.append(tt.getText().strip())
        h_refs.append("https://www.sahibinden.com" + tt.get("href"))

    for i in range(len(titles)):
        inputs = driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
        print("Title: " + titles[i])
        print("Link: " + h_refs[i])
        print("Square Meters: " + square_meters[i])
        print("Rooms: " + rooms[i])
        print("Price: " + prices[i])
        print("Date: " + dates[i])
        print("District: " + districts[i])
        print("--------------------------------------------------" + "\n")
    
        dataWorker.dataWorkerStart(titles[i], h_refs[i], square_meters[i], rooms[i], prices[i], dates[i], districts[i])

        prices[i] = prices[i].replace('.', '').replace(' TL', '')
        if prices[i].isnumeric():
            prices[i] = int(prices[i])
        else:
            ""
        
    
    return True

# Sayfa numarasını kademeli arttırır.
def sahibindenPageSet(driver, url, sayfaNumarasi):
    print("Mevcut sayfa numarası: " + str(sayfaNumarasi))
    print("Sayfa url: " + str(url))
          
    if sayfaNumarasi == "0":
        driver.get(url)
    else:
        pageIndex = 20 * int(sayfaNumarasi - 1)
        driver.get(url + "?pagingOffset=" + str(pageIndex))

    sahibindenCaptchaCheck(driver)
    return True
