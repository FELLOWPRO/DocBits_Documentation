# Processo de transformação de dados EDI



<figure><img src="../../../.gitbook/assets/site-all-edi-list-pt.png" alt="Formato EDI existente com os seus quatro atributos configurados."><figcaption><p>Formato EDI existente com os seus quatro atributos configurados.</p></figcaption></figure>

O DocBits analisa a mensagem EDI original e converte-a em JSON através de um descritor de estrutura JSON. Depois, cria XML intermédio, aplica XSLT para produzir o XML padrão e utiliza esse XML para extrair campos e tabelas e gerar a pré-visualização.

Os exemplos abaixo são fragmentos ilustrativos, não configurações completas prontas a importar. Alguns omitem conteúdo ou contêm marcadores como `...`. Adapte-os e teste-os com a sua mensagem EDI real, o XML intermédio e o resultado transformado; mantenha os identificadores de campos exigidos pela sua configuração.

## Passo 1: Descrever a estrutura EDI

O descritor de estrutura JSON define segmentos como SAC, N1 e PO1, os respetivos campos e os ciclos aninhados. Determina como a mensagem EDI original é analisada para obter JSON estruturado.

```json
{
  "SAC": {"fields": ["SAC", "DTM", "TX1", "TD5"]},
  "N1": {"fields": ["N1", "N2", "N3", "N4", "PER"]},
  "PO1": {
    "fields": ["PO1", "REF"],
    "loops": {
      "SAC": {"fields": ["SAC", "TX1", "DTM"]}
    }
  }
}
```

## Passo 2: Transformar o XML intermédio com XSLT

O DocBits converte o JSON analisado em XML intermédio antes de aplicar a folha de transformação. O XSLT lê este XML intermédio, não o JSON diretamente, e produz a estrutura XML padrão para o processamento seguinte. O exemplo seleciona dados de confirmação e condições a partir de nós XML.

```xml
<xsl:stylesheet version="1.1" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml" />
    <xsl:template match="/">
        <ORDER_CONFIRMATION>
            <ACKNOWLEDGEMENT_TYPE>
                <xsl:value-of select="//BAK/VALUE_2/text()" />
            </ACKNOWLEDGEMENT_TYPE>
            <ACKNOWLEDGEMENT_TYPE_DESCRIPTION>
                <xsl:choose>
                    <xsl:when test="//BAK/VALUE_2='AD'">With detail, no change</xsl:when>
                    <xsl:when test="//BAK/VALUE_2='AC'">With detail and change</xsl:when>
                    <xsl:otherwise>Unknown</xsl:otherwise>
                </xsl:choose>
            </ACKNOWLEDGEMENT_TYPE_DESCRIPTION>
            <!-- Additional fields and conditions are similarly transformed -->
        </ORDER_CONFIRMATION>
    </xsl:template>
</xsl:stylesheet>

```

## Passo 3: Criar uma pré-visualização HTML

Uma folha de estilo de pré-visualização converte em HTML o XML transformado no passo 2. Adapte a apresentação e as ligações de dados ao tipo de documento e verifique se a pré-visualização representa corretamente os dados transformados.

```xml
<xsl:stylesheet version="1.1" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="html" />
    <xsl:template match="/">
        <html lang="en">
            <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Preview of Transformed EDI Data</title>
                <!-- Styles and head elements -->
            </head>
            <body>
                <div>
                    <!-- HTML structure mimicking an invoice or other document type, with data bindings from the transformed XML -->
                </div>
            </body>
        </html>
    </xsl:template>
</xsl:stylesheet>


```

## Passo 4: Configurar a extração com XPath

A configuração de extração é guardada em JSON, mas os seus caminhos são expressões XPath avaliadas sobre o XML transformado no passo 2. Os caminhos de campos selecionam valores; o caminho de linhas de uma tabela seleciona linhas, e os caminhos de colunas selecionam valores dentro de cada linha. Não são expressões JSONPath.

```json
{
  "fields": {
    "purchase_order": "//ORDER_CONFIRMATION/PURCHASE_ORDER/text()",
    "currency": "//ORDER_CONFIRMATION/CURRENCY/text()",
    ...
  },
  "tables": [
    {
      "name": "ORDER_CONFIRMATION_TABLE",
      "row_path": "//ORDER_CONFIRMATION/ORDER_LINES/ORDER_LINE",
      "columns": [
        {"name": "POSITION", "path": "POSITION/text()"},
        ...
      ]
    }
  ]
}
```

O fluxo completo é: EDI original → JSON estruturado → XML intermédio → XML padrão através de XSLT → extração de campos e tabelas com XPath e pré-visualização HTML. Valide o resultado e os valores extraídos com mensagens representativas antes de utilizar uma configuração em produção.


As vistas mostram uma configuração e uma versão existentes. As definições variam consoante o tipo de documento e o formato. Valide as alterações num rascunho antes da ativação.

As imagens mostram as etapas em português e a versão ativa da configuração em modo só de leitura. Os nomes técnicos dos editores, os identificadores de atributos e o código de configuração mantêm-se como na versão ilustrada.
