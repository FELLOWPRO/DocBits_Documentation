---
description: "P1: seguir a tabela de decisão até à atribuição"
---

# P1: seguir a tabela de decisão até à atribuição

Uma tabela de decisão liga campos de entrada a resultados tipados. O exemplo usa `cost_center=4711` e `total_amount`: revisor A até 1000, B acima de 1000. Crie duas regras sem sobreposição e use utilizadores válidos da organização de teste. O ficheiro do pacote descreve a configuração; não garante uma importação no editor.

Em **Decision Table has Returns** v3, ative `store_data=wf_store_data`. A v2 lê antes a opção booleana de armazenamento. A atribuição seguinte precisa de resultados guardados na mesma execução. Uma tabela executada com sucesso não confirma ainda um utilizador válido.

Um resultado de utilizador pode conter `output_type=user` e `value=101`; 101 é sintético e deve ser substituído por um utilizador de teste existente. Depois escolha **Assign document based on decision table** com `assignee_type=user`. A versão 2 analisada desta ação escolhe o último resultado correspondente. Várias correspondências não exigem automaticamente aprovação de todos os utilizadores.

Teste uma, nenhuma e várias correspondências, tipo incorreto, utilizador inválido e armazenamento desativado. Ligue ausência de correspondência e erros de atribuição a uma alternativa explícita. Defina ordem e política de correspondências; não transforme uma ordem ocasional em regra de negócio. Aceite a atribuição real no documento.

A condição de tabela de decisão chama realmente o serviço para avaliar a tabela. O teste não garante ausência de todos os efeitos; use apenas dados próprios de teste e examine as ações envolvidas.

## Cartões e parâmetros de exemplo

Os valores descrevem parâmetros de cartões, não um workflow completo importável. Substitua YOUR_* por seleções próprias de teste. O designer gere o ID oculto do chamador. Catálogo: Dev, DocFlow 2.10.38, 21 de outubro de 2026; confirme versões e permissões da organização.

### `condition_decision_tree_data` · v3

Identidade: `c40160ce-805f-4312-8726-51b0fd7af8ec`

| Parâmetro | Tipo / opções | Exemplo |
| --- | --- | --- |
| `decision_table` | `decision_table:str` | `"YOUR_TEST_DECISION_TABLE_ID"` |
| `boolean` | `boolean:bool` | `true` |
| `store_data` | `wf_store_data / wf_do_not_store_data` | `"wf_store_data"` |

### `action_assign_doc_based_on_decision_table` · v2

Identidade: `699912a7-2369-47e0-9092-8d027e13752a`

| Parâmetro | Tipo / opções | Exemplo |
| --- | --- | --- |
| `assignee_type` | `user / group` | `"user"` |

## Casos de teste de negócio

| Caso | Entrada / configuração | Resultado esperado |
| --- | --- | --- |
| DT-01 | 4711; 1000; store_data=wf_store_data | USER_A |
| DT-02 | 4711; 1000.01; store_data=wf_store_data | USER_B |
| DT-03 | sem resultado / utilizador inválido / tipo incorreto | Percurso alternativo |
| DT-04 | returns=[USER_A, USER_B]; assign v2 | USER_B |
| DT-05 | store_data=wf_do_not_store_data | sem resultado guardado para atribuição |

## Provas e limites

Parâmetros e comportamento foram comparados com o catálogo Dev e o código analisado. Os casos de negócio são uma orientação de aceitação. Não foram feitas aprovações pessoais, alterações reais nem entregas neste capítulo.

[Continuar a aprender](../workflow-learning-path.md) · [Pacote de formação](../workflow-training-kit.md)
