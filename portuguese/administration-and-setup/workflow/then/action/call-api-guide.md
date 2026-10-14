# Call External API

Estes cartões ficam no grupo **Then** do Construtor de fluxos de trabalho — as ações executadas assim que as condições When/And são atendidas:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Os cartões são adicionados ao grupo <strong>Then</strong> através de <strong>Add Card</strong>.</p></figcaption></figure>

## Objetivo
Este cartão permite-lhe enviar dados para um site ou serviço externo e receber informações de volta. Pense nisto como enviar uma pergunta a um serviço externo e obter uma resposta que pode utilizar no seu fluxo de trabalho.

**Exemplo do mundo real:** A sua empresa utiliza um sistema de preços noutro site. Este cartão pode pedir automaticamente a esse sistema de preços o preço atual de um artigo e trazer esse preço para o seu documento.

---

## Quando utilizar este cartão

Utilize este cartão quando precisar de:
- Obter informações de um serviço externo (como preços, validação ou dados de consulta)
- Enviar informações do documento para outro sistema para processamento
- Integrar com serviços de terceiros
- Obter dados automaticamente sem consultas manuais
- Ligar vários sistemas empresariais entre si

**Cenários comuns:**
- Consultar informações de fornecedores numa base de dados
- Obter preços em tempo real de um serviço de preços
- Validar dados num sistema externo
- Obter informações de expedição de um fornecedor de logística

---

## Como funciona

1. **Condition Check**: O fluxo de trabalho verifica primeiro se as condições nas secções "Where" e "And" são cumpridas
2. **Prepare Data**: O cartão recolhe os parâmetros que configurou
3. **Send Request**: Envia os seus dados para a API/serviço externo
4. **Receive Response**: O serviço externo responde com dados
5. **Continue**: O fluxo de trabalho utiliza estes dados nos cartões seguintes

---

## Parâmetros explicados

### API Endpoint URL
**O que é:** O endereço do serviço externo com o qual pretende comunicar

**Exemplo:** `https://api.supplier-system.com/product/pricing`

**Como encontrá-lo:** Peça à sua equipa de TI ou ao fornecedor do serviço o endpoint da API

---

### HTTP Method
**O que é:** O tipo de pedido a enviar

**Opções:**
- **GET**: Pedir informações (como fazer uma pergunta)
- **POST**: Enviar novos dados
- **PUT**: Atualizar dados existentes
- **DELETE**: Remover dados

**O mais comum:** GET (para obter informações)

---

### Headers
**O que é:** Instruções adicionais para o serviço que está a chamar

**Exemplo:**
```
Authorization: Bearer your-api-key
Content-Type: application/json
```

**Porque é necessário:** Os serviços exigem frequentemente autenticação ou instruções de formato específicas

---

### Parameters (Query Parameters)
**O que é:** Informações extra passadas no URL

**Exemplo:**
```
?supplier_id=12345&currency=USD
```

**Exemplo real:** Se estiver a pedir preços, os parâmetros podem incluir o ID do fornecedor e a moeda

---

### Request Data (Body)
**O que é:** As informações que está a enviar para o serviço

**Exemplo:**
```json
{
  "product_id": "ABC123",
  "quantity": 100,
  "currency": "EUR"
}
```

**Quando é utilizado:** Ao utilizar os métodos POST ou PUT

---

## Exemplo passo a passo

### Cenário: Obter preços de fornecedor em tempo real

**Configuração:**
1. **Card Type:** Call API
2. **API Endpoint:** `https://api.suppliers.com/v1/prices`
3. **Method:** POST
4. **Headers:** `Authorization: Bearer YOUR-API-KEY`
5. **Request Data:**
   ```json
   {
     "product_id": "ABC123",
     "quantity": 100
   }
   ```

**O que acontece:**
1. O documento chega com Product ID: ABC123, Quantity: 100
2. O cartão envia o pedido à API do fornecedor
3. A API do fornecedor responde com: `{"unit_price": 25.50, "total_price": 2550}`
4. O fluxo de trabalho continua com estas informações de preço
5. O cartão seguinte pode utilizar estes dados para validar o preço da fatura

---

## Passos de configuração

### 1. Obter informações da API
Contacte o fornecedor do serviço externo e solicite:
- [ ] URL do endpoint da API
- [ ] Método de autenticação (chave de API, nome de utilizador/palavra-passe, OAuth)
- [ ] Parâmetros necessários
- [ ] Formato de resposta esperado
- [ ] Limites de taxa ou quotas

### 2. Configurar o cartão
1. Introduza o URL do endpoint da API
2. Selecione o método HTTP (normalmente GET ou POST)
3. Adicione cabeçalhos de autenticação, se necessário
4. Adicione os parâmetros necessários
5. Formate os dados do pedido como JSON, se necessário

### 3. Testar o cartão
1. Utilize um documento de teste
2. Execute o fluxo de trabalho
3. Verifique se a resposta é recebida corretamente
4. Verifique se o formato dos dados corresponde ao esperado

---

## Cenários de resposta comuns

### Resposta bem-sucedida (Status Code 200)
```json
{
  "success": true,
  "data": {
    "price": 150,
    "currency": "EUR",
    "delivery_days": 5
  }
}
```
✅ Os dados estão disponíveis para serem utilizados pelos cartões seguintes

