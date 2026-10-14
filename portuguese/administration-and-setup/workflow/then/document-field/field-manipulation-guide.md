# Field & Table Manipulation Cards - Complete Guide

Estes cartões ficam no grupo **Then** do Construtor de fluxos de trabalho — as ações executadas assim que as condições When/And são atendidas:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Os cartões são adicionados ao grupo <strong>Then</strong> através de <strong>Add Card</strong>.</p></figcaption></figure>

**Abrange:** 9 cartões para modificar campos e tabelas de documentos

---

# Manipulação de campos de documentos

## Cartão: ACTION_SET_FIELD_TO_TEXT / Set Field to Text Value

### Objetivo
Preenche automaticamente um campo do documento com texto específico

### Quando utilizar
- Preencher um campo a partir de uma decisão
- Definir valores predefinidos
- Preencher informações padronizadas
- Atualizar um campo com base em condições

### Como funciona
```
IF Condition is true
    THEN Set Field "Category" to Value "Premium"
```

### Cenários de exemplo

**Cenário 1: Definir a categoria de aprovação**
```
Condition: Invoice amount > €10,000
    ↓
Action: Set "Approval_Category" field to "High Value"
    ↓
Result: Document now shows "Approval_Category: High Value"
```

**Cenário 2: Definir a categoria do fornecedor**
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

### Parâmetros

**Field Name**
Que campo atualizar
```
Examples: Category, Type, Status, Comment, Notes
```

**Text Value**
O que colocar no campo
```
Examples: "Approved", "Pending Review", "High Priority"
```

### Passos de configuração
1. Escolha o campo a preencher
2. Introduza o valor de texto
3. Defina as condições (quando preencher)
4. Guardar

---

## Cartão: ACTION_SET_BOOLEAN_FIELD / Set Checkbox Field

### Objetivo
Marca ou desmarca automaticamente um campo de caixa de verificação

### Quando utilizar
- Marcar como processado
- Definir indicadores de aprovação
- Ativar/desativar opções
- Marcar para exportação

### Como funciona
```
IF Condition is true
    THEN Check/Uncheck the "Approved" box
```

### True = Marcada, False = Desmarcada

**Exemplos:**

**Exemplo 1: Marcar como verificado**
```
Condition: PO matches perfectly
    ↓
Action: Check "Verified" checkbox
    ↓
Result: ✅ Verified (checked)
```

**Exemplo 2: Sinalizar para revisão manual**
```
Condition: Price variance > 10%
    ↓
Action: Check "Requires_Manual_Review" checkbox
    ↓
Result: ✅ Requires_Manual_Review (marked)
```

**Exemplo 3: Desmarcar uma caixa pré-preenchida**
```
Condition: Supplier is blacklisted
    ↓
Action: Uncheck "Approved_for_Payment" checkbox
    ↓
Result: ☐ Approved_for_Payment (unchecked - blocked)
```

### Parâmetros
```
Checkbox Field: [Choose field]
Set To: ☑ Checked (✅ True)
   or: ☐ Unchecked (❌ False)
```

---

## Cartão: ACTION_INVERT_BOOLEAN_FIELD / Toggle Checkbox

### Objetivo
Inverte o estado da caixa de verificação (marcada → desmarcada e vice-versa)

### Quando utilizar
- Alternar o estado de aprovação
- Mudar o modo de processamento
- Inverter o estado anterior
- Atualizar indicadores booleanos

### Como funciona
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

### Exemplo
```
Invoice received with "Priority" checked
    ↓
After processing, invert "Priority" checkbox
    ↓
Checkbox now unchecked (no longer priority)
```

---

## Cartão: ACTION_COPY_DOCFIELD_TO_DOCFIELD / Copy Field Value

### Objetivo
Copia o valor de um campo para outro campo

### Quando utilizar
- Copiar informações do fornecedor para as informações de faturação
- Duplicar dados entre campos
- Padronizar o formato dos dados
- Criar uma cópia de segurança de um valor

### Como funciona
```
Source Field: "Invoice_Supplier"  Value: "ABC Corp"
    ↓
COPY TO
    ↓
Target Field: "Billing_Partner"  Value: "ABC Corp"

Both fields now have same value
```

### Exemplos reais

**Exemplo 1: Copiar o endereço de entrega**
```
Source: "Delivery_Address" = "123 Main St, Berlin"
    ↓
Copy to: "Billing_Address"
    ↓
Result: Both fields show "123 Main St, Berlin"
```

**Exemplo 2: Copiar o código do fornecedor**
```
Source: "Supplier_Code_External" = "SUPP-789"
    ↓
Copy to: "Supplier_Code_Internal"
    ↓
Result: Both codes match, system recognizes supplier
```

**Exemplo 3: Copiar o montante para validação**
```
Source: "Invoice_Total" = "€5000"
    ↓
Copy to: "Amount_to_Validate"
    ↓
Result: Validation field has correct amount
```

### Parâmetros
```
Source Field: [Choose field to copy FROM]
Target Field: [Choose field to copy TO]
```

### Notas
- O campo de origem permanece inalterado
- O campo de destino é substituído pelo valor de origem
- Útil para padronizar dados

---

# Manipulação de tabelas

## Cartão: EDIT_COLUMN / Edit Table Column

### Objetivo
Altera os valores de uma coluna de tabela com base em condições

### Quando utilizar
- Corrigir erros de preço nas linhas
- Atualizar quantidades
- Corrigir descrições de artigos
- Padronizar valores

