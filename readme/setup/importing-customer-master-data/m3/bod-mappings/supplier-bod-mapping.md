# Supplier BOD Mapiranje

Ova stranica dokumentuje kako DocBits prima matične podatke dobavljača iz Infor M3 preko BOD-ova `SyncSupplierPartyMaster` i `SyncRemitToPartyMaster`. Oba BOD-a popunjavaju istu tabelu matičnih podataka `SUPPLIER` u DocBits-u.

{% file src="../../../../.gitbook/assets/Sync.SupplierPartyMaster.pdf" %}
SupplierPartyMaster — Originalna BOD referenca mapiranja (PDF)
{% endfile %}

{% file src="../../../../.gitbook/assets/Sync.RemitToPartyMaster.pdf" %}
RemitToPartyMaster — Originalna BOD referenca mapiranja (PDF)
{% endfile %}

## Ključni principi

- **CONO + SUNO je ključ podudaranja.** Red `supplier_header` u DocBits-u jedinstveno se identifikuje sa `(customer_number = sharedCONO, supplier_number = sharedSUNO)`. To omogućava jednoj DocBits organizaciji da konsoliduje više M3 kompanija.
- **`variationID` štiti od BOD-ova van redosleda.** M3 može emitovati isti matični zapis više puta u brzoj sukcesiji; dolazni `variationID` mora biti veći od sačuvanog da bi ažuriranje bilo prihvaćeno. Oba BOD-a prate svoj `variationID` nezavisno (`variation_id_supplier_bod`, `variation_id_remit_to_party`).
- **Bez tihog prepisivanja.** SupplierPartyMaster i RemitToPartyMaster dele nekoliko polja (ime, telefon, PDV, banka, status). Svaki BOD ažurira samo polja koja poseduje, i samo ako njegov `variationID` napreduje. Unutar deljenog skupa pobeđuje BOD primljen poslednji (po tipu BOD-a).
- **Sinhronizacija više banaka kontroliše se preko podešavanja.** Podrazumevano ponašanje: poslednji `FinancialParty` se upisuje u `bank_id` u zaglavlju. Sa uključenom postavkom `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC`, svaki unos `FinancialParty` se čuva u `supplier_account` (IBAN, ID računa, kod valute, indikator preference).
- **Opciono uklanjanje CONO sufiksa.** Neke M3 instalacije dodaju sufiks divizije na broj kompanije (npr. `100_01`). Postavka `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` uklanja `_*` sufikse kako bi DocBits ključevi ostali dosledni.

## Sync.SupplierPartyMaster

→ DocBits Tabela Matičnih Podataka: **SUPPLIER**

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

### Referenca polja

| DocBits polje | M3 izvor | Opis |
|---|---|---|
| `sharedCONO` | M3 broj kompanije | Mapira se na `customer_number` u `supplier_header`. Deo ključa podudaranja. |
| `sharedSUNO` | `CIDMAS.IDSUNO` | M3 broj dobavljača. Deo ključa podudaranja. |
| `variationID` | Atribut BOD-a | Čuva se kao `variation_id_supplier_bod`. Dolazni BOD-ovi se prihvataju samo ako njihov `variationID` premaši sačuvanu vrednost. Nedostajući atribut tretira se kao `0` (force-update). |
| `supplierName` | `CIDMAS.IDSUNM` | Prikazno ime dobavljača. |
| `phone` | `CIDMAS.PHNO/PHN2/IDTFNO` | Broj telefona iz komunikacionog kanala `Phone`. |
| `vatNo` | `CIDMAS.IDVRNO` | PDV identifikator. Čita se iz `PartyIDs/TaxID` (bez `@schemeName` filtera na M3 putanji unosa). |
| `paymentTermId` | `CIDVEN.IITEPY` | Identifikator uslova plaćanja. |
| `paymentMethodCode` | — | Kod načina plaćanja, kada je dostavljen. |
| `buyerPersonReferenceId` / `buyerPersonReference` | `CIDVEN.IIBUYE` / `CSYUSR.CRRENM` | Dodeljen kupac (M3 referenca korisnika i prikazno ime). |
| `supplier_category` | — | Čita se iz `Classification/Codes/Code[@listID='Supplier Categories']`. Opcionalno UserArea proširenje; ostaje NULL na standardnim M3 instalacijama. |
| `supplier_group` | `CIDVEN.IISUCL` | Grupa klasifikacije dobavljača. |
| `discount_terms_description` | — | Opcionalno UserArea proširenje (`eam.UDFCHAR06`) koje koristi DocBits-ov kalkulator datuma popusta. Kada dobavljač ovde isporuči vrednost dana popusta, DocBits je kombinuje sa datumom fakture kako bi proizveo datum dospeća popusta za AP tim. |
| `status` | `CIDMAS.IDSTAT` | Aktivan/neaktivan status dobavljača, uzet iz `SupplierPartyMaster/Status/Code`. |
| `bank_id` | `CBANAC.BCBKNO` | Podrazumevani bankovni račun, uzet iz *poslednje* `FinancialParty`. Omogućite `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` da biste sinhronizovali svaki `FinancialParty` u tabelu `supplier_account`. |

