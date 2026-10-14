# Exemplos

Exemplos de ponta a ponta que mostram como usar as ferramentas do eDocs MCP em conjunto.

## Exemplo 1: Criar uma Pré-visualização Personalizada para o XRechnung

Este exemplo percorre o ciclo de vida completo de uma regra PREVIEW personalizada:
1. Verificar quais regras já existem
2. Pré-visualizar o XSLT sem ativá-lo
3. Criar a regra personalizada
4. Atualizá-la para uma nova versão
5. Voltar ao padrão

### Passo 1: Verificar as personalizações existentes

Chame `list_edoc_custom_attributes`:

```json
{
  "electronic_document_type": "XRECHNUNG 2.1 CII",
  "doc_type_key": "INVOICE"
}
```

A resposta mostra duas listas. Se `custom` estiver vazia para o atributo `PREVIEW`, sua organização está usando atualmente a folha de estilo de pré-visualização padrão integrada.

### Passo 2: Testar o XSLT antes de criá-lo

Chame `preview_edoc_custom_xslt` com o ID de um atributo existente (use um padrão da resposta de `list`) e um arquivo XML de exemplo codificado em base64:

```json
{
  "attribute_id": "<attribute_id_from_list>",
  "file_content_base64": "<base64_encoded_xrechnung_xml>",
  "file_name": "test_invoice.xml"
}
```

Inspecione o resultado renderizado para verificar se o seu XSLT produz o resultado esperado antes de confirmá-lo.

### Passo 3: Criar a regra personalizada

Chame `create_edoc_custom_attribute`:

```json
{
  "electronic_document_type": "XRECHNUNG 2.1 CII",
  "attribute_name": "PREVIEW",
  "attribute_value": "<?xml version=\"1.0\"?><xsl:stylesheet xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\" version=\"2.0\">...</xsl:stylesheet>",
  "doc_type_key": "INVOICE"
}
```

Guarde o `attribute_id` da resposta. A partir desse momento, toda fatura XRechnung 2.1 CII processada pela sua organização usará a sua pré-visualização personalizada.

### Passo 4: Atualizar a regra com uma nova versão

Mais tarde, se quiser refinar o XSLT, chame `update_edoc_custom_attribute`:

```json
{
  "attribute_id": "<your_attribute_id>",
  "new_value": "<?xml version=\"1.0\"?><xsl:stylesheet ...><!-- improved version --></xsl:stylesheet>",
  "activate": true
}
```

Definir `activate: true` muda imediatamente para a nova versão. A versão anterior é preservada no histórico. Defina `activate: false` para salvar como rascunho e ativá-lo separadamente.

### Passo 5: Voltar ao padrão integrado

Se quiser voltar à pré-visualização padrão, chame `delete_edoc_custom_attribute`:

```json
{
  "attribute_id": "<your_attribute_id>"
}
```

A regra personalizada é removida e o sistema volta automaticamente à folha de estilo padrão compartilhada. Nenhum outro cliente é afetado.

---

## Exemplo 2: Personalizar os Caminhos de Extração para EDI

Sua organização recebe faturas EDI com um layout de campos fora do padrão. Este exemplo mostra como substituir os caminhos de extração para a sua organização.

### Passo 1: Verificar as regras atuais

```
list_edoc_custom_attributes
  electronic_document_type: "EDI"
  doc_type_key: "INVOICE"
```

Se você vir uma entrada `EXTRACTION_PATHS` em `default`, mas não em `custom`, sua organização herda as regras XPath compartilhadas.

### Passo 2: Criar seus caminhos de extração personalizados

Chame `create_edoc_custom_attribute` com o seu JSON de XPath ajustado:

```json
{
  "electronic_document_type": "EDI",
  "attribute_name": "EXTRACTION_PATHS",
  "attribute_value": "{\"invoice_id\": \"//Invoice/ID/text()\", \"invoice_date\": \"//Invoice/IssueDate/text()\", \"total_amount\": \"//Invoice/LegalMonetaryTotal/TaxInclusiveAmount/text()\"}",
  "doc_type_key": "INVOICE"
}
```

### Passo 3: Verificar com um teste de simulação (dry-run)

Chame `test_electronic_document` com um arquivo EDI de exemplo para confirmar que os caminhos de extração personalizados capturam os valores corretos:

```json
{
  "file_content_base64": "<base64_encoded_edi_xml>",
  "file_name": "sample_edi_invoice.xml"
}
```

A resposta inclui `extracted_fields` e um PNG `preview.image_base64` — inspecione ambos para verificar a correção antes de entrar em produção.

---

## Exemplo 3: Executar uma Verificação Completa de eDoc

Antes de publicar uma alteração, verifique se todos os fixtures de eDoc suportados continuam passando:

```
validate_all_edocs
  fixture_filter: "xrechnung*"
  limit: 0
```

A ferramenta executa todos os fixtures XRechnung no pipeline e relata aprovado/reprovado/aviso para cada fixture. Uma execução limpa confirma que as suas personalizações não quebraram outros tipos de documento.

Para testar rapidamente apenas um tipo:

```
verify_electronic_documents
  fixture_filter: "zugferd*"
  limit: 3
```

Isso envia até 3 fixtures ZUGFeRD, aguarda o processamento e verifica de ponta a ponta a classificação, a extração e a geração da pré-visualização.
