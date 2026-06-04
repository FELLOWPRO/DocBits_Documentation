# Advanced Workflow

**Advanced Workflow** oluşturucusu, dallanma, paralel yollar ve akış kontrolü gerektiren iş akışları için — Standard oluşturucunun doğrusal When/And/Then yapısının ötesinde — bir düğüm grafiği düzenleyicisidir. Düğümleri bir tuvale yerleştirir ve yürütme akışını tanımlamak için onları birbirine bağlarsınız.

## Nasıl erişilir

Advanced Workflow tasarımcısını iş akışı alanından (gelişmiş oluşturucu tuvali) açın. Bir **Start** düğümünden başlar ve düğümler ekleyerek akışı oluşturursunuz.

<figure><img src="../../.gitbook/assets/workflow_advanced_canvas.png" alt="Araç çubuğuyla Advanced Workflow düğüm grafiği tuvali"><figcaption><p>Advanced Workflow tuvali — yakınlaştırma, çalıştırma, ızgara ve kaydetme kontrolleriyle bir düğüm grafiği. Araç çubuğunda iş akışına bir ad verin.</p></figcaption></figure>

## Düğüm ekleme

Düğüm menüsünü açmak için **+ Add**'e tıklayın. Tanıdık **When**, **And** ve **Then** kartlarına ek olarak, gelişmiş oluşturucu akış kontrolü düğümleri ekler:

<figure><img src="../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Düğüm türleriyle Advanced Workflow Add menüsü"><figcaption><p><strong>+ Add</strong> düğüm menüsü: When / And / Then artı Wait ALL, Wait ANY, OR ve Note.</p></figcaption></figure>

- **When / And / Then** — Standard oluşturucuyla aynı koşul ve eylem kartları.
- **Wait ALL** — devam etmeden önce gelen *tüm* dalların tamamlanmasını bekler.
- **Wait ANY** — gelen *herhangi bir* dal tamamlanır tamamlanmaz devam eder.
- **OR** — akışı alternatif yollara dallandırır.
- **Note** — tuvalde serbest metin bir açıklama (yürütmeyi etkilemez).

Akışı oynat kontrolüyle çalıştırın, doğrulayın ve araç çubuğundaki kaydet düğmesiyle kaydedin.

## Sonraki adımlar

- Her kartın ne yaptığını **Cards** bölümünde görün.
- Basit doğrusal otomasyonlar için **Standard Workflow** oluşturucusunun kurulumu daha hızlıdır.
