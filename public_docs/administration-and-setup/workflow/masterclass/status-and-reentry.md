---
description: >-
  Use o cartão Alterar status para de modo que uma alteração de status não
  volte a iniciar o mesmo Workflow.
---

# Alterar o status sem reiniciar o seu Workflow

Quando um documento recebe um novo status, o DocBits inicia os Workflows previstos para esse status. Entre eles pode estar o Workflow que acabou de alterar o status. Se as condições dele continuarem a ser cumpridas, volta a ser executado e cria uma segunda tarefa ou exportação.

Esta página mostra como configurar o seu Workflow para que cada documento passe por ele apenas uma vez.

## A definição que importa

O cartão [Alterar status para](../then/status/change-status-to.md) define o novo status. A sua definição **Fluxos de trabalho de gatilho** decide se esta alteração de status pode iniciar Workflows:

* **Falso:** nenhum Workflow é iniciado. Use este valor, a menos que outro Workflow deva continuar com o documento.
* **Verdadeiro:** o DocBits inicia os Workflows cujas condições correspondem ao documento no seu novo status. Entre eles pode estar o Workflow que fez a alteração.

A página do cartão descreve todos os status e as versões do cartão.

## Que Workflows são iniciados após uma alteração de status

Com **Fluxos de trabalho de gatilho** definido como **Verdadeiro**, o DocBits analisa todos os Workflows ativos e verifica as condições de cada um sobre o tipo e o status do documento, por exemplo um cartão **Status do documento**. Um Workflow é iniciado se o documento, com o novo status, corresponder às condições.

Um Workflow que não verifica o status corresponde a **qualquer** status. Por isso, quando ele próprio altera o status, o novo status volta a iniciá-lo.

Alterar um documento para o status que já tem não produz efeito: o status mantém-se e nenhum Workflow é iniciado.

## Exemplo: executado uma vez ou duas vezes

A regra: depois de o seu Workflow cumprir a sua tarefa, as condições dele já não podem ser cumpridas.

<figure><img src="../../../.gitbook/assets/status-change-runs-once-vs-twice-pt.png" alt="Dois workflows, ambos com Fluxos de trabalho de gatilho definido como Verdadeiro. À esquerda: a condição verifica se o tipo é Fatura e o status é Pronto para validação. Após a alteração para Aprovação pendente, a condição deixa de ser cumprida, o workflow não volta a ser iniciado, resultado 1 tarefa. À direita: a condição verifica apenas se o tipo é Fatura. O novo status inicia o workflow uma segunda vez, que cria uma segunda tarefa e volta a definir Aprovação pendente, o que não altera nada. Resultado 2 tarefas." width="800"><figcaption><p>O mesmo workflow com e sem condição de status</p></figcaption></figure>

À direita, o Workflow é executado uma segunda vez e cria uma tarefa duplicada. Só para aí porque a segunda alteração define um status que o documento já tem.

**Dois Workflows podem iniciar-se um ao outro.** Se um Workflow define **Aprovação pendente** e outro volta a pôr o documento em **Pronto para validação**, ambos com **Verdadeiro**, continuam a iniciar-se um ao outro. Dê a cada Workflow uma condição sobre o status de que parte e use **Verdadeiro** apenas onde for necessário.

## Configuração passo a passo

1. **Use a versão 3 de Alterar status para.** As versões anteriores não têm a definição **Fluxos de trabalho de gatilho** (consulte as versões do cartão em [Alterar status para](../then/status/change-status-to.md)).
2. **Verifique o status de partida.** Adicione o cartão **E** **Status do documento** (em **E → Status**) e defina-o como **É** **Pronto para validação**. Consulte [Condição de status de documento único](../and/status/single-document-status-condition.md). Se o status, por si só, não indicar se o passo já foi feito, verifique também um campo que o seu Workflow preenche quando termina.
3. **Adicione a ação**, por exemplo criar uma tarefa ou exportar o documento.
4. **Adicione Alterar status para** e escolha o status seguinte, por exemplo **Aprovação pendente**.
5. **Escolha Fluxos de trabalho de gatilho.** Comece com **Falso**. Escolha **Verdadeiro** apenas se outro Workflow deve continuar com o novo status.
6. **Experimente com um documento real.** Confirme que foi criada exatamente uma tarefa ou exportação e que o documento tem o novo status.

{% hint style="info" %}
Os testes no designer de Workflows apenas simulam a alteração de status. O status não é guardado e nenhum outro Workflow é iniciado. Para ver o comportamento real, use um documento real.
{% endhint %}

## Proteção integrada

O DocBits limita os danos quando Workflows se iniciam uns aos outros repetidamente:

* **Uma execução de Workflow de cada vez por documento.** As execuções para o mesmo documento esperam umas pelas outras, e cada execução vê o documento tal como a anterior o deixou.
* **Limite de execuções.** Por predefinição, o mesmo Workflow é executado no máximo 50 vezes no mesmo documento. A partir daí, o DocBits deixa de o iniciar para esse documento.

Estes limites acabam por parar a repetição, mas até lá podem já existir muitas tarefas ou exportações. O que a evita é uma condição sobre o status. Se um duplicado for um problema real, verifique-o também antes de agir, por exemplo se já existe uma tarefa aberta para o documento.

## Relacionado

* [Alterar status para](../then/status/change-status-to.md): o cartão, os seus status e versões
* [Condição de status de documento único](../and/status/single-document-status-condition.md): verificar o status do documento numa condição
* [Quando é executado o meu workflow?](../workflow-execution-model.md)
* [Visão geral do percurso de aprendizagem](../workflow-learning-path.md)
