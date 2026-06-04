# Assign Sequentially to User/Group

<figure><img src="../../../../.gitbook/assets/image (11) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito**

O cartão de fluxo de trabalho "**Assign the Document Sequentially to User/Group Based on Decision Table**" atribui dinamicamente documentos a um utilizador ou a um grupo, consoante a avaliação da decision table. Isto assegura que os documentos são encaminhados de forma adequada com base em regras predefinidas.

## **Componentes do cartão**

1. **Priority (Value)**
   * **Descrição**: Especifica o nível de prioridade das atribuições, sendo que números mais baixos representam uma prioridade mais elevada.
   * **Detalhe**: Um campo de introdução numérica onde se pode definir o valor de prioridade para controlar a sequência de atribuição.

## **Funcionalidade**

* **Avaliação da decision table**:\
  A decision table avalia condições predefinidas para decidir se o documento é atribuído a um utilizador ou a um grupo.
* **Atribuição de documentos**:
  * Se a decision table devolver um utilizador, o documento é atribuído diretamente a esse utilizador.
  * Se a decision table devolver um grupo, o documento é atribuído ao grupo de forma sequencial, respeitando o valor de prioridade especificado.

## **Configuração**

1. Adicione o cartão **Assign the Document Sequentially** ao seu fluxo de trabalho.
2. Configure o campo **Priority (Value)**:
   * Introduza um valor numérico para definir a prioridade de atribuição.
3. Guarde e ative o fluxo de trabalho para aplicar a configuração.

## **Conclusão**

O cartão de fluxo de trabalho "**Assign the Document Sequentially to User/Group Based on Decision Table**" assegura um encaminhamento de documentos eficiente e dinâmico. Ao recorrer à lógica da decision table e aos valores de prioridade, o cartão facilita uma atribuição precisa a um utilizador ou a um grupo, simplificando os fluxos de trabalho de documentos.
