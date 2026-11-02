---
description: Suporte para o documento eletrônico KSEF no DocBits
---

# 🇵🇱 KSEF

<!-- edocs-country-scope -->

{% hint style="info" %}
Consulte o guia do país para conhecer os limites das versões, a configuração efetiva e o vídeo explicativo. [Polónia](countries/poland.md). FA2 e FA3 utilizam estruturas diferentes. Confirme o esquema de origem e teste o mapeamento adequado; analisar um ficheiro não submete uma fatura ao KSeF.
{% endhint %}

| Propriedade          | Valor                                    |
| -------------------- | ---------------------------------------- |
| **País / Região**    | Polónia                                  |
| **Tipos de documento** | Fatura, Nota de crédito, Fatura retificativa |
| **Formato**          | XML                                      |
| **Padrão**           | KSeF (Krajowy System e-Faktur)           |

O KSeF é o Sistema Nacional de Faturação Eletrônica polaco, operado pelo Ministério das Finanças. Tornar-se-á obrigatório para todas as empresas polacas registadas para efeitos de IVA. O DocBits suporta as versões de esquema KSeF FA2 e FA3 para o processamento de faturas.

## Status de suporte

| Componente          | Status       |
| ------------------- | ------------ |
| Pré-visualização    | ✅ Suportado |
| Extração de campos  | ✅ Suportado |
| Transformação       | ✅ Suportado |

## Pré-visualização padrão

<figure><img src="../../../../../../.gitbook/assets/ksef-preview.png" alt="Pré-visualização de uma fatura KSeF no DocBits"><figcaption><p>Pré-visualização padrão do DocBits para uma fatura Poland KSeF</p></figcaption></figure>

## Relacionados

* [Documentos eletrônicos suportados](./)
* [KSeF FA2](ksef-fa2.md)
* [KSeF FA3](ksef-fa3.md)
