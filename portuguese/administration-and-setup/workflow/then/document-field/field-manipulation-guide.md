# Cartões de manipulação de campos e tabelas

## Cartões de manipulação de campo e tabela - Guia completo

**Capas:** 9 cartões para modificar campos e tabelas do documento

***

Os cartões de campo e tabela nesta página vão para o grupo **Então** do Workflow Builder — as ações que são executadas quando as condições Quando/E correspondem:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-pt.png" alt="Exemplo não guardado com cartões Quando, E e Então. Configure todos os campos antes da execução. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real."><figcaption><p>Exemplo não guardado com cartões Quando, E e Então. Configure todos os campos antes da execução. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

***

### 📌 Informações da versão

**Cartões multiversão:** CALC\_COLUMNS (v2), CALC\_COLUMNS\_REGEX (v2), EDIT\_COLUMN (v2), AI\_CALC\_MTZ\_ETZ (v2)

**Padrão de versão:** Todos os cartões de manipulação de campo seguem o padrão v1 → v2 **Mudança de chave:** v2 adiciona suporte à internacionalização (i18n) com chaves de tradução

📖 [Histórico completo da versão](../../release.md) | [Versões e comportamento das cartas](../../cards-overview/card-versions-guide.md)

***

## Manipulação de campo de documento

### Cartão: ACTION\_SET\_FIELD\_TO\_TEXT / Definir campo como valor de texto

#### Objetivo

Preenche automaticamente um campo do documento com texto específico

#### Quando usar

* Preencher campo a partir da decisão
* Definir valores padrão
* Preencha informações padronizadas
* Atualizar campo com base nas condições

#### Como funciona

```
IF Condition is true
    THEN Set Field "Category" to Value "Premium"
```

#### Cenários de exemplo

**Cenário 1: Definir categoria de aprovação**

```
Condition: Invoice amount > €10,000
    ↓
Action: Set "Approval_Category" field to "High Value"
    ↓
Result: Document now shows "Approval_Category: High Value"
```

**Cenário 2: Definir categoria do fornecedor**

```
Condition: Supplier name contains "ABC"
    ↓
Action: Set "Supplier_Type" field to "Preferred Supplier"
    ↓
Result: Document marked as "Preferred Supplier"
```

**Cenário 3: Definir notas de processamento**

```
Condition: Document has been rejected
    ↓
Action: Set "Processing_Notes" to "Requires supplier revision"
    ↓
Result: Note appears for next processor
```

#### Parâmetros

**Nome do campo** Qual campo atualizar

```
Examples: Category, Type, Status, Comment, Notes
```

**Valor do texto** O que colocar no campo

```
Examples: "Approved", "Pending Review", "High Priority"
```

#### Etapas de configuração

1. Escolha o campo a preencher
2. Insira o valor do texto
3. Definir condições (quando preencher)
4. Salvar

***

### Cartão: ACTION\_SET\_BOOLEAN\_FIELD / Definir campo de caixa de seleção

#### Objetivo

Marca ou desmarca automaticamente um campo de caixa de seleção

#### Quando usar

* Marcar como processado
* Definir sinalizadores de aprovação
* Ativar/desativar opções
* Marcar para exportação

#### Como funciona

```
IF Condition is true
    THEN Check/Uncheck the "Approved" box
```

#### Verdadeiro = verificado, falso = desmarcado

**Exemplos:**

**Exemplo 1: Marcar como verificado**

```
Condition: PO matches perfectly
    ↓
Action: Check "Verified" checkbox
    ↓
Result: ✅ Verified (checked)
```

**Exemplo 2: Sinalizador para revisão manual**

```
Condition: Price variance > 10%
    ↓
Action: Check "Requires_Manual_Review" checkbox
    ↓
Result: ✅ Requires_Manual_Review (marked)
```

**Exemplo 3: Desmarque a caixa pré-preenchida**

