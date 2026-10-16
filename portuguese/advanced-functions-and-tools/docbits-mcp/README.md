# DocBits MCP

O DocBits expõe um servidor **Model Context Protocol (MCP)** que permite que assistentes de IA trabalhem com seus documentos, extração, busca, análises e configuração — diretamente a partir de um chat ou de uma sessão de programação. Qualquer cliente compatível com MCP pode se conectar: **Claude Code**, **Claude Desktop**, **Google Gemini CLI**, **OpenAI Codex** ou qualquer integração personalizada.

O servidor é montado na API do DocBits em `/v3/mcp` e tem o escopo da sua organização — cada chamada é executada com as permissões do usuário (ou da chave de API) que se conectou.

{% hint style="info" %}
**Endpoint — use a sua região (UE ou EUA):**

* Produção (UE) — `https://eu.api.docbits.com/v3/mcp`
* Produção (EUA) — `https://us.api.docbits.com/v3/mcp`

Veja [Configuração e Instalação](setup-and-configuration.md) para a matriz completa de hosts e como entrar com OAuth.
{% endhint %}

## O Que Você Pode Fazer?

Com o DocBits MCP, um assistente pode, em seu nome:

* **Encontrar e ler documentos** — listar, pesquisar (texto completo e por campos), abrir um documento, ler seu status, logs, imagens de página e pré-visualização de exportação
* **Trabalhar com dados extraídos** — ler campos e tabelas extraídos, corrigir valores de campos, extrair tabelas com IA, validar, aprovar e exportar para o seu ERP
* **Consultar o dashboard** — executar consultas do dashboard em linguagem natural, comparar modos de busca e inspecionar os recursos de busca
* **Obter análises** — resumos executivos, taxas de sucesso, tendências de volume, principais tipos de documento e detalhes de tarefas pendentes
* **Tratar faturas eletrônicas (eDocs)** — listar tipos de documentos eletrônicos, testar e verificar documentos eletrônicos, gerenciar atributos de extração personalizados
* **Gerenciar dados mestres** — fazer upsert de dados mestres de fornecedores, acionar consultas de fornecedores, importar BODs de faturas de fornecedores, manter mapeamentos de condições de pagamento e de descontos
* **Ler e alterar a configuração** — preferências da organização, tipos de documento, configurações de campos, usuários e cache
* **Verificar a saúde do sistema** — saúde da API e do Celery, usuário atual e informações da API

## Visão Geral das Ferramentas

O DocBits MCP agrupa bem mais de cem ferramentas nas categorias abaixo (o número exato cresce a cada versão; seu assistente lista o conjunto atual). A maioria espelha endpoints REST existentes do DocBits; consulte a [Referência da API](../../) para detalhes de requisição/resposta. Um assistente escolhe automaticamente a ferramenta certa a partir do seu pedido; as tabelas são um mapa do que está disponível.

### Documentos e Processamento

| Ferramenta                              | Descrição                                                    |
| --------------------------------------- | ------------------------------------------------------------ |
| `list_documents`                        | Lista os documentos da organização (com filtros)             |
| `get_document` / `get_document_by_name` | Abre um documento por ID ou nome de arquivo                  |
| `upload_document`                       | Envia um novo documento para processamento                   |
| `get_document_status`                   | Status atual de um documento no pipeline                     |
| `get_document_logs`                     | Entradas do log de processamento de um documento             |
| `query_org_logs`                        | Percorre página por página os logs de serviço da organização |
| `restart_document`                      | Executa novamente o pipeline de processamento                |
| `delete_document`                       | Exclui um documento                                          |
| `get_pending_documents_count`           | Quantos documentos aguardam validação                        |

### Extração e Validação

| Ferramenta                                          | Descrição                                                                 |
| --------------------------------------------------- | ------------------------------------------------------------------------- |
| `get_extracted_fields` / `get_document_fields`      | Lê os campos de cabeçalho extraídos                                       |
| `get_extracted_tables`                              | Lê as tabelas de itens extraídas                                          |
| `get_document_for_validation` / `get_next_document` | Abre um documento como a tela de validação o faz; busca o próximo da fila |
| `get_page_image`                                    | Imagem da página para verificações visuais                                |
| `update_document_fields`                            | Corrige ou define valores de campos                                       |
| `validate_document`                                 | Executa as regras de validação de campos                                  |
| `approve_document`                                  | Aprova um documento validado                                              |
| `validate_and_export`                               | Valida e depois exporta para o ERP                                        |
| `get_export_preview`                                | Pré-visualiza o payload de exportação antes do envio                      |

