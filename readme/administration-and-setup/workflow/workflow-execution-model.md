---
description: "Distinguir eventos, condições, ordem de execução, testes e ativação de workflows."
---

# Quando é executado o meu workflow?

Um workflow precisa de um motivo de execução e de condições correspondentes. **O tipo de documento é Fatura** seleciona documentos; não significa que qualquer alteração de uma fatura inicie automaticamente outra execução.

## Do evento à ação

1. Verifique a organização, as permissões e o módulo Workflow, além da habilitação Advanced quando necessária.
2. Identifique o motivo: processamento documental, chamada manual explícita ou acionador de evento suportado. Utilize apenas acionadores realmente disponíveis no catálogo da sua versão.
3. No Standard Workflow, When e todas as condições And têm de corresponder. Uma condição falsa interrompe essa sequência linear.
4. No Advanced Workflow, a entrada e as saídas de resultado ligadas determinam o percurso. Uma condição And falsa pode continuar por laranja; vermelho trata um erro de avaliação.
5. Verifique o resultado no local adequado: resposta do teste, execução persistida, documento ou sistema destinatário.

**Start** é uma entrada manual. O pacote utiliza When para Fatura e o número exato de formação para cumprir os requisitos da interface atual. Importe-o desativado e teste manualmente. Um teste manual bem-sucedido não comprova o acionamento automático por eventos do documento.

## Guardar, testar e ativar

| Estado | Significado |
| --- | --- |
| Rascunho local | A cópia no navegador não substitui guardar no servidor. |
| Guardado | A configuração existe. Verifique a ativação separadamente: guardar uma regra nova pode já ativá-la. |
| Teste Advanced | Avalia o grafo atual, incluindo alterações não guardadas. As ações documentais são simuladas. |
| Ativado | A regra pode ser considerada no evento correspondente. Teste esse evento separadamente. |

O Test Manager e a janela de teste Advanced são superfícies de execução diferentes. Comparar apenas o estado não confirma atribuição, notificação ou receção de uma exportação. Verifique os efeitos da superfície escolhida antes de usar documentos reais.

## Vários workflows e repetições

Os valores mais baixos da **ordem de execução** são processados primeiro. Por exemplo, o workflow 100 prepara um campo e o 200 verifica-o. Utilize valores distintos e confirme os dados efetivamente lidos numa nova execução. A posição de um cartão Advanced no canvas não determina a ordem.

**Change Status to → Trigger Workflows** pode iniciar outra execução. **Run Workflow** chama um workflow selecionado. Ambos exigem condições deliberadas; nenhum garante uma execução única. Limite tarefas e exportações pelo estado do processo e teste explicitamente uma segunda execução. Um indicador de conclusão, por si só, não protege em geral contra duplicados simultâneos.

Continue com o [caso Advanced](advanced-workflow-case-study.md), o [pacote de formação](workflow-training-kit.md) e o [diagnóstico](workflow-troubleshooting.md).

## WF-01: Exercício e aceitação

Registe evento, filtro, ativação e versão. Verifique duas execuções e ordem 100/200 com um campo seguinte realmente lido. Distinga pedido esperado e execução observada.

[Percurso](workflow-learning-path.md)
