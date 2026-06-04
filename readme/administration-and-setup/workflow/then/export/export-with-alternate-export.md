# Export with alternate Export

<figure><img src="../../../../.gitbook/assets/image (286).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç**

**"Export Document with Alternate Export"** iş akışı kartı, bir belgeyi alternatif bir dışa aktarma yapılandırması kullanarak dışa aktarmayı mümkün kılar. Kullanıcıların varsayılan dışa aktarma yapılandırmasını atlamasına ve alternatif birini kullanmasına olanak tanıyarak esneklik sunar ve belirli gereksinimlerle veya senaryolarla uyumluluğu sağlar.

## **Kartın Bileşenleri**

**Alternatif Dışa Aktarma Yapılandırması**

* **Açıklama**: Belge için kullanılacak dışa aktarma yapılandırmasını belirtir.
* **Ayrıntı**: Bu yapılandırma, varsayılan ayarları geçersiz kılar ve iş akışında belirtilen alternatif dışa aktarma yapılandırmasını uygular.

## **İşlevsellik**

* **Koşul Değerlendirmesi**:\
  Sistem, iş akışının **"Where"** ve **"And Bölümleri"**nde ayarlanan koşulları değerlendirir. Kart yalnızca tüm koşullar doğruysa yürütülür.
* **Belge Dışa Aktarma**:\
  Yürütüldükten sonra, kart belgeyi işlemek ve dışa aktarmak için alternatif dışa aktarma yapılandırmasını kullanır. Bu, belirli iş akışları için özel dışa aktarma işlemesini mümkün kılar.

## **Kurulum ve Yapılandırma**

Bu kartı yapılandırmak için:

1. Kart yalnızca bu koşullar doğru olarak değerlendirilirse yürütüldüğünden, **"Where"** ve **"And Bölümleri"**nin doğru yapılandırıldığından emin olun.
2. Alternatif dışa aktarma yapılandırmasının sistemde geçerli ve etkin olduğunu doğrulayın.

## **Sonuç**

**"Export Document with Alternate Export"** iş akışı kartı, belge dışa aktarma süreçlerinde esnekliği ve kontrolü artırır. Alternatif bir dışa aktarma yapılandırmasının seçilmesine izin vererek, verimli iş akışı otomasyonunu korurken çeşitli dışa aktarma gereksinimlerini karşılar.
