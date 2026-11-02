# ZUGFeRD + Swiss QR Code Feldzuordnung

## Überblick

Bei der Verarbeitung von PDF-Rechnungen, die sowohl ZUGFeRD XML-Daten als auch einen Swiss QR Code enthalten, extrahiert DocBits Daten aus beiden Quellen und führt sie intelligent zusammen.

## Wie es funktioniert

1. **ZUGFeRD XML Extraktion** - DocBits extrahiert zuerst Felder aus dem eingebetteten ZUGFeRD XML
2. **Swiss QR Code Erkennung** - Der barcode erkennt und parst Swiss QR Codes
3. **Smart Merge** - Leere Felder werden mit Swiss QR Daten gefüllt (Felder mit Werten bleiben erhalten)
4. **Audit Trail** - Die vollständigen QR Code Daten werden in `qr_code_data` zur Überprüfung gespeichert

## Feldzuordnungstabelle

### Swiss QR Code → DocBits Feldzuordnung

| Swiss QR Feld | DocBits Feld | Beschreibung |
| :--- | :--- | :--- |
| IBAN | `supplier_iban` | IBAN des Gläubigers (z.B. CH9300762011...) |
| Betrag | `total_amount` | Zahlungsbetrag (z.B. 1234.56) |
| Währung | `currency` | Währungscode (CHF oder EUR) |
| Referenz | `payment_reference` / `esr_reference` | QR-Referenz oder ESR-Nummer |
| Creditor.Name | `supplier_name` | Firmenname des Lieferanten |
| Creditor.AddressLine1 | `supplier_address` | Straßenadresse |
| Creditor.PostalCode | `supplier_plz` | Postleitzahl |
| Creditor.City | `supplier_city` | Stadt |
| Creditor.Country | `supplier_country` | Ländercode (CH) |
| Debtor.Name | `company_name` | Firmenname des Empfängers |
| Debtor.AddressLine1 | `company_street` | Straßenadresse des Empfängers |
| Debtor.PostalCode | `company_plz` | Postleitzahl des Empfängers |
| Debtor.City | `company_city` | Stadt des Empfängers |

## Beispiel: Musterrechnungsverarbeitung

### Eingabedokument

*   **PDF**: Rechnung mit eingebettetem ZUGFeRD 1.0 XML + Swiss QR Code Barcode

### Extrahierte Swiss QR Code Daten

```json
{
  "supplier_iban": "CH9300762011623852957",
  "amount_to_pay": 1234.56,
  "currency": "CHF",
  "esr_reference": "210000000003139471430009017",
  "supplier_name": "Sample Company GmbH",
  "supplier": {
    "name": "Sample Company GmbH",
    "address_line_1": "Musterstrasse",
    "address_line_2": "123",
    "postal_code": "8000",
    "city": "Zürich",
    "country": "CH"
  },
  "recipient": {
    "name": "Demo Customer AG",
    "address_line_1": "Beispielweg 45",
    "postal_code": "3000",
    "city": "Bern",
    "country": "CH"
  }
}
```

### Ergebnisse der Feldextraktion

| Feld | Wert | Quelle | Methode |
| :--- | :--- | :--- | :--- |
| `supplier_iban` | CH9300762011623852957 | ZUGFeRD XML | ED |
| `total_amount` | 1234.56 | ZUGFeRD XML | ED |
| `currency` | CHF | ZUGFeRD XML | ED |
| `supplier_name` | Sample Company GmbH | ZUGFeRD XML | ED |
| `supplier_address` | Musterstrasse 123 | ZUGFeRD XML | ED |
| `payment_reference` | 210000000003139471430009017 | Swiss QR | SWISS_QR |
| `supplier_plz` | 8000 | Swiss QR | SWISS_QR |
| `supplier_city` | Zürich | Swiss QR | SWISS_QR |

## Extraktionsmethoden

| Methodencode | Beschreibung |
| :--- | :--- |
| **ED** | Elektronisches Dokument (ZUGFeRD/XRechnung/PEPPOL XML) |
| **SWISS_QR** | Swiss QR Code Barcode-Extraktion |
| **OCR** | Optische Zeichenerkennung (Optical Character Recognition) |
| **ML** | Machine Learning Extraktion |

## Zusammenführungs-Priorität

1.  **ZUGFeRD XML** hat die höchste Priorität (strukturierte, zuverlässige Daten)
2.  **Swiss QR Code** füllt leere Felder (garantiert korrekt für Zahlungsdaten)
3.  **OCR/ML** wird für Felder verwendet, die nicht in elektronischen Quellen vorhanden sind

## Unterstützte Swiss QR Code Versionen

*   Swiss QR Bill Format (ISO 20022)
*   QR-IBAN Format (beginnt mit 30, 31)
*   Standard IBAN Format
*   Mit/ohne strukturierte Referenz (QRR, SCOR)

## Versionsanforderung

Diese Funktion erfordert **api Version 10.95.6** und **barcode Version 1.0.5** oder höher.

### Komponentenversionen (Umgebung)

| Komponente | Version | Beschreibung |
| :--- | :--- | :--- |
| `api` | 10.95.6 | Kern-API mit ZUGFeRD 1.0 Extraktionsunterstützung |
| `barcode` | 1.0.5 | Swiss QR Code Erkennung und Parsing |
| `Auth` | 1.48.8 | Authentifizierungsdienst |

