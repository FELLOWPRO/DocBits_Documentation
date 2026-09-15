---
description: Como importar dados mestres para um conjunto de dados de lookup a partir de um ficheiro XML
---

# Importar Dados Mestres de XML

Para além das importações de BOD, o DocBits consegue ler dados mestres de **qualquer ficheiro XML** para um conjunto de dados de lookup à sua escolha. Indica em que conjunto escrever e de que XPath cada coluna deve ser lida, pelo que o XML não tem de seguir um formato BOD de todo.

Use isto para dados mestres que não chegam como BOD — listas de preços, centros de custo, atributos de artigo, tudo o que o seu ERP consiga exportar como XML.

## Duas formas de enviar o XML

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-endpoints.png)

| Endpoint | Quando o usar |
| --- | --- |
| `/master_data_lookup/xml/import_xml_file` | Tem os dados como **ficheiro XML** e quer carregá-lo. |
| `/master_data_lookup/xml/import_xml_data` | Quer **colar o XML** no pedido. Ao contrário dos endpoints de BOD, este aceita o XML como texto simples — sem invólucro JSON. |

Ambos são descritos abaixo. Os passos 1 e 2 são iguais nos dois casos.

## Antes de começar

Vai precisar de:

* **Uma API key.** Consulte [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md) se ainda não tiver uma.
* **O XML** — como ficheiro ou como conteúdo que possa colar.
* **Um tipo de dados** — o nome do conjunto de dados de lookup onde escrever.
* **Mapeamentos de campos** — que XPath preenche que coluna.
* **O seu Org ID**, em **Settings → Integration & SSO**, na secção **ID**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-org-id.png)

## Instruções passo a passo

### 1. Abrir a ligação da API

Abra a interface de teste da API para o ambiente e a região com que está a trabalhar:

* [Sandbox API (Europa)](https://eu.sandbox.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Sandbox API (Estados Unidos)](https://us.sandbox.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Production API (Europa)](https://eu.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Production API (Estados Unidos)](https://us.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)

Estes endpoints encontram-se em **master data lookup** e não em **import**, mais abaixo na página.

{% hint style="info" %}
Use a região onde a sua organização está alojada — a mesma região com que inicia sessão no DocBits. Os ambientes europeu e americano são separados, pelo que uma importação enviada para a região errada não aparecerá na sua organização.
{% endhint %}

### 2. Autorizar

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-lock.png)

Autorizar funciona exatamente como nas importações de BOD: clique no **ícone de cadeado**, cole o seu **Org ID** em **X-ORG-ID**, cole a sua API key em **X-API-KEY** e clique em **Authorize** em cada uma.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey.png)

### 3. Preencher os campos

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-tryitout-xml.png)

Clique em **Try it out** e preencha depois o formulário.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-form.png)

| Campo | |
| --- | --- |
| **data\_type** | Obrigatório. O conjunto de dados de lookup onde escrever. É convertido automaticamente para minúsculas, pelo que `PriceList` e `pricelist` são o mesmo conjunto. |
| **field\_mappings** | Obrigatório. Um objeto JSON que associa cada coluna ao XPath de onde é lida. Veja abaixo. |
| **file** | Obrigatório em `import_xml_file`. Clique em **Choose file** e selecione o seu XML. |
| **xml** | Obrigatório em `import_xml_data` em vez do ficheiro — cole aí o XML como texto simples. |
| **org\_id** | O seu Org ID — o mesmo valor que colocou em **X-ORG-ID** no passo 2. |
| **sub\_org\_id** | Só é necessário se estiver a importar para uma suborganização específica. |

#### Mapeamentos de campos

`field_mappings` é um objeto JSON com uma entrada por coluna. Ao contrário das importações de BOD, onde os nomes estão fixados em `custom_field_1` … `custom_field_5`, aqui é você que os escolhe:

