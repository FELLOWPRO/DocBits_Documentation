# Hızlı Arama

Panonun üstündeki **Hızlı Arama**, belge bulmanın en hızlı yoludur. Aradığınız
şeyi yazın — bir ad, bir durum, bir tutar, bir tarih — ve liste anında filtrelenir.

Bu kılavuz, aramanın kurulduğu sıraya göre düzenlenmiştir:

1. **Standart alanlar** — her belgenin sahip olduğu sütunlar (belge adı, durum,
   tarihler). Her zaman kullanılabilir.
2. **Tam metin alanları** — çıkarılan içerik (tedarikçi, sipariş numarası, fatura
   numarası, tutarlar, satırlar). Tam metin araması etkinleştirildiğinde
   kullanılabilir.
3. **Operatörler, kısayollar ve tarifler** — tam başvuru.

> Hiçbir şey ezberlemenize gerek yok: arama çubuğuna tıklayın ve listeden bir alan
> ve değer seçin. Aşağıdaki örnekler ayrıca doğrudan kopyalanacak yazılı biçimi de
> gösterir.

---

## Arama çubuğu nasıl çalışır — çipler, araç çubuğu ve ham görünüm

Bir koşulu tamamladığınızda (bir alan, bir operatör ve bir değer) Hızlı Arama bunu
bir **çipe** dönüştürür — çubuğun içinde renkli bir hap — ve yenisine başlar. Bir
çip, kaldırmak için bir **×** ile birlikte **alanı**, **operatörü** ve **değeri**
gösterir. Çipler, verinin nerede yaşadığına göre renklerle kodlanır:

| Çip rengi | Alan türü |
|-----------|-----------|
| **Mavi** | Standart sütun (belge adı, durum, tarihler) |
| **Turuncu** | Tam metin / çıkarılan alan (tedarikçi, tutar, fatura numarası) |
| **Mor** | Vektör (anlamsal) arama |
| **Yeşil** | OCR metin araması |

Bir çipi düzenlemek için tıklayın; silmek için **×** öğesine tıklayın. Birleştirilen
birkaç çip varsayılan olarak **AND** olarak okunur.

**Araç çubuğu** (çubuğun sağında): **ⓘ Yardım**, uygulama içi alanlar ve söz dizimi
başvurusunu açar; **Filtreler**, hızlı bir Durum / Kullanıcı / Yeniden Başlat
panelidir; **dizin halkası**, tam metin dizininin ne kadarının oluşturulduğunu
gösterir (yalnızca tam metin araması açık olduğunda).

**Standart ve ham görünüm:** çubuk sorgunuzu çipler olarak gösterir (standart).
Düz metin olarak görmek ve düzenlemek için **ham görünüme** geçin — uzun bir
sorguyu kopyalamak veya yazmak için kullanışlıdır. Sorgunuz yeniden
yüklediğinizde hatırlanır.

### Belgeleri fatura alt türüne göre bulma

```
invoice_sub_type="Cost Invoice"
```

Fatura alt türü sabit bir listedir (örn. **Cost Invoice**, **Purchase Invoice**),
bu nedenle `=` tam bir eşleşmedir ve çubuk bir değer seçici sunar. O alt tür
dışındaki her şey için `invoice_sub_type!="Cost Invoice"` kullanın.

## Sonuçları gruplama

Düz bir liste yerine sonuçları herhangi bir alana göre **gruplayabilirsiniz** —
tedarikçi, durum, belge türü veya bir tarih kovası:

```
group by supplier_name
```

Liste, her biri bir **sayım** içeren daraltılabilir **grup başlıkları** gösterir.
Bir başlığı genişletmek veya daraltmak için tıklayın; bir grubun içine girerek
**ayrıntıya inin** (o değeri bir filtre olarak uygulayın). Gruplama herhangi bir
filtreyle birleşir.

<figure><img src="../../.gitbook/assets/quick_search_16_grouping.png" alt="Tedarikçiye göre gruplanmış sonuçlar"><figcaption><p><code>group by supplier_name</code> — sonuçlar her tedarikçi için bir genişletilebilir başlığa daralır.</p></figcaption></figure>

---

## Bölüm 1 — Standart alanlar

Standart alanlar, belgenin kendi sütunlarıdır. Tam metin araması açık olsun ya da
olmasın **her zaman kullanılabilir**.

### Belgeleri ada göre bulma

Belge adı en yaygın aramadır. Eşleştirmenin üç yolu vardır — hepsi **büyük/küçük
harfe duyarsız**:

#### `=` → ile başlar

```
filename=invoice
```

