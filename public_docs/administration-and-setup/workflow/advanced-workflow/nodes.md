# Nós

## Vídeo: Nós e percursos

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/pt.mp4" %}

[Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_logic/v2/pt.vtt) · 2:00

<details>
<summary>Transcrição</summary>

**A função de cada nó**

Start inicia manualmente. When define um evento. Nenhum aceita ligações de entrada. And verifica uma condição. Then executa uma ação. Ambos os construtores partilham o catálogo de cartões. As notas explicam o desenho sem serem executadas.

**Três resultados diferentes**

Arraste uma saída para a entrada seguinte. No editor, azul significa sucesso, laranja condição falsa e vermelho erro. And tem três resultados; Then, sucesso e erro. As vistas de execução mostram o sucesso a verde.

**Crie uma alternativa**

Verifique se uma fatura ultrapassa o limiar. Ligue azul à aprovação, laranja ao processamento normal e vermelho à gestão de erros. Uma condição falsa pode continuar pelo percurso ligado; não interrompe todos os ramos.

**Unir com Wait ALL**

Wait ALL reúne ramos. Cada nó de origem deve ter seguido um percurso ligado à junção. Ligue ambas as verificações necessárias e a ação seguinte. Um percurso não selecionado não fornece o resultado obrigatório.

**Alternativas com ANY e OR**

Wait ANY e OR reúnem ramos se pelo menos uma origem seguir um percurso ligado. OR exige dois nós de origem diferentes. Estas junções não criam escolhas exclusivas nem cancelam outras ações. Teste o grafo completo.

**Mantenha o grafo executável**

Os nós devem ser acessíveis a partir de uma entrada. Evite ciclos e ligações de entrada para Start ou When. Inclua uma ação Then e valide os percursos. Nós Delay importados exigem duração positiva; Adicionar não oferece Delay.

</details>

[Ver os cinco capítulos](../advanced-workflow-videos.md)

Um Advanced Workflow é um grafo de **nós** ligados por arestas. Adiciona nós a partir do menu **+ Add** (ou clicando com o botão direito na tela) e liga-os para definir o fluxo de execução.

<figure><img src="../../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Menu de adição de nós com os tipos de nó disponíveis"><figcaption><p>O menu de nós **+ Add** — os tipos de nó disponíveis.</p></figcaption></figure>

## Tipos de nó

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/pt.mp4" %}

**Vídeo:** Alterar a versão de um cartão · 0:36 · [Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/pt.vtt)

<details>

<summary>Transcrição</summary>

**O rótulo mostra a versão do cartão** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/pt.mp4#t=0.25)

Os cartões podem ter várias versões. O pequeno rótulo num cartão, por exemplo v1, mostra qual versão ele usa. Uma versão mais nova faz mais.

