# Vodiči za obrasce toka rada

**Verzija:** 1.0
**Poslednje ažuriranje:** 23. oktobar 2025.

---

## Pregled

Ovaj direktorijum sadrži sveobuhvatne vodiče za obrasce toka rada koji pokazuju kako kombinovati više kartica toka rada za rešavanje uobičajenih poslovnih scenarija. Svaki obrazac pruža uputstva za implementaciju korak po korak, kompletne primere i najbolje prakse.

**Šta su obrasci toka rada?**

Obrasci toka rada su dokazana rešenja za ponovnu upotrebu za uobičajene izazove obrade dokumentacije. Umesto da počinjete od nule, možete koristiti ove obrasce kao šablone i prilagoditi ih svojim specifičnim potrebama.

---

## Workflow Builder na prvi pogled

Svaki obrazac na ovoj stranici sastavlja se u **Workflow Builder**-u. Do njega dolazite preko **Workflow Dashboard → Workflow List → Add Workflow** (ili otvaranjem postojećeg toka rada). Kontrolna tabla vam daje istoriju pokretanja i stope uspeha/neuspeha za sve vaše tokove rada:

<figure><img src="../../../.gitbook/assets/workflow_dashboard.png" alt="Workflow Dashboard prikazuje ukupne brojeve pokretanja, stope uspeha i neuspeha, grafikon pokretanja toka rada i nedavnu aktivnost"><figcaption><p>Workflow Dashboard — ukupni brojevi pokretanja, stope uspeha/neuspeha i nedavna aktivnost za svaki tok rada.</p></figcaption></figure>

Kartica **Workflow List** prikazuje svaki tok rada sa njegovim tipom, redosledom izvršavanja i okidačem. Koristite **Add Workflow** da kreirate novi, ili kliknite na tok rada da ga otvorite u graditelju:

<figure><img src="../../../.gitbook/assets/workflow_list.png" alt="Kartica Workflow List koja navodi tokove rada sa tipom, redosledom izvršavanja i okidačem"><figcaption><p>Workflow List — svaki red je tok rada koji možete otvoriti, uključiti/isključiti ili urediti.</p></figcaption></figure>

Tok rada se gradi od tri grupe kartica — **When** (okidač), **And** (dodatni uslovi) i **Then** (akcije koje treba pokrenuti). Primer ispod se okida na fakturama koje pripadaju pod-organizaciji i dodeljuje ih korisniku:

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder platno sa When, And i Then karticama"><figcaption><p>Workflow Builder platno. Svaki obrazac ispod je samo drugačija kombinacija When / And / Then kartica.</p></figcaption></figure>

