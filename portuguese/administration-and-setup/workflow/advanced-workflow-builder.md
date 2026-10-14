# Advanced Workflow

O construtor **Advanced Workflow** é um editor de grafo de nós para fluxos de trabalho que precisam de ramificações, caminhos paralelos e controlo de fluxo — para além do When/And/Then linear do construtor Standard. Dispõe os nós numa tela e liga-os para definir o fluxo de execução.

{% embed url="https://youtu.be/EeNFVR6z7G8" %}
Advanced Workflow Designer
{% endembed %}

## Como aceder

Abra o designer do Advanced Workflow a partir da área de fluxos de trabalho (a tela do construtor avançado). Começa por um nó **Start** e constrói o fluxo adicionando nós.

<figure><img src="../../.gitbook/assets/workflow_advanced_canvas.png" alt="Tela em grafo de nós do Advanced Workflow com barra de ferramentas"><figcaption><p>A tela do Advanced Workflow — um grafo de nós com controlos de zoom, execução, grelha e gravação. Atribua um nome ao fluxo de trabalho na barra de ferramentas.</p></figcaption></figure>

## Adicionar nós

Clique em **+ Add** para abrir o menu de nós. Para além dos já conhecidos cartões **When**, **And** e **Then**, o construtor avançado acrescenta nós de controlo de fluxo:

<figure><img src="../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Menu Add do Advanced Workflow com tipos de nós"><figcaption><p>O menu de nós <strong>+ Add</strong>: When / And / Then mais Wait ALL, Wait ANY, OR e Note.</p></figcaption></figure>

- **When / And / Then** — os mesmos cartões de condição e de ação do construtor Standard.
- **Wait ALL** — aguarda até que *todas* as ramificações de entrada estejam concluídas antes de continuar.
- **Wait ANY** — continua assim que *qualquer* ramificação de entrada estiver concluída.
- **OR** — ramifica o fluxo por caminhos alternativos.
- **Note** — uma anotação de texto livre na tela (não afeta a execução).

Execute o fluxo com o controlo de reprodução, valide-o e guarde com o botão de gravação na barra de ferramentas.

## Próximos passos

- Veja o que cada cartão faz na secção **Cards**.
- Para automações lineares simples, o construtor **Standard Workflow** é mais rápido de configurar.
