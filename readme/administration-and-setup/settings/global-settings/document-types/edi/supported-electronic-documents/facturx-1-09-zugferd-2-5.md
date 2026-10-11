---
description: Suporte ao documento eletrônico FACTURX 1.09 - ZUGFERD 2.5 no DocBits
---

# 🇫🇷 FACTURX 1.09 - ZUGFERD 2.5

| Propriedade | Valor |
|----------|-------|
| **País / Região** | França / Alemanha |
| **Tipos de documentos** | Fatura, Nota de crédito |
| **Formato** | CII (PDF/A-3 incorporado) |
| **Padrão** | Factur-X 1.09 / ZUGFeRD 2.5 |
| **Com base em** | EN 16931 |

O Factur-X 1.09 é a publicação francesa equivalente ao ZUGFeRD 2.5 (publicação conjunta FeRD/FNFE-MPE, junho de 2026). Seu XML CII usa a base UN/CEFACT D22B, compatível com versões anteriores da D16B, portanto o contrato completo de extração e transformação do Factur-X 1.08 / ZUGFeRD 2.4 continua valendo. O perfil EXTENDED adiciona novos campos para meios de pagamento e BIC, um beneficiário terceiro (factor) e o motivo de isenção de imposto para descontos/acréscimos.

Todos os cinco perfis são suportados: MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) e EXTENDED.

## Status de suporte

| Componente | Status |
|-----------|--------|
| Pré-visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Relacionados

- [ZUGFeRD 2.5](zugferd-2-5.md)
- [Configuração do ZUGFeRD](../zugferd/configuration.md)
- [Mapeamento de campos ZUGFeRD](../zugferd/README.md)
- [Documentos eletrônicos suportados](./)
