# Bildirim Yönlendirme

<figure><img src="../../../../.gitbook/assets/edoc_notification_routing.png" alt="Bildirim yönlendirmeleri"><figcaption><p>Doğrulama bulgularını aracılarla eşleştirme</p></figcaption></figure>

**Bildirim Yönlendirme** sayfası (**Elektronik Belgeler → Eylemler**), doğrulama bulgularını **AI Workforce aracılarıyla** eşleştirir. Engelleyen her bulgu tam olarak bir aracıyı tetikler — kod öneki en uzun eşleşeni. Eşleşmeyen her şey, varsayılan tedarikçi bildirimi aracısına geri döner.

## Bildirim Yönlendirmeleri

Her fatura sorunu türüyle kimin ilgileneceğini seçin. Listelenmeyen her şey varsayılan aracıya gider:

| Yönlendirme | Kapsadığı bulgular |
|-------------|--------------------|
| **Kolombiya iş kuralları** | Kolombiya'ya özgü iş kuralı bulguları. |
| **Almanya iş kuralları** | Almanya'ya özgü iş kuralı bulguları. |
| **IBAN / banka hesabı kontrolleri** | Ödeme verisi bulguları (IBAN sağlama toplamı, uzunluk, ülke). |
| **Vergi kimlik no. kontrolleri** | Vergi kimlik numarası biçimi bulguları. |
| **Diğer her şey** | Yukarıda eşleşmeyen her şey için varsayılan yedek. |

Her yönlendirme için işleyen aracıyı açılır menüden seçin. **Gelişmiş (özel kod kuralları)**, daha ince denetime ihtiyaç duyduğunuzda tam bir bulgu koduna göre yönlendirme yapmanıza olanak tanır.

## Kullanılabilir Aracılar

<figure><img src="../../../../.gitbook/assets/edoc_notification_agents.png" alt="Kullanılabilir aracılar kaydı"><figcaption><p>AI Workforce aracılarının salt okunur kaydı</p></figcaption></figure>

**Kullanılabilir Aracılar** bölümü, dağıtımınızla birlikte gelen AI Workforce aracılarının salt okunur bir kaydıdır, örneğin:

| Aracı | Amaç |
|-------|------|
| **Varsayılan tedarikçi bildirimi** | Genel tedarikçi bildirimi e-postası; daha özel bir aracı eşleşmediğinde devreye giren genel aracı. |
| **Banking Bot** | Ödeme verisi bulguları için özelleştirilmiş şablon (IBAN/BIC düzeltmeleri). |
| **Tax Bot** | Vergi kimlik numarasına özel tedarikçi bildirimi. |
| **Compliance Bot** | Uyumluluk bulgularını işler. |

Her aracı, kendi Celery görevini ve varsayılan olarak işlediği bulgu kodu öneklerini gösterir.
