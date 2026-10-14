# Padrão de Transformação de Dados

**Tipo de padrão:** Processamento e manipulação de dados
**Complexidade:** Média
**Configuração estimada:** 30–45 minutos
**Casos de uso comuns:** Cálculos de campos, formatação de dados, conversão de moeda, conversão de unidades, enriquecimento de dados

---

Este padrão é construído no **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Clique em **Add Card** e abra a categoria **Document Field** — contém as cartas de leitura, escrita, cálculo e formatação que este padrão encadeia:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Biblioteca Add Card no Workflow Builder, agrupada por categoria"><figcaption><p>A biblioteca <strong>Add Card</strong> — as cartas de leitura/escrita de campos, de cálculo e de formatação encontram-se na categoria <strong>Document Field</strong>.</p></figcaption></figure>

---

## Visão geral do padrão

Este padrão demonstra como transformar, calcular, formatar e enriquecer dados de documentos em workflows do DocBits. A transformação de dados é essencial para preparar dados para exportação, efetuar cálculos, normalizar formatos e enriquecer documentos com informações adicionais.

**O que este padrão faz:**
1. Extrai dados de campos do documento
2. Efetua cálculos e transformações
3. Formata os dados de acordo com os padrões exigidos
4. Converte entre unidades, moedas e datas
5. Enriquece os documentos com dados derivados ou consultados
6. Valida e limpa os dados

---

## Quando utilizar este padrão

Utilize este padrão quando precisar de:
- ✅ Calcular totais, subtotais, impostos
- ✅ Converter moedas ou unidades
- ✅ Formatar datas, números, texto
- ✅ Derivar valores de campos existentes
- ✅ Enriquecer dados a partir de fontes externas
- ✅ Normalizar formatos de dados
- ✅ Limpar e validar dados
- ✅ Preparar dados para exportação

**Não utilize este padrão quando:**
- ❌ não for necessária qualquer transformação
- ❌ os dados já estiverem no formato correto
- ❌ bastar uma cópia simples de campos

---

## Tipos de transformação de dados

### 1. Cálculos

**Operações matemáticas:**
```
- Addition: Quantity + Bonus_Quantity = Total_Quantity
- Subtraction: Invoice_Total - Tax_Amount = Net_Amount
- Multiplication: Quantity × Unit_Price = Line_Total
- Division: Total_Amount / Quantity = Unit_Price
- Percentage: (Discount / Subtotal) × 100 = Discount_Percent
```

### 2. Operações de cadeias de carateres

**Manipulação de texto:**
```
- Concatenation: First_Name + " " + Last_Name = Full_Name
- Uppercase: "invoice" → "INVOICE"
- Lowercase: "SUPPLIER" → "supplier"
- Substring: "INV-2025-001" → "2025" (extract year)
- Replace: "01/23/2025" → "2025-01-23"
- Trim: "  ABC Corp  " → "ABC Corp"
```

### 3. Conversão de tipos de dados

**Conversões de tipo:**
```
- String to Number: "123.45" → 123.45
- Number to String: 123.45 → "123.45"
- Date to String: 2025-10-23 → "October 23, 2025"
- String to Date: "23.10.2025" → 2025-10-23
- Boolean to String: true → "Yes"
```

### 4. Conversões de unidades

**Conversões de unidades de medida:**
```
- Weight: kg → lbs, tons → kg
- Length: cm → inches, m → ft
- Volume: liters → gallons
- Temperature: Celsius → Fahrenheit
- Quantity: pieces → dozens, units → pallets
```

### 5. Conversões de moeda

**Aplicação de taxas de câmbio:**
```
- USD → EUR: Amount_USD × Rate = Amount_EUR
- Multi-currency: Convert all to base currency
- Historical rates: Use rate from invoice date
```

### 6. Transformações de datas

**Operações de datas:**
```
- Format change: 10/23/2025 → 2025-10-23
- Add days: Invoice_Date + 30 = Due_Date
- Calculate age: Today - Invoice_Date = Age_Days
- Extract parts: "2025-10-23" → Year: 2025, Month: 10, Day: 23
```

---

## Exemplo completo de workflow

