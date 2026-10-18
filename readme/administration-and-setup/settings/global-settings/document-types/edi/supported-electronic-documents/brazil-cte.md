---
description: Suporte a documentos eletrônicos BRAZIL CT-E no DocBits
---

# 🇧🇷 BRAZIL CT-E

<!-- edocs-country-scope -->

{% hint style="info" %}
Consulte o guia do país para conhecer os limites das versões, a configuração efetiva e o vídeo explicativo. [Brasil](countries/brazil.md). São famílias de documentos diferentes. Uma versão NFS-e configurada não certifica todos os esquemas municipais nem todos os formatos nacionais de faturas de serviços.
{% endhint %}

| Propriedade | Valor |
| --- | --- |
| **País / Região** | Brasil |
| **Tipos de documento** | Fatura de transporte (Conhecimento de Transporte Eletrônico) |
| **Formato** | XML |
| **Padrão** | CT-e 3.0 (conhecimento de transporte/frete eletrônico) |
| **Idioma** | `pt_BR` |

O CT-e (Conhecimento de Transporte Eletrônico, `<mod>57</mod>`) é o documento eletrônico de transporte brasileiro emitido por empresas de logística e de frete. Ele documenta o serviço de transporte, o valor da carga, os municípios de origem e destino (`cMunIni` / `cMunFim`) e o preço do frete (`vTPrest`). Diferentemente da NF-e, o CT-e usa `cteProc` como elemento raiz e faz referência a documentos NF-e vinculados.

## Status de suporte

| Componente | Status |
| --- | --- |
| Visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Visualização padrão

<figure><img src="../../../../../../.gitbook/assets/brazil-cte-preview.png" alt="Visualização de CT-e do Brasil no DocBits"><figcaption><p>Visualização padrão do DocBits para um documento BRAZIL CT-E</p></figcaption></figure>

## Mapeamento de campos

### Campos de cabeçalho

| Campo DocBits | XPath de origem | Observações |
| --- | --- | --- |
| `invoice_id` | `//*[local-name()='ide']/*[local-name()='nCT']` | Número do CT-e |
| `invoice_date` | `//*[local-name()='ide']/*[local-name()='dhEmi']` | ISO 8601 com deslocamento BRT |
| `currency` | Fixo: `BRL` | Sempre real brasileiro |
| `total_amount` | `//*[local-name()='vPrest']/*[local-name()='vTPrest']` | Valor total do serviço de frete |
| `net_amount` | `//*[local-name()='vPrest']/*[local-name()='vRec']` | Valor a receber |
| `tax_amount` | `//*[local-name()='ICMS']//*[local-name()='vICMS']` | ICMS sobre o serviço de transporte |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']` | Nome da transportadora |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']` | CNPJ da transportadora |
| `buyer_name` | `//*[local-name()='dest']/*[local-name()='xNome']` | Nome do destinatário |
| `buyer_id` | `//*[local-name()='dest']/*[local-name()='CNPJ']` | CNPJ do destinatário |

> O CT-e não inclui uma tabela de itens — o serviço de transporte é uma cobrança única em nível de documento.

## Regra de classificação

O DocBits detecta documentos BRAZIL CT-E por meio de:

```
http://www.portalfiscal.inf.br/cte
```

no namespace XML (elemento raiz `<cteProc>`).

## Relacionado

* [BRAZIL NF-E](brazil-nfe.md)
* [BRAZIL NFC-E](brazil-nfce.md)
* [BRAZIL NFS-E](brazil-nfse.md)
* [Documentos Eletrônicos Suportados](./)
