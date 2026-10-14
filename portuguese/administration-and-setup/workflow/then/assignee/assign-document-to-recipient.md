# Assign document to recipient

<figure><img src="../../../../.gitbook/assets/image (301).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

O cartão de fluxo de trabalho **"Assign Document to Disponent / Purchaser"** atribui um documento a um **Disponent** ou a um **Purchaser**. Se não for encontrado nenhum utilizador válido, é selecionado um utilizador alternativo para assegurar que o documento é sempre atribuído a alguém.

## **Componentes do cartão:**

1. **Disponent / Purchaser**
   * **Descrição:** Especifica se o documento será atribuído a um Disponent ou a um Purchaser.
   * **Opções:**
     * **Disponent:** Atribui o documento ao Disponent.
     * **Purchaser:** Atribui o documento ao Purchaser.
2. **Fallback User**
   * **Descrição:** Especifica um utilizador alternativo caso o documento não possa ser atribuído ao Disponent ou Purchaser selecionado.
   * **Detalhe:** A lista pendente de utilizadores disponíveis permite escolher um utilizador alternativo para assegurar que o documento é atribuído mesmo que o utilizador principal não possa ser determinado.

## **Funcionalidade:**

* **Avaliação da condição:**\
  O cartão só executa a sua ação se tanto a secção **"Where"** como as **"And Sections"** forem avaliadas como verdadeiras.
* **Atribuição do documento:**\
  O cartão atribui o documento ao **Disponent** ou ao **Purchaser**, conforme selecionado. Se a pessoa selecionada estiver indisponível ou não for válida, o documento é atribuído ao utilizador alternativo.

## **Configuração:**

* **Selecionar Disponent / Purchaser:**\
  Escolha se pretende atribuir o documento ao **Disponent** ou ao **Purchaser**.
* **Selecionar o Fallback User:**\
  Escolha um utilizador alternativo a partir da lista pendente que receberá o documento caso a atribuição principal não seja possível.

## **Conclusão:**

O cartão de fluxo de trabalho **"Assign Document to Disponent / Purchaser"** assegura que o documento é sempre atribuído, seja ao Disponent/Purchaser selecionado ou, se necessário, ao utilizador alternativo. Isto minimiza interrupções no fluxo de trabalho e assegura que o processamento de documentos continua de forma fluida.
