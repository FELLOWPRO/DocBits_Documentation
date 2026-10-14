# Supplier BOD Mapping

Deze pagina documenteert hoe DocBits leveranciers-stamgegevens uit Infor M3 inleest via de BODs `SyncSupplierPartyMaster` en `SyncRemitToPartyMaster`. Beide BODs vullen dezelfde `SUPPLIER`-stamgegevenstabel in DocBits.

{% file src="../../../../.gitbook/assets/Sync.SupplierPartyMaster.pdf" %}
SupplierPartyMaster — Oorspronkelijke BOD mapping referentie (PDF)
{% endfile %}

{% file src="../../../../.gitbook/assets/Sync.RemitToPartyMaster.pdf" %}
RemitToPartyMaster — Oorspronkelijke BOD mapping referentie (PDF)
{% endfile %}

## Kernprincipes

- **CONO + SUNO is de match-key.** Een rij `supplier_header` in DocBits wordt uniek geïdentificeerd door `(customer_number = sharedCONO, supplier_number = sharedSUNO)`. Hierdoor kan één DocBits-organisatie meerdere M3-bedrijven consolideren.
- **`variationID` beschermt tegen BODs in verkeerde volgorde.** M3 kan dezelfde stamgegevensrecord meerdere keren snel achter elkaar emitteren; de binnenkomende `variationID` moet groter zijn dan de opgeslagen waarde voordat een update wordt geaccepteerd. Beide BODs tracken hun `variationID` onafhankelijk (`variation_id_supplier_bod`, `variation_id_remit_to_party`).
- **Geen stille overschrijving.** SupplierPartyMaster en RemitToPartyMaster delen meerdere velden (naam, telefoon, btw-nummer, bank, status). Elke BOD werkt alleen de velden bij die hij bezit en alleen wanneer zijn `variationID` toeneemt. Binnen de gedeelde set wint de meest recent ontvangen BOD (per BOD-type).
- **Multi-bank-sync is preference-gestuurd.** Standaardgedrag: de laatste `FinancialParty` wordt naar `bank_id` op de header geschreven. Met preference `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` ingeschakeld wordt elke `FinancialParty`-entry in `supplier_account` opgeslagen (IBAN, rekening-ID, valutacode, preference-indicator).
- **Optioneel CONO-suffix-trimmen.** Sommige M3-installaties voegen een divisie-suffix toe aan het bedrijfsnummer (bv. `100_01`). De preference `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` knipt achtervoegsels `_*` af om de DocBits-sleutels consistent te houden. Let op: met het trimmen ingeschakeld vallen meerdere per-divisie geëmitteerde RemitToPartyMaster-BODs op één match-key — en wint de BOD met de hoogste `variationID`. Zie de FAQ "*Wat gebeurt er als per divisie een RemitToPartyMaster-BOD wordt verzonden?*" hieronder.

## Sync.SupplierPartyMaster

→ DocBits Stamgegevenstabel: **SUPPLIER**

```python
header_mappings = {
            "sharedCONO": "//DataArea/Sync/AccountingEntityID",
            "sharedSUNO": "//SupplierPartyMaster/PartyIDs/ID",
            "variationID": "//SupplierPartyMaster/PartyIDs/ID/@variationID",
            "supplierName": "//SupplierPartyMaster/Name",
            "phone": '//Communication[ChannelCode="Phone"]/DialNumber',
            "vatNo": "//SupplierPartyMaster/PartyIDs/TaxID",
            "paymentTermId": "//SupplierPartyMaster/PaymentTermID",
            "paymentMethodCode": "//SupplierPartyMaster/PaymentMethodCode",
            "buyerPersonReferenceId": "//SupplierPartyMaster/BuyerPersonReference/IDs/ID",
            "buyerPersonReference": "//SupplierPartyMaster/BuyerPersonReference/Name",
            "supplier_category": "//SupplierPartyMaster/Classification/Codes/Code[@listID='Supplier Categories']",
            "supplier_group": "//SupplierPartyMaster/Classification/Codes/Code[@listID='Supplier Group']",
            "discount_terms_description": "//SupplierPartyMaster/UserArea/Property/NameValue[@name='eam.UDFCHAR06']",
            "status": "//SupplierPartyMaster/Status/Code",
            "bank_id": "//SupplierPartyMaster/FinancialParty[last()]/FinancialAccount/ID",
        }
```

### Veld-referentie