### Extração de Tabelas

Tudo o que a tela de validação e as configurações de colunas de tabela podem fazer com tabelas de itens. As ferramentas de configuração alteram os tipos de documento da organização; as ferramentas de extração e correção atuam sobre um documento; as ferramentas de regras armazenam o que o DocBits aprendeu sobre um fornecedor.

| Ferramenta                                                    | Descrição                                                                                                                                           |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `list_tables` / `get_table_config`                            | Tabelas e colunas de um tipo de documento, com os indicadores Required / Read Only / Hidden / Use AI                                                |
| `create_table`                                                | Adiciona uma segunda tabela de itens a um tipo de documento                                                                                         |
| `add_table_column` / `delete_table_column`                    | Adiciona ou exclui logicamente (soft delete) uma coluna de tabela                                                                                   |
| `set_ai_table_config`                                         | Ativa a extração de tabelas por IA, a visão e o modo estruturado para a organização                                                                 |
| `extract_table_ai`                                            | Executa a extração de tabelas por IA em um documento (texto ou visão)                                                                               |
| `extract_table_only`                                          | Extrai a tabela sem tocar nos campos de cabeçalho (regras ou IA)                                                                                    |
| `extract_table_nonai`                                         | Extração baseada em regras a partir de coordenadas que você informa, o primeiro passo de um treinamento de tabela pela API                          |
| `apply_ai_table_formatting` / `apply_table_feedback`          | Reformata uma tabela de IA: oculta colunas, remapeia, aplica o feedback do usuário                                                                  |
| `remap_table_columns`                                         | Altera qual coluna extraída alimenta qual coluna configurada                                                                                        |
| `save_table_rules` / `save_table_training_rules`              | Armazena as regras de coordenadas ou as regras de formatação por IA para o fornecedor, de modo que o próximo documento seja extraído da mesma forma |
| `delete_table_training_rules`                                 | Remove as regras salvas de um fornecedor; o próximo documento volta a usar a IA                                                                     |
| `get_table_extraction_report` / `list_table_report_suppliers` | Relatório por fornecedor de como as tabelas são extraídas (regras, IA, modelo), com pré-visualização                                                |
| `compare_table_extraction_models`                             | Extrai o mesmo documento com dois níveis de IA e compara as tabelas                                                                                 |

### Busca e Dashboard

| Ferramenta                                        | Descrição                                                                                                 |
| ------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `search_documents` / `search_documents_by_name`   | Busca em texto completo e por nome de arquivo                                                             |
| `query_document_dashboard`                        | Consulta do dashboard em linguagem natural                                                                |
| `explain_document_dashboard_query`                | Mostra como uma consulta foi interpretada                                                                 |
| `get_search_capabilities`                         | Quais recursos de busca a organização habilitou                                                           |
| `compare_search_modes`                            | Compara os resultados por palavra-chave e vetoriais                                                       |
| `diagnose_document_search`                        | Por que um documento aparece ou não em uma determinada busca, clássica vs. texto completo, lado a lado    |
| `inspect_document_search_index`                   | Se um documento está presente nos índices de documento, de texto e vetorial, e quando cada um foi gravado |
| `get_dashboard_columns` / `set_dashboard_columns` | Lê ou altera as colunas exibidas no dashboard de documentos                                               |

### Touchless Intelligence

Por que os documentos precisam de intervenção humana e o que mudar para que menos documentos precisem. Todas as ferramentas aqui são somente leitura, exceto `touchless_apply_change`, que grava exatamente uma alteração de configuração previamente pré-visualizada.

