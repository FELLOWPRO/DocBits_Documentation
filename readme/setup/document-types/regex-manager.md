# Regex Yöneticisi

DocBits’in bu özelliği, model sınıflandırmasına bir alternatif sunar: bir belge türü için, sınıflandırma ve diğer amaçlarla aranabilir düzenli ifadeler yazmanızı sağlar.

Belge türü: Regex Yöneticisi, daha sonra belgede aranacak düzenli ifadeler yazmanıza olanak tanır. DocBits, tanımlı bir belgenin düzenli ifadesiyle bir eşleşme bulursa belgeyi ilgili belge türüne sınıflandırır. Örneğin “Gutschrift” terimini bulmak için bir düzenli ifade yazarsanız ve DocBits bu terimi bir belgede bulursa, belgeyi alacak dekontu olarak sınıflandırır.

Belge kökeni: DocBits, düzenli ifadeler sayesinde bir belgenin menşe ülkesini de tanır. Örneğin İspanyolca bir belge için yazılan düzenli ifade “Factura” terimini içeriyorsa ve DocBits bu terimi belgede bulursa, belgenin İspanya kökenli olduğunu anlar ve buna göre sınıflandırır.

## **Regex Yöneticisine erişim**

DocBits’te Ayarlar → Belge Türleri bölümüne gidin. “Özel Belge Türleri” altında “Yeni”ye tıklayın. Belge türü için bir ad girin, isteğe bağlı bir açıklama ekleyin ve belge bir tablo içeriyorsa “Tablo mevcut” kutusunu işaretleyin. Ardından “Otomatik” yerine “Düzenli ifade” seçeneğini seçin ve “Sonraki”ye tıklayın.

<figure><img src="../../.gitbook/assets/regex-manager-create-tr-20261006.png" alt="Ad alanı, tablo mevcut kutusu, açıklama ile Otomatik ve Düzenli ifade düğmelerini içeren yeni belge türü oluşturma sayfası"><figcaption><p>Yeni belge türünü düzenli ifadelerle sınıflandırmak için “Düzenli ifade” seçeneğini seçin.</p></figcaption></figure>

## **Regex ekleme ve kaldırma**

“Düzenli ifade” adımı, mevcut regex modellerini kökenleri ve modelleriyle birlikte listeler ve yeni bir regex modeli oluşturmak için “Eklemek” düğmesini sunar. İlgili girişi yönetmek için satır sonundaki işlem menüsünü kullanın. “Alanlar ve gruplar” adımına geçmek için “Sonraki”ye tıklayın.

<figure><img src="../../.gitbook/assets/regex-manager-list-tr-20261006.png" alt="Eklemek düğmesi ile kökeni, modeli ve işlemleri olan üç regex modelinin tablosunu gösteren Düzenli ifade adımı"><figcaption><p>Kökeni ve modeliyle mevcut regex modelleri. “Eklemek” yeni bir model oluşturur.</p></figcaption></figure>
