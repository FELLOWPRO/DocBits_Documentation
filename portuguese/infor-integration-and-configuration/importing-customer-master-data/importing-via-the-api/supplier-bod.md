---
description: Como importar um Supplier BOD no DocBits manualmente através da API
---

# Importar Fornecedores (Supplier BOD)

Os dados mestres de fornecedores chegam normalmente ao DocBits de forma automática através do seu fluxo de dados ION. Esta página descreve como enviar um **Supplier BOD** manualmente — útil quando quer reimportar um fornecedor, carregar um lote que nunca chegou ou testar um mapeamento de campos antes de ativar o fluxo automático.

## Duas formas de enviar o mesmo BOD

Existem dois endpoints e fazem a mesma coisa. A única diferença está na forma como entrega o BOD:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-supplier-endpoints.png)

| Endpoint | Quando o usar |
| --- | --- |
| `/import/supplier_bod` | Tem o BOD como **ficheiro XML** e quer carregá-lo. |
| `/import/supplier_bod_xml` | Quer enviar o **conteúdo XML** no pedido em vez de um ficheiro. O BOD tem de ser envolvido em JSON, pelo que isto se adequa a XML curto ou a outro sistema que chame a API — para um BOD completo à mão, carregue o ficheiro. |

Ambos são descritos abaixo. Os passos 1 e 2 são iguais nos dois casos.

## Antes de começar

Vai precisar de:

* **Uma API key.** Consulte [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md) se ainda não tiver uma.
* **O BOD** — um ficheiro XML `SyncSupplierPartyMaster` ou `SyncRemitToPartyMaster`, ou o respetivo conteúdo.
* **O seu Org ID**, em **Settings → Integration & SSO**, na secção **ID**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-org-id.png)

{% hint style="info" %}
**Sub Org ID** mostra a suborganização que estiver selecionada no cabeçalho. Com **CROSS** selecionado — a vista sobre todas as suborganizações — mostra o mesmo valor que **Org ID**. Mude primeiro para uma suborganização específica se precisar do ID dela.

Se não estiver a importar para uma suborganização específica, deixe o campo `sub_org_id` vazio.
{% endhint %}

## Instruções passo a passo

### 1. Abrir a ligação da API

Abra a interface de teste da API para o ambiente e a região com que está a trabalhar:

