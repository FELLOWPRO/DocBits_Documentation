# Tabela de IA

A Tabela Extraída por IA é a tabela de itens de linha que o DocBits lê com IA quando um fornecedor não tem regras de tabela treinadas. Aparece no ecrã de validação por baixo dos campos de cabeçalho. Esta página explica quando a obtém, como a voltar a executar e como orientar o que ela extrai.

## Quando obtém a tabela de IA

* Um administrador ativou a **Extração de tabelas por IA** (Definições → Processamento de Documentos → Classificação e Extração). Se estiver desativada, a área da tabela mostra *AI Table will display here. Enable in …*.
* O fornecedor **não tem regras guardadas**. Assim que alguém treina a tabela do fornecedor e clica em *Guardar regras*, as regras guardadas substituem a tabela de IA para esse fornecedor; as linhas passam a aparecer no separador *Tabela extraída* em vez do separador *Tabela extraída por IA*.
* Exceção: as colunas marcadas como **Usar IA** nas definições de colunas da tabela são preenchidas pela IA mesmo para fornecedores com regras guardadas, ver [Usar IA por coluna](#usar-ia-por-coluna).

O nível de IA que lê a tabela (Fast, Full, Nexus) é definido por organização e pode ser substituído por fornecedor em *Mais definições* no ecrã de validação, ver [Modelo de IA específico do fornecedor](../validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

## Extrair novamente a tabela de IA

Use esta opção quando faltam linhas ou uma coluna está desalinhada e quer que a IA tente de novo, por exemplo depois de adicionar uma [tag](ai-table-tags.md):

1. Adicione ou altere [tags](ai-table-tags.md) no campo por baixo da tabela e clique em **Aplicar**. A IA reconstrói a tabela para este documento com as suas tags e alterações de colunas; ainda nada é guardado para o fornecedor. Se o documento tiver linhas com correspondência de PO, o DocBits avisa que as correspondências são removidas pela reconstrução.
2. Satisfeito com o resultado? Clique em **Guardar** (*Guardar regras*) para que o próximo documento deste fornecedor seja extraído da mesma forma.
3. Para recomeçar, clique em **Eliminar** (*Eliminar regras*): o DocBits confirma *Rules has been deleted successfully* e volta a executar a extração por IA sem quaisquer tags ou formatação guardadas.

*Eliminar regras* remove as tags e as regras de formatação guardadas para este fornecedor, não a configuração das colunas da tabela. Para extrair novamente o documento inteiro (cabeçalho e tabela) depois de um administrador alterar definições ou colunas, use antes *Reiniciar* no menu do documento no dashboard.

## Usar IA por coluna

Cada coluna da tabela tem uma opção **Usar IA** (Definições → Definições Globais → Tipos de Documento → [Colunas da Tabela](../../../administration-and-setup/settings/global-settings/document-types/table-columns.md)). Com a opção ativada, a IA preenche essa coluna mesmo quando o fornecedor tem regras guardadas; as outras colunas continuam a vir das regras. Utilização típica: uma coluna de descrição em texto livre que as regras treinadas captam mal, ou um valor que muda de posição na página.

Tenha em atenção que a IA passa então a inferir essa coluna a partir da linha inteira. Se colocar sistematicamente o valor errado nessa coluna (por exemplo, o total da linha em *Encargos*), a verificação do total da linha falha em todas as linhas. Nesse caso, desative *Usar IA* nessa coluna ou adicione uma tag que diga à IA o que a coluna é.

## Extração estruturada

Com a opção **Usar Extração estruturada (IA)** ativada nas definições da organização, a IA devolve a tabela numa estrutura fixa que é mapeada diretamente para as colunas de tabela configuradas, em vez de copiar os cabeçalhos de coluna do fornecedor. Os nomes das colunas correspondem então sempre à sua configuração; uma coluna que o fornecedor imprime mas que não configurou não é extraída. Peça ao seu administrador para a ativar quando os cabeçalhos dos fornecedores variam muito e perde tempo a remapear.

## Trabalhar com a tabela extraída

Aqui estão as principais capacidades e instruções de uso:

* **Excluindo Colunas**: Se certas colunas na tabela extraída não forem necessárias, os usuários podem removê-las facilmente clicando no ícone "Excluir coluna" (representado por três pontos verticais) ao lado do cabeçalho da coluna. Isso ajuda a desordenar a tabela e focar apenas nas informações relevantes.

<figure><img src="../../../.gitbook/assets/ai-table1.png" alt=""><figcaption></figcaption></figure>

* **Mudando o Formato da Moeda**: O formato da moeda pode ser alterado selecionando o formato desejado no menu suspenso ao lado do campo "Moeda". Isso garante que os valores monetários sejam exibidos no formato preferido, facilitando a interpretação e análise dos dados financeiros.

<figure><img src="../../../.gitbook/assets/ai-table2.png" alt=""><figcaption></figcaption></figure>

* **Mostrando/Ocultando Colunas Não Mapeadas**: Por padrão, apenas as colunas mapeadas (colunas com dados extraídos) são visíveis na tabela. No entanto, os usuários podem optar por mostrar ou ocultar as colunas não mapeadas clicando no botão "Ocultar colunas não mapeadas" ou "Mostrar colunas não mapeadas" na parte inferior da tabela. Esse recurso é útil quando os usuários desejam revisar todas as colunas disponíveis, mesmo que atualmente não contenham dados.

<figure><img src="../../../.gitbook/assets/ai-table3.png" alt=""><figcaption></figcaption></figure>

* **Mudando os Cabeçalhos da Tabela**: Os cabeçalhos da tabela (nomes das colunas) podem ser modificados clicando no cabeçalho e inserindo o nome desejado. Esse recurso permite que os usuários personalizem os nomes das colunas para alinhar melhor com sua terminologia ou preferências, tornando os dados mais legíveis e compreensíveis.

<figure><img src="../../../.gitbook/assets/ai-table4.png" alt=""><figcaption></figcaption></figure>

* **Guardar o que alterou**: **Guardar** ao lado das tags (dica *Guardar regras*) guarda o mapeamento de colunas atual, as colunas ocultas e as tags para este fornecedor. O próximo documento do fornecedor é extraído com eles.

Estas funcionalidades dão-lhe controlo sobre os dados extraídos. Quando o mesmo fornecedor precisa sempre das mesmas correções, treine antes a tabela uma vez, [Treino de campos de linha / Treino de tabelas](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md), e a tabela de IA deixa de ser usada para esse fornecedor.
