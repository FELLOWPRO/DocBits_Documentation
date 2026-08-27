# Any / All Charges

<figure><img src="../../../../.gitbook/assets/workflow_cards_and_po_compare_any_all_charges.png" alt="Kart kütüphanesindeki kart, sürüm 2 ve sürüm 3"><figcaption><p>Kart kütüphanesindeki kart. Üstte sürüm 2, altta sürüm 3.</p></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, bir belgedeki ek ücretleri, eşleştirilen satın alma siparişindeki ek ücretlerle, tanımlı bir tolerans dahilinde karşılaştırır. Tek bir soruyu yanıtlar: belge ile satın alma siparişi ek maliyetlerde uyuşuyor mu? Satın alma siparişi eşleştirmesinin eşlediği her ücret karşılaştırılır, bu nedenle kartta herhangi bir alan adı belirtmek gerekmez.

Bu kart, tek bir belge alanını Charge ID ile belirlenen tek bir ücretle karşılaştıran **Compare Total Charges** kartından farklıdır. Belgedeki tüm eşleşmiş ücretlerin bir kerede denetlenmesi gerektiğinde bu kartı kullanın.

Satın alma siparişi eşleştirmesi bu karttan önce çalışmalıdır. Belgenin eşleştirilmiş bir satın alma siparişi yoksa kart iş akışını durdurur ve eksik veri bildirir.

## **Kartın Bileşenleri:**

1. **Herhangi biri/Hepsi:**
   * **Açıklama**: Tek tek ücret karşılaştırmalarının kartın tek sonucunda nasıl birleştirildiği.
   * **Seçenekler**:
     * **Herhangi**: en az bir ücretin karşılaştırmayı sağlaması gerekir.
     * **Tüm**: her ücretin karşılaştırmayı sağlaması gerekir.
2. **Operatör:**
   * **Açıklama**: Belgedeki ücret tutarının, aynı ücret için satın alma siparişi tutarıyla nasıl karşılaştırıldığı.
   * **Seçenekler**:
     * **içinde**: iki tutarın, tolerans payı tanınarak uyuşması gerekir.
     * **Dıştan**: iki tutarın toleranstan daha fazla farklılaşması gerekir.
3. **Tolerans Miktarı:**
   * **Açıklama**: Belge ücreti ile satın alma siparişi ücreti arasında izin verilen sapma.
4. **Tolerans Türü:**
   * **Açıklama**: Tolerans miktarının nasıl yorumlandığı.
   * **Seçenekler**:
     * **Yüzde**: satın alma siparişi ücretinin bir yüzdesi.
     * **Değer**: sabit bir tutar.
5. **Eksik veri davranışı (yalnızca sürüm 3):**
   * **Açıklama**: Bir ücret yalnızca tek tarafta, belgede veya satın alma siparişinde bulunduğunda ve karşılaştırılacak bir karşılığı olmadığında ne yapılacağı. Seçenek, sürüm 3 cümlesinin sonunda yer alır.
   * **Seçenekler**:
     * **uyumsuzluk olarak ele almak**: iş akışı durur. Varsayılan değer budur.
     * **Bunu görmezden gel ve bir kibrit çöpü gibi davran.**: iş akışı, ücret uyuşmuş gibi devam eder.

## **İşlevsellik:**

Kart aşağıdaki adımları izler.

1. **Eşleştirilmiş bir satın alma siparişi gerektirir.** Eşleştirilmiş satın alma siparişi yoksa kart hemen durur ve eksik veri bildirir.
2. **Toleransı okur**, karttaki **Tolerans Miktarı** ve **Tolerans Türü** alanlarından.
3. **Sürüm 3, eşleştirilmiş her satın alma siparişi satırını** dört durumdan birine ayırır ve yalnızca her bir tarafın herhangi bir ücret taşıyıp taşımadığını sorar: her iki tarafta ücret, hiçbir tarafta ücret yok, yalnızca belgede ücret veya yalnızca satın alma siparişinde ücret. Belgedeki satın alma siparişi verileriyle ilişkilendirilemeyen bir satır veri hatasıdır ve kart durur.
4. **Yalnızca tek tarafta bulunan bir ücret tüm kartı belirler.** Eşleştirilmiş bir satır bir tarafta ücret taşıyıp diğerinde taşımadığı anda **Eksik veri davranışı** sonucu belirler ve hiçbir ücret karşılaştırılmaz, doğru eşleşmiş satırların ücretleri de dahil. Operatör ve tolerans dikkate alınmaz.
5. **Hiçbir satır iki taraftan birinde ücret taşımıyorsa**, her iki taraf ek maliyet bulunmadığında uyuşur. **Dıştan** operatörü bununla sağlanmaz, çünkü hiçbir şey toleransın ötesinde farklılaşmaz ve iş akışı durur. Diğer her operatör bu uyuşmayı sağlanmış sayar ve iş akışı devam eder. **Eksik veri davranışı** burada etkili değildir.
6. **Aksi hâlde her ücret karşılaştırılır**, belge tutarı ile satın alma siparişi tutarı, operatör ve tolerans kullanılarak. Sayı olmayan bir ücret tutarı kartı eksik veriyle durdurur.
7. **Karşılaştırmalar toplanır ve bir kez birleştirilir.** Eşleştirilmiş her satırın her ücreti tek bir sonuç kümesine katkı verir ve **Herhangi biri/Hepsi** ayarı bunu kartın tek sonucuna indirger. Toplama belge genelindedir, satır başına değil; bu nedenle **Herhangi**, belgenin herhangi bir yerindeki herhangi bir ücret anlamına gelir. Birleştirilen sonuç doğruysa iş akışı devam eder, aksi hâlde sağlanmamış bir koşulla durur.

