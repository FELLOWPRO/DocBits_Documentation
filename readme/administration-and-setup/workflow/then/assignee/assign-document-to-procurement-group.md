# Atribuir documento ao grupo de compras

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-9b2624ff9d34-pt.png" alt="Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real." width="563"><figcaption><p>Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

## **Propósito:**

O cartão de fluxo de trabalho **"Assign to Procurement Group"** é utilizado para atribuir um documento a um grupo de compras especificado dentro do sistema. Isto ajuda a simplificar a gestão de documentos ao assegurar que a equipa adequada trata o documento com base no grupo de compras atribuído.

## **Componentes do cartão:**

1. **Grupo de Aquisições**
   * **Descrição:** Especifica o grupo de compras ao qual o documento será atribuído.
   * **Detalhe:** O grupo de compras selecionado será responsável pelo processamento e gestão do documento.

## **Funcionalidade:**

* **Avaliação da condição:**\
  O cartão só executa a sua ação se tanto a secção **"Quando"** como as **"E Seções"** forem avaliadas como verdadeiras.
* **Execução da ação:**\
  Se ambas as condições forem verdadeiras, o documento é atribuído ao grupo de compras especificado. Se alguma das condições for falsa, não é tomada qualquer ação e o documento permanece por atribuir.

## **Configuração:**

* **Selecionar o Grupo de Compras:** Escolha o grupo de compras ao qual atribuir o documento a partir da lista pendente.

## **Conclusão:**

O cartão de fluxo de trabalho **"Assign to Procurement Group"** oferece uma forma simples mas eficaz de assegurar que os documentos são automaticamente atribuídos à equipa de compras correta para processamento adicional.

<!-- workflow-card-practical-example-20261021 -->

## Exemplo prático

**Quando usar:** Envie uma exceção de compra ao seu grupo de compras.

**Configuração:** Selecione o grupo configurado `Demo Procurement`.

**Resultado esperado e contraexemplo:** O documento é atribuído a esse grupo de compras. Um grupo comum com nome semelhante não deve ser considerado como o mesmo destino configurado.

Esta é uma configuração ilustrativa e resultado esperado. Utilize campos, usuários e grupos configurados em sua organização de teste; não é uma afirmação de que este exemplo foi executado.
