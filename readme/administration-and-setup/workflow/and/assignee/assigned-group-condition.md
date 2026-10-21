# Condição de grupo atribuída

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-bdcdca2a5488-pt.png" alt="Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real." width="563"><figcaption><p>Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

**Propósito:**

Este cartão de fluxo de trabalho executa operações com base no facto de uma tarefa ou documento estar atribuído a um determinado grupo ou conjunto de grupos. Utiliza lógica condicional para acionar ou impedir ações específicas consoante a atribuição de grupo, sendo ideal para fluxos de trabalho que exijam tratamento específico por grupo.

**Componentes do cartão:**

1. **Operador**
   * **Descrição:** Define a condição lógica a aplicar à atribuição de grupo.
   * **Opções:**
     * **IS:** Aciona a operação se o grupo atribuído ao documento ou tarefa corresponder a um dos grupos da lista especificada.
     * **NÃO É:** Aciona a operação se o grupo atribuído ao documento ou tarefa não corresponder a nenhum dos grupos da lista especificada.
2. **Lista de grupos**
   * **Descrição:** Uma lista ou seleção de grupos a comparar com o grupo atribuído.
   * **Detalhe:** Esta lista pode incluir um ou vários grupos, permitindo que o cartão trate eficazmente tanto condições de grupo único como de grupos múltiplos.

**Funcionalidade:**

* **Identificação da atribuição de grupo:** Identifica automaticamente o grupo ou grupos atribuídos a uma determinada tarefa ou documento dentro do sistema.
* **Avaliação da condição:**
  * Com o operador **IS**, o cartão verifica se o grupo atribuído é um dos grupos indicados na Groups List.
  * Com o operador **NÃO É**, o cartão garante que o grupo atribuído não faz parte dos grupos indicados.
* **Execução da ação:**
  * **Condição Verdadeira:** Se a atribuição de grupo cumprir a condição (**IS** ou **NÃO É**), são acionadas as ações relevantes, como notificações, início de tarefas, aprovações ou outros passos do fluxo de trabalho.
  * **Condição Falsa:** Se a condição não for cumprida, o fluxo de trabalho não continuará.

**Interações do utilizador:**

* **Configuração:** Os utilizadores configuram o cartão selecionando um operador e especificando os grupos relevantes a partir da Groups List. A configuração deve ser simples e intuitiva, de modo a acomodar seleções a partir de bases de grupos potencialmente extensas.
* **Monitorização e relatórios:**\
  O sistema deve disponibilizar funcionalidades para monitorizar e gerar relatórios sobre as operações acionadas por este cartão, oferecendo informações sobre a precisão das atribuições e a eficiência do processo.
* **Tratamento de erros e notificações:**\
  Os utilizadores devem ter a opção de receber alertas ou notificações caso existam problemas com as atribuições, como tarefas não atribuídas ou erros na seleção de grupos.

**Conclusão:**\
O cartão de fluxo de trabalho "Assigned Group Condition" é essencial para gerir fluxos de documentos e tarefas que dependem de atribuições de grupo. Ao permitir condições baseadas no facto de uma tarefa ou documento estar atribuído a grupos específicos, garante que os fluxos de trabalho só são acionados por interações de grupo apropriadas, melhorando a responsabilização e a gestão de tarefas entre equipas.

<!-- workflow-card-practical-example-20261021 -->

## Exemplo prático

**Quando usar:** Aplique a mesma regra a duas equipes de revisão.

**Configuração:** Selecione is-one-of e os grupos configurados `Demo Finance` e `Demo Procurement`.

**Resultado esperado e contra-exemplo:** Um documento atribuído a qualquer um dos grupos selecionados é aprovado. Um documento atribuído apenas a `Demo Support` falha.

Esta é uma configuração ilustrativa e resultado esperado. Utilize campos, usuários e grupos configurados em sua organização de teste; não é uma afirmação de que este exemplo foi executado.
