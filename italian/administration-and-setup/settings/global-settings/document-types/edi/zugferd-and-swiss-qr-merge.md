# Mappatura dei campi ZUGFeRD + Swiss QR Code

## Panoramica

Durante l'elaborazione di fatture PDF che contengono sia dati XML ZUGFeRD sia un codice Swiss QR Code, DocBits estrae i dati da entrambe le fonti e li unisce in modo intelligente.

## Come funziona

1. **Estrazione XML ZUGFeRD** - DocBits estrae prima i campi dal XML ZUGFeRD incorporato
2. **Rilevamento Swiss QR Code** - Il barcode rileva e analizza i codici Swiss QR
3. **Unione Intelligente (Smart Merge)** - I campi vuoti vengono riempiti con i dati Swiss QR (i campi con valori vengono preservati)
4. **Audit Trail** - I dati completi del codice QR vengono memorizzati in `qr_code_data` per la verifica

## Tabella di Mappatura dei Campi

### Mappatura Campi Swiss QR Code → DocBits

| Campo Swiss QR | Campo DocBits | Descrizione |
| :--- | :--- | :--- |
| IBAN | `supplier_iban` | IBAN del creditore (es. CH9300762011...) |
| Amount | `total_amount` | Importo del pagamento (es. 1234.56) |
| Currency | `currency` | Codice valuta (CHF o EUR) |
| Reference | `payment_reference` / `esr_reference` | Riferimento QR o numero ESR |
| Creditor.Name | `supplier_name` | Nome dell'azienda fornitrice |
| Creditor.AddressLine1 | `supplier_address` | Indirizzo (via) |
| Creditor.PostalCode | `supplier_plz` | Codice postale |
| Creditor.City | `supplier_city` | Città |
| Creditor.Country | `supplier_country` | Codice paese (CH) |
| Debtor.Name | `company_name` | Nome dell'azienda destinataria |
| Debtor.AddressLine1 | `company_street` | Indirizzo del destinatario |
| Debtor.PostalCode | `company_plz` | Codice postale del destinatario |
| Debtor.City | `company_city` | Città del destinatario |

## Esempio: Elaborazione di una Fattura Campione

### Documento di Input

*   **PDF**: Fattura con XML ZUGFeRD 1.0 incorporato + codice a barre Swiss QR Code

### Dati Estratti dal Swiss QR Code

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

### Risultati dell'Estrazione dei Campi

| Campo | Valore | Fonte | Metodo |
| :--- | :--- | :--- | :--- |
| `supplier_iban` | CH9300762011623852957 | ZUGFeRD XML | ED |
| `total_amount` | 1234.56 | ZUGFeRD XML | ED |
| `currency` | CHF | ZUGFeRD XML | ED |
| `supplier_name` | Sample Company GmbH | ZUGFeRD XML | ED |
| `supplier_address` | Musterstrasse 123 | ZUGFeRD XML | ED |
| `payment_reference` | 210000000003139471430009017 | Swiss QR | SWISS_QR |
| `supplier_plz` | 8000 | Swiss QR | SWISS_QR |
| `supplier_city` | Zürich | Swiss QR | SWISS_QR |

## Metodi di Estrazione

| Codice Metodo | Descrizione |
| :--- | :--- |
| **ED** | Documento Elettronico (ZUGFeRD/XRechnung/PEPPOL XML) |
| **SWISS_QR** | Estrazione codice a barre Swiss QR Code |
| **OCR** | Riconoscimento Ottico dei Caratteri |
| **ML** | Estrazione tramite Machine Learning |

## Priorità di Unione (Merge)

1.  **ZUGFeRD XML** ha la massima priorità (dati strutturati e affidabili)
2.  **Swiss QR Code** riempie i campi vuoti (garantito accurato per i dati di pagamento)
3.  **OCR/ML** utilizzato per i campi non presenti nelle fonti elettroniche

## Versioni Swiss QR Code Supportate

*   Formato Swiss QR Bill (ISO 20022)
*   Formato QR-IBAN (inizia con 30, 31)
*   Formato IBAN Standard
*   Con/senza riferimento strutturato (QRR, SCOR)

## Requisito di Versione

Questa funzionalità richiede **api versione 10.95.6** e **barcode versione 1.0.5** o superiore.

### Versioni dei Componenti (Ambiente Dev)

| Componente | Versione | Descrizione |
| :--- | :--- | :--- |
| `api` | 10.95.6 | API principale con supporto all'estrazione ZUGFeRD 1.0 |
| `barcode` | 1.0.5 | Rilevamento e parsing del Swiss QR Code |
| `Auth` | 1.48.8 | Servizio di autenticazione |

