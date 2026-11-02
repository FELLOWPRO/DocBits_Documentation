---
description: Suporte a documentos eletrônicos FACTURX no DocBits
---

# 🇫🇷 FACTURX

<!-- edocs-country-scope -->

{% hint style="info" %}
Consulte o guia do país para conhecer os limites das versões, a configuração efetiva e o vídeo explicativo. [França](countries/france.md). O marcador XML 1p0 e Factur-X XMP Version 1.0 não identificam uma edição da publicação. Mantenha a designação genérica quando a edição for desconhecida.
{% endhint %}

| Propriedade | Valor |
| --- | --- |
| **País / Região** | França / Alemanha |
| **Tipos de documento** | Fatura, nota de crédito |
| **Formato** | CII (PDF/A-3 incorporado) |
| **Padrão** | Factur-X |
| **Baseado em** | EN 16931 |

Um Guideline ID CII harmonizado pode identificar uma família e um perfil, embora várias edições partilhem o mesmo marcador 1p0. Factur-X XMP Version 1.0 é um marcador de esquema, não uma edição da publicação como 1.08 ou 1.09. O XMP do ZUGFeRD pode declarar a sua versão. Se não existirem metadados fiáveis, mantenha o resultado da família genérica e confirme o ficheiro original com o remetente.

## Status de suporte

| Componente | Status |
| --- | --- |
| Visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Visualização padrão

<figure><img src="../../../../../../.gitbook/assets/facturx-preview.png" alt="Visualização de fatura Factur-X no DocBits"><figcaption><p>Visualização padrão do DocBits para uma fatura Factur-X da França</p></figcaption></figure>

## Relacionado

* [Configuração do ZUGFeRD](../zugferd/)
* [Mapeamento de campos do ZUGFeRD](../zugferd/README.md)
* [Documentos Eletrônicos Suportados](./)
