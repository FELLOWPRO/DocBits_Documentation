# Calcul de la Date d'Échéance

## Que fait ce script ?

Calcule la date d'échéance de paiement en fonction de la date de facture en ajoutant un nombre configurable de jours (ex. 30). Les week-ends sont automatiquement ignorés afin que la date d'échéance tombe toujours un jour ouvrable.

## Déclencheur

`AFTER_FORMATTING` sur le type de document **INVOICE**

## Script complet

```python
# Lire la date de facture
inv_date = get_field_value(document_data, "invoice_date")

if inv_date:
    # Calculer la date d'échéance : 30 jours après la date de facture, sans les week-ends
    set_date_value(document_data, "due_date", inv_date,
                   add_days=30, skip_weekend=True)

    # Définir aussi la date comptable = date de facture
    set_date_value(document_data, "accounting_date", inv_date)
```

## Variantes

### 14 jours, en excluant les lundis

```python
set_date_value(document_data, "due_date", inv_date,
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

### 60 jours, sans saut de week-end

```python
set_date_value(document_data, "due_date", inv_date, add_days=60)
```

### Définir la date de livraison à aujourd'hui

```python
set_date_value(document_data, "delivery_date", None)  # None = aujourd'hui
```

## Explication étape par étape

1. **Lire la date de facture** depuis le document
2. **Calculer la date d'échéance** avec `set_date_value()` avec `add_days=30` et `skip_weekend=True`
3. **Le formatage de la date** est automatique — utilise le `date_format_pattern` du document (ex. `%d.%m.%Y`)
4. **Le saut de week-end** garantit que la date d'échéance tombe du lundi au vendredi

## Codes de jours pour `exclude_final_days`

`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`

## Fonctions utilisées

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Lire la date de facture
- [set\_date\_value()](../field-functions.md#set\_date\_value) — Calculer et définir la date d'échéance
