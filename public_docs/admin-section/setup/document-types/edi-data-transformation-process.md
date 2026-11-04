---
layout:
title:
visible: true
description:
visible: true
tableOfContents:
visible: true
outline:
visible: true
pagination:
visible: true
---

# Processo de Transformação de Dados EDI

####

<figure><img src="../../../.gitbook/assets/docbits_docbits_image_4.png" alt="DocBits DocBits Imagem 4"><figcaption></figcaption></figure>

#### Passo 1: Descritor de Estrutura

* **Formato**: JSON
* **Propósito**: Este passo envolve a definição da estrutura dos dados EDI. Isso inclui a especificação de segmentos como `SAC`, `N1` e `PO1`, e detalha os campos contidos em cada segmento. Para segmentos que contêm estruturas aninhadas, são definidos loops para organizar adequadamente a hierarquia dos dados.
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
#### Passo 2: Transformação Usando XSLT

* **Formato**: XSLT
* **Propósito**: Este passo envolve a transformação dos dados JSON estruturados em um formato XML estruturado, adaptando especificamente a saída para atender aos requisitos para processamento ou integração posteriores. Essa transformação ajuda na extração de informações precisas, como tipos de confirmação, detalhes do pedido e elementos condicionais com base em valores específicos.
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
#### Passo 3: Visualização (Conversão HTML)

* **Formato**: XSLT (produzindo HTML)
* **Propósito**: Converte os dados XML do Passo 2 em um formato HTML para visualização dos dados transformados em um formato legível e visualmente atraente. O layout HTML inclui estilos para apresentação e estrutura os dados como pedidos de compra, detalhes do fornecedor e termos do pedido para uma visualização fácil.
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
#### Passo 4: Caminhos de Extração

* **Formato**: JSON
* **Propósito**: Especifica os caminhos JSON para extrair valores-chave dos dados XML produzidos no Passo 2. Esses caminhos são usados para recuperar pontos de dados específicos, como pedidos de compra e moeda, que são cruciais para o processamento subsequente e integração em outros sistemas.
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
Esta sequência atualizada garante um processo completo, transformando dados EDI brutos em informações estruturadas e acionáveis usando JSON para estruturação de dados, XSLT para transformação e visualização HTML, seguido por caminhos JSON para extração e integração de dados.
