---
description: "P1: distinguir atribuição, tarefa e aprovação sequencial"
---

# P1: distinguir atribuição, tarefa e aprovação sequencial

Uma **atribuição documental** define a responsabilidade atual. Uma **tarefa** é um trabalho separado. Uma **notificação** informa. Nenhuma corresponde já à aprovação de uma pessoa. Atribuir um grupo também não prova o consentimento de todos os membros.

Os cartões sequenciais recolhem destinatários e ordem de aprovação. O exemplo usa A com ordem 10 e B com 20. A finalização analisada começa pelo menor valor. A passagem para B segue a decisão do utilizador processada na aprovação; um nó Wait no designer não realiza essa passagem por si só.

Evite atribuição direta na mesma execução se espera o primeiro destinatário sequencial: a finalização pode ignorar essa primeira atribuição depois de o documento já ter sido atribuído diretamente. Configure `task_type`, prioridade, destinatário e `send_email` separadamente. Mantenha o e-mail desativado nos exercícios.

A aceitação de negócio requer A→aprovar→B→aprovar, rejeição por A, destinatário ausente e evento repetido. A rejeição deve impedir o export final; um destinatário não resolvido não deve parecer aprovação concluída. Verifique responsabilidade documental e tarefas separadamente. A simulação não prova uma passagem real entre utilizadores.

## Cartões e parâmetros de exemplo

Os valores descrevem parâmetros de cartões, não um workflow completo importável. Substitua YOUR_* por seleções próprias de teste. O designer gere o ID oculto do chamador. Catálogo: Dev, DocFlow 2.10.38, 21 de outubro de 2026; confirme versões e permissões da organização.

### `action_assign_doc_to_user_sequential` · v2

Identidade: `859b2ea5-27a9-41e4-b7f1-3cf8812b9343`

| Parâmetro | Tipo / opções | Exemplo |
| --- | --- | --- |
| `user` | `user:int` | `"YOUR_TEST_USER_ID"` |
| `value` | `value:int` | `10` |

### `action_create_task_for_user_sequential` · v2

Identidade: `548b3583-6a96-483f-8c66-7871d5b067fa`

| Parâmetro | Tipo / opções | Exemplo |
| --- | --- | --- |
| `description` | `description:str` | `"WF-TRAINING-001"` |
| `task_type` | `task / notification` | `"task"` |
| `priority` | `high / medium / low` | `"medium"` |
| `send_email` | `send_email:bool` | `false` |
| `value` | `value:int` | `20` |
| `user` | `user:int` | `"YOUR_TEST_USER_ID"` |
| `title` | `title:str` | `"WF-TRAINING-001"` |

## Casos de teste de negócio

| Caso | Entrada / configuração | Resultado esperado |
| --- | --- | --- |
| ASSIGN-01 | A:10; B:20 | A → Aprovar → B → Aprovar |
| ASSIGN-02 | A → Rejeitar | EXPORT=NO |
| ASSIGN-03 | recipient=∅ | Percurso alternativo |
| ASSIGN-04 | RUN-1 → RUN-2 | verificar duplicados |
| ASSIGN-05 | direct + sequential | verificar primeiro destinatário |

## Provas e limites

Parâmetros e comportamento foram comparados com o catálogo Dev e o código analisado. Os casos de negócio são uma orientação de aceitação. Não foram feitas aprovações pessoais, alterações reais nem entregas neste capítulo.

[Continuar a aprender](../workflow-learning-path.md) · [Pacote de formação](../workflow-training-kit.md)
