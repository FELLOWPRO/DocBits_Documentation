# Admin Yetkileri

Bir yöneticinin rolü, bir kuruluştaki BT sistemlerini, ağları ve dijital platformları yönetmek için kritik öneme sahiptir. Bir yönetici, teknik altyapının çeşitli yönlerini denetlemesini ve altyapının verimli ve güvenli bir şekilde işletilmesini sağlamasına olanak tanıyan gelişmiş izinlere ve sorumluluklara sahiptir. İşte bir yöneticinin başlıca sorumluluklarından bazıları:

* **Kullanıcı yönetimi:** Yöneticiler kullanıcı hesaplarını, erişim haklarını ve izinleri yönetir. Yeni kullanıcı hesapları oluşturur, bunlara gerekli izinleri atar ve yalnızca yetkili kullanıcıların belirli kaynaklara erişebilmesini sağlamak için erişim denetimini yönetir.
* **Güvenlik:** Yöneticiler, veri kaybına ve yetkisiz erişime karşı korumak amacıyla BT sistemlerinin güvenliğinden sorumludur.
* **Sorun giderme ve destek:** Yönetici, çoğu zaman teknik sorunlar için ilk başvuru noktasıdır. Kullanıcıların sorunları gidermesine ve çözmesine yardımcı olur ve sistemin sorunsuz çalışmasını sağlar.

Bu sorumlulukların yanı sıra yöneticiler, hassas ayarları yönetmek ve sistemlerin uyumluluk gereksinimlerini ve bilgi güvenliği en iyi uygulamalarını karşılamasını sağlamakla da görevlidir. Buna hassas verilerin yönetimi, erişim denetimlerinin ve izinlerin yapılandırılması ve olası güvenlik risklerini belirlemek ve gidermek için sistem günlüklerinin izlenmesi ve analiz edilmesi dahildir.

## Admin vs System Admin

DocBits'in iki yönetici rolü vardır: **Admin** ve **System Admin**. Kulağa benzer gelseler de farklı işler yaparlar. İşte sade hâliyle açıklaması.

### Admin — kuruluşunuzu yöneten kişi

Bir **Admin**, ekibinizde DocBits'i yönetmesine izin verilen gerçek bir kişidir. Admin'ler şunları yapabilir:

* **Ayarlar**'ın tüm bölümlerini açabilir ve kuruluşunuzun çalışma şeklini değiştirebilir.
* Yeni kullanıcılar ekleyebilir, bunları düzenleyebilir, açıp kapatabilir ve başka kimin Admin olacağına karar verebilir.
* Gruplar, izinler, entegrasyonlar ve iş akışları oluşturabilir.

**İhtiyaç duyduğunuz kadar Admin** ekleyebilirsiniz ve istediğiniz zaman herhangi bir kullanıcıya Admin rolünü verebilir veya ondan alabilirsiniz. Ekibinizdeki yöneticilerin çoğu bu türdendir.

### System Admin — DocBits'in kendi başına çalışmak için kullandığı hesap

Bir **System Admin**, DocBits'in **kimse bir düğmeye basmadan otomatik olarak** gerçekleşen işlemler için kullandığı, **her kuruluşta yalnızca bir tane bulunan özel bir hesaptır** — örneğin belgeler e-postadan içe aktarıldığında, başka bir sisteme dışa aktarıldığında veya bağlı bir hizmet tarafından arka planda iletildiğinde.

Bunu kuruluşun "robot" hesabı olarak düşünebilirsiniz. Sistem kendi başına bir şey yaptığında bunu **System Admin olarak** yapar; böylece otomatik etkinlik kolayca tanınabilir ve gerçek ekip üyelerinizin yaptığı işle karışmaz.

Bir System Admin üç açıdan özeldir:

* **Her zaman aynı zamanda bir Admin'dir.** System Admin'i seçmek, o hesaba otomatik olarak tam Admin haklarını da verir.
* **Her kuruluşta yalnızca bir tane bulunur.** Bir System Admin var olduğunda, başka bir kullanıcıyı System Admin olarak işaretleyemezsiniz.
* **Yalnızca kullanıcı oluşturulurken belirlenir.** Buna, kullanıcıyı eklediğiniz anda karar verirsiniz. **Sonradan açılıp kapatılamaz.**

