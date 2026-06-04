# Assign document to matching sub organization

<figure><img src="../../../../.gitbook/assets/image (303).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

O cartão de fluxo de trabalho **"Assign Document to Matching Sub-Organization Based on Field"** atribui um documento a uma sub-organização de forma dinâmica, com base num campo especificado do documento. Se não for encontrada nenhuma sub-organização correspondente, o cartão utiliza uma sub-organização alternativa predefinida.

## **Componentes do cartão:**

1. **Field Name**
   * **Descrição:** Especifica o campo do documento a utilizar para determinar a sub-organização correspondente.
   * **Detalhe:** O cartão procura um valor no campo especificado para corresponder a uma sub-organização disponível.
2. **Sub-Organization (alternativa)**
   * **Descrição:** Define a sub-organização alternativa a utilizar caso não seja encontrada correspondência no campo especificado.
   * **Detalhe:** Se o valor do campo não corresponder a nenhuma sub-organização, o documento será atribuído à sub-organização alternativa selecionada.

## **Funcionalidade:**

* **Avaliação da condição:**\
  O cartão só executa a sua ação se tanto a secção **"Where"** como as **"And Sections"** forem avaliadas como verdadeiras.
* **Atribuição dinâmica:**\
  O cartão verifica o valor do campo especificado e atribui o documento à sub-organização que corresponde a esse valor.
* **Mecanismo alternativo:**\
  Se não for encontrada nenhuma sub-organização correspondente, o documento é atribuído à sub-organização alternativa.

## **Configuração:**

* **Selecionar o Field Name:**\
  Escolha o campo do documento que contém o valor a corresponder a uma sub-organização.
* **Selecionar a sub-organização alternativa:**\
  Escolha a sub-organização que será utilizada caso não seja encontrada correspondência no campo do documento.

## **Conclusão:**

O cartão de fluxo de trabalho **"Assign Document to Matching Sub-Organization Based on Field"** oferece flexibilidade ao encaminhar dinamicamente os documentos para a sub-organização adequada, com uma opção alternativa adicional para assegurar que nenhum documento fica por atribuir.
