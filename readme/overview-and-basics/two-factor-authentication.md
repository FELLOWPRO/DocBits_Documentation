# İki Faktörlü Kimlik Doğrulama (2FA)

## Genel Bakış

İki Faktörlü Kimlik Doğrulama (2FA), oturum açma işleminize ikinci bir adım ekler. Parolanızdan sonra DocBits, yalnızca sizde bulunan ikinci bir faktör ister — bir kimlik doğrulayıcı uygulamasından gelen bir kod, size e-postayla gönderilen bir kod veya bir passkey (Touch ID, Windows Hello, YubiKey, 1Password). Birisi parolanızı öğrense bile, bu ikinci faktör olmadan oturum açamaz.

2FA **her kullanıcı için isteğe bağlıdır** ve **kuruluşunuzun yöneticisi tarafından zorunlu kılınabilir**. Tek oturum açma (SSO) girişleri (Google, Microsoft, SAML) muaftır — kimlik sağlayıcınız kendi MFA'sını zaten uygular.

Birden fazla yöntem kaydedebilirsiniz. DocBits'in desteklediği yöntemler şunlardır:

* **Kimlik doğrulayıcı uygulaması (TOTP)** — Google Authenticator, Microsoft Authenticator, 1Password, Authy vb.
* **E-posta kodu** — hesap e-postanıza gönderilen 6 haneli bir kod.
* **Passkey (WebAuthn/FIDO2)** — Touch ID, Windows Hello, bir donanım anahtarı (YubiKey) veya bir parola yöneticisi.

İlk faktörünüzü açtığınızda, DocBits ayrıca yönteminize erişiminizi kaybetmeniz durumunda kullanabileceğiniz **on yedek kod** verir.

## Nerede bulunur

**Profil / hesap ayarlarınızı** açın (sağ üstteki hesap menüsü → **Profili düzenle**) ve **İki faktörlü kimlik doğrulama**yı seçin. 2FA iletişim kutusu, mevcut durumunuzu ve ekleyebileceğiniz yöntemleri gösterir.

<figure><img src="../.gitbook/assets/mfa-2fa-dialog.png" alt="The Two-factor authentication dialog"><figcaption><p>İki faktörlü kimlik doğrulama iletişim kutusu. Buradan bir kimlik doğrulayıcı uygulamasını, e-posta doğrulamasını etkinleştirebilir, bir passkey ekleyebilir veya <strong>Yönet</strong>'i açabilirsiniz.</p></figcaption></figure>

## Bir kimlik doğrulayıcı uygulaması (TOTP) kurma

1. 2FA iletişim kutusunda **2FA'yı etkinleştir**e tıklayın.
2. QR kodunu kimlik doğrulayıcı uygulamanızla (Google Authenticator, 1Password, Authy, …) tarayın. Tarayamıyorsanız, QR kodunun altında gösterilen **manuel anahtarı** kullanın.
3. Uygulamanızın gösterdiği 6 haneli kodu girin ve onaylayın.
4. DocBits 2FA'yı etkinleştirir ve **yedek kodlarınızı** gösterir (aşağıya bakın).

<figure><img src="../.gitbook/assets/mfa-totp-setup.png" alt="The authenticator-app setup screen with QR code"><figcaption><p>QR kodunu kimlik doğrulayıcı uygulamanızla tarayın veya manuel anahtarı girin. Ardından uygulamanın gösterdiği 6 haneli kodla onaylayın.</p></figcaption></figure>

## E-posta doğrulaması kurma

1. 2FA iletişim kutusunda **E-posta doğrulamasını etkinleştir**e tıklayın.
2. DocBits, hesap adresinize 6 haneli bir kod gönderir.
3. Onaylamak için kodu girin. E-posta doğrulaması artık açık.

## Passkey ekleme

1. 2FA iletişim kutusunda **Passkey ekle**ye tıklayın.
2. Tarayıcınız veya cihazınız, Touch ID, Windows Hello, bir donanım anahtarı veya parola yöneticinizle onaylamanızı ister.
3. Passkey kaydedilir. Birden fazla passkey ekleyebilir ve bunları daha sonra yeniden adlandırabilir veya kaldırabilirsiniz.

## Yedek kodlar

**İlk** faktörünüzü etkinleştirdiğinizde, DocBits **on yedek kodu** — **bir kez** — gösterir. Her kod yalnızca bir kez çalışır ve kimlik doğrulayıcınızı veya telefonunuzu kaybetmeniz durumunda oturum açmanıza olanak tanır.

* Bunları güvenli bir yere kaydedin (bir parola yöneticisi idealdir).
* **Yedek kodları yeniden oluştur** ile istediğiniz zaman yeni bir set oluşturabilirsiniz (bu, eski seti geçersiz kılar).

