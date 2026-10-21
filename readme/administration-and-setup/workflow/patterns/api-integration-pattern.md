# Padrão de integração de API

**Tipo de padrão:** Integração **Complexidade:** Média **Configuração estimada:** 45–60 minutos **Casos de uso comuns:** Obtenção de dados externos, validação de preços, consulta de dados de referência

***

Este padrão é construído no **Construtor de fluxo de trabalho** (Workflow Dashboard → Workflow List → Add Workflow). Clique em **Adicionar cartão** para abrir a biblioteca de cartas e escolher as cartas utilizadas por este padrão — `CALL_API`, `CONDITION_HTTPS_REQUEST_STATUS`, `ACTION_SET_FIELD_TO_TEXT` e `CONDITION_COMPARE_TWO_DOCFIELD_VALUES`:

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-9a74b1360332-pt.png" alt="Cartões disponíveis na categoria selecionada. Configure os campos antes de utilizar. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real."><figcaption><p>Cartões disponíveis na categoria selecionada. Configure os campos antes de utilizar. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

***

## Visão geral do padrão

Este padrão demonstra como integrar o DocBits com APIs externas para obter, validar e armazenar dados de sistemas externos. É um dos padrões de workflow mais comuns para ligar o DocBits a sistemas de preços, serviços de validação, sistemas ERP e outras fontes de dados externas.

**O que este padrão faz:**

1. Chama uma API externa para obter dados
2. Valida a resposta da API
3. Armazena os dados da resposta em campos do documento
4. Toma decisões com base nos dados obtidos
5. Encaminha os documentos em conformidade

***

## Quando utilizar este padrão

Utilize este padrão quando precisar de:

* ✅ Obter preços em tempo real de sistemas externos
* ✅ Validar informações de fornecedores contra a base de dados de referência
* ✅ Consultar detalhes de produtos em sistemas de catálogo
* ✅ Obter taxas de câmbio de serviços de moeda
* ✅ Verificar endereços com serviços de geocodificação
* ✅ Consultar níveis de stock em sistemas de armazém
* ✅ Validar taxas de imposto em serviços fiscais

**Não utilize este padrão quando:**

* ❌ os dados já estiverem nos dados de referência do DocBits (utilize antes a consulta de dados de referência)
* ❌ o sistema externo não tiver uma API (utilize antes o padrão DocOperator Script)
* ❌ os dados raramente mudarem (considere uma importação manual)

***

## Exemplo completo de fluxo de trabalho

### Cenário: Validar o preço da fatura contra a API de preços atual

**Requisito de negócio:**

* O fornecedor envia uma fatura
* A fatura apresenta um preço unitário de 52,00 €
* Precisamos de verificar se corresponde à lista de preços atual do fornecedor
* Se o preço variar mais de 5 %, escalar para revisão

**Cartas de workflow utilizadas:**

1. CALL\_API – Obter o preço atual da API do fornecedor
2. CONDITION\_HTTPS\_REQUEST\_STATUS – Verificar se a chamada à API teve êxito
3. ACTION\_SET\_FIELD\_TO\_TEXT – Armazenar o preço da API num campo do documento
4. CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES – Comparar o preço da fatura com o preço da API
5. ACTION\_ASSIGN\_TO\_USER – Encaminhar com base no resultado da comparação
6. tasks\_create – Criar uma tarefa de revisão, se necessário

***

## Implementação passo a passo

### Passo 1: Chamar a API externa

**Carta:** CALL\_API ou ACTION\_CALL\_EXTERNAL\_API

**Configuração:**

```json
{
  "api_endpoint": "https://api.supplier-system.com/v1/pricing",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
  },
  "request_body": {
    "product_id": "{{DOCUMENT_FIELD:Product_Code}}",
    "supplier_id": "{{DOCUMENT_FIELD:Supplier_Code}}",
    "quantity": "{{DOCUMENT_FIELD:Quantity}}",
    "currency": "EUR"
  }
}
```