```
Condition: Supplier is blacklisted
    ↓
Action: Uncheck "Approved_for_Payment" checkbox
    ↓
Result: ☐ Approved_for_Payment (unchecked - blocked)
```

#### Parâmetros

```
Checkbox Field: [Choose field]
Set To: ☑ Checked (✅ True)
   or: ☐ Unchecked (❌ False)
```

***

### Cartão: ACTION\_INVERT\_BOOLEAN\_FIELD / Alternar caixa de seleção

#### Objetivo

Inverte o estado da caixa de seleção (marcado → desmarcado, vice-versa)

#### Quando usar

* Alternar status de aprovação
* Alternar modo de processamento
* Reverter estado anterior
* Atualizar sinalizadores booleanos

#### Como funciona

```
Current state: ✅ (Checked)
    ↓
ACTION_INVERT: Toggle the box
    ↓
New state: ☐ (Unchecked)

OR

Current state: ☐ (Unchecked)
    ↓
ACTION_INVERT: Toggle the box
    ↓
New state: ✅ (Checked)
```

#### Exemplo

```
Invoice received with "Priority" checked
    ↓
After processing, invert "Priority" checkbox
    ↓
Checkbox now unchecked (no longer priority)
```

***

### Cartão: ACTION\_COPY\_DOCFIELD\_TO\_DOCFIELD / Copiar valor do campo

#### Objetivo

Copia o valor de um campo para outro campo

#### Quando usar

* Copiar informações do fornecedor para informações de faturamento
* Duplicar dados entre campos
* Padronize o formato dos dados
* Crie backup de valor

#### Como funciona

```
Source Field: "Invoice_Supplier"  Value: "ABC Corp"
    ↓
COPY TO
    ↓
Target Field: "Billing_Partner"  Value: "ABC Corp"

Both fields now have same value
```

#### Exemplos reais

**Exemplo 1: Copiar endereço de entrega**

```
Source: "Delivery_Address" = "123 Main St, Berlin"
    ↓
Copy to: "Billing_Address"
    ↓
Result: Both fields show "123 Main St, Berlin"
```

**Exemplo 2: Copiar código do fornecedor**

```
Source: "Supplier_Code_External" = "SUPP-789"
    ↓
Copy to: "Supplier_Code_Internal"
    ↓
Result: Both codes match, system recognizes supplier
```

**Exemplo 3: Copiar valor para validação**

```
Source: "Invoice_Total" = "€5000"
    ↓
Copy to: "Amount_to_Validate"
    ↓
Result: Validation field has correct amount
```

#### Parâmetros

```
Source Field: [Choose field to copy FROM]
Target Field: [Choose field to copy TO]
```

#### Notas

* Campo original inalterado
* Campo de destino substituído pelo valor de origem
* Bom para padronizar dados

***

## Manipulação de Tabela

### Cartão: EDIT\_COLUMN / Editar coluna da tabela

#### Objetivo

Altera valores em uma coluna da tabela com base nas condições

#### Quando usar

* Corrigir erros de preços em itens de linha
* Atualizar quantidades
* Descrições corretas dos itens
* Padronize valores

#### Como funciona

```
Table Column: "Unit_Price"
Original Values: [100, 105, 103]
    ↓
FIND: Values matching condition
REPLACE: With new value
    ↓
Updated Column: [100, 110, 110] (example)
```

#### Exemplo: Fixar Preço

**Cenário: Preços na moeda errada**

```
Table "Line_Items" with column "Price"

Current prices: [100, 100, 100] (in wrong currency)
    ↓
Condition: "If Price column equals 100"
    ↓
Action: Replace with 95 (corrected price)
    ↓
Result: [95, 95, 95] (prices corrected)
```

#### Parâmetros

```
Table: [Choose table]
Column: [Choose column to edit]
Find: [Value to find]
Replace with: [New value]
Condition: [When to apply]
```

#### Usos comuns

