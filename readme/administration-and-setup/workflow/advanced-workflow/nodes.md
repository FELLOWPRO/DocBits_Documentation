# Nós

Um Advanced Workflow é um grafo de **nós** ligados por arestas. Adiciona nós a partir do menu **+ Add** (ou clicando com o botão direito na tela) e liga-os para definir o fluxo de execução.

<figure><img src="../../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Menu de adição de nós com os tipos de nó disponíveis"><figcaption><p>O menu de nós **+ Add** — os tipos de nó disponíveis.</p></figcaption></figure>

## Tipos de nó

- **Start** — o ponto de entrada do fluxo de trabalho. Adicionado automaticamente; todos os fluxos começam aqui.
- **When** — um cartão de acionamento, igual ao do construtor Standard.
- **And** — um cartão de condição. Avalia para verdadeiro ou falso e pode ramificar o fluxo.
- **Then** — um cartão de ação que executa trabalho (definir campos, criar tarefas, chamar APIs, …).
- **Wait ALL** — espera até que *todos* os ramos de entrada terminem antes de continuar.
- **Wait ANY** — continua assim que *qualquer* ramo de entrada terminar.
- **OR** — ramifica o fluxo por caminhos alternativos.
- **Note** — uma anotação de texto livre na tela; não afeta a execução.

Os nós **When / And / Then** utilizam exatamente os mesmos cartões descritos na secção [Cartões](../cards-overview.md).

## Ligar nós

Os nós são ligados por **arestas coloridas**. Arraste a partir de um conector no lado **direito** de um nó até ao conector de entrada no lado **esquerdo** de outro nó para criar uma ligação. Cada cor indica um resultado de execução diferente:

- **Success** (azul) — o caminho predefinido percorrido quando um nó é concluído com sucesso. Disponível em todos os tipos de nó.
- **Failed Condition** (laranja) — percorrido quando uma condição avalia para falso. Disponível em nós **And** (condição).
- **Error** (vermelho) — percorrido quando um nó encontra um erro durante a execução. Disponível em nós **And** e **Then** (ação).

## Realce do caminho de execução

Clique em qualquer nó para ver o seu caminho de execução. Todos os nós que conduzem a ele e todos os nós que dele decorrem são realçados — tudo o resto é esbatido. Para os nós **Wait ALL**, todos os ramos de entrada são mostrados, para que possa ver exatamente o que a porta espera antes de continuar.

## Próximos passos

- Passe dados entre nós com [Variáveis](variables.md).
- Verifique e execute o seu fluxo com [Validação e Testes](validation-and-testing.md).
