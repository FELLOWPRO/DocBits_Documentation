# Card Versioning System - October 2025 Update

**Dokument:** Pregled verzionisanja kartica radnog toka
**Last Updated:** October 23, 2025
**Status:** Kompletno

---

## Pregled

DocBits Workflow Engine koristi **verzionisanje zasnovano na celim brojevima** za upravljanje evolucijom kartica uz održavanje povratne kompatibilnosti. Ovaj dokument pruža pregled sistema verzionisanja.

---

## Šta je verzionisanje kartica?

### Koncept
Svaka kartica radnog toka može imati više verzija, što sistemu omogućava da:
- Dodaje nove funkcije bez narušavanja postojećih radnih tokova
- Podržava zastarelu funkcionalnost dok je postepeno ukida
- Razvija mogućnosti kartica tokom vremena
- Održava povratnu kompatibilnost

### Struktura verzije
- **Format:** Celobrojne vrednosti (1, 2, 3, 4, 5...)
- **Identifikacija:** Složeni ključ od (card_type, card_version)
- **Status:** Svaka verzija ima oznake deprecated/enabled

### Primer
Kartica `tasks_create` evoluirala je kroz 4 verzije:
- **v1:** Originalno kreiranje zadatka (zastarelo)
- **v2:** Dodata podrška za prevod (zastarelo)
- **v3:** Eksperimentalna podrška za stablo odlučivanja (zastarelo)
- **v4:** Podrška za generički tip radne stavke (trenutno aktivno)

---

## Ključna statistika

### Pregled verzionisanja
| Metric | Value |
|--------|-------|
| **Cards with Multiple Versions** | 30+ |
| **Total Version Records** | 90+ |
| **Versions per Card (average)** | 3 |
| **Maximum Versions** | 5 (CONDITION_DOC_TO_PO_UNIT_PRICE) |
| **Deprecated Versions** | 9 |
| **Fully Disabled Cards** | 2 |

### Raspodela verzija
- **2 Versions:** 14 kartica (jednostavnija evolucija)
- **3 Versions:** 11 kartica (umerena evolucija)
- **4 Versions:** 4 kartice (značajna evolucija)
- **5 Versions:** 1 kartica (najrazvijenija: CONDITION_DOC_TO_PO_UNIT_PRICE)

---

## Uobičajeni obrasci verzija

### Obrazac 1: Usvajanje ključeva za prevod (v1 → v2)

**Pogođeno:** 15+ kartica

**Promena:**
```
v1: Plain text: "Call Api: [param] with method: [param]"
v2: With i18n: "trnsl_%call_api trnsl_be_% Call Api: [param]..."
```

**Svrha:** Omogućavanje višejezičke podrške

**Kartice:** CALL_API, RUN_WORKFLOW, APPROVE, REJECT, CALC_COLUMNS i druge

**Migracija:** Bezbedno - bez funkcionalnih promena

---

### Obrazac 2: Integracija stabla odlučivanja (v2 → v3)

**Pogođeno:** 5 kartica

**Promena:** Dodavanje parametra stabla odlučivanja

```
v2: Create a new Task with title: [param], description: [param]...
v3: (same as v2) + "Use decision tree, if available: [param]"
```

**Svrha:** Podrška za rezultate tabele odlučivanja

**Kartice:**
- tasks_create (v3 zastarelo)
- ACTION_TASK_FOR_GROUP (v3 zastarelo)
- DOC_USER_ASSIGN (v3 zastarelo)
- DOC_GROUP_ASSIGN (v3 zastarelo)
- ACTION_DECISION_TREE_CREATE_TASKS

**Status:** Zastarelo - pristup sa stablom odlučivanja bio je eksperimentalan

---

### Obrazac 3: Evolucija generičkog tipa (v3 → v4)

**Pogođeno:** 4 kartice

**Promena:** "Task" postaje fleksibilan tip radne stavke

```
v3: Create a new Task with the title: [param]
v4: Create a new [param] with the title: [param]
```

**Svrha:** Podrška za Tasks, Tickets, Issues i druge tipove radnih stavki

**Kartice:**
- tasks_create (v4 trenutno)
- ACTION_TASK_FOR_GROUP (v4 trenutno)
- ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP (v3 trenutno)
- ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK (v3 trenutno)

**Trenutni status:** Aktivno i preporučeno

---

### Obrazac 4: Parametri tolerancije (PO kartice)

**Pogođeno:** 6 PO kartica za poređenje

**Promena:** Dodavanje podrške za toleranciju/odstupanje

```
v2: Document value [operator] Purchase Order value
v3+: Document value [operator] PO value with tolerance [amount] [unit]
```

**Svrha:** Dozvoljavanje prihvatljivog odstupanja u podudaranju (npr. razlika u ceni od 2% je u redu)

**Ključne kartice:**
- CONDITION_DOC_TO_PO_UNIT_PRICE (evoluiralo do v5 sa tolerancijom)
- CONDITION_DATES_OPERATOR_OC_LINE_ITEMS (v2 → v3)
- CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY

