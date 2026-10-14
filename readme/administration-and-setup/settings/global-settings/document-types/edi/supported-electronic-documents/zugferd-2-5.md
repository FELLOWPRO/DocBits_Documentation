---
description: Supporto documenti elettronici ZUGFERD 2.5 in DocBits
---

# 🇩🇪 ZUGFERD 2.5

| Proprietà | Valore |
|----------|-------|
| **Paese / Regione** | Germania |
| **Tipi di documento** | Fattura, Nota di credito |
| **Formato** | CII (incorporato in PDF/A-3) o XML UBL |
| **Standard** | ZUGFeRD 2.5 |
| **Basato su** | EN 16931 |

ZUGFeRD 2.5 (la pubblicazione congiunta FeRD/FNFE-MPE di giugno 2026) equivale a Factur-X 1.09. Il suo XML CII utilizza la base UN/CEFACT D22B, retrocompatibile con D16B, pertanto l'intero contratto di estrazione e trasformazione di ZUGFeRD 2.4 continua a valere. Il profilo EXTENDED aggiunge nuovi campi per i mezzi di pagamento e il BIC, per un beneficiario terzo (factor) e per il motivo di esenzione fiscale di abbuoni/addebiti.

Sono supportati tutti e cinque i profili: MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) ed EXTENDED. DocBits classifica separatamente le varianti CII e UBL.

## Stato del supporto

| Componente | Stato |
|-----------|--------|
| Anteprima | ✅ Supportato |
| Estrazione campi | ✅ Supportato |
| Trasformazione | ✅ Supportato |

## Correlati

- [Factur-X 1.09 / ZUGFeRD 2.5](facturx-1-09-zugferd-2-5.md)
- [Configurazione di ZUGFeRD](../zugferd/configuration.md)
- [Mappatura dei campi ZUGFeRD](../zugferd/README.md)
- [Documenti elettronici supportati](./)
