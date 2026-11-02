# Acionar Prompts com um Fluxo de Trabalho

Este guia explica como configurar um fluxo de trabalho do DocBits para acionar automaticamente um prompt salvo. Isso permite integrar prompts do Operador em fluxos de processamento de documentos sem entrada manual.

## Passo 1: Criar um Prompt

Antes de vincular um prompt a um fluxo de trabalho:

* Certifique-se de que seu prompt já foi criado
* Inclua todas as **variáveis** necessárias no corpo do prompt.

Se precisar de ajuda para escrever ou salvar prompts, consulte o [Guia de Escrita de Prompts](../prompt-writing-guide.md) e [Visão Geral da Interface do Operador](../).

## Passo 2: Configurar o Fluxo de Trabalho

Antes de configurar o cartão de Prompt do Operador, certifique-se de que seu fluxo de trabalho foi criado corretamente.

1. Navegue até o **Construtor de Fluxo de Trabalho** na interface do DocBits.
2. Crie um novo fluxo de trabalho ou abra um existente.
3. Defina as **condições de acionamento**—essas determinam quando o fluxo de trabalho será iniciado (por exemplo, tipo de documento, status, presença de campo, etc.).
4. Adicione as etapas de **ação necessárias** ao seu fluxo de trabalho conforme necessário.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fd3qJJhFDHTXDUfUedjaF%252Fimage.png%3Falt%3Dmedia%26token%3D310f9e9c-9e79-4987-af01-2d914f1abbe7&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=873cf566&#x26;sv=2" alt="" width="375"></div>

## Passo 3: Configurar o Cartão de Prompt do Operador no Fluxo de Trabalho

No Construtor de Fluxo de Trabalho, use o **cartão de Prompt do Operador** para configurar um prompt que deve ser executado quando as condições do fluxo de trabalho forem atendidas.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fg11jtpdL4j3mJveYvWSX%252Fimage.png%3Falt%3Dmedia%26token%3Db208669e-b6a8-4879-b08b-d9ba353e908d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=974876f7&#x26;sv=2" alt="" width="375"></div>

### Opções de Configuração Principais

* **Script:** Selecione o **Prompt da Organização** salvo a ser executado.
* **Dados do Script (Variáveis):** Se o prompt selecionado contiver variáveis, defina seus valores aqui usando pares de chave-valor.
  * Se uma variável for deixada em branco aqui, o sistema tentará preenchê-la automaticamente **a partir do documento**.
  * Para que isso funcione, o nome da variável no prompt deve **corresponder exatamente** ao **ID do campo** do atributo do documento.
* **Máximo de Etapas:** Defina o número máximo de etapas que o operador pode executar durante este prompt.
* **Tentativas Máximas:** Defina quantas vezes o sistema deve tentar o prompt em caso de falha.
* **Modo de Execução:** Escolha se o prompt deve ser executado:
  * **Na Nuvem**
  * **Localmente** (necessário se seu ERP ou sistema de destino estiver hospedado localmente)