* Fixar preços unitários
* Padronize descrições
* Quantidades corretas
* Atualizar números SKU

***

### Cartão: CALC\_COLUMNS / Calcular Valores da Coluna

#### Objetivo

Executa cálculos nas colunas da tabela e armazena o resultado

#### Quando usar

* Calcular totais de linha (Qtd × Preço Unitário)
* Colunas de soma
* Calcular descontos
* Calcular porcentagens

#### Como funciona

```
Column A (Quantity): 100
Column B (Unit Price): €50
    ↓
CALCULATE: A × B
    ↓
Column C (Line Total): €5000
```

#### Tipos de cálculo

**Tipo 1: Multiplicação Simples**

```
Formula: Qty × Unit Price = Line Total

Example:
100 units × €50/unit = €5000

Config:
  Column 1: Quantity
  Operator: ×
  Column 2: Unit Price
  Result Column: Line Total
```

**Tipo 2: Adição**

```
Formula: Base Price + Shipping + Tax = Total

Example:
€5000 + €100 + €950 = €6050

Config:
  Column 1: Base Price
  Operator: +
  Column 2: Shipping
  Operator: +
  Column 3: Tax
  Result Column: Total
```

**Tipo 3: Cálculo de porcentagem**

```
Formula: Amount × (1 + Tax%) = Total with Tax

Example:
€5000 × 1.19 = €5950

Config:
  Column: Amount
  Operator: × (1 + Tax%)
  Result Column: Amount_with_Tax
```

**Tipo 4: Subtração**

```
Formula: Original Price - Discount = Final Price

Example:
€100 - €10 = €90

Config:
  Column 1: Original Price
  Operator: -
  Column 2: Discount
  Result Column: Final Price
```

#### Exemplo do mundo real

**Cálculo de itens de linha da fatura:**

```
Table: Invoice_Lines

Row 1:
  Quantity: 100
  Unit Price: €25.00
  Calculate: 100 × €25.00 = €2500.00 (Line Total)

Row 2:
  Quantity: 50
  Unit Price: €40.00
  Calculate: 50 × €40.00 = €2000.00 (Line Total)

Row 3:
  Quantity: 200
  Unit Price: €10.00
  Calculate: 200 × €10.00 = €2000.00 (Line Total)

Subtotal: €6500.00 (sum of line totals)
Tax (19%): €1235.00
Shipping: €100.00
TOTAL: €7835.00
```

#### Parâmetros

```
Table: [Select table]
Column 1: [First column]
Operator: [×, +, -, ÷, %]
Column 2: [Second column] (if needed)
Result Column: [Where to put answer]
```

***

### Cartão: CALC\_COLUMNS\_REGEX / Calcular com padrão Regex

#### Objetivo

Calcula os valores das colunas com base na correspondência de padrões

#### Quando usar

* Extraia valores de texto usando padrões
* Formatar dados com base em regras
* Converta valores com base em padrões
* Analisar texto estruturado

#### Como funciona

**Correspondência de padrão Regex:**

```
Original Value: "ABC-12345-XYZ"
Pattern: Extract numbers only
Calculation: Convert to "12345"
Result: "12345"
```

#### Exemplo: Extrair Código do Fornecedor

**Cenário: os números dos artigos contêm informações do fornecedor**

```
Table Column: "Article_Code"
Values: ["SUPP001-2025-A", "SUPP002-2025-B"]

Pattern: Extract supplier code (first 7 characters)
    ↓
Calculate: SUPP001, SUPP002
    ↓
Store in: "Supplier_Code" column

Result:
Article_Code: SUPP001-2025-A  →  Supplier_Code: SUPP001
Article_Code: SUPP002-2025-B  →  Supplier_Code: SUPP002
```

#### Exemplo: formatar números de telefone

**Cenário: números de telefone não formatados**

```
Original: "491234567890"
Pattern: Format as: +49 123 4567 890
Result: "+49 123 4567 890"
```