Kliknite na **Add Card** u bilo kojoj grupi da otvorite biblioteku kartica. Kartice su organizovane po kategorijama (Compare with Purchase Order, Partner Cards, Document Field, Date &#x26; Time, Document, Logic, Status, Table, Assignee, …) tako da možete pronaći gradivni blok koji svaki obrazac zahteva:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Dijalog Add Card koji prikazuje kategorije kartica i dostupne kartice"><figcaption><p>Biblioteka <strong>Add Card</strong> — svaka kartica navedena u obrascima ispod bira se odavde.</p></figcaption></figure>

---

## Dostupni obrasci

### 1. [API Integration Pattern](api-integration-pattern.md)

**Složenost:** Srednja | **Vreme podešavanja:** 45-60 minuta

Naučite kako da integrišete DocBits sa eksternim API-jima radi preuzimanja, validacije i čuvanja podataka iz eksternih sistema.

**Slučajevi upotrebe:**
- Preuzimanje cena u realnom vremenu iz eksternih sistema
- Validacija informacija o dobavljaču u odnosu na glavne baze podataka
- Pretraga detalja o proizvodu iz katalog sistema
- Dobijanje kursa valuta iz servisa za valute
- Verifikacija adresa pomoću servisa za geokodiranje

**Korišćene kartice:** CALL_API, CONDITION_HTTPS_REQUEST_STATUS, ACTION_SET_FIELD_TO_TEXT, CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**[Pogledajte ceo obrazac →](api-integration-pattern.md)**

---

### 2. [Task Management Pattern](task-management-pattern.md)

**Složenost:** Niska-srednja | **Vreme podešavanja:** 30-45 minuta

Savladajte veštinu kreiranja, dodeljivanja, praćenja i upravljanja zadacima u okviru DocBits tokova rada za procese odobravanja i pregleda.

**Slučajevi upotrebe:**
- Kreiranje tokova rada za odobravanje
- Dodeljivanje zadataka pregleda korisnicima
- Rukovanje izuzecima koji zahtevaju ljudsku intervenciju
- Eskalacija problema menadžerima
- Kreiranje višenivovskih lanaca odobravanja
- Praćenje završetka zadataka i rokova

**Korišćene kartice:** tasks_create, ACTION_ASSIGN_TO_USER, ACTION_SEND_EMAIL_TO_GROUPS, CONDITION_TASK_STATUS

**[Pogledajte ceo obrazac →](task-management-pattern.md)**

---

### 3. [PO Matching Pattern](po-matching-pattern.md)

**Složenost:** Srednja-visoka | **Vreme podešavanja:** 60-90 minuta

Implementirajte sveobuhvatne tokove rada za uparivanje narudžbenica radi validacije faktura u odnosu na narudžbenice sa rutiranjem zasnovanim na toleranciji.

**Slučajevi upotrebe:**
- Validacija faktura u odnosu na narudžbenice
- Otkrivanje grešaka u cenama pre plaćanja
- Identifikacija neslaganja u količini
- Sprovođenje kontrola nabavke
- Sprečavanje duplih plaćanja
- Automatizacija trostrukog uparivanja

**Korišćene kartice:** PURCHASE_ORDER_FULL_MATCH, CONDITION_DOC_TO_PO_UNIT_PRICE, CONDITION_DOC_TO_PO_QUANTITY, CONDITION_DOC_TO_PO_TAX_LINES

**[Pogledajte ceo obrazac →](po-matching-pattern.md)**

---

### 4. [Decision Logic Pattern](decision-logic-pattern.md)

**Složenost:** Srednja | **Vreme podešavanja:** 30-45 minuta

Implementirajte složena stabla odlučivanja i logiku uslovnog rutiranja za obradu dokumenata kroz različite putanje na osnovu poslovnih pravila.

**Slučajevi upotrebe:**
- Rutiranje dokumenata po pragovima iznosa
- Primena različitih pravila za različite tipove dokumenata
- Implementacija logike višenivovskog odobravanja
- Rukovanje složenim poslovnim politikama
- Kreiranje dinamičkog rutiranja na osnovu više kriterijuma
- Implementacija matrica odobravanja

**Korišćene kartice:** CONDITION_DOC_FIELD_AMOUNT, CONDITION_DOC_TYPE_IS_ISNOT, CONDITION_SUPPLIER_STATUS_IS_ISNOT, ACTION_ASSIGN_TO_USER

**[Pogledajte ceo obrazac →](decision-logic-pattern.md)**

---

### 5. [Data Transformation Pattern](data-transformation-pattern.md)

**Složenost:** Srednja | **Vreme podešavanja:** 30-45 minuta

Transformišite, izračunavajte, formatirajte i obogaćujte podatke dokumenta da biste ih pripremili za izvoz, izvršili izračunavanja i standardizovali formate.

**Slučajevi upotrebe:**
- Izračunavanje ukupnih iznosa, međuzbirova, poreza
- Konverzija valuta ili jedinica
- Formatiranje datuma, brojeva, teksta
- Izvođenje vrednosti iz postojećih polja
- Obogaćivanje podataka iz eksternih izvora
- Standardizacija formata podataka
- Validacija izračunavanja

**Korišćene kartice:** ACTION_CALCULATE_FIELD, ACTION_SET_FIELD_TO_TEXT, ACTION_COPY_FIELD_VALUE, CALL_API, CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**[Pogledajte ceo obrazac →](data-transformation-pattern.md)**

---

## Vodič za izbor obrasca

### Po složenosti

| Složenost | Obrasci | Najbolje za |
|------------|----------|----------|
| **Niska-srednja** | [Task Management](task-management-pattern.md) | Početnici, jednostavni tokovi rada |
| **Srednja** | [API Integration](api-integration-pattern.md)<br>[Decision Logic](decision-logic-pattern.md)<br>[Data Transformation](data-transformation-pattern.md) | Korisnici srednjeg nivoa, standardni tokovi rada |
| **Srednja-visoka** | [PO Matching](po-matching-pattern.md) | Napredni korisnici, složena validacija |

---

### Po slučaju upotrebe

| Treba mi da... | Koristite ovaj obrazac |
|--------------|------------------|
| Integrišem sa eksternim sistemima | [API Integration Pattern](api-integration-pattern.md) |
| Kreiram tokove rada za odobravanje | [Task Management Pattern](task-management-pattern.md) |
| Validiram u odnosu na narudžbenice | [PO Matching Pattern](po-matching-pattern.md) |
| Rutiram na osnovu uslova | [Decision Logic Pattern](decision-logic-pattern.md) |
| Izračunavam i transformišem podatke | [Data Transformation Pattern](data-transformation-pattern.md) |

---

### Po industriji/odeljenju

| Industrija/odeljenje | Preporučeni obrasci |
|---------------------|---------------------|
| **Finansije/računovodstvo** | [PO Matching](po-matching-pattern.md), [Task Management](task-management-pattern.md), [Data Transformation](data-transformation-pattern.md) |
| **Nabavka** | [PO Matching](po-matching-pattern.md), [Decision Logic](decision-logic-pattern.md), [API Integration](api-integration-pattern.md) |
| **Operacije** | [Task Management](task-management-pattern.md), [Decision Logic](decision-logic-pattern.md) |
| **IT/Integracija** | [API Integration](api-integration-pattern.md), [Data Transformation](data-transformation-pattern.md) |
| **Sva odeljenja** | [Decision Logic](decision-logic-pattern.md), [Task Management](task-management-pattern.md) |

---

## Kako koristiti ove obrasce

### Korak 1: Izaberite obrazac

1. Pregledajte opise obrazaca iznad
2. Identifikujte koji obrazac odgovara vašem slučaju upotrebe
3. Proverite složenost i procenjeno vreme podešavanja
4. Pregledajte odeljak „Kada koristiti" u vodiču za obrazac

### Korak 2: Pregledajte preduslove

Svaki vodič za obrazac navodi:
- Potrebno znanje
- Povezane vodiče koje treba prvo pročitati
- Kartice koje će se koristiti
- Zahteve za konfiguraciju

### Korak 3: Pratite uputstva korak po korak

Svaki obrazac pruža:
- Kompletan primer toka rada
- Vodič za implementaciju korak po korak
- Šablone za konfiguraciju
- Primere iz stvarnog sveta
- Savete za rešavanje problema

### Korak 4: Prilagodite svojim potrebama

- Prilagodite primer svojim poslovnim pravilima
- Podesite pragove i tolerancije
- Izmenite logiku rutiranja
- Dodajte/uklonite korake po potrebi
- Temeljno testirajte pre upotrebe u produkciji

### Korak 5: Pratite i optimizujte

- Pratite performanse toka rada
- Pratite stope uspeha
- Prikupljajte povratne informacije korisnika
- Doterujte konfiguraciju
- Dokumentujte prilagođavanja

---

## Kombinacije obrazaca

Mnogi scenariji iz stvarnog sveta zahtevaju kombinovanje više obrazaca:

### Primer 1: Kompletna obrada faktura

```
1. API Integration Pattern → Fetch current pricing
2. Data Transformation Pattern → Calculate totals
3. PO Matching Pattern → Validate against PO
4. Decision Logic Pattern → Route based on variance
5. Task Management Pattern → Create approval tasks
```

### Primer 2: Odobravanje faktura velike vrednosti

```
1. Data Transformation Pattern → Calculate amounts
2. Decision Logic Pattern → Check thresholds
3. Task Management Pattern → Multi-level approval
4. API Integration Pattern → Notify external systems
```

### Primer 3: Rukovanje izuzecima

```
1. PO Matching Pattern → Detect variances
2. Decision Logic Pattern → Classify exception severity
3. Task Management Pattern → Create review tasks
4. Data Transformation Pattern → Calculate impact
```

---

## Šabloni obrazaca

Svaki obrazac uključuje ove standardizovane odeljke:

1. **Pregled** - Šta obrazac radi
2. **Kada koristiti** - Odgovarajući slučajevi upotrebe
3. **Kompletan primer** - Scenario iz stvarnog sveta
4. **Korak po korak** - Uputstva za implementaciju
5. **Konfiguracija** - Šabloni za podešavanje kartica
6. **Dijagram toka rada** - Vizuelni prikaz
7. **Napredne varijacije** - Alternativne implementacije
8. **Rukovanje greškama** - Uobičajeni problemi i rešenja
9. **Lista za proveru testiranja** - Koraci validacije
10. **Povezani obrasci** - Komplementarni obrasci
11. **Povezani vodiči** - Referentna dokumentacija

---

## Dobijanje pomoći

### Resursi za podršku obrascima

**Dokumentacija:**
- [Kompletan indeks vodiča za tokove rada](../README.md)
- [Vodiči za pojedinačne kartice](../then/action/)
- [Referenca za uslovne kartice](../and/condition-cards-complete-guide.md)
- [Mapa povezivanja tokova rada](../../../../WORKFLOW_LINKING_MAP.md)

**Dodatni resursi:**
- [Vodič za brzu referencu](../../../../WORKFLOW_LINKING_QUICK_REFERENCE.md)
- [Napomene o izdanju za oktobar 2025.](../changelog/2025-10-october.md)
- [Referenca za verzionisanje kartica](../../../docs/card_version.md)

**Kontakt:**
- Povratne informacije o obrascima: docs@docbits.com
- Tehnička podrška: support@docbits.com
- Pomoć pri implementaciji: consulting@docbits.com

---

## Statistika obrazaca

| Metrika | Vrednost |
|--------|-------|
| **Ukupno obrazaca** | 5 |
| **Ukupno pokrivenih kartica** | 30+ |
| **Kombinovana dokumentacija** | ~1.200 linija |
| **Primeri scenarija** | 25+ |
| **Šabloni za konfiguraciju** | 15+ |
| **Dijagrami tokova rada** | 5 kompletnih dijagrama |
| **Unakrsne reference** | 87+ internih veza |

---

## Doprinos obrascima

Imate obrazac toka rada koji bi mogao koristiti drugima?

**Smernice za doprinos obrascima:**

1. **Dokumentujte svoj tok rada**
   - Jasan poslovni scenario
   - Implementacija korak po korak
   - Funkcionalni primeri konfiguracije
   - Rezultati testiranja iz stvarnog sveta

2. **Pratite šablon obrasca**
   - Koristite standardnu strukturu odeljaka
   - Uključite sve potrebne elemente
   - Obezbedite dijagrame/primere
   - Dodajte vodič za rešavanje problema

3. **Pošaljite na pregled**
   - Pošaljite e-poštu na: docs@docbits.com
   - Uključite: Opis obrasca, slučajeve upotrebe, vodič za implementaciju
   - Pregledaćemo i potencijalno dodati u zvaničnu dokumentaciju

**Prednosti:**
- Pomozite drugim DocBits korisnicima
- Budite prepoznati u dokumentaciji
- Poboljšajte celokupnu bazu znanja o proizvodu
- Dobijte povratne informacije o svojoj implementaciji

---

## Dnevnik promena

### Verzija 1.0 (23. oktobar 2025.)
- Inicijalno izdanje 5 sveobuhvatnih obrazaca toka rada
- Dodat API Integration Pattern
- Dodat Task Management Pattern
- Dodat PO Matching Pattern
- Dodat Decision Logic Pattern
- Dodat Data Transformation Pattern
- Implementirano unakrsno referentno povezivanje (87 veza)
- Kreiran vodič za izbor obrasca

---

## Sledeći koraci

**Novi ste u obrascima toka rada?**
1. Počnite sa [Task Management Pattern](task-management-pattern.md) - najlakši za razumevanje
2. Pregledajte [Decision Logic Pattern](decision-logic-pattern.md) - temeljni za sve tokove rada
3. Istražite [API Integration Pattern](api-integration-pattern.md) - česta potreba za integracijom

**Spremni za implementaciju?**
1. Izaberite svoj obrazac sa liste iznad
2. Pročitajte kompletan vodič za obrazac
3. Pregledajte preduslove i povezane vodiče
4. Pratite uputstva korak po korak
5. Testirajte sa uzorcima dokumenata
6. Postavite u produkciju
7. Pratite i optimizujte

**Treba vam više pomoći?**
- Pregledajte [Pregled dokumentacije tokova rada](../README.md)
- Proverite [Vodič za brzu referencu](../../../../WORKFLOW_LINKING_QUICK_REFERENCE.md)
- Kontaktirajte tim za podršku

---

**Poslednje ažuriranje:** 23. oktobar 2025.
**Održava:** Tim za dokumentaciju
**Verzija:** 1.0