### Cenário: Cálculo do total da fatura e enriquecimento de dados

**Requisito de negócio:**
- Extrair as posições da fatura
- Calcular os totais por posição (Quantidade × Preço)
- Calcular o subtotal (soma dos totais por posição)
- Calcular o montante de imposto (Subtotal × Taxa de imposto)
- Calcular o total geral (Subtotal + Imposto)
- Converter para EUR caso a fatura esteja noutra moeda
- Formatar os montantes para 2 casas decimais
- Acrescentar a conta razão com base na categoria do produto
- Validar os cálculos contra o total da fatura
- Assinalar se o desvio for > 1 %

**Cartas de workflow utilizadas:**
1. ACTION_CALCULATE_FIELD – Efetuar cálculos
2. ACTION_SET_FIELD_TO_TEXT – Armazenar os resultados
3. ACTION_COPY_FIELD_VALUE – Copiar valores
4. CALL_API – Obter taxas de câmbio (se necessário)
5. CONDITION_COMPARE_TWO_DOCFIELD_VALUES – Validar os cálculos
6. ACTION_SET_FIELD_FROM_MASTER_DATA – Enriquecer com contas razão

---

## Implementação passo a passo

### Passo 1: Cálculos por posição

**Calcular os totais por posição:**

**Carta:** ACTION_CALCULATE_FIELD

**Para cada posição:**
```
Field: Line_Total
Formula: {{TABLE_FIELD:Quantity}} * {{TABLE_FIELD:Unit_Price}}
Result Type: Number
Decimal Places: 2
```

**Exemplo:**
```
Line 1:
  Quantity: 100
  Unit Price: €50.00
  Calculation: 100 × 50.00 = €5,000.00
  Store in: Line_Total

Line 2:
  Quantity: 50
  Unit Price: €20.00
  Calculation: 50 × 20.00 = €1,000.00
  Store in: Line_Total

Line 3:
  Quantity: 25
  Unit Price: €15.50
  Calculation: 25 × 15.50 = €387.50
  Store in: Line_Total
```