**Resposta esperada:**

```json
{
  "success": true,
  "data": {
    "product_id": "ABC123",
    "unit_price": 50.00,
    "currency": "EUR",
    "valid_until": "2025-12-31",
    "discount_applicable": true
  }
}
```

**Referência de guia:** [Guia Call API](../then/action/call-api-guide.md)

***

### Passo 2: Validar a resposta da API

**Carta:** CONDITION\_HTTPS\_REQUEST\_STATUS

**Configuração:**

```
Operator: IS EQUAL TO
Status Code: 200
```

**Lógica:**

```
IF API returns 200 (success):
  → Continue to store data
ELSE:
  → Route to "API Error" handling workflow
  → Send email notification
  → Create manual review task
```

**Referência de guia:** [Guia de cartas de condição – Estado HTTP](../and/condition-cards-complete-guide.md)

***

### Passo 3: Armazenar a resposta da API em campos do documento

**Carta:** ACTION\_SET\_FIELD\_TO\_TEXT (ou um setter de campo equivalente)

**Configuração:**

**Campo 1: Current\_API\_Price**

```
Field Name: Current_API_Price
Field Value: {{API_RESPONSE:data.unit_price}}
Field Type: Number
```

**Campo 2: API\_Price\_Valid\_Until**

```
Field Name: API_Price_Valid_Until
Field Value: {{API_RESPONSE:data.valid_until}}
Field Type: Date
```

**Campo 3: API\_Discount\_Available**

```
Field Name: API_Discount_Available
Field Value: {{API_RESPONSE:data.discount_applicable}}
Field Type: Boolean
```

**Resultado:** Os dados da API ficam agora armazenados em campos do documento para utilização posterior

**Referência de guia:** [Guia de manipulação de campos – Armazenamento de dados de API](../then/document-field/field-manipulation-guide.md)

***

### Passo 4: Comparar o preço da fatura com o preço da API

**Carta:** CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES

**Configuração:**

```
Field 1: Invoice_Unit_Price (from OCR extraction)
Field 2: Current_API_Price (from API response)
Operator: Calculate variance percentage
Tolerance: 5%
```

**Cálculo:**

```
Variance % = |(Invoice_Price - API_Price)| / API_Price × 100

Example:
  Invoice Price: €52.00
  API Price: €50.00
  Variance = |52 - 50| / 50 × 100 = 4%

  Is 4% ≤ 5% tolerance? YES ✅
  Result: PASS
```

**Referência de guia:** [Guia de cartas de condição – Comparação de campos](../and/condition-cards-complete-guide.md)

***

### Passo 5: Encaminhar com base no resultado da validação

**Cenário A: Preço dentro da tolerância (Pass)**

**Cartas:**

* ACTION\_SET\_FIELD\_TO\_TEXT
  * Definir o campo «Price\_Validation\_Status» = «PASS»
  * Definir o campo «Price\_Variance\_Percent» = «4%»
* ACTION\_APPROVE\_DOCUMENT
  * Aprovar o documento automaticamente

**Cenário B: Preço fora da tolerância (Fail)**

**Cartas:**

* ACTION\_SET\_FIELD\_TO\_TEXT
  * Definir o campo «Price\_Validation\_Status» = «FAIL»
  * Definir o campo «Price\_Variance\_Percent» = «12%» (exemplo)
* tasks\_create
  * Título da tarefa: «Review Price Variance - \{{DOCUMENT\_NUMBER\}}»
  * Descrição da tarefa: «Invoice price (€\{{Invoice\_Unit\_Price\}}) exceeds API price (€\{{Current\_API\_Price\}}) by \{{Price\_Variance\_Percent\}}»
  * Prioridade: Alta
* ACTION\_ASSIGN\_TO\_USER
  * Atribuir a: Direção de Compras
* ACTION\_SEND\_EMAIL\_TO\_GROUPS
  * Enviar notificação à equipa de Compras

**Referências de guia:**

