# Change Entries with

<figure><img src="../../../../.gitbook/assets/image (293).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

O cartão de fluxo de trabalho **"Change Entries in Table"** é utilizado para atualizar entradas numa tabela de base de dados especificada. Permite selecionar uma **tabela** e uma **coluna** e, em seguida, realizar operações matemáticas (adição, subtração, multiplicação ou divisão) sobre os valores dessa coluna, utilizando um valor especificado.

## **Componentes do cartão:**

1. **Table Name**
   * **Descrição:** Especifica a **tabela** na qual as entradas serão atualizadas.
   * **Detalhe:** É disponibilizada uma lista pendente das **tabelas** disponíveis, permitindo selecionar a tabela de destino para a atualização de entradas.
2. **Column Name**
   * **Descrição:** Especifica a **coluna** dentro da tabela selecionada a atualizar.
   * **Detalhe:** Será disponibilizada uma lista de todas as **colunas** disponíveis para seleção.
3. **Operation**
   * **Descrição:** Define a operação matemática a realizar sobre os valores da **coluna**.
   * **Opções:**
     * **Add (+):** Adiciona um **valor** especificado ao valor atual na coluna selecionada.
     * **Subtract (-):** Subtrai um **valor** especificado ao valor atual na coluna selecionada.
     * **Multiply (\*):** Multiplica o valor atual na coluna selecionada por um **valor** especificado.
     * **Divide (/):** Divide o valor atual na coluna selecionada por um **valor** especificado.
4. **Value**
   * **Descrição:** Especifica o **valor** a utilizar na operação selecionada.
   * **Detalhe:** Este é o número que será adicionado, subtraído, multiplicado ou dividido com as entradas da coluna selecionada.

## **Funcionalidade:**

* **Avaliação da condição:**\
  O cartão só executa a sua ação se tanto a secção **"Where"** como as **"And Sections"** forem avaliadas como verdadeiras.
* **Atualização de entradas da tabela:**\
  O cartão realiza a operação selecionada (**+**, **-**, **\*** ou **/**) sobre os valores da **coluna** escolhida da **tabela** selecionada, utilizando o **valor** especificado.

## **Configuração:**

* **Selecionar a tabela:**\
  Escolha a **tabela** onde as alterações serão aplicadas.
* **Escolher a coluna:**\
  Selecione a **coluna** dentro da tabela que pretende atualizar.
* **Selecionar a operação:**\
  Escolha a operação matemática (**+**, **-**, **\***, **/**) a aplicar aos valores da coluna selecionada.
* **Introduzir o valor:**\
  Forneça o **valor** a utilizar na operação selecionada.

## **Conclusão:**

O cartão de fluxo de trabalho **"Change Entries in Table"** permite atualizações automatizadas das entradas da base de dados ao selecionar uma **tabela**, uma **coluna** e a **operação matemática** pretendida. Este cartão é essencial para realizar modificações de dados em massa ou cálculos dentro da sua base de dados.