Kartı yapılandırmadan önce bilinmesi gereken üç sonuç vardır.

* **içinde ve 0 toleransı tam eşitlik gerektirir.** İki tutarın kuruşuna kadar uyuşması gerekir.
* **Yalnızca tek tarafta bulunan bir ücret her şeyin önüne geçer.** 4. adım her karşılaştırmadan önce çalıştığı için, **Bunu görmezden gel ve bir kibrit çöpü gibi davran.** seçeneği belgedeki doğru eşleşmiş her ücretin tutar denetimini de atlar. Tutarların doğrulanması gerekiyorsa **uyumsuzluk olarak ele almak** seçeneğinde kalın.
* **uyumsuzluk olarak ele almak, iş akışını sağlanmamış bir koşul olarak değil hata olarak durdurur.** İfadeye rağmen kart eksik veri bildirir; iş akışı günlüğü ve kart testi bunu, sağlanmamış bir koşulda kullanılan turuncu yerine kırmızı gösterir. İş akışı her iki durumda da durur.

## **Kurulum ve Yapılandırma:**

Kartı, satın alma siparişi eşleştirmesinden sonra bir And koşulu olarak ekleyin. Her ücretin mi yoksa herhangi bir ücretin mi karşılaştırmayı sağlaması gerektiğini seçin, **içinde** veya **Dıştan** operatörünü seçin ve tolerans miktarı ile türünü girin. Sürüm 3'te, ücretler yalnızca tek tarafta göründüğünde ne olacağını seçin.

Bir yapılandırmayı belge beklemeden denemek için Workflow Builder'da kart menüsünü açın, **Test Kartı** seçeneğini seçin, bir belge seçin ve ardından **Belge Üzerinde Test** seçeneğini seçin. Kart günlüğü, karşılaştırılan her ücreti iki tutar, operatör ve kullanılan toleransla listeler ve bir ücret yalnızca tek tarafta bulunduğunda sonucu hangi **Eksik veri davranışı** değerinin belirlediğini de kaydeder.

## **Örnek Senaryo:**

Bir sipariş onayı 100,00 tutarında bir nakliye ücreti taşır ve eşleştirilmiş satın alma siparişi satırı aynı 100,00 nakliye ücretini taşır. **Tüm**, **içinde** operatörü ve değer olarak 0 toleransıyla tutarlar eşittir, kart sağlanır ve iş akışı devam eder.

Sipariş onayında 100,00 yerine 120,00 bulunduğunda aynı yapılandırma sağlanmaz ve iş akışı sağlanmamış bir koşulla durur.

Ne sipariş onayı ne de satın alma siparişi herhangi bir ücret taşımıyorsa, **içinde** operatörü bunu uyuşma sayar ve iş akışı devam eder, **Dıştan** ise onu durdurur.

Sipariş onayı bir nakliye ücreti taşıyıp satın alma siparişi taşımıyorsa operatör artık geçerli olmaz. **uyumsuzluk olarak ele almak** ile iş akışı durur, böylece birisi ücretin neden yalnızca tek tarafta olduğunu inceleyebilir.

## **Sürümler Arasındaki Farklar:**

Yeni kartlar sürüm 3'ü kullanır. Sürüm 2, mevcut iş akışlarında desteklenmeye devam eder. Her iki sürüm de ücret başına karşılaştırır ve sonuçları **Herhangi biri/Hepsi** ayarıyla belge genelinde birleştirir, ancak sürüm 2'de durum sınıflandırması yoktur; bu da ücretler her iki tarafta bulunmadığı anda ne olacağını değiştirir:

* Sürüm 2'de **Eksik veri davranışı** seçeneği yoktur. Cümlesi tolerans türünden sonra biter.
* Sürüm 2 eşleştirilmiş satırları sınıflandırmaz ve bu nedenle yalnızca tek tarafta bulunan bir ücreti tanımaz. Mevcut tutarı, eksik taraf için tutulan 0,00 ile karşılaştırır ve operatör karar verir: **içinde** sağlanmaz ve iş akışı durur, **Dıştan** sağlanır ve iş akışı devam eder. Kart günlüğü 0,00 ile yapılan karşılaştırmayı gösterir.
* İki taraftan hiçbiri ücret taşımıyorsa sürüm 2'nin karşılaştıracağı bir şey yoktur ve her iki taraftaki yokluğu uyuşma sayacak yerine eksik veri bildirir.

## **Sonuç:**

"Any / All Charges" kartı, faturalanan veya onaylanan ek maliyetlerin sipariş edilen ek maliyetlerle uyuştuğunun denetimini otomatikleştirir. Sürüm 3'te her iki taraftaki ücret yokluğu uyuşma sayıldığı için, ek maliyeti olmayan belgeler elle müdahale olmadan geçer; yalnızca tek tarafta görünen ücretler ise bu kasıtlı olarak izin verilmediği sürece inceleme için bekletilir.
