---
description: Supporto in DocBits per il documento elettronico FACTURX
---

# 🇫🇷 FACTURX

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultate la guida del paese per i limiti delle versioni, la configurazione effettivamente utilizzata e il video esplicativo del paese. [Francia](countries/france.md). Il marcatore XML 1p0 e Factur-X XMP Version 1.0 non identificano una versione di pubblicazione. Mantenete l’etichetta generica quando la pubblicazione è sconosciuta.
{% endhint %}

| Proprietà             | Valore                       |
| --------------------- | ---------------------------- |
| **Paese / Regione**   | Francia / Germania           |
| **Tipi di documento** | Fattura, nota di credito     |
| **Formato**           | CII (incorporato in PDF/A-3) |
| **Standard**          | Factur-X                     |
| **Basato su**         | EN 16931                     |

Un Guideline ID CII armonizzato può identificare una famiglia e un profilo pur condividendo lo stesso marcatore 1p0 tra più versioni. Factur-X XMP Version 1.0 è un marcatore di schema, non una pubblicazione come 1.08 o 1.09. I metadati XMP di ZUGFeRD possono dichiararne la versione. In assenza di metadati autorevoli, mantenete il risultato della famiglia generica e confermate il file originale con il mittente.

## Stato del supporto

| Componente           | Stato         |
| -------------------- | ------------- |
| Anteprima            | ✅ Supportato |
| Estrazione dei campi | ✅ Supportato |
| Trasformazione       | ✅ Supportato |

## Anteprima predefinita

<figure><img src="../../../../../../.gitbook/assets/facturx-preview.png" alt="Anteprima di una fattura Factur-X in DocBits"><figcaption><p>Anteprima predefinita di DocBits per una fattura francese Factur-X</p></figcaption></figure>

## Correlati

* [Configurazione ZUGFeRD](../zugferd/)
* [Mappatura dei campi ZUGFeRD](../zugferd/README.md)
* [Documenti elettronici supportati](./)
