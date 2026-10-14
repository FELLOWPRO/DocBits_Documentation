# Purchase Order (PO) Matching Cards - Complete Guide

Os cartões de correspondência de pedidos desta página ficam no grupo **And** do Construtor de fluxos de trabalho — comparam os dados da fatura com o pedido correspondente antes de as ações Then serem executadas:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Os cartões de correspondência de pedidos são adicionados ao grupo <strong>And</strong> através de <strong>Add Card</strong>.</p></figcaption></figure>

**Estado:** Abrange 15 cartões de comparação de PO com cálculos detalhados

---

## 📌 Informações de versão

**Cartão mais evoluído:** CONDITION_DOC_TO_PO_UNIT_PRICE (5 versões, v5 a mais recente)
**Outros cartões complexos:** CONDITION_OC_TO_PO_ITEMS (v4), CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY (v4)

**Padrões principais:**
- **v2 → v3+:** Adição de parâmetros de tolerância para uma correspondência flexível
- **v3 → v4:** Adição de parâmetros de modo de comparação
- **v4 → v5:** Tolerância melhorada com várias unidades (%, EUR, $, etc.)

📖 [Complete Version History](../../../changelog/release.md#-po-comparison--validation-cards) | [Card Version Database](../../../../DocFlow/docs/card_version.md)

---

## Compreender a correspondência de PO

{% embed url="https://youtu.be/qR-lrSaj4Ug" %}
DocBits PO Matching Tutorial: Auto/Manual Line Matching, Tolerances & Mismatch Indicators
{% endembed %}

Neste vídeo, vai aprender como funciona a correspondência de PO de ponta a ponta, incluindo as principais definições que controlam o comportamento da correspondência e como resolver discrepâncias rapidamente.

**O que vai aprender:**
*   O que é a correspondência de PO e porque é importante para a exatidão das faturas
*   Como configurar tolerâncias (diferenças permitidas) para quantidades, preços unitários, frete, encargos e impostos
*   Os 3 modos de correspondência baseados na quantidade:
    *   Ordered Quantity (comparar com a quantidade encomendada)
    *   Received Quantity (comparar com a quantidade rececionada)
    *   Received Delivery Open Quantity (rececionada menos as quantidades já correspondidas)
*   Como funciona a correspondência automática (números de artigo, quantidades, preços unitários, etc.)
*   Como fazer a correspondência manual de linhas com arrastar e largar
*   Como interpretar o estado da correspondência com indicadores de cor:
    *   Verde = correspondência total
    *   Laranja = discrepância (passe o cursor para ver detalhes na dica, como discrepância de quantidade/preço unitário/número de artigo)

Quando recebe uma fatura, esta deve corresponder à ordem de compra (PO) efetuada anteriormente. Os cartões de correspondência de PO verificam automaticamente se os dados da fatura correspondem aos dados da PO.

**A imagem geral:**
```
PO Placed     Invoice Arrives     PO Matching     Decision
(€100)    →   (€103)          →   (Check if       → Approve/Reject
Qty: 100      Qty: 100            within tolerance)
```

---

# 1. Correspondência total da ordem de compra

## Objetivo
Verifica se a fatura inteira corresponde à PO na perfeição ou dentro da tolerância

## Quando utilizar
- Antes de aprovar uma fatura
- Como verificação preliminar de qualidade
- Para identificar problemas cedo

## Como funciona
O sistema compara:
- Quantidades da fatura vs quantidades da PO
- Preços da fatura vs preços da PO
- Artigos da fatura vs artigos da PO
- Total da fatura vs total da PO

## Resultado
- **TRUE** (correspondência total): Tudo corresponde, prosseguir
- **FALSE** (discrepância): Algo não corresponde, necessita de revisão

## Exemplo
```
PO:
- Item ABC: Qty 100, Unit Price €50 = €5000
- Item XYZ: Qty 50, Unit Price €20 = €1000
- Total: €6000

Invoice:
- Item ABC: Qty 100, Unit Price €50 = €5000
- Item XYZ: Qty 50, Unit Price €20 = €1000
- Total: €6000

Result: ✅ FULL MATCH
```

---

# 2. Comparação de preço unitário (Documento vs PO)

## Objetivo
Compara o preço unitário da fatura com o preço unitário da PO

## Parâmetros
- **Unit Price Tolerance**: Permite uma variação até este montante
- **Tolerance Type**: Percentagem (%) ou absoluta (€/$)
- **Operator**: Is Equal to, Is Greater than, Is Less than, etc.

## Como funciona (tolerância em percentagem)

**Fórmula:**
```
Variance % = |(Invoice Price - PO Price)| / PO Price × 100

Check: Is Variance % ≤ Tolerance %?
```

**Exemplo passo a passo:**
```
Step 1: Get prices
  PO Unit Price: €100.00
  Invoice Unit Price: €103.00

Step 2: Calculate difference
  Difference = |€103.00 - €100.00| = €3.00

Step 3: Calculate percentage
  Percentage = (€3.00 / €100.00) × 100 = 3%

Step 4: Check tolerance (5% allowed)
  Is 3% ≤ 5%? YES ✅

Result: PASS - Within tolerance
```

## Exemplos do mundo real

### Exemplo 1: Pequeno aumento (aceite)
```
PO Price: €50.00
Invoice Price: €51.50
Tolerance: ±3%

Calculation:
  Variance = |(€51.50 - €50.00)| / €50.00 × 100
  Variance = €1.50 / €50.00 × 100 = 3%

Is 3% ≤ 3%? YES ✅ ACCEPT
```

### Exemplo 2: Grande aumento (rejeitado)
```
PO Price: €50.00
Invoice Price: €55.00
Tolerance: ±3%

Calculation:
  Variance = |(€55.00 - €50.00)| / €50.00 × 100
  Variance = €5.00 / €50.00 × 100 = 10%

Is 10% ≤ 3%? NO ❌ REJECT - NEEDS REVIEW
```

### Exemplo 3: Desconto (também verificado)
```
PO Price: €100.00
Invoice Price: €97.00
Tolerance: ±5%

Calculation:
  Variance = |(€97.00 - €100.00)| / €100.00 × 100
  Variance = €3.00 / €100.00 × 100 = 3%

Is 3% ≤ 5%? YES ✅ ACCEPT (Discount is within tolerance)
```

### Exemplo 4: Tolerância de valor absoluto
```
PO Price: €10.00
Invoice Price: €10.50
Tolerance: ±€1.00 (absolute, not %)

Calculation:
  Variance = |€10.50 - €10.00| = €0.50

Is €0.50 ≤ €1.00? YES ✅ ACCEPT
```

## O que fazer com os resultados

**Se PASS ✅:**
- Continuar para a verificação seguinte
- Ou aprovar a fatura
- Ou prosseguir com a exportação

**Se FAIL ❌:**
- Sinalizar para revisão manual
- Pedir explicação ao fornecedor
- Contactar a equipa de aquisições
- Aprovar com nota, se aceitável

---

# 3. Comparação de quantidade

## Objetivo
Verifica se a quantidade encomendada corresponde à quantidade faturada

## Parâmetros
- **Tolerance**: Montante ou % de diferença permitido
- **Operator**: Equals, Greater than, Less than
- **Quantity Type**: Ordered, Received, Open

## Exemplo de cálculo

**Tolerância em percentagem:**
```
Formula:
  Quantity Variance % = |(Invoice Qty - PO Qty)| / PO Qty × 100

Example:
  PO Quantity: 100 units
  Invoice Quantity: 103 units
  Tolerance: ±5%

  Variance = |(103 - 100)| / 100 × 100
  Variance = 3 / 100 × 100 = 3%

  Is 3% ≤ 5%? YES ✅ ACCEPT
```

**Tolerância absoluta:**
```
Formula:
  Quantity Variance = |Invoice Qty - PO Qty|

Example:
  PO Quantity: 100 units
  Invoice Quantity: 102 units
  Tolerance: ±5 units

  Variance = |102 - 100| = 2 units

  Is 2 units ≤ 5 units? YES ✅ ACCEPT
```

## Cenários do mundo real

### Entrega em excesso (mais do que o encomendado)
```
Ordered: 100 units
Invoiced: 110 units
Tolerance: ±5%

Variance = |(110-100)|/100 × 100 = 10%

Is 10% ≤ 5%? NO ❌

Decision: Contact supplier - more delivered than ordered
Possible reason: Error by supplier, partial shipment already received
```

### Entrega em falta (menos do que o encomendado)
```
Ordered: 100 units
Invoiced: 95 units
Tolerance: ±5%

Variance = |(95-100)|/100 × 100 = 5%

Is 5% ≤ 5%? YES ✅

Decision: Accept - within tolerance
Possible reason: Partial shipment, rest to follow
```

---

# 4. Preço combinado da diferença de quantidade

## Objetivo
Quando a quantidade difere, calcula se a diferença total de preço é aceitável

## Porque é importante
```
Scenario: You ordered 100 units but received 110
- Quantity is 10% over (bad)
- BUT: You're only charged for 10% extra
- Combined effect might be acceptable
```

## Cálculo

**Fórmula:**
```
Combined Variance = Quantity Variance × Price Variance

If both are within tolerance, combined is usually acceptable
```

**Exemplo:**
```
PO:
- Unit Price: €100
- Quantity: 100
- Total: €10,000

Invoice:
- Unit Price: €102 (2% higher)
- Quantity: 105 (5% higher)
- Total: €10,710

Analysis:
- Price variance: 2% ✅
- Quantity variance: 5% ✅
- Combined effect: 1.02 × 1.05 = 1.071 = 7.1% total increase

Is combined variance acceptable? Usually YES ✅
```

---

# 5. Comparação de ID de artigo / número de artigo do fornecedor

## Objetivo
Verifica se os artigos da fatura correspondem aos artigos da PO

## Como funciona

**Correspondência exata (a mais simples):**
```
PO Item ID: ABC-123
Invoice Item ID: ABC-123
Result: ✅ MATCH
```

**Número de artigo do fornecedor (mais comum):**
```
PO Item: ABC-123 (Our internal code)
Supplier Item: SUPP-456 (Their code for same item)
System matches these as same item
Result: ✅ MATCH
```

## Cenário: E se não corresponder?

```
PO Item: ABC-123 (Copper Wire, 2mm)
Invoice Item: ABC-124 (Steel Wire, 2mm)

Result: ❌ NO MATCH

Actions:
1. Is this a substitution? Check with procurement
2. Is this an error? Contact supplier
3. Is the description similar? Verify manually
```

---

# 6. Verificação do tipo de pedido

## Objetivo
Verifica se o tipo de ordem de compra está correto

## Tipos de pedido
- **Standard Order**: Compra regular
- **Rush Order**: Urgente, pode ter um prémio
- **Frame Agreement**: Contrato de longo prazo
- **Blanket Order**: Contrato em aberto
- **Consignment**: Só paga quando utilizado

## Exemplo de verificação
```
PO Order Type: Standard Order
Invoice Order Type: Standard Order
Result: ✅ MATCH

If mismatch: Could affect terms, payment, pricing
```

---

# 7. Verificação da data de entrega

## Objetivo
Verifica se a data de entrega corresponde à data prometida na PO

## Cálculo

**Entrega atrasada:**
```
Formula:
  Days Late = Invoice Delivery Date - PO Promised Date

Example:
  PO Promised: 2025-10-15
  Actual Delivery: 2025-10-22
  Days Late = 7 days

If tolerance is ±3 days:
  Is 7 ≤ 3? NO ❌ LATE
```

**Entrega antecipada:**
```
Formula:
  Days Early = PO Promised Date - Invoice Delivery Date

Example:
  PO Promised: 2025-10-15
  Actual Delivery: 2025-10-10
  Days Early = 5 days

Early delivery is usually OK ✅
Unless you need it at specific time
```

## Definições de tolerância
```
±3 days: Allow 3 days late or early
±5 days: Allow up to 5 days variance
0 days: Must match exactly
```

---

# 8. Verificação de encargos (impostos, expedição, etc.)

## Objetivo
Verifica se os encargos adicionais (impostos, expedição, processamento) correspondem à PO

## Encargos comuns
```
- Shipping: €50
- Handling: €10
- Packaging: €5
- Insurance: €15
- Taxes: €300
```

## Cálculo

**Exemplo: verificação de encargo de expedição**
```
PO Shipping: €50.00
Invoice Shipping: €51.00
Tolerance: ±3%

Variance = |€51.00 - €50.00| / €50.00 × 100 = 2%

Is 2% ≤ 3%? YES ✅ ACCEPT
```

**Exemplo: vários encargos**
```
PO Total Charges:
  - Shipping: €50
  - Taxes: €300
  - Handling: €10
  Total: €360

Invoice Total Charges:
  - Shipping: €50
  - Taxes: €312 (11% tax)
  - Handling: €10
  Total: €372

Difference: €12
Check if within tolerance ✅ or ❌
```

---

# 9. Verificação de impostos

## Objetivo
Verifica se os montantes de imposto são calculados corretamente

## Cálculo

**Fórmula:**
```
Tax Amount = Subtotal × Tax Rate

Example:
  Subtotal: €1000
  Tax Rate: 19%
  Expected Tax: €1000 × 0.19 = €190

Invoice Tax: €190
Match? YES ✅
```

**Problemas comuns:**
```
1. Tax rate changed (region-based)
2. Tax applied to wrong amount (before/after discounts)
3. Multiple tax rates (some items 7%, others 19%)
4. Tax exempt items (0% tax)
```

**Exemplo: tributação com várias taxas**
```
Item A: €100 @ 19% tax = €119
Item B: €100 @ 7% tax = €107
Item C: €100 @ 0% tax = €100
Total: €326

Invoice shows €325 (€1 error)

Check: Within tolerance or needs attention?
```

---

# 10. Correspondência de instalação/centro de custo

## Objetivo
Garante que a fatura é para a instalação/centro de custo correto

## Exemplo
```
PO is for:
- Facility: Berlin Plant
- Cost Center: CC-2025

Invoice should have:
- Facility: Berlin Plant ✅
- Cost Center: CC-2025 ✅

If different facility: May need different approval
```

---

# 11. Validação do estado do fornecedor

## Objetivo
Verifica se o fornecedor ainda está aprovado/ativo

## Tipos de estado
```
✅ ACTIVE: Approved, can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

## Exemplo de verificação
```
Supplier: ABC Corp
Status in Database: ACTIVE
Status when creating PO: ACTIVE
Status when invoice arrives: INACTIVE

Alert: Supplier status changed! Investigate why.
```

---

# Que tolerância devo utilizar?

## Tolerâncias estritas (menor risco, mais trabalho manual)
```
Use for:
- High-value items
- Items where exactness matters
- Regulated industries

Settings:
- Unit Price: ±1%
- Quantity: ±1%
- Delivery Date: ±1 day
- Charges: ±1%
```

## Tolerâncias moderadas (equilibradas)
```
Use for:
- Most business transactions
- Standard items
- Normal purchasing

Settings:
- Unit Price: ±3-5%
- Quantity: ±3-5%
- Delivery Date: ±3 days
- Charges: ±5%
```

## Tolerâncias amplas (maior risco, menos trabalho manual)
```
Use for:
- Low-value items
- Bulk purchases
- Supplier agreements with flexibility

Settings:
- Unit Price: ±10%
- Quantity: ±10%
- Delivery Date: ±7 days
- Charges: ±10%
```

---

# Exemplo de fluxo de trabalho de correspondência de PO

```
Invoice Arrives
    ↓
Condition: "Is amount > €5000?" → YES
    ↓
Check: Full Match? → NO (10% price difference)
    ↓
Check: Unit Price within 5%? → NO (12% difference)
    ↓
Check: Quantity within 5%? → YES (2% difference)
    ↓
Decision: FAIL - Price variance too high
    ↓
Flag for: Manual review / Buyer approval
    ↓
Wait for: Buyer comment
    ↓
If Approved: Continue to Export
If Rejected: Return to Supplier
```

---

# Resolução de problemas na correspondência de PO

## "PO Not Found"
```
Cause: Invoice PO number doesn't exist in system
Fix:
1. Verify PO number spelling
2. Check if PO was created
3. Verify PO is in correct organization
4. Ask supplier for PO reference
```

## "Items Don't Match"
```
Cause: Invoice items are different from PO items
Possible Reasons:
1. Substitution approved by procurement
2. Different item numbers for same item
3. Error by supplier
Fix: Contact procurement or supplier
```

## "Price Higher Than PO"
```
Cause: Invoice price > PO price
Possible Reasons:
1. Price increase approved
2. Supplier error
3. Currency difference
4. Additional services included
Fix: Verify with procurement
```

## "Delivery Date Wrong"
```
Cause: Invoice dated after promised delivery
Possible Reasons:
1. Shipment was delayed
2. Receiving date different from invoice date
3. Partial shipment
Fix: Check shipping documents or contact supplier
```

---

# Tabela de resumo

| Cartão | O que verifica | Cálculo principal | Tolerância comum |
|------|----------------|------------------|-----------------|
| Full Match | Tudo | Todas as verificações | Varia |
| Unit Price | Preço por unidade | Diferença em % ou € | ±3-5% |
| Quantity | Quantidade encomendada | Diferença em % ou unidades | ±3-5% |
| Combined Price | Total com alteração de qtd. | Qtd. × Preço | ±5-10% |
| Item ID | Artigos corretos | Correspondência de cadeia | Exata |
| Order Type | Tipo de compra | Correspondência de cadeia | Exata |
| Delivery Date | Quando chegou | Diferença em dias | ±3 dias |
| Charges | Taxas adicionais | Diferença em % ou € | ±5% |
| Tax | Montante de imposto | Cálculo de % de imposto | ±1% |
| Facility | Centro de custo | Correspondência de cadeia | Exata |
| Supplier | Aprovado? | Verificação de estado | Apenas ativo |

---

# Documentação relacionada

- Consulte o guia "Invoice Validation" para o fluxo de trabalho completo
- Consulte "Tolerance Settings" para os valores recomendados por setor
- Consulte "Exception Handling" para saber o que fazer com as falhas
- Contacte a sua equipa de aquisições para conhecer as políticas de tolerância específicas
