# Auto accounting

## Tabel `public.auto_accounting`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `supplier_name`: Leveranciersnaam
* `description`: intern
* `item_number`: intern
* `line_amount`: double precision
* `total_amount`: double precision
* `mapped_amount`: double precision
* `ledger_account`: intern
* `doc_id`: intern

### Analyse & beschrijving

## Technische documentatie voor de tabel `public.auto_accounting`

### Inleiding

De tabel `public.auto_accounting` lijkt bedoeld te zijn voor het beheren en opslaan van boekhoudgegevens met betrekking tot verschillende leveranciers en organisaties. De tabel legt informatie over financiële transacties vast, waaronder bedragen en grootboekrekeningen, die essentieel zijn voor financiële rapportage en analyse.

### Kolombeschrijvingen

#### id

* **Betekenis**: Een unieke identifier voor elk record in de tabel.
* **Rol**: Primaire sleutel.
* **Typische inhoud**: Een UUID-tekenreeks die elke vermelding uniek vertegenwoordigt.
* **Opmerking**: Zorgt ervoor dat elk record eenduidig kan worden geïdentificeerd.

#### org\_id

* **Betekenis**: Identifier van de organisatie die bij de boeking hoort.
* **Rol**: Refererende sleutel.
* **Typische inhoud**: Een UUID-tekenreeks die verwijst naar een organisatie in een bovenliggende tabel.
* **Opmerking**: Wordt gebruikt om boekingen aan specifieke organisaties te koppelen.

#### supplier\_name

* **Betekenis**: De naam van de leverancier die bij de transactie betrokken is.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Tekst die de naam van de leverancier weergeeft, zoals "Fellow Consulting AG".
* **Opmerking**: Geeft informatie over de leverancier die bij de transactie hoort.

#### description

* **Betekenis**: Een korte beschrijving van de transactie of het artikel.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Tekst die de transactie beschrijft, zoals de naam van een artikel ("apple" of "Peaches").
* **Opmerking**: Nuttig om de aard van de transactie te begrijpen.

#### item\_number

* **Betekenis**: Identifier voor een specifiek artikel dat bij de transactie betrokken is.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Kan een product- of SKU-identifier zijn, hoewel er geen voorbeeldgegevens beschikbaar zijn.
* **Opmerking**: Handig voor het volgen van of verwijzen naar specifieke artikelen.

#### line\_amount

* **Betekenis**: Het geldbedrag voor een specifieke regel in de transactie.
* **Rol**: Financieel veld.
* **Typische inhoud**: Een decimale waarde die het bedrag voor een afzonderlijke regel weergeeft.
* **Opmerking**: Belangrijk voor gedetailleerde financiële analyse op regelniveau.

#### total\_amount

* **Betekenis**: Het totale geldbedrag van de transactie.
* **Rol**: Financieel veld.
* **Typische inhoud**: Een decimale waarde die het totale transactiebedrag weergeeft.
* **Opmerking**: Vertegenwoordigt de som van alle regelbedragen in een transactie.

#### mapped\_amount

* **Betekenis**: Het bedrag dat aan een specifieke rekening is toegewezen of gekoppeld.
* **Rol**: Financieel veld.
* **Typische inhoud**: Een decimale waarde die aangeeft hoeveel van de transactie is toegewezen.
* **Opmerking**: Nuttig om te begrijpen hoe middelen over rekeningen zijn verdeeld.

#### ledger\_account

* **Betekenis**: Het rekeningnummer in het grootboek waarop de transactie wordt geboekt.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Tekst die een rekeningnummer weergeeft, zoals "2200" of "2500".
* **Opmerking**: Cruciaal voor de boekhouding om te volgen waar transacties worden geboekt.

#### doc\_id

* **Betekenis**: Een identifier voor een gerelateerd document of record.
* **Rol**: Refererende sleutel of verwijzing.
* **Typische inhoud**: Een UUID-tekenreeks of andere identifier die naar gerelateerde documenten verwijst.
* **Opmerking**: Helpt transacties aan specifieke documenten of records te koppelen voor traceerbaarheid.

Deze documentatie geeft een gedetailleerd overzicht van de tabel `public.auto_accounting` en beschrijft de structuur en het doel van elke kolom, zodat ontwikkelaars en databasebeheerders de gegevens effectief kunnen begrijpen en gebruiken.