**Korist:** Realističniji kriterijumi podudaranja

---

### Obrazac 5: Parametri režima poređenja

**Pogođeno:** 3 PO kartice za poređenje

**Promena:** Podrška za različite algoritme poređenja

```
v3: Standard comparison logic
v4: Same logic + "Compare as [param]" parameter
```

**Svrha:** Fleksibilne metode poređenja

**Kartice:**
- COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE (v2-4)
- CONDITION_OC_TO_PO_ITEMS (v3-4)
- CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY (v3-4)

---

### Obrazac 6: Okidači radnog toka

**Pogođeno:** samo STAUS_CHANGE

**Promena:** Automatsko pokretanje radnih tokova pri promeni statusa

```
v2: Change Status to [param]
v3: Change Status to [param], trigger Workflows [param]
```

**Svrha:** Kaskadno prosleđivanje promena statusa kroz radne tokove

---

## Najrazvijenije kartice

### 1. CONDITION_DOC_TO_PO_UNIT_PRICE (5 verzija)

**Putanja evolucije:** v2 → v3 → v4 → v5

- **v2:** Osnovno poređenje jedinične cene
- **v3:** Isti ključ za prevod (v2)
- **v4:** Dodat parametar režima poređenja
- **v5:** Dodat parametar praga tolerancije

**Trenutno:** v5 (sa podrškom za toleranciju)

---

### 2. CONDITION_OC_TO_PO_ITEMS (4 verzije)

**Putanja evolucije:** v1 → v2 → v3 → v4

- **v1:** Osnovno podudaranje stavki (zastarelo)
- **v2:** Dodat parametar metode poređenja
- **v3:** Poboljšano ključevima za prevod
- **v4:** Dodat parametar režima poređenja

**Trenutno:** v4

**Izbegavajte:** v1 (zastarelo)

---

### 3. tasks_create (4 verzije)

**Putanja evolucije:** v1 → v2 → v3 → v4

- **v1:** Originalna implementacija (zastarelo)
- **v2:** Dodata podrška za prevod (zastarelo)
- **v3:** Dodato stablo odlučivanja (zastarelo)
- **v4:** Generički tipovi radnih stavki (trenutno)

**Trenutno:** v4 (preporučeno)

**Vremenska linija:**
```
v1 → deprecated (old)
  → v2 → deprecated (translation added)
    → v3 → deprecated (decision tree experiment)
      → v4 → CURRENT & ACTIVE
```

---

## Status zastarelosti

### Potpuno zastarele verzije (Ne koristiti)

| Card | Version | Reason | Alternative |
|------|---------|--------|-------------|
| tasks_create | v1 | Veoma staro | Koristite v4 |
| tasks_create | v3 | Stablo odlučivanja zastarelo | Koristite v4 |
| ACTION_TASK_FOR_GROUP | v3 | Stablo odlučivanja zastarelo | Koristite v4 |
| DOC_USER_ASSIGN | v3 | Stablo odlučivanja zastarelo | Koristite v2 |
| DOC_GROUP_ASSIGN | v3 | Stablo odlučivanja zastarelo | Koristite v2 |
| CONDITION_DOC_TYPE_IS_ISNOT | v1 | Veoma staro | Koristite v2 |
| CONDITION_OC_TO_PO_ITEMS | v1 | Veoma staro | Koristite v4 |
| ACTION_RUN_DOCOPERATOR_SCRIPT | v4 | Funkcije vraćene | Koristite v3 |

### Potpuno onemogućene kartice (Ne mogu se koristiti)

| Card | Versions | Notes |
|------|----------|-------|
| DOC_SUBORG_CHANGE | v1, v2 | Nepodržana funkcionalnost |
| RUN_SCRIPT | v2, v3 | Zamenjeno sa ACTION_RUN_DOCOPERATOR_SCRIPT |

---

## Preporuke za verzije

### Po slučaju upotrebe

**Kreiranje novog radnog toka:**
- Uvek koristite **najviši omogućeni broj verzije**
- Pruža najnovije funkcije i poboljšanja
- Podržano i dokumentovano

**Održavanje postojećeg radnog toka:**
- Nastavite da koristite trenutnu verziju ako radi
- Planirajte migraciju kada je izvodljivo
- Nema hitne potrebe za nadogradnjom

**Migracija starog radnog toka:**
- Identifikujte verziju koja se trenutno koristi
- Planirajte putanju nadogradnje
- Temeljno testirajte pre postavljanja

---

## Kako verzije rade

### Izbor verzije
Prilikom kreiranja radnog toka, birate koju verziju kartice ćete koristiti. Primer:
- Koristite `tasks_create v4` za kreiranje novih zadataka (preporučeno)
- Koristite `tasks_create v2` ako stari sistemi to zahtevaju (starije, ali radi)
- NEMOJTE koristiti `tasks_create v1` (zastarelo)

### Povratna kompatibilnost
- Novije verzije ne narušavaju starije radne tokove
- Stari radni tokovi nastavljaju da rade sa svojom originalnom verzijom
- Radne tokove možete postepeno nadograđivati

