---
description: Como importar dados mestres diretamente no DocBits.
---

# Dados Mestres Personalizados

#### Ativar os dados mestres personalizados <a href="#activating-custom-master-data" id="activating-custom-master-data"></a>

No painel, acesse Configurações → Processamento de documentos → Módulo.

![](<../../.gitbook/assets/DocBits_CMD_1 (1).png>)

<div align="left"><figure><img src="../../.gitbook/assets/site-extra-modules-document-integration-pt.png" alt="Módulos de integração de documentos: scripts, digitalização, códigos de barras e dados mestre personalizados. A etiqueta Select do seletor de códigos de barras mantém-se em inglês na versão ilustrada."><figcaption><p>Módulos de integração de documentos: scripts, digitalização, códigos de barras e dados mestre personalizados. A etiqueta Select do seletor de códigos de barras mantém-se em inglês na versão ilustrada.</p></figcaption></figure></div>

Em Módulo, ative os dados mestres personalizados (Custom Master Data) clicando no controle deslizante, como mostrado abaixo.

<div align="left"></div>

#### Visão geral da funcionalidade <a href="#feature-overview" id="feature-overview"></a>

Para adicionar seus próprios dados mestres ao DocBits, acesse Master Data Lookup em Configurações.

<div align="left"><figure><img src="../../.gitbook/assets/site-extra-master-data-overview-pt.png" alt="Consulta de dados mestre: fontes e tabela de fornecedores com valores ocultos."><figcaption><p>Consulta de dados mestre: fontes e tabela de fornecedores com valores ocultos.</p></figcaption></figure></div>

Clique em “Custom Master Data”.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_5.png" alt="Página de configurações do Master Data Lookup com os lookups Additional charge Costing Element, Purchase order, Purchase order Header e Supplier" width="375"><figcaption></figcaption></figure></div>

Em seguida, você pode optar por criar um Template (modelo) ou um Endpoint.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_6.png" alt="Painel Custom Master Data com os botões Create Template e Create Endpoint" width="375"><figcaption></figcaption></figure></div>

#### Criar um template <a href="#create-a-template" id="create-a-template"></a>

A primeira etapa é escolher entre usar o arquivo de API ION da sua organização ou usar OAuth2 e informar os dados necessários.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_7.png" alt="Passo Select Preset do assistente do Master Data Lookup com a pergunta What API do you want to use e as opções ION API e OAUTH2" width="375"><figcaption></figcaption></figure></div>

Em seguida, vamos configurar as predefinições. Aqui você informará o nome da tabela de dados mestres e a URL da chamada de API.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_8.png" alt="Passo Configure Preset do assistente do Master Data Lookup com Preset Name, Application Type, campo GET URL e os separadores PARAMS, HEADERS, AUTHORIZATION e BODY" width="375"><figcaption></figcaption></figure></div>

Depois, você precisará informar o caminho JSON usando a notação de pontos. Para mais informações sobre a notação de pontos, clique [aqui](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/).

Por fim, você precisará mapear os dados para as colunas que deseja criar, como no exemplo abaixo.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_9.png" alt="Assistente do Master Data Lookup com Select Table Columns, uma resposta JSON à esquerda e as colunas de mapeamento Column Name, Spaltenwert Name e Test Extraction" width="375"><figcaption></figcaption></figure></div>

Depois disso, clique em Concluído (Done) para que os novos dados mestres sejam criados e preenchidos.

#### Criar um endpoint <a href="#create-an-endpoint" id="create-an-endpoint"></a>

A primeira etapa é escolher entre usar o arquivo de API ION da sua organização, usar OAuth2 ou deixar essa opção em branco e informar os dados necessários.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_10.png" alt="Passo Select Preset do assistente de endpoints do Master Data Lookup com Choose a preset for your endpoint e as opções BLANK, ION API e OAUTH2" width="375"><figcaption></figcaption></figure></div>

Em seguida, vamos configurar as predefinições. Aqui você informará o nome da tabela de dados mestres e a URL da chamada de API.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_8.png" alt="Passo Configure Preset do assistente do Master Data Lookup com Preset Name, Application Type, campo GET URL e os separadores PARAMS, HEADERS, AUTHORIZATION e BODY" width="375"><figcaption></figcaption></figure></div>

Depois, você precisará informar o caminho JSON usando a notação de pontos. Para mais informações sobre a notação de pontos, clique [aqui](https://docs.hevodata.com/sources/engg-analytics/streaming/rest-api/writing-jsonpath-expressions/).

Por fim, você precisará mapear os dados para as colunas que deseja criar, como no exemplo abaixo.

<div align="left"><figure><img src="../../.gitbook/assets/DocBits_CMD_9.png" alt="Assistente do Master Data Lookup com Select Table Columns, uma resposta JSON à esquerda e as colunas de mapeamento Column Name, Spaltenwert Name e Test Extraction" width="375"><figcaption></figcaption></figure></div>

Depois disso, clique em Concluído (Done) para que os novos dados mestres sejam criados e preenchidos.
