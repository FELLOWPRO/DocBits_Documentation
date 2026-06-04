# Date or Time

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu DocBits kartı, belirtilen bir tarih/saat değerinin tanımlanmış bir aralık içine düşüp düşmediğini kontrol eder. Koşulun karşılanıp karşılanmadığına bağlı olarak iş akışlarının devam etmesini veya durmasını sağlar, bu da onu zamana duyarlı işlemler veya iş akışlarını zamanlama için uygun kılar.

## **İşlevsellik:**

* **Tarih/Saat Doğrulaması:** Bu kart, aşağıdaki koşulları kullanarak belirli bir tarih/saatin belirtilen bir aralık içinde olup olmadığını değerlendirir:
  * **Is:** Tarih/saatin tanımlanan başlangıç ve bitiş aralığı içinde (dahil) olup olmadığını kontrol eder.
  * **Is Not:** Tarih/saatin tanımlanan aralığın dışına düştüğünü garanti eder.

**Tarih/Saat Aralığı:** Kullanıcılar, karşılaştırma için aralığı tanımlamak üzere başlangıç ve bitiş tarih/saat değerlerini belirtir.

## **Kullanım:**

Bu kart, iş akışlarında zamanlama, uyumluluk kontrolleri veya zaman tabanlı koşulları doğrulamak için idealdir. Örneğin, görevlerin yalnızca önceden tanımlanmış zaman dilimlerinde yürütülmesini sağlamak veya son teslim tarihlerini doğrulamak için kullanılabilir.

## **Örnek Senaryo:**

* Bir kullanıcı, bir faturanın **gönderim tarihinin** **"2024-11-01"** ile **"2024-11-30"** arasında **olup olmadığını** kontrol etmek için kartı yapılandırır. Gönderim tarihi bu aralığa düşerse, iş akışı ödeme işlemesine ilerler. Düşmezse, iş akışı daha fazla inceleme için bir bildirim tetikler.

"Tarih/Saat Aralığı Doğrulaması" kartını kullanarak kuruluşlar, doğru zamanlama sağlayabilir, uyumluluğu artırabilir ve önceden tanımlanmış zaman kısıtlamalarına uyarak iş akışlarını kolaylaştırabilir.
