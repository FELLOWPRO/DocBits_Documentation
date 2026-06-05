# Workflow Documentation

**Workflow Documentation**

Genel bir bakış sağlamak için iş akışlarına farklı başlıklar verebilir, böylece bu iş akışının hangi görevle ilgili olduğunu hemen anlayabilirsiniz.

Yeni bir Workflow oluşturun: + ADD WORKFLOW'a tıklayın

![](<../../.gitbook/assets/workflow_add_button.png>)

Bu iş akışlarını (Test 1, 2, 3) kullanarak çeşitli belgeleri şirketteki doğru çalışana otomatik olarak atayabilirsiniz.

![](<../../.gitbook/assets/workflow_list_overview.png>)

Bir fatura veya başka bir belge, önceden inceleme ve onay gerektiren belirli bir toplam tutarı aşarsa, bu belgeler hemen doğru kişiye atanabilir.

<figure><img src="../../.gitbook/assets/workflow_amount_check.png" alt="Workflow Amount Check"><figcaption></figcaption></figure>

**Test 1: Logic Card**

When: **Assignee is:** Amier Haider

And: **Document type is:** Invoice

Then: **Assign document to:** Stefan Reppermund

![](<../../.gitbook/assets/3 (1).png>)

**Test 2: Logic Card**

When: **Assignee is:** Amier Haider

And: **Document type is:** Delivery Note

Then: **Assign document to:** James Edwards

![](<../../.gitbook/assets/4 (1).png>)

**Test 3: Logic Card**

**When:** **Assignee is:** Amier Haider

**And:** **Document type is:** Order Confirmation

**Then:** **Assign document to:** Anian Sollinger

![](<../../.gitbook/assets/5 (1).png>)

Belge tek bir kişiye atanmamışsa, baştan itibaren belirli bir çalışana atamak da mümkündür.

<figure><img src="../../.gitbook/assets/workflow_assign_to_employee_start.png" alt="Workflow Assign to Employee Start" width="375"><figcaption></figcaption></figure>

Bir belgeye ne olması gerektiğine ilişkin daha kolay bir genel bakış için, bu iş akışında gelen belgelerin durumunu ayarlayabilirsiniz. Bu iş akışı, örneğin bekleyen bir onay olup olmadığını hemen görmeyi mümkün kılar.

**Test 4: Logic Card**

**When:** **Document type is:** Delivery Note

**And:** **Assignee is:** Amier Haider

**Then:** **Change Status to:** Pending Approval

<figure><img src="../../.gitbook/assets/workflow_test4_delivery_note_status.png" alt="Workflow Test 4 Delivery Note Status"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/8 (1).png>)

**Test 5: Logic Card**

When: **Document type is:** Invoice

And: **Assignee is:** Stefan Reppermund

Then: **Change Status to:** Pending Second Approval

<figure><img src="../../.gitbook/assets/workflow_test5_invoice_approval_status.png" alt="Workflow Test 5 Invoice Approval Status"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/10 (1).png>)

Bir fatura veya başka bir belge, önceden inceleme ve onay gerektiren belirli bir toplam tutarı aşarsa, bu belgeler hemen doğru kişiye atanabilir.

![](<../../.gitbook/assets/11 (1).png>)

**Test 6: Logic Card**

When: **Assignee is:** Amier Haider

And: Docfield **total\_amount** is **Greater than 500**

Then: **Assign document to:** Asad Usman Khan

<figure><img src="../../.gitbook/assets/workflow_test6_total_amount_assign.png" alt="Workflow Test 6 Total Amount Assign"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/13 (1).png>)

Durumu iş akışına girmek de mümkündür, böylece atanan kişi bu belgenin hangi durumda olduğunu ve bundan sonra onunla ne yapılması gerektiğini hemen görebilir.

**Test 7: Logic Card**

**When:** **Assignee is:** Amier Haider

**And:** Docfield **total\_amount** is **Greater then 500**

**Then:** **Assign document to:** Asad Usman Khan

**Change Status to:** Pending Approval

<figure><img src="../../.gitbook/assets/workflow_test7_status_update.png" alt="Workflow Test 7 Status Update"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/15 (1).png" alt=""><figcaption></figcaption></figure>

Örneğin, bir belgede belirli veya önemli bilgiler eksikse, ancak bunlar önemliyse ve daha fazla işlem için dahil edilmesi gerekiyorsa, iş akışını bu belgelerin hemen alıcıya ve bir vekile (yedeğe) iletilecek şekilde ayarlayabilirsiniz.

<figure><img src="../../.gitbook/assets/workflow_test8_missing_info.png" alt="Workflow Test 8 Missing Info"><figcaption></figcaption></figure>

**Test 9:**

Bu logic card'larla oluşturulan iş akışı, bir sipariş onayında ayrıntılı olarak belirtilen miktar, birim fiyat veya iskontonun satın alma siparişindeki ilgili rakamlarla eşleşip eşleşmediğini otomatik olarak doğrulamak için tasarlanmıştır. Bu doğrulama, sipariş edilen ile tedarikçinin teslim etmeyi onayladığı arasında tutarlılık ve doğruluk sağlar.

Bu belgelere belirli bir durum verebilir veya onları belirli bir çalışana atayabilirsiniz.

<div align="center"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="Workflow Test 9 Match Check Overview"><figcaption></figcaption></figure></div>

