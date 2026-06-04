# Text in Field

<figure><img src="../../../../.gitbook/assets/image (10) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Este cartão de fluxo de trabalho foi concebido para automatizar ações com base na presença ou ausência de texto específico dentro de um campo de documento especificado. Assegura que os fluxos de trabalho se podem adaptar dinamicamente ao conteúdo dos documentos, apoiando um processamento eficiente e uma tomada de decisões precisa.

## **Componentes do cartão:**

1. **Text**
   * **Descrição:** Especifica a cadeia de texto a verificar dentro do campo.
   * **Detalhe:** Pode ser uma palavra, frase ou sequência de caracteres relevante para o fluxo de trabalho.
2. **Operador**
   * **Descrição:** Define a condição para a presença de texto no campo.
   * **Opções:**
     * **Is:** Aciona o fluxo de trabalho se o texto especificado estiver presente no campo.
     * **Is Not:** Aciona o fluxo de trabalho se o texto especificado não estiver presente no campo.
3. **Field Name**
   * **Descrição:** Especifica o nome do campo de documento a avaliar.
   * **Detalhe:** Tem de corresponder ao identificador exato do campo dentro do documento.

## **Funcionalidade:**

1. **Avaliação da condição:** O sistema verifica se o texto especificado existe no campo, com base no operador selecionado (Is ou Is Not).
2. **Execução da ação:**
   * **Condição Verdadeira:**\
     Se a presença do texto no campo corresponder à condição especificada, o sistema inicia as ações associadas. Estas podem incluir o acionamento de alertas, o avanço de fluxos de trabalho ou a atualização de registos.
   * **Condição Falsa:**\
     Se a presença do texto no campo não corresponder à condição, podem ser tomadas ações alternativas ou nenhuma ação, consoante a configuração do fluxo de trabalho.

## **Configuração:**&#x20;

* O utilizador introduz o texto a verificar. De seguida, seleciona o nome do campo do documento relevante.

## **Conclusão:**

O cartão de fluxo de trabalho "Text Presence in Field" é uma ferramenta simples mas poderosa para a análise de conteúdo de documentos. Ao automatizar ações com base na deteção de texto, este cartão apoia fluxos de trabalho mais inteligentes, melhora a precisão do tratamento de documentos e reduz o esforço manual.
