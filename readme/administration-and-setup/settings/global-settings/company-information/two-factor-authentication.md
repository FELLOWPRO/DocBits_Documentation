# İki Faktörlü Kimlik Doğrulama (Yönetici)

## Genel Bakış

Bir kuruluş yöneticisi olarak, üyeler parolayla oturum açtığında **her üyenin iki faktörlü kimlik doğrulama (2FA) kullanmasını zorunlu kılabilirsiniz**. Zorunluluk açık olduğunda, henüz ikinci bir faktör kurmamış bir üye, oturum açmayı tamamlayabilmeden önce kayıt sürecinde yönlendirilir.

Tek oturum açma (SSO) girişleri — Google, Microsoft, SAML — **muaftır**: kimlik sağlayıcıları kendi MFA'sını zaten uygular, bu nedenle zorunluluk yalnızca parola girişlerini etkiler.

Bu ayar **Ayarlar → Genel Ayarlar → Şirket Bilgileri → İki faktörlü kimlik doğrulama** altında bulunur ve yalnızca kuruluş yöneticileri tarafından kullanılabilir.

## Kuruluşunuz için MFA'yı zorunlu kılma

1. **Ayarlar → Genel Ayarlar → Şirket Bilgileri**ne gidin.
2. **İki faktörlü kimlik doğrulama** bölümünü açın.
3. **Tüm üyeler için iki faktörlü kimlik doğrulamayı zorunlu kıl**ı açın ve **Kaydet**e tıklayın.

<figure><img src="../../../../.gitbook/assets/mfa-admin-requirement.png" alt="The organisation MFA requirement toggle and adoption report"><figcaption><p>Tüm üyeler için zorunluluğu açın ve benimsenmeyi aşağıda izleyin.</p></figcaption></figure>

Kaydedildikten sonra değişiklik bir dakika içinde geçerli olur. Bu andan itibaren:

* İkinci faktörü **olan** bir üyeden, her zamanki gibi parolasından sonra bu faktör istenir.
* İkinci faktörü **olmayan** bir üyenin, bir oturum almadan önce bir faktör kaydetmesi gerekir.
* SSO / sosyal girişler etkilenmez.

{% hint style="warning" %}
Bunu açmak, ikinci faktörü olmayan üyeler için kaydı tamamlayana kadar parola girişlerini engeller. Değişikliği ekibinize duyurun ve yoğun saatler dışında etkinleştirmeyi düşünün.
{% endhint %}

## MFA benimseme raporu

Geçiş düğmesinin altında, **MFA benimseme** paneli, zorunlu kılmadan önce kuruluşunuzda 2FA'nın ne kadar yaygın kullanıldığını gösterir:

* genel **benimseme yüzdesi** ve bir ilerleme çubuğu,
* üyelerinizden kaçının 2FA'yı etkinleştirdiği (ör. *74 üyeden 0'ı*),
* faktör bazında bir dağılım — **Kimlik doğrulayıcı**, **E-posta** ve **Passkey**.

<figure><img src="../../../../.gitbook/assets/mfa-adoption-report.png" alt="The MFA adoption report"><figcaption><p>MFA benimseme raporu: genel yüzde, kayıtlı üyeler ve faktör bazında bir dağılım.</p></figcaption></figure>

Hazır olma durumunu ölçmek için bunu kullanın: önce benimsemeyi artırın, ardından kayıt adımında daha az üye engellenecek şekilde zorunluluğu açın.

## Üyelerin gördükleri

Kayıt olması gereken bir üye, bir sonraki girişinde 2FA kurulumuna yönlendirilir ve bir yöntem seçer (kimlik doğrulayıcı uygulaması, e-posta kodu veya passkey). Son kullanıcı adımları [İki Faktörlü Kimlik Doğrulama (2FA)](../../../../overview-and-basics/two-factor-authentication.md) sayfasında ele alınmıştır.

## İlgili güvenlik kontrolleri

Kuruluş genelindeki MFA zorunluluğu, bir kullanıcı 2FA'yı açtığında her zaman geçerli olan yerleşik korumaları tamamlar: tek kullanımlık oturum açma kodları, bir TOTP yeniden oynatma koruması, doğrulama başına ve hesap başına deneme sınırları (çok fazla başarısız denemeden sonra bir hesap geçici olarak kilitlenir) ve bir üye parolasını değiştirdiğinde güvenilir cihazların otomatik olarak iptal edilmesi.
