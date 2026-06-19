# Stabla odlučivanja

{% embed url="https://youtu.be/omFWSkSjlL0" %}
Kako kreirati stablo odlučivanja u DocBits-u (uslovi, politike, testiranje i izvoz)
{% endembed %}

## Pregled

Stabla odlučivanja su moćna funkcija koja omogućava automatizovano usmeravanje i proces donošenja odluka na osnovu unapred definisanih pravila. Ova funkcija je posebno korisna u složenim okruženjima u kojima je potrebno proceniti različite uslove kako bi se utvrdio ispravan tok radnje, kao što su dodeljivanje cena, određivanje količina ili usmeravanje dokumenata.

#### Ključne komponente

* **Lista stabala odlučivanja**: Ovo je glavni interfejs u kome su navedena sva postojeća stabla odlučivanja. Svako stablo odlučivanja može biti povezano sa određenim tipom dokumenta kao što je `INVOICE` ili `QUOTE`.
* **Dizajner stabla odlučivanja**: Ovaj interfejs omogućava kreiranje i uređivanje stabala odlučivanja, gde možete definisati pravila, operatore i radnje koje treba preduzeti kada su ispunjeni određeni uslovi.

## Interfejs stabla odlučivanja

#### Lista stabala odlučivanja

Lista stabala odlučivanja prikazuje sva konfigurisana stabla odlučivanja. Otvorite je preko **Settings → Document Processing → Decision Trees**.

<figure><img src="../../../.gitbook/assets/decision_trees.png" alt="Lista stabala odlučivanja"><figcaption><p>Lista stabala odlučivanja</p></figcaption></figure>

Svaka stavka prikazuje:

| Kolona | Opis |
|--------|-------------|
| **Name** | Naziv stabla odlučivanja. Kliknite na njega da biste otvorili Dizajner. |
| **Document Type** | Tip dokumenta na koji se stablo primenjuje (npr. `INVOICE`, `QUOTE`). |
| **Last Modified By** | Korisnik koji je poslednji uredio stablo. |
| **Last Modified At** | Vremenska oznaka poslednje izmene. |
| **Actions** | Meni sa tri tačke za uređivanje, kopiranje, izvoz ili brisanje stabla. |

#### Kreiranje stabla odlučivanja

1. Kliknite na **+ Add Decision Tree** u gornjem desnom uglu.
2. Unesite **Name** i izaberite **Document Type**.
3. Koristite Dizajner stabla odlučivanja (u nastavku) da biste definisali uslove, politike i rezultate.

#### Uvoz stabla odlučivanja

Kliknite na **Import Decision Tree** da biste otpremili prethodno izvezenu datoteku stabla odlučivanja (JSON format). Ovo je korisno za kopiranje stabla između organizacija ili okruženja.

## Dizajner stabla odlučivanja

Dizajner stabla odlučivanja vam omogućava da konfigurišete pravila koja upravljaju načinom donošenja odluka.

### **Komponente Dizajnera stabla odlučivanja**

* **Pravila**: Svako pravilo se sastoji od uslova i radnji.
* **Select Source**: Ovaj padajući meni vam omogućava da odredite izvorno polje koje se procenjuje.
* **Select Operator**: Definiše logički operator (npr. `<=`, `>=`, `=`, `!=`) koji se primenjuje na izvorno polje.
* **Result**: Definiše ishod ili radnju koja treba da se preduzme kada su ispunjeni uslovi.
* **Add New Row**: Omogućava vam da dodate dodatna pravila u stablo odlučivanja.

### Primer konfiguracije stabla odlučivanja

Ovo stablo odlučivanja procenjuje polje **Total Amount** i dodeljuje ga različitim grupama na osnovu unapred definisanih uslova. Svako pravilo poredi ukupan iznos sa određenom vrednošću, a na osnovu toga koji je uslov tačan, vraća se odgovarajuća vrednost u koloni **Group**.

<figure><img src="../../../.gitbook/assets/decision_tree_example_total_amount.png" alt="Primer stabla odlučivanja Total Amount"><figcaption></figcaption></figure>

