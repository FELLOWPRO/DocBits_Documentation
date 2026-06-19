# Árvores de Decisão

{% embed url="https://youtu.be/omFWSkSjlL0" %}
Como criar uma Árvore de Decisão no DocBits (Condições, Políticas, Testes e Exportação)
{% endembed %}

## Visão geral

As Árvores de Decisão são uma funcionalidade poderosa que permite o encaminhamento automatizado e o processo de tomada de decisão com base em regras predefinidas. Esta funcionalidade é especialmente útil em ambientes complexos onde é necessário avaliar várias condições para determinar a ação correta a tomar, tais como atribuir preços, determinar quantidades ou encaminhar documentos.

#### Componentes principais

* **Lista de Árvores de Decisão**: Esta é a interface principal onde são listadas todas as árvores de decisão existentes. Cada árvore de decisão pode ser associada a um tipo de documento específico, como uma `INVOICE` ou `QUOTE`.
* **Editor de Árvores de Decisão**: Esta interface permite a criação e edição de árvores de decisão, onde pode definir regras, operadores e ações a executar quando determinadas condições são cumpridas.

## Interface da Árvore de Decisão

#### Lista de Árvores de Decisão

A lista de Árvores de Decisão apresenta todas as árvores de decisão configuradas. Abra-a a partir de **Settings → Document Processing → Decision Trees**.

<figure><img src="../../../.gitbook/assets/decision_trees.png" alt="Lista de Árvores de Decisão"><figcaption><p>A lista de Árvores de Decisão</p></figcaption></figure>

Cada entrada apresenta:

| Coluna | Descrição |
|--------|-------------|
| **Name** | O nome da árvore de decisão. Clique no nome para abrir o Editor. |
| **Document Type** | O tipo de documento ao qual a árvore se aplica (por exemplo, `INVOICE`, `QUOTE`). |
| **Last Modified By** | O utilizador que editou a árvore pela última vez. |
| **Last Modified At** | Data e hora da última alteração. |
| **Actions** | Menu de três pontos para editar, copiar, exportar ou eliminar a árvore. |

#### Criar uma Árvore de Decisão

1. Clique em **+ Add Decision Tree** no canto superior direito.
2. Introduza um **Name** e selecione o **Document Type**.
3. Utilize o Editor de Árvores de Decisão (abaixo) para definir condições, políticas e resultados.

#### Importar uma Árvore de Decisão

Clique em **Import Decision Tree** para carregar um ficheiro de árvore de decisão exportado anteriormente (formato JSON). Isto é útil para copiar uma árvore entre organizações ou ambientes.

## Editor de Árvores de Decisão

O Editor de Árvores de Decisão permite-lhe configurar regras que regem a forma como as decisões são tomadas.

### **Componentes do Editor de Árvores de Decisão**

* **Regras**: Cada regra é composta por condições e ações.
* **Select Source**: Esta lista pendente permite-lhe especificar o campo de origem a avaliar.
* **Select Operator**: Define o operador lógico (por exemplo, `<=`, `>=`, `=`, `!=`) a aplicar ao campo de origem.
* **Result**: Define o resultado ou a ação que deve ser executada quando as condições são cumpridas.
* **Add New Row**: Permite-lhe adicionar regras adicionais à árvore de decisão.

### Exemplo de configuração de uma Árvore de Decisão

Esta árvore de decisão avalia o campo **Total Amount** e atribui-o a diferentes grupos com base em condições predefinidas. Cada regra compara o montante total com um valor específico e, com base na condição que é verdadeira, é devolvido o **Group** correspondente.

<figure><img src="../../../.gitbook/assets/decision_tree_example_total_amount.png" alt="Exemplo de Árvore de Decisão Total Amount"><figcaption></figcaption></figure>

Esta árvore de decisão avalia duas condições principais para determinar qual o grupo a atribuir: **Total Amount** e **Warehouse Status**. A árvore utiliza limiares baseados no montante total para definir qual o grupo devolvido, com a distinção adicional de saber se o armazém é designado como "Warehouse Main", "Warehouse Sub" ou "Not Warehouse Main".

<figure><img src="../../../.gitbook/assets/decision_tree_example_warehouse_status.png" alt="Exemplo de Árvore de Decisão Warehouse Status"><figcaption></figcaption></figure>

Cada regra é avaliada sequencialmente.

## Política da Árvore de Decisão

A Política da Árvore de Decisão define como as várias regras de uma árvore de decisão são processadas. Pode escolher entre várias políticas:

### **1. Política Única (Unique)**

Garante que apenas uma única regra é correspondida. Se forem correspondidas várias regras, a árvore de decisão devolverá falso.

**Exemplo:**

| Regra | Condição             | Grupo Devolvido |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Se o montante total for **1500**, as regras avaliadas serão:

* **Regra 1**: Total Amount <= 1000 (não corresponde)
* **Regra 2**: Total Amount <= 2000 (corresponde)
* **Regra 3**: Total Amount <= 5000 (corresponde)
* **Regra 4**: Total Amount <= 4000 (corresponde)
* **Regra 5**: Total Amount <= 3000 (corresponde)

