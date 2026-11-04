# Condição de usuário única atribuída

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_user_is_isnot_v2-pt-pt.png" alt="Condição de usuário única atribuída, Versão 2" width="634"><figcaption><p>Versão 2</p></figcaption></figure>

**Propósito**

Este cartão de fluxo de trabalho facilita operações com base na atribuição de uma tarefa ou documento a um único utilizador específico. Utilizando uma abordagem de lógica condicional direta, gere fluxos de trabalho que exigem o envolvimento direcionado de um utilizador, assegurando precisão no tratamento de tarefas baseadas em utilizadores.

**Componentes do cartão**

1. **Operador**
   * **Descrição**: Especifica a lógica a aplicar à atribuição de utilizador.
   * **Opções**:
     * **IS**: Aciona a operação se o utilizador atribuído ao documento ou tarefa corresponder ao utilizador especificado.
     * **NÃO É**: Aciona a operação se o utilizador atribuído não corresponder ao utilizador especificado.
2. **Usuário**
   * **Descrição**: Permite selecionar um único utilizador com o qual o utilizador atribuído será comparado.
   * **Detalhe**: Envolve uma simples lista pendente ou campo de preenchimento automático onde se pode selecionar um utilizador de cada vez.

**Funcionalidade**

* **Identificação da atribuição de utilizador**: Identifica o utilizador atualmente atribuído a uma determinada tarefa ou documento.
* **Avaliação da condição**:
  * Para o operador **IS**, o cartão verifica se o utilizador atribuído é o mesmo que o utilizador selecionado.
  * Para o operador **NÃO É**, verifica que o utilizador atribuído é diferente do utilizador selecionado.
* **Execução da ação**:
  * **Condição Verdadeira**: Se a atribuição cumprir a condição definida (IS ou IS NOT), aciona ações predefinidas, que podem incluir avançar com aprovações, iniciar novas tarefas, enviar notificações ou outros fluxos de trabalho relacionados.
  * **Condição Falsa**: Se a condição não for cumprida, o fluxo de trabalho não continuará.

**Interações do utilizador**

* **Configuração**: Os utilizadores configuram o cartão escolhendo um operador e selecionando um utilizador no campo de utilizador. Esta configuração deve ser direta, assegurando uma seleção e configuração de utilizador simples.
* **Monitorização e relatórios**: Oferece ferramentas para monitorizar o desempenho do cartão, como acompanhar quais as tarefas acionadas por atribuições de utilizador específicas e os resultados desses acionamentos.
* **Tratamento de erros e notificações**: Disponibiliza mecanismos para alertar os utilizadores caso as tarefas sejam atribuídas incorretamente ou ocorram erros operacionais devido a problemas de atribuição.

#### Conclusão

O cartão de fluxo de trabalho "Single Assigned User Condition" é essencial para uma gestão precisa de documentos e tarefas específica por utilizador dentro de um sistema ERP. Simplifica os fluxos de trabalho ao focar-se em atribuições individuais de utilizador, assegurando assim que as ações só são executadas quando apropriado, com base no papel e nas responsabilidades do utilizador. Documentar este cartão com clareza ajudará os utilizadores a compreender a sua aplicação, permitindo-lhes implementá-lo e geri-lo eficazmente nas suas operações diárias. Esta documentação garante que todos os potenciais utilizadores possam compreender facilmente o propósito do cartão e integrá-lo de forma transparente nos seus fluxos de trabalho.

<!-- workflow-card-practical-example-20261021 -->

## Exemplo prático

**Quando usar:** Lida com a fila de um revisor específico.

**Configuração:** Selecione o operador igual e `Demo Reviewer A`.

**Resultado esperado e contra-exemplo:** Um documento atribuído a esse usuário é aprovado; outro usuário atribuído falha.

Esta é uma configuração ilustrativa e resultado esperado. Utilize campos, usuários e grupos configurados em sua organização de teste; não é uma afirmação de que este exemplo foi executado.
