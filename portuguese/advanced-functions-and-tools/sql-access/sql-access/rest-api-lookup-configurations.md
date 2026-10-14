# Configurações de lookup por API REST

## Tabela `public.rest_api_lookup_configurations`

### Colunas

* `id`: interno
* `org_id`: ID da organização
* `sub_org_id`: interno
* `data_key`: interno
* `url`: interno
* `method`: interno
* `params`: texto
* `headers`: texto
* `body`: texto
* `body_type`: interno
* `authentication_type`: interno
* `authentication_json`: texto
* `data_base_path`: interno
* `column_paths`: texto
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `deleted_on`: timestamp com fuso horário
* `is_template`: booleano
* `is_dynamic`: booleano

### Análise e descrição

## Documentação técnica: tabela `public.rest_api_lookup_configurations`

### Introdução

A tabela `public.rest_api_lookup_configurations` foi projetada para armazenar as configurações de consultas (lookups) por API REST dentro de uma organização. Essa tabela contém as informações essenciais para executar requisições de API, incluindo detalhes sobre os endpoints, os métodos de autenticação e as configurações de requisição e resposta. Ela parece ser usada para construir chamadas de API dinamicamente e interpretar seus resultados.

### Descrição das colunas

#### id

* **Significado**: identificador único de cada entrada de configuração.
* **Função**: chave primária.
* **Conteúdo típico**: strings UUID como `5e9b3637-79a1-4535-99cf-9247dfa48960`.
* **Observação**: é a chave única para identificar uma configuração específica de lookup de API.

#### org\_id

* **Significado**: identificador da organização proprietária da configuração.
* **Função**: chave estrangeira.
* **Conteúdo típico**: strings UUID que representam IDs de organizações.
* **Observação**: vincula a configuração a uma organização.

#### sub\_org\_id

* **Significado**: identificador de uma suborganização dentro da organização principal.
* **Função**: chave estrangeira.
* **Conteúdo típico**: strings UUID que representam IDs de suborganizações.
* **Observação**: permite uma granularidade maior dentro das organizações.

#### data\_key

* **Significado**: um rótulo ou chave para identificar os dados ou o endpoint da API.
* **Função**: campo descritivo.
* **Conteúdo típico**: texto descritivo como `bank_codes`.
* **Observação**: usada para distinguir entre diferentes tipos de dados ou endpoints.

#### url

* **Significado**: a URL do endpoint da API a ser chamado.
* **Função**: campo descritivo.
* **Conteúdo típico**: strings de URL como `/M3/m3api-rest/v2/execute/CRS692MI/LstByID`.
* **Observação**: representa o endpoint para o qual a requisição HTTP é enviada.

#### method

* **Significado**: método HTTP usado na requisição da API.
* **Função**: campo descritivo.
* **Conteúdo típico**: métodos HTTP comuns como `GET`.
* **Observação**: determina o tipo de requisição HTTP a ser executada.

#### params

* **Significado**: parâmetros a serem incluídos na requisição da API.
* **Função**: campo de configuração.
* **Conteúdo típico**: JSON ou pares chave-valor (frequentemente `None` se não for usado).
* **Observação**: contém os parâmetros dinâmicos da requisição.

#### headers

* **Significado**: cabeçalhos HTTP a serem incluídos na requisição.
* **Função**: campo de configuração.
* **Conteúdo típico**: dados em JSON ou texto (frequentemente `None` se não for usado).
* **Observação**: usados para incluir metadados adicionais na requisição.

#### body

* **Significado**: o corpo da requisição HTTP.
* **Função**: campo de configuração.
* **Conteúdo típico**: dados JSON ou outros dados serializados (frequentemente `None` se não for usado).
* **Observação**: contém a carga útil das requisições POST/PUT.

#### body\_type

* **Significado**: especifica o formato do corpo da requisição.
* **Função**: campo descritivo.
* **Conteúdo típico**: tipos MIME como `application/json`.
* **Observação**: indica o tipo de conteúdo do corpo.

#### authentication\_type

* **Significado**: tipo de autenticação usado na requisição da API.
* **Função**: campo descritivo.
* **Conteúdo típico**: métodos de autenticação como `ionapi`.
* **Observação**: determina como a requisição será autenticada.

#### authentication\_json

* **Significado**: detalhes da configuração de autenticação em formato JSON.
* **Função**: campo de configuração.
* **Conteúdo típico**: strings JSON com as informações de autenticação.
* **Observação**: contém as credenciais e os detalhes do endpoint para autenticação.

#### data\_base\_path

* **Significado**: caminho dentro da resposta da API do qual os dados devem ser extraídos.
* **Função**: campo de configuração.
* **Conteúdo típico**: expressões de caminho JSON como `$[results][0][records]`.
* **Observação**: usado para interpretar os dados da resposta da API.

#### column\_paths

* **Significado**: mapeia campos de dados para colunas na extração.
* **Função**: campo de configuração.
* **Conteúdo típico**: strings JSON que mapeiam campos da resposta da API para nomes de colunas.
* **Observação**: facilita a extração de dados da resposta da API.

#### created\_by

* **Significado**: identificador do usuário que criou a configuração.
* **Função**: campo técnico.
* **Conteúdo típico**: IDs inteiros como `1`.
* **Observação**: registra o criador da entrada de configuração.

#### created\_on

* **Significado**: timestamp de quando a configuração foi criada.
* **Função**: campo técnico.
* **Conteúdo típico**: timestamps como `2024-01-24T09:14:24.788788Z`.
* **Observação**: indica a data e a hora de criação.

#### last\_modified\_on

* **Significado**: timestamp da última modificação.
* **Função**: campo técnico.
* **Conteúdo típico**: timestamps (frequentemente `None` se não foi modificada).
* **Observação**: registra o momento da última atualização.

#### is\_deleted

* **Significado**: indicador que informa se uma configuração está marcada como excluída.
* **Função**: campo técnico.
* **Conteúdo típico**: valores booleanos como `False`.
* **Observação**: usado para a exclusão lógica de configurações.

#### deleted\_on

* **Significado**: timestamp de quando a configuração foi marcada como excluída.
* **Função**: campo técnico.
* **Conteúdo típico**: timestamps (frequentemente um valor de espaço reservado se não foi excluída).
* **Observação**: registra quando a configuração foi marcada como excluída.

#### is\_template

* **Significado**: indica se a configuração funciona como um modelo.
* **Função**: campo descritivo.
* **Conteúdo típico**: valores booleanos como `True`.
* **Observação**: identifica modelos para reutilização.

#### is\_dynamic

* **Significado**: especifica se a configuração é dinâmica.
* **Função**: campo descritivo.
* **Conteúdo típico**: valores booleanos como `False`.
* **Observação**: determina se a configuração se ajusta a dados que mudam.
