# Giriş Analitiği

**Giriş Analitiği**, yöneticilere kuruluş genelinde, salt okunur bir görünümde kullanıcıların DocBits'e *ne zaman* ve *ne sıklıkla* giriş yaptığını gösterir. "Girişler artış eğiliminde mi?", "Bu ay kaç farklı kullanıcı etkin oldu?" ve "Kullanım zirveleri ne zaman yaşanıyor?" gibi soruları yanıtlar — hiçbir kullanıcının kimlik bilgilerini veya kişisel verilerini açığa çıkarmadan.

> **Erişim:** **Ayarlar → Kuruluş ve Erişim → Kullanıcılar**'ı açın ve sağ üst köşedeki **Giriş Analitiği** düğmesine tıklayın (`/settings/login-analytics`).

<figure><img src="../../../../../.gitbook/assets/login_analytics_overview.png" alt="Etkinlik grafiği ve özet kartlarıyla Giriş Analitiği sayfası"><figcaption><p>Seçilen dönem boyunca kuruluş giriş etkinliği</p></figcaption></figure>

## Zaman aralığı

Analiz edilecek dönemi sağ üstteki seçiciyle belirleyin: **7D**, **30D**, **90D**, **180D**, **Year** veya serbest bir tarih aralığı için **Custom**. Sayfadaki her şey — grafik ve özet kartları — seçtiğiniz döneme göre yeniden hesaplanır.

**Data Information** afişi, görüntülenen dönemi tam olarak yeniden belirtir (örneğin *19.05.2026 ile 18.06.2026 arasındaki veriler gösteriliyor*), böylece rakamların hangi tarihleri kapsadığı her zaman açıktır.

## Giriş etkinliği grafiği

Grafik, seçilen dönem boyunca iki seriyi çizer:

| Seri | Anlamı |
|--------|---------|
| **Total Logins** | Aynı kişinin yinelenen girişleri dahil olmak üzere, gün başına giriş sayısı. |
| **Unique Users** | O gün giriş yapan *farklı* kullanıcı sayısı. |

O güne ait tam değeri okumak için herhangi bir noktanın üzerine gelin. Zirveler en yoğun günlerinizi gösterir; sivri bir **Total Logins** çizgisinin altında düz bir **Unique Users** çizgisi, birkaç kişinin birçok kez giriş yaptığı anlamına gelir.

## Özet kartları

Grafiğin altında, üç kart seçilen dönemin tamamını özetler:

| Kart | Anlamı |
|------|---------|
| **Total Logins** | Dönem boyunca tüm girişler. |
| **Unique Users** | En az bir kez giriş yapan farklı kullanıcılar. |
| **Avg/Day** | Dönem boyunca gün başına ortalama giriş sayısı. |

## Gizlilik

Giriş Analitiği yalnızca **toplam** rakamları raporlar — bir bütün olarak kuruluşa ilişkin sayılar ve eğilimler. Bireysel kullanıcıları, e-posta adreslerini veya IP adreslerini listelemez. Belirli bir kişinin hesabını görüntülemek veya düzenlemek için bunun yerine [Kullanıcılar](README.md) sayfasını kullanın.
