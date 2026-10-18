---
description: Suporte para o documento eletrônico MYINVOIS no DocBits
---

# 🇲🇾 MYINVOIS

<!-- edocs-country-scope -->

{% hint style="info" %}
Consulte o guia do país para conhecer os limites das versões, a configuração efetiva e o vídeo explicativo. [Malásia](countries/malaysia.md). O caminho de extração examinado baseia-se em XML. A plataforma nacional também aceita JSON, mas isso não comprova o suporte de importação JSON neste mapeamento do DocBits.
{% endhint %}

| Propriedade          | Valor                                                 |
| -------------------- | ----------------------------------------------------- |
| **País / Região**    | Malásia                                               |
| **Tipos de documento** | Fatura, Nota de crédito, Nota de débito, Autofatura |
| **Formato**          | UBL 2.1 XML                                    |
| **Padrão**           | MyInvois (LHDN - Lembaga Hasil Dalam Negeri)          |

O MyInvois é o sistema de faturação eletrônica da Malásia, operado pela Autoridade Tributária (LHDN). Em vigor desde agosto de 2024 para as grandes empresas, exige que todas as faturas sejam submetidas ao portal MyInvois para validação e recebam um identificador único. O sistema utiliza UBL 2.1 e suporta submissões nos formatos XML e JSON.

## Status de suporte

| Componente          | Status       |
| ------------------- | ------------ |
| Pré-visualização    | ✅ Suportado |
| Extração de campos  | ✅ Suportado |
| Transformação       | ✅ Suportado |

## Pré-visualização padrão

<figure><img src="../../../../../../.gitbook/assets/myinvois-preview.png" alt="Pré-visualização de uma fatura MyInvois no DocBits"><figcaption><p>Pré-visualização padrão do DocBits para uma fatura Malaysia MyInvois</p></figcaption></figure>

## Relacionados

* [Documentos eletrônicos suportados](./)
