# Kullanıcılar

<figure><img src="../../../../../.gitbook/assets/users_settings.png" alt="Kullanıcı Yönetimi"><figcaption><p>Kullanıcı Yönetimi Sayfası</p></figcaption></figure>

Kullanıcılar sayfası, yöneticilerin DocBits kuruluşunuzdaki tüm kullanıcı hesaplarını yönetmesini sağlar. Buradan yeni kullanıcılar ekleyebilir, roller atayabilir ve erişimi denetleyebilirsiniz.

## Kullanıcı Listesi

Kullanıcı tablosunda aşağıdaki sütunlar görüntülenir:

| Sütun | Açıklama |
|--------|-------------|
| **Ad** | Kullanıcının tam adı. |
| **E-Posta** | Kullanıcının e-posta adresi; giriş kimliği olarak kullanılır. |
| **Son Giriş** | Kullanıcının en son giriş yaptığı tarih ve saat. |
| **Admin** | Kullanıcının yönetici yetkilerine sahip olup olmadığını gösteren onay kutusu. Admin'ler tüm ayarlara erişebilir ve diğer kullanıcıları yönetebilir. |
| **System Admin** | Kuruluşun tek System Admin hesabını gösteren onay kutusu — bu, DocBits'in otomatik, arka planda gerçekleşen işlemler (örneğin otomatik içe ve dışa aktarmalar) için kullandığı hesaptır. Bir System Admin her zaman Admin yetkilerine de sahiptir. Admin ile System Admin arasındaki fark için bkz. [Admin Yetkileri](admin-privileges.md#admin-vs-system-admin). |
| **Aktif** | Kullanıcı hesabının şu anda etkin olup olmadığını gösteren onay kutusu. Etkin olmayan kullanıcılar giriş yapamaz. |
| **İşlemler** | Kullanıcı bilgilerini düzenleme, parolaları sıfırlama veya hesabı devre dışı bırakma gibi seçenekler içeren menü. |

Kullanıcıları ada veya kimliğe göre hızlıca bulmak için üstteki **Arama** çubuğunu kullanın.

## Giriş Analitiği

Kuruluşunuz genelinde giriş etkinliği verilerini (giriş sıklığı ve örüntüleri dahil) görüntülemek için **Giriş Analitiği**'ne tıklayın.

## Yeni Bir Kullanıcı Ekleme

1. Sağ üst köşedeki **Kullanıcı Ekle** düğmesine tıklayın.
2. Gerekli bilgileri doldurun:
   * **Kullanıcı Adı**: Kullanıcı için benzersiz bir ad.
   * **Ad** ve **Soyad**: Kullanıcının tam adı.
   * **E-Posta Adresi**: Giriş ve bildirimler için kullanılır.
   * **Parola**: Kuruluşunuzun güvenlik politikalarına uygun olmalıdır.
   * **Kullanıcı Rolü**: Uygun rolü atayın (Standard User, Admin veya System Admin).
3. Kullanıcı hesabını oluşturmak için **Kaydet**'e tıklayın. Yeni kullanıcı, giriş bilgilerini içeren bir e-posta bildirimi alacaktır.

> **Not:** **System Admin** rolü yalnızca bir kullanıcı oluşturulurken seçilebilir — sonradan eklenemez veya kaldırılamaz. Her kuruluşta yalnızca bir System Admin bulunabilir ve bu rolün seçilmesi otomatik olarak Admin haklarını da verir. Ne zaman kullanılacağını öğrenmek için bkz. [Admin Yetkileri](admin-privileges.md#admin-vs-system-admin).
