# Endereço do fornecedor

## Colunas

* `org_id`: ID da organização
* `customer_number`: interno
* `supplier_number`: interno
* `address_id`: interno
* `supplier_name`: nome do fornecedor
* `address_1`: interno
* `address_2`: interno
* `address_3`: interno
* `address_4`: interno
* `zip_code`: interno
* `town_city`: interno
* `country_code`: interno
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `sub_org_id`: interno
* `id`: interno

## Análise e descrição

```markdown
# Documentação técnica da tabela `public.supplier_address`

## Introdução

A tabela `public.supplier_address` foi projetada para armazenar informações relacionadas aos endereços de fornecedores. Ela contém vários campos que registram detalhes como IDs organizacionais, números de clientes e de fornecedores, várias linhas de endereço, dados de contato, metadados de criação e modificação e o status de exclusão. Essa tabela provavelmente é usada em um sistema para gerenciar as informações dos fornecedores e seus respectivos endereços, o que pode ser essencial para fins de logística, faturamento e contato.

## Descrição das colunas

### org_id
- **Significado**: esta coluna armazena o identificador único da organização.
- **Função**: chave estrangeira, possivelmente vinculada a uma tabela de organizações.
- **Conteúdo típico**: UUID que representa uma organização.

### customer_number
- **Significado**: esta coluna pode armazenar um número único atribuído aos clientes.
- **Função**: identificador de clientes.
- **Conteúdo típico**: string alfanumérica que representa números de clientes.

### supplier_number
- **Significado**: esta coluna armazena um número único atribuído aos fornecedores.
- **Função**: identificador de fornecedores.
- **Conteúdo típico**: string numérica que representa números de fornecedores.

### address_id
- **Significado**: esta coluna provavelmente armazena o tipo de endereço, como 'Discrete' ou 'Text'.
- **Função**: campo descritivo para a categorização do endereço.
- **Conteúdo típico**: valores como 'Discrete' e 'Text'.

### supplier_name
- **Significado**: esta coluna armazena o nome do fornecedor.
- **Função**: campo descritivo para a identificação do fornecedor.
- **Conteúdo típico**: nome do fornecedor, por exemplo "Cake Corp. GmbH Qualitätsstrawberrys".

### address_1
- **Significado**: esta coluna armazena a primeira linha do endereço do fornecedor.
- **Função**: campo descritivo para as informações de endereço.
- **Conteúdo típico**: logradouro, por exemplo "Irrweg. 42, D-12345 Blastadt".

### address_2
- **Significado**: esta coluna armazena a segunda linha do endereço do fornecedor, se aplicável.
- **Função**: campo complementar para as informações de endereço.
- **Conteúdo típico**: detalhes adicionais do endereço, frequentemente deixado em branco.

### address_3
- **Significado**: esta coluna armazena a terceira linha do endereço do fornecedor, se aplicável.
- **Função**: campo complementar para as informações de endereço.
- **Conteúdo típico**: detalhes adicionais do endereço, frequentemente deixado em branco.

### address_4
- **Significado**: esta coluna armazena a quarta linha do endereço do fornecedor, se aplicável.
- **Função**: campo complementar para as informações de endereço.
- **Conteúdo típico**: detalhes adicionais do endereço, frequentemente deixado em branco.

### zip_code
- **Significado**: esta coluna armazena o código postal do endereço do fornecedor.
- **Função**: campo descritivo para a identificação geográfica.
- **Conteúdo típico**: código postal numérico, por exemplo "06449".

### town_city
- **Significado**: esta coluna armazena o nome da localidade ou da cidade do endereço do fornecedor.
- **Função**: campo descritivo para a identificação geográfica.
- **Conteúdo típico**: nome da localidade ou da cidade, por exemplo "Aschersleben".

### country_code
- **Significado**: esta coluna armazena o código ISO do país do endereço do fornecedor.
- **Função**: campo descritivo para a identificação do país.
- **Conteúdo típico**: código de país com duas letras, por exemplo "DE".

### created_by
- **Significado**: esta coluna armazena o identificador do usuário ou do sistema que criou o registro.
- **Função**: campo técnico para registrar a criação do registro.
- **Conteúdo típico**: número inteiro que representa o ID de um usuário.

### created_on
- **Significado**: esta coluna armazena o timestamp de quando o registro foi criado.
- **Função**: campo técnico para registrar o momento da criação do registro.
- **Conteúdo típico**: timestamp com fuso horário, por exemplo "2021-11-25 11:24:33 UTC".

### last_modified_on
- **Significado**: esta coluna armazena o timestamp da última modificação do registro.
- **Função**: campo técnico para registrar o momento da última atualização.
- **Conteúdo típico**: timestamp com fuso horário, frequentemente deixado como `None`.

### is_deleted
- **Significado**: esta coluna indica se o registro está marcado como excluído.
- **Função**: campo técnico para a funcionalidade de exclusão lógica.
- **Conteúdo típico**: valor booleano, por exemplo `False`.

### sub_org_id
- **Significado**: esta coluna armazena um identificador de suborganização, se aplicável.
- **Função**: chave estrangeira ou identificador de suborganizações.
- **Conteúdo típico**: UUID, frequentemente deixado em branco.

### id
- **Significado**: esta coluna armazena o identificador único do registro.
- **Função**: chave primária da tabela.
- **Conteúdo típico**: UUID que representa o registro.

```
