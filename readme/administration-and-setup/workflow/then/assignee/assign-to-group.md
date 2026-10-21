# Atribuir ao grupo

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-4f514f6ba398-pt.png" alt="Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real." width="563"><figcaption><p>Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

## Propósito:

O cartão de fluxo de trabalho **"Assign to Group"** facilita a atribuição de documentos a um **grupo** específico dentro do sistema. Isto assegura que o documento é processado pela equipa adequada, simplificando o fluxo de trabalho. Melhorado em versões posteriores, introduz a funcionalidade de árvore de decisão para a atribuição dinâmica de grupos.

## Componentes do cartão:

1. **Grupos**
   * **Descrição:** Especifica o **grupo** ao qual o documento será atribuído.
   * **Detalhe:** Selecionado a partir de uma lista pendente de **grupos** disponíveis.

## **Componentes adicionais na Versão 3**

1. **Árvore de Decisão (apenas na Versão 3)**
   * **Descrição:** Permite a utilização de uma árvore de decisão para determinar dinamicamente o **grupo** ao qual o documento deve ser atribuído.
   * **Opções:**
     * **True:** Ativa o processamento da árvore de decisão.
     * **False:** Desativa o processamento da árvore de decisão.

## Funcionalidade:

* **Avaliação da condição:** O cartão só executa a sua ação se tanto a secção **"Quando"** como as **"E Seções"** forem avaliadas como verdadeiras.
* **Atribuição do documento:** Atribui o documento ao **grupo** selecionado. Na **Versão 3**, a **árvore de decisão** determina dinamicamente o grupo de destino, se ativada.

## Configuração:

* **Selecionar o Grupo:** Escolha o **grupo** a partir da lista pendente para atribuir o documento.
* **Use Árvore de Decisão (apenas na Versão 3):** Ative esta opção se a **árvore de decisão** deve ser utilizada para a atribuição dinâmica.

## Conclusão:

O cartão de fluxo de trabalho **"Assign to Group"** automatiza a atribuição de documentos a **grupos** predefinidos, melhorando a coordenação das equipas. A **Versão 3** introduz a capacidade de atribuir grupos de forma dinâmica com base na lógica da árvore de decisão.

<!-- workflow-card-practical-example-20261021 -->

## Exemplo prático

**Quando usar:** Coloque um documento em uma fila de revisão compartilhada.

**Configuração:** Selecione o grupo configurado `Demo Finance`.

**Resultado esperado e contra-exemplo:** O documento é atribuído ao grupo selecionado. Esta é uma atribuição de documento, não uma promessa de que uma tarefa ou e-mail adicional será criado.

Esta é uma configuração ilustrativa e resultado esperado. Utilize campos, usuários e grupos configurados em sua organização de teste; não é uma afirmação de que este exemplo foi executado.
