# Script per la Formattazione dei Numeri di Riferimento del Certificato di Esportazione per Docbits

Questo documento descrive lo script "Formatting Export Certificate Reference Numbers", finalizzato a standardizzare i numeri di riferimento sui certificati di esportazione in Docbits. Una formattazione corretta garantisce che i numeri di riferimento siano conformi ai requisiti dei sistemi esterni o alle normative.

### Scopo

L'obiettivo principale dello script e formattare i numeri di riferimento sui certificati di esportazione, assicurando che soddisfino un requisito di lunghezza predefinito aggiungendo zeri iniziali. Questa coerenza aiuta a mantenere un formato standardizzato per tutti i documenti di esportazione elaborati tramite Docbits.

### Panoramica dello Script

Lo script identifica il campo `reference_number` in un certificato di esportazione, ne verifica la lunghezza e, se necessario, aggiunge zeri iniziali al numero per assicurarsi che soddisfi il requisito di lunghezza minima.

#### Frammento di Codice

```python
ref_number = get_field_value(fields_dict, 'reference_number')
# Assicurarsi che il numero di riferimento abbia una lunghezza minima di 10 caratteri
if len(ref_number) < 10:
    ref_number = ref_number.zfill(10)
    set_field_value(fields_dict, 'reference_number', ref_number)
```