Uma vez que são correspondidas várias regras (**Regra 2**, **Regra 3**, **Regra 4**, **Regra 5**), a árvore de decisão devolverá **falso**, porque a política **Única** garante que apenas uma regra pode corresponder.

### **2. Política Primeira (First)**

A primeira regra correspondente é aplicada e não são avaliadas mais regras.

**Exemplo:**

| Regra | Condição             | Grupo Devolvido |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Se o montante total for **1500**, as regras avaliadas serão:

* **Regra 1**: Total Amount <= 1000 (não corresponde)
* **Regra 2**: Total Amount <= 2000 (corresponde) → A árvore de decisão deixa de avaliar mais regras e aplica **GROUP_2**.

### **3. Política de Prioridade (Priority)**

Escolher esta opção permite-lhe definir prioridades para cada regra. Quanto menor o número selecionado, maior a prioridade (ou seja, a prioridade 1 tem a prioridade mais alta). As regras são avaliadas com base na sua ordem de prioridade. A regra correspondente de prioridade mais alta será aplicada.

**Exemplo:**

<table><thead><tr><th width="137">Regra</th><th width="110">Prioridade</th><th width="268">Condição</th><th>Grupo Devolvido</th></tr></thead><tbody><tr><td>1</td><td>5</td><td>Total Amount &#x3C;= 1000</td><td>GROUP_1</td></tr><tr><td>2</td><td>4</td><td>Total Amount &#x3C;= 2000</td><td>GROUP_2</td></tr><tr><td>3</td><td>3</td><td>Total Amount &#x3C;= 3000</td><td>GROUP_3</td></tr><tr><td>4</td><td>2</td><td>Total Amount &#x3C;= 4000</td><td>GROUP_4</td></tr><tr><td>5</td><td>1</td><td>Total Amount &#x3C;= 5000</td><td>GROUP_5</td></tr></tbody></table>

Se o montante total for **1500**, as regras avaliadas serão:

* **Regra 1**: Total Amount <= 1000 (não corresponde)
* **Regra 2**: Total Amount <= 2000 (corresponde)
* **Regra 3**: Total Amount <= 3000 (corresponde)
* **Regra 4**: Total Amount <= 4000 (corresponde)
* **Regra 5**: Total Amount <= 5000 (corresponde)

Uma vez que a prioridade é aplicada pela ordem **5, 4, 3, 2, 1**, a regra correspondente de prioridade mais alta será a **Regra 5** (**GROUP_5**). A árvore de decisão devolverá **GROUP_5** porque a **Regra 5** tem a prioridade mais alta (prioridade 1).

### **4. Política de Recolha (Collect — soma)**

Esta política recolhe todas as regras correspondentes e soma os resultados. Funciona apenas para **Return Type Value**.

**Exemplo:**

| Regra | Condição             | Valor Devolvido |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

Para o valor de entrada de **Total Amount = 3500**, a avaliação das regras seria:

* **Regra 1**: Total Amount <= 1000 (não corresponde)
* **Regra 2**: Total Amount <= 2000 (não corresponde)
* **Regra 3**: Total Amount <= 3000 (corresponde, Return Value = 3)
* **Regra 4**: Total Amount <= 4000 (corresponde, Return Value = 4)
* **Regra 5**: Total Amount <= 5000 (corresponde, Return Value = 5)

Uma vez que a política **Collect (soma)** é aplicada, somamos os **Return Values** das regras correspondentes, que são **3, 4, 5**.

**Somando estes valores** obtém-se:

* 5 + 4 + 3 = **12**

Assim, o resultado devolvido pela árvore de decisão seria **12**, que é a soma de todos os valores devolvidos correspondentes.

### **5. Política de Recolha (Collect — mín/máx/contagem)**

Esta política recolhe todas as regras correspondentes e seleciona o **mínimo**, o **máximo** ou **conta** as ocorrências. Funciona apenas para **Return Type Value**.

**Exemplo:**

| Regra | Condição             | Valor Devolvido |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

1. Se a opção **Collect (mín)** for selecionada, o resultado devolverá o **mínimo** dos **Return Values** das regras correspondentes.
   * Para o valor de entrada de **Total Amount = 3500**, a avaliação das regras seria:
     * **Regra 1**: Total Amount <= 1000 (não corresponde)
     * **Regra 2**: Total Amount <= 2000 (não corresponde)
     * **Regra 3**: Total Amount <= 3000 (corresponde, Return Value = 3)
     * **Regra 4**: Total Amount <= 4000 (corresponde, Return Value = 4)
     * **Regra 5**: Total Amount <= 5000 (corresponde, Return Value = 5)
   * As **regras correspondentes** são a Regra 3, a Regra 4 e a Regra 5, com **Return Values** de **3, 4 e 5**.
   * Uma vez que a política **Collect (mín)** é aplicada, o resultado será o **valor mínimo**, que é **3**.
   * **Resultado**: **3**
2. Se a opção **Collect (máx)** for selecionada, o resultado devolverá o **máximo** dos **Return Values** das regras correspondentes.
   * Para a mesma avaliação acima, o resultado será:
   * **Resultado**: **5**
