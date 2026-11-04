# Condição de Usuário Único Designado

<figure><img src="../../../.gitbook/assets/userlmn_77e991cee96598023f9a3ac7ad230e50.png" alt=""><figcaption></figcaption></figure>

**Propósito**

Este cartão de fluxo de trabalho facilita operações com base na atribuição de uma tarefa ou documento a um único usuário específico. Usando uma abordagem direta de lógica condicional, ele gerencia fluxos de trabalho que exigem o envolvimento direcionado do usuário, garantindo precisão no manuseio de tarefas baseadas em usuários.

**Componentes do Cartão**

1. **Operador**
* **Descrição**: Especifica a lógica a ser aplicada à atribuição do usuário.
* **Opções**:
* **É**: Aciona a operação se o usuário atribuído ao documento ou tarefa corresponder ao usuário especificado.
* **NÃO É**: Aciona a operação se o usuário atribuído não corresponder ao usuário especificado.
2. **Usuário**
* **Descrição**: Permite a seleção de um único usuário em relação ao qual o usuário atribuído será comparado.
* **Detalhe**: Isso envolve um simples campo de menu suspenso ou de autocompletar onde um usuário pode ser selecionado de cada vez.

**Funcionalidade**

* **Identificação da Atribuição do Usuário**: Identifica o usuário atualmente atribuído a uma tarefa ou documento específico.
* **Avaliação da Condição**:
* Para o operador **É**, o cartão verifica se o usuário atribuído é o mesmo que o usuário selecionado.
* Para o operador **NÃO É**, verifica se o usuário atribuído é diferente do usuário selecionado.
* **Execução da Ação**:
* **Condição Verdadeira**: Se a atribuição atender à condição definida (É ou NÃO É), aciona ações predefinidas, que podem incluir avançar com aprovações, iniciar mais tarefas, enviar notificações ou outros fluxos de trabalho relacionados.
* **Condição Falsa**: Se a condição falhar, o sistema pode redirecionar a tarefa, mantê-la em revisão ou acionar ações predefinidas alternativas.

**Interações do Usuário**

* **Configuração e Configuração**: Os usuários configuram o cartão escolhendo um operador e selecionando um usuário no campo de usuário. Essa configuração deve ser direta, garantindo uma seleção e configuração fáceis para o usuário.
* **Monitoramento e Relatórios**: Oferece ferramentas para monitorar o desempenho do cartão, como rastrear quais tarefas são acionadas por atribuições de usuários específicos e os resultados desses acionamentos.
* **Tratamento de Erros e Notificações**: Fornece mecanismos para alertar os usuários se as tarefas forem atribuídas incorretamente ou se ocorrerem erros operacionais devido a problemas de atribuição.

#### Conclusão

O cartão de fluxo de trabalho "Condição de Usuário Único Designado" é essencial para o gerenciamento preciso de documentos e tarefas específicos do usuário dentro de um sistema ERP. Ele simplifica fluxos de trabalho ao focar em atribuições individuais de usuários, garantindo assim que as ações sejam executadas apenas quando apropriadas, com base no papel e responsabilidades do usuário. Documentar claramente este cartão ajudará os usuários a entender sua aplicação, permitindo que o implementem e gerenciem de forma eficaz em suas operações diárias. Esta documentação garante que todos os usuários em potencial possam entender facilmente o propósito do cartão e integrá-lo perfeitamente em seus fluxos de trabalho.
