# Guia de Escrita de Prompt

Este guia explica como escrever prompts eficazes para o Operador DocBits. Prompts são instruções passo a passo que direcionam o operador a realizar tarefas específicas, como navegar em páginas da web, interagir com elementos de UI e inserir dados.

## O que é um Prompt?

Um prompt é uma sequência de instruções escritas em texto que guia o operador a executar um fluxo de trabalho. Prompts podem incluir comandos como clicar em botões, preencher formulários, aguardar o carregamento de páginas ou elementos, e muito mais.

## Sintaxe e Estrutura do Prompt

* Cada instrução deve ser escrita como uma etapa numerada.
* Use linguagem clara e concisa para descrever cada ação.
* Especifique elementos de UI por nome, rótulo ou número de índice para garantir precisão.
* Use formatação consistente para melhorar a legibilidade.

## Usando Variáveis em Prompts

Variáveis permitem que você torne os prompts dinâmicos inserindo diferentes valores em tempo de execução. Em vez de codificar valores como datas ou números de documentos, use espaços reservados dentro de chaves—por exemplo: `{invoice_number}`, `{url}`, ou `{purchase_order}`.

Isso torna os prompts reutilizáveis e adaptáveis em diferentes fluxos de trabalho ou conjuntos de dados.

### Como Usar Variáveis

* Escreva variáveis dentro de chaves no texto do seu prompt:
  * Insira o número da fatura: {invoice\_number} no campo 'Número da fatura HP'.
* Cada variável deve ter um nome único (por exemplo, `invoice_number`, `url`, `document_type`).
* Nomes de variáveis não devem incluir espaços ou caracteres especiais (underscores são permitidos).
* Para fluxos de trabalho, os nomes das variáveis devem corresponder exatamente aos IDs dos campos do documento para permitir o mapeamento automático de dados.

## Popup de Variáveis do Prompt

Para abrir o popup de Variáveis do Prompt, clique no **ícone de engrenagem** localizado ao lado do campo de entrada do prompt.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FvEC6vmU6CCsAa36OK9V6%252Fimage.png%3Falt%3Dmedia%26token%3Dfd26ce70-0de4-4bdb-adf4-85d0052f9d53&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=fc29eaa3&#x26;sv=2" alt="" width="375"></div>

## Layout e Controles do Popup

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FftlMKp0ql0miqBTdCtt3%252Fimage.png%3Falt%3Dmedia%26token%3D979b7c8e-0728-4a10-bb8a-3275203c4c3d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=b07844a9&#x26;sv=2" alt="" width="375"></div>

* **Campo de Entrada de Chave:** Insira o nome da variável aqui (sem chaves).
* **Campo de Entrada de Valor:** Insira o valor a ser usado para esta variável quando o prompt é executado.
* **Salvar como Sensível (Checkbox):** Quando marcado, isso marca o valor da variável como sensível. Valores sensíveis são criptografados e ocultos em fluxos de trabalho para proteger informações confidenciais de usuários não autorizados.
* **Botão Adicionar (+):** Clique para adicionar outra linha de entrada de par chave-valor.
* **Ícone de Exclusão (Lixeira):** Quando existem vários pares chave-valor, todos os pares, exceto o primeiro, mostram um pequeno ícone de lixeira para excluir esse par específico.
* **Botão Limpar:** Reseta o popup ao limpar todos os pares chave-valor e valores inseridos.
* **Botão Salvar:** Salva todas as variáveis definidas e seus valores para o prompt atual.
