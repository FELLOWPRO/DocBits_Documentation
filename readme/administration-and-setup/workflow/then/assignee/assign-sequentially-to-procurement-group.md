# Atribuir sequencialmente ao grupo de compras

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-3b31b4f42710-pt.png" alt="Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real." width="563"><figcaption><p>Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

## **Propósito**

O cartão de fluxo de trabalho "**Atribuir o documento sequencialmente ao grupo de compras**" permite a atribuição sequencial de documentos a um grupo de compras especificado. O valor de prioridade determina a ordem de atribuição, sendo que números mais baixos representam uma prioridade mais elevada.

## **Componentes do cartão**

1. **Grupo**
   * **Descrição**: Um campo de introdução de texto onde se pode inserir o nome do grupo de compras.
   * **Detalhe**: Especifica o grupo de compras ao qual o documento será atribuído.
2. **Prioridade (Valor)**
   * **Descrição**: Um campo de introdução numérica onde se pode definir o nível de prioridade do grupo.
   * **Detalhe**: Números mais baixos significam prioridade mais elevada, assegurando que os documentos são atribuídos aos grupos por ordem crescente de prioridade.

## **Funcionalidade**

* **Atribuição de documentos**:\
  O cartão atribui documentos ao grupo de compras especificado de forma sequencial.\
  Os valores de prioridade ditam a ordem de atribuição, sendo os números mais baixos processados em primeiro lugar.

## **Configuração**

1. Adicione o cartão **Atribuir o documento sequencialmente** ao seu fluxo de trabalho.
2. Configure o campo **Grupo**:
   * Introduza o nome do grupo de compras no campo de texto.
3. Configure o campo **Prioridade (Valor)**:
   * Introduza um valor numérico para definir a prioridade de atribuição.
4. Guarde e ative o fluxo de trabalho para aplicar a configuração.

## **Conclusão**

O cartão de fluxo de trabalho "Assign the Document Sequentially to the Procurement Group" assegura uma alocação eficaz de documentos aos grupos de compras com base na prioridade. Isto melhora a eficiência organizacional e a gestão de tarefas.

<!-- workflow-card-practical-example-20261021 -->

## Exemplo prático

**Quando usar:** Priorize um grupo de compras na revisão de documentos.

**Configuração:** Selecione `Demo Procurement` e prioridade `10`.

**Resultado esperado e contraexemplo:** O documento recebe a atribuição do grupo de compras com prioridade `10`. Verifique se as atribuições posteriores usam as prioridades numéricas mais altas pretendidas.

Esta é uma configuração ilustrativa e resultado esperado. Utilize campos, usuários e grupos configurados em sua organização de teste; não é uma afirmação de que este exemplo foi executado.
