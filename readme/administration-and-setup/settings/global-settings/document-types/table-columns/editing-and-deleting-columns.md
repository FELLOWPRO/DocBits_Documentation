# Editando e excluindo colunas

Tudo, exceto o título, é alterado diretamente na lista; não há caixa de diálogo de edição.

**Onde:** Settings → Global Settings → Document Types → Table Columns

## Alterando um indicador

Marque ou desmarque a caixa de seleção na linha. A alteração é salva imediatamente (*Successfully saved*).

| Indicador | Ativado | Desativado |
|---|---|---|
| **Is Required** | A aprovação é bloqueada enquanto a coluna estiver vazia em qualquer linha; a tela de validação marca a célula. | Células vazias são permitidas. |
| **Read Only** | O valor é exibido, mas não pode ser sobrescrito. Use para valores que vêm de uma consulta ou de um script. | Os usuários podem editar a célula. |
| **Hidden** | A coluna desaparece da tela de validação e da exportação. Os dados dela são mantidos. | A coluna é exibida e exportada. |
| **Use AI** | A extração de tabela por IA preenche esta coluna, inclusive para fornecedores que têm regras treinadas. | A coluna é preenchida pelas regras treinadas ou pela IA quando não existem regras. |

{% hint style="info" %}
Os indicadores passam a valer para documentos enviados ou reiniciados **depois** da alteração. Documentos abertos mantêm a tabela atual até serem reiniciados.
{% endhint %}

## Renomeando o título

Clique no ícone de tradução na coluna *Actions* (*Update translation key*), informe o novo rótulo e confirme. O ícone de informações ao lado mostra qual rótulo está em vigor no momento e de onde ele vem. Somente o rótulo muda; o *Column name* técnico permanece o mesmo, de modo que scripts, mapeamentos de exportação e regras treinadas continuam funcionando.

## Alterando o tipo ou a tabela

Não é possível. Oculte a coluna (ou exclua-a, se for sua) e adicione uma nova com o tipo correto.

## Excluindo uma coluna

A ação de exclusão só é oferecida para colunas criadas pela sua organização. As colunas padrão não podem ser excluídas; oculte-as.

1. Abra o menu de três pontos na coluna *Actions* e escolha **Delete**. A opção não existe para colunas padrão.
2. Confirme.

O que acontece:

* A coluna é removida da configuração. Os documentos processados **a partir de agora** não a terão mais.
* Os documentos já extraídos mantêm a coluna e seus valores até serem reiniciados.
* As regras treinadas que mapeavam esta coluna continuam funcionando para as outras colunas; o mapeamento da coluna excluída é ignorado.
* Se a coluna for referenciada em um mapeamento de exportação ou em um script, remova essa referência; caso contrário, a exportação ou o script falha com um erro de coluna ausente.

## Desfazendo uma exclusão

Uma coluna excluída não pode ser restaurada pela lista. Adicione-a novamente com o mesmo título: o nome técnico é derivado do título, portanto uma coluna criada com o mesmo título recebe o mesmo *Column name* e os mapeamentos existentes voltam a corresponder.