```json
{
  "ID": "//Item/ID",
  "Description": "//Item/Description",
  "Price": "//Item/UnitPrice"
}
```

Os nomes à esquerda passam a ser as colunas do conjunto de dados e são da sua escolha. Os valores à direita têm de corresponder à estrutura do XML que está a carregar — no exemplo acima, `//Item/ID` apanha o elemento `<ID>` dentro de cada `<Item>`. Os dois lados são independentes: o mapeamento acima lê `<UnitPrice>` para uma coluna chamada `Price`.

{% hint style="warning" %}
Só os XPath **malformados** são rejeitados, com um `400` a nomear o campo. Um XPath que seja válido mas não corresponda a nada no seu XML passa em silêncio e deixa simplesmente essa coluna vazia — uma gralha num caminho parece portanto uma importação que funcionou mas perdeu uma coluna. Se for o caminho do `ID` a não corresponder a nada, a importação falha e comunica que falta a coluna `ID` para esse registo.
{% endhint %}

{% hint style="warning" %}
**Uma das colunas tem de se chamar `ID`.** É ela que identifica um registo: importar os mesmos dados de novo atualiza a linha com esse ID em vez de acrescentar um duplicado. O nome não distingue maiúsculas de minúsculas, pelo que `ID`, `Id` e `id` funcionam todos, mas um nome como `ItemID` não conta — o pedido é rejeitado com `ID_FIELD_IS_MISSING` e nada é escrito.
{% endhint %}

{% hint style="warning" %}
**Um pedido importa um registo.** Cada XPath é lido uma vez, pelo que, se o seu XML contiver vários elementos, apenas a primeira correspondência de cada um é usada. Para carregar uma lista, envie um pedido por registo ou use antes uma importação CSV.
{% endhint %}

#### Escolher um tipo de dados

`data_type` é a chave do conjunto de dados onde está a escrever. É convertido para minúsculas e limpo de espaços, pelo que `Items` e `items` são o mesmo conjunto. Qualquer nome que ainda não esteja ocupado cria um conjunto seu — `items_example`, `cost_centres`, `price_list` — e importar novamente para ele atualiza-o.

{% hint style="danger" %}
Alguns nomes não estão livres: são as próprias tabelas de dados mestres do DocBits, e importar para uma delas escreve diretamente lá dentro.

| Nome | |
| --- | --- |
| `purchase_order_header`, `purchase_order_address` | Rejeitados com `RESERVED_DATASET_NAME`. |
| `supplier`, `supplier_accounts`, `purchase_order`, `receive_delivery`, `receive_delivery_lines`, `costing_element`, `customer_erp_items`, `supplier_item_price`, `supplier_item_number_mapping` | **Aceites, e sobrescrevem dados mestres reais.** Use-os apenas se for genuinamente isso que pretende. |

Para tudo o resto, escolha um nome seu.
{% endhint %}

{% hint style="warning" %}
Verifique para que ambiente e que organização está a apontar antes de executar. Uma importação escreve diretamente nos dados mestres dessa organização.
{% endhint %}

### 4. Executar

Antes de executar, verifique a lista pendente **Servers** no fundo do formulário.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-execute.png)

Clique em **Execute**. Uma importação bem-sucedida devolve:

```json
{
  "success": true,
  "message": "Record(s) created/updated successfully"
}
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-response.png)

Ao contrário das importações de BOD, estes endpoints comunicam os problemas com um estado de erro propriamente dito em vez de um `200` a transportar `"success": false` — um **400** significa que o pedido foi rejeitado e que nada foi escrito.

### 5. Verificar se os dados chegaram

* No DocBits, vá a **Settings → Document Processing → Lookup Master Data**.
* Selecione **Imported** à esquerda e abra depois o separador do seu tipo de dados.
* As colunas são os nomes que usou do lado esquerdo de `field_mappings`.

<!-- SCREENSHOT: Lookup Master Data with Imported selected and the new dataset open -->
