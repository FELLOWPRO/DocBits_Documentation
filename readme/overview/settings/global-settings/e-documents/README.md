# Elektronik Belgeler

DocBits, gelen elektronik faturaları (e-faturalar) resmi standartlara — **XRechnung**, **ZUGFeRD** ve **Factur-X** — göre doğrular ve bulduğu sorunları doğru işleyiciye yönlendirir. **Elektronik Belgeler** ayar grubu (**Belge İşleme** altında) iki sayfa içerir:

* **[Doğrulama Kuralları](validation-rules.md)** — hangi e-fatura sürümlerini ve profillerini kabul ettiğinizi seçin ve her doğrulama kuralının önem derecesini kuruluşunuz için ayarlayın.
* **[Bildirim Yönlendirme](notification-routing.md)** — doğrulama bulgularını bunları işlemesi gereken AI Workforce aracısıyla eşleştirin.

Birlikte, gelen bir e-faturada **neyin sorun sayılacağına** ve **kimin ilgileneceğine** karar vermenizi sağlar.

## E-fatura doğrulamasını etkinleştirme veya devre dışı bırakma

İki Elektronik Belgeler sayfası yalnızca **e-fatura doğrulaması belge türü için açıldığında** etkili olur. Anahtar, Elektronik Belgeler menüsünde değil, belge türünün kendisinde bulunur.

**Ayarlar → Belge Türleri → Fatura → Gelişmiş Ayarlar** bölümüne gidin ve **E-Fatura Doğrulama** bölümünü açın.

<figure><img src="../../../../.gitbook/assets/edoc_enable_validation_toggle.png" alt="Fatura belge türündeki e-fatura doğrulama anahtarları"><figcaption><p>E-fatura doğrulamasını belge türüne göre açın veya kapatın, isteğe bağlı tedarikçi bildirimi ile</p></figcaption></figure>

* **Gelen e-faturaları doğrula** — ana anahtar. **Açık** olduğunda, yüklenen her fatura KoSIT XRechnung Schematron kurallarına ek olarak L0 (PDF/A-3) ve L4 (IBAN/KDV) anlamsal kontrollerine göre denetlenir; [Doğrulama Kuralları](validation-rules.md) sayfasında belirlediğiniz önem dereceleri kullanılır. Geçersiz faturalar engellenir. **Kapalı** olduğunda, faturalar e-fatura doğrulamasını tamamen atlar ve Doğrulama Kuralları ile Bildirim Yönlendirme sayfalarının hiçbir etkisi olmaz.
* **Reddedildiğinde tedarikçiye bildir** — doğrulama etkinleştirildiğinde görünür. **Açık** olduğunda, reddedilen bir fatura, tedarikçinin faturayı yeniden düzenleyebilmesi için eksik veya hatalı alanları listeleyen bir e-posta gönderir. Her bulguyu kimin alıp işleyeceği [Bildirim Yönlendirme](notification-routing.md) sayfasında yapılandırılır.

> E-fatura doğrulaması **belge türüne göre** yapılandırılır. Şu anda **Fatura** belge türü için geçerlidir; doğrulanması gereken her belge türü için etkinleştirin.
