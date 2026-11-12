---
description: "Percurso de principiante a especialista"
---

# Percurso de principiante a especialista

Sete níveis levam do primeiro olhar ao designer de workflows até à responsabilidade por uma alteração num workflow em produção. Cada nível indica um objetivo, os passos que executa na sua própria organização de teste e um resultado que pode verificar. Percorra-os por ordem e construa cada exercício: cada nível assenta na configuração do anterior.

1. [Orientação e modelo de execução](#level-1)
2. [Primeira regra própria](#level-2)
3. [Campos, tipos e limites](#level-3)
4. [Regras de negócio e aprovações](#level-4)
5. [Controlo Advanced e subworkflows](#level-5)
6. [Cálculo, integração e exportação](#level-6)
7. [Alterações e operação especializada](#level-7)

## Antes de começar

* Uma organização de teste própria, com uma fatura sintética lá dentro. Nunca pratique com documentos de clientes.
* O seu papel, a licença de workflow e a permissão Advanced, verificados antes do nível 1.
* Os exercícios importados ficam inativos até os ter testado.
* Os dados JSON completos vão em **Advanced Test → Custom Data**.
* As aprovações e integrações reais precisam de utilizadores e destinos de teste próprios; um teste no designer não os substitui.

## 1. Orientação e modelo de execução <a href="#level-1" id="level-1"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/pt.mp4" %}

[Abrir o vídeo com legendas e transcrição em português](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/pt.html).

**Objetivo:** Saber o que inicia um workflow e o que um resultado de teste pode afirmar, ou não, sobre uma execução real.

1. Verifique a organização, o seu acesso, o módulo de workflow e a permissão Advanced.
2. Diga When–And–Then por palavras suas e explique depois onde termina uma regra linear e como um grafo Advanced segue, em vez disso, as saídas ligadas.
3. Distinga quatro coisas que se parecem no designer: o filtro de tipo de documento, o evento de execução, o guardar e o ativar.

**Critério de conclusão:** Consegue dizer quando uma regra é sequer considerada e que prova separa uma simulação de uma execução sobre um documento real.

**Aprofundamento:** [Quando é que o meu workflow é executado?](workflow-execution-model.md) · [Alterar o estado sem reiniciar o workflow](masterclass/status-and-reentry.md)

## 2. Primeira regra própria <a href="#level-2" id="level-2"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/pt.mp4" %}

[Abrir o vídeo com legendas e transcrição em português](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/pt.html).

**Objetivo:** Levar uma regra do designer até um resultado verificado, sem tocar num documento.

1. Crie-a no Advanced Builder: When Invoice → And invoice\_id = WF-TRAINING-001 → And total\_amount > 1000 → Then wf\_training\_route = REVIEW. Uma regra linear deste tamanho não precisa de nó de controlo.
2. Guarde-a e verifique na lista de regras se continua inativa, porque guardar uma regra nova já a pode ativar. O Advanced Test é uma superfície de execução à parte: avalia o grafo no construtor, não a regra ativada.
3. Execute o Advanced Test com dados completos para 999, 1000 e 1000.01. Anote por caso o tipo de campo, o operador e a saída escolhida, e acrescente um caso em que o montante falta por completo.

**Critério de conclusão:** REVIEW só é alcançado com 1000.01, um montante em falta aparece como erro e não como resultado normal abaixo do limite, e no fim a regra volta a estar desativada.

**Aprofundamento:** [Caso de negócio Advanced: encaminhamento de faturas](advanced-workflow-case-study.md) · [Kit de exercícios de workflow](workflow-training-kit.md)

## 3. Campos, tipos e limites <a href="#level-3" id="level-3"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/pt.mp4" %}

[Abrir o vídeo com legendas e transcrição em português](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/pt.html).

**Objetivo:** Saber o que uma condição compara de facto antes de confiar no resultado.

1. Teste a verificação de vazio contra um campo em falta, `null`, texto vazio, espaços, `false`, `0`, `"0"` e `"false"`, e anote quais contam como vazios.
2. Calcule duas vezes a mesma tolerância de 2 por cento: uma com a encomenda como referência (encomenda 100, documento 102.02) e outra com o documento como referência.
3. Alterne entre Any e All no cartão da encomenda e conte quantas linhas foram realmente comparadas.

**Critério de conclusão:** Explica verdadeiro, falso e erro a partir do valor, do tipo, da referência e dos dados existentes. Na versão 5 do cartão da encomenda, um documento sem linha comparável é um erro de dados e não uma aprovação bem-sucedida.

**Aprofundamento:** [P1: Field is, Docfield is e comparar dois campos](masterclass/field-conditions.md) · [P1: Tornar tolerâncias e referência da encomenda inequívocas](masterclass/tolerances-and-po.md)

## 4. Regras de negócio e aprovações <a href="#level-4" id="level-4"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/pt.mp4" %}

[Abrir o vídeo com legendas e transcrição em português](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/pt.html).

**Objetivo:** Enviar uma fatura à pessoa certa através de uma tabela de decisão e, depois, correr uma cadeia de aprovação que espera pela primeira pessoa revisora.

**Exercício 1: tabela de decisão com atribuição direta**

1. Crie uma tabela de decisão com duas regras que não possam coincidir ao mesmo tempo: revisora A até 1000, revisor B acima de 1000, com `cost_center=4711` e `total_amount`.
2. Em **Decision Table has Returns** versão 3, defina `store_data=wf_store_data`. Atribua o documento com **Assign document based on decision table** e `assignee_type=user`, usando utilizadores reais da sua organização de teste.
3. Teste uma correspondência, nenhuma, várias e um ID de utilizador inválido, e encaminhe as não correspondências e os erros de atribuição para um recurso explícito. Aceite a atribuição no próprio documento.

**Exercício 2: aprovação sequencial sem atribuição direta**

1. Crie uma segunda regra separada com os cartões sequenciais: o cartão de atribuição sequencial na posição 10 para a revisora A e depois o cartão de tarefa sequencial na posição 20 para o revisor B. Deixe a atribuição direta de fora nesta execução, porque a finalização verificada pode saltar o primeiro destinatário sequencial quando o documento já foi atribuído diretamente na mesma execução.
2. Aprove como A e verifique que B só recebe o documento depois da decisão processada de A; aprove depois como B.
3. Rejeite como A numa execução nova e confirme que a exportação não acontece. Teste em seguida o que acontece quando não é possível determinar nenhum destinatário.

**Critério de conclusão:** Distingue responsabilidade, tarefa, notificação e aprovação efetiva; A → aprovação → B → aprovação aconteceu nessa ordem; uma rejeição de A impediu a exportação; e um destinatário em falta não contou como aprovação concluída.

**Aprofundamento:** [P1: Seguir a tabela de decisão até à atribuição](masterclass/decision-table-routing.md) · [P1: Distinguir atribuição, tarefa e aprovação sequencial](masterclass/assignment-task-sequential.md)

## 5. Controlo Advanced e subworkflows <a href="#level-5" id="level-5"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/pt.mp4" %}

[Abrir o vídeo com legendas e transcrição em português](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/pt.html).

**Objetivo:** Juntar corretamente caminhos paralelos e entregar trabalho a outro workflow.

1. Compare ALL, ANY e OR em duas verificações realmente alcançadas: ALL precisa de uma saída correspondente de cada origem, ANY e OR precisam de uma, e verde mais laranja de uma origem continuam a contar como uma só origem.
2. Veja um ramo que a execução não seguiu, como no caso MERGE-04: o Advanced Test continua a avaliar a junção em espera, enquanto a execução normal a salta assim que um antecessor nunca chega.
3. Execute os sete casos do estudo de caso v2 (acima, abaixo, limite, logo acima, em falta, número inválido, outra fatura). Depois chame com Run Workflow um workflow seu inativo e abra o caminho no próprio destino.

**Critério de conclusão:** Explica a diferença do caso MERGE-04 entre teste e execução do passo 2, como as origens são contadas e para onde vai um erro. Uma chamada Run Workflow verde continua a exigir verificação no destino. V2 designa aqui a segunda versão do grafo do estudo de caso: o cartão de estado de cada caminho leva diretamente ao cartão de fecho comum, sem nó OR em espera.

**Aprofundamento:** [P0: Ligar corretamente Wait ALL, Wait ANY e OR](masterclass/control-nodes.md) · [P0: Compreender Run Workflow, condições de destino e erros](masterclass/run-workflow.md) · [Caso de negócio Advanced: encaminhamento de faturas](advanced-workflow-case-study.md)

## 6. Cálculo, integração e exportação <a href="#level-6" id="level-6"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/pt.mp4" %}

[Abrir o vídeo com legendas e transcrição em português](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/pt.html).

**Objetivo:** Calcular valores, recuperar um resultado de um sistema externo e exportar só depois de uma aprovação real.

1. Calcule uma coluna e compare a tabela toda antes e depois, incluindo uma linha em que a expressão regular não corresponde e uma divisão por zero.
2. Escreva o contrato de escrita de retorno com o sistema externo: que campo do documento recebe o resultado, que cartão ou extensão o escreve aí e como verifica depois o valor guardado. Um HTTP 200 por si só não é um resultado.
3. Planeie a exportação após a aprovação com a sua própria configuração e anote o que vai verificar no destinatário.

**Critério de conclusão:** Valores seguintes no campo, receção no destinatário e processamento no ERP têm cada um a sua prova. Uma simulação ou uma exportação em fila não é uma entrega.

**Aprofundamento:** [P1: Calcular tabelas e verificar a dependência de regex](masterclass/table-calculations.md) · [P1: Verificar a chamada à API e o reaproveitamento da resposta](masterclass/api-response-contract.md) · [P1: Variantes de exportação, tarefas abertas e estado de fecho](masterclass/export-lifecycle.md)

## 7. Alterações e operação especializada <a href="#level-7" id="level-7"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/pt.mp4" %}

[Abrir o vídeo com legendas e transcrição em português](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/pt.html).

**Objetivo:** Alterar um workflow que não construiu e conseguir desfazer a alteração.

1. Exporte o workflow e anote as versões dos cartões antes de tocar em alguma coisa.
2. Repita depois da alteração os casos positivos, negativos, de erro e de limite, mais uma segunda execução do mesmo caso.
3. Recue o primeiro erro até uma entrada e uma configuração concretas e mantenha a exportação guardada como caminho de volta.

**Critério de conclusão:** Consegue aceitar a alteração, restaurar a configuração guardada e comparar uma nova execução documental com provas. Anote a causa, a correção e os limites que permanecem.

**Aprofundamento:** [Diagnosticar erros de workflow de forma sistemática](workflow-troubleshooting.md) · [Compreender os cartões e configurá-los com fiabilidade](card-reference-standard.md)

## Verificar conhecimentos

| Pergunta | Resposta |
| --- | --- |
| `false` conta como vazio em Field is v2? | Sim. O número 0 e o texto "false" não estão vazios. |
| Um teste OR verde garante a execução documental? | Não. No caso verificado MERGE-04, um teste avalia a junção que uma execução documental salta quando um antecessor nunca chega. |
| O Run Workflow pode chamar um destino inativo? | Sim, na chamada explícita verificada. Verifique mesmo assim as condições do destino e o resultado. |
| Um HTTP 200 expõe automaticamente api.response.cost\_center? | Não. As ações verificadas não oferecem esse contrato automático de saída JSON. |
| Um teste verde prova a receção da exportação? | Não. Execução documental, receção no destinatário e processamento no ERP exigem provas separadas. |

## Registar o que aceitou

Descarregue `workflow-training-kit-v2.zip` do [kit de exercícios de workflow](workflow-training-kit.md), extraia-o e abra `acceptance-record-template.json`. É um registo em branco e não algo que se importe; o mesmo ZIP contém também os dados, as expectativas e as respostas de teste guardadas a que os níveis se referem.

Anote o que testou e como o sabe: o cenário, a configuração (hash da exportação do workflow, versões dos cartões), o que esperava, o que observou e que tipo de prova tem. Mantenha separados um teste no Advanced Test, uma verificação isolada da origem, uma execução sobre documento real, a receção no destinatário e o processamento no ERP, e deixe como abertos os passos que não testou.