### Tehnička implementacija
Verzije se upravljaju na nivou baze podataka:
```
card_templates table (PostgreSQL)
- card_type: Identifies the card (e.g., "tasks_create")
- card_version: Version number (e.g., 2, 3, 4)
- deprecated: Boolean flag
- enabled: Boolean flag
- text: Card description/parameters
```

---

## Za potrebe dokumentacije

### Razumevanje informacija o verziji
Kada vidite „Card v3“ u dokumentaciji:
- Odnosi se na verziju 3 te konkretne kartice
- Proverite [Full Versioning Reference](../../docs/card_version.md) za detalje
- Proverite koja se verzija preporučuje

### Provera vaše verzije
Da biste znali koju verziju koristite:
1. Otvorite karticu u svom radnom toku
2. Proverite prikazani broj verzije
3. Uporedite sa preporukama u vodičima

### Vremenska linija evolucije verzija
- **2024-2025:** Kontinuirana evolucija
- **October 2025:** Kompletna dokumentacija verzionisanja
- **Future:** Kontinuirana poboljšanja

---

## Povezana dokumentacija

### Sveobuhvatna referenca
→ [Full Card Versioning Reference](../../docs/card_version.md)

Uključuje:
- Svih 30+ kartica sa verzijama
- Detaljnu evoluciju teksta za svaku
- Specifične promene parametara
- SQL upite za pretragu verzija

### Vodiči specifični za kartice
→ [Workflow Guides](../)

Dokumentacija za svaku karticu sa preporukama za verzije

### Detalji istorije verzija
Svaki vodič uključuje informacije o verziji i napomene o migraciji

---

## Brza referenca

### Kartice sa najviše verzija
1. CONDITION_DOC_TO_PO_UNIT_PRICE - 5 verzija
2. CONDITION_OC_TO_PO_ITEMS - 4 verzije
3. tasks_create - 4 verzije
4. COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE - 3 verzije
5. CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY - 4 verzije

### Najčešći obrazac evolucije
**Usvajanje ključeva za prevod (v1 → v2)** - 15+ kartica

### Najznačajnija promena
**Evolucija generičkog tipa (v3 → v4)** - Promenjeno iz „Task“ u fleksibilan tip radne stavke

### Potpuno onemogućeno
- DOC_SUBORG_CHANGE
- RUN_SCRIPT

---

## Često postavljana pitanja

### P: Koju verziju treba da koristim?
O: Koristite **najvišu omogućenu verziju** osim ako nemate specifičan razlog da koristite stariju verziju.

### P: Mogu li da nadogradim svoj radni tok na noviju verziju?
O: Da, ali temeljno testirajte. Neke verzije imaju različite zahteve za parametre.

### P: Šta se dešava ako koristim zastarelu verziju?
O: Nastavlja da radi, ali nećete dobiti nove funkcije. Preporučuje se migracija.

### P: Mogu li da koristim onemogućenu karticu?
O: Ne, onemogućene kartice se ne mogu koristiti. Umesto toga koristite preporučenu alternativu.

### P: Kako da znam da li moja kartica zahteva nadogradnju?
O: Proverite [Full Versioning Reference](../../docs/card_version.md) za vaš tip kartice i pratite preporuke.

---

## Najbolje prakse

1. **Novi radni tokovi:** Koristite najnoviju stabilnu verziju
2. **Ažuriranja:** Periodično proveravajte nove verzije
3. **Testiranje:** Prvo testirajte nadogradnje verzija u sandbox-u
4. **Dokumentacija:** Pogledajte vodiče specifične za kartice radi detalja o verziji
5. **Migracija:** Planirajte nadogradnje postepeno
6. **Podrška:** Kontaktirajte podršku ako se pojave pitanja o kompatibilnosti verzija

---

## Tabela rezimea

| Card Type | Current Version | Total Versions | Status | Notes |
|-----------|-----------------|----------------|--------|-------|
| tasks_create | 4 | 4 | Active | Najrazvijenije; v3 zastarelo |
| CONDITION_DOC_TO_PO_UNIT_PRICE | 5 | 4 | Active | Najveći broj verzija |
| CONDITION_OC_TO_PO_ITEMS | 4 | 4 | Active | v1 zastarelo |
| ACTION_TASK_FOR_GROUP | 4 | 3 | Active | v3 zastarelo |
| ACTION_RUN_DOCOPERATOR_SCRIPT | 3 | 3 | Active | v4 zastarelo/onemogućeno |
| Most cards | 2 | 2 | Active | obrazac v1 → v2 |

---

## Pogledajte i

- 📖 [Full Card Versioning Reference](../../docs/card_version.md)
- 🔗 [Workflow Guides](../)
- 📋 [October 2025 Release Notes](./2025-10-october.md)
- 🔄 [Workflow Linking Analysis](../../WORKFLOW_LINKING_MAP.md)

---

**Last Updated:** October 23, 2025
**Source:** postgres-dev-docflow database
**Status:** Complete Reference
