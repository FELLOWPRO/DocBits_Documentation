# ZATCA Fatoora (Saudi-Arabien)

## Überblick

**ZATCA Fatoora** ist der von der Zakat-, Steuer- und Zollbehörde Saudi-Arabiens vorgeschriebene E-Invoicing-QR-Code. Seit **Dezember 2021 (Phase 1)** muss jede im Königreich ausgestellte B2C-Rechnung einen Fatoora-QR mit den fünf Kern-Rechnungsfeldern tragen; seit **Januar 2023 (Phase 2)** enthält der QR zusätzlich eine kryptografische Signatur-Hülle. DocBits decodiert beide Phasen und liefert alle Phase-1-Zahlungsfelder als benannte Eigenschaften in der Dokumenten-API-Antwort.

### Funktions-Überblick

ZATCA Fatoora nutzt ein **binäres TLV**-Format (1 Byte Tag-ID, 1 Byte Länge, Wert), verpackt in **Base64**. Der gesamte Text ist UTF-8, daher werden arabische Verkäufernamen sauber dekodiert. Der Extraktor stellt Phase-1-Tags 1–5 als strukturierte Felder bereit und — falls vorhanden — Phase-2-Tags 6–9 als Base64-Strings für nachgelagerte Compliance-Tools. **Signatur- und Hash-Verifikation sind bewusst nicht Teil des Scopes**; sie gehören in spezialisierte E-Invoicing-Compliance-Stacks.

#### Hauptvorteile

* **Pflicht-Compliance-Abdeckung**: Jede saudische B2C-Rechnung wird geparst.
* **Arabisch-Unterstützung**: UTF-8-Verkäufernamen bleiben ohne erneutes Encoding erhalten.
* **Phase 1 und Phase 2**: Beide Phasen werden erkannt; die Phase wird in der Ausgabe angezeigt.
* **Phase-2-Hülle erhalten**: Hash, Signatur, Public Key und Zertifikatssignatur bleiben als Base64-Strings für Compliance-Tools verfügbar.

***

### Erkennung

- Base64-gewickeltes binäres TLV (Tags 1–9, 1 Byte Tag-ID + 1 Byte Länge + Wert)
- Phase-Erkennung: `zatca_phase = 1`, wenn nur Tags 1–5 vorhanden sind; `zatca_phase = 2`, wenn auch Tags 6–9 vorhanden sind

### TLV-Tag-Aufteilung

| Tag | Phase | Inhalt |
|-----|-------|--------|
| 1 | 1 | Verkäufername (UTF-8, arabisch möglich) |
| 2 | 1 | USt-Registriernummer |
| 3 | 1 | Rechnungszeitstempel (ISO 8601) |
| 4 | 1 | Rechnungssumme |
| 5 | 1 | USt-Summe |
| 6 | 2 | XML-Rechnungs-Hash (Base64) |
| 7 | 2 | Digitale Signatur (Base64) |
| 8 | 2 | Public Key (Base64) |
| 9 | 2 | Zertifikatssignatur (Base64) |

### Extrahierte Felder

Alle Felder verwenden das Präfix `zatca_`:

| Feld | Beschreibung |
|------|--------------|
| `zatca_seller_name` | Verkäufername (UTF-8) |
| `zatca_vat_number` | USt-Registriernummer |
| `zatca_invoice_timestamp` | Rechnungsdatum/-zeit |
| `zatca_invoice_total` | Rechnungssumme (Dezimal) |
| `zatca_vat_total` | USt-Summe (Dezimal) |
| `zatca_phase` | `1` (Phase 1) oder `2` (Phase 2) |
| `zatca_invoice_hash` | XML-Rechnungs-Hash — nur Phase 2, Base64 |
| `zatca_signature` | Digitale Signatur — nur Phase 2, Base64 |
| `zatca_public_key` | Public Key — nur Phase 2, Base64 |
| `zatca_certificate_signature` | Zertifikatssignatur — nur Phase 2, Base64 |

{% hint style="info" %}
**Ausserhalb des Scopes**: DocBits verifiziert weder die kryptografische Signatur noch den Hash oder die Zertifikatskette. Diese Prüfung ist eine eigenständige Compliance-Aufgabe und sollte von einem ZATCA-zertifizierten E-Invoicing-Stack übernommen werden.
{% endhint %}

### Beispiel einer API-Antwort (Phase 1)

```json
{
  "zatca_seller_name": "شركة أكمي التجارية",
  "zatca_vat_number": "300123456700003",
  "zatca_invoice_timestamp": "2026-04-24T10:00:00",
  "zatca_invoice_total": 115.00,
  "zatca_vat_total": 15.00,
  "zatca_phase": 1
}
```

***

### So aktivieren Sie die Funktion

Die ZATCA-Fatoora-Erkennung ist Teil der allgemeinen **Bar-Code / QR-Code-Extraktion** — eine standardspezifische Konfiguration ist nicht nötig.

1. **Einstellungen öffnen**:
   * Gehen Sie vom Dashboard zu **Einstellungen**.
   * Wählen Sie **Dokumentenverarbeitung** und dann **Modul**.
2. **Funktion aktivieren**:
   * Scrollen Sie zur Option **Bar-Code / QR-Code-Extraktion**.
   * Schalten Sie den Schieberegler um, um sie zu aktivieren.

Eine vollständige Liste der Payment-QR-Code-Standards finden Sie auf der [Übersichtsseite](./README.md).
