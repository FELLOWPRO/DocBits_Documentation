# Atribuir sequencialmente a grupos

## **Propósito**

O cartão de fluxo de trabalho "**Atribuir o documento sequencialmente aos grupos**" permite a atribuição sequencial de documentos a um ou mais grupos selecionados. O valor de prioridade determina a ordem de atribuição, sendo que números mais baixos representam uma prioridade mais elevada.

## **Componentes do cartão**

1. **Grupo**
   * **Descrição**: Especifica os grupos que receberão a atribuição do documento.
   * **Detalhe**: Um menu pendente onde podem ser selecionados um ou vários grupos para a atribuição do documento.
2. **Prioridade (Valor)**
   * **Descrição**: Um campo de introdução numérica onde se pode definir o nível de prioridade dos grupos.
   * **Detalhe**: Números mais baixos significam prioridade mais elevada, assegurando que os documentos são atribuídos aos grupos por ordem crescente de prioridade.

## **Funcionalidade**

* **Atribuição de documentos**:\
  O cartão atribui documentos sequencialmente aos grupos selecionados com base nos seus valores de prioridade.\
  Se vários grupos partilharem a mesma prioridade, os documentos são atribuídos pela ordem em que os grupos foram selecionados.

## **Configuração**

1. Adicione o cartão **Atribuir o documento sequencialmente** ao seu fluxo de trabalho.
2. Configure o campo **Grupo**:
   * Selecione um ou vários grupos no menu pendente.
3. Configure o campo **Prioridade (Valor)**:
   * Introduza um valor numérico para definir a prioridade de atribuição.
4. Guarde e ative o fluxo de trabalho para aplicar a configuração.

## **Conclusão**

O cartão de fluxo de trabalho "Assign the Document Sequentially to Groups" assegura uma alocação eficiente de documentos a um ou mais grupos com base na prioridade. Esta funcionalidade apoia um processamento de documentos flexível e organizado entre várias equipas ou departamentos.

<!-- workflow-card-practical-example-20261021 -->

## Exemplo prático

**Quando usar:** Priorize a atribuição de documentos para as equipes de revisão.

**Configuração:** Selecione os grupos de demonstração configurados e defina a prioridade necessária, por exemplo `10`.

**Resultado esperado e contraexemplo:** O documento recebe as atribuições do grupo selecionado naquela prioridade. Testar uma segunda prioridade separadamente quando os grupos tiverem que ocupar estágios diferentes.

Esta é uma configuração ilustrativa e resultado esperado. Utilize campos, usuários e grupos configurados em sua organização de teste; não é uma afirmação de que este exemplo foi executado.
