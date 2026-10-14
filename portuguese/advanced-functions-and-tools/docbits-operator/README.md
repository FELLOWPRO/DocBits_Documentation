# Operador DocBits

## Visão Geral

O **Operador DocBits** é um assistente de automação alimentado por IA projetado para simplificar tarefas repetitivas em seus fluxos de trabalho. Os usuários criam _prompts_ - instruções passo a passo aprimoradas com variáveis - que guiam a IA para navegar, inserir dados e clicar através de interfaces automaticamente. Isso reduz o esforço manual e acelera as operações de rotina.

## Habilitando o Operador DocBits

Para habilitar o Operador DocBits, siga estas etapas:

1. **Navegue até Configurações**:
   * No Painel, vá para **Configurações**.
   *   Selecione **Processamento de Documentos** e depois escolha **Módulo**.

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4Yyo7aXyVeWyfJHclHpK%252Fimage.png%3Falt%3Dmedia%26token%3D0071c149-3ea8-452b-a2e3-0fbbc9d3b496\&width=768\&dpr=4\&quality=100\&sign=23009aa7\&sv=2)
2. **Habilitar o Recurso**:
   * Role para baixo para localizar a opção **Operador DocBits**.
   *   Alterne o controle deslizante para habilitar o **Operador DocBits**.

       <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FyqNyGI2OelO415pf3RHN%252Fimage.png%3Falt%3Dmedia%26token%3D8899a256-a1d6-486f-aaf6-b8e244f9b348&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=ce097a28&#x26;sv=2" alt="" width="563"></div>

## Acessando a Interface

*   Uma vez que o recurso está habilitado, abra o **Operador DocBits** no menu de navegação principal.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FS67AFPuaQ3CNXQ7Oe80V%252Fimage.png%3Falt%3Dmedia%26token%3D6b6d6782-cc16-48e6-8622-5c596ac54f57\&width=768\&dpr=4\&quality=100\&sign=e6d0fd8e\&sv=2)

### **1. Entrada de Prompt**

Na parte inferior da tela, há um campo de entrada rotulado como _“Digite seu prompt aqui…”_. Aqui é onde os usuários escrevem instruções para o operador seguir.

Ao lado do campo de entrada estão vários botões de controle:

* **Variáveis de Prompt** – Abre um popup onde você pode inserir pares chave-valor usados no prompt. As variáveis são escritas usando chaves, como `{numero_fatura}` ou `{url}`. Esses valores se aplicam apenas ao prompt atual no campo de entrada.
* **Salvar Prompt** – Salva o prompt atual. Escolha salvá-lo como:
  * **Prompt da Organização** – Editável dentro da sua organização; inclui tanto o prompt quanto os valores de variáveis definidos.
  * **Prompt Global** – Compartilhado entre todos os inquilinos; inclui apenas o prompt e espaços reservados de variáveis (nenhum valor é salvo).
* **Limpar Chat** – Limpa a conversa atual com o operador, mas deixa o prompt no campo de entrada inalterado. Útil ao reutilizar ou refinar um prompt.

Para orientações detalhadas sobre como escrever prompts eficazes - incluindo sintaxe, variáveis e exemplos - consulte o [**Guia de Escrita de Prompt**](prompt-writing-guide.md).

### **2. Navegação na Barra Lateral**

Use o ícone no canto superior esquerdo para abrir ou fechar a barra lateral. A barra lateral mostra prompts salvos, organizados em duas categorias:

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fm08uq4Kqj0SEZWSnlnoS%252Fimage.png%3Falt%3Dmedia%26token%3D4ba4542a-a707-4907-ae5e-b06286af8240&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=ef6b0706&#x26;sv=2" alt="" width="375"></div>

* **Prompts da Organização**: Editáveis e reutilizáveis dentro da sua organização.
* **Prompts Globais**: Compartilhados entre todos os inquilinos. Estes não podem armazenar variáveis e não podem ser editados ou excluídos.
  *   Um prompt global ainda é editável e excluível pela **organização que o criou**, onde aparece sob Prompts da Organização.

      <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlVnXjwtnxAtqsftRvYUi%252Fimage.png%3Falt%3Dmedia%26token%3D60b3d0dd-3eee-40a8-b447-c9e91087a27d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=f9b364a&#x26;sv=2" alt="" width="375"></div>
