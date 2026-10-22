# Calcular colunas com

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-aafc18d42905-pt.png" alt="Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real." width="563"><figcaption><p>Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

## **Propósito:**

O cartão de fluxo de trabalho **"Calcular colunas na tabela"** é utilizado para realizar cálculos entre colunas numa tabela selecionada. Permite aos utilizadores selecionar colunas, aplicar uma operação matemática e armazenar o resultado numa coluna de resultado especificada.

## **Componentes do cartão:**

1. **Nome da tabela**
   * **Descrição:** Especifica a **tabela** na qual as colunas serão calculadas.
   * **Detalhe:** É disponibilizada uma lista pendente com todas as **tabelas** disponíveis para seleção.
2. **Nome da coluna (1.ª coluna)**
   * **Descrição:** Especifica a **primeira coluna** a envolver no cálculo.
   * **Detalhe:** É disponibilizada uma lista de todas as **colunas** disponíveis para seleção.
3. **Operação**
   * **Descrição:** Define a operação matemática a aplicar entre as colunas selecionadas.
   * **Opções:**
     * **Add (+):** Adiciona o valor da segunda coluna ao valor da primeira coluna.
     * **Subtrair (-):** Subtrai o valor da segunda coluna ao valor da primeira coluna.
     * **Multiply (\*):** Multiplica o valor na primeira coluna pelo valor na segunda coluna.
     * **Dividir (/):** Divide o valor na primeira coluna pelo valor na segunda coluna.
4. **Nome da coluna (2.ª coluna)**
   * **Descrição:** Especifica a **segunda coluna** a envolver no cálculo.
   * **Detalhe:** É disponibilizada uma lista das **colunas** disponíveis para seleção.
5. **Coluna de resultados**
   * **Descrição:** Especifica a **coluna** onde o resultado do cálculo será armazenado.
   * **Detalhe:** É disponibilizada uma lista das **colunas** disponíveis onde o valor calculado será guardado.

## **Funcionalidade:**

* **Avaliação da condição:**\
  O cartão só executa a sua ação se tanto a secção **"Quando"** como as **"E Seções"** forem avaliadas como verdadeiras.
* **Cálculo de colunas:**\
  O cartão realiza a operação matemática selecionada entre as duas colunas escolhidas.
* **Armazenamento do resultado:**\
  O resultado do cálculo é armazenado na **coluna de resultado** selecionada.

## **Configuração:**

* **Selecionar a tabela:**\
  Escolha a **tabela** onde as colunas serão calculadas.
* **Escolher colunas:**\
  Selecione a **primeira coluna** e a **segunda coluna** que serão utilizadas no cálculo.
* **Selecionar a operação:**\
  Escolha a operação matemática (**Add (+)**, **Subtrair (-)**, **Multiply (\*)**, **Divide (/)**) a aplicar entre as colunas.
* **Selecionar a coluna de resultado:**\
  Escolha a **coluna de resultado** onde o cálculo será armazenado.

## **Conclusão:**

O cartão de fluxo de trabalho **"Calcular colunas na tabela"** permite aos utilizadores realizar cálculos dinâmicos entre colunas numa tabela e armazenar os resultados numa coluna designada. O cartão oferece flexibilidade para aplicar diferentes operações matemáticas e assegura que o resultado é armazenado na coluna especificada.

<!-- workflow-card-practical-example-20261021 -->

## Exemplo prático

**Quando usar:** Calcule os totais das linhas a partir da quantidade e do preço unitário.

**Configuração:** Selecione tabela `lines`, colunas `quantity` e `unit_price`, multiplicação e coluna de resultado `line_total`.

**Resultado esperado e contra-exemplo:** Uma linha contendo `2` e `10` produz `20`. Teste outra linha de forma independente e diagnostique entradas ausentes ou não numéricas, em vez de tratá-las como um total válido.

Esta é uma configuração ilustrativa e resultado esperado. Utilize campos, usuários e grupos configurados em sua organização de teste; não é uma afirmação de que este exemplo foi executado.
