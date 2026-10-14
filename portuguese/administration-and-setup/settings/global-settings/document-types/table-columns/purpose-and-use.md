# Finalidade e uso

Uma coluna de tabela é um campo da tabela de itens de linha. Tudo o que o DocBits faz com uma tabela (extração, validação, PO matching, exportação) trabalha com as colunas configuradas aqui.

## Onde uma coluna aparece

| Local | O que a coluna faz ali |
|---|---|
| **Tela de validação** | Uma coluna na tabela de itens de linha. O *Title* é o cabeçalho e o *Column Type* define o editor (valor, data, texto, sim/não). As colunas ocultas não são exibidas. |
| **Treinamento de tabelas** | Ao treinar a tabela de um fornecedor, você mapeia cada coluna de tabela detectada para uma destas colunas configuradas. Somente colunas configuradas podem ser mapeadas. |
| **Extração de tabela por IA** | A IA preenche as colunas configuradas. Uma coluna marcada com *Use AI* é preenchida pela IA mesmo para fornecedores com regras treinadas. |
| **Regras de validação** | Verificações de itens de linha, como *quantidade × preço unitário = total da linha*, são executadas nas colunas padrão `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `CHARGES`, `DISCOUNT`. |
| **PO matching** | Precisa das colunas padrão de número do item, preço unitário, quantidade e valor total. Sem elas, o documento exibe *Line Item Table is missing Mandatory column for PO*. |
| **Exportação** | Toda coluna não oculta faz parte dos dados de itens de linha enviados ao ERP. O mapeamento de exportação referencia o *Column name*. |
| **Scripts** | Os scripts leem e gravam colunas pelo *Column name*, por exemplo `row["TOTAL_AMOUNT"]`. |

## Escopo

* As colunas de tabela são configuradas **por tabela**, e uma tabela pertence a um **tipo de documento**. As colunas de fatura não afetam as notas de entrega.
* A configuração é **por organização**. As suborganizações a herdam.
* Quais colunas são *preenchidas* para um determinado fornecedor é decidido pelo treinamento desse fornecedor ou pela IA; a configuração de colunas apenas define quais colunas existem.

## Motivos típicos para alterar a configuração

* Um valor específico do cliente precisa ser capturado por linha (centro de custo, número de projeto, número de artigo interno) → adicione uma coluna.
* Uma coluna padrão nunca é usada e polui a tela de validação → oculte-a.
* Uma coluna sempre precisa estar preenchida antes da exportação → marque-a como *Required*.
* Um valor vem da consulta ao ERP e não deve ser editado pelos usuários → marque-o como *Read Only*.
* A IA captura uma coluna melhor do que as regras treinadas (por exemplo, descrições em texto livre) → marque-a como *Use AI*.

## Páginas relacionadas

* [Adicionando uma nova coluna](adding-a-new-column.md)
* [Editando e excluindo colunas](editing-and-deleting-columns.md)
* [Table Extraction Troubleshoot](../../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md)
