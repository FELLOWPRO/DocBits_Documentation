# Exemplos

Consulte os prompts e o procedimento completo de diagnóstico, rascunho, ativação e reversão em [Configurar o DocBits com Claude ou Codex](../docbits-mcp/configuration-with-claude-or-codex.md). Os exemplos usam os argumentos atuais. Substitua todos os marcadores por valores da sua organização e forneça fontes completas com escape JSON correto.

## 1. Alterar uma regra Custom existente

Leia a `TRANSFORMATION` efetiva com `get_edoc_attribute_source`, usando a etiqueta exata do formato devolvida pela classificação:

```json
{
  "electronic_document_type": "<detected_type_from_response>",
  "attribute_name": "TRANSFORMATION",
  "doc_type_key": "INVOICE",
  "source": "effective"
}
```

Registe `attribute_id`, `active_value_id`, `active_version` e `value`. Leia `source: "default"` separadamente para comparar e o histórico com `list_edoc_attribute_versions`. Os passos seguintes pressupõem um atributo Custom existente da sua organização.

Teste o candidato completo sem o guardar com `preview_edoc_custom_xslt`. Use um documento já existente na mesma organização:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "candidate_value": "<complete_candidate_xslt>",
  "doc_id": "<test_document_id_in_this_org>"
}
```

O resultado é XML transformado para `TRANSFORMATION`, PDF para `PREVIEW` ou campos/tabelas para `EXTRACTION_PATHS`. A pré-visualização não seleciona um rascunho guardado nem testa scripts posteriores ou exportações.

Depois de rever diff e pré-visualização, volte a ler a fonte ativa e guarde um rascunho com `update_edoc_custom_attribute`. Indique explicitamente `activate: false`; o valor predefinido é `true`.

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "new_value": "<complete_reviewed_xslt>",
  "activate": false
}
```

Após testes na organização de teste e confirmação da alteração concreta, chame `activate_edoc_attribute_version`. `draft_id` é o ID do valor de versão. Volte a ler a fonte efetiva. Para reverter, use o `active_value_id` anterior na mesma chamada.

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "draft_id": "<value_id_of_reviewed_version>"
}
```

## 2. Quando não existe um atributo Custom

`create_edoc_custom_attribute` cria uma primeira versão imediatamente ativa, não um rascunho. Teste a nova personalização numa organização de teste ou use o fluxo suportado do editor DocBits. Não crie nem elimine personalizações de produção só para obter uma pré-visualização. Preserve mapeamentos necessários; não altere globalmente as regras predefinidas partilhadas.

## 3. Testar a configuração ativa

Chame `test_electronic_document` com o XML original codificado em base64:

```json
{
  "file_content_base64": "<base64_of_original_xml>",
  "file_name": "credit-note-test.xml"
}
```

Isto testa as regras ativas sem guardar um documento, não um rascunho inativo. MCP HTTP remoto não pode ler um `file_path` local do seu computador. `compare_edoc_extraction` compara apenas Extraction Paths e exige um atributo personalizado de caminhos de extração; não compara transformações.

`validate_all_edocs` testa sem persistência os ficheiros disponíveis no servidor. `verify_electronic_documents` carrega-os e processa-os, criando documentos. Nenhum comprova entrega ao ERP. Use amostras representativas, verifique separadamente campos/montantes guardados e exportação e não reinicie documentos históricos em massa.
