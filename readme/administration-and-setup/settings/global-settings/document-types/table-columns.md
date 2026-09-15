# Colunas da Tabela

As colunas da tabela definem quais as colunas que a tabela de itens de linha de um tipo de documento tem: o que o DocBits extrai para cada coluna, o que o utilizador vê no ecrã de validação e o que é enviado para o ERP na exportação.

**Onde:** Definições → Definições Globais → Tipos de Documento → Colunas da Tabela

<figure><img src="../../../../.gitbook/assets/table-columns_list.png" alt="Lista de Colunas da Tabela com as opções Obrigatória, Só de leitura, Oculta e Usar IA por coluna"><figcaption><p>Colunas da Tabela: uma linha por coluna, as opções são alteradas diretamente na lista</p></figcaption></figure>

## O que vê

Cada linha corresponde a uma coluna de uma tabela. A lista mostra:

| Coluna | Significado |
|---|---|
| **Nome da coluna** | Nome técnico, gerado a partir do título (maiúsculas, sublinhados). Usado em scripts, mapeamentos de exportação e na API. Não pode ser alterado posteriormente. |
| **Título** | Etiqueta apresentada no ecrã de validação. Altere-a com o ícone de tradução na coluna *Ações* (*Atualizar chave de tradução*). |
| **Tipo de coluna** | `AMOUNT`, `STRING`, `DATE`, `NUMBER`, `BOOLEAN` ou `CURRENCY`. Determina a validação e a formatação. |
| **Nome da tabela** | A tabela a que a coluna pertence, por exemplo `INVOICE_TABLE`. |
| **Obrigatória** | O documento não pode ser aprovado enquanto esta coluna estiver vazia em qualquer linha. |
| **Só de leitura** | Os utilizadores veem o valor, mas não o podem editar. |
| **Oculta** | A coluna não é apresentada nem exportada. Serve para desativar colunas predefinidas de que não precisa. |
| **Usar IA** | A extração de tabelas por IA preenche esta coluna, mesmo quando o fornecedor tem regras treinadas. |
| **Ações** | Ícone de tradução: alterar o título. Ícone de informação: origem da etiqueta apresentada (a sua tradução, a predefinição, a chave). Menu de três pontos: *Eliminar*, apenas para colunas criadas pela sua organização; as colunas predefinidas só podem ser ocultadas. |

Por cima da lista há dois botões:

* **Criar nova tabela**: uma segunda tabela de itens de linha para o tipo de documento (por exemplo, uma tabela de encargos ao lado da tabela de artigos).
* **Adicionar nova coluna de tabela**: abre a caixa de diálogo descrita na secção *Adicionar uma nova coluna* abaixo.

## Colunas predefinidas e colunas próprias

Cada tipo de documento inclui um conjunto de colunas predefinidas (para faturas: número do artigo, descrição, quantidade, preço unitário, valor total, imposto, …). Pertencem ao DocBits, não à sua organização, pelo que não podem ser eliminadas; em vez disso, oculte-as. As colunas que adiciona pertencem à sua organização e podem ser eliminadas.

{% hint style="info" %}
**As alterações aplicam-se apenas a documentos novos.** Uma coluna que adicione, oculte ou elimine aparece nos documentos carregados ou reiniciados depois da alteração. Os documentos que já estão no dashboard mantêm a tabela tal como foi extraída. Reinicie um documento para que este passe a usar a nova configuração.
{% endhint %}

## Finalidade e utilização

Uma coluna da tabela é um campo da tabela de itens de linha. Tudo o que o DocBits faz com uma tabela (extração, validação, correspondência de PO, exportação) baseia-se nas colunas aqui configuradas.

### Onde uma coluna aparece