<figure><img src="../../.gitbook/assets/workflow_test9_match_check_detail.png" alt="Workflow Test 9 Match Check Detail"><figcaption></figcaption></figure>

**Logic Card: Quantity or Unit Price or Discount Match**

Bu logic card, bir sipariş onayında ayrıntılı olarak belirtilen miktar, birim fiyat veya iskontonun satın alma siparişindeki ilgili rakamlarla eşleşip eşleşmediğini otomatik olarak doğrulamak için tasarlanmıştır. Bu doğrulama, sipariş edilen ile tedarikçinin teslim etmeyi onayladığı arasında tutarlılık ve doğruluk sağlar.

**Tetikleme Koşulu**

Bu mantık, bir sipariş onayında orijinal satın alma siparişine kıyasla aşağıdaki koşullardan herhangi biri karşılandığında etkinleştirilir:

* **Miktar**: Sipariş edilen kalemlerin miktarı, tedarikçi tarafından onaylanan miktarla eşleşir.
* **Birim Fiyat**: Üzerinde anlaşılan kalem başına fiyat, tedarikçinin onayıyla eşleşir.
* **İskonto**: Uygulanan iskontolar, satın alma siparişi ile sipariş onayı arasında tutarlıdır.
* **Karşılaştırma Parametrelerini Tanımlama**: Logic card'ın eşleşme açısından kontrol edeceği belirli alanları (miktar, birim fiyat, iskonto) ayarlayın.
* **Doğrulamayı Otomatikleştirme**: Sistemi, bir sipariş onayı alındığında bu ayrıntıları otomatik olarak karşılaştıracak şekilde yapılandırın.
* **Uyarıları Özelleştirme**: Manuel inceleme için uyarıların özelleştirilmesi dahil, tutarsızlıkların ele alınmasına ilişkin iş akışına karar verin.

Bu logic card, bir sipariş onayının ayrıntılarının orijinal satın alma siparişiyle uyumlu olmasını sağlamak ve böylece satın alma döngüsünün bütünlüğünü korumak için hayati önem taşır.

**Test 10:**

Ek ücretler için farklı bir hesaplamanız varsa veya bunlar yalnızca bazı kalemlerde mevcutsa, genel tablo hesaplama kartlarını kullanabilirsiniz; bunların bazıları ayrıca düzenli ifadelere (regular expressions) göre filtrelemeye de olanak tanır.

<figure><img src="../../.gitbook/assets/19 (1).png" alt=""><figcaption></figcaption></figure>

Yukarıda, 01, 06, 9, 001 veya 000 ile başlayan kalem numaraları için bir filtreyle MTZ'ye yönelik bir hesaplama örneği yer almaktadır.

Manuel bir kurulumda, yeni sütunlara bağlı hesaplamaların ayrı bir iş akışına bölünmesi önerilir. Hesaplamaya devam etmek için Run Workflow kartını kullanabilirsiniz.

**Run Workflow**

<figure><img src="../../.gitbook/assets/20 (1).png" alt=""><figcaption></figcaption></figure>

Bu kartla, koşulları karşılandığında ve geçerli iş akışının önceki then kartlarından sonra mevcut iş akışının ardından çalıştırılacak bir iş akışının adını belirtebilirsiniz. Çalıştırılabilir, etkin iş akışlarına öncelik verirken, belge iş akışının koşullarını karşılıyorsa devre dışı bırakılmış iş akışlarını da çalıştırmanıza olanak tanır.

### **Hesaplanan ek ücretleri mevcut bir sütuna ekleme** <a href="#pekg4i18rshn" id="pekg4i18rshn"></a>

<figure><img src="https://lh7-us.googleusercontent.com/XYY1xsFpp7_-Bi0WOSbotiVzspDLdaufx_xgoopMHmxdZnSDhroLpb0AE_si5PhwMq1jHfndc9FwOte9MOoCoTP5_JUYawO5cr4uIctIDHmwVjz3KacQrLJd8iBQy5KY4N-dMaWEi3IeTcc5OBRNJk4" alt=""><figcaption></figcaption></figure>

Tüm ek ücretleri negatif bir iskonto olarak iskonto sütununa eklemek istiyorsanız, hesaplama kartını kullanabilirsiniz. Bu sütunda zaten girdiler olabilir; bunu karttaki değişkenlerden biri olarak ayarlayabilir, ondan MTZ'yi çıkarabilir ve sonucu tekrar bu sütuna ekleyebilirsiniz. Boş alanların olması durumunda (yalnızca bazı kalemler için ek ücretler), hesaplaması için 0 değeri varsayılır.

**Sipariş onayını DocBits'te yetkilendirmesi için kullanıcıyı bilgilendirme**

Ek ücretleri hesapladıktan sonra, sipariş onayını yetkilendirmesi için belirli bir kullanıcıyı bilgilendirmek isteyebilirsiniz. Bunun için bildirim kartını kullanabilirsiniz.

<figure><img src="../../.gitbook/assets/workflow_notification_card_overview.png" alt="Workflow Notification Card"><figcaption></figcaption></figure>

Ayarlara bağlı olarak, kullanıcıya DocBits'te yeni bir görev atanır ve isteğe bağlı olarak yeni görevi hakkında onu bilgilendirmek için bir e-posta gönderilir.
