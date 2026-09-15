# Itens de linha na exportação

O que acontece à tabela de itens de linha quando um documento é aprovado e exportado depende do método de exportação. Esta página explica quais as colunas que saem do DocBits, quais são obrigatórias e porque é que uma exportação pode mostrar menos linhas do que o ecrã de validação.

## Dois tipos de exportação

| Método de exportação | O que é enviado para a tabela |
|---|---|
| **webhook**, **watcher**, **sftp**, **infor_sftp** (JSON / XML) | A tabela tal como está no ecrã de validação: todas as [colunas de tabela](../global-settings/document-types/table-columns.md) não ocultas de todas as linhas, com valor, valor formatado e confiança. |
| **infor-m3-cloud**, **infor-m3-toml-cloud**, **infor-idm-***, **infor-gls840-onpremise**, **infor-m3-oc-charges-onpremise** (BODs Infor ERP / SAP) | Não a tabela em bruto. O DocBits constrói a partir dela **linhas de receção** e **linhas de custo** (ver abaixo) e mapeia-as para os campos do BOD com o mapeamento configurado em [Exportação para Infor](../../../infor-integration-and-configuration/exporting-to-infor/README.md). |

## Linhas de receção e linhas de custo (exportações Infor)

Uma linha de fatura no ERP é ou uma **linha de receção**, que liquida uma receção de ordem de compra, ou uma **linha de custo**, que contabiliza um valor numa conta do razão com dimensões. O DocBits decide por linha de fatura:

* As **linhas de receção** vêm da **correspondência de PO**. Cada linha de fatura que foi associada a uma linha da ordem de compra (Dashboard → PO Match, ou automaticamente com *PO auto match*) torna-se uma linha de receção com o número da ordem de compra, a linha da ordem, a linha de receção e a quantidade e o valor correspondidos. Uma fatura sem correspondência de PO **não tem linhas de receção**; a pré-visualização da exportação mostra então `receipt_lines: []`, o que está correto, não é um bug.
* As **linhas de custo** vêm do **registo contabilístico** que o passo de contabilidade de custos (ou o Auto Accounting) cria: conta do razão, dimensões, valor, quantidade por linha. Uma fatura sem registo contabilístico não tem linhas de custo.
* As **linhas de imposto** são construídas a partir dos valores de imposto do cabeçalho, não da tabela.

Assim, nas exportações Infor, a tabela de itens de linha é a *entrada* da correspondência de PO e da contabilidade; o que o ERP recebe é o resultado desses dois passos. Uma linha que não tem correspondência de PO nem foi contabilizada não chega ao ERP.

{% hint style="warning" %}
Para que a correspondência de PO funcione, a tabela tem de ter as colunas predefinidas **número do artigo, preço unitário, quantidade e valor total**. Se uma delas estiver oculta, o ecrã de validação mostra *Line Item Table is missing Mandatory column for PO* e não é possível construir linhas de receção.
{% endhint %}

## Colunas obrigatórias e a caixa de diálogo de aprovação

Antes de um documento poder ser aprovado, o DocBits verifica a tabela:

1. Todas as colunas marcadas como **Obrigatória** (Definições → Tipos de Documento → Colunas da Tabela) têm de ter um valor em todas as linhas.
2. Todas as linhas têm de passar a **verificação do total da linha**: `total = quantidade × preço unitário + encargos − desconto`, com uma tolerância de 0,02. As linhas que falham são assinaladas; a mensagem indica o valor esperado e o valor real.
3. A **soma dos totais das linhas** é comparada com o valor líquido no cabeçalho. Uma diferença é um aviso e não bloqueia a aprovação.

A caixa de diálogo de aprovação lista o que ainda falta. Um administrador pode desativar todas as verificações de tabela por tipo de documento com **Ignorar validação da tabela** (Tipos de Documento → Mais definições); os totais das linhas e as colunas obrigatórias deixam então de ser verificados, mas as verificações do cabeçalho mantêm-se.

Detalhes das mensagens: [Resolução de Problemas de Extração de Tabelas](../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md#mensagens-na-tabela).

## Tabela vazia

* As **exportações JSON / XML** enviam o documento com `tables: []` (ou a tabela com zero linhas). O sistema recetor tem de lidar com uma tabela vazia.
* As **exportações Infor** sem linhas de receção nem linhas de custo enviam apenas o cabeçalho e as linhas de imposto. A maioria dos ERPs rejeita uma fatura sem linhas; configure o Auto Accounting ou uma linha de custo predefinida para esses tipos de documento, ou encaminhe-os para uma exportação diferente.
* Um tipo de documento **sem tabela** (nenhuma tabela configurada) nunca envia dados de linhas; isso é o esperado para tipos de documento como confirmações de encomenda, que são correspondidos ao nível do cabeçalho.

## Verificar antes de aprovar

Os parceiros e o suporte com acesso à API ou ao MCP podem pedir o payload de exportação de um documento antes de este ser enviado: a ferramenta MCP `get_export_preview(doc_id)` devolve exatamente o que a exportação vai enviar, `receipt_lines`, `cost_lines` e `tax_lines` para exportações Infor, `tables` para exportações JSON. Use-a quando o ERP comunicar linhas em falta: se `receipt_lines` estiver vazio, a fatura não teve correspondência de PO; se `cost_lines` estiver vazio, não existe registo contabilístico.

## Páginas relacionadas

* [Exportação](export.md): configurações e métodos de exportação
* [Colunas da Tabela](../global-settings/document-types/table-columns.md)
* [Exportação para Infor](../../../infor-integration-and-configuration/exporting-to-infor/README.md): mapeamentos de campos BOD para linhas de receção, de custo e de imposto
