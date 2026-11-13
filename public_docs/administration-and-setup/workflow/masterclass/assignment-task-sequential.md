---
description: "P1: distinguir atribuição, tarefa e aprovação sequencial"
---

# P1: distinguir atribuição, tarefa e aprovação sequencial

Uma **atribuição documental** define a responsabilidade atual. Uma **tarefa** é um trabalho separado. Uma **notificação** informa. Nenhuma corresponde já à aprovação de uma pessoa. Atribuir um grupo também não prova o consentimento de todos os membros.

Os cartões sequenciais recolhem destinatários e ordem de aprovação. O exemplo usa A com ordem 10 e B com 20. A finalização analisada começa pelo menor valor. A passagem para B segue a decisão do utilizador processada na aprovação; um nó Wait no designer não realiza essa passagem por si só.

Evite atribuição direta na mesma execução se espera o primeiro destinatário sequencial: a finalização pode ignorar essa primeira atribuição depois de o documento já ter sido atribuído diretamente. Configure `task_type`, prioridade, destinatário e `send_email` separadamente. Mantenha o e-mail desativado nos exercícios.

A aceitação de negócio requer A→aprovar→B→aprovar, rejeição por A, destinatário ausente e evento repetido. A rejeição deve impedir o export final; um destinatário não resolvido não deve parecer aprovação concluída. Verifique responsabilidade documental e tarefas separadamente. A simulação não prova uma passagem real entre utilizadores.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/pt.mp4" %}

**Vídeo:** Aprovação em duas etapas com tabelas de decisão · 2:54 · [Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/pt.vtt)

<details>

<summary>Transcrição</summary>

**Duas etapas, duas tabelas de decisão** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/pt.mp4#t=0.25)

Uma aprovação em duas etapas: primeiro os aprovadores que uma tabela de decisão retorna, depois um grupo final que sempre vem por último. Duas tabelas de decisão: uma retorna usuários, a outra um grupo.

**Uma cadeia: tabela, atribuição, tabela, atribuição** · [0:14](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/pt.mp4#t=14.216)

Coloque cada cartão de atribuição logo depois da sua própria tabela de decisão, em uma única cadeia: tabela, atribuição, tabela, atribuição. As duas tabelas guardam os retornos.

**Cada atribuição logo após sua tabela** · [0:27](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/pt.mp4#t=27.516)

Um Workflow guarda só o último resultado de uma tabela de decisão. Cada cartão de atribuição o lê quando é executado, então precisa rodar antes que a próxima tabela o substitua.

**As prioridades definem a ordem** · [0:38](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/pt.mp4#t=38.283)

A ordem das aprovações vem das prioridades, não da ordem dos cartões: o menor número recebe o documento primeiro. Dê ao grupo final o maior número.

**Teste: aprovadores, depois o grupo** · [0:49](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/pt.mp4#t=49.383)

O teste mostra todos os cartões com sucesso. O primeiro cartão de atribuição coloca os dois aprovadores na fila, o segundo o grupo final. No fim da execução, uma última atribuição entrega o documento ao primeiro deles.

**Lado a lado: não funciona** · [1:17](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/pt.mp4#t=77.45)

Este layout não funciona. Dois caminhos lado a lado parecem iguais, mas o Workflow os executa passo a passo: primeiro as duas tabelas, depois os dois cartões de atribuição.

**Aprovadores perdidos - sem erro** · [1:29](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/pt.mp4#t=89.183)

O teste executa primeiro as duas tabelas, depois os dois cartões de atribuição. Os dois leem o resultado da segunda tabela: o grupo entra na fila duas vezes e os aprovadores se perdem. Todos os cartões ainda mostram sucesso, nada avisa você. Use a cadeia.

**Um último aprovador fixo: prioridade 99** · [1:59](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/pt.mp4#t=119.383)

Em um Workflow Padrão, um aprovador fixo pode vir sempre por último: atribua os usuários da tabela e depois adicione um cartão que atribui um usuário com prioridade alta, por exemplo 99.

**Prioridades da tabela mais baixas** · [2:12](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/pt.mp4#t=132.783)

As prioridades da tabela precisam ficar abaixo desse número. Se a tabela não encontra ninguém, o Workflow para no cartão da tabela e ninguém é atribuído. Um usuário retornado pelos dois é consultado duas vezes.

**Conferir em um teste** · [2:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-two-step/v1/pt.mp4#t=145.95)

Um Workflow Padrão testa um cartão por vez, então teste os mesmos cartões em um Advanced Workflow. O primeiro cartão coloca os aprovadores da tabela na fila, o segundo adiciona o usuário fixo. As prioridades o deixam por último.

</details>

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