Ovo stablo odlučivanja procenjuje dva ključna uslova kako bi utvrdilo koju grupu treba dodeliti: **Total Amount** i **Warehouse Status**. Stablo koristi pragove zasnovane na ukupnom iznosu da definiše koja se grupa vraća, uz dodatnu razliku da li je skladište označeno kao "Warehouse Main", "Warehouse Sub" ili "Not Warehouse Main".

<figure><img src="../../../.gitbook/assets/decision_tree_example_warehouse_status.png" alt="Primer stabla odlučivanja Warehouse Status"><figcaption></figcaption></figure>

Svako pravilo se procenjuje redom.

## Politika stabla odlučivanja

Politika stabla odlučivanja definiše kako se obrađuje više pravila unutar stabla odlučivanja. Možete izabrati između nekoliko politika:

### **1. Politika jedinstvenosti (Unique)**

Obezbeđuje da se podudara samo jedno pravilo. Ako se podudari više pravila, stablo odlučivanja će vratiti false.

**Primer:**

| Pravilo | Uslov            | Vraćena grupa |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Ako je ukupan iznos **1500**, procenjena pravila će biti:

* **Pravilo 1**: Total Amount <= 1000 (ne podudara se)
* **Pravilo 2**: Total Amount <= 2000 (podudara se)
* **Pravilo 3**: Total Amount <= 5000 (podudara se)
* **Pravilo 4**: Total Amount <= 4000 (podudara se)
* **Pravilo 5**: Total Amount <= 3000 (podudara se)

Pošto se podudara više pravila (**Pravilo 2**, **Pravilo 3**, **Pravilo 4**, **Pravilo 5**), stablo odlučivanja će vratiti **false** jer politika **jedinstvenosti (Unique)** obezbeđuje da se može podudariti samo jedno pravilo.

### **2. Politika prvog (First)**

Primenjuje se prvo pravilo koje se podudara, a dalja pravila se ne procenjuju.

**Primer:**

| Pravilo | Uslov            | Vraćena grupa |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Ako je ukupan iznos **1500**, procenjena pravila će biti:

* **Pravilo 1**: Total Amount <= 1000 (ne podudara se)
* **Pravilo 2**: Total Amount <= 2000 (podudara se) → Stablo odlučivanja prestaje da procenjuje dalja pravila i primenjuje **GROUP_2**.

### **3. Politika prioriteta (Priority)**

Izbor ove opcije vam omogućava da postavite prioritete za svako pravilo. Što je izabrani broj niži, to je prioritet viši (tj. prioritet 1 ima najviši prioritet). Pravila se procenjuju na osnovu redosleda prioriteta. Primeniće se pravilo sa najvišim prioritetom koje se podudara.

**Primer:**

<table><thead><tr><th width="137">Pravilo</th><th width="110">Prioritet</th><th width="268">Uslov</th><th>Vraćena grupa</th></tr></thead><tbody><tr><td>1</td><td>5</td><td>Total Amount &#x3C;= 1000</td><td>GROUP_1</td></tr><tr><td>2</td><td>4</td><td>Total Amount &#x3C;= 2000</td><td>GROUP_2</td></tr><tr><td>3</td><td>3</td><td>Total Amount &#x3C;= 3000</td><td>GROUP_3</td></tr><tr><td>4</td><td>2</td><td>Total Amount &#x3C;= 4000</td><td>GROUP_4</td></tr><tr><td>5</td><td>1</td><td>Total Amount &#x3C;= 5000</td><td>GROUP_5</td></tr></tbody></table>

Ako je ukupan iznos **1500**, procenjena pravila će biti:

* **Pravilo 1**: Total Amount <= 1000 (ne podudara se)
* **Pravilo 2**: Total Amount <= 2000 (podudara se)
* **Pravilo 3**: Total Amount <= 3000 (podudara se)
* **Pravilo 4**: Total Amount <= 4000 (podudara se)
* **Pravilo 5**: Total Amount <= 5000 (podudara se)

Pošto se prioritet primenjuje redosledom **5, 4, 3, 2, 1**, pravilo sa najvišim prioritetom koje se podudara biće **Pravilo 5** (**GROUP_5**). Stablo odlučivanja će vratiti **GROUP_5** jer **Pravilo 5** ima najviši prioritet (prioritet 1).

### **4. Politika prikupljanja sume (Collect – sum)**

