# Döviz Takip ve Tahmin Sistemi

Bu proje, Türkiye Cumhuriyet Merkez Bankası (TCMB) verilerini kullanarak döviz kurlarını (USD, EUR, CHF) takip eden, görselleştiren ve günlük olarak raporlayan bir sistemdir. Ayrıca Yapay zeka ile (Lineer regresyon) kullanarak Dolar kuru için gelecek tahminlerinde bulunur.

## Özellikler

*   **Veri Çekme:** TCMB'den XML formatında günlük kur verilerini otomatik olarak çeker.
*   **Veritabanı:** Çekilen verileri (Alış/Satış fiyatları) tarihsel olarak **SQLite** veritabanında saklar.
*   **Görselleştirme:** Matplotlib kullanarak USD, EUR ve CHF için zaman serisi grafikleri oluşturur.
*   **Tahminleme (Machine Learning):** Enflasyon, Faiz ve geçmiş kur verilerini kullanarak Scikit-learn ile **Lineer Regresyon** modeli eğitir ve gelecek 6 gün için dolar kuru tahmini yapar.
*   **Web Arayüzü:** Flask tabanlı bir web arayüzü ile anlık kurları, grafikleri ve tahmin sonuçlarını sunar.
*   **E-posta Bildirimi:** Günlük grafikleri ve kur bilgilerini içeren bir e-postayı belirlediğiniz adrese gönderir.

## Gereksinimler

Projenin çalışması için aşağıdaki Python kütüphanelerine ihtiyacınız vardır:

```bash
pip install flask pandas scikit-learn matplotlib requests python-dotenv
```

## Kurulum ve Yapılandırma

1.  Projeyi bilgisayarınıza indirin.
2.  Gerekli kütüphaneleri yukarıdaki komut ile yükleyin.
3.  Proje dizininde `password.env` adında bir dosya oluşturun veya mevcut olanı düzenleyin. İçeriği şu şekilde olmalıdır:

    ```env
    EMAİL=gonderici_mail_adresi@gmail.com
    APP_PASSWORD=google_app_password
    ```
    *(Not: Gmail kullanıyorsanız, 2 adımlı doğrulamayı açıp bir "Uygulama Şifresi" oluşturmanız gerekebilir.)*

## Kullanım

### Web Arayüzünü Başlatma

Web sunucusunu başlatmak için `API.py` dosyasını çalıştırın:

```bash
python API.py
```

Tarayıcınızda `http://127.0.0.1:5000` adresine giderek arayüzü görüntüleyebilirsiniz.

### Veri İşleme ve Mail Gönderme

İstatistiklerin güncellenmesi, grafiklerin oluşturulması ve raporun mail atılması işlemleri `Statistics.py` içerisindeki fonksiyonlarla yürütülür. Bu dosya `API.py` çalıştığında otomatik olarak çağrılır ve gerekli hesaplamaları yapar.

## Dosya Yapısı

*   `API.py`: Flask uygulamasını başlatır ve web arayüzünü sunar.
*   `Statistics.py`: Veri çekme, veritabanı kaydı, grafik oluşturma ve mail gönderme işlemlerini yapan ana modüldür.
*   `Linear.py`: Döviz tahmini için kullanılan regresyon modelini içerir.
*   `templates/index.html`: Web arayüzünün HTML şablonudur.
*   `Currency.db`: Kur verilerinin saklandığı veritabanı dosyası.


