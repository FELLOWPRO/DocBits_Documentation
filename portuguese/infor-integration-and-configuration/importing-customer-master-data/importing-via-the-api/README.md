---
description: Enviar dados mestres para o DocBits manualmente através da API
---

# Importar através da API

Os dados mestres chegam normalmente ao DocBits de forma automática através do seu fluxo de dados ION. As páginas desta secção descrevem como enviar os mesmos dados manualmente através da interface de teste da API — útil quando quer reimportar um registo, carregar algo que nunca chegou ou experimentar um novo mapeamento de campos antes de ativar o fluxo automático.

Cada página segue os mesmos cinco passos: abrir a ligação da API do seu ambiente, autorizar com o seu Org ID e a sua API key, preencher o formulário, executar e verificar se os dados chegaram.

* [Importar Fornecedores (Supplier BOD)](supplier-bod.md)
* [Importar Ordens de Compra (Purchase Order BOD)](purchase-order-bod.md)
* [Importar Receções de Mercadorias (Receive Delivery BOD)](receive-delivery-bod.md)
* [Importar Dados Mestres de XML](master-data-xml.md)

## Do que precisa

* **Uma API key** — consulte [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md).
* **O seu Org ID** — em **Settings → Integration & SSO**, na secção **ID**.
* **Os próprios dados**, como ficheiro XML ou como conteúdo XML que possa colar.

{% hint style="warning" %}
Uma importação escreve diretamente nos dados mestres da sua organização. Verifique para que ambiente, que região e que organização está a apontar antes de executar.
{% endhint %}
