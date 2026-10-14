# Melhores práticas

## Mantenha as colunas padrão para valores e quantidades

As verificações de itens de linha (*quantidade × preço unitário = total da linha*) e a correspondência de pedidos de compra (PO matching) procuram as colunas padrão `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `ITEM_NUMBER`. Se você criar colunas próprias para esses valores, as verificações não são executadas e o PO matching informa colunas obrigatórias ausentes. Renomeie o *título* se a redação não for adequada; mantenha a coluna.

## Oculte, não exclua

As colunas padrão de que você não precisa são ocultadas, não excluídas; de qualquer forma, elas não podem ser excluídas. Para as suas próprias colunas, ocultar também é a escolha mais segura enquanto você não tiver certeza de que um script ou um mapeamento de exportação ainda referencia a coluna.

## Marque como obrigatório somente o que bloqueia a exportação

Toda coluna obrigatória precisa estar preenchida em todas as linhas antes que um usuário possa aprovar o documento. Use isso para valores que o ERP rejeita quando ausentes (por exemplo, o centro de custo em uma exportação contábil), não para valores que são apenas úteis.

## Use *Read Only* para valores consultados

Valores que um script ou uma consulta de dados mestres grava na tabela (descrição do artigo a partir do cadastro de itens, código de imposto a partir do fornecedor) devem ser somente leitura, para que os usuários corrijam a origem e não a cópia.

## Use AI por coluna, não por fornecedor

Para um fornecedor com regras treinadas, a maioria das colunas sai correta a partir das regras. Se uma coluna não for confiável (descrições longas que quebram linha, um desconto que às vezes fica em outro lugar), ative *Use AI* somente nessa coluna. As regras continuam cuidando do restante.

## Dê nomes às colunas pensando no ERP, não no documento

O *Column name* vai parar nos mapeamentos de exportação e nos scripts. `COST_CENTRE` é mais fácil de mapear do que `KST` e não muda quando um fornecedor o imprime de forma diferente.

## Teste em um documento reiniciado

Depois de uma alteração, reinicie um documento existente do tipo de documento e abra-o: a nova coluna aparece, a coluna oculta desaparece e as células obrigatórias ficam marcadas. Só depois disso libere para os usuários.

## Uma tabela por estrutura de itens de linha

Crie uma segunda tabela somente quando um tipo de documento realmente tiver duas tabelas independentes (por exemplo, linhas de itens e uma tabela separada de encargos). Tabelas extras vazias aparecem em todos os documentos do tipo.
