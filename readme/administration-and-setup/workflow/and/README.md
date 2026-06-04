---
description: Configuração das condições E nos fluxos de trabalho DocBits
---

# And

## Compreender os cartões "And"

### **Propósito dos cartões "And":**

* Os cartões **And** funcionam como cartões de condição que especificam critérios que têm de ser cumpridos para que o fluxo de trabalho continue. Atuam efetivamente como operadores lógicos "AND", ou seja, todas as condições especificadas nestes cartões têm de ser satisfeitas para que a ação seguinte seja acionada.

#### Categorias de cartões "And"

A partir das capturas de ecrã, é claro que estes cartões abrangem uma vasta gama de condições, que incluem:

* **Compare with Purchase Order**:
  * Condições relacionadas com a validação e comparação face a ordens de compra, tais como comparar datas de entrega, preços unitários ou diferenças de quantidade. São cruciais para garantir que as transações estão de acordo com os termos acordados.

<figure><img src="../../../.gitbook/assets/image (14) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Document Field**:
  * Envolvem condições baseadas em campos específicos dentro dos documentos, como caixas de verificação assinaladas, comparação de valores de campos ou garantir que um campo de documento cumpre uma tolerância especificada. Isto é particularmente importante para a integridade dos dados e verificações automáticas em formulários ou sistemas de gestão documental.

<figure><img src="../../../.gitbook/assets/image (15) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Date & Time:**
  * Condições baseadas em datas e horas

<figure><img src="../../../.gitbook/assets/image (17) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Document**:
  * Condições baseadas nas características do documento, como o tipo ou a associação a uma sub-organização específica. Estas condições podem orientar os fluxos de trabalho com base na categorização do documento ou no envolvimento de departamentos.

<figure><img src="../../../.gitbook/assets/image (18) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Logic**:
  * Condições lógicas que podem envolver avaliações como "Continuar com uma probabilidade de X%" ou a execução de pedidos HTTPS, que são vitais para integrações e tomada de decisões probabilística dentro dos fluxos de trabalho.

<figure><img src="../../../.gitbook/assets/image (19) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Status**:
  * Focando-se no estado dos documentos ou tarefas, estas condições garantem que apenas os itens em determinados estados acionam fluxos de trabalho específicos, o que é crucial para a gestão de processos orientada por estado.

<figure><img src="../../../.gitbook/assets/image (20) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Table**:
  * Envolvem condições baseadas em dados de tabelas, como a correspondência de padrões regex ou a comparação de valores dentro de uma tabela. Tais condições são essenciais para validar e manipular grandes conjuntos de dados.

<figure><img src="../../../.gitbook/assets/image (22) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Assignee**:
  * Condições baseadas nos responsáveis de tarefas ou documentos. Isto garante que as ações só são realizadas quando determinados utilizadores estão envolvidos, reforçando a responsabilização e a especificidade das tarefas.

<figure><img src="../../../.gitbook/assets/image (24) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Aplicação prática

Estes cartões "And" são configurados dentro do fluxo de trabalho para realizar verificações e validações que garantem que o processo cumpre rigorosamente as regras de negócio e os padrões de integridade de dados. Por exemplo:

* **Um fluxo de trabalho pode usar um cartão "And" para verificar se o valor total de uma fatura corresponde à ordem de compra antes de acionar o pagamento.**
* **Outro fluxo de trabalho pode usar um cartão "And" para garantir que um documento é revisto por membros específicos da equipa antes de avançar para a fase seguinte.**

### Conclusão

Os cartões "And" são um componente fundamental dos sistemas de fluxo de trabalho que exigem um controlo preciso da execução do processo com base em múltiplas condições. Garantem que cada passo de um fluxo de trabalho só avança quando todos os critérios necessários são plenamente cumpridos, automatizando assim árvores de decisão complexas dentro dos processos de negócio.

Compreender e configurar corretamente estes cartões é crucial para aproveitar todas as capacidades do seu sistema de gestão de fluxos de trabalho, de modo a aumentar a eficiência, a precisão e a conformidade nos processos da organização.