* [Guia de atribuição](../then/assignee/assignment-user-guide.md)
* [Guia de atribuição de tarefas](../then/task/task-assignment-guide.md)
* [Guia de envio de e-mail](../then/action/send-email-groups-guide.md)

***

## Diagrama completo de fluxo de trabalho

```
DOCUMENT ARRIVES (Invoice with Product ABC123, Price €52)
│
├─ STEP 1: Call Pricing API
│  Card: CALL_API
│  Request: Get current price for ABC123
│  │
│  ├─ SUCCESS (200) ✅
│  │  Response: {"unit_price": 50.00}
│  │  │
│  │  ├─ STEP 2: Check API Status
│  │  │  Card: CONDITION_HTTPS_REQUEST_STATUS
│  │  │  Result: 200 = Success
│  │  │  │
│  │  │  ├─ STEP 3: Store API Data
│  │  │  │  Card: ACTION_SET_FIELD_TO_TEXT
│  │  │  │  Action: Store €50 in "Current_API_Price" field
│  │  │  │  │
│  │  │  │  ├─ STEP 4: Compare Prices
│  │  │  │  │  Card: CONDITION_COMPARE_TWO_DOCFIELD_VALUES
│  │  │  │  │  Calculate: Variance = |52-50|/50 = 4%
│  │  │  │  │  │
│  │  │  │  │  ├─ IF Variance ≤ 5% (PASS) ✅
│  │  │  │  │  │  │
│  │  │  │  │  │  ├─ Set Status Field: "PASS"
│  │  │  │  │  │  └─ Auto-Approve Document
│  │  │  │  │  │     → END (Document Approved)
│  │  │  │  │  │
│  │  │  │  │  └─ IF Variance > 5% (FAIL) ❌
│  │  │  │  │     │
│  │  │  │  │     ├─ Set Status Field: "FAIL"
│  │  │  │  │     ├─ Create Review Task
│  │  │  │  │     ├─ Assign to Procurement Manager
│  │  │  │  │     └─ Send Email Notification
│  │  │  │  │        → END (Pending Review)
│  │  │  │  │
│  │  │  │  └─ [Field storage complete]
│  │  │  │
│  │  │  └─ [Status check complete]
│  │  │
│  │  └─ [API data retrieved]
│  │
│  └─ ERROR (Non-200) ❌
│     │
│     ├─ Set Error Status
│     ├─ Create "API Error" Task
│     ├─ Assign to IT Support
│     └─ Send Email to Admin
│        → END (API Error - Manual Review)
```

***

## Modelos de configuração

### Modelo 1: Pedido GET simples (consulta)

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/lookup",
  "method": "GET",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}"
  },
  "parameters": {
    "id": "{{DOCUMENT_FIELD:Lookup_ID}}"
  }
}
```

**Utilização:** Consulta simples de dados por ID

***

### Modelo 2: Pedido POST com corpo (validação)

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/validate",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "document_number": "{{DOCUMENT_NUMBER}}",
    "supplier_id": "{{DOCUMENT_FIELD:Supplier_Code}}",
    "total_amount": "{{DOCUMENT_FIELD:Total_Amount}}",
    "currency": "{{DOCUMENT_FIELD:Currency}}"
  }
}
```

**Utilização:** Enviar dados do documento para validação

***

### Modelo 3: Pedido complexo com dados aninhados

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/process",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "document": {
      "type": "{{DOCUMENT_TYPE}}",
      "number": "{{DOCUMENT_NUMBER}}",
      "date": "{{DOCUMENT_FIELD:Invoice_Date}}"
    },
    "vendor": {
      "code": "{{DOCUMENT_FIELD:Supplier_Code}}",
      "name": "{{DOCUMENT_FIELD:Supplier_Name}}"
    },
    "items": [
      {
        "product": "{{TABLE_FIELD:Product_Code}}",
        "quantity": "{{TABLE_FIELD:Quantity}}",
        "unit_price": "{{TABLE_FIELD:Unit_Price}}"
      }
    ]
  }
}
```

**Utilização:** Processamento complexo de documentos com dados de tabela

***

## Tratamento de erros

### Erros comuns e soluções

#### Erro 1: Timeout de ligação

**Sintomas:**

* A API não responde
* O fluxo de trabalho fica em espera

**Solução:**

```
1. Check API endpoint URL (typo?)
2. Verify network connectivity
3. Check API service status
4. Implement timeout handling:

   IF CONDITION_HTTPS_REQUEST_STATUS = TIMEOUT:
     → Create "API Timeout" task
     → Assign to IT Support
     → Send email notification
     → Use fallback value (if available)