> **Öneri:** Bu amaç için özel bir hesap oluşturun — örneğin `system@your-company.com` — ve bunu System Admin olarak işaretleyin. Böylece DocBits'in otomatik olarak yaptığı her şey, günlüklerinizde ve belge geçmişinizde gerçek kullanıcılarınızdan ayrı olarak açıkça **System Admin** şeklinde görünür.

### Bir bakışta

| | Admin | System Admin |
|---|---|---|
| Kuruluşu yönetmek için tam erişim | Evet | Evet |
| Kaç tane olabileceği | İhtiyaç duyduğunuz kadar | Yalnızca bir |
| Kullanıcı oluşturulduktan sonra değiştirilebilir mi | Evet, istediğiniz zaman | Hayır, yalnızca oluşturma sırasında belirlenir |
| Otomatik, arka plan işlemleri için kullanılır mı | Hayır | Evet |
| Her zaman Admin haklarına sahiptir | — | Evet |

## Güvenlik En İyi Uygulaması

Güvenlik, özellikle kullanıcı hesaplarının ve erişim haklarının yönetimi söz konusu olduğunda, her kuruluş için temel bir unsurdur. Güvenli bir kullanıcı yönetimi protokolünü sürdürmek için bazı en iyi uygulamalar şunlardır:

* **Düzenli parola güncellemeleri:** Hesaplarını güvende tutmak için kullanıcıları parolalarını düzenli olarak güncellemeye teşvik edin. Parola karmaşıklığı politikaları oluşturun ve harf, rakam ve özel karakter kombinasyonu içeren güçlü parolaların kullanılmasını zorunlu kılın.
* **Yönetici işlemlerini izleyin:** Şüpheli veya olağan dışı etkinlikleri tespit etmek için yönetici faaliyetlerini izleyen mekanizmalar kurun. Hesap verebilirliği sağlamak ve olası güvenlik ihlallerini belirlemek için hassas verilere veya ayarlara erişim dahil tüm yönetici işlemlerini kaydedin.
* **Yönetici sayısını sınırlayın:** Yönetici sayısını mümkün olan en aza indirin ve yönetici yetkilerini yalnızca gerçekten ihtiyacı olanlara verin. Yönetici sayısını sınırlayarak güvenlik ihlali riskini en aza indirir ve kullanıcı hesaplarının yönetimini ve izlenmesini kolaylaştırırsınız.
* **İki Faktörlü Kimlik Doğrulama (2FA):** Güvenliği daha da artırmak için yönetici hesapları için iki faktörlü kimlik doğrulama uygulayın. Bu, ek bir güvenlik adımı getirir ve bir parola ele geçirilse bile saldırganın hesaba yetkisiz erişim sağlayamamasını güvence altına alır.
* **Düzenli güvenlik denetimleri:** Olası güvenlik açıklarını veya zayıf noktaları belirlemek ve gidermek için düzenli güvenlik denetimleri ve incelemeleri yapın. Kullanıcı hesaplarının erişim haklarını ve izinlerini gözden geçirerek bunların güncel gereksinimlere ve en iyi uygulamalara uygun olmasını sağlayın.
* **Eğitim ve farkındalık:** Çalışanları ve yöneticileri güvenlik en iyi uygulamaları ile kimlik avı saldırıları ve diğer siber tehditlere yönelik farkındalık konusunda düzenli olarak eğitin. Onları güvenliğin önemi konusunda bilinçlendirin ve şüpheli etkinlikleri bildirmeye teşvik edin.

Bu en iyi uygulamaları hayata geçirerek kuruluşlar, kullanıcı yönetimi protokollerinin güvenliğini artırabilir ve güvenlik ihlalleri ile veri kaybı riskini en aza indirebilir. Güvenliği sürekli bir süreç olarak görmek ve sürekli değişen tehditlere ve güvenlik gereksinimlerine ayak uydurmak için düzenli güncellemeler ve ayarlamalar yapmak önemlidir.
