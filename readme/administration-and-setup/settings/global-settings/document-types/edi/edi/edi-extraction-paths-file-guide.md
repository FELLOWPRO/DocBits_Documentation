# Guia do Arquivo de Caminhos de Extração EDI

## 1. Visão Geral

O **Arquivo de Caminhos de Extração** define como os dados são extraídos do **XML estruturado** em campos de documento específicos e tabelas dentro da interface. Ele mapeia **IDs de campo** para **expressões XPath**, que são avaliadas para extrair valores do XML para os campos de documento correspondentes. Este arquivo desempenha um papel crítico em garantir que os dados extraídos apareçam corretamente durante a validação de campo e processamento subsequente.

## 2. Propósito e Função

* Mapeia cada campo de documento e coluna de tabela para uma localização específica no XML estruturado usando expressões XPath.
* Garante que os valores corretos sejam populados em campos como `order_number`, `supplier_name` e `total_amount`.
* Suporta tanto **campos únicos** (via um objeto `fields`) quanto **tabelas** (via um array `tables` com caminhos de linha e mapeamentos de coluna).
* Permite controle preciso sobre como os dados são recuperados do XML, incluindo o uso de funções XPath como `sum()`.

Exemplo de mapeamento de campo:

Copy

```
"order_number": "//PURCHASE_ORDER/PURCHASE_ORDER/text()"
```

## 3. Acesso e Edição Básica

#### **Acessando o Arquivo:**

1.  Vá para **Configurações** → **Tipo de Documento** → _\[Seu Documento (por exemplo, Ordem de Compra)]_ → **E-Doc**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff6zyL0AvmqSvrogZdnox%252Fimage.png%3Falt%3Dmedia%26token%3D6bc9ab55-6ee9-43d1-b576-4c5833c208cf\&width=768\&dpr=4\&quality=100\&sign=a23de442\&sv=2)
2. Sob a aba **E-Doc**, selecione seu formato (por exemplo, **EDI**).
3.  Clique em **Caminhos de Extração** para visualizar ou editar o arquivo.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FawwG5QnErp1yy1eYHrlX%252Fimage.png%3Falt%3Dmedia%26token%3D46a6d8b3-52d2-4c13-bc72-1a74955efd9f\&width=768\&dpr=4\&quality=100\&sign=e612882b\&sv=2)

#### **Gerenciamento de Rascunho:**

* **Criar um Rascunho:** Clique no ícone ✏️ lápis.
* **Excluir Rascunhos:** Use o ícone 🗑️ lixeira para remover rascunhos não utilizados.
* **Ativar Alterações:** Clique no ✅ marca de seleção para publicar uma versão.
  * **Nota**: Ativar uma nova versão irá **desativar automaticamente** a anterior.

## 4. Editor e Sintaxe

O Arquivo de Caminhos de Extração é escrito em **JSON** e contém dois componentes principais:

* **fields**: Um dicionário onde cada chave é um ID de campo e cada valor é uma expressão XPath que define como extrair os dados.
* **tables**: Uma lista de definições de tabela que incluem:
  * `name`: O ID da tabela.
  * `row_path`: Um XPath que identifica cada linha da tabela.
  * `columns`: Uma lista de mapeamentos de coluna (`name`, `path`).

Você também pode usar funções XPath (por exemplo, `sum()`) e expressões para calcular valores dinamicamente a partir de elementos repetidos.

Copy

```
jsonCopyEdit"total_net_amount": "sum(//PURCHASE_ORDER/ORDER_LINES/ORDER_LINE/SUB_TOTAL)"
```

## 5. Função de Visualização (Avaliar Extração)

A **Função de Visualização** permite simular como os caminhos de extração se comportarão com um documento real enviado.

**Uso:**

* Envie um arquivo EDI através do processo de envio padrão.
* Copie o **ID do Documento**.
* Vá para a interface de **Caminhos de Extração**.
* Abra a **Função de Visualização**.\
  \
  &#x20;![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a\&width=300\&dpr=4\&quality=100\&sign=36ce2b93\&sv=2)
* Insira o ID do Documento e clique em **Testar**.
* O resultado mostrará como cada campo e tabela é populado com base nos caminhos configurados.

Esta funcionalidade é essencial para verificar se suas expressões XPath estão corretamente definidas e puxando os valores esperados antes de ativar o rascunho.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F81uvH6FFVBJsSZucanWY%252Fimage.png%3Falt%3Dmedia%26token%3Dde3ba545-1ee3-44b2-a629-9660d80174f2\&width=768\&dpr=4\&quality=100\&sign=43c8b507\&sv=2)

## 6. Tutorial em Vídeo

Um guia em vídeo para este tipo de arquivo está disponível na [página de Vídeos.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Use-o para acompanhar a configuração, edição e visualização.

## Regras efetivas e ativação

Se uma nota de crédito eletrónica aparecer como Invoice, siga o [guia de resolução de problemas de classificação](../credit-note-recognized-as-invoice.md). Este explica como verificar a origem personalizada ou predefinida efetivamente utilizada, os códigos de tipo, os Extraction Paths e a ativação segura.
