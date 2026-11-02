# Documentos

## Colunas

* `id`: interno
* `org_id`: ID da organização
* `batch_id`: interno
* `doc_path`: interno
* `doc_type`: tipo de documento
* `status`: interno
* `message`: texto
* `export_attempts`: inteiro
* `last_attempted_on`: timestamp com fuso horário
* `next_attempt_on`: timestamp com fuso horário
* `assigned_to`: inteiro
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `task_id`: interno
* `filename`: interno
* `assigned_on`: timestamp com fuso horário
* `pages`: inteiro
* `auto_processed`: booleano
* `exception_info`: texto
* `doc_language`: idioma
* `is_trimmed`: booleano
* `doc_origin`: origem do documento
* `doc_locale`: localidade do documento
* `is_doc2landing_doc`: booleano
* `extraction_time`: precisão dupla
* `export_time`: precisão dupla
* `po_all_matched`: booleano
* `restart_allowed`: booleano
* `table_version`: interno
* `force_ocr`: booleano
* `locked_by`: inteiro
* `locked_on`: timestamp com fuso horário
* `lock_renewed_on`: timestamp com fuso horário
* `lock_key`: interno
* `last_saved_by`: inteiro
* `last_saved_on`: timestamp com fuso horário
* `document_version`: inteiro
* `lock_session_key`: interno
* `sub_org_id`: interno
* `doc_source`: interno
* `sub_doc_type`: interno
* `assigned_to_group`: interno
* `status_changed_on`: timestamp com fuso horário
* `improve_quality`: booleano
* `priority`: inteiro
* `metadata_field`: json
* `doc_classification_label`: interno
* `doc_start_page`: inteiro
* `doc_classification_class`: interno
* `celery_task_token`: interno
* `celery_task_attempt`: inteiro
* `celery_task_priority`: inteiro
* `has_zugferd`: booleano
* `has_peppol`: booleano
* `timestamp_for_validation`: timestamp com fuso horário
* `exception_details`: texto
* `has_annotated_version`: booleano
* `po_match_status`: interno
* `tr_ocr_extracted_data`: texto
* `pending_workflow_execution`: booleano
* `extracted_document_id`: interno
* `extracted_supplier_id`: interno
* `classification_manually_corrected`: booleano
* `supplier_as_org_id`: interno
* `extracted_data_basic`: jsonb
* `celery_task_queue`: interno
* `extracted_data`: jsonb
* `extracted_data_jsonb`: jsonb
* `warnings`: jsonb

## Análise e descrição

