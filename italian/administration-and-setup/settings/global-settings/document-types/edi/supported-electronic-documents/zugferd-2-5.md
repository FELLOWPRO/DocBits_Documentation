---
description: Supporto del documento elettronico ZUGFERD 2.5 in DocBits
---

# 🇩🇪 ZUGFERD 2.5

| Proprietà | Valore |
|----------|-------|
| **Paese / Regione** | Germania |
| **Tipi di documento** | Fattura, Nota di credito |
| **Formato** | CII (PDF/A-3 incorporato) o UBL XML |
| **Standard** | ZUGFeRD 2.5 |
| **Basato su** | EN 16931 |

ZUGFeRD 2.5 (pubblicazione comune FeRD/FNFE-MPE del giugno 2026) è equivalente a Factur-X 1.09. Il suo XML CII utilizza la base UN/CEFACT D22B, retrocompatibile con D16B, quindi il contratto completo di estrazione e trasformazione di ZUGFeRD 2.4 continua ad applicarsi. Il profilo EXTENDED aggiunge nuovi campi per i mezzi di pagamento e il BIC, un beneficiario terzo (factor) e il motivo di esenzione fiscale di abbuono/oneri.

Tutti e cinque i profili sono supportati: MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) ed EXTENDED. DocBits classifica separatamente le varianti CII e UBL.

## Stato del supporto

| Componente | Stato |
|-----------|--------|
| Anteprima | ✅ Supportato |
| Estrazione campi | ✅ Supportato |
| Trasformazione | ✅ Supportato |

## Correlati

- [Factur-X 1.09 / ZUGFeRD 2.5](facturx-1-09-zugferd-2-5.md)
- [Configurazione ZUGFeRD](../zugferd/configuration.md)
- [Mappatura dei campi ZUGFeRD](../zugferd/README.md)
- [Documenti elettronici supportati](./)
