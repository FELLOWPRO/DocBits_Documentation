---
description: DocBits Workflow Engine
---

# Workflow

<figure><img src="../../.gitbook/assets/docbits_workflow_3.png" alt="DocBits Fluxo de trabalho 3"><figcaption></figcaption></figure>

## Motor de Fluxo de Trabalho DocBits: Simplificando a Automação de Processos

### Introdução

### Compreender e preparar workflows <a id="workflow-orientation"></a>

Conheça a conta de teste real do DocBits: oito execuções no painel, dois workflows guardados com ordem de execução 100/200 e três cenários de teste aprovados. O tutorial também explica os workflows Standard e Advanced, as licenças, os modelos e o Card SDK.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pt.mp4" %}

[Ver com legendas](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pt.html) · [Abrir vídeo](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pt.mp4) · [Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pt.vtt) · [Transcrição](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pt.txt) · 3:07

<details>
<summary>Capítulos e transcrição</summary>

| Capítulo | Início |
| --- | --- |
| Conhecer o administrador | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pt.mp4#t=0.000) |
| Organização e acesso | [0:01](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pt.mp4#t=1.625) |
| Painel e filtros | [0:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pt.mp4#t=14.750) |
| Lista de workflows | [0:54](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pt.mp4#t=54.208) |
| Ordem de execução | [1:08](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pt.mp4#t=68.458) |
| Standard Workflow | [1:26](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pt.mp4#t=86.417) |
| Advanced Workflow | [1:38](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pt.mp4#t=98.917) |
| Licenças | [1:55](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pt.mp4#t=115.083) |
| Modelos | [2:10](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pt.mp4#t=130.750) |
| Test Manager | [2:23](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pt.mp4#t=143.333) |
| Card SDK | [2:38](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pt.mp4#t=158.500) |
| Verificar a preparação | [2:52](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-orientation-admin/v1/pt.mp4#t=172.542) |

**Conhecer o administrador**

Administro o DocBits.

**Organização e acesso**

Bem, começo por verificar a organização indicada no topo. Estas definições de workflow pertencem à organização selecionada. Nesta demonstração utilizo a nossa conta de teste da documentação.

**Painel e filtros**

O painel de workflows apresenta a visão geral. Para esta vista, executei manualmente dois workflows de formação oito vezes com uma fatura de exemplo. Aqui vejo oito execuções no total e seis execuções bem-sucedidas. Em duas execuções, a condição do montante não foi cumprida. A taxa de sucesso também inclui estas verificações concluídas corretamente. Filtro pelo nome do workflow e verifico o período. Os contadores e o gráfico acompanham essa seleção. À direita, alterno entre workflows guardados e cenários de teste. As execuções do Test Manager são contadas separadamente.

**Lista de workflows**

Na lista faço a gestão de cada workflow. Verifico o nome, o tipo Standard ou Advanced, a ordem de execução, o evento inicial e as ações disponíveis. Procuro um workflow existente antes de criar outro.

**Ordem de execução**

A ordem de execução importa quando vários workflows processam o mesmo documento. Verifico qual deve correr primeiro e de que dados precisa o seguinte. Aqui, a revisão da fatura tem a ordem cem e a verificação seguinte duzentos. Os valores mais baixos são executados primeiro.

**Standard Workflow**

Para uma regra linear escolho Standard Workflow. Quando define o evento inicial, E acrescenta condições, e Então executa as ações. A biblioteca contém os cartões disponíveis.

**Advanced Workflow**

Para percursos alternativos utilizo Advanced Workflow. Esta pré-visualização mostra Start e ligações explícitas. Sucesso, condição não cumprida e erro podem seguir percursos diferentes. A posição dos cartões não define a ordem.

**Licenças**

Em Licença verifico separadamente Workflow e Advanced Workflow. Aqui ambos estão inativos. A janela mostra as subscrições disponíveis. Fecho esta consulta sem alterações. Abrir o designer não ativa o motor.

**Modelos**

Os modelos permitem reutilizar um ponto de partida. Abro a biblioteca e a opção dos modelos predefinidos. Verifico sempre os campos, destinatários e ações para o meu próprio processo.

**Test Manager**

O Test Manager guarda cenários para workflows Standard e Advanced. Depois da configuração acrescento dados representativos e resultados esperados. Executar todos os testes ajuda-me a verificar as alterações.

**Card SDK**

O Card SDK serve para extensões próprias. Os programadores podem utilizar um modelo, carregar um pacote ou importar do GitHub. Na administração habitual começo pela biblioteca de cartões existente.

**Verificar a preparação**

Antes de construir confirmo a organização, o acesso, a licença necessária, os campos do documento e o resultado pretendido. Decido se uma regra linear é suficiente. No próximo vídeo criamos um Standard Workflow passo a passo.

</details>


No campo da automação de processos, o Motor de Fluxo de Trabalho DocBits se destaca por sua abordagem direta e intuitiva. Este motor simplifica a criação e gestão de fluxos de trabalho através de uma estrutura clara e simples baseada em regras. O princípio fundamental por trás de seu design é a regra "Easy When-And-Then" (Fácil Quando-E-Então), que divide o processo de automação em três componentes fundamentais: Gatilho, Condição e Ação. Este guia explica como cada componente funciona dentro do sistema e como eles trabalham juntos para facilitar a automação perfeita.

### A Regra "Easy When-And-Then" Explicada

O Motor de Fluxo de Trabalho DocBits opera em um princípio básico, mas poderoso, que torna a automação de fluxos de trabalho acessível a usuários de todos os níveis de habilidade. Este princípio está encapsulado na regra "Easy When-And-Then", que pode ser dividida da seguinte forma:

#### [When](./#when-trigger) (Gatilho)

* **Definição**: O componente "When" (Quando) representa o _Gatilho_ do fluxo de trabalho. Este é o evento ou condição que inicia a execução do fluxo de trabalho. Os gatilhos podem ser uma variedade de ocorrências, como a chegada de um novo e-mail, uma data e hora específicas ou a criação de um novo documento.
* **Exemplo**: "Quando um novo formulário de cliente é enviado..."

#### [And](./#and-condition) (Condição)

* **Definição**: O componente "And" (E) introduz a _Condição_ que deve ser atendida para que a ação prossiga. As condições servem como filtros ou critérios que refinam o gatilho, garantindo que o fluxo de trabalho seja executado apenas sob certas circunstâncias.
* **Exemplo**: "...e o cliente é do segmento 'Enterprise'..."

#### [Then](./#then-action) (Ação)

* **Definição**: Finalmente, a parte "Then" (Então) especifica a _Ação_ a ser tomada uma vez que o gatilho ocorre e a condição é satisfeita. As ações são as tarefas ou operações executadas pelo fluxo de trabalho, como enviar um e-mail, atualizar um banco de dados ou criar uma tarefa em uma ferramenta de gerenciamento de projetos.
* **Exemplo**: "...então atribuir o lead à equipe de vendas empresariais e enviar um e-mail de boas-vindas."

### Combinando Componentes para Automações Poderosas

Ao reunir esses três componentes—Gatilho, Condição e Ação—o Motor de Fluxo de Trabalho DocBits permite aos usuários criar fluxos de trabalho altamente personalizados e eficientes. Esta abordagem modular não apenas simplifica o processo de configuração de automações, mas também oferece a flexibilidade para criar fluxos de trabalho complexos capazes de lidar com uma ampla gama de tarefas e processos.

### Conclusão

A regra "Easy When-And-Then" do Motor de Fluxo de Trabalho DocBits exemplifica o compromisso do motor em fornecer uma plataforma amigável ao usuário para automatizar processos. Esta regra direta, ao dividir a automação nos elementos essenciais de Gatilho, Condição e Ação, torna mais fácil para os usuários conceituar, criar e gerenciar fluxos de trabalho. Seja você novo na automação de fluxos de trabalho ou um profissional experiente, o Motor de Fluxo de Trabalho DocBits oferece uma ferramenta eficiente e acessível para aumentar a produtividade e otimizar as operações.