```markdown
# Documentação técnica da tabela `public.documents`

## Introdução

A tabela `public.documents` foi projetada para armazenar e gerenciar metadados e informações de processamento relacionados ao tratamento de documentos dentro de uma organização. Isso inclui o acompanhamento do status do documento, das tentativas de processamento, do idioma e de outros detalhes administrativos. A tabela é estruturada para oferecer suporte à classificação de documentos, ao fluxo de processamento e às atribuições de usuários, sendo parte integrante do sistema de gerenciamento de documentos.

## Descrição das colunas

### id
- **Significado**: identificador único de cada documento.
- **Função**: chave primária.
- **Conteúdo típico**: uma string UUID que representa o documento.

### org_id
- **Significado**: identificador da organização associada ao documento.
- **Função**: chave estrangeira.
- **Conteúdo típico**: uma string UUID que representa a organização.

### batch_id
- **Significado**: identificador do lote em que o documento foi processado.
- **Função**: chave estrangeira.
- **Conteúdo típico**: uma string UUID que representa o lote.

### doc_path
- **Significado**: caminho do arquivo em que o documento está armazenado.
- **Função**: campo técnico.
- **Conteúdo típico**: caminho para o arquivo do documento, por exemplo, `documents/{id}/{id}.pdf`.

### doc_type
- **Significado**: tipo de documento armazenado (por exemplo, fatura).
- **Função**: classificação do documento.
- **Conteúdo típico**: uma string como `INVOICE`.

### status
- **Significado**: status atual de processamento do documento.
- **Função**: indicador de fluxo de trabalho.
- **Conteúdo típico**: uma string que indica o status, por exemplo, `ready_for_validation`.

### message
- **Significado**: informações sobre o estado de processamento do documento ou sobre erros.
- **Função**: campo descritivo.
- **Conteúdo típico**: texto que descreve erros ou mensagens relacionados ao processamento do documento.

### export_attempts
- **Significado**: número de vezes que foi feita uma tentativa de exportação do documento.
- **Função**: acompanhamento do processamento.
- **Conteúdo típico**: contagem inteira de tentativas de exportação.

### last_attempted_on
- **Significado**: timestamp da última tentativa de processar ou exportar o documento.
- **Função**: campo de timestamp.
- **Conteúdo típico**: data e hora com fuso horário.

### next_attempt_on
- **Significado**: timestamp agendado para a próxima tentativa de processar ou exportar o documento.
- **Função**: campo de agendamento.
- **Conteúdo típico**: data e hora com fuso horário.

### assigned_to
- **Significado**: identificador do usuário atribuído a este documento.
- **Função**: chave estrangeira.
- **Conteúdo típico**: inteiro que representa o ID do usuário.

### created_by
- **Significado**: identificador do usuário que criou ou enviou o documento.
- **Função**: chave estrangeira.
- **Conteúdo típico**: inteiro que representa o ID do usuário.

### created_on
- **Significado**: timestamp de quando o documento foi criado ou enviado.
- **Função**: campo de timestamp.
- **Conteúdo típico**: data e hora com fuso horário.

### last_modified_on
- **Significado**: timestamp da última modificação feita no registro do documento.
- **Função**: campo de timestamp.
- **Conteúdo típico**: data e hora com fuso horário.

### is_deleted
- **Significado**: indica se o documento está marcado como excluído.
- **Função**: indicador de exclusão lógica.
- **Conteúdo típico**: valor booleano (True ou False).

### task_id
- **Significado**: identificador da tarefa associada ao processamento do documento.
- **Função**: chave estrangeira.
- **Conteúdo típico**: uma string UUID que representa a tarefa.

### filename
- **Significado**: nome original do arquivo do documento.
- **Função**: campo descritivo.
- **Conteúdo típico**: nome do arquivo, por exemplo, `document.pdf`.

### assigned_on
- **Significado**: timestamp de quando o documento foi atribuído a um usuário.
- **Função**: campo de timestamp.
- **Conteúdo típico**: data e hora com fuso horário.

### pages
- **Significado**: número de páginas do documento.
- **Função**: campo descritivo.
- **Conteúdo típico**: inteiro que indica a contagem de páginas.

### auto_processed
- **Significado**: indica se o documento foi processado automaticamente.
- **Função**: indicador de status de processamento.
- **Conteúdo típico**: valor booleano (True ou False).

### exception_info
- **Significado**: informações sobre quaisquer exceções encontradas durante o processamento.
- **Função**: campo descritivo.
- **Conteúdo típico**: texto que descreve as exceções de processamento.

### doc_language
- **Significado**: idioma do conteúdo do documento.
- **Função**: classificação de idioma.
- **Conteúdo típico**: código de idioma ISO, por exemplo, `en`, `de`.

### is_trimmed
- **Significado**: indica se o documento foi aparado ou recortado.
- **Função**: indicador de modificação do documento.
- **Conteúdo típico**: valor booleano (True ou False).

### doc_origin
- **Significado**: origem do documento, possivelmente indicando o país ou o sistema de origem.
- **Função**: campo descritivo.
- **Conteúdo típico**: código de país ou identificador de origem, por exemplo, `DE`.

### doc_locale
- **Significado**: configurações de localidade do documento, que indicam idioma e região.
- **Função**: classificação de localidade.
- **Conteúdo típico**: string de localidade, por exemplo, `de_DE.ISO8859-1`.

### is_doc2landing_doc
- **Significado**: indica se o documento está relacionado a um fluxo de processamento específico (Doc2Landing).
- **Função**: indicador de fluxo de trabalho.
- **Conteúdo típico**: valor booleano (True ou False).

### extraction_time
- **Significado**: tempo necessário para extrair os dados do documento.
- **Função**: métrica de desempenho.
- **Conteúdo típico**: valor de precisão dupla que representa o tempo de extração.

### export_time
- **Significado**: tempo necessário para exportar o documento.
- **Função**: métrica de desempenho.
- **Conteúdo típico**: valor de precisão dupla que representa o tempo de exportação.

### po_all_matched
- **Significado**: indica se todos os pedidos de compra relacionados ao documento foram correspondidos.
- **Função**: indicador de status de correspondência.
- **Conteúdo típico**: valor booleano (True ou False).

### restart_allowed
- **Significado**: indica se o processamento do documento pode ser reiniciado.
- **Função**: indicador de controle do fluxo de trabalho.
- **Conteúdo típico**: valor booleano (True ou False).

### table_version
- **Significado**: versão da estrutura de tabela usada para o documento.
- **Função**: controle de versão.
- **Conteúdo típico**: string que indica a versão, por exemplo, `v3`.

### force_ocr
- **Significado**: indica se o processamento por OCR é forçado para o documento.
- **Função**: indicador de controle de processamento.
- **Conteúdo típico**: valor booleano (True ou False).

### locked_by
- **Significado**: identificador do usuário que bloqueou o documento para edição.
- **Função**: chave estrangeira.
- **Conteúdo típico**: inteiro que representa o ID do usuário.

### locked_on
- **Significado**: timestamp de quando o documento foi bloqueado para edição.
- **Função**: campo de timestamp.
- **Conteúdo típico**: data e hora com fuso horário.

### lock_renewed_on
- **Significado**: timestamp de quando o bloqueio do documento foi renovado pela última vez.
- **Função**: campo de timestamp.
- **Conteúdo típico**: data e hora com fuso horário.

### lock_key
- **Significado**: chave associada ao bloqueio do documento.
- **Função**: controle de bloqueio.
- **Conteúdo típico**: string que representa a chave de bloqueio.

### last_saved_by
- **Significado**: identificador do usuário que salvou o documento pela última vez.
- **Função**: chave estrangeira.
- **Conteúdo típico**: inteiro que representa o ID do usuário.

### last_saved_on
- **Significado**: timestamp de quando o documento foi salvo pela última vez.
- **Função**: campo de timestamp.
- **Conteúdo típico**: data e hora com fuso horário.

### document_version
- **Significado**: número da versão do documento.
- **Função**: acompanhamento de versão.
- **Conteúdo típico**: inteiro que representa a versão do documento.

### lock_session_key
- **Significado**: chave de sessão associada ao bloqueio do documento.
- **Função**: controle de bloqueio.
- **Conteúdo típico**: string que representa a chave de sessão.

### sub_org_id
- **Significado**: identificador de uma suborganização associada ao documento.
- **Função**: chave estrangeira.
- **Conteúdo típico**: uma string UUID que representa a suborganização.

### doc_source
- **Significado**: sistema de origem ou procedência do documento.
- **Função**: campo descritivo.
- **Conteúdo típico**: string que indica a origem, por exemplo, `doc2app`.

### sub_doc_type
- **Significado**: classificação do subtipo do documento.
- **Função**: classificação do documento.
- **Conteúdo típico**: string que indica o subtipo.

### assigned_to_group
- **Significado**: identificador do grupo ao qual o documento está atribuído.
- **Função**: acompanhamento de atribuição.
- **Conteúdo típico**: uma string UUID que representa o grupo.

### status_changed_on
- **Significado**: timestamp de quando o status do documento foi alterado pela última vez.
- **Função**: campo de timestamp.
- **Conteúdo típico**: data e hora com fuso horário.

### improve_quality
- **Significado**: indica se processos de melhoria de qualidade são aplicados ao documento.
- **Função**: indicador de controle de qualidade.
- **Conteúdo típico**: valor booleano (True ou False).

### priority
- **Significado**: prioridade de processamento do documento.
- **Função**: controle do fluxo de trabalho.
- **Conteúdo típico**: inteiro que indica o nível de prioridade.

### metadata_field
- **Significado**: campo JSON com metadados relacionados ao documento.
- **Função**: armazenamento de metadados.
- **Conteúdo típico**: estrutura JSON com diversos campos de metadados.

### doc_classification_label
- **Significado**: rótulo que indica a classificação do documento.
- **Função**: rótulo de classificação.
- **Conteúdo típico**: string que indica a classificação, por exemplo, `INVOICE`.

### doc_start_page
- **Significado**: número da página em que o conteúdo do documento começa.
- **Função**: campo descritivo.
- **Conteúdo típico**: inteiro que indica a página inicial.

### doc_classification_class
- **Significado**: classe que indica a classificação detalhada do documento.
- **Função**: detalhe da classificação.
- **Conteúdo típico**: string que indica a classe de classificação.

### celery_task_token
- **Significado**: token para acompanhar a tarefa do Celery associada ao documento.
- **Função**: acompanhamento de tarefas.
- **Conteúdo típico**: string que representa o token da tarefa.

### celery_task_attempt
- **Significado**: número de tentativas feitas para a tarefa do Celery.
- **Função**: acompanhamento de tarefas.
- **Conteúdo típico**: contagem inteira de tentativas da tarefa.

### celery_task_priority
- **Significado**: nível de prioridade da tarefa do Celery.
- **Função**: controle de tarefas.
- **Conteúdo típico**: inteiro que indica a prioridade da tarefa.

### has_zugferd
- **Significado**: indica se o documento está no formato ZUGFeRD.
- **Função**: indicador de formato.
- **Conteúdo típico**: valor booleano (True ou False).

### has_peppol
- **Significado**: indica se o documento está no formato PEPPOL.
- **Função**: indicador de formato.
- **Conteúdo típico**: valor booleano (True ou False).

### timestamp_for_validation
- **Significado**: timestamp de quando o documento foi validado.
- **Função**: acompanhamento da validação.
- **Conteúdo típico**: data e hora com fuso horário.

### exception_details
- **Significado**: informações detalhadas sobre exceções durante o processamento.
- **Função**: campo descritivo.
- **Conteúdo típico**: texto com os detalhes da exceção.

### has_annotated_version
- **Significado**: indica se existe uma versão anotada do documento.
- **Função**: indicador de versão.
- **Conteúdo típico**: valor booleano (True ou False).

### po_match_status
- **Significado**: status da correspondência de pedidos de compra.
- **Função**: indicador de status de correspondência.
- **Conteúdo típico**: string que indica o status da correspondência.

### tr_ocr_extracted_data
- **Significado**: dados extraídos do documento por OCR.
- **Função**: armazenamento de dados.
- **Conteúdo típico**: texto com os dados extraídos.

### pending_workflow_execution
- **Significado**: indica se há execuções de fluxo de trabalho pendentes.
- **Função**: indicador de status do fluxo de trabalho.
- **Conteúdo típico**: valor booleano (True ou False).

### extracted_document_id
- **Significado**: identificador do documento extraído.
- **Função**: acompanhamento da extração.
- **Conteúdo típico**: uma string UUID que representa o documento extraído.

### extracted_supplier_id
- **Significado**: identificador do fornecedor extraído.
- **Função**: acompanhamento da extração.
- **Conteúdo típico**: uma string UUID que representa o fornecedor extraído.

### classification_manually_corrected
- **Significado**: indica se a classificação do documento foi corrigida manualmente.
- **Função**: indicador de status da classificação.
- **Conteúdo típico**: valor booleano (True ou False).

### supplier_as_org_id
- **Significado**: identificador do fornecedor tratado como organização.
- **Função**: chave estrangeira.
- **Conteúdo típico**: uma string UUID que representa a organização do fornecedor.

### extracted_data_basic
- **Significado**: dados básicos extraídos no formato JSONB.
- **Função**: armazenamento de dados.
- **Conteúdo típico**: estrutura JSONB com os campos de dados extraídos.

### celery_task_queue
- **Significado**: nome da fila de tarefas do Celery.
- **Função**: gerenciamento de tarefas.
- **Conteúdo típico**: string que indica o nome da fila.

### extracted_data
- **Significado**: dados extraídos do documento no formato JSONB.
- **Função**: armazenamento de dados.
- **Conteúdo típico**: estrutura JSONB com os campos de dados extraídos.

### extracted_data_jsonb
- **Significado**: campo JSONB com os dados extraídos detalhados.
- **Função**: armazenamento de dados.
- **Conteúdo típico**: estrutura JSONB com os campos de dados extraídos.

### warnings
- **Significado**: avisos relacionados ao processamento do documento, armazenados no formato JSONB.
- **Função**: armazenamento de avisos.
- **Conteúdo típico**: estrutura JSONB com mensagens de aviso.
```
