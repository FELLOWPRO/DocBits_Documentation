# DocBits Operator

## Visão geral

O **DocBits Operator** é um assistente de automação com IA criado para simplificar tarefas repetitivas nos seus workflows. Os usuários criam _prompts_ — instruções passo a passo enriquecidas com variáveis — que orientam a IA a navegar, inserir dados e clicar pelas interfaces automaticamente. Isso reduz o esforço manual e acelera as operações de rotina.

## Habilitando o DocBits Operator

Para habilitar o DocBits Operator, siga estas etapas:

1. **Acesse as configurações**:
   * No Dashboard, acesse **Configurações**.
   *   Selecione **Processamento de documentos** e depois escolha **Módulo**.

       <figure><img src="../../.gitbook/assets/docbits_operator_module_selection.png" alt="Seleção de módulo do DocBits Operator"><figcaption></figcaption></figure>
2. **Habilite o recurso**:
   * Role a página para baixo até encontrar a opção **DocBits Operator**.
   *   Ative o controle deslizante para habilitar o **DocBits Operator**.

       <div align="left"><figure><img src="../../.gitbook/assets/docbits_operator_enable_toggle.png" alt="Controle para habilitar o DocBits Operator" width="563"><figcaption></figcaption></figure></div>

## Acessando a interface

* Depois que o recurso estiver habilitado, abra o **DocBits Operator** no menu de navegação principal.

### **1. Entrada do prompt**

Na parte inferior da tela há um campo de entrada com o rótulo _“Enter your prompt here…”_. É aqui que os usuários escrevem as instruções que o operador deve seguir.

Ao lado do campo de entrada há vários botões de controle:

* **Prompt Variables** – Abre um pop-up onde você pode inserir pares chave-valor usados no prompt. As variáveis são escritas entre chaves, como `{invoice_number}` ou `{url}`. Esses valores se aplicam somente ao prompt atual no campo de entrada.
* **Save Prompt** – Salva o prompt atual. Você pode salvá-lo como:
  * **Organization Prompt** – Editável dentro da sua organização; inclui o prompt e os valores de variáveis definidos.
  * **Global Prompt** – Compartilhado entre todos os tenants; inclui apenas o prompt e os marcadores de variáveis (nenhum valor é salvo).
* **Clear Chat** – Limpa a conversa atual com o operador, mas mantém o prompt do campo de entrada inalterado. Útil ao reutilizar ou refinar um prompt.

Para orientações detalhadas sobre como escrever prompts eficazes — incluindo sintaxe, variáveis e exemplos — consulte o [**Guia de redação de prompts**](prompt-writing-guide.md).

### **2. Navegação na barra lateral**

Use o ícone no canto superior esquerdo para abrir ou fechar a barra lateral. Ela mostra os prompts salvos, organizados em duas categorias:

* **Organization Prompts**: editáveis e reutilizáveis dentro da sua organização.
* **Global Prompts**: compartilhados entre todos os tenants. Eles não podem armazenar variáveis e não podem ser editados nem excluídos.
  * Um prompt global ainda pode ser editado e excluído pela **organização que o criou**, onde ele aparece em Organization Prompts.
* **Função de pesquisa:** uma barra de pesquisa no topo da barra lateral permite encontrar rapidamente os prompts salvos por nome ou palavra-chave.
* **Referência dos ícones:** cada prompt salvo tem um conjunto de ícones de ação
  * **Seta** – Inicia o prompt
  * **Caneta** – Edita o prompt (disponível somente para os prompts da sua própria organização)
  * **Lixeira** – Exclui o prompt (disponível somente para os prompts da sua própria organização)

### 3. Salvar prompt

Ao clicar no botão **Save Prompt**, abre-se um pop-up onde você pode salvar o prompt atual para uso futuro.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_notification_card_overview.png" alt="Pop-up Save Prompt"><figcaption></figcaption></figure></div>

#### **Campos do pop-up Save Prompt**

* **Prompt Name:** informe um nome para identificar o prompt.
* **Save Prompt Publicly (caixa de seleção):** quando marcada, o prompt é salvo como **Global Prompt**. Os Global Prompts são compartilhados entre todos os tenants e não podem armazenar **valores** de variáveis (somente **nomes** de variáveis).
* **Edit Variables:** abre o [**pop-up Prompt Variables**](prompt-writing-guide.md#popup-de-variaveis-do-prompt) para revisar ou ajustar as definições das variáveis antes de salvar.

**Ações**

* **Cancel:** fecha o pop-up sem salvar.
* **Save:** salva o prompt com o nome e a configuração de visibilidade informados.

### 4. Controles de execução do prompt

Quando um prompt está em execução, os usuários têm várias opções de controle para gerenciar ou intervir no processo de execução:

* **Pause Prompt:** interrompe temporariamente a execução atual. Útil se você quiser observar o estado atual ou preparar o sistema para as próximas etapas.&#x20;
* **Resume Prompt:** continua a execução do ponto em que foi pausada. ![](<../../.gitbook/assets/image (3) (1).png>)
* **Cancel Prompt:** interrompe a execução por completo e redefine a sessão. Útil quando o prompt precisa ser abortado ou reiniciado por causa de um comportamento incorreto ou de mudanças na entrada.&#x20;
* **Take Control:** permite que o usuário intervenha manualmente, interagindo diretamente com o sistema. Útil se o operador travar ou interpretar uma etapa de forma errada. Ao assumir o controle, o prompt é **pausado automaticamente** e passa para o modo manual até que você escolha retomar ou cancelar.

### 5. Visualização detalhada do operador

Quando um prompt é iniciado, um botão adicional passa a ficar disponível e permite alternar para uma **visualização detalhada da execução**. ![](<../../.gitbook/assets/Detailed view .jpg>)

* **Open Detail View:** este botão leva a uma visualização dedicada que mostra, passo a passo e em tempo real, o que o operador está fazendo.

Na visualização detalhada, os usuários podem:

* Acompanhar cada ação executada (por exemplo, cliques, entradas, esperas).
* Ver qual etapa está ativa no momento.
* Identificar onde ocorrem problemas se o prompt encontrar dificuldades.
* Usar as mesmas ações **Pause**, **Resume**, **Cancel** e **Take Control**.

<div align="left"><figure><img src="../../.gitbook/assets/detailed view 2 .jpg" alt="" width="563"><figcaption></figcaption></figure></div>
