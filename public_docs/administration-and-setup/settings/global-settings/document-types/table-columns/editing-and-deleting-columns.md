# Editando e excluindo colunas

As caixas controlam valores obrigatórios, edição e visibilidade. Use AI é configurado separadamente na lista de três estados explicada abaixo.

Tudo, exceto o título, é alterado diretamente na lista; não há caixa de diálogo de edição.

**Onde:** Settings → Document Processing → Document Types → Table Columns

## Alterando um indicador

Marque ou desmarque a caixa de seleção na linha. A alteração é salva imediatamente (*Successfully saved*).

| Indicador | Ativado | Desativado |
|---|---|---|
| **Is Required** | A aprovação é bloqueada enquanto a coluna estiver vazia em qualquer linha; a tela de validação marca a célula. | Células vazias são permitidas. |
| **Read Only** | O valor é exibido, mas não pode ser sobrescrito. Use para valores que vêm de uma consulta ou de um script. | Os usuários podem editar a célula. |
| **Hidden** | A coluna desaparece da tela de validação e da exportação. Os dados dela são mantidos. | A coluna é exibida e exportada. |


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

## Use AI: Padrão, Sim ou Não

Abra [Colunas de tabela](README.md) para o tipo de documento e a tabela corretos. **Usar IA (Use AI)** é uma lista de três estados, não uma caixa de seleção. A alteração é salva imediatamente.

| Opção atual | Efeito no esquema base |
| --- | --- |
| **Default · solicitado** ou **Default · não solicitado** | Usa a seleção DocBits para esse tipo e nome de coluna. Padrão não significa sempre ativado nem sempre desativado. |
| **Yes · solicitado** | Solicita explicitamente essa coluna configurada à IA. |
| **Não · não solicitado** | Exclui a coluna do esquema base, mesmo que normalmente seja solicitada. |

Voltar a **Default** remove a escolha explícita. Uma coluna própria recém-criada normalmente não pertence à seleção padrão de IA: escolha **Yes** para solicitá-la. As colunas padrão de IA não são todas as colunas fornecidas. Verifique o efeito indicado e a prévia.

**Required**, **Read Only** e **Hidden** controlam completude, edição e visibilidade; não substituem a escolha de IA. **Não** não exclui a coluna nem apaga valores, e não impede que regras, scripts ou outras fontes a preencham. Treinamento do fornecedor e tags de IA podem ampliar a solicitação efetiva: resolva também ali as contradições. O interruptor não substitui automaticamente um resultado obtido apenas por regras.

[Structured Output para tabelas](../../../../../end-user-and-partner-section/end-user-section/ai-table/structured-output.md).