#### Exemplo: extrair preços do texto

**Cenário: Preços em formato de texto**

```
Original: "Price is 99.99 EUR"
Pattern: Extract number only
Result: "99.99"
```

#### Parâmetros

```
Table: [Select table]
Column: [Column to analyze]
Regex Pattern: [Pattern to find]
Replacement: [What to replace with]
Result Column: [Where to store result]
```

#### Padrões Regex Comuns

```
Numbers only: [0-9]+
Letters only: [a-zA-Z]+
First word: ^\w+
Extract €: €(\d+\.\d{2})
Date format: \d{4}-\d{2}-\d{2}
```

***

## Exemplos de cálculo

### Exemplo 1: Cálculo Total da Fatura

```
Step 1: Calculate line totals
  Each row: Qty × Unit Price

Step 2: Sum all line totals
  Sum: €2500 + €2000 + €2000 = €6500

Step 3: Calculate tax
  Tax: €6500 × 0.19 = €1235

Step 4: Add shipping
  Final: €6500 + €1235 + €100 = €7835
```

### Exemplo 2: Cálculo da Variância

```
PO Price: €100
Invoice Price: €103

Variance = |(Invoice - PO)| / PO × 100
Variance = |3| / 100 × 100 = 3%

Store in "Price_Variance%" column
```

### Exemplo 3: Aplicação de Desconto

```
Original Price: €100
Discount %: 10%
Discount Amount: €100 × 0.10 = €10
Final Price: €100 - €10 = €90
```

***

## Exemplo de fluxo de trabalho de manipulação de campo

```
Document arrives
    ↓
Check condition: "Amount > €5000?"
    ↓
YES → Set field "Category" = "High Value"
    ↓
Check condition: "Supplier is preferred?"
    ↓
YES → Check "FastTrack" checkbox
    ↓
Copy "Delivery_Address" to "Invoice_Address"
    ↓
In table: Calculate line totals (Qty × Price)
    ↓
In table: Calculate total with tax
    ↓
Document now has all calculated and populated fields
```

***

## Melhores Práticas

✅ **Fazer:**

* Mantenha as fórmulas simples
* Cálculos de teste com dados de amostra
* Verifique se os resultados fazem sentido
* Documente por que você está alterando os campos
* Use o campo de cópia quando os dados forem iguais

❌ **Não:**

* Crie referências circulares (A=B, B=A)
* Substitua dados importantes sem motivo
* Crie padrões regex excessivamente complexos
* Esquecer de verificar os resultados do cálculo
* Calcular em tabelas/colunas erradas

***

## Solução de problemas

### "Campo não atualizando"

**Causa:** Condição não atendida ou cartão não acionado

**Solução:**

* Verifique se a condição é verdadeira
* Verifique se o cartão está no fluxo de trabalho
* Teste com dados de amostra
* Verifique se há erros de digitação no nome do campo

### "Resultado do cálculo errado"

**Causa:** Colunas erradas selecionadas ou fórmula incorreta

**Solução:**

* Verifique as colunas de origem
* Verifique se a fórmula está correta
* Teste manualmente
* Revise casas decimais/arredondamentos

### "Tabela mostra erro"

**Causa:** A coluna referenciada não existe

**Solução:**

* Verifique a ortografia do nome da coluna
* Verifique se a coluna contém dados
* Certifique-se de que o tipo de dados da coluna corresponda ao cálculo
* Adicione colunas ausentes, se necessário

***

## Cartões Relacionados

* **ACTION\_COPY\_DOCFIELD\_TO\_DOCFIELD** - Copiar valores
* **EDIT\_COLUMN** - Alterar valores da tabela
* **CALC\_COLUMNS** - Calcular fórmulas
* **ACTION\_SET\_FIELD\_TO\_TEXT** - Definir valores de texto
* **ACTION\_SET\_BOOLEAN\_FIELD** - Caixas de seleção