**Referência de guia:** [Guia de manipulação de campos – Cálculos](../then/document-field/field-manipulation-guide.md#calculate-field)

---

### Passo 2: Calcular o subtotal do documento

**Somar todos os totais por posição:**

**Carta:** ACTION_CALCULATE_FIELD

**Configuração:**
```
Field: Calculated_Subtotal
Formula: SUM({{TABLE_COLUMN:Line_Total}})
Result Type: Number
Decimal Places: 2
```

**Exemplo:**
```
Line 1 Total: €5,000.00
Line 2 Total: €1,000.00
Line 3 Total: €387.50

Subtotal = 5000 + 1000 + 387.50 = €6,387.50
Store in: Calculated_Subtotal
```

---

### Passo 3: Calcular o montante de imposto

**Aplicar a taxa de imposto ao subtotal:**

**Carta:** ACTION_CALCULATE_FIELD

**Configuração:**
```
Field: Calculated_Tax_Amount
Formula: {{Calculated_Subtotal}} * ({{Tax_Rate}} / 100)
Result Type: Number
Decimal Places: 2
```

**Exemplo:**
```
Calculated_Subtotal: €6,387.50
Tax_Rate: 19% (VAT)

Tax Amount = 6387.50 × (19 / 100)
          = 6387.50 × 0.19
          = €1,213.63

Store in: Calculated_Tax_Amount
```

---

### Passo 4: Calcular o total geral

**Adicionar o subtotal e o imposto:**

**Carta:** ACTION_CALCULATE_FIELD

**Configuração:**
```
Field: Calculated_Grand_Total
Formula: {{Calculated_Subtotal}} + {{Calculated_Tax_Amount}}
Result Type: Number
Decimal Places: 2
```

**Exemplo:**
```
Calculated_Subtotal: €6,387.50
Calculated_Tax_Amount: €1,213.63

Grand Total = 6387.50 + 1213.63 = €7,601.13

Store in: Calculated_Grand_Total
```

---

### Passo 5: Conversão de moeda (se necessário)

**Verificar se é necessária uma conversão:**

**Carta:** CONDITION_DOC_FIELD_IS

**Configuração:**
```
Field: Invoice_Currency
Operator: IS NOT EQUAL TO
Value: EUR
```

**Se for necessária uma conversão:**

**Passo 5a: Obter a taxa de câmbio**

**Carta:** CALL_API

**Configuração:**
```
Endpoint: https://api.exchangerate-api.com/v4/latest/{{Invoice_Currency}}
Method: GET
Response Path: rates.EUR
Store in: Exchange_Rate_To_EUR
```

**Exemplo:**
```
Invoice Currency: USD
API Response: {
  "base": "USD",
  "rates": {
    "EUR": 0.92
  }
}

Exchange_Rate_To_EUR = 0.92
```

**Passo 5b: Converter os montantes**

**Carta:** ACTION_CALCULATE_FIELD

**Configuração:**
```
Field: Grand_Total_EUR
Formula: {{Calculated_Grand_Total}} * {{Exchange_Rate_To_EUR}}
Result Type: Number
Decimal Places: 2
```

**Exemplo:**
```
Grand Total (USD): $7,601.13
Exchange Rate: 0.92

Grand Total (EUR) = 7601.13 × 0.92 = €6,993.04

Store in: Grand_Total_EUR
```

**Referência de guia:** [Padrão de Integração de API – Conversão de moeda](api-integration-pattern.md#exemplo-1-consulta-de-taxa-de-câmbio)

---

### Passo 6: Enriquecimento de dados – Acrescentar contas razão

**Consultar a conta razão pela categoria do produto:**

**Carta:** ACTION_SET_FIELD_FROM_MASTER_DATA

**Configuração:**
```
Lookup Table: GL_Account_Mapping
Lookup Key: {{TABLE_FIELD:Product_Category}}
Return Field: GL_Account_Number
Store in: GL_Account
```

**Exemplo:**
```
Line 1:
  Product Category: "Office Supplies"
  Lookup → GL_Account_Mapping table
  Result: GL Account "4200-100" (Office Expense)

Line 2:
  Product Category: "IT Equipment"
  Lookup → GL_Account_Mapping table
  Result: GL Account "6100-200" (IT Assets)

Line 3:
  Product Category: "Services"
  Lookup → GL_Account_Mapping table
  Result: GL Account "5000-300" (Services Expense)
```

**Referência de guia:** [Guia de manipulação de campos – Dados de referência](../then/document-field/field-manipulation-guide.md#master-data-lookup)

---

### Passo 7: Validar os cálculos

**Comparar a soma calculada com o total da fatura:**

**Carta:** CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**Configuração:**
```
Field 1: Calculated_Grand_Total
Field 2: Invoice_Total (from OCR)
Operator: Calculate Variance Percentage
Tolerance: 1%
```

**Cálculo:**
```
Variance % = |Calculated - Invoice| / Invoice × 100

Example:
  Calculated Total: €7,601.13
  Invoice Total: €7,600.00

  Variance = |7601.13 - 7600.00| / 7600.00 × 100
          = 1.13 / 7600.00 × 100
          = 0.015%

  Is 0.015% ≤ 1% tolerance? YES ✅
  Result: PASS (calculations match invoice)
```

**Lógica:**
```
IF Variance ≤ 1%:
  Set Validation_Status = "PASS"
  Continue processing
ELSE:
  Set Validation_Status = "FAIL"
  Create review task
  Flag for manual verification
```

**Referência de guia:** [Guia de cartas de condição – Comparação de campos](../and/condition-cards-complete-guide.md#field-comparison)

---

### Passo 8: Formatar os dados para exportação

**Normalizar os formatos:**

**Carta:** ACTION_SET_FIELD_TO_TEXT

**Formatação de datas:**
```
Field: Invoice_Date_Formatted
Value: FORMATDATE({{Invoice_Date}}, "YYYY-MM-DD")
Example: 10/23/2025 → 2025-10-23
```

**Formatação de números:**
```
Field: Amount_Formatted
Value: FORMATNUMBER({{Grand_Total_EUR}}, 2, ",", ".")
Example: 7601.13 → 7.601,13 (German format)
```

**Formatação de texto:**
```
Field: Supplier_Name_Upper
Value: UPPERCASE({{Supplier_Name}})
Example: "ABC Corporation" → "ABC CORPORATION"
```

---

## Transformações avançadas

### Transformação 1: Cálculo de imposto em vários níveis

**Cenário:** Taxas de imposto diferentes por posição

```
Line 1: Product A (Tax Rate 19%)
Line 2: Product B (Tax Rate 7% - reduced)
Line 3: Product C (Tax Rate 0% - exempt)

Calculation:
  Line 1 Tax = €5,000.00 × 0.19 = €950.00
  Line 2 Tax = €1,000.00 × 0.07 = €70.00
  Line 3 Tax = €387.50 × 0.00 = €0.00

  Total Tax = €950.00 + €70.00 + €0.00 = €1,020.00
```

**Implementação:**
```
For each line:
  1. Get product tax category
  2. Lookup applicable tax rate
  3. Calculate: Line_Net × Tax_Rate = Line_Tax
  4. Sum all Line_Tax values = Total_Tax
```

---

### Transformação 2: Cálculo de descontos

**Cenário:** Aplicar desconto de quantidade e desconto de pronto pagamento

```
Original Subtotal: €10,000.00

Step 1: Volume Discount (10% for orders > €5,000)
  Discount = €10,000.00 × 0.10 = €1,000.00
  After Volume Discount = €10,000.00 - €1,000.00 = €9,000.00

Step 2: Early Payment Discount (2% if paid within 10 days)
  Discount = €9,000.00 × 0.02 = €180.00
  After Payment Discount = €9,000.00 - €180.00 = €8,820.00

Step 3: Calculate Tax (on discounted amount)
  Tax = €8,820.00 × 0.19 = €1,675.80

Final Total = €8,820.00 + €1,675.80 = €10,495.80
```

**Implementação:**
```
1. Check order value for volume discount eligibility
2. Calculate volume discount
3. Apply volume discount to subtotal
4. Check payment terms for early payment discount
5. Calculate early payment discount
6. Apply early payment discount
7. Calculate tax on final discounted amount
8. Calculate grand total
```

---

### Transformação 3: Conversão da unidade de medida

**Cenário:** Converter a unidade de medida da fatura para a unidade padrão

```
Invoice shows:
  Product: Steel Rods
  Quantity: 50
  Unit: Meters
  Unit Price: €10.00/meter
  Line Total: €500.00

Company standard UOM: Feet

Conversion:
  1 meter = 3.28084 feet

  Quantity (feet) = 50 meters × 3.28084 = 164.042 feet
  Unit Price (feet) = €10.00/meter ÷ 3.28084 = €3.05/foot

  Verification: 164.042 feet × €3.05/foot ≈ €500.00 ✅
```

**Implementação:**
```
1. Identify invoice UOM
2. Get conversion factor to standard UOM
3. Convert quantity
4. Convert unit price
5. Verify line total remains same
6. Store both original and converted values
```

---

### Transformação 4: Cálculos de datas

**Cenário:** Calcular condições de pagamento e datas de vencimento

```
Invoice Date: 2025-10-23
Payment Terms: NET30

Calculations:
  Due Date = Invoice Date + 30 days = 2025-11-22

  Early Payment Discount Available If:
    Payment Date ≤ Invoice Date + 10 days
    Discount End Date = 2025-11-02

  Days Until Due = Due Date - Today
    If Today = 2025-10-23: Days = 30
    If Today = 2025-11-15: Days = 7
    If Today = 2025-11-23: Days = -1 (overdue)
```

**Implementação:**
```
1. Extract Invoice_Date
2. Extract Payment_Terms (e.g., "NET30", "NET60", "2/10 NET30")
3. Parse payment terms
4. Calculate Due_Date
5. Calculate Discount_End_Date (if applicable)
6. Calculate Days_Until_Due
7. Set Status: "Current", "Due Soon", "Overdue"
```

---

### Transformação 5: Análise e extração de texto

**Cenário:** Extrair dados estruturados de texto não estruturado

```
Original Field: "PO-2025-ABC-12345-REV2"

Extract:
  Year: "2025"
  Department: "ABC"
  PO Number: "12345"
  Revision: "2"

Method:
  Split by delimiter "-"
  Array: ["PO", "2025", "ABC", "12345", "REV2"]

  Extract:
    Year = Array[1] = "2025"
    Department = Array[2] = "ABC"
    PO_Number = Array[3] = "12345"
    Revision = Extract digits from Array[4] = "2"
```

---

## Diagrama completo do workflow de transformação

```
INVOICE DATA EXTRACTED
│
├─ STEP 1: LINE ITEM CALCULATIONS
│  For each line:
│    Quantity × Unit_Price = Line_Total
│  Result: Line totals calculated
│
├─ STEP 2: SUBTOTAL CALCULATION
│  SUM(All Line_Totals) = Subtotal
│  Result: €6,387.50
│
├─ STEP 3: TAX CALCULATION
│  Subtotal × Tax_Rate = Tax_Amount
│  €6,387.50 × 19% = €1,213.63
│
├─ STEP 4: GRAND TOTAL CALCULATION
│  Subtotal + Tax_Amount = Grand_Total
│  €6,387.50 + €1,213.63 = €7,601.13
│
├─ STEP 5: CURRENCY CHECK
│  │
│  ├─ Currency = EUR? YES
│  │  → Skip conversion
│  │  → Use Grand_Total as is
│  │
│  └─ Currency ≠ EUR? NO (e.g., USD)
│     │
│     ├─ Call Exchange Rate API
│     │  Get: USD → EUR rate (0.92)
│     │
│     ├─ Convert Amount
│     │  $7,601.13 × 0.92 = €6,993.04
│     │
│     └─ Store converted amount
│        Grand_Total_EUR = €6,993.04
│
├─ STEP 6: DATA ENRICHMENT
│  For each line:
│    Lookup Product_Category → GL_Account
│    Store GL_Account in line item
│  Result: All lines have GL accounts
│
├─ STEP 7: VALIDATION
│  │
│  ├─ Compare Calculated vs Invoice Total
│  │  Variance = |Calculated - Invoice| / Invoice × 100
│  │
│  ├─ Variance ≤ 1%? ✅
│  │  Set Validation_Status = "PASS"
│  │  Continue processing
│  │
│  └─ Variance > 1%? ❌
│     Set Validation_Status = "FAIL"
│     Create review task
│     Flag for manual check
│
├─ STEP 8: FORMATTING
│  │
│  ├─ Format Dates
│  │  10/23/2025 → 2025-10-23
│  │
│  ├─ Format Numbers
│  │  7601.13 → 7.601,13 (locale-specific)
│  │
│  ├─ Format Text
│  │  "abc corp" → "ABC CORP"
│  │
│  └─ Format for Export
│     All fields in ERP-compatible format
│
└─ TRANSFORMATION COMPLETE
   Document ready for next workflow step
```

---

## Modelos de configuração

### Modelo 1: Cálculos de faturas padrão

```json
{
  "transformations": [
    {
      "step": 1,
      "name": "Calculate Line Totals",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Quantity}} * {{Unit_Price}}",
      "result_field": "Line_Total"
    },
    {
      "step": 2,
      "name": "Calculate Subtotal",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "SUM({{Line_Total}})",
      "result_field": "Calculated_Subtotal"
    },
    {
      "step": 3,
      "name": "Calculate Tax",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Calculated_Subtotal}} * {{Tax_Rate}} / 100",
      "result_field": "Calculated_Tax"
    },
    {
      "step": 4,
      "name": "Calculate Total",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Calculated_Subtotal}} + {{Calculated_Tax}}",
      "result_field": "Calculated_Total"
    }
  ]
}
```

---

### Modelo 2: Workflow de conversão de moeda

```json
{
  "currency_conversion": {
    "check_needed": {
      "card": "CONDITION_DOC_FIELD_IS",
      "field": "Invoice_Currency",
      "operator": "NOT EQUAL TO",
      "value": "EUR"
    },
    "get_rate": {
      "card": "CALL_API",
      "endpoint": "https://api.exchangerate.com/v1/rates/{{Invoice_Currency}}",
      "method": "GET",
      "response_path": "rates.EUR"
    },
    "convert": {
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Amount}} * {{Exchange_Rate}}",
      "result_field": "Amount_EUR"
    },
    "store_details": {
      "original_currency": "{{Invoice_Currency}}",
      "original_amount": "{{Amount}}",
      "exchange_rate": "{{Exchange_Rate}}",
      "converted_amount": "{{Amount_EUR}}",
      "conversion_date": "{{Today}}"
    }
  }
}
```

---

## Tratamento de erros

### Erros comuns de transformação

**Erro 1: Divisão por zero**
```
Problem: Unit_Price = Total / Quantity, but Quantity = 0

Solution:
  IF Quantity = 0 OR Quantity IS NULL:
    Set Unit_Price = 0
    Flag for review
  ELSE:
    Calculate normally
```

**Erro 2: Formato de número inválido**
```
Problem: Field contains "€1,234.56" but need number 1234.56

Solution:
  1. Remove currency symbols
  2. Remove thousand separators
  3. Convert decimal separator if needed
  4. Parse to number
  5. Validate result
```

**Erro 3: Falha na análise da data**
```
Problem: Date in unexpected format

Solution:
  1. Try multiple date formats
  2. If all fail: Set to null
  3. Flag for manual review
  4. Log original value
```

**Erro 4: Fator de conversão em falta**
```
Problem: Unknown UOM conversion

Solution:
  1. Check conversion table
  2. If not found: Skip conversion
  3. Flag for admin to add conversion
  4. Use original values
```

---

## Lista de verificação de testes

- [ ] Todos os cálculos produzem resultados corretos
- [ ] A precisão decimal é mantida
- [ ] As conversões de moeda estão corretas
- [ ] Os cálculos de datas estão corretos
- [ ] As transformações de texto funcionam
- [ ] Os valores nulos/vazios são tratados
- [ ] A divisão por zero é evitada
- [ ] Os formatos de número são validados
- [ ] As regras de arredondamento são aplicadas corretamente
- [ ] Todos os campos transformados são preenchidos
- [ ] A validação deteta erros
- [ ] O formato de exportação está correto

---

## Padrões relacionados

### Padrões que combinam bem:

- **[Padrão de Integração de API](api-integration-pattern.md)** – Obter taxas de câmbio e dados de enriquecimento
- **[Padrão de Correspondência de Encomendas (PO Matching)](po-matching-pattern.md)** – Cálculos de desvios
- **[Padrão de Lógica de Decisão](decision-logic-pattern.md)** – Encaminhar com base nos valores calculados
- **[Padrão de Gestão de Tarefas](task-management-pattern.md)** – Criar tarefas em caso de falhas de validação

---

## Guias relacionados

### Pré-requisitos
- [Guia de manipulação de campos](../then/document-field/field-manipulation-guide.md) – Todas as operações de campos
- [Guia de cartas de condição](../and/condition-cards-complete-guide.md) – Condições de validação
- [Guia Call API](../then/action/call-api-guide.md) – Obtenção de dados externos

### Cartas relacionadas
- **ACTION_CALCULATE_FIELD** – [Guia de manipulação de campos](../then/document-field/field-manipulation-guide.md#calculate-field)
- **ACTION_SET_FIELD_TO_TEXT** – [Guia de manipulação de campos](../then/document-field/field-manipulation-guide.md#set-field)
- **ACTION_COPY_FIELD_VALUE** – [Guia de manipulação de campos](../then/document-field/field-manipulation-guide.md#copy-field)
- **CALL_API** – [Guia Call API](../then/action/call-api-guide.md)
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** – [Guia de cartas de condição](../and/condition-cards-complete-guide.md)

### Próximos passos
- Validar resultados: [Padrão de Lógica de Decisão](decision-logic-pattern.md)
- Criar tarefas para erros: [Padrão de Gestão de Tarefas](task-management-pattern.md)
- Utilizar na correspondência de encomendas: [Padrão de Correspondência de Encomendas (PO Matching)](po-matching-pattern.md)

---

**Versão do padrão:** 1.0
**Última atualização:** 23 de outubro de 2025
**Dificuldade:** Média
**Tempo estimado:** 30–45 minutos
**Taxa de êxito:** Alta
