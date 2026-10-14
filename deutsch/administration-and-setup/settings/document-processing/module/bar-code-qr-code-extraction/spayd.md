# SPAYD / Short Payment Descriptor (Tschechien)

## Überblick

**SPAYD** (Short Payment Descriptor), auch **SPD** genannt, ist der von der tschechischen Bankenvereinigung definierte Standard-QR-Code für Zahlungen. Er ist auf nahezu jeder tschechischen Geschäftsrechnung zu finden und wird teilweise auch in der Slowakei genutzt. DocBits decodiert SPAYD-Payloads und liefert die vollständige Zahlungsanweisung — inklusive der tschechischen Spezifika (Variable-, Specific-, Constant-Symbol) — in der Dokumenten-API-Antwort.

### Funktions-Überblick

Eine SPAYD-Payload ist eine durch Sterne getrennte Liste aus Schlüssel-Wert-Paaren. Werte sind prozent-codiert, sodass UTF-8-Empfängernamen und -Nachrichten erhalten bleiben. DocBits unterstützt die verbreitete `ACC`-Variante (IBAN plus optionaler BIC, plus-getrennt), `ALT-ACC` (alternative IBANs, komma-getrennt) und bewahrt unbekannte anbieterspezifische Schlüssel in einem eigenen Feld (`spayd_raw_pairs`) auf, damit keine Daten verloren gehen.

#### Hauptvorteile

* **Vollständige Abdeckung des tschechischen Zahlungsverkehrs**: IBAN/BIC sowie VS/SS/KS-Symbole werden in benannte Felder überführt.
* **Unicode-sicher**: prozent-codierte UTF-8-Empfängernamen und -Nachrichten bleiben erhalten.
* **Vorwärtskompatibel**: unbekannte Schlüssel bleiben in `spayd_raw_pairs` erhalten.

***

### Erkennung

- Magic-Präfix: `SPD*1.0*`
- Payload ist eine mit `*` getrennte Liste von `KEY:value`-Paaren, z. B. `SPD*1.0*ACC:CZ5508000000001234567899*AM:480.55*CC:CZK`
- Werte sind **prozent-codiert** (RFC 3986)
- `ACC` kann `IBAN+BIC` (plus-getrennt) enthalten; `ALT-ACC` enthält komma-getrennte alternative IBANs

### Extrahierte Felder

Alle Felder verwenden das Präfix `spayd_`:

| Feld | Beschreibung |
|------|--------------|
| `spayd_iban` | Haupt-IBAN (aus `ACC`) |
| `spayd_bic` | BIC (aus `ACC`, falls vorhanden) |
| `spayd_alt_ibans` | Liste alternativer IBANs (aus `ALT-ACC`) |
| `spayd_amount` | Betrag (Dezimal, aus `AM`) |
| `spayd_currency` | Währung (aus `CC`, meist `CZK`) |
| `spayd_variable_symbol` | Variables Symbol (`VS`) — Rechnungs-/Referenznummer |
| `spayd_specific_symbol` | Spezifisches Symbol (`SS`) |
| `spayd_constant_symbol` | Konstantes Symbol (`KS`) |
| `spayd_recipient_name` | Empfängername (aus `RN`) |
| `spayd_due_date` | Fälligkeitsdatum (aus `DT`, `YYYYMMDD`) |
| `spayd_message` | Freitext-Nachricht (aus `MSG`) |
| `spayd_raw_pairs` | Unbekannte bzw. anbieterspezifische `KEY:value`-Paare, unverändert erhalten |

### Beispiel einer API-Antwort

```json
{
  "spayd_iban": "CZ5508000000001234567899",
  "spayd_amount": 480.55,
  "spayd_currency": "CZK",
  "spayd_variable_symbol": "2026041720",
  "spayd_constant_symbol": "0308",
  "spayd_recipient_name": "Moje firma, s.r.o.",
  "spayd_due_date": "20260507",
  "spayd_message": "Platba za fakturu 2026041720"
}
```

***

### So aktivieren Sie die Funktion

Die SPAYD-Erkennung ist Teil der allgemeinen **Bar-Code / QR-Code-Extraktion** — eine standardspezifische Konfiguration ist nicht nötig.

1. **Einstellungen öffnen**:
   * Gehen Sie vom Dashboard zu **Einstellungen**.
   * Wählen Sie **Dokumentenverarbeitung** und dann **Modul**.
2. **Funktion aktivieren**:
   * Scrollen Sie zur Option **Bar-Code / QR-Code-Extraktion**.
   * Schalten Sie den Schieberegler um, um sie zu aktivieren.

Eine vollständige Liste der Payment-QR-Code-Standards finden Sie auf der [Übersichtsseite](./README.md).
