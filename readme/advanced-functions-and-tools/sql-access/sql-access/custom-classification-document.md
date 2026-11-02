# Documento de classificação personalizada

## Tabela `public.custom_classification_document`

### Colunas

* `id`: interno
* `org_id`: ID da organização
* `first_page_content`: texto
* `content`: texto
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano

### Análise e descrição

## Documentação técnica da tabela `public.custom_classification_document`

### Introdução

A tabela `public.custom_classification_document` foi projetada para armazenar informações detalhadas sobre classificações de documentos dentro de uma organização. Isso inclui metadados sobre o documento, como seu conteúdo, os detalhes de criação e o contexto organizacional. A estrutura da tabela sugere seu uso no gerenciamento de documentos relacionados a processos organizacionais, possivelmente envolvendo faturas ou formulários de pedido, conforme se deduz dos dados de exemplo.

### Descrição das colunas

#### id

* **Significado**: esta coluna provavelmente armazena um identificador único para cada entrada de documento.
* **Função**: chave primária
* **Conteúdo típico**: um UUID que representa um identificador único de documento.

#### org\_id

* **Significado**: esta coluna armazena o identificador da organização associada ao documento.
* **Função**: chave estrangeira
* **Conteúdo típico**: um UUID que vincula o documento a uma organização específica.

#### first\_page\_content

* **Significado**: esta coluna contém o conteúdo de texto da primeira página do documento.
* **Função**: campo de dados
* **Conteúdo típico**: representação textual do documento de uma organização, possivelmente incluindo cabeçalhos, endereços e os detalhes iniciais de uma fatura ou pedido.

#### content

* **Significado**: esta coluna armazena o conteúdo de texto completo do documento.
* **Função**: campo de dados
* **Conteúdo típico**: conteúdo textual completo do documento, incluindo todos os detalhes presentes na primeira página e nas páginas seguintes.

#### created\_by

* **Significado**: esta coluna indica o usuário que criou a entrada do documento.
* **Função**: campo de dados
* **Conteúdo típico**: um inteiro que representa o ID do usuário criador.

#### created\_on

* **Significado**: esta coluna registra a data e a hora em que a entrada do documento foi criada.
* **Função**: campo técnico
* **Conteúdo típico**: um timestamp com informações de fuso horário, que indica a data e a hora da criação.

#### last\_modified\_on

* **Significado**: esta coluna armazena a data e a hora da última modificação da entrada do documento.
* **Função**: campo técnico
* **Conteúdo típico**: um timestamp com informações de fuso horário, que indica a data e a hora da última modificação. Às vezes é `None`, se não ocorreram modificações após a criação.

#### is\_deleted

* **Significado**: esta coluna indica se a entrada do documento foi marcada como excluída.
* **Função**: campo técnico
* **Conteúdo típico**: um valor booleano (`True` ou `False`) que mostra o status de exclusão da entrada do documento.

Esta tabela oferece uma estrutura robusta para o gerenciamento de dados de documentos, garantindo que cada documento possa ser identificado de forma única, associado a uma organização e acompanhado ao longo de seu ciclo de vida de criação e modificação.
