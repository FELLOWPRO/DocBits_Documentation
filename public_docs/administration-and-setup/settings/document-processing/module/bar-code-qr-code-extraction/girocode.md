# GiroCode (EPC069-12)

## Überblick

Der **GiroCode** ist der vom European Payments Council in der Spezifikation **EPC069-12** definierte SEPA-Zahlungs-QR-Code. Er ist der De-facto-Standard auf Rechnungen deutscher und österreichischer Banken (Sparkasse, VR-Banken, Deutsche Bank, Commerzbank, PSA Austria) und wird auch in den Niederlanden, Belgien und Finnland ausgegeben. DocBits decodiert beide Revisionen (**v001** und **v002**) und liefert die vollständige SEPA-Zahlung in der Dokumenten-API-Antwort.

### Funktions-Überblick

Ein GiroCode enthält alles, was für eine SEPA-Überweisung nötig ist: BIC und IBAN des Zahlungsempfängers, Empfängernamen, Betrag, Verwendungszweck sowie eine strukturierte Gläubigerreferenz oder eine unstrukturierte Verwendungszweck-Zeile. DocBits normalisiert die Payload so, dass **Beträge mit `.` oder `,` als Dezimaltrennzeichen** — eine häufige Abweichung deutscher QR-Generatoren von der Spezifikation — fehlerfrei akzeptiert werden.

#### Hauptvorteile

* **Breite Abdeckung in DE / AT**: Jede grosse Privatbank druckt GiroCodes auf Kundenrechnungen.
* **Beide Revisionen unterstützt**: v001 (BIC verpflichtend) und v002 (BIC optional im EWR).
* **Dezimaltrenner-tolerant**: `227.01` und `227,01` werden gleich behandelt.

***

### Erkennung

- Magic-Präfix: `BCD\n001` (v001) oder `BCD\n002` (v002)
- Zeilenbasierte strukturierte Payload nach der EPC069-12-Spezifikation
- **v002** macht den BIC optional, sofern die IBAN im Einheitlichen Euro-Zahlungsverkehrsraum liegt

### Extrahierte Felder

Alle Felder verwenden das Präfix `girocode_`:

| Feld | Beschreibung |
|------|--------------|
| `girocode_bic` | BIC des Empfängers (in v001 Pflicht, in v002 optional im EWR) |
| `girocode_creditor_name` | Empfängername |
| `girocode_iban` | IBAN des Empfängers |
| `girocode_amount` | Betrag (Dezimal) — `.` und `,` werden akzeptiert |
| `girocode_currency` | Währung (üblicherweise `EUR`) |
| `girocode_purpose` | SEPA-Verwendungszweckschlüssel |
| `girocode_structured_reference` | Strukturierte Gläubigerreferenz (ISO 11649 RF) |
| `girocode_unstructured_remittance` | Freitext-Verwendungszweck |
| `girocode_version` | `001` oder `002` |

### Beispiel einer API-Antwort

Praxisbeispiel (Rechnung Dr. Meindl u. Partner):

```json
{
  "girocode_bic": "DAAEDEDDXXX",
  "girocode_creditor_name": "Dr. Meindl u. Partner",
  "girocode_iban": "DE69300606010006343686",
  "girocode_amount": 227.01,
  "girocode_currency": "EUR",
  "girocode_unstructured_remittance": "38710498001705 - QR",
  "girocode_version": "002"
}
```

***

### So aktivieren Sie die Funktion

Die GiroCode-Erkennung ist Teil der allgemeinen **Bar-Code / QR-Code-Extraktion** — eine standardspezifische Konfiguration ist nicht nötig.

1. **Einstellungen öffnen**:
   * Gehen Sie vom Dashboard zu **Einstellungen**.
   * Wählen Sie **Dokumentenverarbeitung** und dann **Modul**.
2. **Funktion aktivieren**:
   * Scrollen Sie zur Option **Bar-Code / QR-Code-Extraktion**.
   * Schalten Sie den Schieberegler um, um sie zu aktivieren.

Eine vollständige Liste der Payment-QR-Code-Standards finden Sie auf der [Übersichtsseite](./README.md).