* **Funcionalidade de Busca:** uma barra de pesquisa no topo da barra lateral permite aos usuários encontrar rapidamente prompts salvos por nome ou palavra-chave.
* **Referência de Ícones:** Cada prompt salvo tem um conjunto de ícones de ação
  * **Seta** – Iniciar o prompt
  * **Caneta** – Editar o prompt (disponível apenas para prompts de sua própria organização)
  * **Lixeira** – Excluir o prompt (disponível apenas para prompts de sua própria organização)

### 3. Salvar Prompt

Clicar no botão **Salvar Prompt** abre um popup onde você pode salvar o prompt atual para uso futuro.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FgrBpDnbo80nPkozFhgCE%252Fimage.png%3Falt%3Dmedia%26token%3Dd31c06fc-dcd0-4fbe-9e1e-6c5bc001e4bb&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=900c948&#x26;sv=2" alt="" width="375"></div>

#### **Campos do Popup de Salvar Prompt**

* **Nome do Prompt:** Insira um nome para identificar o prompt.
* **Salvar Prompt Publicamente (Checkbox):** Quando marcado, o prompt será salvo como um **Prompt Global**. Prompts Globais são compartilhados entre todos os inquilinos e não podem armazenar **valores** de variáveis (apenas **nomes** de variáveis).
* **Editar Variáveis:** Abre o [**Popup de Variáveis de Prompt**](prompt-writing-guide.md) para revisar ou ajustar definições de variáveis antes de salvar.

**Ações**

* **Cancelar:** Fecha o popup sem salvar.
* **Salvar:** Salva o prompt usando o nome especificado e a configuração de visibilidade.

### 4. Controles de Execução de Prompt

Quando um prompt está em execução, os usuários têm várias opções de controle para gerenciar ou intervir no processo de execução:

* **Pausar Prompt:** Pára temporariamente a execução atual. Útil se você deseja observar o estado atual ou preparar o sistema para os próximos passos.\
  ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzG9U15jmVTb202efDR5l%252Fimage.png%3Falt%3Dmedia%26token%3Dee52f250-15d4-4139-b612-ba5ff1876841\&width=300\&dpr=4\&quality=100\&sign=329efe81\&sv=2)
* **Continuar Prompt:** Continua a execução a partir do ponto em que foi pausado. ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FewGCZ9wSXt7VsvS8RjZH%252Fimage.png%3Falt%3Dmedia%26token%3D92ec27df-07b4-4e9f-a125-6f0a87d9db47\&width=300\&dpr=4\&quality=100\&sign=8e03589c\&sv=2)
* **Cancelar Prompt:** Interrompe completamente a execução e reinicia a sessão. Isso é útil se o prompt precisar ser abortado ou reiniciado devido a comportamento incorreto ou alterações na entrada. ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FYUKk03iazolJlx6reOO3%252Fimage.png%3Falt%3Dmedia%26token%3Da722c82b-e4c1-4c23-8c56-a31f2685cce7\&width=300\&dpr=4\&quality=100\&sign=170c122e\&sv=2)
* **Assumir o Controle:** Permite ao usuário intervir manualmente interagindo diretamente com o sistema. Isso é útil se o operador ficar preso ou interpretar erroneamente um passo. Assumir o controle **pausa automaticamente** o prompt e muda para o modo manual até que você escolha continuar ou cancelar.

### 5. Visualização Detalhada do Operador

Uma vez que um prompt é iniciado, um botão adicional se torna disponível que permite aos usuários alternar para uma **visualização detalhada da execução**.\
![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9kObRWZFb3woomL045KL%252FDetailed%2520view%2520.jpg%3Falt%3Dmedia%26token%3Dbd0f94e2-84f2-4fd0-ae89-82408e85e03a\&width=300\&dpr=4\&quality=100\&sign=3aefc79\&sv=2)

* **Abrir Visualização Detalhada:** Este botão leva a uma visualização dedicada que mostra, passo a passo, o que o operador está fazendo em tempo real.

Na visualização detalhada, os usuários podem:

* Monitorar cada ação sendo executada (por exemplo, cliques, entradas, esperas).
* Ver qual etapa está atualmente ativa.
* Identificar onde ocorrem problemas se o prompt encontrar problemas.
* Usar as mesmas ações de **Pausar**, **Continuar**, **Cancelar** e **Assumir o Controle**.