Adı «invoice» **ile başlayan** belgeleri bulur. Büyük/küçük harf yok sayıldığı
için bunların tümü `filename=invoice` ile eşleşir:

```
Invoice.pdf   iNVoice.pdf   iNvoiCE.pdf   INVOICE.pdf
Invoice.xml   iNVoice.xml   iNvoiCE.edi   …
```

`XYZ_Invoice.pdf` ile **eşleşmez** (orada «invoice» ortadadır — `:` kullanın).

<figure><img src="../../.gitbook/assets/tr_quick_search_02_filename_starts.png" alt="filename=invoice yalnızca invoice ile başlayan adlarla eşleşir"><figcaption><p><code>filename=invoice</code> — yalnızca «invoice» <strong>ile başlayan</strong> adlar, herhangi bir büyük/küçük harfle (<code>INVOICE.pdf</code>, <code>iNvoiCE.pdf</code>, <code>iNVoice.pdf</code>, <code>Invoice.pdf</code> eşleşir — 7 sonuç).</p></figcaption></figure>

#### `:` → içerir (herhangi bir yerde)

```
filename:invoice
```

`:` ile sözcük adın **herhangi bir yerinde** eşleşir — `2026_Invoice.pdf`,
`XYZ_Invoice ABC.pdf`, `123_Invoice ABC bla bla.pdf`.

<figure><img src="../../.gitbook/assets/tr_quick_search_03_filename_contains.png" alt="filename:invoice sözcükle adın herhangi bir yerinde eşleşir"><figcaption><p><code>filename:invoice</code> — «invoice» ile adın herhangi bir konumunda eşleşir (<code>XYZ_Invoice ABC.pdf</code> de dahil).</p></figcaption></figure>

#### `="…"` → ile başlar *veya* biter

```
filename="invoice"
```

Tırnak işaretleri `=` operatörünün değerle **başlayan veya biten** adlarla
eşleşmesini sağlar.

> **Üçü bir satırda:** `=` → ile başlar · `:` → içerir · `="…"` → ile başlar veya
> biter. Hepsi büyük/küçük harfi yok sayar.

### Duruma göre bulma

```
status=ready_for_validation
```

Durum sabit bir listedir, bu nedenle `=` **tam** eşleşmedir ve çubuk bir değer
seçici sunar.

### Tarihe göre bulma

```
created_on>2026-05-25
```

Tarih aralıkları için `>`, `<`, `>=`, `<=` kullanın. Ayrıca **göreceli** tarihler:
`today()`, `today()-7` (son 7 gün), `today()+30`.

---

## Bölüm 2 — Tam metin alanları

Tam metin alanları **çıkarılan içerikte** arama yapar — tedarikçi, sipariş
numarası, fatura numarası, tutarlar, satırlar. **Turuncu** görünürler ve **tam
metin aramasının açık** olmasını gerektirir. Eşleştirme kuralları standart metin
alanlarıyla aynıdır (`=` ile-başlar, `:` içerir, `="…"` başlar-veya-biter).

### Bir tedarikçinin belgelerini bulma

```
supplier_name=Test
```

Çıkarılan tedarikçi adında ile-başlar; `supplier_name:fuji` herhangi bir yerde
eşleşir; `supplier_name:"Ruiz Foods"` boşluk içeren bir değeri tırnak içine alır.

### Tutara göre bulma

```
total_amount>5000
```

Bir pencere için `>`, `<`, `>=`, `<=` veya `between 1000 and 5000` kullanın.

### Eksik olanı bulma

```
supplier_name=""
```

`=""` «bu alan **ayarlanmamış**» demektir; `supplier_name!=""` «herhangi bir
tedarikçisi var» demektir. Aynı denetim her alan için geçerlidir, örn.
`ap_assignment_code=""`.

---

## Akıllı filtreler — tek tık

Arama açılır menüsünün üstünde **Akıllı filtreler** bulunur: tek tıkla hazır
aramalar. Her biri yazabileceğiniz bir sorgunun kısayoludur:

| Akıllı filtre | Bulur | Şuna eşittir |
|---------------|-------|--------------|
| ⚠️ **Gecikmiş** | Vade tarihi geçmiş | `invoice_due_date<today()` |
| 🕐 **Yakında dolacak** | Önümüzdeki 7 gün içinde | `invoice_due_date<=today()+7` |
| 👤 **Bana atanmış** | İşleminizi bekliyor | `assigned_to=<siz>` |
| 📅 **Bugünün gelen kutusu** | Bugün içe aktarılmış | `imported_on>=today()` |
| 📋 **Doğrulama bekliyor** | Doğrulanmaya hazır | `status=ready_for_validation` |
| 🧾 **Elektronik belgeler** | E-faturalar (XML, ZUGFeRD, EDI) | `is_edoc=true` |
| ✅ **Tam PO eşleşmesi** | Bir siparişle tam eşleşmiş | `po_match_status=full_matched` |
| ➗ **Kısmi PO eşleşmesi** | Kısmen eşleşmiş | `po_match_status=partial_matched` |
| 📉 **Eksik PO eşleşmesi** | Miktar veya fiyat siparişin altında | `po_match_status=under_matched` |