Ova politika prikuplja sva pravila koja se podudaraju i sabira rezultate. Radi samo za **Return Type Value**.

**Primer:**

| Pravilo | Uslov            | Vraćena vrednost |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

Za ulaznu vrednost **Total Amount = 3500**, procena pravila bila bi:

* **Pravilo 1**: Total Amount <= 1000 (ne podudara se)
* **Pravilo 2**: Total Amount <= 2000 (ne podudara se)
* **Pravilo 3**: Total Amount <= 3000 (podudara se, Return Value = 3)
* **Pravilo 4**: Total Amount <= 4000 (podudara se, Return Value = 4)
* **Pravilo 5**: Total Amount <= 5000 (podudara se, Return Value = 5)

Pošto se primenjuje politika **prikupljanja sume (Collect – sum)**, sabiramo **vraćene vrednosti** pravila koja se podudaraju, a to su **3, 4, 5**.

**Sabiranjem ovih vrednosti** dobijamo:

* 5 + 4 + 3 = **12**

Dakle, rezultat koji vraća stablo odlučivanja bio bi **12**, što je zbir svih vraćenih vrednosti koje se podudaraju.

### **5. Politika prikupljanja (Collect – min/max/count)**

Ova politika prikuplja sva pravila koja se podudaraju i bira **minimum**, **maksimum** ili **broji** pojavljivanja. Radi samo za **Return Type Value**.

**Primer:**

| Pravilo | Uslov            | Vraćena vrednost |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

1. Ako je izabrana opcija **Collect (min)**, rezultat će vratiti **minimum** **vraćenih vrednosti** za pravila koja se podudaraju.
   * Za ulaznu vrednost **Total Amount = 3500**, procena pravila bila bi:
     * **Pravilo 1**: Total Amount <= 1000 (ne podudara se)
     * **Pravilo 2**: Total Amount <= 2000 (ne podudara se)
     * **Pravilo 3**: Total Amount <= 3000 (podudara se, Return Value = 3)
     * **Pravilo 4**: Total Amount <= 4000 (podudara se, Return Value = 4)
     * **Pravilo 5**: Total Amount <= 5000 (podudara se, Return Value = 5)
   * **Pravila koja se podudaraju** su Pravilo 3, Pravilo 4 i Pravilo 5, sa **vraćenim vrednostima** **3, 4 i 5**.
   * Pošto se primenjuje politika **Collect (min)**, rezultat će biti **minimalna vrednost**, koja iznosi **3**.
   * **Rezultat**: **3**
2. Ako je izabrana opcija **Collect (max)**, rezultat će vratiti **maksimum** **vraćenih vrednosti** za pravila koja se podudaraju.
   * Za istu procenu kao gore, rezultat će biti:
   * **Rezultat**: **5**
3. Ako je izabrana opcija **Collect (count)**, rezultat će prebrojati **broj pravila koja se podudaraju**.
   * Za istu procenu kao gore, rezultat će biti:
   * **Rezultat**: **3** (pošto su se podudarila 3 pravila).

### **6. Politika redosleda pravila (Rule Order)**

Ova politika primenjuje pravila redosledom kojim se pojavljuju u stablu odlučivanja i vraća rezultat pravila koje se prvo podudari.

**Primer:**

| Pravilo | Uslov            | Vraćena grupa |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

S obzirom na to da je ulazna vrednost **Total Amount = 3500**, procena pravila bila bi:

* **Pravilo 1**: Total Amount <= 1000 (ne podudara se)
* **Pravilo 2**: Total Amount <= 2000 (ne podudara se)
* **Pravilo 3**: Total Amount <= 3000 (podudara se)
* **Pravilo 4**: Total Amount <= 4000 (podudara se)
* **Pravilo 5**: Total Amount <= 5000 (podudara se)

Pod politikom **Rule Order**, stablo će obraditi pravila redosledom kojim su navedena. Dakle, pravila koja se podudaraju biće:

* **Pravilo 3**: GROUP_3
* **Pravilo 4**: GROUP_4
* **Pravilo 5**: GROUP_5

**Rezultat**: **GROUP_3**, **GROUP_4**, **GROUP_5**

### **7. Politika bilo kog (Any)**

