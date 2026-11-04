---
description: "Percurso de principiante a especialista"
---

# Percurso de principiante a especialista

Percorra os níveis por ordem. Ler não basta: cada nível termina com configuração própria, expectativa verificável e provas. P0 evita erros fundamentais de execução; P1 aprofunda dados, decisões de negócio e integrações.

1. [Orientação e modelo de execução](#level-1)
2. [Primeira regra própria](#level-2)
3. [Campos, tipos e limites](#level-3)
4. [Regras de negócio e aprovações](#level-4)
5. [Controlo Advanced e subworkflows](#level-5)
6. [Cálculo, integração e exportação](#level-6)
7. [Alterações e operação especializada](#level-7)

## Pré-requisitos

Use uma organização própria de teste e um documento sintético. Confirme organização, função, licença workflow e autorização Advanced. Mantenha inativos os exercícios importados. Os JSON completos destinam-se a Advanced Test → Custom Data. Aprovações e integrações reais exigem utilizadores e destinos de teste específicos.

## 1. Orientação e modelo de execução <a id="level-1"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/pt.mp4" %}

[Abrir o vídeo com legendas em português e transcrição](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-01-admin/v1/pt.html).

**Exercício:** Explique organização, acesso, When–And–Then e diferença entre regra linear e grafo Advanced. Distinga filtro documental, evento, guardar e ativar.

**Critério de conclusão:** Explica quando a regra é considerada e que prova distingue simulação de execução documental.

Ler e construir: [Quando é executado o meu workflow?](workflow-execution-model.md) · [P0: mudar o estado e limitar novas execuções](masterclass/status-and-reentry.md).

## 2. Primeira regra própria <a id="level-2"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/pt.mp4" %}

[Abrir o vídeo com legendas em português e transcrição](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-02-admin/v1/pt.html).

**Exercício:** Crie When Invoice → And invoice_id = WF-TRAINING-001 → And total_amount > 1000 → Then wf_training_route = REVIEW. Mantenha inativa. Teste dados completos para 999, 1000 e 1000.01. Esta regra linear ainda não precisa de nó de controlo.

**Critério de conclusão:** REVIEW só é alcançado acima de 1000. Registe tipo, operador e saída escolhida. Trate a entrada ausente separadamente.

Ler e construir: [Caso Advanced: encaminhamento de faturas](advanced-workflow-case-study.md) · [Pacote de formação de workflows](workflow-training-kit.md).

## 3. Campos, tipos e limites <a id="level-3"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/pt.mp4" %}

[Abrir o vídeo com legendas em português e transcrição](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-03-admin/v1/pt.html).

**Exercício:** Verifique ausente, null, texto vazio, espaços, false, 0 e números em texto. Calcule tolerância com referência à encomenda e ao documento. Compare uma e todas as linhas efetivamente associadas.

**Critério de conclusão:** Explique verdadeiro, falso e erro a partir de valor, tipo, referência e dados. Nenhuma linha comparável não significa aprovação bem-sucedida.

Ler e construir: [P1: escolher Field is, Docfield is ou Compare two Fields](masterclass/field-conditions.md) · [P1: definir a referência de tolerâncias e comparação PO](masterclass/tolerances-and-po.md).

## 4. Regras de negócio e aprovações <a id="level-4"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/pt.mp4" %}

[Abrir o vídeo com legendas em português e transcrição](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-04-admin/v1/pt.html).

**Exercício:** Configure duas regras de montante sem sobreposição. Siga o resultado de utilizador guardado até à atribuição. Planeie A com ordem 10, B com 20, rejeição e alternativa.

**Critério de conclusão:** Distinga responsabilidade, tarefa, notificação e aprovação efetiva. Aceite a passagem a B apenas após decisão de A processada.

Ler e construir: [P1: seguir a tabela de decisão até à atribuição](masterclass/decision-table-routing.md) · [P1: distinguir atribuição, tarefa e aprovação sequencial](masterclass/assignment-task-sequential.md).

## 5. Controlo Advanced e subworkflows <a id="level-5"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/pt.mp4" %}

[Abrir o vídeo com legendas em português e transcrição](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-05-admin/v1/pt.html).

**Exercício:** Compare ALL, ANY e OR com duas verificações alcançadas. Examine um ramo não escolhido. Execute os sete casos v2 e teste Run Workflow com destino próprio inativo.

**Critério de conclusão:** Explique diferenças teste/escalonador, contagem de origens e erros. V2 termina sem OR bloqueado; confirme no destino uma chamada verde.

Ler e construir: [P0: ligar corretamente Wait ALL, Wait ANY e OR](masterclass/control-nodes.md) · [P0: compreender Run Workflow, condições e erros](masterclass/run-workflow.md) · [Caso Advanced: encaminhamento de faturas](advanced-workflow-case-study.md).

## 6. Cálculo, integração e exportação <a id="level-6"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/pt.mp4" %}

[Abrir o vídeo com legendas em português e transcrição](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-06-admin/v1/pt.html).

**Exercício:** Compare toda a tabela antes/depois, incluindo regex sem correspondência e divisão por zero. Defina a escrita efetiva dos resultados de integração. Planeie exportação após aprovação com configuração própria de teste.

**Critério de conclusão:** Prove valores posteriores, receção e processamento ERP separadamente. Não registe simulação ou pedido de exportação como entrega.

Ler e construir: [P1: calcular colunas e verificar dependências regex](masterclass/table-calculations.md) · [P1: verificar chamadas API e uso posterior das respostas](masterclass/api-response-contract.md) · [P1: escolher exportação, tarefas abertas e estado final](masterclass/export-lifecycle.md).

## 7. Alterações e operação especializada <a id="level-7"></a>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/pt.mp4" %}

[Abrir o vídeo com legendas em português e transcrição](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-learning-step-07-admin/v1/pt.html).

**Exercício:** Guarde exportação do workflow e versões antes de alterar. Repita positivos, negativos, erros, limites e segunda execução. Relacione o primeiro erro com entrada e configuração concretas.

**Critério de conclusão:** Consegue aceitar alterações, restaurar configuração e comparar nova execução com efeitos. Registe causa, correção e limites.

Ler e construir: [Diagnosticar problemas de workflow sistematicamente](workflow-troubleshooting.md) · [Compreender e configurar cartões de workflow](card-reference-standard.md).

## Verificar conhecimentos

| Pergunta | Resposta |
| --- | --- |
| false é vazio em Field is v2? | Sim; o número 0 e o texto "false" não são vazios. |
| Um teste OR verde garante a execução documental? | Não. Predecessores não alcançados diferem entre teste e escalonador analisado. |
| Run Workflow pode chamar um destino inativo? | Sim, na chamada explícita analisada. Confirme condições e resultado do destino. |
| HTTP 200 disponibiliza automaticamente api.response.cost_center? | Não. As ações analisadas não oferecem esse contrato automático de saída JSON. |
| Um teste verde prova receção da exportação? | Não. Execução documental, receção e processamento ERP exigem provas próprias. |

## Os cinco guias de apoio

Use ao longo dos exercícios: modelo de execução → caso reproduzível → pacote → diagnóstico → referência dos cartões. São materiais dos níveis, não cinco tarefas adicionais não verificadas.

1. [Quando é executado o meu workflow?](workflow-execution-model.md)
2. [Caso Advanced: encaminhamento de faturas](advanced-workflow-case-study.md)
3. [Pacote de formação de workflows](workflow-training-kit.md)
4. [Diagnosticar problemas de workflow sistematicamente](workflow-troubleshooting.md)
5. [Compreender e configurar cartões de workflow](card-reference-standard.md)

## Registo de conclusão

Use acceptance-record-template.json do pacote. Registe cenário, revisão, expectativa, observação e tipo de prova. Distinga teste Dev, verificação isolada do código, execução documental real, receção e processamento ERP. Deixe explicitamente abertos os passos não verificados.
