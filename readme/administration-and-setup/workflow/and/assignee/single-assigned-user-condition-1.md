# Condição de grupo atribuído único

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-d12f96578747-pt.png" alt="Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real." width="563"><figcaption><p>Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

**Propósito:**\
Este cartão de fluxo de trabalho executa operações com base no facto de uma tarefa ou documento estar atribuído a um determinado grupo. Utiliza uma condição simples para acionar ou impedir ações com base na atribuição de grupo.

**Componentes do cartão:**

1. **Operador**
   * **Descrição:** Define a condição lógica a aplicar à atribuição de grupo.
   * **Opções:**
     * **IS:** Aciona a operação se o grupo atribuído ao documento ou tarefa corresponder ao grupo especificado.
     * **NÃO É:** Aciona a operação se o grupo atribuído ao documento ou tarefa não corresponder ao grupo especificado.
2. **Grupo**
   * **Descrição:** Especifica o grupo a comparar com o grupo atribuído.
   * **Detalhe:** Este campo permite selecionar um único grupo para comparar a atribuição.

**Funcionalidade:**

* **Identificação da atribuição de grupo:** Identifica automaticamente o grupo atribuído a uma determinada tarefa ou documento.
* **Avaliação da condição:**
  * Com o operador **IS**, o cartão verifica se o grupo atribuído corresponde ao grupo especificado.
  * Com o operador **NÃO É**, o cartão garante que o grupo atribuído não corresponde ao grupo especificado.
* **Execução da ação:**
  * **Condição Verdadeira:** Se a atribuição de grupo cumprir a condição (**IS** ou **NÃO É**), são acionadas as ações relevantes, como notificações, início de tarefas, aprovações ou outros passos do fluxo de trabalho.
  * **Condição Falsa:** Se a condição não for cumprida, o documento ou tarefa pode seguir um encaminhamento diferente, ou podem ser especificadas ações alternativas.

**Interações do utilizador:**

* **Configuração:**\
  Os utilizadores configuram o cartão selecionando um operador e especificando o grupo relevante. A configuração deve ser simples e intuitiva.
* **Monitorização e relatórios:**\
  O sistema deve disponibilizar funcionalidades para monitorizar e gerar relatórios sobre as operações acionadas por este cartão, oferecendo informações sobre a precisão das atribuições e a eficiência do processo.
* **Tratamento de erros e notificações:**\
  Os utilizadores devem ter a opção de receber alertas ou notificações caso existam problemas com as atribuições, como tarefas não atribuídas ou erros na seleção de grupos.

**Conclusão:**\
O cartão de fluxo de trabalho "Assigned Group Condition" é essencial para gerir fluxos de documentos e tarefas baseados em atribuições de grupo. Ao permitir condições baseadas no facto de uma tarefa ou documento estar atribuído a um grupo específico, garante que os fluxos de trabalho só são acionados pelas interações de grupo apropriadas, melhorando a gestão de tarefas e a eficiência do fluxo de trabalho.

<!-- workflow-card-practical-example-20261021 -->

## Exemplo prático

**Quando usar:** Aplique uma regra à fila de revisão financeira.

**Configuração:** Selecione o operador igual e o grupo `Demo Finance`.

**Resultado esperado e contra-exemplo:** Um documento atribuído a `Demo Finance` é aprovado. A atribuição apenas a um usuário individual não estabelece a associação a esse grupo de atribuição de documentos selecionado.

Esta é uma configuração ilustrativa e resultado esperado. Utilize campos, usuários e grupos configurados em sua organização de teste; não é uma afirmação de que este exemplo foi executado.
