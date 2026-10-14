---
description: Suporte a documentos eletrônicos FACTURX no DocBits
---

# 🇫🇷 FACTURX

| Propriedade | Valor |
| --- | --- |
| **País / Região** | França / Alemanha |
| **Tipos de documento** | Fatura, nota de crédito |
| **Formato** | CII (PDF/A-3 incorporado) |
| **Padrão** | Factur-X |
| **Baseado em** | EN 16931 |

O Factur-X é a implementação francesa do padrão híbrido franco-alemão de fatura. Ele incorpora dados XML CII estruturados em um documento PDF/A-3, permitindo um faturamento legível por pessoas e processável por máquinas. O DocBits detecta automaticamente a versão e o perfil do Factur-X a partir do XML incorporado.

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
* [Mapeamento de campos do ZUGFeRD](../zugferd/versions/)
* [Documentos Eletrônicos Suportados](./)
