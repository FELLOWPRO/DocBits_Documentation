---
description: Supporto in DocBits per il documento elettronico FACTURX
---

# 🇫🇷 FACTURX

| Proprietà             | Valore                       |
| --------------------- | ---------------------------- |
| **Paese / Regione**   | Francia / Germania           |
| **Tipi di documento** | Fattura, nota di credito     |
| **Formato**           | CII (incorporato in PDF/A-3) |
| **Standard**          | Factur-X                     |
| **Basato su**         | EN 16931                     |

Factur-X è l'implementazione francese dello standard di fattura ibrida franco-tedesco. Incorpora dati XML CII strutturati all'interno di un documento PDF/A-3, consentendo una fatturazione leggibile sia dalle persone sia dalle macchine. DocBits rileva automaticamente la versione e il profilo di Factur-X dall'XML incorporato.

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
* [Mappatura dei campi ZUGFeRD](../zugferd/versions/)
* [Documenti elettronici supportati](./)
