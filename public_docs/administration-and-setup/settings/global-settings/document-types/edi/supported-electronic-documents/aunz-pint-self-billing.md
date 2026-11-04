---
description: Suporte a documentos eletrônicos AUNZ PINT SELF-BILLING no DocBits
---

# 🇦🇺 AUNZ PINT SELF-BILLING

<!-- edocs-country-scope -->

{% hint style="info" %}
Consulte o guia do país para conhecer os limites das versões, a configuração efetiva e o vídeo explicativo. [Austrália](countries/australia.md). A designação da família ativa não tem um número fixo de edição PINT. Verifique os identificadores de personalização e de perfil; a entrega através da rede exige uma integração separada.
{% endhint %}

| Propriedade | Valor |
|----------|-------|
| **País / Região** | Austrália / Nova Zelândia |
| **Tipos de documento** | Fatura de auto-faturação |
| **Formato** | UBL 2.1 XML |
| **Padrão** | PINT A-NZ Self-Billing |
| **Locale** | `en_AU` |

AUNZ PINT Self-Billing é a variante de auto-faturação do modelo de faturação Peppol International A-NZ. Em cenários de auto-faturação, o comprador cria a fatura em nome do fornecedor. Este tipo de documento segue a mesma estrutura PINT A-NZ, mas com papéis de parte invertidos — o `AccountingCustomerParty` torna-se a parte faturadora e o `AccountingSupplierParty` é a parte faturada.

## Estado do suporte

| Componente | Estado |
|-----------|--------|
| Pré-visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Pré-visualização padrão

<figure><img src="../../../../../../.gitbook/assets/aunz-pint-preview.png" alt="Pré-visualização da fatura AUNZ PINT Self-Billing no DocBits"><figcaption><p>Pré-visualização padrão do DocBits para uma fatura AUNZ PINT Self-Billing</p></figcaption></figure>

## Mapeamento de campos

O mapeamento de campos é idêntico ao [AUNZ PINT](aunz-pint.md) com a seguinte diferença principal:

- **Os papéis das partes são invertidos**: Na auto-faturação, o comprador é a parte faturadora e o fornecedor é a parte faturada
- O `CustomizationID` contém `urn:peppol.org:pint:selfbilling-1@aunz` em vez de `billing-1@aunz`

Para a tabela completa de mapeamento de campos, consulte [AUNZ PINT](aunz-pint.md#mapeamento-de-campos).

## Regra de classificação

O DocBits detecta documentos de auto-faturação correspondendo ao `CustomizationID`:

```
urn:peppol.org:pint:selfbilling-1@aunz
```

Tanto a auto-faturação como a faturação regular são classificadas sob o tipo de documento eletrônico `PINT A-NZ`.

## Veja também

- [AUNZ PINT](aunz-pint.md)
- [Documentos eletrônicos suportados](./)
