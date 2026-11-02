# Tipo de documento

## Colunas

* `id`: interno
* `org_id`: ID da organização
* `document_key`: interno
* `document_name`: interno
* `title`: interno
* `translation_key`: interno
* `extraction_type`: interno
* `document_type_category`: interno
* `has_table`: booleano
* `sort_order`: inteiro
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano

## Análise e descrição

```markdown
# Tabela: public.document_type

## Introdução
A tabela `public.document_type` foi projetada para armazenar informações relacionadas aos diversos tipos de documentos dentro de uma organização. Ela inclui identificadores e metadados para a categorização, o gerenciamento e o processamento de documentos, como chaves de documento, nomes, títulos, chaves de tradução e outros atributos que facilitam o tratamento e a recuperação de documentos. A tabela também acompanha a criação e a modificação dessas entradas, oferecendo suporte aos estados ativo e excluído.

## Descrição das colunas

### id
- **Significado**: um identificador único para cada entrada de tipo de documento.
- **Função**: chave primária.
- **Conteúdo típico**: uma string UUID que identifica uma entrada de tipo de documento de forma única.

### org_id
- **Significado**: identificador da organização à qual o tipo de documento pertence.
- **Função**: chave estrangeira.
- **Conteúdo típico**: uma string UUID que faz referência a uma organização.

### document_key
- **Significado**: uma chave única para identificar o tipo de documento, potencialmente usada em sistemas de armazenamento ou processamento de documentos.
- **Função**: identificador.
- **Conteúdo típico**: uma string que combina informações do tipo de documento com o ID da organização.

### document_name
- **Significado**: o nome interno do tipo de documento.
- **Função**: campo descritivo.
- **Conteúdo típico**: uma string em maiúsculas que representa o nome do tipo de documento.

### title
- **Significado**: o título de exibição do tipo de documento nas interfaces de usuário.
- **Função**: campo descritivo.
- **Conteúdo típico**: uma string com capitalização de título, legível e descritiva do tipo de documento.

### translation_key
- **Significado**: uma chave usada para localizar o título ou o nome do documento em diferentes idiomas.
- **Função**: suporte à internacionalização.
- **Conteúdo típico**: uma string em minúsculas que serve de referência para os sistemas de tradução.

### extraction_type
- **Significado**: indica o método ou o processo pelo qual os dados são extraídos do documento.
- **Função**: campo de metadados.
- **Conteúdo típico**: atualmente não preenchido nos dados de exemplo.

### document_type_category
- **Significado**: categoriza o tipo de documento em categorias ou classificações mais amplas.
- **Função**: campo de categorização.
- **Conteúdo típico**: atualmente não preenchido nos dados de exemplo.

### has_table
- **Significado**: indica se o tipo de documento envolve dados tabulares.
- **Função**: campo de metadados.
- **Conteúdo típico**: valor booleano (`True` ou `False`) que indica a presença de dados tabulares.

### sort_order
- **Significado**: define a ordem em que os tipos de documento são classificados ou exibidos.
- **Função**: campo de ordenação.
- **Conteúdo típico**: um inteiro que representa a sequência de ordenação.

### created_by
- **Significado**: identificador do usuário que criou a entrada do tipo de documento.
- **Função**: campo de metadados.
- **Conteúdo típico**: um inteiro que faz referência a um ID de usuário.

### created_on
- **Significado**: timestamp que indica quando a entrada do tipo de documento foi criada.
- **Função**: campo de auditoria.
- **Conteúdo típico**: data e hora com informações de fuso horário.

### last_modified_on
- **Significado**: timestamp que indica a data da última modificação da entrada do tipo de documento.
- **Função**: campo de auditoria.
- **Conteúdo típico**: data e hora com informações de fuso horário, `None` se nunca foi modificado.

### is_deleted
- **Significado**: indica se a entrada do tipo de documento está marcada como excluída.
- **Função**: campo de status.
- **Conteúdo típico**: valor booleano (`True` ou `False`) que indica o status de exclusão.
```