### Como funciona
```
Table Column: "Unit_Price"
Original Values: [100, 105, 103]
    ↓
FIND: Values matching condition
REPLACE: With new value
    ↓
Updated Column: [100, 110, 110] (example)
```

### Exemplo: Corrigir preços

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

### Parâmetros
```
Table: [Choose table]
Column: [Choose column to edit]
Find: [Value to find]
Replace with: [New value]
Condition: [When to apply]
```

### Utilizações comuns
- Corrigir preços unitários
- Padronizar descrições
- Corrigir quantidades
- Atualizar números SKU

---

## Cartão: CALC_COLUMNS / Calculate Column Values

### Objetivo
Realiza um cálculo em colunas de tabela e armazena o resultado

### Quando utilizar
- Calcular totais de linha (Qtd. × Preço Unitário)
- Somar colunas
- Calcular descontos
- Calcular percentagens

### Como funciona
```
Column A (Quantity): 100
Column B (Unit Price): €50
    ↓
CALCULATE: A × B
    ↓
Column C (Line Total): €5000
```

### Tipos de cálculo

**Tipo 1: Multiplicação simples**
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

**Tipo 3: Cálculo de percentagem**
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

### Exemplo do mundo real

**Cálculo das linhas de uma fatura:**
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

### Parâmetros
```
Table: [Select table]
Column 1: [First column]
Operator: [×, +, -, ÷, %]
Column 2: [Second column] (if needed)
Result Column: [Where to put answer]
```

---

## Cartão: CALC_COLUMNS_REGEX / Calculate with Regex Pattern

### Objetivo
Calcula os valores de uma coluna com base na correspondência de padrões

### Quando utilizar
- Extrair valores de texto utilizando padrões
- Formatar dados com base em regras
- Converter valores com base em padrões
- Analisar texto estruturado

### Como funciona

**Correspondência de padrões regex:**
```
Original Value: "ABC-12345-XYZ"
Pattern: Extract numbers only
Calculation: Convert to "12345"
Result: "12345"
```

### Exemplo: Extrair o código do fornecedor

**Cenário: Os números de artigo contêm informações do fornecedor**
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

### Exemplo: Formatar números de telefone

**Cenário: Números de telefone sem formatação**
```
Original: "491234567890"
Pattern: Format as: +49 123 4567 890
Result: "+49 123 4567 890"
```

### Exemplo: Extrair preços de texto

**Cenário: Preços em formato de texto**
```
Original: "Price is 99.99 EUR"
Pattern: Extract number only
Result: "99.99"
```

### Parâmetros
```
Table: [Select table]
Column: [Column to analyze]
Regex Pattern: [Pattern to find]
Replacement: [What to replace with]
Result Column: [Where to store result]
```

### Padrões regex comuns
```
Numbers only: [0-9]+
Letters only: [a-zA-Z]+
First word: ^\w+
Extract €: €(\d+\.\d{2})
Date format: \d{4}-\d{2}-\d{2}
```

---

# Exemplos de cálculo

## Exemplo 1: Cálculo do total da fatura
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

## Exemplo 2: Cálculo de variação
```
PO Price: €100
Invoice Price: €103

Variance = |(Invoice - PO)| / PO × 100
Variance = |3| / 100 × 100 = 3%

Store in "Price_Variance%" column
```

## Exemplo 3: Aplicação de desconto
```
Original Price: €100
Discount %: 10%
Discount Amount: €100 × 0.10 = €10
Final Price: €100 - €10 = €90
```

---

# Exemplo de fluxo de trabalho de manipulação de campos

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

---

# Boas práticas

✅ **Faça:**
- Mantenha as fórmulas simples
- Teste os cálculos com dados de amostra
- Verifique se os resultados fazem sentido
- Documente o motivo da alteração dos campos
- Utilize a cópia de campo quando os dados são iguais

❌ **Não faça:**
- Criar referências circulares (A=B, B=A)
- Substituir dados importantes sem motivo
- Criar padrões regex demasiado complexos
- Esquecer-se de verificar os resultados dos cálculos
- Calcular na tabela/colunas erradas

---

# Resolução de problemas

## "O campo não é atualizado"
**Causa:** A condição não é cumprida ou o cartão não é acionado

**Solução:**
- Verifique se a condição é verdadeira
- Verifique se o cartão está no fluxo de trabalho
- Teste com dados de amostra
- Verifique se há erros de escrita no nome do campo

## "O resultado do cálculo está errado"
**Causa:** Colunas erradas selecionadas ou fórmula incorreta

**Solução:**
- Verifique as colunas de origem
- Verifique se a fórmula está correta
- Teste manualmente
- Reveja as casas decimais/o arredondamento

## "A tabela apresenta um erro"
**Causa:** A coluna referenciada não existe

**Solução:**
- Verifique a escrita do nome da coluna
- Verifique se a coluna tem dados
- Garanta que o tipo de dados da coluna corresponde ao cálculo
- Adicione as colunas em falta, se necessário

---

# Cartões relacionados

- **ACTION_COPY_DOCFIELD_TO_DOCFIELD** - Copiar valores
- **EDIT_COLUMN** - Alterar valores de tabela
- **CALC_COLUMNS** - Calcular fórmulas
- **ACTION_SET_FIELD_TO_TEXT** - Definir valores de texto
- **ACTION_SET_BOOLEAN_FIELD** - Marcar caixas