Više pravila može biti tačno, ali rezultat tih pravila mora biti isti.

**Primer:**

| Pravilo | Uslov            | Vraćena grupa |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Ako je ukupan iznos **2500**, procenjena pravila će biti:

* **Pravilo 1**: Total Amount <= 1000 (ne podudara se)
* **Pravilo 2**: Total Amount <= 2000 (ne podudara se)
* **Pravilo 3**: Total Amount <= 3000 (podudara se)
* **Pravilo 4**: Total Amount <= 4000 (podudara se)
* **Pravilo 5**: Total Amount <= 5000 (podudara se)

Da bi se politika **Any** primenila, sva pravila koja se podudaraju moraju vratiti istu **vraćenu grupu**. Pošto se grupe ne podudaraju kroz različita pravila, rezultat bi bio **false**.

### **8. Politika prvog i susednog (First & Adjacent)**

Bira rezultat pravila koje je susedno prvom pravilu koje je tačno.

**Primer:**

| Pravilo | Uslov            | Vraćena grupa |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Ako je ukupan iznos **1500**, procenjena pravila će biti:

* **Pravilo 1**: Total Amount <= 1000 (ne podudara se)
* **Pravilo 2**: Total Amount <= 2000 (podudara se)

Pošto je **Pravilo 2** prvo pravilo koje se podudara, politika **First & Adjacent** bi primenila rezultat **Pravila 3**: **GROUP_3**.

## **Testiranje stabla odlučivanja**

**Pregled:**
Dizajner stabla odlučivanja uključuje funkciju testiranja za proveru logike konfigurisanih pravila. Ova funkcija omogućava korisnicima da testiraju stablo odlučivanja unosom određenih ulaznih vrednosti za izabrana polja.

**Koraci za korišćenje funkcije testiranja:**

1.  **Pronađite dugme Test:**

    * U dizajneru stabla odlučivanja pronađite dugme **Test**.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_button.png" alt="Dugme Test stabla odlučivanja" width="563"><figcaption></figcaption></figure>
2.  **Otvorite iskačući prozor za testiranje:**

    * Kliknite na dugme **Test**.
    * Pojaviće se iskačući prozor sa poljima za unos koja odgovaraju kriterijumima korišćenim u stablu odlučivanja.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_popup.png" alt="Iskačući prozor za testiranje stabla odlučivanja" width="421"><figcaption></figcaption></figure>
3. **Unesite ulazne vrednosti:**
   *   Unesite vrednosti u polja za unos da biste simulirali stvarni scenario.

       <figure><img src="../../../.gitbook/assets/decision_tree_test_input.png" alt="Unos za testiranje stabla odlučivanja" width="428"><figcaption></figcaption></figure>
4.  **Procenite rezultate:**

    * Nakon unosa, stablo ih obrađuje na osnovu izabrane politike.
    * Sistem ističe pravilo (ili pravila) koje se podudara sa unetim vrednostima.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_result.png" alt="Rezultat testiranja stabla odlučivanja" width="563"><figcaption></figcaption></figure>
5. **Pregledajte povratne informacije u slučaju nepodudaranja:**
   * Ako nijedno pravilo nije istaknuto, sistem će prikazati povratne informacije koje objašnjavaju zašto se nijedno pravilo nije podudarilo.
   * Koristite ove povratne informacije da prilagodite ulazne vrednosti ili pregledate konfiguraciju stabla zbog mogućih problema.

## Izvoz i čuvanje

* **Save**: Čuva trenutnu konfiguraciju stabla odlučivanja.
* **Export**: Omogućava vam da izvezete konfiguraciju stabla odlučivanja, koja se zatim može uvesti u drugo okruženje ili koristiti za potrebe rezervne kopije.

## Slučajevi upotrebe

* **Radni tokovi odobravanja** — usmeravajte fakture različitim odobravateljima na osnovu pragova iznosa (na primer, iznosi preko 10.000 zahtevaju odobrenje menadžera).
* **Pravila validacije** — automatski proveravajte vrednosti polja i označavajte dokumente koji ne ispunjavaju konfigurisane kriterijume.
* **Sekvencijalno dodeljivanje** — dodeljujte dokumente korisnicima određenim redosledom na osnovu uslova.
