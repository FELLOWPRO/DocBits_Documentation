# Assign user from field

<figure><img src="../../../../.gitbook/assets/image (299).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

O cartão de fluxo de trabalho **"Assign User from Field with Fallback"** atribui dinamicamente um utilizador com base no valor encontrado num campo de documento especificado. Se o campo não contiver um utilizador válido, é selecionado um utilizador alternativo a partir de uma lista predefinida de utilizadores disponíveis, de modo a assegurar que a tarefa ou ação é devidamente atribuída.

## **Componentes do cartão:**

1. **Field Name**
   * **Descrição:** Especifica o **campo do documento** que contém a informação do utilizador a atribuir.
   * **Detalhe:** Este campo é avaliado para determinar que utilizador deve ser atribuído. Se o campo contiver um utilizador válido, esse utilizador será atribuído à tarefa. Se o campo estiver vazio ou for inválido, será atribuído o utilizador alternativo.
2. **User (alternativo)**
   * **Descrição:** Especifica o **utilizador alternativo** a atribuir caso o campo do documento não contenha um utilizador válido.
   * **Detalhe:** É disponibilizada uma lista pendente de todos os utilizadores disponíveis para seleção. Este utilizador será atribuído se o campo do documento estiver vazio ou não contiver um utilizador válido.

## **Funcionalidade:**

* **Avaliação da condição:**\
  O cartão só executa a sua ação se tanto a secção **"Where"** como as **"And Sections"** forem avaliadas como verdadeiras.
* **Atribuição de utilizador com base no campo:**\
  O cartão tenta primeiro atribuir a tarefa ou ação ao utilizador identificado no **Field Name**.
* **Atribuição do utilizador alternativo:**\
  Se o campo não contiver um utilizador válido (ou estiver vazio), o cartão atribui a tarefa ao utilizador alternativo selecionado na lista pendente **User (alternativo)**.

## **Configuração:**

* **Selecionar o Field Name:**\
  Escolha o **campo do documento** que especifica o utilizador para a atribuição.
* **Selecionar o utilizador alternativo:**\
  Escolha o **utilizador alternativo** a partir da lista pendente. Este utilizador será atribuído à tarefa caso o campo do documento não contenha um utilizador válido.

## **Conclusão:**

O cartão de fluxo de trabalho **"Assign User from Field with Fallback"** assegura que uma tarefa ou ação é sempre atribuída a um utilizador válido. Se o utilizador no campo do documento não estiver disponível, o utilizador alternativo é automaticamente atribuído, proporcionando flexibilidade e assegurando a conclusão da tarefa.
