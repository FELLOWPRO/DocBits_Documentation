---
description: "P1: escolher exportação, tarefas abertas e estado final"
---

# P1: escolher exportação, tarefas abertas e estado final

**Start Export** usa a via de exportação configurada. **Export with Export Configuration** executa uma configuração selecionada. A variante diferida coloca-a em fila para o export final no fim da execução atual. Colocar em fila não significa enviar automaticamente depois de futuras aprovações humanas.

As novas versões analisadas oferecem `status=finished` ou `status=exported`: finished fecha o documento; exported permite continuar a editar. Start Export permite escolher desde v4; exportação configurada e diferida desde v3. As anteriores usam finished. Nas novas, uma opção ausente também usa finished; um valor inválido é erro de configuração.

Com `ignore_pending_tasks=false`, verificam-se tarefas abertas. O serviço pode por isso recusar a exportação configurada imediata. Este cartão não prova retoma automática após conclusão posterior das tarefas. Defina um novo evento e procure registos já existentes no destino antes de reenviar. Ignorar tarefas não substitui a aprovação.

Ligue exportação apenas depois de verificar explicitamente uma condição de aprovação. A aceitação cobre tarefa aberta, concluída, aprovação ausente, receção no destino de teste e nova execução. Distinga pedido, receção e processamento ERP. O pacote não contém destinos reais; os seus testes não provam entrega.

## Cartões e parâmetros de exemplo

Os valores descrevem parâmetros de cartões, não um workflow completo importável. Substitua YOUR_* por seleções próprias de teste. O designer gere o ID oculto do chamador. Catálogo: Dev, DocFlow 2.10.38, 21 de outubro de 2026; confirme versões e permissões da organização.

### `export` · v4

Identidade: `757f30ca-ed60-4e04-8131-2779df17f019`

| Parâmetro | Tipo / opções | Exemplo |
| --- | --- | --- |
| `boolean` | `boolean:bool` | `true` |
| `status` | `finished / exported` | `"finished"` |

### `action_export_with` · v3

Identidade: `ebcd854d-68b3-4b5f-8d45-1bcf8c675b21`

| Parâmetro | Tipo / opções | Exemplo |
| --- | --- | --- |
| `export_configuration` | `export_configuration:int` | `"YOUR_TEST_EXPORT_CONFIGURATION_ID"` |
| `ignore_pending_tasks` | `ignore_pending_tasks:bool` | `false` |
| `status` | `finished / exported` | `"exported"` |

### `action_export_with_config_deferred` · v3

Identidade: `060ef4c8-625f-447c-83c9-2ca3f680d88d`

| Parâmetro | Tipo / opções | Exemplo |
| --- | --- | --- |
| `export_configuration` | `export_configuration:int` | `"YOUR_TEST_EXPORT_CONFIGURATION_ID"` |
| `ignore_pending_tasks` | `ignore_pending_tasks:bool` | `false` |
| `status` | `finished / exported` | `"finished"` |

## Casos de teste de negócio

| Caso | Entrada / configuração | Resultado esperado |
| --- | --- | --- |
| EXPORT-01 | status=finished | fechado |
| EXPORT-02 | status=exported | editável |
| EXPORT-03 | ignore_pending_tasks=false; pending_tasks>0 | recusa possível; retoma automática não demonstrada |
| EXPORT-04 | action_export_with_config_deferred | em fila ≠ recebido |
| EXPORT-05 | RUN-1 → RUN-2 | destination_records=1 |

## Provas e limites

Parâmetros e comportamento foram comparados com o catálogo Dev e o código analisado. Os casos de negócio são uma orientação de aceitação. Não foram feitas aprovações pessoais, alterações reais nem entregas neste capítulo.

[Continuar a aprender](../workflow-learning-path.md) · [Pacote de formação](../workflow-training-kit.md)
