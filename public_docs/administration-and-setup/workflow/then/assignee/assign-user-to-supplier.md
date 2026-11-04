# Atribuir utilizador ao fornecedor

<figure><img src="../../../../.gitbook/assets/workflow_card_action_assign_user_to_supplier_v2-pt-pt.png" alt="Atribuir utilizador ao fornecedor, Versão 2" width="634"><figcaption><p>Versão 2</p></figcaption></figure>

## Propósito:

Este cartão de fluxo de trabalho define o utilizador atribuído de um fornecedor registado. O utilizador atribuído é o contacto interno responsável pelo fornecedor. O cartão não atua sobre um documento: destina-se a fluxos de trabalho que são iniciados por uma alteração do estado de um fornecedor, por exemplo com o cartão When **Supplier status changed**. O fornecedor cujo estado mudou é o fornecedor ao qual o utilizador é atribuído.

## Componentes do cartão:

1. **Usuário**
   * **Descrição:** O utilizador que passa a ser o utilizador atribuído do fornecedor.
   * **Detalhe:** Pode ser selecionado um utilizador da organização. Se o fornecedor já tiver um utilizador atribuído, esse utilizador é substituído.

## Funcionalidade:

* **Execução da ação:** O cartão obtém o fornecedor a partir da execução do fluxo de trabalho e guarda o utilizador selecionado como utilizador atribuído do fornecedor. O resultado é registado no registo do fluxo de trabalho.
* **Utilização com e-mails:** Depois de um utilizador ser atribuído, podem ser enviados e-mails a este utilizador com a opção **Usuário atribuído ao fornecedor**, por exemplo no cartão **Send Email**.
* **Dados em falta:** Se não estiver selecionado nenhum utilizador no cartão, o cartão não é executado e regista os dados em falta no registo do fluxo de trabalho.
* **Erros:** Se o serviço de fornecedores rejeitar o pedido ou não responder a tempo, o cartão termina com um erro.

## Configuração:

* O cartão pode ser utilizado num fluxo de trabalho que é iniciado por uma alteração do estado de um fornecedor.
* O cartão pode ser adicionado a partir da categoria **Cessionário**. Em seguida, o utilizador que deverá ser responsável pelo fornecedor é selecionado no campo **Usuário**.

## Conclusão:

O cartão de fluxo de trabalho "Assign User to Supplier" atribui automaticamente a cada fornecedor um contacto responsável quando o respetivo estado muda, por exemplo após o registo. Os passos seguintes, como e-mails para o utilizador atribuído, podem basear-se nesta atribuição.