* [Sandbox API (Europa)](https://eu.sandbox.api.docbits.com/docs#/import/import_supplier_bod_import_supplier_bod_post)
* [Sandbox API (Estados Unidos)](https://us.sandbox.api.docbits.com/docs#/import/import_supplier_bod_import_supplier_bod_post)
* [Production API (Europa)](https://eu.api.docbits.com/docs#/import/import_supplier_bod_import_supplier_bod_post)
* [Production API (Estados Unidos)](https://us.api.docbits.com/docs#/import/import_supplier_bod_import_supplier_bod_post)

Expanda o endpoint pretendido clicando nele.

{% hint style="info" %}
Use a região onde a sua organização está alojada — a mesma região com que inicia sessão no DocBits. Os ambientes europeu e americano são separados, pelo que uma importação enviada para a região errada não aparecerá na sua organização.

Os endereços sem prefixo de região — `api.docbits.com` e `sandbox.api.docbits.com` — apontam para a Europa. Encontrá-los-á em documentação mais antiga e em configurações existentes; são o mesmo ambiente que os endereços `eu.` acima.
{% endhint %}

### 2. Autorizar

Tudo o que está sob **import** fica bloqueado até autorizar. Há duas coisas a preencher: a sua organização e a sua API key.

* Clique no **ícone de cadeado** à direita do endpoint.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-supplier-lock.png)

* Abre-se a caixa de diálogo **Available authorizations** com duas entradas.
* Cole o seu **Org ID** em **X-ORG-ID** e clique em **Authorize**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid-done.png)

* Desça até **X-API-KEY**, cole a sua API key e clique em **Authorize**. No DocBits encontra-a em **Settings → Integration & SSO**, na secção **API Key**, ou pode [criar uma nova chave](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md#criar-uma-chave-api).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey-done.png)

* Clique em **Close**.

{% hint style="info" %}
Cole a chave sozinha — não escreva `Bearer` à frente. Ambas as autorizações permanecem ativas até recarregar a página ou clicar em **Logout**.
{% endhint %}

### 3. Preencher os campos

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-tryitout.png)

Clique em **Try it out** e preencha depois o formulário do endpoint que escolheu.

#### Carregar um ficheiro — `/import/supplier_bod`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-supplier-bod-form.png)

| Campo | |
| --- | --- |
| **file** | Obrigatório. Clique em **Choose file** e selecione o seu ficheiro XML do supplier BOD. |
| **org\_id** | O seu Org ID — o mesmo valor que colocou em **X-ORG-ID** no passo 2. Defini-lo também aqui torna explícito para que organização o pedido está a escrever. Tem de ser uma organização a que a sua API key tenha acesso; qualquer outra é recusada. |
| **sub\_org\_id** | Só é necessário se estiver a importar para uma suborganização específica. |
| **custom\_fields\_mapping** | Opcional. Lê campos adicionais do BOD para os campos personalizados do fornecedor. Consulte [Mapeamentos de campos personalizados](#mapeamentos-de-campos-personalizados) abaixo. |

Não existe aqui um campo de mapeamento de linhas — os dados mestres de fornecedores não têm linhas.

{% hint style="warning" %}
**`string` é um valor, não um marcador de posição.** O Swagger preenche os campos opcionais com a palavra `string`, e ela é enviada tal e qual se a deixar lá — uma importação com `org_id` a `string` vai falhar.

Para cada campo opcional que não queira usar, limpe o campo. Limpá-lo ativa a caixa **Send empty value** por baixo, que pode então assinalar.
{% endhint %}

#### Mapeamentos de campos personalizados

O campo de mapeamento aceita um objeto JSON. O **nome à esquerda tem de ser um dos campos personalizados do próprio DocBits** — de `custom_field_1` a `custom_field_5` para fornecedores. Qualquer outro nome é ignorado sem aviso, pelo que uma gralha aqui parece exatamente um mapeamento que não funcionou.

O valor à direita é o XPath a partir do qual se lê. Escreva-o sem prefixos de espaço de nomes — o DocBits acrescenta-os sozinho:

```json
{"custom_field_2": "//SupplierPartyMaster/UserArea/Property/NameValue[@name='User defined 6']/text()"}
```

#### Colar o XML — `/import/supplier_bod_xml`

Este endpoint não aceita o BOD como uma simples colagem. O campo **xml** é um objeto, pré-preenchido com `{"xml": "string"}`. Substitua `string` pelo conteúdo do seu BOD, mantendo as aspas e as chavetas que o rodeiam:

```json
{
  "xml": "<SyncSupplierPartyMaster ...>...</SyncSupplierPartyMaster>"
}
```

{% hint style="warning" %}
O BOD fica dentro de uma cadeia JSON, pelo que cada aspa dupla do XML tem de ser escapada como `\"` — e um BOD está cheio delas. Se o resultado não for JSON válido, o pedido falha com um **422** e nada é importado.

Para um BOD real isso é moroso de fazer à mão, pelo que é preferível **carregar o ficheiro**.
{% endhint %}

Os campos `org_id`, `sub_org_id` e `custom_fields_mapping` funcionam exatamente como acima.

{% hint style="warning" %}
Verifique para que ambiente e que organização está a apontar antes de executar. Uma importação escreve diretamente nos dados mestres dessa organização.
{% endhint %}

### 4. Executar

Antes de executar, verifique a lista pendente **Servers** no fundo do formulário. É ela que decide para que ambiente o pedido é realmente enviado, e pode diferir da página que abriu.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-execute.png)

Clique em **Execute**. Uma importação bem-sucedida devolve:

```json
{
  "success": true,
  "message": "BOD processed successfully."
}
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-supplier-response.png)

Os supplier BOD são processados enquanto espera, pelo que, quando vir esta mensagem, os dados já lá estão.

Se algo estava errado no pedido, obtém `"success": false` juntamente com uma mensagem a descrever o problema. As causas mais comuns são conteúdo que não é um supplier BOD e um Org ID a que a sua API key não tem acesso.

### 5. Verificar se os dados chegaram

* No DocBits, vá a **Settings → Document Processing → Lookup Master Data**.
* Selecione **BOD Input Data** à esquerda e abra depois o separador **Supplier**.
* Procure o fornecedor do seu BOD.

<!-- SCREENSHOT: Lookup Master Data with BOD Input Data selected and the Supplier tab open -->

{% hint style="info" %}
O DocBits decide o que fazer com o BOD lendo o tipo que está lá dentro, e não pelo endpoint de importação que usou. Se enviar aqui um purchase order BOD por engano, ele é importado como ordem de compra em vez de ser rejeitado — verifique portanto se o separador onde encontra os dados é o que esperava.
{% endhint %}
