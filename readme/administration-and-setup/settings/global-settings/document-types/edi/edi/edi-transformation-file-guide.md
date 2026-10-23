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

    ![Editor do tipo de documento Purchase Order com os separadores Edit layout, Document Sub Types, Table columns, Fields, Model Training, Regex, Scripts e E-Doc](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1yCRagLzRFmy2hPRDDc1%252Fimage.png%3Falt%3Dmedia%26token%3D020874a9-1eae-4965-9dd2-c23461fc5884\&width=768\&dpr=4\&quality=100\&sign=5e53a730\&sv=2)
2. Na aba **E-Doc**, selecione o seu formato (por exemplo, **EDI**).
3.  Clique em **Transformação** para visualizar ou editar.

    ![Separador EDI E-Doc que mostra os ficheiros Transformation e Preview XSLT além das entradas Extraction Paths e Purchase Order BOD](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZtaE4dZT9E1exWMZ5FCI%252Fimage.png%3Falt%3Dmedia%26token%3D787868b4-47b4-455e-9a26-112f692b91f3\&width=768\&dpr=4\&quality=100\&sign=460124f1\&sv=2)

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


    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9lddYJl2G4tzpdr9RD5F%252Fimage.png%3Falt%3Dmedia%26token%3Df7663f70-ef10-4e64-bbdc-41048ed8352a&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=36ce2b93&#x26;sv=2" alt="Painel de pré-visualização de Extraction paths com um seletor de documentos a mostrar 29 documentos e um botão Preview" width="375"></div>
* Insira o **ID do Documento** no campo e pressione **Testar**.
* A saída do **XML transformado resultante** será exibida.

Isso é especialmente útil para depurar mapeamentos XSLT e garantir que a estrutura final do XML atenda aos requisitos do seu formato.

![Vista de teste de Transformation XSLT mostrando a folha de estilos com seletores de valores EDI e o XML da ordem de compra transformado com linhas de pedido e totais](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWbwwmXgp6nRPIb1zBpgj%252Fimage.png%3Falt%3Dmedia%26token%3Dab5766f1-45bf-484e-9aa4-ab3059705591\&width=768\&dpr=4\&quality=100\&sign=46905864\&sv=2)

## 6. Tutorial em Vídeo

Um guia em vídeo para este tipo de arquivo está disponível na [página de Vídeos.](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/edi/edi-videos) Use-o para acompanhar a configuração, edição e visualização.

## Regras efetivas e ativação

As regras específicas da organização têm prioridade sobre as predefinições do formato eDoc detetado. Verifique a TRANSFORMATION ativa e verifique qual o nó que fornece invoice_type no XML transformado; o caminho depende do formato. Save guarda um rascunho; utilize a marca de verificação para o ativar após os testes. Uma Preview renderizada não comprova o tipo de documento guardado. Consulte o [guia de resolução de problemas de classificação](../credit-note-recognized-as-invoice.md) para obter informações sobre os códigos 381/261, os scripts posteriores e as precauções de reprocessamento.


<figure><img src="../../../../../../.gitbook/assets/site-all-edi-list-pt.png" alt="Formato EDI existente com os seus quatro atributos configurados."><figcaption><p>Formato EDI existente com os seus quatro atributos configurados.</p></figcaption></figure>

<figure><img src="../../../../../../.gitbook/assets/site-all-edi-transformation-pt.png" alt="Atributo TRANSFORMATION ativo: código-fonte XSLT para transformar o XML intermédio."><figcaption><p>Atributo TRANSFORMATION ativo: código-fonte XSLT para transformar o XML intermédio.</p></figcaption></figure>


As vistas mostram uma configuração e uma versão existentes. As definições variam consoante o tipo de documento e o formato. Valide as alterações num rascunho antes da ativação.

As imagens mostram as etapas em português e a versão ativa da configuração em modo só de leitura. Os nomes técnicos dos editores, os identificadores de atributos e o código de configuração mantêm-se como na versão ilustrada.