```

#### Erro 2: 401 não autorizado

**Sintomas:**

* A API devolve o estado 401
* Autenticação falhada

**Solução:**

```
1. Verify API key is correct
2. Check if API key expired
3. Ensure Authorization header formatted correctly
4. Implement auth error handling:

   IF CONDITION_HTTPS_REQUEST_STATUS = 401:
     → Create "API Auth Failed" task
     → Assign to Admin
     → Log error details
     → Stop workflow execution
```

#### Erro 3: Formato de resposta inválido

**Sintomas:**

* Resposta recebida, mas não analisável
* Faltam campos esperados

**Solução:**

```
1. Verify API documentation
2. Check response structure matches expectations
3. Implement response validation:

   IF API_RESPONSE:data.unit_price IS NULL:
     → Set default value
     → Create "Invalid Response" task
     → Log response for debugging
```

**Referência de guia:** [Call API – Resolução de problemas](../then/action/call-api-guide.md)

***

## Variantes avançadas

### Variante 1: Encadeamento de várias APIs

**Cenário:** São necessários dados de várias APIs

```
Step 1: Call Supplier API → Get Supplier Details
Step 2: Call Product API → Get Product Info (using Supplier ID from Step 1)
Step 3: Call Pricing API → Get Price (using Product ID from Step 2)
Step 4: Validate & Store all data
```

***

### Variante 2: Chamadas condicionais à API

**Cenário:** Chamar a API apenas em determinadas condições

```
IF DOCUMENT_TYPE = "Invoice" AND AMOUNT > 10000:
  → Call Pricing Validation API
  → Verify prices
ELSE:
  → Skip API call (not needed for small amounts)
```

***

### Variante 3: Caching de respostas da API

**Cenário:** Reduzir as chamadas à API com caching das respostas

```
1. Check if "API_Last_Called" date is today
2. IF Yes:
     → Use cached value from "Cached_API_Price" field
3. IF No:
     → Call API
     → Store response in "Cached_API_Price"
     → Set "API_Last_Called" to today
