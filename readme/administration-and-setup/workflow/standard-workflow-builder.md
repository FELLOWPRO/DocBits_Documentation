# Standard Workflow

O construtor **Standard Workflow** é o editor linear, baseado em cartões, para automatizar o processamento de documentos. Um fluxo de trabalho é composto por três grupos de cartões — **When** (o gatilho), **And** (condições adicionais) e **Then** (as ações a executar). Quando um documento corresponde às condições When/And, as ações Then são executadas automaticamente.

## Como aceder

Abra o **Workflow Dashboard → Workflow List** e clique em **Add Workflow** para criar um novo fluxo de trabalho Standard, ou clique num fluxo de trabalho existente para o editar.

<figure><img src="../../.gitbook/assets/workflow_list.png" alt="Workflow List com tipo, ordem de execução e gatilho"><figcaption><p>A Workflow List — cada linha é um fluxo de trabalho que pode abrir, ativar/desativar ou editar.</p></figcaption></figure>

## O modelo When / And / Then

<figure><img src="../../.gitbook/assets/workflow_designer_cards.png" alt="Tela do Standard Workflow com cartões When, And e Then"><figcaption><p>A tela do Standard Workflow. Este exemplo é acionado por faturas numa sub-organização e atribui-as a um utilizador.</p></figcaption></figure>

- **When** — o gatilho que inicia o fluxo de trabalho (por exemplo, *o tipo de documento é Fatura*).
- **And** — condições adicionais que também têm de ser verdadeiras (por exemplo, *o documento faz parte de uma sub-organização*). Deixe vazio para executar em todas as correspondências do cartão When.
- **Then** — as ações a realizar (por exemplo, *atribuir o documento ao utilizador*, criar uma tarefa, chamar uma API, enviar um e-mail).

## Adicionar cartões

Clique em **Add Card** em qualquer grupo para abrir a biblioteca de cartões. Os cartões estão organizados por categoria para que possa encontrar o bloco de construção de que precisa:

<figure><img src="../../.gitbook/assets/workflow_add_card_picker.png" alt="Biblioteca Add Card agrupada por categoria"><figcaption><p>A biblioteca <strong>Add Card</strong> — cartões de condição, cartões de comparação, cartões de ação e mais, agrupados por categoria.</p></figcaption></figure>

Guarde com **Save Workflow** ou guarde o esquema como um modelo reutilizável com **Save Template**.

## Próximos passos

- Veja o que cada cartão faz na secção **Cards**.
- Combine cartões em soluções comprovadas com os **Workflow Pattern Guides**.
- Para fluxos com ramificações e caminhos paralelos (Wait ALL / Wait ANY / OR), utilize o construtor **Advanced Workflow**.
