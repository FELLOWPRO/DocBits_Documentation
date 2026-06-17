# Infrastruktura

Stranica **Infrastruktura** pruža administratorima uvid u realnom vremenu u to gde se izvršava svaki deo DocBits-a (EU ili SAD), kako dokument prolazi kroz sistem i da li je pozadinska obrada ispravna. Stranica je samo za čitanje — ovde se ništa ne podešava; ona odgovara na pitanje: *„da li sve radi i da li moji podaci ostaju u mom regionu?"*

> **Pristup:** Infrastruktura je stranica isključivo za administratore. Otvorite **Podešavanja → Organizacija i Pristup → Infrastruktura**.

<figure><img src="../../.gitbook/assets/infrastructure_overview.png" alt="Stranica Infrastruktura sa otvorenom karticom Topologija"><figcaption><p>Stranica Infrastruktura, kartica Topologija</p></figcaption></figure>

Stranica je podeljena na tri kartice:

| Kartica | Odgovara na |
|---------|-------------|
| **Topologija** | Gde se izvršava svaka komponenta i da li je sve u mom regionu? |
| **Obrada** | Da li se koraci obrade (OCR, ekstrakcija, PO usklađivanje …) izvršavaju i da li su ažurni? |
| **Zakazani zadaci** | Da li se ponavljajući pozadinski zadaci izvršavaju po planu? |

## Topologija

Kartica Topologija prikazuje celu DocBits platformu kao dijagram, grupisan u slojeve — **Edge / Web**, **Core API**, **Uvoz**, **Pozadinski servisi**, **Skladišta podataka** i **Autentifikacija**. Svako polje je jedna komponenta (Veb aplikacija/CDN, API gateway, OCR worker, baza podataka i tako dalje).

<figure><img src="../../.gitbook/assets/infrastructure_topology.png" alt="Dijagram topologije sa oznakama regiona"><figcaption><p>Svaka komponenta je označena regionom u kojem se izvršava</p></figcaption></figure>

### Transparentnost regiona

Svaka komponenta nosi oznaku regiona, tako da na prvi pogled možete potvrditi gde se nalaze vaši podaci:

| Oznaka | Značenje |
|--------|----------|
| **EU ✓** / **US ✓** | Komponenta se izvršava u regionu vaše organizacije. |
| **SHARED** | Globalna komponenta (npr. CDN) bez jednog regiona — to je očekivano i nije problem. |
| **Neusklađenost regiona** | Komponenta se izvršava u *drugom* regionu nego vaša organizacija. Istaknuta je kako biste to mogli prijaviti podršci. |

Baner na vrhu sumira rezultat: **„Sve komponente se izvršavaju u vašem regionu (EU)"** kada se sve poklapa, ili upozorenje ako je neka kritična komponenta u drugom regionu.

### Arhitektura vs. Pusti proces

Koristite prekidač iznad dijagrama da promenite prikaz:

- **Arhitektura** — statička mapa svih komponenti i načina na koji su povezane.
- **Pusti proces** — animira putovanje dokumenta kroz sistem, korak po korak, tako da vidite redosled kojim su komponente uključene.

Indikator **● live** pokazuje da informacije o stanju na dijagramu odražavaju trenutno stanje sistema.

### Opcioni moduli

Komponente koje pripadaju opcionom modulu (Pretraga celog teksta, DocFlow, Auto-Accounting, DocNet, PO usklađivanje) prikazuju oznaku **aktiviran** ili **deaktiviran**. Klik na deaktiviran modul vodi vas direktno na stranicu na kojoj ga možete uključiti — **Podešavanja → Modul** za većinu modula, ili **Tipovi dokumenata** za PO usklađivanje (koje se uključuje po tipu dokumenta).

## Obrada

Kartica Obrada prikazuje tok obrade dokumenata za **vašu organizaciju** — kada je svaki korak poslednji put izvršen i da li posao teče ili se gomila.

<figure><img src="../../.gitbook/assets/infrastructure_processing.png" alt="Tabela obrade sa oznakama statusa"><figcaption><p>Status obrade po koraku za vašu organizaciju</p></figcaption></figure>

| Kolona | Opis |
|--------|------|
| **Proces** | Korak obrade — Obrada dokumenata, OCR, TR-OCR, Podela po barkodu, Ekstrakcija barkoda, Ekstrakcija, PO usklađivanje. |
| **Poslednje izvršavanje** | Pre koliko vremena je korak poslednji put izvršen. Pređite mišem za tačan vremenski žig. *„Nikada izvršeno"* znači da nijedan dokument još nije stigao do ovog koraka. |
| **Status** | Oznaka tipa semafora (vidi ispod). |

Oznake statusa:

| Oznaka | Značenje |
|--------|----------|
| **OK** (zeleno) | Nema skorašnjih grešaka i ničega na čekanju — korak je ispravan. |
| **U toku (N)** (žuto) | `N` dokumenata se trenutno obrađuje u ovom koraku. |
| **Greška (N)** (crveno) | `N` dokumenata je nedavno otkazalo u ovom koraku. |

Greške i *u toku* su nezavisni signali, pa korak može prikazati obe oznake istovremeno — tako vidite grešku i dok drugi posao još traje. Koristite **Osveži** (gore desno) da preuzmete najnovije brojeve.

## Zakazani zadaci

Kartica Zakazani zadaci navodi ponavljajuće pozadinske zadatke koji održavaju DocBits u radu (osvežavanja keša, upozorenja o statusu, isteci vremena dokumenata, odlazne sinhronizacije i drugo) i potvrđuje da se svaki pokreće na vreme.

<figure><img src="../../.gitbook/assets/infrastructure_scheduled.png" alt="Tabela zakazanih zadataka"><figcaption><p>Ponavljajući pozadinski zadaci i njihov status rasporeda</p></figcaption></figure>

| Kolona | Opis |
|--------|------|
| **Zadatak** | Naziv zakazanog zadatka. |
| **Poslednje izvršavanje** | Pre koliko vremena je poslednji put izvršen. Pređite mišem za tačan vremenski žig; *„Nikada izvršeno"* znači da se još nije pokrenuo. |
| **Status** | Status rasporeda (vidi ispod). |

Vrednosti statusa:

| Oznaka | Značenje |
|--------|----------|
| **Po rasporedu** (zeleno) | Zadatak se izvršava u očekivanom intervalu. |
| **Kasni** (crveno) | Zadatak nije izvršen kada je očekivano — vredi istražiti ili prijaviti podršci. |
| **Nepoznato** (sivo) | Status rasporeda nije bilo moguće utvrditi. |

Koristite **Osveži** da ponovo proverite status rasporeda po potrebi.
