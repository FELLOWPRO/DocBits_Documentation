---
description: Supporto documenti elettronici ZUGFERD 1.0 in DocBits
---

# 🇩🇪 ZUGFERD 1.0

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultate la guida del paese per i limiti delle versioni, la configurazione effettivamente utilizzata e il video esplicativo del paese. [Germania](countries/germany.md). Sintassi, versione di pubblicazione e profilo sono scelte diverse. Non deducete una pubblicazione Factur-X dal marcatore condiviso 1p0.
{% endhint %}

| Proprietà               | Valore                           |
| ----------------------- | -------------------------------- |
| **Paese / Regione**     | Germania                         |
| **Tipi di documento**   | Fattura, Nota di credito         |
| **Formato**             | CII (incorporato in PDF/A-3)     |
| **Standard**            | ZUGFeRD 1.0                      |
| **Basato su**           | Specifica ZUGFeRD 1.0            |

ZUGFeRD 1.0 è stato il primo standard tedesco di fattura ibrida, pubblicato nel 2014. Incorpora un file XML CII (ZUGFeRD-invoice.xml) all'interno di un documento PDF/A-3. Questa versione è precedente alla norma europea EN 16931 e utilizza un proprio sistema di profili.

## Stato del supporto

| Componente        | Stato       |
| ----------------- | ----------- |
| Anteprima         | ✅ Supportato |
| Estrazione campi  | ✅ Supportato |
| Trasformazione    | ✅ Supportato |

## Anteprima predefinita

<figure><img src="../../../../../../.gitbook/assets/zugferd-preview.png" alt="Anteprima di una fattura ZUGFeRD 1.0 in DocBits"><figcaption><p>Anteprima DocBits predefinita per una fattura tedesca ZUGFeRD 1.0</p></figcaption></figure>

## Correlati

* [Configurazione di ZUGFeRD](../zugferd/)
* [Mappatura dei campi ZUGFeRD](../zugferd/versions/)
* [Documenti elettronici supportati](./)