### Resposta de erro (Status Code 404)
```json
{
  "error": "Product not found"
}
```
⚠️ A API não conseguiu encontrar o que procura

### Timeout
O serviço externo não respondeu dentro do tempo limite
⚠️ Verifique se o serviço está disponível ou se o URL do endpoint está correto

---

## Exemplos de fluxos de trabalho

### Exemplo 1: Validação automática de preços
**Cenário:** Validar os preços da fatura em relação aos preços atuais do fornecedor

**Fluxo:**
1. O documento chega com uma linha de fatura (Product: A123, Price: €50)
2. **Call API Card** → Pergunta à API do fornecedor: "Qual é o preço atual de A123?"
3. O fornecedor responde: "€48"
4. **Condition Card** → Verifica se o preço da fatura (€50) está dentro de 5% do preço atual (€48)
5. **Approval Card** → Aprova se estiver dentro da tolerância

### Exemplo 2: Consulta automática de fornecedor
**Cenário:** Obter os dados mestre do fornecedor a partir da base de dados central

**Fluxo:**
1. A fatura chega com o Supplier Code: SUPP-789
2. **Call API Card** → Pergunta ao sistema: "Dá-me os detalhes do fornecedor SUPP-789"
3. O sistema responde com: Nome, Contacto, Condições, etc.
4. **Set Field Cards** → Preenche os campos do documento com estes dados
5. **Export Card** → Exporta com as informações completas

### Exemplo 3: Custos de expedição em tempo real
**Cenário:** Obter o custo de expedição automático com base no destino

**Fluxo:**
1. O documento tem o endereço de entrega
2. **Call API Card** → Pergunta ao fornecedor de expedição: "Qual é o custo para [address]?"
3. O fornecedor responde com o custo de expedição
4. **Calculate Card** → Adiciona a expedição ao montante total da fatura
5. **Export Card** → Envia com o total atualizado

---

## Resolução de problemas

### Erro "Connection Timeout"
**Causa:** O serviço da API não está a responder

**Soluções:**
- [ ] Verifique se o serviço está disponível (visite o site)
- [ ] Verifique se o URL do endpoint está correto (sem erros de escrita)
- [ ] Verifique a ligação à Internet
- [ ] Contacte o fornecedor do serviço
- [ ] Verifique se o serviço tem limites de taxa (está a enviar demasiados pedidos)

### Erro "Unauthorized" ou "403 Forbidden"
**Causa:** A autenticação falhou

**Soluções:**
- [ ] Verifique se a sua chave de API está correta
- [ ] Verifique se a sua chave de API expirou
- [ ] Garanta que o cabeçalho de autenticação está formatado corretamente
- [ ] Verifique se tem permissões para este endpoint

### Erro "Bad Request" ou "400 Error"
**Causa:** O formato dos dados do pedido está incorreto

**Soluções:**
- [ ] Verifique a sintaxe JSON (vírgulas, aspas em falta, etc.)
- [ ] Verifique se todos os campos obrigatórios estão incluídos
- [ ] Verifique se os nomes dos parâmetros correspondem ao que o serviço espera
- [ ] Consulte a documentação da API

### "A resposta não funciona como esperado"
**Soluções:**
- [ ] Teste a API utilizando uma ferramenta como o Postman
- [ ] Compare o formato real da resposta com o formato esperado
- [ ] Verifique se a documentação da API foi alterada
- [ ] Verifique se os dados que está a enviar estão corretos

---

## Utilização dos dados de resposta

Assim que receber dados da API, os cartões seguintes podem utilizá-los:

```
API Response:
{
  "unit_price": 45.00,
  "currency": "USD",
  "available": true
}

Next Card (Set Field):
- Set "Unit_Price" field to 45.00
- Set "Currency" field to USD
- Set "In_Stock" checkbox to true
```

---

## Notas de segurança

⚠️ **Importante:** Nunca coloque informações sensíveis na configuração do cartão que possam ser visíveis para outros utilizadores

- Não codifique palavras-passe diretamente
- Utilize as chaves de API de forma segura
- Não inclua dados pessoais nos registos
- Utilize endpoints HTTPS (não HTTP)

---

## Dicas e boas práticas

✅ **Faça:**
- Teste primeiro com uma pequena amostra de documentos
- Mantenha as chamadas de API simples e focadas
- Adicione tratamento de erros com cartões Condition
- Monitorize a utilização/os custos da API
- Documente os requisitos da API para a sua equipa

❌ **Não faça:**
- Chamar APIs para cada pedido individual se puder colocar os dados em cache
- Ignorar os códigos de erro das respostas
- Utilizar APIs de teste em produção
- Esquecer-se de adicionar cabeçalhos de autenticação
- Assumir que a API estará sempre disponível

---

## Cartões relacionados

- **ACTION_HTTPS_REQUEST** - Pedidos HTTPS semelhantes, mas mais simples
- **CONDITION_HTTPS_REQUEST_STATUS** - Verifica se a chamada de API foi bem-sucedida
- **ACTION_SEND_EMAIL** - Envia dados por e-mail em vez de API
- **CALL_API** (versão diferente) - Método alternativo de chamada de API

---

## Precisa de ajuda?

- Peça à sua equipa de TI/Integração a documentação da API
- Utilize a ferramenta Postman para testar primeiro os endpoints da API
- Consulte o portal de suporte do fornecedor do serviço
- Reveja a documentação da API para conhecer os formatos necessários
