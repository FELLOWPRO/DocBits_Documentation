# Atribuir documento ao grupo da instalação

<figure><img src="../../../../.gitbook/assets/workflow_card_action_assign_doc_to_facility_group_v2-pt-pt.png" alt="Atribuir documento ao grupo da instalação, Versão 2" width="634"><figcaption><p>Versão 2</p></figcaption></figure>

## Propósito:

Este cartão de fluxo de trabalho atribui um documento ao grupo responsável pela instalação da respetiva ordem de compra. A instalação não é selecionada no cartão: é obtida a partir das ordens de compra com as quais o documento está associado. Em seguida, o cartão procura um grupo de utilizadores cujo nome contenha tanto o nome de grupo introduzido no cartão como o código da instalação, e atribui o documento a esse grupo.

Isto é útil quando o mesmo tipo de equipa existe uma vez por instalação, por exemplo um grupo de aprovação por fábrica ou armazém, e cada documento deverá ir para a equipa da instalação para a qual foi encomendado.

Para uma atribuição que é acrescentada a uma sequência de aprovadores em vez de ser feita diretamente, pode ser utilizado o cartão **Assign Sequentially to Facility Group**.

## Componentes do cartão:

1. **Nome do grupo**
   * **Descrição:** A parte do nome que os grupos de instalações têm em comum.
   * **Detalhe:** Um texto que é comparado com os nomes dos grupos de utilizadores da organização. Um grupo corresponde se o seu nome contiver este texto e o código da instalação da ordem de compra. A comparação não distingue maiúsculas de minúsculas. Por exemplo, com o nome de grupo **Approver** e uma ordem de compra para a instalação **1000**, corresponderia um grupo chamado **Approver 1000**.

## Funcionalidade:

* **Determinação da instalação:** O cartão lê as ordens de compra com as quais o documento está associado e recolhe o código da instalação (a localização da ordem de compra) de cada uma delas.
* **Determinação do grupo:** Para cada código de instalação, o cartão procura grupos de utilizadores cujo nome contenha tanto o **Nome do grupo** indicado no cartão como o código da instalação. Os códigos de instalação para os quais não é encontrado nenhum grupo são listados no registo do fluxo de trabalho.
* **Execução da ação:** O documento é atribuído ao grupo correspondente. Se vários grupos corresponderem, por exemplo porque o documento está associado a ordens de compra de instalações diferentes, o documento é atribuído a apenas um deles; o cartão não determina qual.
* **Dados em falta:**
  * Se não for introduzido nenhum nome de grupo no cartão, o cartão não é executado e regista os dados em falta no registo do fluxo de trabalho.
  * Se o documento não estiver associado a uma ordem de compra, o cartão regista os dados em falta em vez de atribuir o documento.
  * Se nenhum grupo corresponder a qualquer dos códigos de instalação, o documento não é atribuído e o registo do fluxo de trabalho indica que não foi encontrado nenhum grupo correspondente.

## Configuração:

* Os grupos de utilizadores deverão ser nomeados de forma a que cada nome contenha a parte comum do nome e o código da instalação, por exemplo **Approver 1000**, **Approver 2000**.
* O cartão pode ser adicionado a partir da categoria **Cessionário**. Em seguida, a parte comum do nome dos grupos é introduzida no campo **Nome do grupo**.
* Como a instalação provém das ordens de compra associadas, o cartão é mais adequado para fluxos de trabalho de documentos que já foram associados a uma ordem de compra.

## Conclusão:

O cartão de fluxo de trabalho "Assign Document to Facility Group" encaminha os documentos para a equipa da instalação para a qual foram encomendados. Um único cartão abrange todas as instalações, desde que os grupos de utilizadores sigam um esquema de nomes consistente, com o código da instalação no nome.