**Clique para ver as versões** · [0:11](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/pt.mp4#t=11.016)

Clique no rótulo da versão para ver as versões deste cartão.

**Versão 3: Status após a exportação** · [0:15](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/pt.mp4#t=15.383)

Escolha a versão mais nova. Ela também pode definir o status do documento após a exportação.

**Definir os valores de novo** · [0:21](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/pt.mp4#t=21.883)

Os valores não são mantidos. Defina-os de novo, aqui a configuração de exportação e o status.

**Validar e testar** · [0:29](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-version/v1/pt.mp4#t=29.05)

Depois valide e teste o Workflow, como após qualquer mudança. Salve-o quando ele fizer o que você espera.

</details>

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

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/pt.mp4" %}

**Vídeo:** Sucesso, condição com falha e erro em uma execução · 1:16 · [Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/pt.vtt)

<details>

<summary>Transcrição</summary>

**Quando, E, Então na execução** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/pt.mp4#t=0.25)

Quando um Workflow é executado, o cartão Quando o inicia. Os cartões E verificam condições e os cartões Então agem. O que acontece depois depende do resultado de cada cartão.

**Sucesso, condição não atendida ou erro** · [0:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/pt.mp4#t=12.616)

Cada cartão E termina com um de três resultados. O sucesso segue o caminho azul, uma condição não atendida o caminho laranja e um erro o caminho vermelho.

**Dados ausentes são um erro** · [0:22](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/pt.mp4#t=22.916)

Dados ausentes não são uma condição não atendida. Se faltar um campo de que o cartão precisa, uma variável ou o documento, o cartão informa um erro e segue o caminho vermelho.

**Sem caminho laranja: a execução para** · [0:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/pt.mp4#t=34.416)

Se uma condição falhar e o caminho laranja dela não estiver conectado, o Workflow para nesse cartão. A execução termina como condição não atendida.

**Conectado: só outro ramo** · [0:43](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/pt.mp4#t=43.816)

Se o caminho laranja estiver conectado, uma condição não atendida é só outro ramo. O Workflow continua por ali e ainda pode terminar com sucesso.

**Caminho vermelho: capturar erros** · [0:53](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/pt.mp4#t=53.05)

Conecte o caminho vermelho a uma alternativa, por exemplo uma tarefa para uma pessoa, para que os erros não passem despercebidos. A alternativa é executada, mas a execução continua marcada como erro.

**Como uma execução termina** · [1:04](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-results/v1/pt.mp4#t=64.85)

Resumindo: qualquer erro torna a execução um erro. Uma condição não atendida sem caminho laranja conectado a torna uma condição não atendida. Todo o resto termina com sucesso.

</details>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/pt.mp4" %}

**Vídeo:** E e OU: combinar condições · 4:15 · [Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/pt.vtt)

<details>

<summary>Transcrição</summary>

**E e OU** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/pt.mp4#t=0.25)

As condições podem ser combinadas de duas formas. Cartões um depois do outro funcionam como E: todos precisam ser verdadeiros. Cartões lado a lado, ligados ao mesmo cartão seguinte, funcionam como OU: basta um cartão verdadeiro. Os nós de junção mostram isso na área de trabalho.

**E: cartões um depois do outro** · [0:18](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/pt.mp4#t=18.45)

Um cartão depois do outro é E: cada cartão do caminho precisa ser verdadeiro antes que o próximo seja executado. Esta fatura está pronta para validação e não pendente de aprovação, então os dois cartões são verdadeiros e a ação é executada.

**OU: cartões lado a lado** · [0:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/pt.mp4#t=34.75)

OU significa cartões lado a lado. Ligue a saída verde dos dois cartões E diretamente à entrada do próximo cartão. Teste: o primeiro cartão é falso, o segundo verdadeiro, e um caminho verdadeiro basta para a ação ser executada. O banner do teste ainda indica uma condição não atendida, porque a saída laranja do cartão falso não está ligada, mas a ação é executada.

**O mesmo com um cartão OU** · [0:56](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/pt.mp4#t=56.65)

Você também pode unir os caminhos com um cartão OU. Ele faz o mesmo, mas deixa o OU visível na área de trabalho. Clique com o botão direito na área de trabalho, Adicionar e depois OU. Ligue os dois cartões E a ele, e o cartão OU à ação.

**Para OU basta um caso verdadeiro** · [1:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/pt.mp4#t=74.783)

O teste dá o mesmo resultado: ao cartão OU basta um caso verdadeiro, então a ação é executada. Aqui também o banner indica a condição não atendida do cartão falso.

**Aguardar QUALQUER: o mesmo que OU** · [1:28](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/pt.mp4#t=88.783)

Aguardar QUALQUER funciona exatamente como OU: espera por cada cartão à sua frente e continua quando pelo menos um caminho foi seguido. Os dois são intercambiáveis, use o nome que se lê melhor no seu workflow.

**E com Aguardar TODOS** · [1:50](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/pt.mp4#t=110.483)

Para E com cartões lado a lado, use Aguardar TODOS. Clique com o botão direito na área de trabalho, Adicionar e depois Aguardar TODOS. Ligue os dois cartões E a ele, e Aguardar TODOS à ação. Teste: ele espera os dois cartões, os dois são verdadeiros, então a ação é executada.

**A ordem: como as ligações foram desenhadas** · [2:18](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/pt.mp4#t=138.25)

Em que ordem isto é executado? O workflow percorre uma lista. Os cartões depois de um cartão entram na ordem em que as suas ligações foram desenhadas, então a condição de cima é executada primeiro e depois a de baixo. O cartão OU espera até que as duas tenham sido executadas, e a ação é executada uma vez, não importa quantas condições foram verdadeiras.

**Direto para uma ação: sem espera** · [2:49](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/pt.mp4#t=169.983)

Cartões ligados diretamente a uma ação não esperam. A ação é alcançada pelo caminho curto e é executada antes de o último cartão do caminho longo ser verificado, então esse cartão já não muda nada. Se a ação deve esperar por todas as verificações, coloque antes dela um cartão OU, Aguardar QUALQUER ou Aguardar TODOS.

**Cada saída pode levar a outro lugar** · [3:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/pt.mp4#t=192.15)

Cada cartão tem até três saídas: sucesso, condição não atendida e erro. Cada saída pode levar ao seu próprio cartão seguinte.

**Várias saídas, uma entrada: basta uma** · [3:24](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/pt.mp4#t=204.016)

Você também pode ligar várias saídas de um cartão à mesma entrada. Só uma delas pode ser tomada, porque um cartão termina com exatamente um resultado, então o próximo cartão espera só essa. Isso vale para qualquer entrada, não só para estes nós de junção. Teste: a condição não é atendida, e Aguardar TODOS continua mesmo assim.

**Nós de junção: quais caminhos foram tomados** · [3:50](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-merge/v2/pt.mp4#t=230.216)

Os nós de junção servem principalmente para deixar um Workflow mais fácil de ler. OU e Aguardar QUALQUER continuam assim que pelo menos um caminho ligado foi tomado. Aguardar TODOS espera até todos os cartões anteriores terminarem e só continua se todos os caminhos ligados foram tomados. Qualquer saída de um cartão pode ser ligada, não só a verde: se um cartão termina com uma condição não atendida, a saída laranja conta como tomada.

</details>

Os nós são ligados por **arestas coloridas**. Arraste a partir de um conector no lado **direito** de um nó até ao conector de entrada no lado **esquerdo** de outro nó para criar uma ligação. Cada cor indica um resultado de execução diferente:

- **Success** (azul) — o caminho predefinido percorrido quando um nó é concluído com sucesso. Disponível em todos os tipos de nó.
- **Failed Condition** (laranja) — percorrido quando uma condição avalia para falso. Disponível em nós **And** (condição).
- **Error** (vermelho) — percorrido quando um nó encontra um erro durante a execução. Disponível em nós **And** e **Then** (ação).

## Realce do caminho de execução

Clique em qualquer nó para ver o seu caminho de execução. Todos os nós que conduzem a ele e todos os nós que dele decorrem são realçados — tudo o resto é esbatido. Para os nós **Wait ALL**, todos os ramos de entrada são mostrados, para que possa ver exatamente o que a porta espera antes de continuar.

## Próximos passos

- Passe dados entre nós com [Variáveis](variables.md).
- Verifique e execute o seu fluxo com [Validação e Testes](validation-and-testing.md).
