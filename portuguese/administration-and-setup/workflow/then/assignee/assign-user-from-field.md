# Atribuir usuário do campo

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-a30b121432e4-pt.png" alt="Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real." width="563"><figcaption><p>Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

## **Propósito:**

O cartão de fluxo de trabalho **"Atribuir usuário do campo com substituto"** atribui dinamicamente um utilizador com base no valor encontrado num campo de documento especificado. Se o campo não contiver um utilizador válido, é selecionado um utilizador alternativo a partir de uma lista predefinida de utilizadores disponíveis, de modo a assegurar que a tarefa ou ação é devidamente atribuída.

## **Componentes do cartão:**

1. **Nome do campo**
   * **Descrição:** Especifica o **campo do documento** que contém a informação do utilizador a atribuir.
   * **Detalhe:** Este campo é avaliado para determinar que utilizador deve ser atribuído. Se o campo contiver um utilizador válido, esse utilizador será atribuído à tarefa. Se o campo estiver vazio ou for inválido, será atribuído o utilizador alternativo.
2. **User (alternativo)**
   * **Descrição:** Especifica o **utilizador alternativo** a atribuir caso o campo do documento não contenha um utilizador válido.
   * **Detalhe:** É disponibilizada uma lista pendente de todos os utilizadores disponíveis para seleção. Este utilizador será atribuído se o campo do documento estiver vazio ou não contiver um utilizador válido.

## **Funcionalidade:**

* **Avaliação da condição:**\
  O cartão só executa a sua ação se tanto a secção **"Quando"** como as **"E Seções"** forem avaliadas como verdadeiras.
* **Atribuição de utilizador com base no campo:**\
  O cartão tenta primeiro atribuir a tarefa ou ação ao utilizador identificado no **Nome do campo**.
* **Atribuição do utilizador alternativo:**\
  Se o campo não contiver um utilizador válido (ou estiver vazio), o cartão atribui a tarefa ao utilizador alternativo selecionado na lista pendente **User (alternativo)**.

## **Configuração:**

* **Selecionar o Nome do Campo:**\
  Escolha o **campo do documento** que especifica o utilizador para a atribuição.
* **Selecionar o utilizador alternativo:**\
  Escolha o **utilizador alternativo** a partir da lista pendente. Este utilizador será atribuído à tarefa caso o campo do documento não contenha um utilizador válido.

## **Conclusão:**

O cartão de fluxo de trabalho **"Atribuir usuário do campo com substituto"** assegura que uma tarefa ou ação é sempre atribuída a um utilizador válido. Se o utilizador no campo do documento não estiver disponível, o utilizador alternativo é automaticamente atribuído, proporcionando flexibilidade e assegurando a conclusão da tarefa.

<!-- workflow-card-practical-example-20261021 -->

## Exemplo prático

**Quando usar:** Atribua o revisor nomeado pelos dados do documento.

**Configuração:** Selecione o campo `reviewer_name` e o usuário substituto `Demo Reviewer A`. Forneça um nome de usuário de demonstração resolvível no primeiro teste.

**Resultado esperado e contra-exemplo:** Um valor de campo válido seleciona esse usuário. Um valor vazio ou não resolvível usa o substituto configurado; verifique ambos os casos.

Esta é uma configuração ilustrativa e resultado esperado. Utilize campos, usuários e grupos configurados em sua organização de teste; não é uma afirmação de que este exemplo foi executado.
