# Gerenciamento de Cache

<figure><img src="../../.gitbook/assets/cache_management.png" alt="Gerenciamento de Cache"><figcaption><p>Página Gerenciamento de Cache</p></figcaption></figure>

O Gerenciamento de Cache controla a limpeza automática do cache de dados acessados com frequência. Ativar o cache melhora o desempenho, pois reduz chamadas repetidas à API.

## Limpar Cache

Clique no botão **Clear Cache** (canto superior direito) para invalidar imediatamente todos os dados em cache manualmente.

## Tabela de Cache

| Coluna | Descrição |
|--------|-------------|
| **Object** | O tipo de dados em cache (por exemplo, Receive Delivery Cache, Purchase Order Cache). |
| **Status** | Alternador para ativar ou desativar o cache para este objeto. |
| **TTL** | Time to Live (tempo de vida) em minutos — por quanto tempo os dados em cache permanecem válidos antes de serem atualizados automaticamente. Defina como `0` para desativar a expiração automática. |

## Caches Disponíveis

| Cache | Descrição |
|-------|-------------|
| **Receive Delivery Cache** | Armazena em cache os dados de recebimento de mercadorias usados na correspondência de PO. |
| **Purchase Order Cache** | Armazena em cache os dados de pedidos de compra para uma consulta mais rápida durante o processamento de documentos. |
| **Task and Notification Cache** | Armazena em cache a contagem de tarefas e os dados de notificações exibidos no painel. |
