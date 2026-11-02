# Texto no campo

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_doc_field_contains_v2-pt-pt.png" alt="Texto no campo, Versão 2" width="634"><figcaption><p>Versão 2</p></figcaption></figure>

## **Propósito:**

Este cartão de fluxo de trabalho foi concebido para automatizar ações com base na presença ou ausência de texto específico dentro de um campo de documento especificado. Assegura que os fluxos de trabalho se podem adaptar dinamicamente ao conteúdo dos documentos, apoiando um processamento eficiente e uma tomada de decisões precisa.

## **Componentes do cartão:**

1. **Texto**
   * **Descrição:** Especifica a cadeia de texto a verificar dentro do campo.
   * **Detalhe:** Pode ser uma palavra, frase ou sequência de caracteres relevante para o fluxo de trabalho.
2. **Operador**
   * **Descrição:** Define a condição para a presença de texto no campo.
   * **Opções:**
     * **Is:** Aciona o fluxo de trabalho se o texto especificado estiver presente no campo.
     * **Não é:** Aciona o fluxo de trabalho se o texto especificado não estiver presente no campo.
3. **Nome do campo**
   * **Descrição:** Especifica o nome do campo de documento a avaliar.
   * **Detalhe:** Tem de corresponder ao identificador exato do campo dentro do documento.

## **Funcionalidade:**

1. **Avaliação da condição:** O sistema verifica se o texto especificado existe no campo, com base no operador selecionado (Is ou Is Not).
2. **Execução da ação:**
   * **Condição Verdadeira:**\
     Se a presença do texto no campo corresponder à condição especificada, o sistema inicia as ações associadas. Estas podem incluir o acionamento de alertas, o avanço de fluxos de trabalho ou a atualização de registos.
   * **Condição Falsa:**\
     Se a presença do texto no campo não corresponder à condição, podem ser tomadas ações alternativas ou nenhuma ação, consoante a configuração do fluxo de trabalho.

## **Configuração:**

* O utilizador introduz o texto a verificar. De seguida, seleciona o nome do campo do documento relevante.

## **Conclusão:**

O cartão de fluxo de trabalho "Text Presence in Field" é uma ferramenta simples mas poderosa para a análise de conteúdo de documentos. Ao automatizar ações com base na deteção de texto, este cartão apoia fluxos de trabalho mais inteligentes, melhora a precisão do tratamento de documentos e reduz o esforço manual.

<!-- workflow-card-practical-example-20261021 -->

## Exemplo prático

**Quando usar:** Encontre documentos que contenham um marcador de revisão.

**Configuração:** Selecione o campo de texto `review_note`, que contém o operador e o texto `manual review`.

**Resultado esperado e contra-exemplo:** `Please start manual review` passa. `Ready for export` não contém o texto selecionado e falha.

Esta é uma configuração ilustrativa e resultado esperado. Utilize campos, usuários e grupos configurados em sua organização de teste; não é uma afirmação de que este exemplo foi executado.