| Local | O que a coluna faz aí |
|---|---|
| **Ecrã de validação** | Uma coluna na tabela de itens de linha. O *Título* é o cabeçalho, o *Tipo de coluna* decide o editor (valor, data, texto, sim/não). As colunas ocultas não são apresentadas. |
| **Treino de tabelas** | Ao treinar a tabela de um fornecedor, mapeia cada coluna detetada para uma destas colunas configuradas. Só as colunas configuradas podem ser mapeadas. |
| **Extração de tabelas por IA** | A IA preenche as colunas configuradas. Uma coluna marcada como *Usar IA* é preenchida pela IA mesmo para fornecedores com regras treinadas. |
| **Regras de validação** | As verificações por linha, como *quantidade × preço unitário = total da linha*, correm sobre as colunas predefinidas `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `CHARGES`, `DISCOUNT`. |
| **Correspondência de PO** | Precisa das colunas predefinidas número do artigo, preço unitário, quantidade e valor total. Sem elas, o documento mostra *Line Item Table is missing Mandatory column for PO*. |
| **Exportação** | Todas as colunas não ocultas fazem parte dos dados de itens de linha enviados para o ERP. O mapeamento de exportação referencia o *Nome da coluna*. |
| **Scripts** | Os scripts leem e escrevem colunas pelo *Nome da coluna*, por exemplo `row["TOTAL_AMOUNT"]`. |

### Âmbito

* As colunas da tabela são configuradas **por tabela**, e uma tabela pertence a um **tipo de documento**. As colunas de faturas não afetam as guias de remessa.
* A configuração é **por organização**. As suborganizações herdam-na.
* Quais as colunas que são *preenchidas* para um determinado fornecedor é decidido pelo treino desse fornecedor ou pela IA; a configuração das colunas apenas define quais as colunas que existem.

### Motivos típicos para alterar a configuração

* É necessário captar por linha um valor específico do cliente (centro de custo, número de projeto, número de artigo interno): adicione uma coluna.
* Uma coluna predefinida nunca é usada e sobrecarrega o ecrã de validação: oculte-a.
* Uma coluna tem de estar sempre preenchida antes da exportação: marque-a como *Obrigatória*.
* Um valor vem da consulta ao ERP e não deve ser editado pelos utilizadores: marque-a como *Só de leitura*.
* A IA capta uma coluna melhor do que as regras treinadas (por exemplo, descrições em texto livre): marque-a como *Usar IA*.

## Adicionar uma nova coluna

Adicione uma coluna quando for necessário captar por item de linha um valor que as colunas predefinidas não cobrem: um centro de custo, um número de projeto, um número de artigo interno.

### Antes de começar

* Decida a que **tabela** a coluna pertence. A maioria dos tipos de documento tem uma tabela (por exemplo `INVOICE_TABLE`). Se a lista estiver vazia, clique primeiro em **Criar nova tabela**; a caixa de diálogo pede apenas o nome da tabela.
* Decida o **tipo**: `AMOUNT` para valores monetários, `NUMBER` para quantidades, `DATE`, `BOOLEAN` para sim/não, `CURRENCY` para um código de moeda ISO, `STRING` para tudo o resto. O tipo não pode ser alterado depois de guardar.
* Verifique se já existe uma **coluna predefinida** com o mesmo significado, mas oculta. As colunas ocultas aparecem na lista com a opção *Oculta* ativada; desative-a em vez de criar um duplicado.

### Passos

1. Abra **Definições → Definições Globais → Tipos de Documento → Colunas da Tabela**.
2. Clique em **Adicionar nova coluna de tabela**.

<figure><img src="../../../../.gitbook/assets/table-columns_add-dialog.png" alt="Caixa de diálogo Adicionar nova coluna de tabela com Título, A coluna é obrigatória?, Selecionar tipo de coluna e Selecionar tabela"><figcaption><p>Adicionar nova coluna de tabela</p></figcaption></figure>

3. Preencha a caixa de diálogo:

| Campo | O que introduzir |
|---|---|
| **Título** | Etiqueta que o utilizador vê no ecrã de validação, por exemplo `Cost Centre`. Apenas letras e números. O DocBits deriva daqui o *Nome da coluna* técnico (`COST_CENTRE`). |
| **A coluna é obrigatória?** | Assinale quando o documento não deve poder ser aprovado enquanto a coluna estiver vazia em qualquer linha. |
| **Selecionar tipo de coluna** | Consulte a lista de tipos acima. |
| **Selecionar tabela** | A tabela que recebe a coluna. |

4. Clique em **Continuar**. A coluna aparece na lista com *Só de leitura*, *Oculta* e *Usar IA* desativadas. Se necessário, altere essas opções na lista, ver a secção *Editar e eliminar colunas* abaixo.

### Depois de adicionar

* A coluna está **vazia nos documentos existentes**. É preenchida nos documentos carregados ou reiniciados depois da alteração.
* Para fornecedores com **regras treinadas**, abra um dos seus documentos no treino de tabelas e mapeie a nova coluna; caso contrário, a coluna fica vazia para esse fornecedor. Consulte [Definir tabelas e colunas](../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).
* Com a **extração de tabelas por IA**, a IA preenche a coluna se o valor for reconhecível no documento. Marque a coluna como *Usar IA* se o fornecedor tiver regras treinadas mas esta coluna dever, ainda assim, vir da IA.
* Adicione a coluna ao **mapeamento de exportação** se o ERP a dever receber, ver [Exportação](../../document-processing/export.md).

### Mensagens

| Mensagem | Significado |
|---|---|
| *Column name already exists* | Já existe na tabela uma coluna com este nome técnico. Escolha um título diferente. |
| *Column name already exists – Please activate it in Table Column settings* | Uma coluna predefinida oculta tem este nome. Desative a opção *Oculta* dessa coluna em vez de criar uma nova. |
| *No table exists. Please create table before creating columns.* | O tipo de documento ainda não tem tabela: clique primeiro em **Criar nova tabela**. |

## Editar e eliminar colunas

Tudo, exceto o título, é alterado diretamente na lista; não existe uma caixa de diálogo de edição.

### Alterar uma opção

Assinale ou desmarque a caixa de verificação na linha. A alteração é guardada de imediato (*Successfully saved*).

| Opção | Ativada | Desativada |
|---|---|---|
| **Obrigatória** | A aprovação é bloqueada enquanto a coluna estiver vazia em qualquer linha; o ecrã de validação assinala a célula. | São permitidas células vazias. |
| **Só de leitura** | O valor é apresentado, mas não pode ser substituído. Use-a para valores provenientes de uma consulta ou de um script. | Os utilizadores podem editar a célula. |
| **Oculta** | A coluna desaparece do ecrã de validação e da exportação. Os dados são mantidos. | A coluna é apresentada e exportada. |
| **Usar IA** | A extração de tabelas por IA preenche esta coluna, também para fornecedores que têm regras treinadas. | A coluna é preenchida pelas regras treinadas ou pela IA quando não existem regras. |

{% hint style="info" %}
As opções produzem efeito nos documentos carregados ou reiniciados **depois** da alteração. Os documentos abertos mantêm a tabela atual até serem reiniciados.
{% endhint %}

### Alterar o título

Clique no ícone de tradução na coluna *Ações* (*Atualizar chave de tradução*), introduza a nova etiqueta e confirme. O ícone de informação ao lado mostra qual a etiqueta atualmente em vigor e de onde vem. Só a etiqueta muda; o *Nome da coluna* técnico mantém-se, pelo que os scripts, os mapeamentos de exportação e as regras treinadas continuam a funcionar.

### Alterar o tipo ou a tabela

Não é possível. Oculte a coluna (ou elimine-a, se for sua) e adicione uma nova com o tipo correto.

### Eliminar uma coluna

A ação de eliminar só está disponível para colunas criadas pela sua organização. As colunas predefinidas não podem ser eliminadas; oculte-as.

1. Abra o menu de três pontos na coluna *Ações* e escolha **Eliminar**. Nas colunas predefinidas, esta entrada não existe.
2. Confirme.

O que acontece:

* A coluna é removida da configuração. Os documentos processados **a partir desse momento** deixam de a ter.
* Os documentos já extraídos mantêm a coluna e os seus valores até serem reiniciados.
* As regras treinadas que mapeavam esta coluna continuam a funcionar para as outras colunas; o mapeamento da coluna eliminada é ignorado.
* Se a coluna for referenciada num mapeamento de exportação ou num script, remova essa referência; caso contrário, a exportação ou o script falha com um erro de coluna em falta.

### Anular uma eliminação

Uma coluna eliminada não pode ser restaurada a partir da lista. Adicione-a novamente com o mesmo título: o nome técnico é derivado do título, pelo que uma coluna criada com o mesmo título recebe o mesmo *Nome da coluna* e os mapeamentos existentes voltam a corresponder.

## Boas práticas

### Mantenha as colunas predefinidas para valores e quantidades

As verificações por linha (*quantidade × preço unitário = total da linha*) e a correspondência de PO procuram as colunas predefinidas `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `ITEM_NUMBER`. Se, em vez disso, criar colunas próprias para estes valores, as verificações não correm e a correspondência de PO comunica colunas obrigatórias em falta. Se a designação não lhe agradar, altere o *título*; mantenha a coluna.

