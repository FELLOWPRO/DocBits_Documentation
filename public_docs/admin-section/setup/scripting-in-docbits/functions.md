# Funções

**Documentação Funcional**

Este módulo contém funções para manipular dados de documentos e realizar várias operações relacionadas aos campos do documento.

## **Funções**

1. ### **set\_field\_value(document\_data, field\_name, value)**
* Descrição: Define o valor de um campo nos dados do documento.
* Parâmetros:
* `document_data` (dict): Os dados do documento contendo informações do campo.
* `field_name` (str): O nome do campo a ser definido.
* `value`: O valor a ser definido para o campo.
*   Exemplo:

`set_field_value(document_data, "nome", "Fulano de Tal")`
2. ### **set\_date\_value(document\_data, field\_name, value)**
* Descrição: Define o valor de um campo de data nos dados do documento.
* Parâmetros:
* `document_data` (dict): Os dados do documento contendo informações do campo.
* `field_name` (str): O nome do campo de data a ser definido.
* `value`: O valor da data a ser definido no formato ISO (por exemplo, "2020-12-31").
*   Exemplo:

`set_date_value(document_data, "data_de_nascimento", "1990-05-15")`
3. ### **set\_amount\_value(document\_data, field\_name, value)**
* Descrição: Define o valor de um campo de quantidade nos dados do documento.
* Parâmetros e uso de exemplo semelhantes ao `set_field_value`.
4. ### **set\_is\_required(document\_data, field\_name, value)**
* Descrição: Define o atributo 'is\_required' de um campo nos dados do documento.
* Parâmetros e uso de exemplo semelhantes ao `set_field_value`.
5. ### **set\_force\_validation(document\_data, field\_name, value)**
* Descrição: Define o atributo 'force\_validation' de um campo nos dados do documento.
* Parâmetros e uso de exemplo semelhantes ao `set_field_value`.
6. ### **set\_field\_attribute(document\_data, field\_name, attribute\_name, value)**
* Descrição: Define um atributo personalizado de um campo nos dados do documento.
* Parâmetros:
* `attribute_name` (str): O nome do atributo a ser definido.
* `value`: O valor a ser definido para o atributo.
*   Exemplo:

`set_field_attribute(document_data, "endereço", "está_verificado", True)`
7. ### **get\_field\_value(document\_data, field\_name, default\_value=None, is\_clean=False)**
* Descrição: Obtém o valor de um campo nos dados do documento.
* Parâmetros e uso de exemplo semelhantes ao `set_field_value`.
8. ### **create\_new\_field(field\_name, value="")**
* Descrição: Cria um novo campo com o nome e valor especificados.
* Parâmetros:
* `field_name` (str): O nome do campo a ser criado.
* `value`: O valor inicial para o campo (o padrão é uma string vazia).
*   Exemplo:

`create_new_field("endereço", "Rua Principal, 123")`
9. ### **delete\_field(document\_data, field\_name)**
* Descrição: Exclui um campo dos dados do documento.
* Parâmetros e uso de exemplo semelhantes ao `set_field_value`.
10. ### **update\_document\_status\_with\_doc\_id(doc\_id, user, org\_id, status, message=None, doc\_classification\_class=None)**
* Descrição: Atualiza o status de um documento com o ID especificado.
* Parâmetros:
* `doc_id` (str): O ID do documento a ser atualizado.
* `user`: O usuário que realiza a atualização (ID do usuário ou objeto UserAuthentication).
* `org_id`: O ID da organização à qual o documento pertence.
* `status` (str): O novo status do documento.
* `message`: Mensagem opcional associada à atualização de status.
* `doc_classification_class`: Classe de classificação de documento opcional.
*   Exemplo:

`update_document_status_with_doc_id("123456", user, org_id, "aprovado", "Documento aprovado")`
11. ### **is\_supplier\_valid(user: UserAuthentication, filter\_data\_json, sub\_org\_id=None)**
* Descrição: Verifica se um fornecedor é válido com base nos critérios fornecidos.
* Parâmetros:
* `user` (UserAuthentication): O usuário autenticado.
* `filter_data_json`: Critérios de filtro para validar o fornecedor.
* `sub_org_id`: ID de sub-organização opcional para filtragem.
*   Exemplo:

`is_supplier_valid(user, {"nome": "Fornecedor S.A."})`
12. ### **set\_field\_as\_invalid(document\_data, field\_name, message, code=None)**
* Descrição: Marca um campo como inválido nos dados do documento.
* Parâmetros:
* `document_data` (dict): Os dados do documento contendo informações do campo.
* `field_name` (str): O nome do campo a ser marcado como inválido.
* `message` (str): A mensagem de validação para o campo.
* `code` (opcional): Código de erro para a validação (o padrão é Nenhum).
*   Exemplo:

`set_field_as_invalid(document_data, "email", "Formato de e-mail inválido", "EMAIL_FORMAT_INVALID")`
13. ### **compare\_values(value1, value2)**
* Descrição: Compara dois valores quanto à igualdade, lidando com vários tipos de dados.
* Parâmetros:
* `value1`: O primeiro valor a ser comparado.
* `value2`: O segundo valor a ser comparado.
*   Exemplo:

`compare_values(10, "10")`
