# Debug Collector

O Debug Collector captura uma imagem completa da sua sessão DocBits — atividade de rede, erros, ambiente do navegador e métricas de desempenho — empacota como um relatório JSON e pode, opcionalmente, abrir um chamado de suporte diretamente a partir da mesma janela.

## Como acessar

Pressione <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> no Windows e Linux ou <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> no macOS. A janela Performance Report abre imediatamente.

<figure><img src="../../.gitbook/assets/debug-collector-dialog.png" alt="Janela do Debug Collector"><figcaption><p>A janela Performance Report mostra a captura e um formulário integrado para criação de chamado.</p></figcaption></figure>

## O que é capturado

* **Chamadas de API** — as últimas 60 chamadas REST e WebSocket, com tempos, códigos de status e URLs acessadas. Chamadas com mais de dois segundos são sinalizadas separadamente.
* **Erros** — erros JavaScript recentes e rejeições de promessas não capturadas a partir do console do navegador.
* **Logs de console** — as mensagens de log mais recentes da aplicação.
* **Ambiente** — versão do navegador, sistema operacional, tamanho da tela e flags de funcionalidades ativas.
* **Contexto do usuário** — sua função, organização e a página em que estava ao tirar a captura.
* **Métricas de desempenho** — tempos de carregamento da página (LCP, FCP), uso de memória e tamanho do DOM.
* **Trace IDs** — identificadores de correlação que ligam a captura aos logs do backend.

## Criando um chamado de suporte direto da janela

Você não precisa baixar nem anexar nada manualmente — a janela contém um formulário **Create Support Ticket**.

1. Preencha seu e-mail, mantenha o assunto sugerido ou substitua-o, escolha uma prioridade e adicione notas explicando o que estava fazendo quando o problema aconteceu.
2. Clique em **Send Report**. A captura JSON é anexada e o chamado é criado em um único passo.

Pronto — o suporte recebe o chamado com todos os dados necessários para reproduzir o caso.

Se quiser uma cópia local da captura, use **Copy Debug Data** para copiar o JSON para a área de transferência ou use Salvar como do navegador para guardar o relatório como arquivo `.json`.

## Privacidade e manuseio de dados

* Tokens de autenticação e cabeçalhos sensíveis são removidos das chamadas de API capturadas antes da construção da imagem.
* Nada sai do seu navegador até você clicar em **Send Report** — o atalho apenas abre a janela.

<mark>Revise a captura antes de enviar se estava trabalhando com documentos contendo dados de clientes. Identificadores de documento visíveis nas URLs aparecerão no relatório.</mark>
