---
description: "P0: compreender Run Workflow, condições e erros"
---

# P0: compreender Run Workflow, condições e erros

**Run Workflow** chama um workflow pelo ID e espera pela execução. O nome não basta. O designer gere o ID oculto do workflow chamador; não o altere como parâmetro de negócio. O documento atual é passado ao destino, cuja entrada e condições são novamente avaliadas.

A chamada explícita analisada também chega a um destino **inativo**. Inativo não significa inacessível através de Run Workflow. Os testes Dev abrangeram um destino próprio inativo, autochamada e ID desconhecido. Os dois últimos seguiram Error. Os limites internos de recursão e encadeamento não substituem regras para limitar chamadas repetidas.

Distinga variáveis de organização e campos documentais dos resultados locais de uma execução. A chamada não transmite automaticamente todos os resultados de tabelas de decisão ou HTTP do processo principal. Defina os campos necessários e verifique os valores reais no cartão seguinte.

Uma chamada verde não confirma todas as condições de negócio do destino: um resultado Advanced sem erro técnico é tratado como chamada bem-sucedida e pode incluir `failed_condition`. Examine o percurso escolhido e o efeito. Trate erros explicitamente no chamador; evite A→B→A e chamadas repetidas ao mesmo destino.

## Cartões e parâmetros de exemplo

Os valores descrevem parâmetros de cartões, não um workflow completo importável. Substitua YOUR_* por seleções próprias de teste. O designer gere o ID oculto do chamador. Catálogo: Dev, DocFlow 2.10.38, 21 de outubro de 2026; confirme versões e permissões da organização.

### `run_workflow` · v2

Identidade: `bb773bc7-b258-49b9-b0e9-b1c28ac227cb`

| Parâmetro | Tipo / opções | Exemplo |
| --- | --- | --- |
| `hidden_workflow_id` | `hidden_workflow_id` | `"MANAGED_BY_DESIGNER"` |
| `workflow` | `workflow:str` | `"YOUR_TARGET_WORKFLOW_ID"` |

## Casos de teste de negócio

| Caso | Entrada / configuração | Resultado esperado |
| --- | --- | --- |
| CHILD-01 | enabled=false; workflow=VALID_ID | call=success |
| CHILD-02 | caller_id=target_id | error |
| CHILD-03 | workflow=UNKNOWN_ID | error |
| CHILD-04 | Advanced target=failed_condition | a chamada pode ter sucesso; verificar destino |

## Provas e limites

Resultados selecionados de cartões e nós foram verificados com dados sintéticos em Advanced Test. As respostas estão no pacote. As ações documentais são simuladas e não provam execução persistida nem entrega externa.

[Continuar a aprender](../workflow-learning-path.md) · [Pacote de formação](../workflow-training-kit.md)
