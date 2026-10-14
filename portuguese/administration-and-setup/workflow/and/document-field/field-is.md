# Field is

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Este cartão de fluxo de trabalho foi concebido para automatizar ações com base na presença ou no estado de um campo especificado dentro de um documento. Ao avaliar se o campo está vazio, em falta ou preenchido, permite que os fluxos de trabalho tratem os documentos com precisão e exatidão.

## **Componentes do cartão:**

1. **Field Name**
   * **Descrição:** Especifica o nome do campo a avaliar.
   * **Detalhe:** Tem de corresponder ao identificador exato utilizado no documento para assegurar uma deteção de campo precisa.
2. **Operadores**
   * **Descrição**: Define a condição que aciona o fluxo de trabalho, com base na presença ou no estado do campo.
   * **Opções**:
     * **Empty/Not in Document:** O fluxo de trabalho é acionado se o campo estiver em falta no documento ou se estiver presente mas vazio.
     * **In Document/Not Empty:** O fluxo de trabalho é acionado se o campo existir no documento e contiver um valor.

## **Funcionalidade:**

* **Deteção de estado:** O cartão monitoriza o campo especificado para avaliar a sua presença e estado.
* **Avaliação da condição:**
  * O sistema avalia se o campo especificado está no estado (Empty/Not in Document ou In Document/Not Empty) definido pelo operador selecionado.
*

    **Execução da ação:**

    * **Condição Empty/Not in Document:** Se o estado do campo corresponder a esta condição (ou seja, o campo está ausente do documento ou presente mas vazio), o sistema inicia as ações associadas. Estas podem incluir a geração de alertas, a sinalização do documento para revisão ou a interrupção do fluxo de trabalho.
    * **Condição In Document/Not Empty:** Se o estado do campo corresponder a esta condição (ou seja, o campo existe no documento e contém um valor), o sistema aciona as ações associadas. Estas podem envolver a ativação de passos subsequentes do fluxo de trabalho, a atualização de registos ou o acionamento de notificações.

## **Configuração:**&#x20;

* Os utilizadores selecionam o campo a partir de uma lista de campos de documento disponíveis. O operador é escolhido através de um menu pendente, oferecendo opções claras para "Empty/Not in Document" ou "In Document/Not Empty".

## **Conclusão:**

O cartão de fluxo de trabalho "Field Presence and State Validation" é uma ferramenta crucial para os fluxos de processamento de documentos, assegurando o tratamento preciso de campos em falta ou preenchidos. Ao automatizar ações com base nos estados dos campos, este cartão reforça a integridade dos dados, reduz erros e assegura que os fluxos de trabalho funcionam de forma fluida e eficiente.