### Oculte, não elimine

As colunas predefinidas de que não precisa são ocultadas, não eliminadas; de qualquer forma, não podem ser eliminadas. Para as suas próprias colunas, ocultar é também a opção mais segura enquanto não tiver a certeza de que nenhum script ou mapeamento de exportação ainda referencia a coluna.

### Marque como obrigatório apenas o que bloqueia a exportação

Cada coluna obrigatória tem de estar preenchida em todas as linhas antes de um utilizador poder aprovar o documento. Use-a para valores que o ERP rejeita quando estão em falta (por exemplo, o centro de custo numa exportação contabilística), não para valores que são apenas úteis.

### Use *Só de leitura* para valores obtidos por consulta

Os valores que um script ou uma consulta aos dados mestre escreve na tabela (descrição do artigo a partir dos dados mestre de artigos, código de imposto a partir do fornecedor) devem ser só de leitura, para que os utilizadores corrijam a origem e não a cópia.

### Use a IA por coluna, não por fornecedor

Para um fornecedor com regras treinadas, a maioria das colunas sai correta a partir das regras. Se uma coluna for pouco fiável (descrições longas que quebram linha, um desconto que por vezes está noutro sítio), ative *Usar IA* apenas nessa coluna. As regras mantêm o resto.

### Dê nomes às colunas a pensar no ERP, não no documento

