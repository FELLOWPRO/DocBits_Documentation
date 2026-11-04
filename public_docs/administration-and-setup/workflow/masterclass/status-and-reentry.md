---
description: "P0: mudar o estado e limitar novas execuções"
---

# P0: mudar o estado e limitar novas execuções

**Change Status to** atualiza o estado documental. Na versão 3, `trigger_docflow` controla se é pedido novo processamento de workflows. Defina-o explicitamente. Se faltar, o código usa `true`; as versões 1/2 não leem o parâmetro pelo mesmo percurso de execução. Confirme a versão guardada.

Comece com `validated_pending_approval` e `trigger_docflow=false`. O estado é uma opção técnica: um `pending_approval` inventado não o substitui. Advanced Test simula a alteração. Não prova a persistência do estado nem o processamento de uma execução seguinte pedida.

Um processo limitado verifica estado inicial e marcador de processamento, realiza a ação e passa ao estado seguinte. Um evento repetido já não deve cumprir a condição inicial. Contudo, duas execuções concorrentes podem ler o mesmo marcador antigo: tarefas e destinos de exportação precisam de controlo adicional de duplicados.

Na aceitação, compare primeira e segunda execuções reais: estado, processamento seguinte pedido e quantidade de tarefas ou registos de destino. Não alterne entre dois estados apenas para experimentar. Mudar o estado não concede uma aprovação cuja condição de negócio continua por cumprir.

## Cartões e parâmetros de exemplo

Os valores descrevem parâmetros de cartões, não um workflow completo importável. Substitua YOUR_* por seleções próprias de teste. O designer gere o ID oculto do chamador. Catálogo: Dev, DocFlow 2.10.38, 21 de outubro de 2026; confirme versões e permissões da organização.

### `staus_change` · v3

Identidade: `4e0d38a2-a0af-4c1c-b0c2-2f380d70d910`

| Parâmetro | Tipo / opções | Exemplo |
| --- | --- | --- |
| `trigger_docflow` | `trigger_docflow:bool` | `false` |
| `status` | `error / rejected / ready_for_validation / validated_pending_approval / approved_pending_second_approval / archived / finished / exported` | `"validated_pending_approval"` |

## Casos de teste de negócio

| Caso | Entrada / configuração | Resultado esperado |
| --- | --- | --- |
| STATUS-01 | v3; trigger_docflow=false | validated_pending_approval; trigger=false |
| STATUS-02 | v3; trigger_docflow=true | execução seguinte pedida ≠ concluída |
| STATUS-03 | v3; trigger_docflow: — | default=true |
| STATUS-04 | RUN-1 → RUN-2 | tasks=1; destination_records=1 |

## Provas e limites

Resultados selecionados de cartões e nós foram verificados com dados sintéticos em Advanced Test. As respostas estão no pacote. As ações documentais são simuladas e não provam execução persistida nem entrega externa.

[Continuar a aprender](../workflow-learning-path.md) · [Pacote de formação](../workflow-training-kit.md)
