---
description: Suporte a documentos eletrônicos FACTURX 1.09 - ZUGFERD 2.5 no DocBits
---

# 🇫🇷 FACTURX 1.09 - ZUGFERD 2.5

<!-- edocs-country-scope -->

{% hint style="info" %}
Consulte o guia do país para conhecer os limites das versões, a configuração efetiva e o vídeo explicativo. [França](countries/france.md). O marcador XML 1p0 e Factur-X XMP Version 1.0 não identificam uma edição da publicação. Mantenha a designação genérica quando a edição for desconhecida.
{% endhint %}

| Propriedade | Valor |
|----------|-------|
| **País / Região** | França / Alemanha |
| **Tipos de documento** | Fatura, nota de crédito |
| **Formato** | CII (PDF/A-3 incorporado) |
| **Padrão** | Factur-X 1.09 / ZUGFeRD 2.5 |
| **Baseado em** | EN 16931 |

O Factur-X 1.09 é a publicação francesa equivalente ao ZUGFeRD 2.5 (publicação comum FeRD/FNFE-MPE, junho de 2026). Seu XML CII usa a base UN/CEFACT D22B, que é retrocompatível com a D16B; portanto, todo o contrato de extração e transformação do Factur-X 1.08 / ZUGFeRD 2.4 continua válido. O perfil EXTENDED adiciona novos campos para meios de pagamento e BIC, um beneficiário terceiro (factor) e o motivo de isenção de imposto em descontos/encargos.

Todos os cinco perfis são suportados: MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) e EXTENDED.

## Status de suporte

| Componente | Status |
|-----------|--------|
| Visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Relacionado

- [ZUGFeRD 2.5](zugferd-2-5.md)
- [Configuração do ZUGFeRD](../zugferd/configuration.md)
- [Mapeamento de campos do ZUGFeRD](../zugferd/README.md)
- [Documentos Eletrônicos Suportados](./)
