# Compare Campo com tolerâncias

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-4ee291b0848d-pt.png" alt="Campos do cartão na versão apresentada. Os campos ainda não estão configurados." width="563"><figcaption><p>Campos do cartão na versão apresentada. Os campos ainda não estão configurados.</p></figcaption></figure>

## **Propósito:**

Este cartão de fluxo de trabalho foi concebido para comparar o valor de um campo com um valor de referência especificado, permitindo tolerâncias. Possibilita um processamento condicional preciso em fluxos de trabalho onde pequenos desvios são aceitáveis, sendo ideal para cenários como garantia de qualidade, análise financeira ou ações baseadas em limiares.

## **Componentes do cartão:**

1. **Nome do campo**
   * **Descrição:** O campo a avaliar na comparação.
   * **Detalhe:** Tem de corresponder ao identificador exato do primeiro campo dentro do documento.
2. **Operador de comparação**
   * **Descrição:** Especifica como o valor do campo selecionado será comparado com o valor de referência.
   * **Opções:**
     * **Igual a (=):** Verifica se o valor do campo corresponde exatamente ao valor de referência.
     * **Não é igual (≠):** Verifica se o valor do campo não corresponde ao valor de referência.
     * **Maior que (>):** Verifica se o valor do campo é superior ao valor de referência.
     * **Maior ou Igual (≥):** Verifica se o valor do campo é superior ou igual ao valor de referência.
     * **Menor que (<):** Verifica se o valor do campo é inferior ao valor de referência.
     * **Menor ou igual (≤):** Verifica se o valor do campo é inferior ou igual ao valor de referência.
3. **Valor de referência**
   * **Descrição:** O valor com o qual o campo é comparado.
   * **Detalhe:** Este valor pode ser numérico, de texto ou de data, consoante o contexto da comparação.
4. **Valor de tolerância**
   * **Descrição:** Define a margem de erro aceitável para a comparação.
   * **Detalhe:** O valor de tolerância é um valor numérico que indica a diferença máxima permitida entre os dois valores de campo para que a comparação seja considerada verdadeira.
5. **Tipo de tolerância**
   * **Descrição:** Especifica a unidade de medida do valor de tolerância.
   * **Opções:**
     * **Valor:** A tolerância é um valor absoluto, ou seja, os dois campos podem diferir pelo valor de tolerância especificado.
     * **Percent:** A tolerância é calculada como uma percentagem do valor do segundo campo, permitindo uma margem de erro relativa.

## **Funcionalidade:**

* **Avaliação da condição:** O sistema avalia o valor do campo face ao valor de referência utilizando o operador de comparação selecionado. Se estiver configurada uma tolerância, o sistema considera a comparação bem-sucedida se o valor do campo estiver dentro do intervalo de tolerância definido.
* **Execução da ação:**
  * **Dentro da tolerância:** Se o valor do campo cumprir a condição dentro da tolerância especificada, o fluxo de trabalho continua, acionando as ações associadas.
  * **Fora da tolerância:** Se o valor do campo não cumprir a condição ou ficar fora do intervalo de tolerância, podem ser executadas ações alternativas, como registo, envio de alertas ou interrupção do fluxo de trabalho.

## **Configuração:**

* Os utilizadores configuram o cartão selecionando o campo a avaliar a partir de uma lista de campos disponíveis e escolhendo o operador de comparação (por exemplo, equals, greater than) a partir de uma lista pendente. De seguida, especificam o valor de referência a comparar e definem o valor de tolerância, e depois selecionam o tipo de tolerância (por exemplo, percent ou value).

## **Conclusão:**

O cartão "Field Comparison with Tolerances" é uma ferramenta versátil para fluxos de trabalho que exigem avaliações flexíveis. Ao permitir comparações com tolerâncias, assegura que os fluxos de trabalho permanecem eficientes e adaptáveis, acomodando variações do mundo real sem comprometer a precisão.

<!-- workflow-card-complete-example-20261021 condition_docfield_operator_value_tolerances -->

### Exemplo de tolerância de valor de referência

**Configuração:** Escolha o campo numérico do documento `total_amount`, igualdade, valor de referência `100`, tolerância absoluta `5` e tipo de tolerância Valor.

**Resultado esperado e contraexemplo:** Com valor `103`, a condição é verdadeira porque a diferença está dentro da tolerância permitida. Com o valor `110`, a condição é falsa porque a diferença excede essa tolerância. Este cartão compara um campo com um valor de referência configurado. Use o cartão de dois campos separado quando ambos os lados precisarem vir dos campos do documento. Dados ausentes ou não numéricos requerem investigação, não uma correspondência presumida.

Esta é uma configuração de teste ilustrativa e resultado esperado; não foi executado. Use dados e destinatários configurados na sua organização de teste.
