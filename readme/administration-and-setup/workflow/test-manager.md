# Test Manager

**Test Manager**, iş akışlarınız için yeniden kullanılabilir **test senaryolarını** kaydetmenize ve bunları birlikte çalıştırmanıza olanak tanır — böylece bir iş akışını değiştirdikten sonra hâlâ doğru çalıştığını doğrulayabilirsiniz. Hem Standart hem de Gelişmiş iş akışları için çalışır.

Bunu **Workflow Dashboard → Test Manager List** üzerinden açın.

<figure><img src="../../.gitbook/assets/workflow_test_manager.png" alt="Test Manager List with test scenarios, status and Run All Tests"><figcaption><p>Test Manager List — kaydedilen her senaryo bir başarılı/başarısız sonucu gösterir.</p></figcaption></figure>

## Test senaryosu nedir

Bir test senaryosu, bir iş akışını, bir örnek girdiyi ve **beklenen sonucu** yakalar. Çalıştırdığınızda, Test Manager iş akışını o girdiye karşı yeniden oynatır ve sonucu beklediğiniz şeyle karşılaştırır — satırı **yeşile** (başarılı) veya **kırmızıya** (başarısız) çevirir.

## Senaryolarla çalışma

- **Add Test Scenario** — bir iş akışından ve bir örnek belgeden yeni bir senaryo oluşturun.
- **Run All Tests** — tüm senaryoları aynı anda çalıştırın ve hangi iş akışlarının hâlâ başarılı olduğunu bir bakışta görün.
- **View Details** — bir senaryoyu açıp sonucunu inceleyin.

<figure><img src="../../.gitbook/assets/workflow_test_manager_detail.png" alt="Workflow test scenario details with status, run time and data"><figcaption><p>Senaryo ayrıntıları — adı, durumu, çalışma süresi ve çalıştırmanın ürettiği gerçek (actual) ve çıkarılan (extracted) veriler.</p></figcaption></figure>

Ayrıntılar görünümü; senaryo adını ve **durumunu**, **iş akışı adını**, **çalışma süresini** ve çalıştırmanın ürettiği **gerçek (actual)** ve **çıkarılan (extracted) verileri** gösterir — böylece bir senaryonun tam olarak neden başarılı veya başarısız olduğunu görebilirsiniz.

## Test Manager ile oluşturucuda test etme karşılaştırması

Bunlar iki farklı şeydir:

- **Test Manager** (bu sayfa) — beklenen sonuçlara sahip, **Run All Tests** ile birlikte çalıştırılan *kaydedilmiş, tekrarlanabilir* senaryolar. Değişikliklerden sonra regresyon testi için kullanın.
- **Oluşturucuda test etme** — Gelişmiş İş Akışı oluşturucusunun içindeki, oluştururken hızlı kontroller için olan satır içi **Validate** ve **Test** denetimleri. Bkz. [Doğrulama ve Test Etme](advanced-workflow/validation-and-testing.md).