## Sync.RemitToPartyMaster

→ DocBits Tabela Matičnih Podataka: **SUPPLIER**

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

### Referenca polja

| DocBits polje | M3 izvor | Opis |
|---|---|---|
| `sharedCONO` / `sharedSUNO` | M3 kompanija / `CIDMAS.IDSUNO` | Ista semantika kao u `SupplierPartyMaster`. Pridružuje se istom redu `supplier_header`. |
| `variationID` | Atribut BOD-a | Čuva se kao `variation_id_remit_to_party` — prati se nezavisno od SupplierPartyMaster `variationID`. |
| `supplierName` | `CIDMAS.IDSUNM` | Prikazno ime remit-to strane. Upisuje u deljenu kolonu `supplier_name`. |
| `phone` | `CIDREF.IRPHNO` | Broj telefona iz komunikacionog bloka remit-to. |
| `vatNo` | `CIDMAS.IDCORG` | PDV identifikator remit-to strane. |
| `bank_id` | `CBANAC.BCBKNO` | Remit-to bankovni račun (`FinancialParty[last()]`). Važi ista postavka više banaka. |
| `status` | `CIDMAS.IDSTAT` | Aktivan/neaktivan status remit-to strane. |

## Kako dva BOD-a interaguju na deljenoj tabeli `SUPPLIER`

Oba BOD-a popunjavaju isti red `supplier_header`. Za polja koja dele (`supplierName`, `phone`, `vatNo`, `bank_id`, `status`), DocBits primenjuje sledeća pravila:

1. Pronaći red preko `(customer_number = sharedCONO, supplier_number = sharedSUNO)`.
2. Uporediti dolazni `variationID` sa sačuvanim `variationID` *za isti tip BOD-a*.
3. Ako je dolazni `variationID` veći (ili `0`, force-update), ažurirati polja koja taj BOD poseduje. U suprotnom, odbaciti BOD.
4. `variationID` drugog tipa BOD-a se ne dira; njegove ranije sačuvane vrednosti ostaju na mestu.

Redovi `supplier_address` i `supplier_account` povezani sa dobavljačem se brišu i ponovo umeću prilikom ažuriranja, tako da sekundarne tabele uvek odražavaju najnoviji BOD.

## Često postavljana pitanja

### Zašto DocBits prati CONO ako svi moji dobavljači dolaze iz jedne M3 kompanije?

CONO rutiranje je obavezno jer je DocBits multi-tenant po dizajnu: organizacija može primati BOD-ove iz više M3 kompanija. CONO je deo ključa podudaranja kako se dobavljači iz različitih kompanija ne bi sudarali. Ako imate samo jednu kompaniju, možete zanemariti vrednost, ali se kolona ključa svejedno popunjava.

### Oba BOD-a pišu u isti red dobavljača — da li poslednji BOD prepisuje sve?

Ne. Svaki tip BOD-a poseduje samo polja koja šalje, a ažuriranja se upravljaju nezavisnim `variationID`. SupplierPartyMaster koji menja samo ime dobavljača ne vraća broj telefona koji je kasniji RemitToPartyMaster upisao.

### `Supplier Categories` i `eam.UDFCHAR06` moj M3 nikada ne isporučuje — šta da radim?

Oba su opcionalna UserArea proširenja. Bez proširenja kolone ostaju NULL i nijedna DocBits funkcija ne zavisi od njih. Logiku datuma popusta uključite samo kada je vaš M3 konfigurisan da emituje `eam.UDFCHAR06`.

### Da li `vatNo` treba da filtrira po `schemeName='TaxIdentificationNumber'`?

M3 BOD putanja unosa trenutno čita `PartyIDs/TaxID` bez `schemeName` filtera. Filter se koristi u XSLT putanjama e-fakture (Facturae, XRechnung, KSeF), ne u M3 unosu. Ako vaš M3 emituje više TaxID elemenata sa različitim `schemeName` atributima, kontaktirajte nas sa primerom BOD-a pre nego što se oslonite na nefiltrirano ponašanje.

### Želim da sinhronizujem sve bankovne račune dobavljača, a ne samo poslednji. Kako?

Omogućite postavku `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC`. Sa uključenom zastavicom, svaki `FinancialParty` iz BOD-a čuva se u tabeli `supplier_account` (IBAN, ID finansijskog računa, kod valute, indikator preference). Nasleđena kolona `bank_id` u zaglavlju nastavlja da čuva poslednji unos zbog povratne kompatibilnosti.
