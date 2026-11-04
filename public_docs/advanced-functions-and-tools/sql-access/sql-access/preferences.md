# Preferências

## Colunas

* `id`: interno
* `org_id`: ID da organização
* `pref_key`: interno
* `pref_value`: texto
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `deleted_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `user_id`: inteiro
* `sub_org_id`: interno

## Análise e descrição

```markdown
# Documentação técnica da tabela `public.preferences`

## Introdução
A tabela `public.preferences` foi projetada para armazenar configurações e preferências de várias entidades organizacionais dentro de um sistema. Cada entrada da tabela representa uma chave de preferência específica e o valor correspondente, associados a uma organização ou suborganização. Esses dados de configuração podem incluir ajustes relacionados a números de IVA, configurações de extração, ativação de módulos e muito mais.

## Descrição das colunas

### id
- **Significado**: esta coluna armazena o identificador único de cada entrada de preferência.
- **Função**: chave primária.
- **Conteúdo típico**: uma string UUID que identifica cada linha de forma única, como `23f3d697-7411-4c95-981d-faf089d266be`.

### org_id
- **Significado**: esta coluna armazena o identificador da organização à qual a preferência está associada.
- **Função**: chave estrangeira.
- **Conteúdo típico**: uma string UUID que corresponde a uma organização, semelhante a `23f3d697-7411-4c95-981d-faf089d266be`.

### pref_key
- **Significado**: esta coluna representa a chave ou o nome da configuração de preferência.
- **Função**: campo descritivo.
- **Conteúdo típico**: strings que representam chaves de configuração, como `VAT_NUMBERS` e `TABLE_EXTRACTION_SETTING`.

### pref_value
- **Significado**: esta coluna contém o valor da preferência correspondente a `pref_key`.
- **Função**: campo descritivo.
- **Conteúdo típico**: varia conforme a `pref_key`; os exemplos incluem números de IVA separados por vírgulas ou valores booleanos como `true` ou `false`.

### created_by
- **Significado**: esta coluna indica o ID do usuário que criou a entrada de preferência.
- **Função**: campo descritivo.
- **Conteúdo típico**: um número inteiro que representa o ID de um usuário, por exemplo `1`.

### created_on
- **Significado**: esta coluna registra o timestamp de quando a preferência foi criada.
- **Função**: campo técnico.
- **Conteúdo típico**: um timestamp com fuso horário, por exemplo `2021-11-09 11:04:18+00`.

### last_modified_on
- **Significado**: esta coluna registra o timestamp da última modificação da preferência.
- **Função**: campo técnico.
- **Conteúdo típico**: um timestamp com fuso horário que indica o momento da última atualização, como `2023-12-04 10:10:26+00`.

### deleted_on
- **Significado**: esta coluna registra o timestamp de quando a preferência foi marcada como excluída.
- **Função**: campo técnico.
- **Conteúdo típico**: normalmente `null`, a menos que a linha esteja marcada para exclusão.

### is_deleted
- **Significado**: esta coluna indica se a preferência foi marcada como excluída.
- **Função**: campo técnico.
- **Conteúdo típico**: um valor booleano, normalmente `false`.

### user_id
- **Significado**: esta coluna armazena o ID do usuário associado à preferência.
- **Função**: campo descritivo, potencialmente uma chave estrangeira.
- **Conteúdo típico**: um número inteiro ou `null` se não for aplicável.

### sub_org_id
- **Significado**: esta coluna identifica a suborganização associada à preferência.
- **Função**: chave estrangeira.
- **Conteúdo típico**: uma string UUID ou `null` se não for aplicável.

A tabela `public.preferences` oferece uma forma flexível e abrangente de gerenciar as configurações de diferentes entidades organizacionais, garantindo que as preferências possam ser ajustadas dinamicamente e acompanhadas ao longo do tempo.
```
