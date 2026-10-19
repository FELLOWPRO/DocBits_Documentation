# Activity Logging

<figure><img src="../../../.gitbook/assets/activity_logging.png" alt="Activity Logging"><figcaption><p>Página Activity Logging</p></figcaption></figure>

O Activity Logging oferece uma visão em tempo real dos eventos do sistema em todos os serviços do DocBits. Use-o para monitorar a atividade de processamento, solucionar erros e auditar o comportamento do sistema.

## Banner de Analytics

Na parte superior da página, um banner leva ao **Analytics Dashboard**, com gráficos, métricas e monitoramento em tempo real.

## Filtros

| Filtro | Descrição |
|--------|-------------|
| **Time Range** | Selecione uma janela de tempo (por exemplo, Today, Last 7 Days, Last 30 Days). |
| **Severity** | Ative ou desative os níveis de severidade a incluir ou excluir: **Debug**, **Info**, **Warning**, **Error**. Cada chip mostra a contagem atual. |
| **Service** | Filtre os logs por serviço (por exemplo, api, auth, api-service). |
| **Search logs** | Pesquisa de texto livre nas mensagens de log. |

## Tabela de Logs

| Coluna | Descrição |
|--------|-------------|
| **Timestamp** | Data e hora em que o evento ocorreu. Ordenável. |
| **Severity** | Selo colorido: Info (azul), Warning (amarelo), Error (vermelho), Debug (cinza). |
| **Component** | O serviço ou módulo que gerou o log (por exemplo, api, auth, api-service). |
| **Message** | A mensagem de log completa com os detalhes do evento. |

Os resultados são paginados — use os controles na parte inferior para navegar entre as páginas.

## Ações do Rodapé

| Ação | Descrição |
|--------|-------------|
| **Auto-refresh** | Ative para atualizar automaticamente a visualização dos logs em intervalos regulares. |
| **Refresh Now** | Atualize manualmente os dados de log. |
| **Export JSON** | Exporte os logs filtrados atuais como um arquivo JSON. |
| **Download Logs** | Baixe os dados de log completos. |
