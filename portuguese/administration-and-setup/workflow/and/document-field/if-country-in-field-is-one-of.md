# Se o país no campo for um dos

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-364a45ddb67d-pt.png" alt="Campos do cartão na versão apresentada. Os campos ainda não estão configurados." width="563"><figcaption><p>Campos do cartão na versão apresentada. Os campos ainda não estão configurados.</p></figcaption></figure>

## **Propósito**

Este cartão de fluxo de trabalho foi concebido para avaliar se um país especificado, localizado num campo designado, faz parte de uma lista predefinida de países. Com base nesta avaliação, o fluxo de trabalho pode continuar com uma condição verdadeira ou falsa. Ajuda a automatizar processos em que as ações dependem do facto de o país estar listado num conjunto de países permitidos ou restritos.

## **Componentes do cartão:**

1. **Nome do campo**
   * **Descrição:** Especifica o campo do documento onde o nome ou código do país está armazenado.
   * **Detalhe:** Deve corresponder ao identificador exato do campo dos dados do país dentro do documento.
2. **Operador**
   * **Descrição:** Define se o país no campo tem de fazer parte de uma lista predefinida de países.
   * **Opções:**
     * **Is:** O país tem de estar incluído na lista de países especificados para que a condição seja verdadeira.
     * **Não é:** O país não pode estar incluído na lista de países especificados para que a condição seja verdadeira.
3. **Países**
   * **Descrição:** Especifica a lista de países com a qual o país selecionado será comparado.
   * **Detalhe:** Trata-se de uma lista de países separada por vírgulas. A comparação verifica se o país no campo está incluído nesta lista.
4. **Condição Continuar**
   * **Descrição:** Define o resultado da comparação. Se o país cumprir a condição, o fluxo de trabalho continua com o valor Boolean especificado.
   * **Opções:**
     * **True:** O fluxo de trabalho continua se a condição corresponder.
     * **False:** O fluxo de trabalho continua se a condição não corresponder.

## **Funcionalidade:**

* **Avaliação da condição:** O sistema avalia se o país especificado no campo faz parte da lista de países predefinidos. Esta avaliação verifica o nome ou código do país face à lista fornecida.
* **Execução da ação:**
  * **Condição Verdadeira:**\
    Se o país no campo fizer parte da lista de países especificada, o fluxo de trabalho continua com a condição verdadeira. Isto pode acionar ações adicionais, como encaminhar documentos para o departamento adequado, aplicar regras de processamento específicas ou ativar funcionalidades específicas de cada região.
  * **Condição Falsa:**\
    Se o país não corresponder à lista, o fluxo de trabalho continua com a condição falsa. Isto permite executar ações alternativas ou interromper o fluxo de trabalho consoante a configuração do sistema.

## **Configuração:**

* Os utilizadores configuram o cartão selecionando o campo do documento que contém o país e especificando a lista de países a verificar. O operador é depois escolhido a partir de uma lista pendente para definir se o país tem de fazer parte ou não da lista de países especificada. Por fim, os utilizadores definem a condição de continuação (verdadeira ou falsa), que determina o passo seguinte no fluxo de trabalho.

## **Conclusão:**

O cartão de fluxo de trabalho "Country in Field Comparison with List" é uma ferramenta valiosa para automatizar ações com base no facto de um país fazer parte de um grupo predefinido. Ao comparar os dados do país com uma lista de países permitidos ou restritos, este cartão melhora a eficiência do fluxo de trabalho e assegura que os processos do sistema seguem as regras geográficas corretas.

<!-- workflow-card-practical-example-20261021 -->

## Exemplo prático

**Quando usar:** Encaminhe faturas de dois países especificados.

**Configuração:** Selecione o campo do país, é um de, códigos de país `DE` e `FR` e continuação `true`.

**Resultado esperado e contra-exemplo:** `DE` passa; `US` não satisfaz a lista de países selecionados.

Esta é uma configuração ilustrativa e resultado esperado. Utilize campos, usuários e grupos configurados em sua organização de teste; não é uma afirmação de que este exemplo foi executado.
