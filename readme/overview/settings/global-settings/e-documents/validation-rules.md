# Doğrulama Kuralları

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_setup.png" alt="Doğrulama kurulumu ve kabul edilen sürümler"><figcaption><p>Doğrulama kurulumu ve kabul edilen XRechnung sürümleri</p></figcaption></figure>

**Doğrulama Kuralları** sayfası (**Elektronik Belgeler → Kurallar**), DocBits'in gelen e-faturaları nasıl doğruladığını denetler. Resmi **KoSIT XRechnung + ZUGFeRD** kural setine ve doğrulayıcının kurum içi bulgu kodlarına dayanır ve her kuralın önem derecesini kuruluşunuz için geçersiz kılmanıza olanak tanır.

## Doğrulama Kurulumu

**Doğrulama Kurulumu** kartı, mevcut doğrulama profilinizi gösterir (örneğin *B2G — Public Sector Receiver*). Kurulum sihirbazını yeniden çalıştırmak ve doğruladığınız standardı değiştirmek için **Yanıtları düzenle** öğesine tıklayın.

## Kabul edilen XRechnung sürümleri

**Kabul edilen XRechnung sürümleri** geçidi her XRechnung sürümünü listeler. Kabul ettiğiniz sürümleri işaretleyin — CustomizationID'si bu listenin dışında kalan belgeler, diğer herhangi bir kontrolden önce `VAL-VERSION-NOT-ALLOWED` ile reddedilir. Boş liste "her şeyi kabul et" anlamına gelir. Her sürüm, yayın tarihiyle birlikte **current**, **deprecated** veya **EOL** olarak etiketlenir.

## Kabul edilen profiller ve önem derecesi modeli

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_severity.png" alt="Kabul edilen profiller ve önem derecesi açıklaması"><figcaption><p>Kabul edilen profiller ve her önem derecesinin anlamı</p></figcaption></figure>

**Tümünü kabul et** / **Temizle** ve ardından **Kaydet** ile hangi **profilleri** kabul edeceğinizi seçin (BASIC WL, BASIC, EN 16931 / COMFORT, EXTENDED, XRECHNUNG (CIUS)).

Her doğrulama kuralının, tetiklendiğinde ne olacağını belirleyen bir **önem derecesi** vardır:

| Önem derecesi | Etki |
|---------------|------|
| **FATAL** | İşlemeyi hemen durdurur. Sonraki hiçbir katman kontrol edilmez; belge Hata durumuna geçer. |
| **ERROR** | Belge reddedilir. Aynı belgedeki diğer bulgular yine de gösterilir; tedarikçi bildirimi (etkinse) tetiklenir. |
| **WARNING** | Doğrulama raporunda görünür, ancak belge ardışık düzende normal şekilde ilerler. |
| **INFO** | Yalnızca denetim günlüğü. Kullanıcıya yönelik etki ve reddetme yoktur. |

## Kural önem derecelerini geçersiz kılma

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_table.png" alt="Doğrulama kuralı tablosu"><figcaption><p>Kural başına önem derecesi geçersiz kılmalı tam kural tablosu</p></figcaption></figure>

Kural tablosu her doğrulama kuralını listeler (toplam 1.600'den fazla). **Katman (Layer)**, **Profil** veya **Sürüm** ölçütüne göre filtreleyin ya da kod veya alana göre arayın. Her kural için **Önem derecesini** açılır menüden kuruluşunuzun politikasına uyacak şekilde geçersiz kılabilirsiniz — örneğin bir kuralı `ERROR`'dan `WARNING`'e düşürerek belgeyi artık reddetmemesini sağlayabilirsiniz.
