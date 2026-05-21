# Supplier BOD Mapping

Diese Seite dokumentiert, wie DocBits Lieferanten-Stammdaten aus Infor M3 über die BODs `SyncSupplierPartyMaster` und `SyncRemitToPartyMaster` einliest. Beide BODs befüllen dieselbe `SUPPLIER`-Stammdaten-Tabelle in DocBits.

{% file src="../../../../.gitbook/assets/Sync.SupplierPartyMaster.pdf" %}
SupplierPartyMaster — Original BOD Mapping Referenz (PDF)
{% endfile %}

{% file src="../../../../.gitbook/assets/Sync.RemitToPartyMaster.pdf" %}
RemitToPartyMaster — Original BOD Mapping Referenz (PDF)
{% endfile %}

## Grundprinzipien

- **CONO + SUNO ist der Match-Key.** Eine `supplier_header`-Zeile in DocBits wird eindeutig identifiziert durch `(customer_number = sharedCONO, supplier_number = sharedSUNO)`. So kann eine DocBits-Organisation mehrere M3-Mandanten konsolidieren.
- **`variationID` schützt vor Out-of-Order-BODs.** M3 kann denselben Stammdatensatz mehrfach in kurzer Folge emittieren; die eingehende `variationID` muss höher sein als die gespeicherte, damit ein Update akzeptiert wird. Beide BODs tracken ihre `variationID` unabhängig (`variation_id_supplier_bod`, `variation_id_remit_to_party`).
- **Kein stilles Überschreiben.** SupplierPartyMaster und RemitToPartyMaster teilen mehrere Felder (Name, Phone, USt-ID, Bank, Status). Jeder BOD aktualisiert nur die Felder, die er besitzt, und nur, wenn seine `variationID` höher ist. Innerhalb der geteilten Felder gewinnt der jeweils zuletzt eingegangene BOD (pro BOD-Typ).
- **Multi-Bank-Sync ist Preference-gesteuert.** Standardverhalten: Die letzte `FinancialParty` wird in `bank_id` im Header geschrieben. Mit aktivierter Preference `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` wird jede `FinancialParty` in `supplier_account` persistiert (IBAN, Konto-ID, Währungscode, Preference-Indikator).
- **Optionales CONO-Suffix-Trimming.** Manche M3-Installationen hängen ein Division-Suffix an die Mandantennummer an (z. B. `100_01`). Die Preference `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` schneidet `_*`-Suffixe ab, damit die DocBits-Keys konsistent bleiben. Beachten Sie: mit aktivem Trimming fallen mehrere pro-Division emittierte RemitToPartyMaster-BODs auf denselben Match-Key — und der BOD mit der höchsten `variationID` gewinnt. Siehe FAQ "*Was passiert, wenn pro Division ein RemitToPartyMaster-BOD gesendet wird?*" weiter unten.

## Sync.SupplierPartyMaster

→ DocBits Stammdaten-Tabelle: **SUPPLIER**

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

### Feldreferenz

