# Explicar e melhorar o Touchless com MCP

<!-- touchless-admin-video-v2-20261104:start -->
**Capítulo do vídeo (versão de revisão):** [Consultar números com MCP](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/pt.html#chapter=12).
<!-- touchless-admin-video-v2-20261104:end -->

Os fluxos de trabalho a seguir usam ferramentas realmente anunciadas pelo DocBits MCP. Distinga leitura e explicação de escrita. Verifique organização, função, tipo de documento, período e carimbo de data dos dados; não invente evidências ausentes.

<figure><img src="../../../.gitbook/assets/touchless-owned-po-price-pt.png" alt="Visão real em Dev de um PO fictício próprio: 10 × 9 = 90. Trata-se de uma comparação de origem para o diagnóstico MCP, não de uma captura de um cliente MCP nem de prova de extração ou processamento bem-sucedidos."><figcaption><p>Visão real em Dev de um PO fictício próprio: 10 × 9 = 90. Trata-se de uma comparação de origem para o diagnóstico MCP, não de uma captura de um cliente MCP nem de prova de extração ou processamento bem-sucedidos.</p></figcaption></figure>

## Explicar o Touchless por meio do MCP

> Explique o Pure Touchless, os resultados apenas com aprovação e a taxa AP combinada para faturas nos últimos 30 dias. Indique o numerador, o denominador, os documentos em andamento e excluídos, o escopo e o carimbo de data dos dados. Mantenha a correção da extração separada.

Use `touchless_get_summary` com `period: "30d"` e `doc_type: "INVOICE"`. Para um subprocesso, use somente campos e valores de segmento realmente retornados por `touchless_list_segments`. Compare o painel e o MCP com a mesma organização, tipo de documento, segmento e período; leia `data_as_of`.

**Contraexemplo verificado no Dev:** três faturas de teste recém-enviadas ainda estavam `IN_PROGRESS`. O resumo retornou `population.total: 3`, `population.in_progress: 3`, `population.eligible: 0` e `official_touchless_rate.ap_pct: null`. Nenhuma taxa era mensurável ainda. Isso não é 0% de precisão de extração nem 100% de Touchless. A elegibilidade do resumo aqui se refere à população concluída do KPI; um rastreamento individual pode mostrar ao mesmo tempo `eligible: true` e `bucket_final: false`.

Os exemplos MCP nestas cinco páginas usam ferramentas diretas do DocBits MCP verificadas no Dev. A organização e a função da sua conta conectada são aplicadas; a disponibilidade em outra interface ou em uma lista de permissões adicional de ferramentas não é comprovada por esse teste.

## FAQ

**O DocBits extraiu tudo corretamente. Por que a fatura é AP assisted?**
O Touchless mede o processo inteiro. Dados incorretos ou desatualizados do Infor podem exigir uma correção registrada ou um reinício manual mesmo com extração correta. Verifique separadamente a fatura original, os valores que o DocBits extraiu e os dados de origem importados.

**O AP assisted me diz se o trabalho foi causado pelo DocBits ou pelo Infor?**
Não. Ele registra a intervenção, não a responsabilidade. Use o rastreamento do documento e os dados do documento e da origem subjacentes para confirmar a causa.

**As taxas mostram um traço (—).** Nenhum documento alcançou um resultado final no período, ou foram medidos menos documentos do que o mínimo. Documentos que ainda estão em andamento não são contados.

**A aba está faltando.** Peça ao seu administrador para ativar o módulo e conceder à sua função a aba **Analytics dashboard**.

**Um documento é contado como tratado, mas desta vez passou sem ninguém.** Ele foi tratado em uma execução anterior (uma correção ou um reinício). A taxa conta o trabalho que aconteceu.

**Por que o número muda depois de algumas horas?** O ERP pode confirmar uma exportação horas depois de ela ter sido enviada. O resultado é recalculado a cada 15 minutos.

**A IA altera algo por conta própria?** Não. A IA escreve apenas explicações. Uma configuração só muda depois que um administrador a pré-visualiza e a aplica.

## Investigar divergências por meio do MCP

> Verifique o número do PO desta fatura, o status da importação e as regras de correspondência realmente ativas. Separe extração, importação desatualizada, dados de origem errados e configuração ausente. Não altere nada por enquanto.

1. Compare o original, `get_extracted_fields` e `get_extracted_tables` antes de afirmar que a extração está correta.
2. Use `get_po_sync_status` com `po_number: "TL20261104X1-PO02"` e `language: "en"`. O teste no Dev confirmou uma importação processada e um PO existente. Isso prova a chegada, não a correção do negócio nem o registro atual no Infor.
3. Use `touchless_get_document_trace` e `touchless_explain_po_match` com o mesmo `doc_id`. Leia o motor real, a versão da regra ativa, as colunas e as tolerâncias efetivas. Para um cluster realmente retornado, use o seu `issue_signature` em `touchless_get_po_match_evidence`.
4. Preserve as evidências ausentes: o nosso novo tipo de teste retornou `state: "none_published"` e `parse_error: "no published rule set"`, além de campos de extração vazios. Nenhum bloqueio de preço/quantidade nem correspondência bem-sucedida foi comprovado. Um fluxo de decisão genérico não substitui essas verificações ausentes.
5. Corrija a causa confirmada e verifique as novas faturas. A correção ou o reinício humano continua relevante após o sucesso; uma falha final do ERP tem precedência como exceção, e um documento inacabado está fora do denominador da taxa.

Para um caso completo, guarde o original, a extração anterior à correção, os valores de origem importados/atuais e o momento da importação, as regras reais, a ação de AP e o resultado final. Evidências ausentes permanecem em aberto.

## Ler as evidências por meio do MCP

> Inspecione esta fatura sem alterá-la. Compare o original, os campos atuais e as tabelas. Explique as etapas e execuções registradas e identifique as evidências históricas de extração ausentes.

| Ferramenta, usando o mesmo `doc_id` | Evidência e limite |
| --- | --- |
| `get_extracted_fields` | Valores atuais de cabeçalho e confiança; não é um instantâneo histórico |
| `get_extracted_tables` | Tabelas e linhas reais; não prova que coincidem com o original |
| `touchless_get_document_trace` | Resultados, intervenções, etapas e execuções registrados |
| `touchless_explain_pipeline` | Explicação do caminho de processamento evidenciado; não preenche evidências ausentes |

**Verificação negativa observada:** a nossa fatura de teste recente tinha uma etapa de header extraction `passed`, mas `extracted_field_count: 0`, oito campos obrigatórios vazios e nenhuma tabela. A validação de campos bloqueou com `REQUIRED_FIELD_MISSING`. O assistente deve investigar extração/configuração ausentes, em vez de afirmar uma extração correta a partir de uma etapa verde ou um bloqueio comprovado de preço do PO a partir de valores de origem diferentes.

### Uma ação MCP conta como intervenção humana?

A inspeção somente de leitura não altera uma fatura. Outras ferramentas MCP podem gravar campos, validar ou reiniciar. A classificação depende do evento registrado e de o seu autor ser uma pessoa ou uma conta de sistema. Uma chave de API pode agir como conta de sistema; "realizado por meio do MCP" por si só não prova nem uma intervenção humana nem Pure Touchless. Nunca use credenciais de sistema para ocultar retrabalho humano.

Após uma ação no documento, inspecione `human_touched`, `human_touch_source`, `human_restart_count`, `business_approval_touched`, o status final e as execuções. Apenas aprovação de negócio é diferente de uma correção salva, de uma validação manual ou de um reinício humano.

## Priorizar fornecedores e verificar uma melhoria duradoura por meio do MCP

> Classifique os fornecedores que mais perdem faturas Touchless. Separe erros de extração, divergências na origem importada e configurações de processo. Proponha uma ação e uma verificação de sucesso verificável para cada causa confirmada; não altere nada por enquanto.

1. Use `touchless_rank_supplier_opportunities` com `period: "30d"`, `doc_type: "INVOICE"`, `order_by_field: "lost_docs"`, `order_by_direction: "desc"`. Use `search` para um número ou nome de fornecedor; `limit` e `offset` paginam os resultados.
2. Passe o `supplier_key` retornado sem alterações para `touchless_diagnose_supplier`. Use `window: 30` para problemas atuais ou 90 para investigar problemas recorrentes.
3. Passe um `issue_signature` realmente retornado para `touchless_get_issue_cluster`. Revise os documentos de exemplo e as evidências ausentes antes de confirmar a causa. Não invente identificadores.
4. Use `touchless_get_recommendations` para explicar uma ação suportada. O ganho esperado é uma estimativa; clusters sobrepostos não devem ser simplesmente somados.
5. Verifique novas faturas comparáveis após a correção e a [medição de alterações](touchless-change-proposals.md). Faturas tratadas anteriormente não se tornam Pure Touchless retroativamente.

Para extração correta e PO desatualizados, corrija os dados de origem/importação. Para uma divergência entre original e extração, investigue a configuração da extração. Uma aprovação exigida por política é um resultado AP Touchless bem-sucedido separado. Uma classificação vazia não é prova de ausência de problemas: as nossas três faturas de teste em andamento ainda não produziram nenhum resultado de fornecedor classificado. Verifique o escopo, o carimbo de data dos dados, a identificação do fornecedor e o volume concluído.

## Pré-visualizar, aplicar e medir por meio do MCP

> Explique a causa confirmada e liste as propostas suportadas. Pré-visualize a alteração selecionada, o seu escopo e os seus riscos. Aplique apenas essa alteração escolhida e depois verifique a configuração salva, o histórico de alterações e o efeito mensurável.

| Etapa | Ferramenta e identificadores realmente retornados | O que comprova |
| --- | --- | --- |
| List | `touchless_list_change_proposals`, opcionais `issue_signature`, `window: "30d"`, `lang: "en"` | Propostas disponíveis; nenhuma configuração salva |
| Preview | `touchless_preview_change` com o `proposal_id` retornado e o `issue_signature` correspondente | Escopo concreto e um `preview_token` vinculado quando permitido |
| Apply selected change | `touchless_apply_change` com os mesmos IDs, `preview_token`, `overrides` e `window` | **Grava** a configuração suportada; uma resposta bem-sucedida retorna um `change_id` |
| Read effect | `touchless_verify_change` com esse `change_id` e o mesmo `window` | Medição antes/depois; ainda são necessários pelo menos 20 documentos concluídos elegíveis por período |

Copie IDs e tokens de respostas genuínas. Um token que pré-visualiza um valor não pode aplicar um valor diferente. Uma pré-visualização expirada, proibida ou incompleta não é evidência de uma alteração aplicada. Ferramentas de leitura e a aplicação não devem ser descritas como equivalentes. Esta tabela explica a sequência de ferramentas; não afirma que a demonstração executou uma proposta ou mediu um ganho.

**Exemplo de configuração:** após uma correção de configuração confirmada, inspecione o valor realmente salvo e as novas faturas. 52% antes e 61% depois é uma diferença observada de 9 pontos percentuais, não prova de que esta alteração sozinha a causou. **Exemplo de dados de origem:** um PO errado no Infor precisa de uma correção de negócio e de uma importação verificada. `touchless_apply_change` não é uma ferramenta genérica de escrita no Infor. Não amplie tolerâncias para encobrir dados de origem errados.

A captura do relatório mostra recomendações e impacto estimado, não aplicação ou reversão. Uma aplicação bem-sucedida precisa de uma resposta de sucesso e de uma entrada no histórico. O Undo só está disponível quando a proposta selecionada o suporta; verifique a configuração realmente restaurada. Recarregar o histórico não aplica uma configuração, e a reversão não elimina intervenções passadas nos documentos.

## Páginas relacionadas

* [Touchless Intelligence](./)
* [Métricas e cálculo](touchless-metrics.md)
* [Usar o painel](touchless-dashboard.md)
* [Exemplos práticos: preço e quantidade](touchless-examples.md)
* [Supplier Diagnosis e clusters de problemas](touchless-supplier-diagnosis.md)
* [PO Matching Diagnosis](touchless-po-matching-diagnosis.md)
* [Document Trace](touchless-document-trace.md)
* [Change Proposals e relatórios](touchless-change-proposals.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
