# EMVCo MPM (Händler-präsentierter QR)

## Überblick

**EMVCo MPM** (Merchant-Presented Mode) ist die globale QR-Code-Spezifikation der EMVCo — derselben Organisation, die auch hinter Chipkarten- und kontaktlosen Zahlungsstandards steht. Eine einzige TLV-Hülle (Tag-Length-Value) wird von mehr als einem Dutzend nationaler Instant-Payment-Systeme geteilt; ein Parser deckt daher **Pix** (Brasilien), **UPI** (Indien), **PayNow** (Singapur), **PromptPay** (Thailand), **QRIS** (Indonesien), **QR Ph** (Philippinen), **VietQR** (Vietnam), **FPS** (Hongkong), **DuitNow** (Malaysia), **NETS** (Singapur) und weitere ab.

### Funktions-Überblick

Jede EMVCo-MPM-Payload teilt dieselbe Hülle: Sie beginnt mit `000201` (Payload Format Indicator = 01) und endet mit `6304<CRC>`, wobei `<CRC>` eine 4-stellige CRC16-CCITT-FALSE-Prüfsumme in Hex ist. Innerhalb der Hülle tragen TLV-codierte Tags 26–51 **Merchant Account Info**-Templates, die über ein **GUI-Untertag** identifiziert werden — daran erkennt DocBits, welchem nationalen Schema der QR angehört. Die CRC wird validiert und das Ergebnis als Boolean ausgewiesen, damit Händler manipulierte oder beschädigte QR-Codes erkennen können.

#### Hauptvorteile

* **Ein Extraktor, viele Schemata**: Ein generischer TLV-Parser deckt die gesamte EMVCo-MPM-Familie ab.
* **Nationale Schemata erkannt**: Die Ausgabe enthält einen benannten Scheme-Wert (z. B. `pix`, `upi`, `paynow`), damit nachgelagerte Logik sauber verzweigen kann.
* **CRC-Gültigkeit ausgewiesen**: `emvmpm_crc16_valid` legt manipulierte oder korrupte QR-Codes offen.
* **Währungsnormalisierung**: Numerische ISO-4217-Codes werden automatisch auf Alpha-3 gemappt (20+ Währungen; unbekannte Codes bleiben numerisch erhalten).

***

### Erkennung

- Magic-Form: beginnt mit `000201` und endet mit `6304<4-hex CRC16-CCITT-FALSE>`
- Ein generischer TLV-Dekoder (Tag-Length-Value) läuft alle Tags ab
- Nationale Schemata werden über das **GUI-Untertag** in den Merchant-Account-Info-Templates (Tags 26–51) identifiziert

### Erkannte nationale Schemata

| GUI-Untertag | Schema | Land |
|--------------|--------|------|
| `br.gov.bcb.pix` | **Pix** | Brasilien |
| `UPI` | **UPI** | Indien |
| `SG.PAYNOW` | **PayNow / SGQR** | Singapur |
| `SG.COM.NETS` | **NETS** | Singapur |
| `HK.COM.HKICL.FPS` | **FPS** | Hongkong |
| `ID.CO.QRIS.WWW` | **QRIS** | Indonesien |
| `COM.BDO.QRPH` / `COM.BPI.QRPH` / `PH.PPMI.P2MEMV` | **QR Ph** | Philippinen |
| `COM.QRCODE.TELLUSBANGKOK` + AID `A000000677010111` | **PromptPay** | Thailand |
| `A000000727` | **VietQR** | Vietnam |

Nicht erkannte GUI-/AID-Werte lassen sich dennoch parsen — der Extraktor fällt auf das generische EMVCo-MPM-Feldset zurück.

### Extrahierte Felder

Alle Felder verwenden das Präfix `emvmpm_`:

| Feld | Beschreibung |
|------|--------------|
| `emvmpm_scheme` | Erkanntes nationales Schema (z. B. `pix`, `upi`, `paynow`, `qris`, `promptpay`, `vietqr`, `fps`, `qrph`, `nets`) oder `generic` |
| `emvmpm_merchant_name` | Händlername (Tag 59) |
| `emvmpm_merchant_city` | Händlerort (Tag 60) |
| `emvmpm_country_code` | Länder-Code ISO 3166 alpha-2 (Tag 58) |
| `emvmpm_amount` | Transaktionsbetrag (Dezimal, Tag 54) |
| `emvmpm_currency` | Währung Alpha-3 (konvertiert aus dem numerischen Tag-53-Wert) |
| `emvmpm_additional_data` | Verschachteltes Objekt: Rechnungsnummer, Referenzlabel, Terminallabel, Transaktionszweck (Tag 62 Untertags) |
| `emvmpm_crc16_valid` | Boolean — `true`, wenn die CRC16-Prüfsumme stimmt |

### Beispiel einer API-Antwort (Pix)

```json
{
  "emvmpm_scheme": "pix",
  "emvmpm_merchant_name": "ACME COMERCIO LTDA",
  "emvmpm_merchant_city": "SAO PAULO",
  "emvmpm_country_code": "BR",
  "emvmpm_amount": 125.00,
  "emvmpm_currency": "BRL",
  "emvmpm_additional_data": {
    "reference_label": "PEDIDO-2026-0427"
  },
  "emvmpm_crc16_valid": true
}
```

***

### So aktivieren Sie die Funktion

Die EMVCo-MPM-Erkennung ist Teil der allgemeinen **Bar-Code / QR-Code-Extraktion** — eine standardspezifische Konfiguration ist nicht nötig.

1. **Einstellungen öffnen**:
   * Gehen Sie vom Dashboard zu **Einstellungen**.
   * Wählen Sie **Dokumentenverarbeitung** und dann **Modul**.
2. **Funktion aktivieren**:
   * Scrollen Sie zur Option **Bar-Code / QR-Code-Extraktion**.
   * Schalten Sie den Schieberegler um, um sie zu aktivieren.

Eine vollständige Liste der Payment-QR-Code-Standards finden Sie auf der [Übersichtsseite](./README.md).
