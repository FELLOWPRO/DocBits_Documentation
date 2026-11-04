# Exemplos

Depois que o DocBits MCP estiver conectado (veja [Configuração e Instalação](setup-and-configuration.md)), você conversa com seu assistente em linguagem natural — ele escolhe as ferramentas certas do DocBits para você. Abaixo estão situações realistas do dia a dia dos clientes, com o tipo de pedido que você digitaria e as ferramentas que o assistente usa nos bastidores.

{% hint style="info" %}
Isso funciona da mesma forma no Claude Code, no Gemini CLI e no Codex — os pedidos são em linguagem natural, não comandos.
{% endhint %}

## Triagem da fila de trabalho

> *"Quantos documentos estão aguardando validação e de que tipos eles são?"*

Usa `get_pending_documents_count`, `get_pending_tasks_detail`, `get_top_document_types`. O assistente resume o backlog e pode detalhar qualquer documento.

> *"Mostre-me as faturas que deram erro hoje e diga-me por quê."*

Usa `search_documents` / `query_document_dashboard` + `get_document_logs` para encontrar os documentos com erro e explicar a falha a partir dos logs.

## Encontrar e inspecionar um documento

> *"Abra a fatura INV-2026-00231 e mostre os campos extraídos e os itens."*

Usa `get_document_by_name`, `get_extracted_fields`, `get_extracted_tables`. O assistente retorna os dados do cabeçalho e a tabela, e pode buscar a imagem da página com `get_page_image` se você quiser ver a origem.

> *"Pesquise todos os documentos do fornecedor 'ACME GmbH' do mês passado acima de €10.000."*

Usa `search_documents` / `query_document_dashboard` com filtros por campo.

## Corrigir e aprovar

> *"No documento 84213, defina o número do pedido como 4500098123 e a data de vencimento como 2026-07-15, e depois valide-o."*

Usa `update_document_fields` e depois `validate_document`. O assistente informa quaisquer erros de validação para que você possa corrigi-los.

> *"Valide e exporte o documento 84213 para o ERP, mas mostre-me antes a pré-visualização da exportação."*

Usa `get_export_preview` e, depois que você confirmar, `validate_and_export`.

## Corrigir uma extração de tabela

> *"A tabela de itens desta nota de entrega está sem duas linhas; extraia-a novamente com IA, oculte a coluna *Charges* e mantenha isso para este fornecedor."*

Usa `extract_table_ai` para executar novamente a tabela de IA no documento, `apply_ai_table_formatting` para ocultar a coluna e `save_table_training_rules` para armazenar o resultado para o fornecedor; a próxima nota de entrega dele será extraída da mesma forma. `get_extracted_tables` mostra a tabela final. Útil para documentos em que a extração baseada em regras perdeu linhas.

## Análises e relatórios

> *"Dê-me um resumo executivo deste mês: tendência de volume, taxa touchless e os 5 principais tipos de documento."*

Usa `get_executive_summary`, `get_volume_trends`, `get_success_rates`, `get_top_document_types`. Ótimo para uma atualização rápida para a gestão sem abrir o dashboard.

## Faturamento eletrônico (eDocs)

> *"Quais formatos de fatura eletrônica estão habilitados para nós, e este arquivo ZUGFeRD é extraído corretamente?"*

Usa `list_electronic_document_types` + `test_electronic_document` e, depois, `verify_electronic_documents` para confirmar os campos extraídos.

## Dados mestres e enriquecimento de fornecedores

> *"Adicione um novo fornecedor (nome, IVA, IBAN) aos dados mestres e depois execute novamente a consulta de fornecedor no documento 84500."*

Usa `upsert_vendor_master_data` + `trigger_supplier_lookup`.

## Alterações de configuração

> *"Habilite a extração de código QR para a nossa organização e confirme que a preferência foi definida."*

Usa `set_preference` (que limpa o cache automaticamente) + `get_preference` para confirmar.

> *"Liste os nossos tipos de documento e mostre as configurações de campos de 'Invoice'."*

Usa `list_document_types` + `get_field_settings`.

## Saúde e diagnóstico

> *"A API do DocBits e o worker de processamento estão saudáveis neste momento? Com qual usuário estou conectado?"*

Usa `check_api_health`, `check_celery_health`, `get_current_user`.

---

## Dicas

- **Seja específico sobre o documento** — um ID ou um nome de arquivo exato é o mais rápido; caso contrário, o assistente fará primeiro uma busca.
- **Peça uma pré-visualização antes de exportar** — `get_export_preview` permite confirmar o payload do ERP antes de `validate_and_export` enviá-lo.
- **As permissões se aplicam** — o assistente só pode fazer o que o seu usuário do DocBits ou a sua chave de API tem permissão para fazer. Aprovações e exportações respeitam o seu papel e as suas ACLs.
- **Cuidado com a produção** — o MCP atua sobre dados reais. Em ambientes de clientes/produção, prefira ações de leitura/pré-visualização e confirme antes de aprovar, exportar ou excluir.
