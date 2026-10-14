# Dados de treinamento

## Tabela `public.training_data`

### Colunas

* `id`: interno
* `org_id`: ID da organização
* `doc_type`: tipo de documento
* `doc_origin`: origem do documento
* `doc_locale`: localidade do documento
* `doc_language`: idioma
* `first_page_content`: texto
* `supplier_name`: nome do fornecedor
* `supplier_vat`: interno
* `doc_created_on`: timestamp with time zone
* `is_training_sample`: boolean
* `sample_doc_id`: interno
* `sample_file_name`: interno
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `is_table_training_sample`: boolean

### Análise e descrição

## Documentação técnica da tabela `public.training_data`

### Introdução

A tabela `public.training_data` foi projetada para armazenar diversos dados relacionados a documentos, provavelmente usados para treinar modelos ou sistemas que processam e analisam o conteúdo de documentos. A tabela contém informações sobre o tipo de documento, a origem, o idioma, os dados do fornecedor e os carimbos de data e hora de criação e modificação dos registros, entre outros atributos. Ela parece ter foco especial em faturas e recibos médicos, o que sugere seu uso em aplicações de processamento de dados financeiros ou de saúde.

### Descrição das colunas

#### id

* **Significado**: identificador único de cada registro da tabela.
* **Função**: chave primária.
* **Conteúdo típico**: um identificador único universal (UUID) em formato de caracteres.
* **Observação**: essencial para identificar cada entrada de forma única.

#### org\_id

* **Significado**: identificador da organização associada ao documento.
* **Função**: chave estrangeira que se vincula a um registro de organização.
* **Conteúdo típico**: UUID que representa uma organização.
* **Observação**: ajuda a associar documentos a organizações específicas.

#### doc\_type

* **Significado**: tipo de documento armazenado no registro.
* **Função**: campo descritivo.
* **Conteúdo típico**: valores como 'INVOICE' ou 'MEDICAL\_RECEIPT'.
* **Observação**: útil para categorizar os documentos.

#### doc\_origin

* **Significado**: origem ou código do país de origem do documento.
* **Função**: campo descritivo.
* **Conteúdo típico**: código de país, como 'DE' para a Alemanha.
* **Observação**: indica a origem geográfica do documento.

#### doc\_locale

* **Significado**: informações de localidade do documento.
* **Função**: campo descritivo.
* **Conteúdo típico**: código de localidade, como 'en\_DE'.
* **Observação**: combina idioma e região para fins de localização.

#### doc\_language

* **Significado**: idioma em que o documento está escrito.
* **Função**: campo descritivo.
* **Conteúdo típico**: código de idioma, como 'en' ou 'de'.
* **Observação**: indica o idioma principal usado no documento.

#### first\_page\_content

* **Significado**: conteúdo da primeira página do documento.
* **Função**: campo descritivo.
* **Conteúdo típico**: dados de texto com o conteúdo da primeira página do documento.
* **Observação**: pode ser usado para análise ou processamento de texto.

#### supplier\_name

* **Significado**: nome do fornecedor associado ao documento.
* **Função**: campo descritivo.
* **Conteúdo típico**: nome do fornecedor em formato de texto.
* **Observação**: importante para identificar a origem ou o emissor do documento.

#### supplier\_vat

* **Significado**: número de identificação de IVA do fornecedor.
* **Função**: campo descritivo.
* **Conteúdo típico**: ID de IVA, por exemplo 'DE 129375678'.
* **Observação**: útil para processos fiscais e tributários.

#### doc\_created\_on

* **Significado**: carimbo de data e hora da criação do documento.
* **Função**: campo descritivo.
* **Conteúdo típico**: data e hora em formato UTC.
* **Observação**: fornece o contexto temporal da criação do documento.

#### is\_training\_sample

* **Significado**: indica se o registro é usado como amostra de treinamento.
* **Função**: campo técnico.
* **Conteúdo típico**: valor booleano (`True` ou `False`).
* **Observação**: identifica os registros marcados especificamente para fins de treinamento.

#### sample\_doc\_id

* **Significado**: identificador do documento de amostra.
* **Função**: campo descritivo ou possível chave estrangeira.
* **Conteúdo típico**: UUID que se vincula a outro documento.
* **Observação**: pode referenciar um documento relacionado ou original usado como amostra.

#### sample\_file\_name

* **Significado**: nome do arquivo associado à amostra do documento.
* **Função**: campo descritivo.
* **Conteúdo típico**: nome de arquivo em formato de texto.
* **Observação**: útil para processos de gerenciamento ou recuperação de arquivos.

#### created\_on

* **Significado**: carimbo de data e hora da criação do registro.
* **Função**: campo técnico.
* **Conteúdo típico**: data e hora em formato UTC.
* **Observação**: indica quando o registro foi adicionado ao banco de dados.

#### last\_modified\_on

* **Significado**: carimbo de data e hora da última modificação do registro.
* **Função**: campo técnico.
* **Conteúdo típico**: data e hora em formato UTC.
* **Observação**: registra quando o registro foi atualizado pela última vez.

#### is\_deleted

* **Significado**: indica se o registro foi marcado como excluído.
* **Função**: campo técnico.
* **Conteúdo típico**: valor booleano (`True` ou `False`).
* **Observação**: oferece suporte à funcionalidade de exclusão lógica (soft delete).

#### is\_table\_training\_sample

* **Significado**: indica se o registro é uma amostra de treinamento específica para tabelas.
* **Função**: campo técnico.
* **Conteúdo típico**: valor booleano (`True` ou `False`).
* **Observação**: diferencia-se das amostras de treinamento gerais, pois se concentra em dados de tabelas.
