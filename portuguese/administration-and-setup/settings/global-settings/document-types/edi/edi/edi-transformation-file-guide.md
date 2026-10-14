# Guia do Arquivo de Transformação EDI

## 1. Visão Geral

O **Arquivo de Transformação** define como o XML estruturado—criado usando o **Arquivo de Descritor de Estrutura**—é convertido em um formato XML personalizado que corresponde aos requisitos específicos de tipo de documento ou formulário da sua organização.

Essa transformação é realizada usando **XSLT (Extensible Stylesheet Language Transformations)**, que pode ser criado e mantido por meio do **Editor XSLT** na interface do DocBits.

## 2. Propósito e Função

* Transforma o **XML intermediário** (saída do Descritor de Estrutura) em um **XML final** alinhado com o esquema do seu documento.
* Permite flexibilidade para acomodar formatos de parceiros EDI variados e requisitos internos do sistema.
* Construído usando **regras XSLT**, que permitem definir mapeamentos, formatação de valores, lógica condicional e estrutura.

## 3. Acesso e Edição Básica

#### Acessando o Arquivo

1.  Vá para **Configurações → Tipo de Documento** → \[Seu Documento (por exemplo, _Ordem de Compra_)] → **E-Doc.**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1yCRagLzRFmy2hPRDDc1%252Fimage.png%3Falt%3Dmedia%26token%3D020874a9-1eae-4965-9dd2-c23461fc5884\&width=768\&dpr=4\&quality=100\&sign=5e53a730\&sv=2)
2. Na aba **E-Doc**, selecione o seu formato (por exemplo, **EDI**).
3.  Clique em **Transformação** para visualizar ou editar.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZtaE4dZT9E1exWMZ5FCI%252Fimage.png%3Falt%3Dmedia%26token%3D787868b4-47b4-455e-9a26-112f692b91f3\&width=768\&dpr=4\&quality=100\&sign=460124f1\&sv=2)

#### Gerenciamento de Rascunhos

* **Criar um Rascunho**: Clique no ícone de ✏️ lápis.
* **Excluir Rascunhos**: Use o ícone de 🗑️ lixeira para remover rascunhos não utilizados.
* **Ativar Alterações**: Clique no ✅ marca de seleção para publicar uma versão.
  * **Nota**: Ativar uma nova versão irá **desativar automaticamente** a anterior.

## 4. Editor XSLT

O Arquivo de Transformação é editado usando um **Editor XSLT** incorporado que suporta destaque de sintaxe e validação.

* Adicione modelos para mapear caminhos específicos do XML de entrada para a estrutura desejada.
* Use lógica condicional (por exemplo, `<xsl:if>`, `<xsl:choose>`) para lidar com formatos de dados opcionais ou variados.
* Aplique funções de formatação conforme necessário (por exemplo, manipulação de strings, formatação de datas).

## 5. Função de Visualização (Visualizar XML Transformado)

A **Função de Visualização** permite testar e visualizar como um arquivo EDI enviado é processado usando o **Arquivo de Transformação** atual.

#### Uso

* Envie um arquivo EDI via o fluxo de upload padrão.
* Copie o **ID do Documento** do arquivo enviado.
* Navegue até a interface do **Arquivo de Transformação**.
*   Abra a **Função de Visualização**.\


    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=36ce2b93&#x26;sv=2" alt="" width="375"></div>
* Insira o **ID do Documento** no campo e pressione **Testar**.
* A saída do **XML transformado resultante** será exibida.

Isso é especialmente útil para depurar mapeamentos XSLT e garantir que a estrutura final do XML atenda aos requisitos do seu formato.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWbwwmXgp6nRPIb1zBpgj%252Fimage.png%3Falt%3Dmedia%26token%3Dab5766f1-45bf-484e-9aa4-ab3059705591\&width=768\&dpr=4\&quality=100\&sign=46905864\&sv=2)

## 6. Tutorial em Vídeo

Um guia em vídeo para este tipo de arquivo está disponível na [página de Vídeos.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Use-o para acompanhar a configuração, edição e visualização.