O *Nome da coluna* acaba nos mapeamentos de exportação e nos scripts. `COST_CENTRE` é mais fácil de mapear do que `KST` e não muda quando um fornecedor o imprime de forma diferente.

### Teste num documento reiniciado

Depois de uma alteração, reinicie um documento existente do tipo de documento e abra-o: a nova coluna aparece, a coluna oculta desapareceu, as células obrigatórias estão assinaladas. Só então a disponibilize aos utilizadores.

### Uma tabela por estrutura de itens de linha

Crie uma segunda tabela apenas quando um tipo de documento tiver realmente duas tabelas independentes (por exemplo, linhas de artigos e uma tabela de encargos separada). As tabelas vazias adicionais aparecem em todos os documentos desse tipo.

## Resolução de problemas

### A nova coluna não aparece no ecrã de validação

* O documento foi processado antes de a coluna ser adicionada. As alterações aplicam-se aos documentos carregados ou reiniciados posteriormente; **reinicie o documento** (Dashboard → menu do documento → Reiniciar).
* A coluna está **Oculta**. Verifique a opção na lista de Colunas da Tabela.
* A coluna foi adicionada a uma **tabela diferente** da apresentada. O ecrã de validação mostra as tabelas do tipo de documento; compare a coluna *Nome da tabela*.
* O documento não é do tipo de documento que configurou.

### A coluna existe, mas está sempre vazia

* O fornecedor tem **regras treinadas** e a nova coluna não está mapeada nelas. Abra um dos documentos do fornecedor no treino de tabelas e mapeie a coluna, ou ative *Usar IA* na coluna.
* Com a extração por IA, o valor não é reconhecível no documento (sem cabeçalho, abreviado, noutro idioma). Adicione uma [tag da tabela de IA](../../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md) que identifique a coluna, ou mapeie-a no treino.

### "Column name already exists"

Já existe na tabela uma coluna com o mesmo nome técnico. Se não estiver na lista, é uma coluna predefinida oculta: a mensagem diz *Please activate it in Table Column settings*. Desative *Oculta* nessa coluna em vez de criar uma nova.

### A aprovação é bloqueada por uma coluna obrigatória

A mensagem na tabela indica o nome da coluna. Preencha a célula em todas as linhas ou (se o valor não existir neste documento) desmarque *Obrigatória* na coluna, reinicie o documento e tente novamente. Pondere se a coluna deve sequer ser obrigatória (ver a secção *Boas práticas* acima).

### A IA preenche uma coluna com o valor errado

Caso típico: `CHARGES` recebe o total da linha e, a partir daí, todas as linhas falham a verificação do total da linha com *Line total does not match quantity x unit price (expected …, got …)*, porque os encargos fazem parte da fórmula `quantidade × preço unitário + encargos`.

* Desmarque *Usar IA* na coluna se as regras treinadas a captarem corretamente.
* Se o fornecedor não tiver regras, treine a tabela uma vez (treino de tabelas) para que a coluna fique associada à posição correta, ou oculte a coluna se o fornecedor nunca imprimir esse valor.
* Como último recurso, *Ignorar validação da tabela* nas Mais definições do tipo de documento desativa todas as verificações de tabela para todo o tipo de documento; a discrepância deixa então de ser detetada, tal como as colunas obrigatórias vazias.

### Correspondência de PO: "Line Item Table is missing Mandatory column"

A correspondência de PO precisa das colunas predefinidas número do artigo, preço unitário, quantidade e valor total. Uma delas está oculta ou foi substituída por uma coluna personalizada. Torne a coluna predefinida visível, ou mapeie o valor para ela no treino de tabelas.

### Um script ou uma exportação falha depois de eliminar uma coluna

O script ou o mapeamento de exportação ainda referencia o *Nome da coluna* eliminado. Remova a referência, ou adicione novamente a coluna com o mesmo título; o nome técnico é derivado do título e volta a corresponder.

## Páginas relacionadas

* [Resolução de Problemas de Extração de Tabelas](../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md): qualidade da extração, OCR, E-Text
* [Treino de campos de linha / Treino de tabelas](../../../setup/document-training/training-line-fields-table-training/README.md): ensine ao DocBits onde está a tabela de um fornecedor
* [Tabela de IA](../../../../end-user-and-partner-section/end-user-section/ai-table/README.md): o que o utilizador vê no ecrã de validação
