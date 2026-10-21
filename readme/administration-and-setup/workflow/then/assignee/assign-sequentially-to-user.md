# Atribuir sequencialmente ao usuário

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-5b15eaee7258-pt.png" alt="Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real." width="563"><figcaption><p>Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

## **Propósito**

O cartão de fluxo de trabalho "**Atribuir sequencialmente ao usuário**" automatiza a atribuição de documentos a um utilizador selecionado de forma sequencial. O valor de prioridade determina a ordem de atribuição, sendo que números mais baixos representam uma prioridade mais elevada.

## **Componentes do cartão**

1. **Usuário**
   * **Descrição**: O utilizador selecionado receberá o documento com base na sequência do fluxo de trabalho.
   * **Detalhe**: Um menu pendente que lista todos os utilizadores disponíveis para atribuição.
2. **Prioridade (Valor)**
   * **Descrição**: Um campo de introdução numérica onde se pode definir o nível de prioridade do utilizador.
   * **Detalhe**: Números mais baixos significam prioridade mais elevada. Os documentos são atribuídos aos utilizadores por ordem crescente de prioridade.

## **Funcionalidade**

* **Atribuição de documentos**:\
  O cartão atribui documentos ao utilizador selecionado de forma sequencial, tendo em conta o nível de prioridade.\
  Se vários utilizadores tiverem a mesma prioridade, os documentos são atribuídos pela ordem em que os utilizadores aparecem no menu pendente.

## **Configuração**

1. Adicione o cartão **Atribuir o documento sequencialmente** ao seu fluxo de trabalho.
2. Configure o campo **Usuário**:
   * Selecione um utilizador no menu pendente.
3. Configure o campo **Prioridade (Valor)**:
   * Introduza um valor numérico para definir a prioridade de atribuição.
4. Guarde e ative o fluxo de trabalho para aplicar a configuração.

## **Conclusão**

O cartão de fluxo de trabalho "Assign the Document Sequentially to User" assegura uma distribuição organizada de documentos ao atribuí-los numa sequência priorizada. Isto melhora a gestão de tarefas e reduz atrasos no processamento.

<!-- workflow-card-practical-example-20261021 -->

## Exemplo prático

**Quando usar:** Adicione um usuário a uma sequência de aprovação de documento priorizada.

**Configuração:** Selecione `Demo Reviewer A` e prioridade `10`. Adicione uma tarefa separada com prioridade `20` quando for necessário um revisor posterior.

**Resultado esperado e contraexemplo:** As atribuições carregam as prioridades configuradas; o valor numérico mais baixo tem prioridade mais alta. Verifique a sequência das tarefas, não apenas a ordem dos cartões na tela.

Esta é uma configuração ilustrativa e resultado esperado. Utilize campos, usuários e grupos configurados em sua organização de teste; não é uma afirmação de que este exemplo foi executado.
