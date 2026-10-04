---
description: Suporte ao documento eletrônico ZUGFERD 2.5 no DocBits
---

# 🇩🇪 ZUGFERD 2.5

| Propriedade | Valor |
|----------|-------|
| **País / Região** | Alemanha |
| **Tipos de documentos** | Fatura, Nota de crédito |
| **Formato** | CII (PDF/A-3 incorporado) ou XML UBL |
| **Padrão** | ZUGFeRD 2.5 |
| **Com base em** | EN 16931 |

O ZUGFeRD 2.5 (publicação conjunta FeRD/FNFE-MPE de junho de 2026) é equivalente ao Factur-X 1.09. Seu XML CII usa a base UN/CEFACT D22B, compatível com versões anteriores da D16B, portanto o contrato completo de extração e transformação do ZUGFeRD 2.4 continua valendo. O perfil EXTENDED adiciona novos campos para meios de pagamento e BIC, um beneficiário terceiro (factor) e o motivo de isenção de imposto para descontos/acréscimos.

Todos os cinco perfis são suportados: MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) e EXTENDED. O DocBits classifica separadamente as variantes CII e UBL.

## Status de suporte

| Componente | Status |
|-----------|--------|
| Pré-visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Relacionados

- [Factur-X 1.09 / ZUGFeRD 2.5](facturx-1-09-zugferd-2-5.md)
- [Configuração do ZUGFeRD](../zugferd/configuration.md)
- [Mapeamento de campos ZUGFeRD](../zugferd/README.md)
- [Documentos eletrônicos suportados](./)