| Ferramenta                                                       | Descrição                                                                                              |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `touchless_get_summary`                                          | Painel touchless da organização: quantos documentos passaram sem intervenção, por período e segmento   |
| `touchless_list_segments`                                        | Valores pelos quais você pode segmentar os números (fornecedor, tipo de documento, …)                  |
| `touchless_rank_supplier_opportunities`                          | Fornecedores classificados pela quantidade de trabalho manual que causam                               |
| `touchless_diagnose_supplier`                                    | Por que os documentos de um fornecedor param para um humano                                            |
| `touchless_get_issue_cluster`                                    | Um problema recorrente e os documentos que ele afetou                                                  |
| `touchless_get_document_trace`                                   | Histórico touchless completo de um documento                                                           |
| `touchless_explain_pipeline`                                     | Em que ponto do pipeline um documento ou um cluster parou                                              |
| `touchless_explain_po_match` / `touchless_get_po_match_evidence` | Por que o PO Matching foi bem-sucedido ou falhou, com o conjunto de regras e o cálculo das tolerâncias |
| `touchless_get_recommendations`                                  | O que mudar, e não apenas o que deu errado                                                             |
| `touchless_list_change_proposals`                                | Alterações de configuração que aumentariam a taxa touchless, com o ganho esperado                      |
| `touchless_preview_change`                                       | Simulação de uma proposta: nada é gravado                                                              |
| `touchless_apply_change`                                         | Aplica à organização uma proposta previamente pré-visualizada                                          |
| `touchless_verify_change`                                        | Quanto uma alteração aplicada acabou valendo                                                           |

### Análises e BI

| Ferramenta                 | Descrição                              |
| -------------------------- | -------------------------------------- |
| `get_executive_summary`    | KPIs de alto nível da organização      |
| `get_success_rates`        | Taxas touchless / straight-through     |
| `get_volume_trends`        | Volume de documentos ao longo do tempo |
| `get_top_document_types`   | Tipos de documento mais frequentes     |
| `get_pending_tasks_detail` | Detalhes do trabalho pendente          |

### Documentos Eletrônicos (faturas eletrônicas)

| Ferramenta                                                     | Descrição                                                                       |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `list_electronic_document_types`                               | Formatos de fatura eletrônica suportados (ZUGFeRD, XRechnung, Factur-X, UBL, …) |
| `test_electronic_document`                                     | Classifica e extrai um documento eletrônico de exemplo                          |
| `verify_electronic_documents` / `validate_all_edocs`           | Verifica a extração de documentos eletrônicos                                   |
| `list_edoc_custom_attributes` / `create_edoc_custom_attribute` | Gerencia atributos de extração personalizados                                   |

### Dados Mestres

| Ferramenta                                                | Descrição                                                                                 |
| --------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `upsert_vendor_master_data`                               | Cria ou atualiza dados mestres de fornecedores                                            |
| `trigger_supplier_lookup`                                 | Enriquece um documento com os dados mestres do fornecedor                                 |
| `import_supplier_invoice_bod`                             | Importa um BOD de fatura de fornecedor                                                    |
| `get_supplier_invoice`                                    | Lê os dados persistidos da fatura de fornecedor (BOD) por fatura, fornecedor ou documento |
| `upsert_payment_term_mapping` / `upsert_discount_mapping` | Mantém os mapeamentos de cálculo                                                          |

### Configuração, Administração e Saúde

| Ferramenta                                              | Descrição                                                     |
| ------------------------------------------------------- | ------------------------------------------------------------- |
| `get_preferences` / `get_preference` / `set_preference` | Lê e altera as preferências da organização                    |
| `list_document_types` / `get_field_settings`            | Inspeciona a configuração dos tipos de documento e dos campos |
| `list_users`                                            | Lista os usuários da organização                              |
| `clear_org_cache`                                       | Limpa a configuração em cache                                 |
| `check_api_health` / `check_celery_health`              | Saúde dos serviços                                            |
| `get_current_user` / `get_api_info`                     | Identidade e metadados da API                                 |

## Próximos passos

* [**Configuração e Instalação**](setup-and-configuration.md) — conecte o Claude Code, o Gemini CLI ou o Codex (com login ou chave de API)
* [**Exemplos**](examples.md) — coisas reais que os clientes pedem ao assistente
* [**Documentos Eletrônicos (eDocs)**](edocs-mcp/) — aprofundamento nas ferramentas de eDoc: inspecionar/testar o processamento de faturas eletrônicas e gerenciar regras personalizadas de extração/pré-visualização (mesmo endpoint, mesmo login)
* [**Workflows e Cards (DocFlow)**](docflow-mcp/) — gerencie workflows avançados e cards de parceiros

{% hint style="info" %}
**Um único MCP para tudo.** As ferramentas de eDoc e as ferramentas de **Workflows e Cards (DocFlow)** são executadas no **mesmo** endpoint `api.docbits.com/v3/mcp`, com o mesmo login do DocBits. As ferramentas do DocFlow aparecem ali com o prefixo `docflow_` (por exemplo `docflow_list_workflows`); a página do DocFlow as documenta pelos nomes simples. Conectar-se diretamente ao host do DocFlow continua possível, mas não é mais necessário.
{% endhint %}
