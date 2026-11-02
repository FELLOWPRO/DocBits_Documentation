# Solução de problemas

## A nova coluna não aparece na tela de validação

* O documento foi processado antes de a coluna ser adicionada. As alterações se aplicam a documentos enviados ou reiniciados depois; **reinicie o documento** (Dashboard → menu do documento → Restart).
* A coluna está **Hidden**. Verifique o indicador na lista de Table Columns.
* A coluna foi adicionada a uma **tabela diferente** da exibida. A tela de validação mostra as tabelas do tipo de documento; compare a coluna *Table name*.
* O documento não é do tipo de documento que você configurou.

## A coluna existe, mas está sempre vazia

* O fornecedor tem **regras treinadas** e a nova coluna não está mapeada nelas. Abra um dos documentos do fornecedor no treinamento de tabelas e mapeie a coluna, ou ative *Use AI* na coluna.
* Com a extração por IA, o valor não é reconhecível no documento (sem cabeçalho, abreviado, em outro idioma). Adicione uma [AI table tag](../../../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md) que nomeie a coluna, ou mapeie-a no treinamento.

## "Column name already exists"

Já existe na tabela uma coluna com o mesmo nome técnico. Se ela não estiver na lista, trata-se de uma coluna padrão oculta: a mensagem diz *Please activate it in Table Column settings*. Desative *Hidden* nessa coluna em vez de criar uma nova.

## A aprovação está bloqueada por uma coluna obrigatória

A mensagem na tabela informa o nome da coluna. Preencha a célula em todas as linhas ou, se o valor não existir neste documento, desmarque *Is Required* da coluna, reinicie o documento e tente novamente. Avalie se a coluna deve realmente ser obrigatória (consulte [Melhores práticas](best-practices-2.md)).

## A IA preenche uma coluna com o valor errado

Caso típico: `CHARGES` recebe o total da linha e, então, todas as linhas falham na verificação do total da linha com *Line total does not match quantity x unit price (expected …, got …)*, porque os encargos fazem parte da fórmula `quantidade × preço unitário + encargos`.

* Desmarque *Use AI* na coluna se as regras treinadas a capturarem corretamente.
* Se o fornecedor não tiver regras, treine a tabela uma vez (treinamento de tabelas) para que a coluna seja vinculada à posição correta, ou oculte a coluna se o fornecedor nunca imprimir esse valor.
* Como último recurso, *Skip table validation* em More Settings do tipo de documento desativa todas as verificações de tabela para todo o tipo de documento; a divergência deixa de ser detectada, assim como as colunas obrigatórias vazias.

## PO matching: "Line Item Table is missing Mandatory column"

O PO matching precisa das colunas padrão de número do item, preço unitário, quantidade e valor total. Uma delas está oculta ou foi substituída por uma coluna personalizada. Reexiba a coluna padrão ou mapeie o valor para ela no treinamento de tabelas.

## Um script ou uma exportação falha depois de excluir uma coluna

O script ou o mapeamento de exportação ainda referencia o *Column name* excluído. Remova a referência ou adicione a coluna novamente com o mesmo título; o nome técnico é derivado do título e volta a corresponder.

## Onde procurar mais informações

* [Table Extraction Troubleshoot](../../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md): qualidade da extração, OCR, E-Text
* [Treinar campos de linha e tabelas](../../../../setup/document-training/training-line-fields-table-training/README.md)