| DocBits Feld | M3 Quelle | Beschreibung |
|---|---|---|
| `sharedCONO` | M3-Mandantennummer | Mappt auf `customer_number` in `supplier_header`. Teil des Match-Keys. |
| `sharedSUNO` | `CIDMAS.IDSUNO` | M3-Lieferantennummer. Teil des Match-Keys. |
| `variationID` | BOD-Attribut | Wird in `variation_id_supplier_bod` gespeichert. Eingehende BODs werden nur akzeptiert, wenn ihre `variationID` größer ist als die gespeicherte. Ein fehlendes Attribut wird als `0` interpretiert (Force-Update). |
| `supplierName` | `CIDMAS.IDSUNM` | Anzeigename des Lieferanten. |
| `phone` | `CIDMAS.PHNO/PHN2/IDTFNO` | Telefonnummer aus dem `Phone`-Communication-Channel. |
| `vatNo` | `CIDMAS.IDVRNO` | USt-Identifikation. Wird aus `PartyIDs/TaxID` gelesen (kein `@schemeName`-Filter im M3-Ingest-Pfad). **OFFEN** — wenn M3 mehrere `TaxID`-Elemente mit unterschiedlichen `@schemeName`-Werten emittiert (z. B. `VatCode`, `TaxIdentificationNumber`), gewinnt das erste Vorkommen. Ein konfigurierbarer `schemeName`-Filter wird in [DOCB-12313](https://fellowpro.atlassian.net/browse/DOCB-12313) getrackt. |
| `paymentTermId` | `CIDVEN.IITEPY` | Zahlungsbedingungs-Identifikator. |
| `paymentMethodCode` | — | Zahlungsmethoden-Code, sofern geliefert. |
| `buyerPersonReferenceId` / `buyerPersonReference` | `CIDVEN.IIBUYE` / `CSYUSR.CRRENM` | Zugeordneter Käufer (M3-User-Referenz und Anzeigename). |
| `supplier_category` | — | Lesen aus `Classification/Codes/Code[@listID='Supplier Categories']`. Optionale UserArea-Erweiterung; bei Standard-M3-Installationen NULL. |
| `supplier_group` | `CIDVEN.IISUCL` | Lieferanten-Klassifikationsgruppe. |
| `discount_terms_description` | — | Optionale UserArea-Erweiterung (`eam.UDFCHAR06`) für DocBits' Skontodatum-Berechnung. Wenn der Lieferant hier einen Skonto-Tage-Wert liefert, kombiniert DocBits ihn mit dem Rechnungsdatum, um ein Skontofälligkeitsdatum für das AP-Team zu erzeugen. |
| `status` | `CIDMAS.IDSTAT` | Lieferanten-Aktiv-/Inaktiv-Status aus `SupplierPartyMaster/Status/Code`. |
| `bank_id` | `CBANAC.BCBKNO` | Standard-Bankverbindung, gelesen aus der *letzten* `FinancialParty`. Aktivieren Sie `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC`, um stattdessen jede `FinancialParty` in die `supplier_account`-Tabelle zu synchronisieren. |

## Sync.RemitToPartyMaster

→ DocBits Stammdaten-Tabelle: **SUPPLIER**

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

### Feldreferenz

| DocBits Feld | M3 Quelle | Beschreibung |
|---|---|---|
| `sharedCONO` / `sharedSUNO` | M3-Mandant / `CIDMAS.IDSUNO` | Gleiche Semantik wie beim `SupplierPartyMaster`. Verbindet sich mit derselben `supplier_header`-Zeile. |
| `variationID` | BOD-Attribut | Wird in `variation_id_remit_to_party` gespeichert — unabhängig vom SupplierPartyMaster-`variationID` getrackt. |
| `supplierName` | `CIDMAS.IDSUNM` | Anzeigename der Zahlungsempfänger-Partei. Schreibt in die geteilte `supplier_name`-Spalte. |
| `phone` | `CIDREF.IRPHNO` | Telefonnummer aus dem RemitTo-Kommunikationsblock. |
| `vatNo` | `CIDMAS.IDCORG` | USt-Identifikation der Zahlungsempfänger-Partei. Gleiche `@schemeName`-Einschränkung wie beim SupplierPartyMaster — siehe [DOCB-12313](https://fellowpro.atlassian.net/browse/DOCB-12313). |
| `bank_id` | `CBANAC.BCBKNO` | Zahlungsempfänger-Bankverbindung (`FinancialParty[last()]`). Gleiche Multi-Bank-Preference greift. |
| `status` | `CIDMAS.IDSTAT` | Aktiv-/Inaktiv-Status der Zahlungsempfänger-Partei. |

## Wie die beiden BODs auf der geteilten `SUPPLIER`-Tabelle zusammenspielen

Beide BODs befüllen dieselbe `supplier_header`-Zeile. Für die geteilten Felder (`supplierName`, `phone`, `vatNo`, `bank_id`, `status`) wendet DocBits folgende Regeln an:

1. Die Zeile per `(customer_number = sharedCONO, supplier_number = sharedSUNO)` matchen.
2. Die eingehende `variationID` mit der gespeicherten `variationID` *für denselben BOD-Typ* vergleichen.
3. Wenn die eingehende `variationID` höher ist (oder `0`, also Force-Update), die vom jeweiligen BOD besessenen Felder aktualisieren. Andernfalls den BOD verwerfen.
4. Die `variationID` des anderen BOD-Typs bleibt unberührt; dessen zuvor gespeicherte Werte bleiben erhalten.

`supplier_address` und `supplier_account` werden bei Updates gelöscht und neu eingefügt, damit Sekundärtabellen stets den aktuellsten BOD-Stand widerspiegeln. Das hat einen Seiteneffekt, wenn M3 pro Division einen RemitToPartyMaster-BOD sendet (das tun manche Mandanten, wenn Bankverbindungen sowohl auf einer leeren Division als auch auf spezifischen Divisions gepflegt sind): nachdem `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` das Division-Suffix abschneidet, zielen alle pro-Division-BODs auf denselben `(customer_number, supplier_number)`-Key. Der BOD mit der höchsten `variationID` gewinnt. Wenn dieser "gewinnende" BOD aus einer Division ohne Bankverbindungen stammt, werden die Bankkonten des vorherigen BODs beim Re-Insert überschrieben.

## Häufige Fragen

### Warum trackt DocBits CONO, wenn alle meine Lieferanten aus einem M3-Mandanten kommen?

CONO-Routing ist verpflichtend, weil DocBits per Design mandantenfähig ist: Eine Organisation kann BODs aus mehreren M3-Mandanten ingestieren. CONO ist Teil des Match-Keys, damit Lieferanten verschiedener Mandanten nicht kollidieren. Bei nur einem Mandanten können Sie den Wert ignorieren — die Key-Spalte wird trotzdem befüllt.

### Beide BODs schreiben auf dieselbe Lieferanten-Zeile — überschreibt der jeweils letzte BOD alles?

Nein. Jeder BOD-Typ besitzt nur die Felder, die er sendet, und Updates werden über eine unabhängige `variationID` gesteuert. Ein SupplierPartyMaster, der nur den Lieferantennamen ändert, macht keine Telefonnummer rückgängig, die ein späterer RemitToPartyMaster geschrieben hat.

### `Supplier Categories` und `eam.UDFCHAR06` werden von meinem M3 nie geliefert — was tun?

Beides sind optionale UserArea-Erweiterungen. Ohne die Erweiterung bleiben die Spalten NULL, und kein DocBits-Feature hängt davon ab. Aktivieren Sie die Skontodatum-Logik nur, wenn Ihr M3 `eam.UDFCHAR06` emittiert.

### Soll `vatNo` auf `schemeName='TaxIdentificationNumber'` filtern?

Der M3-BOD-Ingest-Pfad liest aktuell `PartyIDs/TaxID` ohne `schemeName`-Filter. Der Filter wird in den e-Invoice-XSLT-Pfaden (Facturae, XRechnung, KSeF) verwendet, nicht im M3-Ingest. Wenn M3 mehrere `TaxID`-Elemente mit unterschiedlichen `@schemeName`-Werten emittiert, gewinnt das erste Vorkommen — was zu falschen USt-Identifikationen führen kann. Ein konfigurierbarer Filter wird in [DOCB-12313](https://fellowpro.atlassian.net/browse/DOCB-12313) getrackt; ein Beispiel-BOD aus Ihrem Mandanten hilft uns, den richtigen Default-`schemeName` festzulegen.

### Was passiert, wenn pro Division ein RemitToPartyMaster-BOD gesendet wird?

Manche M3-Mandanten pflegen Bankverbindungen sowohl auf einer leeren Division als auch auf spezifischen Divisions, was dazu führt, dass M3 pro Division einen separaten RemitToPartyMaster-BOD emittiert. Der Match-Key in DocBits ist `(customer_number = sharedCONO, supplier_number = sharedSUNO)` — die Division ist nicht Teil davon.

- Mit aktivierter Preference `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` fallen die pro-Division-BODs auf dieselbe Zeile. Der BOD mit der höchsten `variationID` gewinnt, und `supplier_account`-Zeilen werden nur aus diesem BOD neu eingefügt. Wenn der gewinnende BOD aus einer Division ohne Bankverbindungen stammt, werden zuvor gespeicherte Bankkonten überschrieben.
- Mit deaktivierter Preference (die CONO behält das Division-Suffix) zielen die pro-Division-BODs auf unterschiedliche Keys und koexistieren.

Wenn Ihr Mandant pro-Division-RemitToPartyMaster-BODs sendet und auf die konsolidierte Bank-Liste angewiesen ist, kontaktieren Sie uns mit einem Beispiel, damit wir eine Verfeinerung planen können.

### Ich möchte alle Lieferanten-Bankverbindungen synchronisieren, nicht nur die letzte. Wie?

Aktivieren Sie die Preference `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC`. Mit aktiviertem Flag wird jede `FinancialParty` aus dem BOD in die `supplier_account`-Tabelle persistiert (IBAN, Finanzkonto-ID, Währungscode, Preference-Indikator). Die Legacy-Spalte `bank_id` im Header enthält weiterhin den letzten Eintrag zur Abwärtskompatibilität.
