---
description: >-
  Bir üst bilgi alanının değerinin nereden geldiği ve nasıl oluştuğu —
  doğrulama ekranındaki Üst Bilgi Alanı Kontrolü'nün arkasındaki açıklama.
---

# Üst Bilgi Alanı Kontrolü: Veriler nereden geliyor

**Üst Bilgi Alanı Kontrolü** düğmesi, doğrulama ekranında **Kaydet** düğmesinin yanında yer alır. *Her değer nereden geliyor?* raporunu açar: her üst bilgi alanı için belgede ne yazdığını, değerin yolda neyin değiştirdiğini, DocBits'in şimdi ne gösterdiğini ve nedenini gösterir.

Bu sayfa, bir değerin nasıl oluştuğunu ve her kaynağın ne anlama geldiğini açıklar. Uzmanlık bilgisi gerekmez.

{% hint style="info" %}
Üst Bilgi Alanı Kontrolü **Analytics** modülünün bir parçasıdır. Düğme gri görünüyorsa, bir yönetici bunu rolünüze **Ayarlar › Roller** altından verebilir.
{% endhint %}

## Bir değer her zaman şu sırayla oluşur

| Adım | Ne olur |
| --- | --- |
| **1. Okuma** | Değer belgeden okunur — eğitilmiş bir kuralla, yapay zekâyla veya doğrudan bir e-faturadan. |
| **2. Dönüştürme** | Müşterinin betikleri ve dönüştürme kuralları okunan değeri değiştirir: kısaltır, ekleme yapar, biçimini ayarlar. |
| **3. Arama** | Değer ana verilerde aranır. Bir şey bulunursa, ana veri kaydı okunan değerin yerini alır. |
| **4. Gösterme** | Kullanıcı yalnızca sonucu görür. Yolda neler olduğunu Üst Bilgi Alanı Kontrolü gösterir. |

2. ve 3. adımlar her zaman çalışmaz — ancak çalıştıklarında değeri değiştirirler. Bildirilen vakaların çoğu tam olarak buradan gelir.

## Kaynaklar — her birinin anlamı

Simgeler, raporun **İşlem** sütununda ve üstteki filtre çubuğunda gösterdikleriyle aynıdır.

### Eğitilmiş kural

DocBits, bir alanın bu belge türünde nerede durduğunu hatırlar, çünkü biri onu bir kez oraya işaretlemiştir.

* **Örnek:** Tedarikçi “Bornemann” — her zaman sol üstte aynı yerde.
* **Yanlışsa:** belgede doğru yeri işaretleyin ve kaydedin — kural bundan öğrenir.

### Yapay zekâ

Sabit bir kalıp yok. Yapay zekâ belgeyi bir insan gibi okur ve hangi metnin hangi alana ait olduğuna kendisi karar verir.

* **Örnek:** Fatura tarihi, tutarlar, ödeme koşulları.
* **Yanlışsa:** düzeltin. **Ayarlar › OCR üst bilgi alanları** altından açılıp kapatılabilir.

### E-fatura

XRechnung veya ZUGFeRD ile hiçbir şey tanınmaz: değer belgede zaten bir veri alanıdır ve doğrudan alınır.

* **Örnek:** Göndericinin XML alanındaki fatura numarası.
* **Yanlışsa:** hata göndericidedir. DocBits değerin tam olarak hangi XML alanından geldiğini gösterir.

### Betik / dönüştürme kuralı

Okumadan sonra müşterinin mantığı devreye girer ve değeri yeniden biçimlendirir. Belge aynı kalır — değer kalmaz.

* **Örnek:** `1001 / LS 206776` değeri `1001` olur.
* **Yanlışsa:** belgede aramayın. **Ayarlar › Betikler** veya **Dönüştürme kuralları** bölümünü kontrol edin.

### Ana veriler

Okunan değer kendi verilerinizde aranır — siparişler, tedarikçiler. Bir eşleşme değerin yerini alır ve başka alanları da beraberinde getirir.

* **Örnek:** `1001`, `06O051001` siparişini bulur — tedarikçi ve alıcı da artık oradan gelir.
* **Yanlışsa:** **Ayarlar › Lookup yapılandırması** bölümünü kontrol edin. Orada aramanın tam mı olduğu yoksa kısmi eşleşmeleri de kabul edip etmediği yazar.

### Hesaplanan

Okunmaz, diğer alanlardan hesaplanır.

* **Örnek:** Fatura tarihi artı ödeme koşullarından vade tarihi.
* **Yanlışsa:** genellikle hesaplamanın dayandığı alanlardan biri yanlıştır.

### Barkod

Belgedeki bir barkoddan veya QR kodundan okunur.

* **Örnek:** Fatura numarası QR koduna kodlanmıştır.
* **Yanlışsa:** belge türünün barkod ayarlarını kontrol edin.

## En sık yanlış anlaşılan şey

{% hint style="warning" %}
Bir alan birdenbire belgede bu şekilde görünmeyen bir değer içeriyorsa, bu neredeyse hiçbir zaman yapay zekâ değildir — 2. veya 3. adımdır. Çoğunlukla kısmi eşleşmeleri de kabul eden ana veri eşleşmesidir: `1001`, `06O051001` ile eşleşir ve bulunan siparişle birlikte tedarikçi de değişir.
{% endhint %}

Raporda böyle bir alan kırmızı işaretlenir. **İşlem** sütunu, ana veri kaydını kırmızı bir *yalnızca kısmi eşleşme* çipiyle birlikte gösterir ve değerin eşleşen kısmı vurgulanır.

## Raporu okuma

* Üstteki **durum çipleri**, belgeden değişmeden gelen, yolda değişen veya gösterildiği şekliyle belgede bulunmayan alanları sayar. Yalnızca o alanları göstermek için bir çipe tıklayın; hepsini göstermek için tekrar tıklayın.
* **Kaynak filtresi:** simge sırası her çıkarma yöntemini gösterir. Yalnızca o yöntemden geçen alanları göstermek için birine tıklayın.
* **İşlem:** değerin geçtiği her adım, kaynağının simgesiyle birlikte. Geçerli değerin geldiği adım vurgulanır. Her adımın ne yaptığını, hangi değerden hangisine geçtiğini görmek için üzerine gelin.
* **Neden:** alanın durumu. (i) simgesi değerin neden böyle olduğunu açıklar. *Alan yoktu* yazıyorsa, alan belgede mevcut değildi.
* Uzun değerler … ile kısaltılır — tam değeri görmek için üzerine gelin.
