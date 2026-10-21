# Atribuir documento ao usuário

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-e7f92cca6e9d-pt.png" alt="Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real." width="563"><figcaption><p>Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

## **Propósito:**

O cartão de fluxo de trabalho **"Assign Document to User"** permite aos utilizadores atribuir um documento a um utilizador específico, assegurando uma gestão fluida do fluxo de trabalho ao encaminhar os documentos para a pessoa adequada. A Versão 3 acrescenta a capacidade de utilizar uma árvore de decisão para determinar dinamicamente a atribuição de utilizador com base nas condições disponíveis.

## **Componentes do cartão:**

1. **Usuário**
   * **Descrição:** Especifica o utilizador ao qual o documento será atribuído.
   * **Detalhe:** É disponibilizada uma lista pendente de todos os utilizadores disponíveis para seleção. O utilizador selecionado será o responsável pelo documento para ação adicional.

## **Componentes adicionais na Versão 3:**

1. **Usar árvore de decisão**
   * **Descrição:** Se ativado, o cartão utiliza uma árvore de decisão para determinar dinamicamente a atribuição de utilizador.
   * **Opções:**
     * **True:** Utiliza a árvore de decisão para a atribuição dinâmica de utilizador.
     * **False:** Atribui o documento ao utilizador selecionado sem utilizar a árvore de decisão.

## **Funcionalidade:**

* **Avaliação da condição:**\
  O cartão só executa a sua ação se tanto a secção **"Quando"** como as **"E Seções"** forem avaliadas como verdadeiras.
* **Atribuição do documento:**\
  O cartão atribui o documento ao utilizador selecionado, assegurando que a tarefa é encaminhada para a pessoa adequada para ação. Isto ajuda na responsabilização e numa gestão de documentos eficaz.
* **Árvore de decisão (Versão 3):**\
  Se a árvore de decisão estiver ativada, o cartão avalia as condições definidas dentro da árvore para selecionar dinamicamente o utilizador para a atribuição do documento.

## **Configuração:**

* **Selecionar o User:**\
  Escolha o **utilizador** a partir da lista pendente ao qual o documento será atribuído.
* **Usar Árvore de Decisão (Versão 3):**\
  Ative ou desative a utilização da árvore de decisão para selecionar dinamicamente o utilizador.

## **Conclusão:**

O cartão de fluxo de trabalho **"Assign Document to User"** facilita o encaminhamento eficiente de documentos ao atribuí-los ao utilizador selecionado, com a flexibilidade adicional na Versão 3 de determinar dinamicamente o utilizador através de uma árvore de decisão. Isto assegura um processo de fluxo de trabalho mais adaptável e eficiente.

<!-- workflow-card-practical-example-20261021 -->

## Exemplo prático

**Quando usar:** Envie faturas que necessitam de revisão manual para uma pessoa responsável.

**Configuração:** Selecione o usuário configurado `Demo Reviewer A`.

**Resultado esperado e contra-exemplo:** O documento está atribuído a esse usuário. Confirme a atribuição do documento resultante; este cartão por si só não cria uma tarefa de revisão separada.

Esta é uma configuração ilustrativa e resultado esperado. Utilize campos, usuários e grupos configurados em sua organização de teste; não é uma afirmação de que este exemplo foi executado.
