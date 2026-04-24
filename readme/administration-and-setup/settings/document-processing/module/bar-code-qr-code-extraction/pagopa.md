# PagoPA

## Überblick

**PagoPA** ist der Payment-QR-Standard der italienischen öffentlichen Verwaltung. Jede Rechnung einer italienischen PA-Stelle (Gemeinden, Universitäten, Gesundheitswesen, Steuerbehörden) trägt einen PagoPA-QR-Code. DocBits decodiert die Payload und liefert die vier Pflichtfelder in der Dokumenten-API-Antwort.

### Funktions-Überblick

PagoPA-Payloads sind kompakt und streng strukturiert: Genau **fünf durch Pipes getrennte Felder** in einer Zeile. Beträge sind in **Cent** (Ganzzahl) codiert und werden vom Extraktor automatisch in Euro-Dezimalwerte umgerechnet. Die führenden Nullen des `codice_avviso` (18-stellige Zahlungsanzeige) bleiben erhalten — er darf nie als Integer interpretiert werden, da es sich um einen Bezeichner fester Länge handelt.

#### Hauptvorteile

* **Pflichtabdeckung** für italienische PA-Rechnungen: `codice_avviso` und Fiskalcode des Gläubigers werden in benannte Felder überführt.
* **Sichere numerische Behandlung**: Der 18-stellige `codice_avviso` behält seine führenden Nullen; der Cent-Betrag wird zusätzlich als Euro-Gleitkommazahl bereitgestellt.

***

### Erkennung

- Magic-Präfix: `PAGOPA|002|`
- Genau **5 durch Pipes getrennte Felder** nach dem Präfix: `PAGOPA|002|<codice_avviso>|<fiscal_code_creditor>|<amount_cents>|<auth>`
- **Nur EUR** — keine andere Währung ist laut Spezifikation gültig

### Extrahierte Felder

Alle Felder verwenden das Präfix `pagopa_`:

| Feld | Beschreibung |
|------|--------------|
| `pagopa_codice_avviso` | 18-stellige Zahlungsanzeige — führende Nullen erhalten (String) |
| `pagopa_fiscal_code_creditor` | 11-stelliger Fiskalcode des Gläubigers (String) |
| `pagopa_amount_cents` | Betrag in Cent (Ganzzahl) |
| `pagopa_amount` | Betrag in Euro (Dezimal, aus `pagopa_amount_cents` abgeleitet) |
| `pagopa_auth` | Optionaler Auth-/Versionsindikator aus der Payload |

### Beispiel einer API-Antwort

```json
{
  "pagopa_codice_avviso": "301234567890123456",
  "pagopa_fiscal_code_creditor": "80012345678",
  "pagopa_amount_cents": 12050,
  "pagopa_amount": 120.50
}
```

***

### So aktivieren Sie die Funktion

Die PagoPA-Erkennung ist Teil der allgemeinen **Bar-Code / QR-Code-Extraktion** — eine standardspezifische Konfiguration ist nicht nötig.

1. **Einstellungen öffnen**:
   * Gehen Sie vom Dashboard zu **Einstellungen**.
   * Wählen Sie **Dokumentenverarbeitung** und dann **Modul**.
2. **Funktion aktivieren**:
   * Scrollen Sie zur Option **Bar-Code / QR-Code-Extraktion**.
   * Schalten Sie den Schieberegler um, um sie zu aktivieren.

Eine vollständige Liste der Payment-QR-Code-Standards finden Sie auf der [Übersichtsseite](./README.md).
