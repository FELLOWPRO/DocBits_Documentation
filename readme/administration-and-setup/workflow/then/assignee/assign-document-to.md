# Atribuir documento a

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-0e17d9fb5a83-pt.png" alt="Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real." width="563"><figcaption><p>Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

## Propósito:

O cartão de fluxo de trabalho **"Atribuir documento a \[Usuário/grupo] com base na tabela de decisão"** atribui dinamicamente documentos a utilizadores ou grupos com base no resultado de uma **tabela de decisão**. Esta funcionalidade assegura que a atribuição de documentos é tratada de forma eficiente e consistente com base em condições predefinidas.

## Componentes do cartão:

1. **Usuário/Grupo**
   * **Descrição:** Especifica o **utilizador** ou **grupo** ao qual o documento será atribuído.
   * **Detalhe:** Selecionado com base no resultado da **tabela de decisão**.
2. **Tabela de Decisão**
   * **Descrição:** Uma **tabela de decisão** é utilizada para determinar o **utilizador** ou **grupo** adequado para a atribuição do documento.
   * **Detalhe:** Utiliza a decision table definida na secção **"e"**.

## Funcionalidade:

* **Avaliação da condição:** O cartão só executa a sua ação se tanto a secção **"Quando"** como as **"E Seções"** forem avaliadas como verdadeiras.
* **Atribuição dinâmica de documentos:** O documento é atribuído ao **utilizador** ou **grupo** determinado pela **tabela de decisão**.

## Configuração:

* **Definir a Decision Table:** Configure a **tabela de decisão** para incluir as condições para determinar o **utilizador** ou **grupo** de destino.
* **Atribuir documento a utilizador/grupo:** O documento será atribuído dinamicamente com base no resultado da decision table.

## Conclusão:

O cartão de fluxo de trabalho **"Atribuir documento a \[Usuário/grupo] com base na tabela de decisão"** oferece capacidades de atribuição dinâmica de documentos com base em lógica de decisão. Isto assegura um processamento preciso e eficiente ao direcionar automaticamente os documentos para o **utilizador** ou **grupo** adequado, reforçando a automação do fluxo de trabalho.

<!-- workflow-card-practical-example-20261021 -->

## Exemplo prático

**Quando usar:** Escolha um destinatário do documento em uma tabela de decisão.

**Configuração:** Selecione uma tabela de decisão de demonstração cuja regra correspondente retorne o revisor configurado e escolha o tipo de destinatário oferecido por esta versão do cartão.

**Resultado esperado e contra-exemplo:** O usuário ou grupo retornado torna-se o cessionário do documento. Um resultado vazio da tabela de decisão deve ser diagnosticado separadamente.

Esta é uma configuração ilustrativa e resultado esperado. Utilize campos, usuários e grupos configurados em sua organização de teste; não é uma afirmação de que este exemplo foi executado.
