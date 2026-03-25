# Auto-izvoz na osnovu uslova

## Sta ova skripta radi?

Automatski postavlja status dokumenta na "spremno za izvoz" kada su ispunjeni odredjeni uslovi: dobavljac je poznati/pouzdani vendor I iznos fakture je ispod praga. Ovo preskace rucnu validaciju za fakture niskog rizika.

## Okidac

`AFTER_FORMATTING` na tipu dokumenta **INVOICE**

## Kompletna skripta

```python
# Citanje relevantnih polja
net = get_field_value(document_data, "net_amount", "0")
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)

try:
    net_float = float(net)
except ValueError:
    net_float = 0

# Definisanje pouzdanih dobavljaca za auto-izvoz
auto_export_suppliers = ["OFFICEDEPOT", "STAPLES", "AMAZON"]

# Auto-izvoz za poznate dobavljace sa malim iznosima
if any(s in supplier for s in auto_export_suppliers) and net_float < 500:
    doc_id = document_json["doc_id"]
    update_document_status_with_doc_id(
        doc_id, user, org_id, "ready_for_export",
        message="Auto-exported (small amount, known supplier)"
    )
```

## Objasnjenje korak po korak

1. **Citanje neto iznosa i naziva dobavljaca** iz dokumenta (dobavljac sa `is_clean=True` za poredjenje)
2. **Definisanje pouzdanih dobavljaca** -- lista poznatih naziva dobavljaca (ocisceni/velika slova)
3. **Provera uslova** -- dobavljac mora biti na listi pouzdanih I iznos mora biti ispod 500
4. **Promena statusa** na `"ready_for_export"` sa opisnom porukom

{% hint style="warning" %}
**Oprez:** Promene statusa pokrecu nizvodne tokove rada (DocFlow, kuke za izvoz). Uverite se da su uslovi dovoljno strogi da se izbegnu nenamerni izvozi.
{% endhint %}

## Koriscene funkcije

- [get\_field\_value()](../field-functions.md#get\_field\_value) -- Citanje vrednosti polja
- [update\_document\_status\_with\_doc\_id()](../business-logic-functions.md#update\_document\_status\_with\_doc\_id) -- Promena statusa dokumenta