```

***

## Aspetos de desempenho

### Boas práticas

✅ **Recomendado:**

* Fazer caching das respostas da API sempre que possível
* Utilizar definições de timeout (30–60 segundos)
* Implementar lógica de repetição para falhas temporárias
* Registar as chamadas à API para resolução de problemas
* Monitorizar a utilização/custos da API
* Testar primeiro com documentos de exemplo

❌ **Não recomendado:**

* Chamar APIs de forma síncrona para cada documento (considerar processamento em lote)
* Ignorar erros de resposta
* Guardar credenciais não corrige fluxo de trabalho
* Efetuar chamadas desnecessárias à API
* Deixar timeouts por tratar

***

## Lista de verificação de testes

Antes da utilização em produção deste padrão:

* [ ] Testar a chamada à API com dados válidos
* [ ] Testar a chamada à API com dados inválidos
* [ ] Testar o cenário de timeout (o que acontece se a API estiver lenta?)
* [ ] Testar a falha de autenticação
* [ ] Testar um formato de resposta inválido
* [ ] Testar o armazenamento de campos (dados armazenados corretamente?)
* [ ] Testar a lógica de comparação (cálculo correto?)
* [ ] Testar o encaminhamento (os documentos vão para o local certo?)
* [ ] Testar o tratamento de erros (erros tratados de forma adequada?)
* [ ] Testar com volume elevado (desempenho aceitável?)

***

## Exemplos do mundo real

### Exemplo 1: Consulta de taxa de câmbio

**API:** https://api.exchangerate-api.com/v4/latest/USD

**Fluxo de trabalho:**

1. Extrair a moeda da fatura: «GBP»
2. Chamar a API de taxas de câmbio
3. Obter a taxa GBP→EUR
4. Calcular o equivalente em EUR
5. Armazenar no campo «Amount\_EUR»
6. Continuar o processamento com o montante em EUR

***

### Exemplo 2: Verificação de crédito do fornecedor

**API:** Serviço interno de verificação de crédito

**Fluxo de trabalho:**

1. Extrair o código do fornecedor
2. Chamar a API de verificação de crédito
3. Obter o estado de crédito: «APPROVED» ou «BLOCKED»
4. SE BLOQUEADO:
   * Parar o processamento
   * Criar uma tarefa urgente
   * Notificar a equipa financeira
5. SE APROVADO:
   * Continuar o fluxo de trabalho normal

***

### Exemplo 3: Enriquecimento dos dados de referência de produtos

**API:** Serviço de catálogo de produtos

**Fluxo de trabalho:**

1. Extrair o código do produto da fatura
2. Chamar a API de produtos
3. Obter: Nome do produto, categoria, conta razão
4. Armazenar em campos do documento
5. Utilizar para a contabilização automática

***

## Padrões relacionados

### Este padrão combina bem com:

* [**Padrão de Transformação de Dados**](data-transformation-pattern.md) – Transformar os dados de resposta da API
* [**Padrão de Lógica de Decisão**](decision-logic-pattern.md) – Encaminhar com base nos dados da API
* [**Padrão de Gestão de Tarefas**](task-management-pattern.md) – Criar tarefas para erros de API
* [**Padrão de Correspondência de Encomendas (PO Matching)**](po-matching-pattern.md) – Combinar preços de API com a validação de encomendas

***

## Guias relacionados

### Pré-requisitos

* [Guia Call API](../then/action/call-api-guide.md) – Documentação da carta de API
* [Guia de cartas de condição](../and/condition-cards-complete-guide.md) – Lógica de condições
* [Guia de manipulação de campos](../then/document-field/field-manipulation-guide.md) – Operações de campos

### Cartas relacionadas

* **CALL\_API** – [Guia Call API](../then/action/call-api-guide.md)
* **ACTION\_HTTPS\_REQUEST** – [Guia HTTPS Request](../then/action/https-request-guide.md)
* **CONDITION\_HTTPS\_REQUEST\_STATUS** – [Guia de cartas de condição](../and/condition-cards-complete-guide.md)
* **ACTION\_SET\_FIELD\_TO\_TEXT** – [Guia de manipulação de campos](../then/document-field/field-manipulation-guide.md)
* **CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES** – [Guia de cartas de condição](../and/condition-cards-complete-guide.md)

### Próximos passos

* Resolver erros de API: [Tratamento de erros](api-integration-pattern.md#tratamento-de-erros) acima
* Adicionar criação de tarefas: [Padrão de Gestão de Tarefas](task-management-pattern.md)
* Transformar dados: [Padrão de Transformação de Dados](data-transformation-pattern.md)

***

## Suporte e recursos

**Precisa de ajuda?**

* Ler [Call API – Resolução de problemas](../then/action/call-api-guide.md)
* Verificar os [códigos de resposta da API](../then/action/call-api-guide.md)
* Testar a API primeiro com o Postman
* Contactar o suporte do fornecedor da API

**Comentários:**

* Comunicar problemas do padrão para: docs@docbits.com
* Sugerir melhorias
* Partilhar os seus casos de uso

***

**Versão do padrão:** 1.0 **Última atualização:** 23 de outubro de 2025 **Dificuldade:** Média **Tempo estimado:** 45–60 minutos **Taxa de êxito:** Alta (com API estável)
