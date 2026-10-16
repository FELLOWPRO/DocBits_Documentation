# Swiss QR Bill

## Überblick

Die **Swiss QR Bill** ist der nationale Zahlungsbeleg-Standard, der seit dem 30. Juni 2020 die orangen und roten Schweizer Einzahlungsscheine abgelöst hat. Jede inländische Schweizer Rechnung — von Versorgern, Versicherern bis hin zu Geschäftspartnern — trägt heute einen Swiss-QR-Bill-Code. DocBits decodiert diese Codes automatisch und stellt jedes Zahlungsfeld in der API-Antwort bereit.

### Funktions-Überblick

Swiss QR Bills folgen dem **ISO-20022**-Zahlungsstandard und werden in zwei Versionen ausgegeben: **v1.0** (früher Rollout) und **v2.0** (aktuell). Der DocBits-Extraktor unterstützt beide. Erkannte Payloads liefern ein vollständiges Feldset — Zahlungsempfänger, Einzahler, IBAN / QR-IBAN, Betrag, Währung, Referenztyp (QRR, SCOR oder NON), strukturierte und unstrukturierte Nachrichten sowie alternative Zahlungsverfahren.

<figure><img src="../../../../../.gitbook/assets/image (6) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

#### Hauptvorteile

* **Null manuelle Eingabe** für Schweizer Rechnungen: IBAN, Betrag, Referenz und Zahlungsempfänger fliessen direkt ins Dokument.
* **Beide Versionen abgedeckt**: v1.0 und v2.0 werden automatisch erkannt.
* **Referenztypen erhalten**: QRR, SCOR und NON bleiben exakt wie gedruckt erhalten — unverzichtbar für die nachgelagerte Abstimmung.

***

### Erkennung

- Magic-Präfix: `SPC\n0100` (v1.0) oder `SPC\n0200` (v2.0)
- ISO-20022-konform
- Der Parser stellt zusätzlich `alt-schemes` (alternative Zahlungsverfahren) bereit, sofern vorhanden

### Extrahierte Felder

Alle Felder verwenden das Präfix `swissqr_`:

| Feld | Beschreibung |
|------|--------------|
| `swissqr_account` | IBAN oder QR-IBAN des Zahlungsempfängers |
| `swissqr_creditor_name` | Name des Zahlungsempfängers |
| `swissqr_creditor_street` | Strasse / Adresszeile |
| `swissqr_creditor_city` | Ort |
| `swissqr_creditor_postal_code` | Postleitzahl |
| `swissqr_creditor_country` | Land (ISO 3166 alpha-2) |
| `swissqr_debtor_name` | Einzahler-Name (falls gedruckt) |
| `swissqr_debtor_street`, `swissqr_debtor_city`, `swissqr_debtor_postal_code`, `swissqr_debtor_country` | Einzahler-Adresse |
| `swissqr_amount` | Betrag (Dezimalwert) |
| `swissqr_currency` | Währung (ISO 4217) — meist `CHF` oder `EUR` |
| `swissqr_reference` | Strukturierte Referenz (QRR oder SCOR) |
| `swissqr_reference_type` | `QRR`, `SCOR` oder `NON` |
| `swissqr_unstructured_message` | Freitext-Zahlungsmitteilung |
| `swissqr_bill_information` | Strukturierte Rechnungsinformationen (S1 / Swico) |
| `swissqr_alt_schemes` | Alternative Verfahren (falls vorhanden) |

### Beispiel einer API-Antwort

```json
{
  "swissqr_account": "CH4431999123000889012",
  "swissqr_creditor_name": "Robert Schneider AG",
  "swissqr_creditor_street": "Rue du Lac 1268",
  "swissqr_creditor_city": "Biel",
  "swissqr_creditor_postal_code": "2501",
  "swissqr_creditor_country": "CH",
  "swissqr_amount": 1949.75,
  "swissqr_currency": "CHF",
  "swissqr_reference": "210000000003139471430009017",
  "swissqr_reference_type": "QRR",
  "swissqr_unstructured_message": "Bill No. 3139 for services 2026"
}
```

***

### So aktivieren Sie die Funktion

Die Swiss-QR-Bill-Erkennung ist Teil der allgemeinen **Bar-Code / QR-Code-Extraktion** — eine standardspezifische Konfiguration ist nicht nötig.

1. **Einstellungen öffnen**:
   * Gehen Sie vom Dashboard zu **Einstellungen**.
   * Wählen Sie **Dokumentenverarbeitung** und dann **Modul**.
2. **Funktion aktivieren**:
   * Scrollen Sie zur Option **Bar-Code / QR-Code-Extraktion**.
   * Schalten Sie den Schieberegler um, um sie zu aktivieren.

<figure><img src="../../../../../.gitbook/assets/image (444).png" alt=""><figcaption></figcaption></figure>

Eine vollständige Liste der Payment-QR-Code-Standards finden Sie auf der [Übersichtsseite](./README.md).
