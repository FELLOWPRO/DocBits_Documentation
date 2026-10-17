# eDocs MCP

A API do DocBits expõe um servidor **Model Context Protocol (MCP)** com ferramentas para inspecionar e personalizar o processamento de documentos eletrônicos (eDoc). Qualquer cliente compatível com MCP — Claude Code, Claude Desktop ou integrações personalizadas — pode se conectar e usar essas ferramentas.

## O Que Você Pode Fazer?

Com as ferramentas do eDocs MCP você pode:

- **Inspecionar** como qualquer tipo de documento eletrônico é classificado e quais regras de extração se aplicam
- **Testar** documentos em todo o pipeline de processamento sem gravar no banco de dados
- **Criar regras personalizadas** para a sua organização — pré-visualizações XSLT, caminhos de extração, transformações
- **Atualizar** uma regra personalizada com uma nova versão (com ou sem ativação imediata)
- **Excluir** uma regra personalizada para voltar ao padrão integrado
- **Verificar** se todos os fixtures de eDoc suportados são processados corretamente

## Modelo de Permissões

O DocBits vem com uma biblioteca de regras padrão integradas, compartilhadas por todos os clientes. Esses padrões usam o ID de organização reservado `00000000-0000-0000-0000-000000000000`.

**As regras padrão são imutáveis via MCP.** Cada ferramenta de gravação verifica o ID da sua organização antes de fazer qualquer requisição. Se ele corresponder à organização padrão, a operação é rejeitada imediatamente — nenhuma chamada à API é feita.

Os clientes só podem criar, alterar ou excluir regras **dentro da sua própria organização**. Quando existe uma regra personalizada para a sua organização, ela tem precedência sobre a padrão. Excluir uma regra personalizada restaura automaticamente o comportamento padrão.

```
Your org rule  ──► used if present
      │
      ▼ (if absent)
Default rule   ──► built-in, immutable via MCP
```

## Visão Geral das Ferramentas

### Inspeção (somente leitura)

| Ferramenta | Descrição |
|------|-------------|
| `test_electronic_document` | Simulação (dry-run) do pipeline completo de eDoc — classificação, extração, pré-visualização — sem gravar |
| `list_electronic_document_types` | Lista todos os tipos de eDoc suportados com o estado da configuração |
| `get_extraction_rules` | Mostra as regras XPath usadas para extrair os campos de um determinado tipo de documento |
| `get_extracted_fields` | Obtém os campos de cabeçalho extraídos de um documento processado |
| `get_extracted_tables` | Obtém os itens extraídos de um documento processado |
| `get_preview_pdf` | Recupera o PDF de pré-visualização renderizado por XSLT de um documento |
| `get_preview_image` | Recupera uma imagem de página renderizada de um documento processado |
| `extract_edoc_table` | Extrai um arquivo XML/EDI que você informa e retorna os campos como uma tabela plana, junto com a regra que produziu cada um |
| `compare_edoc_extraction` | Compara a extração padrão e a sua extração personalizada (e, opcionalmente, uma regra candidata) em um documento |

### Personalização (no escopo da organização, organização padrão bloqueada)

| Ferramenta | Descrição |
|------|-------------|
| `list_edoc_custom_attributes` | Lista as substituições personalizadas da sua organização em comparação com os padrões integrados para um tipo de documento |
| `create_edoc_custom_attribute` | Cria uma nova regra personalizada (EXTRACTION_PATHS, TRANSFORMATION ou PREVIEW) |
| `update_edoc_custom_attribute` | Adiciona uma nova versão de uma regra personalizada, opcionalmente ativando-a imediatamente |
| `delete_edoc_custom_attribute` | Exclui uma regra personalizada — o sistema volta automaticamente ao padrão |
| `preview_edoc_custom_xslt` | Simulação (dry-run) de uma transformação XSLT em um documento XML antes de ativá-la |
| `get_edoc_attribute_source` | Obtém o código-fonte editável de um atributo (PREVIEW, EXTRACTION_PATHS, TRANSFORMATION) para alterá-lo |
| `list_edoc_attribute_versions` | Histórico de versões de um atributo personalizado: rascunhos e a versão ativa |
| `activate_edoc_attribute_version` | Ativa uma versão ou rascunho específico (é assim que se faz um rollback) |
| `delete_edoc_attribute_draft` | Exclui um rascunho que nunca foi ativado |

