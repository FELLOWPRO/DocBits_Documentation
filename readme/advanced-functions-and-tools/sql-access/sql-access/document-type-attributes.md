# Atributos do tipo de documento

## Colunas

* `id`: interno
* `org_id`: ID da organização
* `doc_type_key`: interno
* `sub_doc_type_key`: interno
* `attribute_key`: interno
* `attribute_value`: texto
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `sub_org_id`: interno

## Análise e descrição

```markdown
# Documentação técnica da tabela `public.document_type_attributes`

## Introdução

A tabela `public.document_type_attributes` parece ter sido projetada para gerenciar atributos relacionados a diversos tipos de documentos em um contexto organizacional. Esta tabela provavelmente oferece suporte ao gerenciamento de configurações ou metadados de diferentes tipos de documentos, como faturas ou notas de entrega, associando atributos específicos a cada tipo de documento.

## Descrição das colunas

### id
- **Significado**: um identificador único para cada registro da tabela.
- **Função**: chave primária.
- **Conteúdo típico**: uma string UUID que identifica uma linha da tabela de forma única.

### org_id
- **Significado**: representa a organização à qual o atributo do tipo de documento pertence.
- **Função**: chave estrangeira.
- **Conteúdo típico**: uma string UUID que faz referência a uma organização.

### doc_type_key
- **Significado**: o tipo de documento ao qual o atributo se aplica (por exemplo, INVOICE, DELIVERY_NOTE).
- **Função**: campo descritivo.
- **Conteúdo típico**: uma string que representa um tipo de documento.

### sub_doc_type_key
- **Significado**: uma categorização mais específica dentro do tipo de documento, se aplicável.
- **Função**: campo descritivo.
- **Conteúdo típico**: normalmente `None`, o que indica que pode nem sempre ser usado.

### attribute_key
- **Significado**: a chave do atributo ou da propriedade específica relacionada ao tipo de documento.
- **Função**: campo descritivo.
- **Conteúdo típico**: uma string que representa uma chave de atributo, como `SECOND_APPROVAL_BEFORE_EXPORT`.

### attribute_value
- **Significado**: o valor associado à chave do atributo para o tipo de documento.
- **Função**: campo descritivo.
- **Conteúdo típico**: uma string ou um valor numérico que fornece o valor do atributo, por exemplo, `true`, `123`.

### created_by
- **Significado**: o identificador do usuário que criou o registro.
- **Função**: campo descritivo.
- **Conteúdo típico**: um inteiro que representa um ID de usuário.

### created_on
- **Significado**: o timestamp de quando o registro foi criado.
- **Função**: campo técnico.
- **Conteúdo típico**: um timestamp com fuso horário que indica quando o registro foi criado.

### last_modified_on
- **Significado**: o timestamp da última modificação feita no registro.
- **Função**: campo técnico.
- **Conteúdo típico**: um timestamp com fuso horário que indica o momento da última atualização.

### is_deleted
- **Significado**: indica se o registro está marcado como excluído.
- **Função**: campo técnico.
- **Conteúdo típico**: um valor booleano, em que `false` implica que o registro está ativo.

### sub_org_id
- **Significado**: representa uma suborganização dentro da organização principal, se aplicável.
- **Função**: chave estrangeira.
- **Conteúdo típico**: normalmente `None`, o que indica que pode nem sempre ser usado.
```

Esta documentação oferece uma visão geral estruturada da tabela `public.document_type_attributes`, permitindo que os desenvolvedores entendam a finalidade e o uso de cada coluna.
