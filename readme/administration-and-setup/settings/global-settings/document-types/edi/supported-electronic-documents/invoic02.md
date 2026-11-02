---
description: Suporte para o documento eletrônico INVOIC02 no DocBits
---

# INVOIC02

<!-- edocs-country-scope -->

{% hint style="info" %}
Consulte o guia do país para conhecer os limites das versões, a configuração efetiva e o vídeo explicativo. [Internacional](countries/international.md). Os mapeamentos de faturas, encomendas, respostas e expedições são distintos. O processamento de ficheiros, por si só, não disponibiliza um ponto de acesso Peppol nem conectividade com parceiros comerciais.
{% endhint %}

| Propriedade          | Valor                   |
| -------------------- | ----------------------- |
| **País / Região**    | Internacional           |
| **Tipos de documento** | Fatura                |
| **Formato**          | EDIFACT                 |
| **Padrão**           | UN/EDIFACT INVOIC D.02B |

O INVOIC02 é uma mensagem de fatura UN/EDIFACT baseada na versão de diretório D.02B. O EDIFACT (Electronic Data Interchange for Administration, Commerce and Transport) é um padrão EDI amplamente utilizado na logística, no retalho e na indústria transformadora. O DocBits analisa a estrutura de segmentos EDIFACT e extrai os campos de cabeçalho, de linhas de itens e de resumo.

## Status de suporte

| Componente          | Status       |
| ------------------- | ------------ |
| Pré-visualização    | ✅ Suportado |
| Extração de campos  | ✅ Suportado |
| Transformação       | ✅ Suportado |

## Pré-visualização padrão

<figure><img src="../../../../../../.gitbook/assets/invoic02-preview.png" alt="Pré-visualização de uma fatura INVOIC02 no DocBits"><figcaption><p>Pré-visualização padrão do DocBits para uma fatura INVOIC02</p></figcaption></figure>

## Relacionados

* [Documentos eletrônicos suportados](./)