### Verificação

| Ferramenta | Descrição |
|------|-------------|
| `verify_electronic_documents` | Envia fixtures e verifica de ponta a ponta a classificação, a extração e a pré-visualização |
| `validate_all_edocs` | Executa todos os fixtures de eDoc em um pipeline de simulação (dry-run) e relata os problemas |

## Tipos de Atributos

Cada regra personalizável tem um tipo e um formato específicos:

| Nome do atributo | Formato | Finalidade |
|----------------|--------|---------|
| `EXTRACTION_PATHS` | JSON | Expressões XPath que mapeiam nós XML para campos do DocBits |
| `TRANSFORMATION` | XSLT | Folha de estilo aplicada ao XML antes da extração |
| `PREVIEW` | XSLT | Folha de estilo que renderiza a pré-visualização em PDF legível por humanos |
| `STRUCTURE_DESCRIPTOR` | JSON | Mapa de estrutura somente para documentos EDI |

A ferramenta `create_edoc_custom_attribute` infere automaticamente o formato correto a partir do nome do atributo.

## Início Rápido

### Liste o que a sua organização personalizou

```
list_edoc_custom_attributes
  electronic_document_type: "XRECHNUNG 2.1 CII"
```

Retorna duas listas: `custom` (as substituições da sua organização) e `default` (as regras compartilhadas que você herda).

### Crie uma pré-visualização personalizada para o XRechnung

```
create_edoc_custom_attribute
  electronic_document_type: "XRECHNUNG 2.1 CII"
  attribute_name: "PREVIEW"
  attribute_value: "<xsl:stylesheet ...>...</xsl:stylesheet>"
```

Retorna o novo `attribute_id` — guarde-o para atualizações e exclusão.

### Atualize uma regra personalizada existente

```
update_edoc_custom_attribute
  attribute_id: "069cd17c-673c-7c94-8000-b512417eefe3"
  new_value: "<xsl:stylesheet ...>...</xsl:stylesheet>"
  activate: true
```

Cria uma nova versão e a ativa. A versão anterior é mantida no histórico.

### Volte ao padrão

```
delete_edoc_custom_attribute
  attribute_id: "069cd17c-673c-7c94-8000-b512417eefe3"
```

Remove a substituição personalizada. O sistema volta imediatamente à regra padrão integrada.

## Regras de Segurança

| Ação | Permitida |
|--------|---------|
| Ler as regras padrão | ✅ Sim |
| Criar uma regra personalizada para a sua organização | ✅ Sim |
| Atualizar uma regra personalizada da sua organização | ✅ Sim |
| Excluir uma regra personalizada da sua organização | ✅ Sim |
| Modificar ou excluir as regras padrão | ❌ **Nunca** — bloqueado na camada MCP |

Tentar gravar em `00000000-0000-0000-0000-000000000000` retorna:

```json
{
  "error": true,
  "blocked": true,
  "detail": "Writing to the default org is forbidden via MCP. Default rules are immutable and shared across all customers."
}
```

## Regras efetivas e ativação

Se uma nota de crédito eletrónica aparecer como Invoice, siga o [guia de resolução de problemas de classificação](../../administration-and-setup/settings/global-settings/document-types/edi/credit-note-recognized-as-invoice.md). Este explica como verificar a origem personalizada ou predefinida efetivamente utilizada, os códigos de tipo, os Extraction Paths e a ativação segura.
