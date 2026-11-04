# Formattazione dello script di numeri di riferimento dell'esportazione del certificato per Docbits

Questo documento illustra lo script "Formattazione dei numeri di riferimento dell'esportazione del certificato", mirato a standardizzare i numeri di riferimento nei certificati di esportazione in Docbits. Una formattazione corretta garantisce che i numeri di riferimento siano conformi ai requisiti dei sistemi esterni o normativi.

### Scopo

L'obiettivo principale dello script è formattare i numeri di riferimento nei certificati di esportazione, garantendo che rispettino un requisito di lunghezza predefinito riempiendoli con zeri iniziali. Questa coerenza aiuta a mantenere un formato standardizzato per tutti i documenti di esportazione elaborati tramite Docbits.

### Panoramica dello script

Lo script identifica il campo `reference_number` in un certificato di esportazione, ne controlla la lunghezza e, se necessario, riempie il numero con zeri iniziali per garantire che rispetti il requisito di lunghezza minima.

#### Frammento di codice
```python
ref_number = get_field_value(fields_dict, 'reference_number')
# Ensure the reference number meets a minimum length of 10 characters
if len(ref_number) < 10:
ref_number = ref_number.zfill(10)
set_field_value(fields_dict, 'reference_number', ref_number)
```

