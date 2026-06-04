# Run Workflow

<figure><img src="../../../../.gitbook/assets/image (307).png" alt="" width="563"><figcaption></figcaption></figure>

## Amaç:

**"Run Workflow"** kartı, kullanıcıların kullanılabilir iş akışları listesinden seçilen bir iş akışını dinamik olarak yürütmesine olanak tanır. Bu kart, birden fazla iş akışının birbirine bağlı olduğu süreçleri otomatikleştirmek için yararlıdır ve kolaylaştırılmış operasyonları mümkün kılar.

## Kartın Bileşenleri:

1. **İş Akışı (Workflow)**
   * **Açıklama:** Koşullar doğru olarak değerlendirildiğinde yürütülecek iş akışını belirtir.
   * **Ayrıntı:** Seçim için tüm kullanılabilir iş akışlarının bir açılır listesi sağlanır.

## İşlevsellik:

* **Koşul Değerlendirmesi:** Kart, seçilen iş akışını yalnızca hem **"Where"** hem de **"And Bölümleri"** doğru olarak değerlendirilirse yürütür.
  * Koşullardan biri yanlışsa, hiçbir eylem gerçekleştirilmez ve iş akışı tetiklenmemiş olarak kalır.
* **İş Akışı Yürütme:**
  * Koşullar karşılandığında, belirtilen iş akışı otomatik olarak tetiklenir.
  * Koşullar karşılanmazsa, hiçbir iş akışı yürütülmez.

## Kurulum ve Yapılandırma:

1. **İş Akışını Seç:** Tetiklenecek iş akışını kullanılabilir iş akışlarının **açılır listesinden** seçin.
2. **Koşulları Tanımla:** İş akışının yürütülmesi için karşılanması gereken ölçütleri belirtmek üzere **"Where"** ve **"And Bölümleri"**ni yapılandırın.

## Sonuç:

**"Run Workflow"** kartı, iş akışlarını bağlamak ve çok adımlı süreçleri kolaylıkla otomatikleştirmek için kullanışlı ve verimli bir yol sunar. **"Where"** ve **"And Bölümleri"**ndeki koşulların karşılanmasını sağlayarak, kullanıcılar iş akışlarını dinamik olarak yürütebilir ve manuel müdahaleyi azaltabilir.
