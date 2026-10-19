---
description: Suporte para documento eletrônico ZUGFERD 2.5 no DocBits
---

# 🇩🇪 ZUGFERD 2.5

<!-- edocs-country-scope -->

{% hint style="info" %}
Consulte o guia do país para conhecer os limites das versões, a configuração efetiva e o vídeo explicativo. [Alemanha](countries/germany.md). A sintaxe, a versão da publicação e o perfil são escolhas diferentes. Não deduza uma edição Factur-X a partir do marcador partilhado 1p0.
{% endhint %}

| Propriedade | Valor |
|----------|-------|
| **País / Região** | Alemanha |
| **Tipos de documento** | Fatura, Nota de crédito |
| **Formato** | CII (incorporado em PDF/A-3) ou XML UBL |
| **Padrão** | ZUGFeRD 2.5 |
| **Baseado em** | EN 16931 |

O ZUGFeRD 2.5 (a publicação conjunta FeRD/FNFE-MPE de junho de 2026) é equivalente ao Factur-X 1.09. Seu XML CII utiliza a base UN/CEFACT D22B, retrocompatível com a D16B, de modo que todo o contrato de extração e transformação do ZUGFeRD 2.4 continua a ser aplicado. O perfil EXTENDED adiciona novos campos para meios de pagamento e BIC, um beneficiário terceiro (factor) e o motivo de isenção fiscal em descontos/encargos.

Todos os cinco perfis são suportados: MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) e EXTENDED. O DocBits classifica separadamente as variantes CII e UBL.

## Estado do suporte

| Componente | Estado |
|-----------|--------|
| Pré-visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Relacionados

- [Factur-X 1.09 / ZUGFeRD 2.5](facturx-1-09-zugferd-2-5.md)
- [Configuração do ZUGFeRD](../zugferd/configuration.md)
- [Mapeamento de campos do ZUGFeRD](../zugferd/README.md)
- [Documentos eletrônicos suportados](./)
