# E

## Compreensão dos Cartões "E"

### **Propósito dos Cartões 'E':**

* Os cartões **E** funcionam como cartões de condição que especificam critérios que devem ser atendidos para que o fluxo de trabalho prossiga. Eles atuam efetivamente como operadores lógicos "E", o que significa que todas as condições especificadas nesses cartões devem ser satisfeitas para que a ação subsequente seja acionada.

#### Categorias de Cartões 'E'

A partir das capturas de tela, fica claro que esses cartões abrangem uma ampla gama de condições, que incluem:

*   **Comparar com Ordem de Compra**:

* Condições relacionadas à validação e comparação com ordens de compra, como comparar datas de entrega, preços unitários ou diferenças de quantidade. Isso é crucial para garantir que as transações estejam alinhadas com os termos acordados.



<figure><img src="../../../.gitbook/assets/And1.png" alt=""><figcaption></figcaption></figure>

*   **Campo de Documento**:

* Esses envolvem condições baseadas em campos específicos dentro de documentos, como marcação de caixas de seleção, comparação de valores de campo ou garantia de que um campo de documento atenda a uma tolerância especificada. Isso é particularmente importante para integridade de dados e verificações automatizadas em formulários ou sistemas de gerenciamento de documentos.



<figure><img src="../../../.gitbook/assets/And2.png" alt=""><figcaption></figcaption></figure>

* **Documento**:
* Condições baseadas em características do documento, como tipo ou associação com uma sub-organização específica. Essas condições podem direcionar fluxos de trabalho com base na categorização de documentos ou envolvimento departamental.

<figure><img src="../../../.gitbook/assets/And3.png" alt=""><figcaption></figcaption></figure>

* **Lógica**:
* Condições lógicas que podem envolver avaliações como "Continuar com uma chance de X%" ou execução de solicitações HTTPS, que são vitais para integrações e tomada de decisões probabilísticas dentro de fluxos de trabalho.

<figure><img src="../../../.gitbook/assets/And4.png" alt=""><figcaption></figcaption></figure>

*   **Status**:

* Focando no status de documentos ou tarefas, essas condições garantem que apenas itens em determinados estados acionem fluxos de trabalho específicos, crucial para o gerenciamento de processos orientado por status.

<figure><img src="../../../.gitbook/assets/And5.png" alt=""><figcaption></figcaption></figure>

* **Tabela**:
* Esses envolvem condições baseadas em dados de tabela, como correspondência de padrões regex ou comparação de valores dentro de uma tabela. Tais condições são essenciais para validar e manipular grandes conjuntos de dados.

<figure><img src="../../../.gitbook/assets/And6.png" alt=""><figcaption></figcaption></figure>

*   **Responsável**:

* Condições baseadas em responsáveis por tarefas ou documentos. Isso garante que ações sejam tomadas apenas quando determinados usuários estão envolvidos, melhorando a responsabilidade e especificidade da tarefa.

<figure><img src="../../../.gitbook/assets/And7.png" alt=""><figcaption></figcaption></figure>

### Aplicação Prática

Esses cartões "E" são configurados dentro do fluxo de trabalho para realizar verificações e validações que garantem que o processo siga estritamente as regras de negócios e os padrões de integridade de dados. Por exemplo:

* **Um fluxo de trabalho pode usar um cartão 'E' para verificar se o valor total de uma fatura corresponde à ordem de compra antes de acionar o pagamento.**
* **Outro fluxo de trabalho poderia usar um cartão 'E' para garantir que um documento seja revisado por membros específicos da equipe antes de avançar para a próxima etapa.**

### Conclusão

Os cartões "E" são um componente fundamental de sistemas de fluxo de trabalho que exigem controle preciso sobre a execução do processo com base em múltiplas condições. Eles garantem que cada etapa de um fluxo de trabalho prossiga somente quando todos os critérios necessários são totalmente atendidos, automatizando assim árvores de decisão complexas dentro dos processos de negócios.

Compreender e configurar esses cartões corretamente é crucial para aproveitar ao máximo as capacidades do seu sistema de gerenciamento de fluxo de trabalho para aprimorar a eficiência, precisão e conformidade nos processos organizacionais.
