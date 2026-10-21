# Atribuir documento à suborganização

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-a05599461b30-pt.png" alt="Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real." width="563"><figcaption><p>Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

## **Propósito:**

O cartão de fluxo de trabalho **"Atribuir documento à suborganização"** atribui um documento a uma sub-organização específica dentro do sistema, assegurando que é encaminhado para a unidade organizacional adequada para processamento.

## **Componentes do cartão:**

1. **Suborganização**
   * **Descrição:** Especifica a sub-organização à qual o documento será atribuído.
   * **Detalhe:** É disponibilizada uma lista pendente das sub-organizações disponíveis para selecionar a sub-organização de destino.

## **Funcionalidade:**

* **Avaliação da condição:**\
  O cartão só executa a sua ação se tanto a secção **"Quando"** como as **"E Seções"** forem avaliadas como verdadeiras.
* **Atribuição do documento:**\
  O cartão atribui o documento à sub-organização selecionada na lista pendente.

## **Configuração:**

* **Selecionar uma suborganização:**\
  Escolha a sub-organização adequada a partir da lista pendente à qual o documento deve ser atribuído.

## **Conclusão:**

O cartão de fluxo de trabalho **"Atribuir documento à suborganização"** assegura que os documentos são encaminhados para a sub-organização correta, simplificando o processo de gestão de documentos ao atribuir responsabilidades com base na estrutura organizacional.

<!-- workflow-card-practical-example-20261021 -->

## Exemplo prático

**Quando usar:** Encaminhe um documento para uma unidade de negócios conhecida.

**Configuração:** Selecione a suborganização configurada `Demo North`.

**Resultado esperado e contraexemplo:** O documento pertence à suborganização selecionada após a ação. Confirme o destino antes de ativar o fluxo de trabalho porque as regras de acesso da suborganização podem ser diferentes.

Esta é uma configuração ilustrativa e resultado esperado. Utilize campos, usuários e grupos configurados em sua organização de teste; não é uma afirmação de que este exemplo foi executado.