Üç **PO eşleşmesi** filtresi ve tam metin alanları, tam metin aramasının açık
olmasını gerektirir.

---

## Bölüm 3 — Operatörler, bağlayıcılar, kısayollar

### Yerleşik yardım

Arama çubuğundaki **yardım simgesi**, çalışma alanınızdaki tüm alanların,
operatörlerin ve kısayolların tam bir başvurusunu açar.

<figure><img src="../../.gitbook/assets/tr_quick_search_08_help_modal.png" alt="Tüm operatörlerle yerleşik pano arama yardımı"><figcaption><p>Yerleşik yardım <strong>Pano Araması — Alanlar ve Söz Dizimi</strong>, her operatörü ve değerlerin nasıl eşleştiğini listeler (örn. «Tam / ile başlar»).</p></figcaption></figure>

### Alan türüne göre `=` ne anlama gelir

Her metin eşleşmesi büyük/küçük harfi yok sayar.

| Alan türü | Örnek | `=` anlamı |
|-----------|-------|------------|
| Metin (ad, tedarikçi, sipariş) | `filename=invoice` | **ile başlar** |
| Metin, herhangi bir yerde | `filename:invoice` | **içerir** |
| Metin, başlangıç *veya* son | `filename="invoice"` | **ile başlar veya biter** |
| Durum / tür / PO eşleşmesi (sabit listeler) | `status=finished` | **tam** |
| Tanımlayıcılar (fatura no, tedarikçi id) | `invoice_number=INV-100` | **tam** |
| Sayı | `total_amount>5000` | aralık (`> < >= <= between`) |
| Tarih | `created_on>2026-01-01` | aralık + `today()±N` |

### Operatörler

| Operatör | Anlamı |
|----------|--------|
| `=` | ile-başlar (metin) / tam (liste, sayı, tarih) |
| `:` | içerir (metin, herhangi bir yerde) |
| `="…"` | ile-başlar veya biter (metin) |
| `!=` | `=` operatörünün tersi |
| `>` `<` `>=` `<=` | büyük / küçük |
| `between … and …` | dahil aralık |
| `field=""` / `field!=""` | boş / ayarlanmış |
| `today()`, `today()-7`, `today()+30` | göreceli tarihler |

### Bağlayıcılar

Koşulları **AND** (her ikisi), **OR** (biri), **NOT** ve gruplamak için
parantez `( … )` ile birleştirin:

```
status=ready_for_validation AND supplier_name=Test
(status=error OR status=failed) AND created_on>today()-1
```

### Kısayollar

Aynı sorgular için daha kısa biçimler:

| Kısayol | Şuna eşittir |
|---------|--------------|
| `total_amount gt 5000` | `total_amount>5000` (gt/gte/lt/lte takma adları) |
| `due_date > today` | `due_date>today()` |
| `imported_on this_week` | bu ISO haftası (ayrıca `last_week`, `this_month`, …) |
| `ap_assignment_code is empty` | `ap_assignment_code=""` |
| `status:open` | `status=ready_for_validation` (open/closed/failed/done) |
| `total_amount not between 100, 200` | `total_amount<100 OR total_amount>200` |
| `status in (finished, error)` | `status=finished OR status=error` |
| `not status=finished` | `status!=finished` |
| `filename contains rechnung` | `filename:rechnung` |
| `total_amount > 5k` | `total_amount>5000` (`k`=bin, `M`=milyon) |
| `overdue` | `invoice_due_date<today() AND status!=finished` |
| `#INV-1234` | `invoice_id:INV-1234` |
| `@User` | `assigned_to:User` |
| `$5000+` | `total_amount>=5000` |

### Kısayollar için sorgu + sonuç galerisi

Bu örnekler her kısayol desenini yazdığınız sorgu ve panelde görünen sonuçla birlikte gösterir. İlk grup standart alanları kullanır ve tam metin araması açık olmasa da çalışır. İkinci grup tutar veya fatura vadesi gibi yalnızca tam metin alanlarını kullanır.

#### Tam metin olmadan çalışır

##### Operatör takma adları

- Sorgu: `created_on gt 2026-05-25`
- Eşdeğeri: `created_on>2026-05-25`
- Sonuç: Created alanını 25 Mayıs 2026 sonrasına göre filtreler.

