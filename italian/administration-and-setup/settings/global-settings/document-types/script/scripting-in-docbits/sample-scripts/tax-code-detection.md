# Rilevamento Codice Fiscale

## Cosa fa questo script?

Determina automaticamente il codice fiscale corretto basandosi sul testo completo del documento e sugli importi di imposta/netto. Rileva scenari di reverse charge, fatture esenti da imposta e calcola l'aliquota fiscale per assegnare il codice appropriato (es. S1 per il 19%, S2 per il 7%).

## Trigger

`AFTER_FORMATTING` sul tipo di documento **INVOICE**

## Script Completo

```python
# Ottenere il testo completo del documento e gli importi
content = get_document_content(document_data)
tax_amount = get_field_value(document_data, "tax_amount", "0")
net_amount = get_field_value(document_data, "net_amount", "0")

try:
    tax = float(tax_amount) if tax_amount else 0
    net = float(net_amount) if net_amount else 0
except ValueError:
    tax = 0
    net = 0

# Regola 1: Rilevamento reverse charge tramite testo completo
if "REVERSE CHARGE" in content.upper() or "UMKEHR DER STEUERSCHULD" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Regola 2: Imposta zero = esente da imposta
elif tax == 0:
    set_field_value(document_data, "tax_code", "Z0")

# Regola 3: Calcolare l'aliquota fiscale dagli importi
elif net > 0:
    tax_rate = round((tax / net) * 100, 0)
    if tax_rate == 19:
        set_field_value(document_data, "tax_code", "S1")    # Aliquota standard
    elif tax_rate == 7:
        set_field_value(document_data, "tax_code", "S2")    # Aliquota ridotta
    else:
        set_field_value(document_data, "tax_code", "S3")    # Altra aliquota
```

## Spiegazione Passo dopo Passo

1. **Leggere il testo completo** con `get_document_content()` per il rilevamento delle parole chiave
2. **Leggere gli importi di imposta e netto** per il calcolo dell'aliquota fiscale
3. **Verificare le parole chiave reverse charge** nel testo del documento (tedesco e inglese)
4. **Verificare l'imposta a zero** — se l'importo dell'imposta e 0, assegnare il codice esente da imposta
5. **Calcolare l'aliquota fiscale** dal rapporto imposta/netto e assegnare il codice corrispondente

## Funzioni Utilizzate

- [get\_document\_content()](../business-logic-functions.md#get\_document\_content) — Leggere il testo completo OCR
- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leggere i valori dei campi
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Impostare il codice fiscale
