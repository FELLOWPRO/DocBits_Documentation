# Belge Türleri

{% embed url="https://youtu.be/pFz_6tvNlU4" %}
DocBits Admin Guide: Adding, Editing & Configuring Document Types (Full Walkthrough)
{% endembed %}

<figure><img src="../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 08.44.19.png" alt=""><figcaption></figcaption></figure>

#### Genel Bakış

Belge Türleri bölümü, Docbits tarafından tanınan ve işlenen tüm belge türlerini listeler. Yöneticiler, her belge türü için düzen, alan tanımları, çıkarma kuralları ve daha fazlasını yönetebilir. Bu özelleştirme, doğru veri işleme ve kurumsal standartlara uyumluluğun sağlanmasında önemlidir.

#### Temel Özellikler ve Seçenekler

1. **Belge Türü Listesi**:
* Her satır, Fatura, Kredi Notu, Teslimat Bildirimi vb. gibi bir belge türünü temsil eder.
* Belge türleri, "Standart" gibi etiketlerle belirtilen şekilde standart veya özel olabilir.
2. **Düzeni Düzenle**: Bu seçenek, yöneticilerin belge düzeni ayarlarını değiştirmesine olanak tanır; bu ayarlar belgenin nasıl göründüğünü ve veri alanlarının nerede bulunduğunu tanımlar.
3. **Belge Alt Türleri**: Eğer belge türlerinin alt kategorileri varsa, bu seçenek yöneticilerin her alt tür için özgü ayarları yapılandırmasına olanak tanır.
4. **Tablo sütunları**: Belge türü listelerinde veya raporlarda belge türü görüntülendiğinde hangi veri sütunlarının görünmesini özelleştirin.
5. **Alanlar**: Belge türü ile ilişkilendirilen veri alanlarını yönetin, yeni alanlar ekleyin veya mevcut olanları değiştirin.
6. **Model Eğitimi**: Belgelerden veri tanımlamak ve çıkarmak için kullanılan modeli yapılandırın ve eğitin. Bu, zamanla daha fazla veri ile gelişen makine öğrenimi modelleri için parametreler belirlemeyi içerebilir.
7. **Regex**: Belgelerden veri çıkarmak için kullanılan desenlere dayalı olarak düzenli ifadeleri ayarlayın. Bu, yapılandırılmış veri çıkarma için özellikle yararlıdır.
8. **Komut Dosyaları**: Bu tür belgeler için özel işleme kuralları veya iş akışları çalıştıran komut dosyalarını yazın veya değiştirin.
9. **EDI (Elektronik Veri Değişimi)**: Standartlaştırılmış elektronik formatlarda belgelerin değişimine ilişkin ayarları yapılandırın.

#### Özel Doğrulama Kuralları

Bir belge türünü açın, **Özel Doğrulama Kuralları** işlevini etkinleştirin ve bu türün doğrulama kurallarını yönetmek için **Doğrulama Kurallarını Yönetin** bağlantısını seçin (işlevin belge türünde etkin olması gerekir). Var olan bir kuralı baştan oluşturmadan yeniden kullanmak için [Özel Doğrulama Kuralını Çoğaltma](../../../administration-and-setup/settings/global-settings/document-types/duplicate-a-custom-validation-rule.md) rehberine bakın. Rehber kural adı, kural anahtarı ve onay düğmelerini açıklar.

{% hint style="info" %}
[Belge Türü Kurulumu'na](../../../setup/document-types/) bakın.
{% endhint %}

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2489" %}