<figure><img src="../../.gitbook/assets/quick_search_shortcut_01_operator_aliases.png" alt="Şu sorgu için Quick Search sonucu created_on gt 2026-05-25"><figcaption><p><code>created_on gt 2026-05-25</code> - Created alanını 25 Mayıs 2026 sonrasına göre filtreler.</p></figcaption></figure>

##### Parantezsiz tarih sözcükleri

- Sorgu: `created_on < today`
- Eşdeğeri: `created_on<today()`
- Sonuç: today sözcüğünü today() biçimine genişletir.

<figure><img src="../../.gitbook/assets/quick_search_shortcut_02_bare_date.png" alt="Şu sorgu için Quick Search sonucu created_on &lt; today"><figcaption><p><code>created_on &lt; today</code> - today sözcüğünü today() biçimine genişletir.</p></figcaption></figure>

##### Göreceli dönem

- Sorgu: `created_on this_month`
- Eşdeğeri: `created_on>=first day of this month AND created_on<=last day of this month`
- Sonuç: this_month ifadesini bir tarih aralığına genişletir.

<figure><img src="../../.gitbook/assets/quick_search_shortcut_03_period.png" alt="Şu sorgu için Quick Search sonucu created_on this_month"><figcaption><p><code>created_on this_month</code> - this_month ifadesini bir tarih aralığına genişletir.</p></figcaption></figure>

##### Boş/dolu sözcükleri

- Sorgu: `assigned_to is empty`
- Eşdeğeri: `assigned_to=""`
- Sonuç: Atanmamış belgeleri bulur.

<figure><img src="../../.gitbook/assets/quick_search_shortcut_04_presence.png" alt="Şu sorgu için Quick Search sonucu assigned_to is empty"><figcaption><p><code>assigned_to is empty</code> - Atanmamış belgeleri bulur.</p></figcaption></figure>

##### Okunabilir durum

- Sorgu: `status:open`
- Eşdeğeri: `status=ready_for_validation`
- Sonuç: open ifadesini doğrulama durumuna eşler.

<figure><img src="../../.gitbook/assets/quick_search_shortcut_05_status_open.png" alt="Şu sorgu için Quick Search sonucu status:open"><figcaption><p><code>status:open</code> - open ifadesini doğrulama durumuna eşler.</p></figcaption></figure>

##### Arasında değil

- Sorgu: `created_on not between 2026-06-01, 2026-06-15`
- Eşdeğeri: `(created_on<2026-06-01 OR created_on>2026-06-15)`
- Sonuç: Tarih penceresinin dışındaki değerleri bulur.

<figure><img src="../../.gitbook/assets/quick_search_shortcut_06_not_between.png" alt="Şu sorgu için Quick Search sonucu created_on not between 2026-06-01, 2026-06-15"><figcaption><p><code>created_on not between 2026-06-01, 2026-06-15</code> - Tarih penceresinin dışındaki değerleri bulur.</p></figcaption></figure>

##### In listesi

- Sorgu: `status in (ready_for_validation, exported)`
- Eşdeğeri: `status=ready_for_validation OR status=exported`
- Sonuç: Listelenen durumlardan herhangi biriyle eşleşir.

<figure><img src="../../.gitbook/assets/quick_search_shortcut_07_in_list.png" alt="Şu sorgu için Quick Search sonucu status in (ready_for_validation, exported)"><figcaption><p><code>status in (ready_for_validation, exported)</code> - Listelenen durumlardan herhangi biriyle eşleşir.</p></figcaption></figure>

##### Olumsuzlama öneki

- Sorgu: `not status=finished`
- Eşdeğeri: `status!=finished`
- Sonuç: finished durum koşulunu tersine çevirir.

<figure><img src="../../.gitbook/assets/quick_search_shortcut_08_negation.png" alt="Şu sorgu için Quick Search sonucu not status=finished"><figcaption><p><code>not status=finished</code> - finished durum koşulunu tersine çevirir.</p></figcaption></figure>

##### Metin içerir

- Sorgu: `filename contains E2E`
- Eşdeğeri: `filename:E2E`
- Sonuç: contains ifadesini dosya adı içinde alt dize araması olarak kullanır.

<figure><img src="../../.gitbook/assets/quick_search_shortcut_09_contains.png" alt="Şu sorgu için Quick Search sonucu filename contains E2E"><figcaption><p><code>filename contains E2E</code> - contains ifadesini dosya adı içinde alt dize araması olarak kullanır.</p></figcaption></figure>

##### Fatura öneki

