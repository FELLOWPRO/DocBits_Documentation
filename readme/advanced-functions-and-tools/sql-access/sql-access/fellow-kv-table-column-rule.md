# Regra de coluna de tabela Fellow KV

## Tabela `public.fellow_kv_table_column_rule`

### Colunas

* `id`: interno
* `docType`: interno
* `tableName`: interno
* `dlfName`: interno
* `multi_line`: booleano
* `filterID1`: interno
* `filterID2`: interno
* `filterID3`: interno
* `tfidf_doc_id`: interno
* `tfidf_id`: interno
* `valuePattern`: interno
* `coordsY0`: inteiro
* `coordsY1`: inteiro
* `coordsX0`: inteiro
* `coordsX1`: inteiro
* `normalizedY0`: numérico
* `normalizedY1`: numérico
* `normalizedX0`: numérico
* `normalizedX1`: numérico
* `width`: inteiro
* `height`: inteiro
* `patternLeft`: interno
* `patternRight`: interno
* `patternAbove`: interno
* `patternBelow`: interno
* `wordLeft`: interno
* `wordAbove`: interno
* `ruleWeight`: inteiro
* `user_id`: inteiro
* `org_id`: ID da organização
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `is_new`: booleano

### Análise e descrição

## Documentação técnica de `public.fellow_kv_table_column_rule`

### Introdução

A tabela `public.fellow_kv_table_column_rule` parece ter sido projetada para armazenar regras e padrões para o processamento ou a extração de dados de documentos. Isso se deduz da presença de campos como `docType`, `tableName`, `dlfName` e de vários campos de padrões e coordenadas. A tabela parece facilitar a aplicação de regras a diferentes tipos de documentos, permitindo o reconhecimento de padrões e a extração de dados de documentos estruturados, como faturas ou contratos.

### Descrição das colunas

#### id

* **Significado**: identificador único de cada regra.
* **Função**: chave primária.
* **Conteúdo típico**: strings UUID.
* **Observação**: essencial para identificar cada linha de forma única.

#### docType

* **Significado**: tipo de documento ao qual a regra se aplica.
* **Função**: campo descritivo.
* **Conteúdo típico**: tipos de documento como 'INVOICE' e 'CONTRACT'.
* **Observação**: ajuda a categorizar as regras por tipo de documento.

#### tableName

* **Significado**: nome da tabela na qual a regra é aplicada.
* **Função**: campo descritivo.
* **Conteúdo típico**: nomes de tabelas como 'INVOICE\_TABLE'.
* **Observação**: indica o contexto em que a regra é aplicada.

#### dlfName

* **Significado**: nome de um campo ou coluna específico no documento.
* **Função**: campo descritivo.
* **Conteúdo típico**: nomes de campos como 'COUNTRY\_ORIGIN'.
* **Observação**: especifica o campo de destino para a extração de dados.

#### multi\_line

* **Significado**: indica se a regra se aplica a texto de várias linhas.
* **Função**: indicador booleano.
* **Conteúdo típico**: `True` ou `False`.
* **Observação**: útil para o tratamento de campos de texto de várias linhas.

#### filterID1, filterID2, filterID3

* **Significado**: filtros ou condições para a aplicação da regra.
* **Função**: campos descritivos ou condicionais.
* **Conteúdo típico**: possivelmente strings que representam condições de filtro.
* **Observação**: usados para refinar a aplicação da regra com base em determinadas condições.

#### tfidf\_doc\_id, tfidf\_id

* **Significado**: identificadores relacionados ao processamento TF-IDF.
* **Função**: funções semelhantes a chave estrangeira ou identificadores.
* **Conteúdo típico**: strings UUID.
* **Observação**: provavelmente relacionados à análise de texto e à extração de características.

#### valuePattern

* **Significado**: padrão de expressão regular para a extração de valores.
* **Função**: campo de padrão.
* **Conteúdo típico**: expressões regulares.
* **Observação**: define o padrão usado para identificar e extrair valores.

#### coordsY0, coordsY1, coordsX0, coordsX1

* **Significado**: coordenadas que definem a caixa delimitadora para a extração.
* **Função**: campos de coordenadas.
* **Conteúdo típico**: números inteiros que representam posições em pixels.
* **Observação**: definem a área de interesse em um documento para a extração de dados.

#### normalizedY0, normalizedY1, normalizedX0, normalizedX1

* **Significado**: coordenadas normalizadas para a extração.
* **Função**: campos de coordenadas.
* **Conteúdo típico**: valores numéricos que representam posições proporcionais.
* **Observação**: usados para definir áreas independentes da resolução.

#### width, height

* **Significado**: dimensões da área definida pelas coordenadas.
* **Função**: campos de dimensão.
* **Conteúdo típico**: valores inteiros.
* **Observação**: ajudam a definir o tamanho da área de extração.

#### patternLeft, patternRight, patternAbove, patternBelow

* **Significado**: padrões contextuais ao redor dos dados de destino.
* **Função**: campos de padrão.
* **Conteúdo típico**: expressões regulares.
* **Observação**: fornecem contexto sobre onde os dados estão localizados em relação a outros textos.

#### wordLeft, wordAbove

* **Significado**: palavras específicas localizadas próximas aos dados de destino.
* **Função**: campos contextuais.
* **Conteúdo típico**: palavras ou frases específicas.
* **Observação**: ajudam a refinar a busca pelos dados de destino com base em palavras próximas.

#### ruleWeight

* **Significado**: importância ou prioridade da regra.
* **Função**: campo de peso ou prioridade.
* **Conteúdo típico**: valores inteiros.
* **Observação**: valores mais altos podem indicar maior prioridade ou importância.

#### user\_id

* **Significado**: identificador do usuário que criou ou modificou a regra.
* **Função**: chave estrangeira.
* **Conteúdo típico**: valores inteiros.
* **Observação**: vincula a regra a um usuário específico.

#### org\_id

* **Significado**: identificador da organização associada à regra.
* **Função**: chave estrangeira.
* **Conteúdo típico**: strings UUID.
* **Observação**: associa a regra a uma organização.

#### created\_on

* **Significado**: timestamp de quando a regra foi criada.
* **Função**: campo técnico.
* **Conteúdo típico**: timestamp com fuso horário.
* **Observação**: útil para acompanhar o histórico de criação da regra.

#### last\_modified\_on

* **Significado**: timestamp da última modificação da regra.
* **Função**: campo técnico.
* **Conteúdo típico**: timestamp com fuso horário ou `None`.
* **Observação**: registra as alterações da regra ao longo do tempo.

#### is\_deleted

* **Significado**: indica se a regra está marcada como excluída.
* **Função**: indicador booleano.
* **Conteúdo típico**: `True` ou `False`.
* **Observação**: usado para a exclusão lógica de regras.

#### is\_new

* **Significado**: indica se a regra foi criada recentemente.
* **Função**: indicador booleano.
* **Conteúdo típico**: `True` ou `False`.
* **Observação**: ajuda a identificar regras adicionadas recentemente.
