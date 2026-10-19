---
description: Como importar dados mestres diretamente no DocBits.
---

# Dados Mestres Personalizados

#### Ativar os dados mestres personalizados <a href="#activating-custom-master-data" id="activating-custom-master-data"></a>

No painel, acesse Configurações → Processamento de documentos → Módulo.

![](<../../.gitbook/assets/DocBits_CMD_1 (1).png>)

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_2.png" alt="" width="375"><figcaption></figcaption></figure></div>

Em Módulo, ative os dados mestres personalizados (Custom Master Data) clicando no controle deslizante, como mostrado abaixo.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_3.png" alt="" width="375"><figcaption></figcaption></figure></div>

#### Visão geral da funcionalidade <a href="#feature-overview" id="feature-overview"></a>

Para adicionar seus próprios dados mestres ao DocBits, acesse Master Data Lookup em Configurações.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_4.png" alt="" width="375"><figcaption></figcaption></figure></div>

Clique em “Custom Master Data”.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_5.png" alt="" width="375"><figcaption></figcaption></figure></div>

Em seguida, você pode optar por criar um Template (modelo) ou um Endpoint.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_6.png" alt="" width="375"><figcaption></figcaption></figure></div>

#### Criar um template <a href="#create-a-template" id="create-a-template"></a>

A primeira etapa é escolher entre usar o arquivo de API ION da sua organização ou usar OAuth2 e informar os dados necessários.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_7.png" alt="" width="375"><figcaption></figcaption></figure></div>

Em seguida, vamos configurar as predefinições. Aqui você informará o nome da tabela de dados mestres e a URL da chamada de API.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_8.png" alt="" width="375"><figcaption></figcaption></figure></div>

Depois, você precisará informar o caminho JSON usando a notação de pontos. Para mais informações sobre a notação de pontos, clique [aqui](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/).

Por fim, você precisará mapear os dados para as colunas que deseja criar, como no exemplo abaixo.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_9.png" alt="" width="375"><figcaption></figcaption></figure></div>

Depois disso, clique em Concluído (Done) para que os novos dados mestres sejam criados e preenchidos.

#### Criar um endpoint <a href="#create-an-endpoint" id="create-an-endpoint"></a>

A primeira etapa é escolher entre usar o arquivo de API ION da sua organização, usar OAuth2 ou deixar essa opção em branco e informar os dados necessários.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_10.png" alt="" width="375"><figcaption></figcaption></figure></div>

Em seguida, vamos configurar as predefinições. Aqui você informará o nome da tabela de dados mestres e a URL da chamada de API.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_8.png" alt="" width="375"><figcaption></figcaption></figure></div>

Depois, você precisará informar o caminho JSON usando a notação de pontos. Para mais informações sobre a notação de pontos, clique [aqui](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/).

Por fim, você precisará mapear os dados para as colunas que deseja criar, como no exemplo abaixo.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_9.png" alt="" width="375"><figcaption></figcaption></figure></div>

Depois disso, clique em Concluído (Done) para que os novos dados mestres sejam criados e preenchidos.
