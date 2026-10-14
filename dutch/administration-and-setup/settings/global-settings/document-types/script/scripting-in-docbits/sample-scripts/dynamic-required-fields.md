# Dynamische Verplichte Velden

## Wat doet dit script?

Stelt dynamisch veldvereisten in op basis van de documentinhoud. In dit voorbeeld: wanneer de factuurvaluta niet EUR is, wordt het wisselkoersveld verplicht en zichtbaar. Voor EUR-facturen wordt het wisselkoersveld verborgen en optioneel.

## Trigger

`ON_FIELD_CHANGE` op documenttype **INVOICE**

## Volledig Script

```python
# Huidige valuta lezen
currency = get_field_value(document_data, "currency", "EUR")

# Vreemde valuta: wisselkoers is verplicht en zichtbaar
if currency and currency != "EUR":
    set_is_required(document_data, "exchange_rate", True)
    set_is_hidden(document_data, "exchange_rate", False)
else:
    # EUR: wisselkoers is optioneel en verborgen
    set_is_required(document_data, "exchange_rate", False)
    set_is_hidden(document_data, "exchange_rate", True)
```

## Variatie: Inkoopfactuur vs. kostenfactuur

```python
po = get_field_value(document_data, "purchase_order", "")

if po and po.strip():
    # Inkoopfactuur: PO-nummer is verplicht
    set_field_value(document_data, "invoice_category", "PURCHASE_INVOICE")
    set_is_required(document_data, "purchase_order", True)
else:
    # Kostenfactuur: PO-nummer niet nodig, tabel verbergen
    set_field_value(document_data, "invoice_category", "COST_INVOICE")
    set_is_required(document_data, "purchase_order", False)
    delete_tables(document_data)
```

## Stapsgewijze Uitleg

1. **Het sturende veld lezen** (valuta in dit geval)
2. **Bedrijfsregels toepassen** — verschillende veldvereisten op basis van de waarde
3. **Zichtbaarheid instellen** — irrelevante velden verbergen om de UI overzichtelijk te houden
4. **Vereisten instellen** — relevante velden verplicht maken

{% hint style="info" %}
**Triggerkeuze:** `ON_FIELD_CHANGE` wordt elke keer uitgevoerd wanneer een gebruiker een veld wijzigt, zodat de vereisten in realtime worden bijgewerkt. `AFTER_FORMATTING` wordt slechts eenmaal uitgevoerd na de eerste extractie.
{% endhint %}

## Gebruikte Functies

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Sturend veld lezen
- [set\_is\_required()](../field-functions.md#set\_is\_required) — Veld als verplicht/optioneel instellen
- [set\_is\_hidden()](../field-functions.md#set\_is\_hidden) — Velden tonen/verbergen
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Categorieveld instellen
- [delete\_tables()](../table-functions.md#delete\_tables) — Tabellen verwijderen voor kostenfacturen
