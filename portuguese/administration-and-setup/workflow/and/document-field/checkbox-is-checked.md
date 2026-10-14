# Checkbox is checked

<figure><img src="../../../../.gitbook/assets/image (20) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Este cartão de fluxo de trabalho foi concebido para automatizar ações com base no estado (assinalado ou não assinalado) de uma caixa de verificação dentro do seu sistema ERP. Ao avaliar a condição da caixa de verificação, facilita o acionamento de processos específicos ou a aplicação de determinadas regras dentro da aplicação.

## **Componentes do cartão:**

* **Field Name**
  * **Descrição:** Especifica o nome do campo de caixa de verificação que será avaliado.
  * **Detalhe:** Deve corresponder ao identificador exato do campo utilizado no sistema. Determina qual o estado da caixa de verificação que está a ser monitorizado.
* **Boolean**
  * **Descrição:** Define a condição que aciona o fluxo de trabalho.
  * **Opções:**
    * **True:** O fluxo de trabalho é acionado se a caixa de verificação estiver assinalada.
    * **False:** O fluxo de trabalho é acionado se a caixa de verificação não estiver assinalada.

#### **Funcionalidade:**

* **Deteção de estado:** O cartão monitoriza continuamente o estado do campo de caixa de verificação especificado.
* **Avaliação da condição:** O sistema verifica se a caixa de verificação está no estado (assinalada ou não assinalada) especificado pela condição Boolean.
* **Execução da ação:**
  * **Condição Verdadeira:**\
    Se o estado da caixa de verificação corresponder à condição Boolean especificada (true para assinalada ou false para não assinalada), o sistema inicia as ações associadas. Estas podem incluir ativar ou desativar campos de formulário, acionar notificações, iniciar fluxos de trabalho ou atualizar registos.
  * **Condição Falsa:**\
    Se o estado da caixa de verificação não corresponder à condição, podem ser tomadas ações alternativas ou nenhuma ação, consoante a configuração do fluxo de trabalho.

## **Configuração:**

* Os utilizadores configuram o cartão selecionando o campo de caixa de verificação a partir de uma lista de campos disponíveis e definindo a condição Boolean.&#x20;

## Conclusão:

O cartão de fluxo de trabalho "Checkbox Field Condition" é uma ferramenta fundamental para gerir formulários e documentos dinâmicos dentro de um sistema ERP, onde as entradas do utilizador podem ditar os processos de dados subsequentes. Ao automatizar ações com base no estado de uma caixa de verificação, este cartão melhora a eficiência do fluxo de trabalho e assegura que os comportamentos do sistema estão alinhados com as entradas do utilizador. Uma documentação clara deste cartão ajudará os utilizadores a implementá-lo eficazmente nas suas operações, permitindo um melhor controlo sobre os comportamentos dos formulários e as automações de processos.



**Nota: Nem todos os clientes têm a caixa de verificação, mas esta pode ser adicionada se assim o desejarem.**