<figure><img src="../.gitbook/assets/mfa-backup-codes.png" alt="The backup codes screen"><figcaption><p>On yedek kodunuz, bir kez gösterilir. Her biri yalnızca bir kez çalışır — bunları güvenli bir yere saklayın.</p></figcaption></figure>

{% hint style="warning" %}
Yedek kodlar yalnızca oluşturuldukları anda gösterilir. DocBits bunları tekrar gösteremez — hemen saklayın.
{% endhint %}

## 2FA ile oturum açma

1. E-postanızı ve parolanızı her zamanki gibi girin.

    <figure><img src="../.gitbook/assets/mfa-login.png" alt="The DocBits login screen"><figcaption><p>Oturum açma ekranı. <strong>Passkey ile oturum aç</strong>'ı kullanarak parola olmadan da oturum açabilirsiniz.</p></figcaption></figure>
2. DocBits ikinci faktörünüzü ister. Yönteminizi seçin:
   * **Kimlik doğrulayıcı** — uygulamanızdaki geçerli 6 haneli kodu yazın.
   * **E-posta** — e-postayla bir kod almak için **Bana e-postayla kod gönder**e tıklayın, ardından yazın.
   * **Passkey** — **Passkey kullan**a tıklayın ve Touch ID / Windows Hello / anahtarınızla onaylayın.
   * **Yedek kod** — her zamanki yönteminizi kullanamıyorsanız.

    <figure><img src="../.gitbook/assets/mfa-challenge.png" alt="The second-factor challenge screen"><figcaption><p>Parolanızdan sonra DocBits ikinci faktörünüzü ister. <strong>Passkey kullan</strong> veya <strong>Bana e-postayla kod gönder</strong> ile yöntemi değiştirin ve isteğe bağlı olarak cihaza 30 gün boyunca güvenin.</p></figcaption></figure>
3. Başarılı olduğunuzda oturumunuz açılır.

### E-posta kodu nasıl görünür

**E-posta**yı seçerseniz, DocBits 10 dakika içinde sona eren 6 haneli bir kod içeren bir mesaj gönderir:

<figure><img src="../.gitbook/assets/mfa-email-otp.png" alt="The DocBits verification-code email"><figcaption><p>Doğrulama kodu e-postası. Kod 10 dakika sonra sona erer ve bir kez kullanılabilir.</p></figcaption></figure>

## Bu cihaza güven

İkinci faktör ekranında **Bu cihazı hatırla**yı işaretleyebilirsiniz. DocBits ardından o cihazda 2FA adımını **30 gün** boyunca atlar. Parolanızı değiştirdiğinizde güven otomatik olarak kaldırılır ve istediğiniz zaman kendiniz de iptal edebilirsiniz (aşağıya bakın).

## Passkey'lerinizi ve güvenilir cihazlarınızı yönetme

Nelerin kayıtlı olduğunu gözden geçirmek için 2FA iletişim kutusunu açın ve **Yönet**e tıklayın.

* **Passkey'ler** — bir passkey'i yeniden adlandırın (adına tıklayın) veya silin. Kalan son faktörünüzü silmek 2FA'yı kapatır.
* **Güvenilir cihazlar** — tek bir cihazı iptal edin veya her yerde yeni bir 2FA istemini zorlamak için **Tüm cihazları iptal et**e tıklayın.

<figure><img src="../.gitbook/assets/mfa-passkeys-list.png" alt="Managing enrolled passkeys and trusted devices"><figcaption><p>Yönet görünümü, kayıtlı passkey'lerinizi ve güvenilir cihazlarınızı listeler; burada bunları yeniden adlandırabilir veya kaldırabilirsiniz.</p></figcaption></figure>

## 2FA'yı kapatma

2FA iletişim kutusunda **2FA'yı devre dışı bırak**a tıklayın ve geçerli bir kimlik doğrulayıcı kodu veya bir yedek kod ile onaylayın. 2FA'yı kapatmak ayrıca yedek kodlarınızı temizler ve güvenilir cihazlarınızı iptal eder.

{% hint style="info" %}
Kuruluşunuz MFA'yı **zorunlu** kılıyorsa, en az bir faktör kurulana kadar parolayla oturum açamazsınız. MFA'nın kuruluşunuz için zorunlu olup olmadığından emin değilseniz yöneticinize sorun.
{% endhint %}

## Parolasız oturum açma (isteğe bağlı)

Bir passkey'iniz olduğunda, oturum açma ekranında **Passkey ile oturum aç**'ı kullanarak **parolanızı yazmadan** oturum açabilirsiniz. Parolanız yedek olarak çalışmaya devam eder. Parolasız oturum açma, sizi doğrulaması için passkey gerektirir (Touch ID / Windows Hello / PIN), bu nedenle hem daha hızlı hem de kimlik avına dayanıklıdır.
