# Document Type

<figure><img src="../../../../.gitbook/assets/image (16) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## Propósito:

Este cartão de fluxo de trabalho foi concebido para avaliar se um documento corresponde a um tipo específico. Ao verificar se o documento corresponde ao tipo indicado, os fluxos de trabalho podem continuar ou tomar ações alternativas com base nesta condição. Isto ajuda a automatizar processos em que o tipo de documento dita os passos seguintes no fluxo de trabalho.

## Componentes do cartão:

1. **Operador**
   * **Descrição**: Define se o documento deve ser do tipo especificado ou não.
   * **Opções**:
     * **Is**: O documento tem de corresponder ao tipo especificado para que a condição seja verdadeira.
     * **Is Not**: O documento não pode corresponder ao tipo especificado para que a condição seja verdadeira.
2. **Type**
   * **Descrição**: Especifica o tipo de documento a comparar.
   * **Detalhe**: Inclui uma variedade de tipos de documento, como "Invoice", "Purchase Order", etc., com base nos quais a condição (is/is not) será avaliada.

## Funcionalidade:

* **Avaliação da condição**: O sistema avalia se o tipo de documento no campo especificado corresponde à condição definida pelo operador. Compara o valor do campo com o tipo de documento fornecido.
* **Execução da ação**:
  * **Condição Verdadeira**: Se o tipo de documento corresponder ao tipo especificado (ou não, consoante o operador), o fluxo de trabalho prossegue com a condição verdadeira. Isto pode acionar ações como o processamento adicional do documento, o envio para aprovação ou a aplicação de regras específicas com base no tipo de documento.
  * **Condição Falsa**: Se o tipo de documento não corresponder ao tipo especificado, o fluxo de trabalho prossegue com a condição falsa. Isto pode acionar ações alternativas, como encaminhar o documento para um processo diferente ou interromper ações adicionais.

## Configuração:

* Os utilizadores configuram o cartão selecionando o campo do documento que contém o tipo de documento a partir de uma lista de campos disponíveis. De seguida, é selecionado o operador para definir se o documento tem de ser do tipo especificado ou não. Por fim, os utilizadores definem a condição de continuação (verdadeira ou falsa), que determina a ação seguinte com base no tipo de documento.

## Conclusão:

O cartão de fluxo de trabalho "Document Type Comparison" é essencial para garantir que os fluxos de trabalho prosseguem com base no tipo de documento que está a ser processado. Ao comparar o tipo de documento, ajuda as organizações a automatizar tarefas de encaminhamento e processamento de documentos, assegurando que os documentos são tratados de forma adequada com base no seu tipo.
