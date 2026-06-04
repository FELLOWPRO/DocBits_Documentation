# Send HTTPS Request

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu DocBits kartı, belirtilen URL'lere HTTPS istekleri göndererek harici sistemlerle etkileşimi kolaylaştırmak için tasarlanmıştır. İş akışlarının API çağrıları yaparak veri alma, güncelleme veya silme gibi eylemleri gerçekleştirmesini sağlar ve harici servislerle sorunsuz entegrasyon sağlar.

## **İşlevsellik:**

* **HTTPS İstek Yürütme:** Kart, yapılandırılmış HTTP yöntemini (örn. GET, POST, PUT, DELETE) kullanarak belirtilen bir URL'ye bir istek gönderir.
* **Başlıklar ve Parametreler:** Kullanıcılar, isteğin harici API'nin gereksinimlerini karşılamasını sağlamak için özel başlıklar ve sorgu parametreleri ekleyebilir.
* **İstek Verisi:** Kullanıcıların, JSON veya form kodlu veri gibi istekle birlikte gönderilecek veri yükünü (varsa) tanımlamasına olanak tanır.
* **Yanıt Değerlendirmesi:** İş akışı, alınan durum kodunun beklenen değerle eşleşip eşleşmediğini kontrol eder ve devam etmeden önce başarılı iletişimi sağlar.
* **Desteklenen HTTP Yöntemleri:**
  * GET: Belirtilen URL'den veri alır.
  * POST: Kaynaklar oluşturmak için belirtilen URL'ye veri gönderir.
  * PUT: Belirtilen URL'deki mevcut kaynakları günceller.
  * DELETE: Belirtilen URL'den kaynakları kaldırır.

## **Kullanım:**

Bu kart, özellikle iş akışlarının bir CRM'e güncellemeler gönderme, sipariş durumlarını alma veya bir veritabanına yeni girişler ekleme gibi veri alışverişi için harici API'lerle etkileşime girmesi gereken senaryolarda yararlıdır.

## **Örnek Senaryo:**

* Bir kullanıcı, yeni sipariş ayrıntılarını içeren bir veri yüküyle harici bir sipariş yönetim sistemine bir POST isteği göndermek için kartı yapılandırır. API kimlik doğrulama belirteçlerini eklemek için özel başlıklar eklenir. Kart, yalnızca yanıt durum kodu 201 (Created) ise devam edecek şekilde ayarlanır. Durum kodu farklıysa, iş akışı manuel müdahale için bir hata bildirimi tetikler.

"Send HTTPS Request" kartını kullanarak kuruluşlar, harici entegrasyonları otomatikleştirebilir, sistemler arası iletişimi geliştirebilir ve karmaşık iş akışlarını kolaylaştırabilir.
