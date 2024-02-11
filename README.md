# SahibindenLib

sahibinden.com adresinden, tarayıcı ile (Google Chrome) veri çekme kütüphanesi

Bu repo tamamen eğitim amaçlıdır. Lütfen dikkatli ilerleyin ve kötü amaçlı kullanmayın.

## Çalışma Mantığı

Kütüphane sırayla libraries/ içerisindeki dosyalardan fonksiyonları çağırarak aşağıdaki örnek mantıkta gider.

- sahibinden.com a gir ve bot korumasını aş
- Emlak ilanları sayfasına gir ve şehir ismini aratarak sonuçları filtrele
- Sayfanın tam yüklenmesini bekle ve ilanların bilgilerini çek
- data.csv dosyasına yaz (yoksa oluştur). Eğer .CSV dosyasında varsa es geç

ve 3. adımdan itibaren tekrar et.

## Kütüphane Kullanımı

### sahibindenLib

#### sahibindenInit()

```python
  sahibindenLib.sahibindenInit(driver)
```

Chrome sayfası (driver) açar ve bot korumasını aşmaya çalışır.


| Parametre  | Tip      | Açıklama            |
| :--------- | :------- | :-------------------- |
| `driver`   | `string` | `selenium driver`     |
| `<return>` | `bool`   | `başarılıysa true` |

#### sahibindenCaptchaSolver()

CloudFlare sayfasını geçmeye çalışır

```python
  sahibindenLib.sahibindenCaptchaSolver(driver)
```


| Parametre | Tip      | Açıklama        |
| :-------- | :------- | :---------------- |
| `driver`  | `string` | `selenium driver` |

#### sahibindenCaptchaCheck()

Normal websitesinde mi yoksa Captcha sayfasında olup olmadığını kontrol eder

```python
  sahibindenLib.sahibindenCaptchaCheck(driver)
```


| Parametre  | Tip      | Açıklama            |
| :--------- | :------- | :-------------------- |
| `driver`   | `string` | `selenium driver`     |
| `<return>` | `bool`   | `başarılıysa true` |

#### sahibindenSearch()

/satilik-daire ye girer ve arama yapılacak şehri aratır.

```python
  sahibindenLib.sahibindenSearch(driver, sehir)
```


| Parametre | Tip      | Açıklama                |
| :-------- | :------- | :------------------------ |
| `driver`  | `string` | `selenium driver`         |
| `sehir`   | `string` | `arama yapılacak şehir` |

#### sahibindenPostRecorder()

Önceden arama yapılmış sayfada, sürekli sonraki sayfaya geçerek ilanları kopyalar. return fonksiyonu yerine içerisindeki "dataWorker.dataWorketStart()" fonksiyonu ile kayıt eder.

```python
  sahibindenLib.sahibindenPostRecorder(driver)
```


| Parametre | Tip      | Açıklama        |
| :-------- | :------- | :---------------- |
| `driver`  | `string` | `selenium driver` |

#### sahibindenPageSet()

Sonraki sayfaya, sayfa numarasını url'ye ekleyerek geçer.

```python
  sahibindenLib.sahibindenPostRecorder(driver, url, sayfaNumarasi)
```


| Parametre       | Tip       | Açıklama                             |
| :-------------- | :-------- | :------------------------------------- |
| `driver`        | `string`  | `selenium driver`                      |
| `url`           | `string`  | `sayfaNumarasi'sındaki url'ye gider.` |
| `sayfaNumarasi` | `integer` | `mevcut sayfa numarası`               |

## Kurulum

### Kurulum

#### Conda ile Kurulum

Conda başlatma

```bash
$ conda init
```

env oluşturma

```bash
$ conda create -n sahibindenLib python=3.8
```

env aktifleştirme

```bash
$ conda activate sahibindenLib
```

Gerekli Kütüphanelerin yüklenmesi

```bash
$ pip install -r sahibindenRequirements.txt
```

Eğer seleniumbase kütüphanesi hata verirse

```bash
$ python.exe -m pip install seleniumbase
```

## Örnek Kullanım

Örnek kullanım için libraries/playground.ipynb dosyası sırayla çalıştırılabilir.

## Hata Çözüm

- seleniumbase kütüphanesi yüklenirken hata veriyor:

```
$ python.exe -m pip install seleniumbase
```

- Warning: uc_driver not found. Getting it now...

```
Warning: uc_driver not found. Getting it now:

*** chromedriver to download = 121.0.6167.85 (Latest Stable) 

Downloading chromedriver-win64.zip from:
https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/121.0.6167.85/win64/chromedriver-win64.zip ...
Download Complete!

Extracting ['chromedriver.exe'] from chromedriver-win64.zip ...
Unzip Complete!

The file [uc_driver.exe] was saved to:
C:\Users\yildiz\.conda\envs\sahibindenLib\Lib\site-packages\seleniumbase\drivers\uc_driver.exe

Making [uc_driver.exe 121.0.6167.85] executable ...
[uc_driver.exe 121.0.6167.85] is now ready for use!
```

## Roadmap

- İlanların daha sonra tekrar kontrol edilerek daha fazla bilgi ve ilandan kaldırılma süresinin ölçülmesi.
- Makine modeline öğretilerek ilanın temel özelliklerine göre (ilçe-m2-kat-vs..) fiyat tahmini yapması.