| DocBits veld | M3 bron | Beschrijving |
|---|---|---|
| `sharedCONO` | M3 bedrijfsnummer | Mapt naar `customer_number` in `supplier_header`. Onderdeel van de match-key. |
| `sharedSUNO` | `CIDMAS.IDSUNO` | M3 leveranciersnummer. Onderdeel van de match-key. |
| `variationID` | BOD-attribuut | Opgeslagen als `variation_id_supplier_bod`. Binnenkomende BODs worden alleen geaccepteerd als hun `variationID` de opgeslagen waarde overstijgt. Een ontbrekend attribuut wordt behandeld als `0` (force-update). |
| `supplierName` | `CIDMAS.IDSUNM` | Weergavenaam van de leverancier. |
| `phone` | `CIDMAS.PHNO/PHN2/IDTFNO` | Telefoonnummer uit het `Phone`-communicatiekanaal. |
| `vatNo` | `CIDMAS.IDVRNO` | Btw-identificatie. Gelezen uit `PartyIDs/TaxID` (geen `@schemeName`-filter in het M3-ingestiepad). **OPEN** — wanneer M3 meerdere `TaxID`-elementen met verschillende `@schemeName`-waarden emitteert (bv. `VatCode`, `TaxIdentificationNumber`), wint het eerste voorkomen. Een configureerbare `schemeName`-filter is gepland; deel een voorbeeld-BOD zodat we de juiste default kunnen vastleggen. <!-- tracked in DOCB-12313 --> |
| `paymentTermId` | `CIDVEN.IITEPY` | Identifier van betalingsvoorwaarden. |
| `paymentMethodCode` | — | Betalingsmethodecode, indien aangeleverd. |
| `buyerPersonReferenceId` / `buyerPersonReference` | `CIDVEN.IIBUYE` / `CSYUSR.CRRENM` | Toegewezen inkoper (M3-gebruikersreferentie en weergavenaam). |
| `supplier_category` | — | Gelezen uit `Classification/Codes/Code[@listID='Supplier Categories']`. Optionele UserArea-uitbreiding; blijft NULL bij standaard M3-installaties. |
| `supplier_group` | `CIDVEN.IISUCL` | Classificatiegroep van de leverancier. |
| `discount_terms_description` | — | Optionele UserArea-uitbreiding (`eam.UDFCHAR06`) gebruikt door de kortingsdatum-rekenmodule van DocBits. Wanneer de leverancier hier een kortingsdagenwaarde aanlevert, combineert DocBits deze met de factuurdatum tot een kortingsvervaldatum voor het AP-team. |
| `status` | `CIDMAS.IDSTAT` | Actief/inactief-status van de leverancier, uit `SupplierPartyMaster/Status/Code`. |
| `bank_id` | `CBANAC.BCBKNO` | Standaard bankrekening, uit de *laatste* `FinancialParty`. Schakel `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` in om elke `FinancialParty` in de `supplier_account`-tabel te synchroniseren. |

## Sync.RemitToPartyMaster

→ DocBits Stamgegevenstabel: **SUPPLIER**

```python
header_mappings = {
            "sharedCONO": "//DataArea/Sync/AccountingEntityID",
            "sharedSUNO": "//RemitToPartyMaster/PartyIDs/ID",
            "variationID": "//RemitToPartyMaster/PartyIDs/ID/@variationID",
            "supplierName": "//RemitToPartyMaster/Name",
            "phone": '//Communication[ChannelCode="Phone"]/DialNumber',
            "vatNo": "//RemitToPartyMaster/PartyIDs/TaxID",
            "bank_id": "//RemitToPartyMaster/FinancialParty[last()]/FinancialAccount/ID",
            "status": "//RemitToPartyMaster/Status/Code",
        }
```

### Veld-referentie

| DocBits veld | M3 bron | Beschrijving |
|---|---|---|
| `sharedCONO` / `sharedSUNO` | M3-bedrijf / `CIDMAS.IDSUNO` | Zelfde semantiek als bij `SupplierPartyMaster`. Wordt aan dezelfde `supplier_header`-rij gekoppeld. |
| `variationID` | BOD-attribuut | Opgeslagen als `variation_id_remit_to_party` — onafhankelijk gevolgd van de SupplierPartyMaster-`variationID`. |
| `supplierName` | `CIDMAS.IDSUNM` | Weergavenaam van de remit-to-partij. Schrijft naar de gedeelde kolom `supplier_name`. |
| `phone` | `CIDREF.IRPHNO` | Telefoonnummer uit het remit-to-communicatieblok. |
| `vatNo` | `CIDMAS.IDCORG` | Btw-identificatie van de remit-to-partij. Dezelfde `@schemeName`-beperking als bij SupplierPartyMaster — het eerste voorkomen wint. <!-- tracked in DOCB-12313 --> |
| `bank_id` | `CBANAC.BCBKNO` | Remit-to bankrekening (`FinancialParty[last()]`). Zelfde multi-bank-preference geldt. |
| `status` | `CIDMAS.IDSTAT` | Actief/inactief-status van de remit-to-partij. |

## Hoe de twee BODs samenwerken op de gedeelde `SUPPLIER`-tabel

Beide BODs vullen dezelfde `supplier_header`-rij. Voor de gedeelde velden (`supplierName`, `phone`, `vatNo`, `bank_id`, `status`) past DocBits de volgende regels toe:

