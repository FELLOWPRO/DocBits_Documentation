# ZATCA Fatoora (Saoedi-Arabië)

## Overzicht

**ZATCA Fatoora** is de e-invoicing QR-code die door de Zakat, Belasting- en Douaneautoriteit van Saoedi-Arabië is voorgeschreven. Sinds **december 2021 (Fase 1)** moet elke B2C-factuur die in het Koninkrijk wordt uitgegeven een Fatoora-QR met de vijf kernvelden van de factuur bevatten; sinds **januari 2023 (Fase 2)** draagt de QR bovendien een cryptografische handtekeningenvelop. DocBits decodeert beide fases en retourneert elk betalingsveld uit Fase 1 als benoemde eigenschap in de API-respons van het document.

### Functieoverzicht

ZATCA Fatoora gebruikt een **binair TLV**-formaat (1 byte tag-ID, 1 byte lengte, waarde) verpakt in **Base64**. Alle tekst is UTF-8, dus Arabische verkopernamen worden correct gedecodeerd. De extractor stelt Fase 1-tags 1–5 bloot als gestructureerde velden en — indien aanwezig — Fase 2-tags 6–9 als Base64-strings voor downstream compliance-tooling. **Verificatie van handtekening/hash ligt bewust buiten de scope**; dat hoort thuis in toegewijde e-invoicing compliance-stacks.

#### Belangrijkste Voordelen

* **Verplichte compliance-dekking**: elke Saoedische B2C-factuur wordt geparseerd.
* **Arabische ondersteuning**: UTF-8-verkopernamen komen heel door zonder her-codering.
* **Fase 1 en Fase 2**: beide fases worden gedetecteerd; de fase wordt blootgesteld in de output.
* **Fase 2-envelop bewaard**: hash, handtekening, public key en certificaathandtekening worden bewaard als Base64-strings voor compliance-tooling.

***

### Detectie

- Base64-omwikkeld binair TLV (tags 1–9, 1 byte tag-ID + 1 byte lengte + waarde)
- Fasedetectie: `zatca_phase = 1` als alleen tags 1–5 aanwezig zijn; `zatca_phase = 2` als tags 6–9 ook aanwezig zijn

### TLV-Tagopmaak

| Tag | Fase | Inhoud |
|-----|------|--------|
| 1 | 1 | Verkopernaam (UTF-8, ondersteunt Arabisch) |
| 2 | 1 | BTW-registratienummer |
| 3 | 1 | Tijdstempel van de factuur (ISO 8601) |
| 4 | 1 | Factuurtotaal |
| 5 | 1 | BTW-totaal |
| 6 | 2 | XML-factuurhash (Base64) |
| 7 | 2 | Digitale handtekening (Base64) |
| 8 | 2 | Public key (Base64) |
| 9 | 2 | Certificaathandtekening (Base64) |

### Geëxtraheerde Velden

Alle velden gebruiken de prefix `zatca_`:

| Veld | Beschrijving |
|------|--------------|
| `zatca_seller_name` | Verkopernaam (UTF-8) |
| `zatca_vat_number` | BTW-registratienummer |
| `zatca_invoice_timestamp` | Factuurdatum/-tijd |
| `zatca_invoice_total` | Factuurtotaal (decimaal) |
| `zatca_vat_total` | BTW-totaal (decimaal) |
| `zatca_phase` | `1` (Fase 1) of `2` (Fase 2) |
| `zatca_invoice_hash` | XML-factuurhash — alleen Fase 2, Base64 |
| `zatca_signature` | Digitale handtekening — alleen Fase 2, Base64 |
| `zatca_public_key` | Public key — alleen Fase 2, Base64 |
| `zatca_certificate_signature` | Certificaathandtekening — alleen Fase 2, Base64 |

{% hint style="info" %}
**Buiten scope**: DocBits verifieert geen cryptografische handtekening, hash of certificaatketen. Die verificatie is een aparte compliance-aangelegenheid en moet worden afgehandeld door een ZATCA-gecertificeerde e-invoicing-stack.
{% endhint %}

### Voorbeeld API-respons (Fase 1)

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

### Hoe de Functie In te Schakelen

Parsing van ZATCA Fatoora wordt afgedekt door de algemene **Barcode / QR-Code Extractie** schakelaar — er is geen standaardspecifieke configuratie nodig.

1. **Navigeer naar Instellingen**:
   * Ga vanuit het Dashboard naar **Instellingen**.
   * Selecteer **Documentverwerking** en kies vervolgens **Module**.
2. **Schakel de Functie In**:
   * Scroll naar beneden om de optie **Barcode / QR-Code Extractie** te vinden.
   * Gebruik de schuifregelaar om deze in te schakelen.

Voor de volledige lijst van Betalings-QR-code standaarden, zie de [Overzichtspagina](./README.md).