3. Se a opção **Collect (contagem)** for selecionada, o resultado contará o **número de regras correspondentes**.
   * Para a mesma avaliação acima, o resultado será:
   * **Resultado**: **3** (uma vez que 3 regras corresponderam).

### **6. Política de Ordem das Regras (Rule Order)**

Esta política aplica as regras pela ordem em que aparecem na árvore de decisão e devolve o resultado da regra que corresponde em primeiro lugar.

**Exemplo:**

| Regra | Condição             | Grupo Devolvido |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Dado que o valor de entrada é **Total Amount = 3500**, a avaliação das regras seria:

* **Regra 1**: Total Amount <= 1000 (não corresponde)
* **Regra 2**: Total Amount <= 2000 (não corresponde)
* **Regra 3**: Total Amount <= 3000 (corresponde)
* **Regra 4**: Total Amount <= 4000 (corresponde)
* **Regra 5**: Total Amount <= 5000 (corresponde)

Sob a política **Rule Order**, a árvore processará as regras pela ordem em que estão listadas. Assim, as regras correspondentes serão:

* **Regra 3**: GROUP_3
* **Regra 4**: GROUP_4
* **Regra 5**: GROUP_5

**Resultado**: **GROUP_3**, **GROUP_4**, **GROUP_5**

### **7. Política Qualquer (Any)**

Várias regras podem ser verdadeiras, mas o resultado dessas regras tem de ser o mesmo.

**Exemplo:**

| Regra | Condição             | Grupo Devolvido |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Se o montante total for **2500**, as regras avaliadas serão:

* **Regra 1**: Total Amount <= 1000 (não corresponde)
* **Regra 2**: Total Amount <= 2000 (não corresponde)
* **Regra 3**: Total Amount <= 3000 (corresponde)
* **Regra 4**: Total Amount <= 4000 (corresponde)
* **Regra 5**: Total Amount <= 5000 (corresponde)

Para que a política **Any** se aplique, todas as regras correspondentes têm de devolver o mesmo **Return Group**. Uma vez que os grupos não coincidem entre as diferentes regras, o resultado seria **falso**.

### **8. Política Primeira e Adjacente (First & Adjacent)**

Escolhe o resultado da regra que é adjacente à primeira regra que é verdadeira.

**Exemplo:**

| Regra | Condição             | Grupo Devolvido |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Se o montante total for **1500**, as regras avaliadas serão:

* **Regra 1**: Total Amount <= 1000 (não corresponde)
* **Regra 2**: Total Amount <= 2000 (corresponde)

Uma vez que a **Regra 2** é a primeira regra que corresponde, a política **First & Adjacent** aplicaria o resultado da **Regra 3**: **GROUP_3**.

## **Testar a Árvore de Decisão**

**Visão geral:**
O editor de árvores de decisão inclui uma funcionalidade de teste para validar a lógica das regras configuradas. Esta funcionalidade permite aos utilizadores testar a árvore de decisão fornecendo valores de entrada específicos para os campos selecionados.

**Passos para utilizar a funcionalidade de teste:**

1.  **Localizar o botão Test:**

    * No editor de árvores de decisão, encontre o botão **Test**.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_button.png" alt="Botão Test da Árvore de Decisão" width="563"><figcaption></figcaption></figure>
2.  **Abrir o pop-up de teste:**

    * Clique no botão **Test**.
    * Será apresentada uma janela de pop-up, com campos de entrada correspondentes aos critérios utilizados na árvore de decisão.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_popup.png" alt="Pop-up de Teste da Árvore de Decisão" width="421"><figcaption></figcaption></figure>
3. **Fornecer valores de entrada:**
   *   Introduza valores nos campos de entrada para simular um cenário real.

       <figure><img src="../../../.gitbook/assets/decision_tree_test_input.png" alt="Entrada de Teste da Árvore de Decisão" width="428"><figcaption></figcaption></figure>
4.  **Avaliar os resultados:**

    * Após introduzir os dados, a árvore processa-os com base na política escolhida.
    * O sistema destaca a(s) regra(s) que corresponde(m) aos dados fornecidos.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_result.png" alt="Resultado de Teste da Árvore de Decisão" width="563"><figcaption></figcaption></figure>
5. **Rever o feedback quando não há correspondência:**
   * Se nenhuma regra for destacada, o sistema apresentará feedback a explicar por que motivo nenhuma regra correspondeu.
   * Utilize este feedback para ajustar os dados de entrada ou rever a configuração da árvore quanto a potenciais problemas.

## Exportar e guardar

* **Save**: Guarda a configuração atual da árvore de decisão.
* **Export**: Permite-lhe exportar a configuração da árvore de decisão, que pode depois ser importada para outro ambiente ou utilizada para fins de cópia de segurança.

## Casos de utilização

* **Fluxos de trabalho de aprovação** — encaminhe faturas para diferentes aprovadores com base em limiares de montante (por exemplo, montantes superiores a 10 000 requerem aprovação do gestor).
* **Regras de validação** — valide automaticamente os valores dos campos e assinale os documentos que não cumprem os critérios configurados.
* **Atribuição sequencial** — atribua documentos a utilizadores por uma ordem específica com base em condições.
