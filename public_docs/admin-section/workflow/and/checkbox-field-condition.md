# Condição do Campo de Seleção

<figure><img src="../../../.gitbook/assets/userlmn_b689c7ce31284b4635be85f674a90917.png" alt=""><figcaption></figcaption></figure>

**Propósito**

Este cartão de fluxo de trabalho é projetado para automatizar ações com base no estado (marcado ou desmarcado) de uma caixa de seleção dentro do seu sistema ERP. Ao avaliar a condição da caixa de seleção, facilita o acionamento de processos específicos ou a aplicação de determinadas regras dentro da aplicação.

**Componentes do Cartão**

1. **Nome do Campo**
* **Descrição**: Especifica o nome do campo de seleção que será avaliado.
* **Detalhe**: Isso deve corresponder ao rótulo exato do campo ou identificador usado no sistema. Ele determina qual estado da caixa de seleção está sendo monitorado.
2. **Booleano**
* **Descrição**: Define a condição que aciona o fluxo de trabalho.
* **Opções**:
* **Verdadeiro**: O fluxo de trabalho é acionado se a caixa de seleção estiver marcada.
* **Falso**: O fluxo de trabalho é acionado se a caixa de seleção estiver desmarcada.

**Funcionalidade**

* **Detecção de Estado**: O cartão monitora continuamente o estado do campo de seleção especificado.
* **Avaliação de Condição**:
* O sistema verifica se a caixa de seleção está no estado (marcado ou desmarcado) especificado pela condição Booleana.
* **Execução de Ação**:
* **Condição Verdadeira**: Se o estado da caixa de seleção corresponder à condição Booleana especificada (verdadeira para marcado ou falso para desmarcado), o sistema inicia as ações associadas. Estas podem incluir habilitar ou desabilitar campos de formulário, acionar notificações, iniciar fluxos de trabalho ou atualizar registros.
* **Condição Falsa**: Se o estado da caixa de seleção não corresponder à condição, ações alternativas ou nenhuma ação podem ser tomadas, dependendo da configuração do fluxo de trabalho.

**Interações do Usuário**

* **Configuração e Configuração**: Os usuários configuram o cartão selecionando o campo de seleção em uma lista de campos disponíveis e definindo a condição Booleana. Esse processo de configuração deve ser intuitivo, envolvendo tipicamente um menu suspenso simples para seleção de campo e uma alternância para a condição Booleana.
* **Monitoramento e Relatórios**: Fornece funcionalidades para os usuários monitorarem o status dessa condição, possivelmente por meio de um painel que mostra atualizações em tempo real sobre quais condições estão ativas ou acionadas.
* **Tratamento de Erros e Notificações**: Garante que os usuários sejam notificados se houver discrepâncias ou erros no processo de verificação da condição, como falhas do sistema ao ler o estado da caixa de seleção.

#### Conclusão

O cartão de fluxo de trabalho "Condição do Campo de Seleção" é uma ferramenta fundamental para gerenciar formulários dinâmicos e documentos dentro de um sistema ERP, onde as entradas do usuário podem ditar processos de dados subsequentes. Ao automatizar ações com base no estado de uma caixa de seleção, este cartão aprimora a eficiência do fluxo de trabalho e garante que os comportamentos do sistema estejam alinhados com as entradas do usuário. Uma documentação clara deste cartão ajudará os usuários a implementá-lo efetivamente em suas operações, permitindo um melhor controle sobre os comportamentos do formulário e automações de processos.