- Sorgu: `#INV-1234`
- Eşdeğeri: `invoice_id:INV-1234`
- Sonuç: #... ifadesini fatura ID aramasına eşler.

<figure><img src="../../.gitbook/assets/quick_search_shortcut_12_invoice_prefix.png" alt="Şu sorgu için Quick Search sonucu #INV-1234"><figcaption><p><code>#INV-1234</code> - #... ifadesini fatura ID aramasına eşler.</p></figcaption></figure>

##### Atanan öneki

- Sorgu: `@Daniel`
- Eşdeğeri: `assigned_to:"Daniel"`
- Sonuç: @... ifadesini atanan kişi adı aramasına eşler.

<figure><img src="../../.gitbook/assets/quick_search_shortcut_13_assignee_prefix.png" alt="Şu sorgu için Quick Search sonucu @Daniel"><figcaption><p><code>@Daniel</code> - @... ifadesini atanan kişi adı aramasına eşler.</p></figcaption></figure>

#### Tam metin araması gerektirir

Aynı kısayolu yalnızca tam metin alanıyla kullanırsanız sorgu yine tam metin gerektirir. Örneğin `ap_assignment_code is empty`, `assigned_to is empty` ile aynı boş/dolu kısayolunu kullanır, ancak AP atama alanı tam metin alanıdır.

##### Tutar soneki

- Sorgu: `total_amount > 5k`
- Eşdeğeri: `total_amount>5000`
- Sonuç: Tutar alanında k değerini binlere genişletir.

<figure><img src="../../.gitbook/assets/quick_search_shortcut_10_currency_suffix.png" alt="Şu sorgu için Quick Search sonucu total_amount &gt; 5k"><figcaption><p><code>total_amount &gt; 5k</code> - Tutar alanında k değerini binlere genişletir.</p></figcaption></figure>

##### Gecikmiş kısayolu

- Sorgu: `overdue`
- Eşdeğeri: `invoice_due_date<today() AND status!=finished`
- Sonuç: Vadesi geçmiş ve tamamlanmamış faturaları bulur.

<figure><img src="../../.gitbook/assets/quick_search_shortcut_11_overdue.png" alt="Şu sorgu için Quick Search sonucu overdue"><figcaption><p><code>overdue</code> - Vadesi geçmiş ve tamamlanmamış faturaları bulur.</p></figcaption></figure>

##### Tutar öneki

- Sorgu: `$5000+`
- Eşdeğeri: `total_amount>=5000`
- Sonuç: $...+ ifadesini tutar eşiğine eşler.

<figure><img src="../../.gitbook/assets/quick_search_shortcut_14_amount_prefix.png" alt="Şu sorgu için Quick Search sonucu $5000+"><figcaption><p><code>$5000+</code> - $...+ ifadesini tutar eşiğine eşler.</p></figcaption></figure>

---

## Bölüm 4 — Gelişmiş arama modları

Alan aramasının ötesinde, üç önek belgenin içeriğinde arama yapar.

### Vektör (anlamsal) arama — `vector:`

Tam metne göre değil **anlama** göre eşleşir. Vector modülünü gerektirir.

```
vector: invoices about office supplies
vector: shipping delays with Hamburg port
```

### OCR metin araması — `ocr:`

Yalnızca sütunlarda değil, OCR'nin çıkardığı **sayfa metninde** arar.

```
ocr: Versandkosten
ocr: "purchase order PO-12345"
ocr: Hamburg AND doc_type=INVOICE
```

### Doğal dil (YZ) araması — `ai:`

Aradığınızı normal dilde tarif edin; YZ cümlenizi okur ve filtreleri (tedarikçi,
tarihler, tutarlar) yapılandırılmış bir sorguya çıkarır.

```
ai: invoices from Ruiz over 1000 last quarter
ai: overdue invoices waiting on approval
```

---

### Tarifler

| İstediğiniz… | Şunu yazın |
|--------------|------------|
| Doğrulamaya hazır, tam eşleşmiş | `status=ready_for_validation AND po_match_status=full_matched` |
| Bu tedarikçi, bu hafta | `supplier_name=Test AND created_on>today()-7` |
| Yüksek tutarlı gecikmiş faturalar | `total_amount>5000 AND invoice_due_date<today()` |
| Aynı anda iki tedarikçi | `supplier_name=fuji OR supplier_name=acme` |
| Bugünkü hatalı belgeler | `(status=error OR status=failed) AND created_on>today()-1` |
| Sipariş numarası önekine göre | `purchase_order=PO-2026` |

> Turuncu (tam metin) alanlar ve akıllı PO filtreleri **tam metin aramasının**
> açık olmasını gerektirir.
