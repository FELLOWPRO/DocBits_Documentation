# Documento de teste automático

## Colunas

* `id`: interno
* `org_id`: ID da organização
* `doc_id`: interno
* `doc_type`: tipo de documento
* `extracted_data`: texto
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `filename`: interno

## Análise e descrição

```markdown
# Documentação da tabela: `public.auto_test_document`

## Introdução

A tabela `public.auto_test_document` foi projetada para armazenar metadados e resultados de extração do processamento de documentos dentro de uma organização. A tabela registra informações sobre os documentos, seus tipos e os dados extraídos deles. Ela inclui campos para identificação do documento, metadados de processamento e indicadores de status, que são essenciais para gerenciar fluxos de trabalho de documentos e garantir a integridade dos dados.

## Descrição das colunas

### id
- **Significado**: identificador único de cada entrada de documento na tabela.
- **Função**: chave primária.
- **Conteúdo típico**: string UUID.
- **Observação**: serve como identificador único dos registros, garantindo que cada entrada seja distinta.

### org_id
- **Significado**: identificador da organização associada ao documento.
- **Função**: chave estrangeira.
- **Conteúdo típico**: string UUID.
- **Observação**: vincula o documento a uma organização específica dentro do sistema.

### doc_id
- **Significado**: identificador do documento que está sendo processado.
- **Função**: chave estrangeira.
- **Conteúdo típico**: string UUID.
- **Observação**: usado para associar os dados extraídos ao documento original.

### doc_type
- **Significado**: tipo ou categoria do documento.
- **Função**: campo descritivo.
- **Conteúdo típico**: string como "MEDI_ORDER".
- **Observação**: ajuda a categorizar os documentos para processamento e análise.

### extracted_data
- **Significado**: estrutura JSON com os dados detalhados extraídos do documento.
- **Função**: campo de dados.
- **Conteúdo típico**: texto JSON com campos, valores e metadados de extração.
- **Observação**: armazena os resultados do processo de extração de dados do documento.

### created_by
- **Significado**: identificador do usuário que criou o registro do documento.
- **Função**: campo descritivo.
- **Conteúdo típico**: inteiro que representa um ID de usuário.
- **Observação**: registra qual usuário iniciou a entrada do documento no sistema.

### created_on
- **Significado**: timestamp que indica quando o registro do documento foi criado.
- **Função**: campo técnico.
- **Conteúdo típico**: data e hora com informações de fuso horário.
- **Observação**: útil para auditoria e para acompanhar o ciclo de vida do documento.

### last_modified_on
- **Significado**: timestamp que indica a última modificação feita no registro do documento.
- **Função**: campo técnico.
- **Conteúdo típico**: data e hora com informações de fuso horário.
- **Observação**: ajuda a acompanhar alterações e atualizações do registro do documento.

### is_deleted
- **Significado**: indicador que informa se o registro do documento foi marcado como excluído.
- **Função**: campo de status.
- **Conteúdo típico**: valor booleano.
- **Observação**: facilita a exclusão lógica de registros, permitindo a recuperação, se necessário.

### filename
- **Significado**: nome do arquivo associado ao documento.
- **Função**: campo descritivo.
- **Conteúdo típico**: string, por exemplo, "7.pdf".
- **Observação**: fornece uma referência ao arquivo físico associado à entrada do documento.

```
