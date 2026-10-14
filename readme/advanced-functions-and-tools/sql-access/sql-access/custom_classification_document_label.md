# Custom\_classification\_document\_label

## Tabela `public.custom_classification_document_label`

### Colunas

* `id`: inteiro
* `org_id`: ID da organização
* `doc_id`: interno
* `label_id`: inteiro
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano

### Análise e descrição

## Documentação técnica da tabela `public.custom_classification_document_label`

### Introdução

A tabela `public.custom_classification_document_label` foi projetada para gerenciar e armazenar as associações entre documentos e seus respectivos rótulos dentro de uma organização. Esta tabela facilita a categorização e a recuperação de documentos com base em rótulos personalizados, oferecendo uma forma estruturada de gerenciar a classificação de documentos para diversas necessidades organizacionais.

### Descrição das colunas

#### id

* **Significado**: esta coluna serve como identificador único de cada registro da tabela.
* **Função**: chave primária
* **Conteúdo típico**: um valor inteiro que identifica cada linha de forma única.
* **Observação**: cada entrada da tabela possui um `id` distinto para garantir a integridade dos dados e permitir referências eficientes.

#### org\_id

* **Significado**: representa a organização à qual a associação entre documento e rótulo pertence.
* **Função**: chave estrangeira
* **Conteúdo típico**: uma cadeia de caracteres, provavelmente um UUID, que identifica uma organização de forma única.
* **Observação**: garante que a associação entre documentos e rótulos fique restrita ao contexto organizacional correto.

#### doc\_id

* **Significado**: identifica o documento que recebe o rótulo.
* **Função**: chave estrangeira
* **Conteúdo típico**: uma cadeia de caracteres, provavelmente um UUID, que identifica um documento de forma única.
* **Observação**: permite vincular documentos específicos a rótulos, viabilizando a categorização de documentos.

#### label\_id

* **Significado**: refere-se ao rótulo aplicado ao documento.
* **Função**: chave estrangeira
* **Conteúdo típico**: um inteiro que referencia um rótulo de uma tabela de rótulos separada.
* **Observação**: facilita a associação entre documentos e seus respectivos rótulos.

#### created\_by

* **Significado**: identifica o usuário que criou o registro.
* **Função**: chave estrangeira (potencialmente para uma tabela de usuários)
* **Conteúdo típico**: um inteiro que representa o ID do usuário.
* **Observação**: registra a origem de cada associação entre documento e rótulo para fins de auditoria e responsabilização.

#### created\_on

* **Significado**: indica quando o registro foi criado.
* **Função**: campo técnico
* **Conteúdo típico**: um timestamp com informações de fuso horário.
* **Observação**: fornece o contexto temporal de quando a relação entre documento e rótulo foi estabelecida.

#### last\_modified\_on

* **Significado**: registra o timestamp da última modificação do registro.
* **Função**: campo técnico
* **Conteúdo típico**: um timestamp com informações de fuso horário; pode ser `None` se nunca foi modificado.
* **Observação**: útil para acompanhar o histórico de alterações das associações entre documento e rótulo.

#### is\_deleted

* **Significado**: sinaliza se o registro foi marcado como excluído.
* **Função**: campo técnico
* **Conteúdo típico**: um valor booleano (`True` ou `False`).
* **Observação**: oferece suporte a práticas de exclusão lógica, permitindo a remoção lógica dos dados sem exclusão física do banco de dados.
