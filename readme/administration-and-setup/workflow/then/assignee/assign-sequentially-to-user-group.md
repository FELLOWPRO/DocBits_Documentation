# Atribuir sequencialmente ao usuário/grupo

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-61e424b9ad8c-pt.png" alt="Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real." width="563"><figcaption><p>Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

## **Propósito**

O cartão de fluxo de trabalho "**Atribuir o documento sequencialmente ao usuário/grupo com base na tabela de decisão**" atribui dinamicamente documentos a um utilizador ou a um grupo, consoante a avaliação da decision table. Isto assegura que os documentos são encaminhados de forma adequada com base em regras predefinidas.

## **Componentes do cartão**

1. **Prioridade (Valor)**
   * **Descrição**: Especifica o nível de prioridade das atribuições, sendo que números mais baixos representam uma prioridade mais elevada.
   * **Detalhe**: Um campo de introdução numérica onde se pode definir o valor de prioridade para controlar a sequência de atribuição.

## **Funcionalidade**

* **Avaliação da decision table**:\
  A decision table avalia condições predefinidas para decidir se o documento é atribuído a um utilizador ou a um grupo.
* **Atribuição de documentos**:
  * Se a decision table devolver um utilizador, o documento é atribuído diretamente a esse utilizador.
  * Se a decision table devolver um grupo, o documento é atribuído ao grupo de forma sequencial, respeitando o valor de prioridade especificado.

## **Configuração**

1. Adicione o cartão **Atribuir o documento sequencialmente** ao seu fluxo de trabalho.
2. Configure o campo **Prioridade (Valor)**:
   * Introduza um valor numérico para definir a prioridade de atribuição.
3. Guarde e ative o fluxo de trabalho para aplicar a configuração.

## **Conclusão**

O cartão de fluxo de trabalho "**Atribuir o documento sequencialmente ao usuário/grupo com base na tabela de decisão**" assegura um encaminhamento de documentos eficiente e dinâmico. Ao recorrer à lógica da decision table e aos valores de prioridade, o cartão facilita uma atribuição precisa a um utilizador ou a um grupo, simplificando os fluxos de trabalho de documentos.

<!-- workflow-card-practical-example-20261021 -->

## Exemplo prático

**Quando usar:** Use uma tabela de decisão para selecionar um destinatário de documento priorizado.

**Configuração:** Configure uma regra de tabela de decisão de demonstração correspondente que retorne o usuário ou grupo pretendido e selecione essa tabela no cartão.

**Resultado esperado e contra-exemplo:** O responsável retornado é usado para atribuição sequencial de documentos. Sem retorno correspondente, não assuma um responsável padrão; inspecione o resultado e configure o comportamento de fallback desta versão.

Esta é uma configuração ilustrativa e resultado esperado. Utilize campos, usuários e grupos configurados em sua organização de teste; não é uma afirmação de que este exemplo foi executado.
