# Guia do Arquivo de Pré-visualização EDI

## 1. Visão Geral

O **Arquivo de Pré-visualização** define como os dados XML estruturados são renderizados em um formato legível por humanos, semelhante a um PDF. Ele combina **HTML e CSS** para apresentação visual e usa declarações **XSLT** `**select**` para inserir dinamicamente dados do XML Personalizado. Esta pré-visualização é exibida durante a **validação de campo** e também é incluída ao exportar documentos para **IDM**.

## 2. Propósito e Função

* Converte o XML Personalizado legível por máquina em uma pré-visualização formatada visualmente (PDF).
* Permite a revisão e validação amigável dos dados extraídos.
* Garante a renderização consistente de campos de documentos-chave, como cabeçalhos, tabelas, totais, etc.
* Construído usando **HTML + CSS** para layout e design, e **XSLT** para vincular dados ao layout.

## 3. Acesso e Edição Básica

#### **Acessando o Arquivo:**

1.  Vá para **Configurações** → **Tipo de Documento** → _\[Seu Documento (por exemplo, Ordem de Compra)]_ → **E-Doc**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Ff6zyL0AvmqSvrogZdnox%252Fimage.png%3Falt%3Dmedia%26token%3D6bc9ab55-6ee9-43d1-b576-4c5833c208cf\&width=768\&dpr=4\&quality=100\&sign=a23de442\&sv=2)
2. Na aba **E-Doc**, selecione o formato (por exemplo, **EDI**).
3.  Clique em **Pré-visualização** para visualizar ou editar o arquivo.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fdo1R389GeSqFuZKLD0OP%252Fimage.png%3Falt%3Dmedia%26token%3D930903d4-44af-4188-b015-c60c2dd9d9ab\&width=768\&dpr=4\&quality=100\&sign=77bbb2ce\&sv=2)

#### **Gerenciamento de Rascunhos:**

* **Criar um Rascunho:** Clique no ícone ✏️ lápis.
* **Excluir Rascunhos:** Use o ícone 🗑️ lixeira para remover rascunhos não utilizados.
* **Ativar Alterações:** Clique no ✅ marca de seleção para publicar uma versão.
  * **Nota**: Ativar uma nova versão irá **desativar automaticamente** a anterior.

## 4. Editor HTML/XSLT/CSS

O **Arquivo de Pré-visualização** é editado em um editor dedicado que suporta HTML, XSLT e CSS.

* **HTML** define a estrutura do documento de saída (por exemplo, tabelas, divs, layout).
* **CSS** controla o estilo (por exemplo, fontes, espaçamento, cores, alinhamento).
*   As declarações **XSLT** `**select**` são usadas para popular dinamicamente campos do XML Personalizado, como:

    Copy

    ```
    <xsl:value-of select="/PURCHASE_ORDER/PURCHASE_ORDER_NUMBER/text()" />
    ```
* Você também pode usar **lógica XSLT** (`<xsl:if>`, `<xsl:for-each>`, etc.) para lidar com exibição condicional ou iterar sobre itens de linha.

## 5. Função de Pré-visualização (Renderização de Saída)

A Função de Pré-visualização permite testar e verificar como um documento EDI é renderizado com o Arquivo de Pré-visualização atual.

#### **Uso:**

* Faça upload de um arquivo EDI através do processo de upload padrão.
* Copie o **ID do Documento** do arquivo enviado.
* Navegue até a interface de **Pré-visualização**.
* Abra a **Função de Pré-visualização**.\
  \
  ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a\&width=300\&dpr=4\&quality=100\&sign=36ce2b93\&sv=2)
* Insira o ID do Documento e clique em **Testar**.
* A pré-visualização em estilo PDF será exibida usando a configuração HTML/CSS/XSLT.

Este recurso é crucial para depurar vinculações de dados, aprimorar o layout e garantir que o documento seja preciso e visualmente claro para os usuários e sistemas downstream como **IDM**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FJH103tnbqZjuimpOniVg%252Fimage.png%3Falt%3Dmedia%26token%3D4e63cc09-b0de-488f-bdd0-ee5a9246a371\&width=768\&dpr=4\&quality=100\&sign=bfff5bba\&sv=2)

## 6. Tutorial em Vídeo

Um guia em vídeo para este tipo de arquivo está disponível na [página de Vídeos.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Use-o para acompanhar a configuração, edição e pré-visualização.
