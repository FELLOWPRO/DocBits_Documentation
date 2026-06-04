# Compare Field with tolerances

<figure><img src="../../../../.gitbook/assets/image (15) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Este cartão de fluxo de trabalho foi concebido para comparar o valor de um campo com um valor de referência especificado, permitindo tolerâncias. Possibilita um processamento condicional preciso em fluxos de trabalho onde pequenos desvios são aceitáveis, sendo ideal para cenários como garantia de qualidade, análise financeira ou ações baseadas em limiares.

## **Componentes do cartão:**

1. **Field Name**
   * **Descrição:** O campo a avaliar na comparação.
   * **Detalhe:** Tem de corresponder ao identificador exato do primeiro campo dentro do documento.
2. **Comparison Operator**
   * **Descrição:** Especifica como o valor do campo selecionado será comparado com o valor de referência.
   * **Opções:**
     * **Equals (=):** Verifica se o valor do campo corresponde exatamente ao valor de referência.
     * **Not Equals (≠):** Verifica se o valor do campo não corresponde ao valor de referência.
     * **Greater Than (>):** Verifica se o valor do campo é superior ao valor de referência.
     * **Greater or Equals (≥):** Verifica se o valor do campo é superior ou igual ao valor de referência.
     * **Lesser Than (<):** Verifica se o valor do campo é inferior ao valor de referência.
     * **Lesser or Equals (≤):** Verifica se o valor do campo é inferior ou igual ao valor de referência.
3. **Reference Value**
   * **Descrição:** O valor com o qual o campo é comparado.
   * **Detalhe:** Este valor pode ser numérico, de texto ou de data, consoante o contexto da comparação.
4. **Tolerance Amount**
   * **Descrição:** Define a margem de erro aceitável para a comparação.
   * **Detalhe:** O valor de tolerância é um valor numérico que indica a diferença máxima permitida entre os dois valores de campo para que a comparação seja considerada verdadeira.
5. **Tolerance Type**
   * **Descrição:** Especifica a unidade de medida do valor de tolerância.
   * **Opções:**
     * **Value:** A tolerância é um valor absoluto, ou seja, os dois campos podem diferir pelo valor de tolerância especificado.
     * **Percent:** A tolerância é calculada como uma percentagem do valor do segundo campo, permitindo uma margem de erro relativa.

## **Funcionalidade:**

* **Avaliação da condição:** O sistema avalia o valor do campo face ao valor de referência utilizando o operador de comparação selecionado. Se estiver configurada uma tolerância, o sistema considera a comparação bem-sucedida se o valor do campo estiver dentro do intervalo de tolerância definido.
* **Execução da ação:**
  * **Dentro da tolerância:** Se o valor do campo cumprir a condição dentro da tolerância especificada, o fluxo de trabalho continua, acionando as ações associadas.
  * **Fora da tolerância:** Se o valor do campo não cumprir a condição ou ficar fora do intervalo de tolerância, podem ser executadas ações alternativas, como registo, envio de alertas ou interrupção do fluxo de trabalho.

## **Configuração:**

* Os utilizadores configuram o cartão selecionando o campo a avaliar a partir de uma lista de campos disponíveis e escolhendo o operador de comparação (por exemplo, equals, greater than) a partir de uma lista pendente. De seguida, especificam o valor de referência a comparar e definem o valor de tolerância, e depois selecionam o tipo de tolerância (por exemplo, percent ou value).&#x20;

## **Conclusão:**

O cartão "Field Comparison with Tolerances" é uma ferramenta versátil para fluxos de trabalho que exigem avaliações flexíveis. Ao permitir comparações com tolerâncias, assegura que os fluxos de trabalho permanecem eficientes e adaptáveis, acomodando variações do mundo real sem comprometer a precisão.
