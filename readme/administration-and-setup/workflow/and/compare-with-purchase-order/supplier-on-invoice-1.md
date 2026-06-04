---
hidden: true
---

# Supplier on Invoice

<figure><img src="../../../../.gitbook/assets/image (1) (1) (2).png" alt=""><figcaption></figcaption></figure>

## **Amaç**

Bu DocBits kartı, faturanın tedarikçisini sipariş onayının tedarikçisiyle karşılaştırarak ayrıntılı karşılaştırmaya olanak tanır. Faturayı düzenleyen tedarikçinin sipariş onayındakiyle aynı olduğundan emin olunmalıdır.

## **İşlevsellik:**

* **Faturadaki Tedarikçi Satınalma Siparişindeki Tedarikçi:** Bu kart, faturadaki tedarikçinin sipariş onayındakiyle aynı olup olmadığını kontrol eder.
* **Operatör Değeri:** Kullanıcılar şu gibi belirli koşullar ayarlayabilir: Faturayı düzenleyen tedarikçi PO'dakiyle aynı mı yoksa değil mi. Kullanılabilir operatörler şunları içerir:
  * **Is (=):** Faturadaki tedarikçinin sipariş onayındaki tedarikçiyle eşleşip eşleşmediğini kontrol eder.
  * **Is not (≠):** Faturayı düzenleyen tedarikçinin sipariş onayındakiyle aynı olduğunu garanti eder.

## **Kullanım:**

Bu kart, tüm sürecin aynı tedarikçiyle ele alınmasını ve her şeyin birbirine uymasını sağlamak için yararlıdır. Bu, tutarsızlıklar varsa bu tutarsızlıkların kontrol edilmesine dikkat çekilmesini ve sipariş ile sipariş onayıyla hiçbir ilgisi olmayan yanlış bir tedarikçiye faturanın ödenmemesini sağlar.

## **Örnek Senaryo:**

* Bir sipariş verilir, ardından sipariş onayı gelir ve sonra fatura düzenlenir. Tüm sipariş süreci tek bir tedarikçiyle yürütülür. Durum böyle değilse, kart tedarikçiler arasında tutarsızlıklar olduğunu hemen belirleyebilir ve böylece yanlış ödemelerin yapılmamasını ve faturanın yalnızca tüm sürece dahil olan tedarikçiyle yapılmasını sağlar.

"Supplier on Invoice … Supplier on Purchase Order" kartını kullanarak şirketler, fatura düzenleyen tedarikçilerin ve ilgili sipariş onaylarının doğrulanmasını otomatikleştirebilir.
