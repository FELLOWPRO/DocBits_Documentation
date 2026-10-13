# Gerenciamento de Cache

![Cache Management](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/cache_management.png)

O Gerenciamento de Cache controla a limpeza automática do cache para dados acessados com frequência. Ativar o cache melhora o desempenho, reduzindo chamadas de API repetidas.

## Limpar o cache

Clique no botão **Clear Cache** (canto superior direito) para invalidar imediatamente, de forma manual, todos os dados em cache.

## Tabela de cache

| Coluna | Descrição |
|--------|-------------|
| **Object** | O tipo de dado em cache (por exemplo, Receive Delivery Cache, Purchase Order Cache). |
| **Status** | Ative ou desative o cache para este objeto. |
| **TTL** | Time to Live em minutos — por quanto tempo os dados em cache permanecem válidos antes de serem atualizados automaticamente. Defina como `0` para desativar a expiração automática. |

## Caches disponíveis

| Cache | Descrição |
|-------|-------------|
| **Receive Delivery Cache** | Armazena em cache os dados de recebimento de entregas usados na correspondência de pedidos de compra (PO). |
| **Purchase Order Cache** | Armazena em cache os dados de pedidos de compra para uma consulta mais rápida durante o processamento de documentos. |
| **Task and Notification Cache** | Armazena em cache a contagem de tarefas e os dados de notificações exibidos no dashboard. |