1. Match de rij via `(customer_number = sharedCONO, supplier_number = sharedSUNO)`.
2. Vergelijk de binnenkomende `variationID` met de opgeslagen `variationID` *voor hetzelfde BOD-type*.
3. Als de binnenkomende `variationID` groter is (of `0`, force-update), update dan de velden die deze BOD bezit. Anders verwerp de BOD.
4. De `variationID` van het andere BOD-type wordt niet aangeraakt; eerder opgeslagen waarden blijven behouden.

De `supplier_address`- en `supplier_account`-rijen worden bij een update verwijderd en opnieuw ingevoegd, zodat secundaire tabellen altijd de meest recente BOD weergeven. Dit heeft een neveneffect wanneer M3 een RemitToPartyMaster-BOD *per divisie* uitstuurt (sommige tenants doen dit wanneer bankverbindingen zowel op een lege divisie als op specifieke divisies worden bijgehouden): nadat `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` het divisie-suffix afsnijdt, richt elke per-divisie-BOD zich op dezelfde `(customer_number, supplier_number)`-key. De BOD met de hoogste `variationID` wint. Als die "winnende" BOD uit een divisie zonder bankverbindingen komt, worden de bankrekeningen van de vorige BOD bij het re-insert overschreven.

## Veelgestelde vragen

### Waarom volgt DocBits CONO als al mijn leveranciers uit één M3-bedrijf komen?

CONO-routering is verplicht omdat DocBits per ontwerp multi-tenant is: een organisatie kan BODs uit meerdere M3-bedrijven inleveren. CONO is onderdeel van de match-key zodat leveranciers van verschillende bedrijven niet botsen. Bij één bedrijf kun je de waarde negeren — de sleutelkolom wordt toch gevuld.

### Beide BODs schrijven naar dezelfde leveranciersrij — overschrijft de laatste BOD alles?

Nee. Elk BOD-type bezit alleen de velden die het verstuurt, en updates worden gestuurd door een onafhankelijke `variationID`. Een SupplierPartyMaster die alleen de leveranciersnaam wijzigt, draait het telefoonnummer dat een latere RemitToPartyMaster had geschreven, niet terug.

### `Supplier Categories` en `eam.UDFCHAR06` worden nooit door mijn M3 geleverd — wat te doen?

Beide zijn optionele UserArea-uitbreidingen. Zonder de uitbreiding blijven de kolommen NULL en geen DocBits-functie hangt ervan af. Schakel de kortingsdatumlogica alleen in als jouw M3 is geconfigureerd om `eam.UDFCHAR06` te emitteren.

### Moet `vatNo` filteren op `schemeName='TaxIdentificationNumber'`?

Het M3-BOD-ingestiepad leest momenteel `PartyIDs/TaxID` zonder `schemeName`-filter. Het filter wordt gebruikt in de e-factuur-XSLT-paden (Facturae, XRechnung, KSeF), niet in de M3-ingestie. Wanneer M3 meerdere `TaxID`-elementen met verschillende `@schemeName`-waarden emitteert, wint het eerste voorkomen — wat onjuiste btw-identificaties kan opleveren. Een configureerbaar filter is gepland; een voorbeeld-BOD uit jouw tenant helpt ons de juiste default-`schemeName` vast te leggen. <!-- tracked in DOCB-12313 -->

### Wat gebeurt er als per divisie een RemitToPartyMaster-BOD wordt verzonden?

Sommige M3-tenants houden bankverbindingen bij op zowel een lege divisie als op specifieke divisies, waardoor M3 per divisie een aparte RemitToPartyMaster-BOD uitstuurt. De match-key in DocBits is `(customer_number = sharedCONO, supplier_number = sharedSUNO)` — divisie maakt er geen deel van uit.

- Met preference `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` ingeschakeld vallen de per-divisie-BODs op dezelfde rij samen. De BOD met de hoogste `variationID` wint, en `supplier_account`-rijen worden alleen vanuit die BOD opnieuw ingevoegd. Als de winnende BOD uit een divisie zonder bankverbindingen komt, worden eerder opgeslagen bankrekeningen overschreven.
- Met de preference uitgeschakeld (de CONO behoudt zijn divisie-suffix) richten de per-divisie-BODs zich op verschillende keys en coëxisteren ze.

Als jouw tenant per-divisie RemitToPartyMaster-BODs verzendt en afhankelijk is van de geconsolideerde banklijst, neem contact met ons op met een voorbeeld zodat we een verbetering kunnen plannen.

### Ik wil elke leveranciers-bankrekening synchroniseren, niet alleen de laatste. Hoe?

Schakel de preference `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` in. Met de vlag aan wordt elke `FinancialParty` uit de BOD opgeslagen in de `supplier_account`-tabel (IBAN, financiële rekening-ID, valutacode, preference-indicator). De legacy-kolom `bank_id` op de header blijft de laatste entry behouden voor achterwaartse compatibiliteit.
