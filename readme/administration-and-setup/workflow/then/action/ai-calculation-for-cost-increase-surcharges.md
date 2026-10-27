# AI Calculation for Cost Increase Surcharges

<figure><img src="../../../../.gitbook/assets/image (309).png" alt="" width="563"><figcaption></figcaption></figure>

## Bu kart ne zaman kullanılır

Bu eylemi, geçerli belge için yapılandırılmış MTZ/ETZ malzeme ve enerji ek ücreti hesaplamasını talep etmek için kullanın. Önce kuruluşunuzun gerektirdiği belge verilerini ve hesaplama hizmeti yapılandırmasını hazırlayın.

## Gerçek yapılandırma

Görüntülenen kartta Cost Increase Factor, Base Cost Field veya Surcharge Field girdileri yoktur. Hesaplamayı yapılandırılmış hizmete devreder. Var olmayan bu kart denetimlerini aramayın ve kart adından sabit bir yüzde formülü varsaymayın.

## Sonuç ve doğrulama

Hizmetten gelen başarılı yanıt kartı başarılı olarak işaretler. Zaman aşımı veya başarısız yanıt kart hatası üretir. Kart günlüğünü ve belgede oluşan ek ücret verilerini inceleyin; çağrının başarılı olması tek başına belirli bir tutarı belgelemez.

Kart test modunda çağrı atlanır ve başarı simüle edilir. Bu, iş akışı yapısını test etmek için yararlıdır, ancak hizmetin çalıştığını veya herhangi bir ek ücretin hesaplandığını kanıtlamaz.

<!-- workflow-card-practical-example-20261021 -->

## Uygulamalı örnek

**Ne zaman kullanılır:** Hazırlanmış bir fatura için yapılandırılmış malzeme/enerji ek ücreti hesaplamasını talep edin.

**Yapılandırma:** Yapılandırılmış MTZ/ETZ hizmetinizin gerektirdiği verilere sahip `DEMO-001` sentetik faturasını kullanın. Bu eylemi belge doğrulama koşullarından sonra ekleyin.

**Beklenen sonuç ve karşı örnek:** Hizmetten gelen başarılı yanıt kartı başarılı olarak işaretler; zaman aşımı veya başarısız yanıt kart hatası üretir. Belge alanlarını ve hesaplama sonucunu ayrı ayrı inceleyin. Kart test modu başarıyı simüle eder ve hizmeti çağırmaz; bu nedenle gerçek bir ek ücret sonucunu kanıtlayamaz.

Bu, açıklayıcı bir yapılandırma ve beklenen sonuçtur. Test kuruluşunuzda yapılandırılmış alanları, kullanıcıları ve grupları kullanın; örneğin yürütüldüğü iddiası değildir.
