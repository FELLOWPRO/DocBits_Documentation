# Condição do Usuário Designado

<figure><img src="../../../.gitbook/assets/userlmn_5e16e9b23626ec1211c753fec5333513.png" alt=""><figcaption></figcaption></figure>

**Propósito**

Este cartão de fluxo de trabalho gerencia a execução de operações com base em se uma tarefa ou documento é atribuído a um usuário específico ou a um conjunto de usuários. Ele emprega lógica condicional para acionar ou impedir ações específicas, sendo ideal para fluxos de trabalho que exigem tratamento específico do usuário.

**Componentes do Cartão**

1. **Operador**
* **Descrição**: Define a condição lógica a ser aplicada à atribuição do usuário.
* **Opções**:
* **É**: Aciona a operação se o usuário atribuído ao documento ou tarefa corresponder a qualquer usuário na lista especificada.
* **NÃO É**: Aciona a operação se o usuário atribuído ao documento ou tarefa não corresponder a nenhum usuário na lista especificada.
2. **Lista de Usuários**
* **Descrição**: Uma lista ou seleção de usuários para comparar com o usuário atribuído.
* **Detalhe**: Esta lista pode incluir um ou vários usuários, permitindo que o cartão lide efetivamente com condições de usuário singular e múltiplo. A seleção pode ser feita por meio de caixas de seleção, um menu suspenso de seleção múltipla ou elementos de UI semelhantes.

**Funcionalidade**

* **Identificação da Atribuição do Usuário**: Identifica automaticamente o usuário ou usuários atribuídos a uma tarefa ou documento específico dentro do sistema ERP.
* **Avaliação da Condição**:
* Usando o operador **É**, o cartão verifica se o usuário atribuído está entre aqueles listados na Lista de Usuários.
* Usando o operador **NÃO É**, o cartão garante que o usuário atribuído não esteja entre aqueles listados.
* **Execução da Ação**:
* **Condição Verdadeira**: Se a atribuição do usuário atender à condição (seja **É** ou **NÃO É**), ações relevantes são acionadas, como notificações, iniciações de tarefas, aprovações ou outras etapas do fluxo de trabalho.
* **Condição Falsa**: Se a condição não for atendida, o documento ou tarefa pode seguir por uma rota diferente, ou ações alternativas podem ser especificadas.

**Interações do Usuário**

* **Configuração e Configuração**: Os usuários configuram o cartão selecionando um operador e especificando os usuários relevantes da Lista de Usuários. A configuração deve ser amigável e intuitiva para acomodar seleções de bases de usuários potencialmente grandes.
* **Monitoramento e Relatórios**: O sistema ERP deve fornecer funcionalidade para monitorar e relatar as operações acionadas por este cartão, oferecendo insights sobre a precisão da atribuição e a eficiência do processo.
* **Tratamento de Erros e Notificações**: Os usuários devem ter opções para receber alertas ou notificações se houver problemas com as atribuições, como tarefas não atribuídas ou erros na seleção de usuários.

#### Conclusão

O cartão de fluxo de trabalho "Condição do Usuário Designado" é uma ferramenta crítica para gerenciar fluxos de trabalho de documentos e tarefas que dependem de atribuições de usuários. Ao permitir condições com base em se uma tarefa ou documento é atribuído a usuários específicos, garante que os fluxos de trabalho sejam acionados apenas por interações de usuário apropriadas, aprimorando tanto a responsabilidade quanto o alinhamento de tarefas dentro das equipes. Documentar claramente este cartão ajudará os usuários a entender sua importância e integrá-lo efetivamente em seus fluxos de trabalho, garantindo operações suaves e eficientes adaptadas aos papéis e responsabilidades do usuário.
