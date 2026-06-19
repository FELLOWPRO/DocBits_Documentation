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

* [Politika jedinstvenosti (Unique)](decision-trees/unique-policy.md)
* [Politika prvog (First)](decision-trees/first-policy.md)
* [Politika prioriteta (Priority)](decision-trees/priority-policy.md)
* [Politika prikupljanja sume (Collect – sum)](decision-trees/collect-sum-policy.md)
* [Politika prikupljanja (Collect – min/max/count)](decision-trees/collect-min-max-count-policy.md)
* [Politika redosleda pravila (Rule Order)](decision-trees/rule-order-policy.md)
* [Politika bilo kog (Any)](decision-trees/any-policy.md)
* [Politika prvog i susednog (First & Adjacent)](decision-trees/first-and-adjacent-policy.md)

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
