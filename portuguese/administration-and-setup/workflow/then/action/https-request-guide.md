# Send HTTPS Request

Estes cartões ficam no grupo **Then** do Construtor de fluxos de trabalho — as ações executadas assim que as condições When/And são atendidas:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Os cartões são adicionados ao grupo <strong>Then</strong> através de <strong>Add Card</strong>.</p></figcaption></figure>

## Objetivo
Este cartão envia uma mensagem segura para um site ou serviço e pode receber uma resposta de volta. É mais simples do que o cartão "Call API" e é útil para integrações rápidas.

**Exemplo do mundo real:** Enviar dados da fatura para o seu sistema de contabilidade, ou perguntar a um sistema externo se um colaborador está aprovado para processar esta compra.

---

## Quando utilizar este cartão

Utilize este cartão quando precisar de:
- Enviar notificações de webhook para serviços externos
- Acionar ações noutros sistemas
- Consultar um serviço web simples
- Enviar atualizações de estado para outras aplicações
- Realizar integrações simples sem requisitos complexos de API

---

## Como funciona

1. **Trigger Check**: O sistema verifica se as condições "Where" e "And" são cumpridas
2. **Build Request**: O sistema prepara o pedido HTTPS com os seus parâmetros
3. **Send Securely**: Os dados são enviados através de uma ligação HTTPS segura
4. **Receive Response**: O serviço externo responde
5. **Continue**: O fluxo de trabalho prossegue com os dados da resposta

---

## Parâmetros

### URL
O endereço do site para onde enviar o pedido

**Exemplo:** `https://webhook.company.com/process`

### Headers
Instruções especiais para o destinatário

**Exemplo:**
```
Content-Type: application/json
Authorization: Bearer token123
```

### Method
- **GET**: Pedir informações
- **POST**: Enviar dados
- **PUT**: Atualizar dados

### Parameters (Query String)
Dados adicionados ao URL

**Exemplo:** `?action=approve&user_id=123`

### Request Data
As informações efetivamente enviadas (em formato JSON)

**Exemplo:**
```json
{
  "invoice_number": "INV-2025-001",
  "amount": 5000,
  "currency": "EUR"
}
```

---

## Exemplo passo a passo

### Cenário: Enviar fatura para o sistema de contabilidade

**Configuração do cartão:**
- **URL:** `https://accounting.company.com/invoices/create`
- **Method:** POST
- **Headers:** `Authorization: Bearer YOUR-TOKEN`
- **Request Data:**
```json
{
  "supplier_id": "SUPP001",
  "invoice_number": "12345",
  "amount": 1500.00,
  "currency": "EUR",
  "date": "2025-10-23"
}
```

**Resposta esperada:**
```json
{
  "status": "success",
  "accounting_id": "ACC-98765",
  "message": "Invoice recorded in accounting system"
}
```

---

## Casos de utilização comuns

### 1. Notificações de webhook
Enviar notificações em tempo real para outros sistemas sempre que algo acontece no DocFlow

**Exemplo:**
- Documento aprovado → Enviar notificação para o sistema de cumprimento
- Fornecedor alterado → Notificar a equipa de compras através de webhook do Slack/Teams

### 2. Integração com sistema externo
Ligar o DocFlow a outros sistemas empresariais para troca automática de dados

**Exemplo:**
- Após o documento ser processado → Sincronizar com o sistema ERP
- Novo fornecedor adicionado → Criar o registo de fornecedor no sistema de dados mestre

### 3. Fluxos de trabalho de aprovação
Enviar o documento para um sistema de aprovação externo e receber a decisão

**Exemplo:**
- Fatura de valor elevado → Enviar para o departamento financeiro para aprovação
- Devolver o documento ao sistema externo com a decisão

---

## Guia de configuração

### Passo 1: Obter informações do endpoint
Peça ao sistema recetor:
- [ ] URL HTTPS
- [ ] Cabeçalhos necessários
- [ ] Método de autenticação
- [ ] Formato de pedido esperado
- [ ] Formato de resposta esperado

### Passo 2: Configurar o cartão
1. Introduza o URL HTTPS
2. Defina o método HTTP (normalmente POST)
3. Adicione autenticação, se necessário
4. Formate os dados do pedido como JSON
5. Adicione quaisquer cabeçalhos personalizados

### Passo 3: Testar
Envie um pedido de teste e verifique a resposta

---

## Tratamento de respostas

O seu pedido HTTPS receberá uma resposta. Respostas comuns:

### Sucesso (200, 201)
```json
{
  "success": true,
  "id": "REC-12345",
  "status": "processed"
}
```

### Bad Request (400)
```json
{
  "error": "Missing required field: invoice_number"
}
```

### Unauthorized (401)
```json
{
  "error": "Invalid authentication token"
}
```

### Server Error (500)
O sistema recetor tem um problema interno

---

## Resolução de problemas

### "Certificate Error"
**Causa:** Problema com o certificado de segurança HTTPS

**Solução:**
- Verifique se o URL está correto
- Verifique se o certificado do site é válido
- Garanta que está a utilizar HTTPS (não HTTP)

### "Connection Refused"
**Causa:** Não é possível ligar ao servidor

**Solução:**
- Verifique se o URL/endereço IP está correto
- Verifique se o serviço está em execução
- Verifique as regras da firewall
- Verifique a ligação à Internet

### "No Response / Timeout"
**Causa:** O servidor não responde dentro do tempo limite

**Solução:**
- Verifique se o serviço está disponível
- Verifique o URL do endpoint
- Verifique se existem limites de taxa
- Contacte o administrador do sistema

### "Invalid JSON"
**Causa:** Os dados do pedido estão malformados

**Solução:**
- Verifique se faltam vírgulas no JSON
- Verifique se todas as aspas estão corretas
- Valide o formato JSON (utilize um validador JSON online)
- Verifique a existência de caracteres especiais

---

## Exemplos

### Exemplo 1: Enviar para um serviço de webhook
```
URL: https://webhook.site/your-unique-id
Method: POST
Data:
{
  "document_id": "DOC-123",
  "status": "approved",
  "amount": 5000
}
```

### Exemplo 2: Atualizar um sistema externo
```
URL: https://api.company.com/update
Method: PUT
Data:
{
  "record_id": "REC-456",
  "status": "completed",
  "timestamp": "2025-10-23T10:30:00"
}
```

### Exemplo 3: Consultar um serviço externo
```
URL: https://lookup.company.com/validate?id=SUP-789
Method: GET
Headers: Authorization: Bearer token
```

---

## Diferença em relação ao cartão "Call API"

| Funcionalidade | HTTPS Request | Call API |
|---------|---------------|----------|
| Simplicidade | Simples | Mais complexo |
| Parâmetros | Básicos | Avançados |
| Tratamento de erros | Básico | Detalhado |
| Utilizar para | Integrações rápidas | APIs complexas |
| Ideal para | Webhooks | APIs profissionais |

---

## Considerações de segurança

✅ **Utilize sempre HTTPS** (ligação segura)

⚠️ **Nunca:**
- Coloque palavras-passe no URL
- Exponha chaves de API nos registos
- Inclua dados pessoais nos parâmetros
- Utilize HTTP para dados sensíveis

---

## Boas práticas

✅ **Faça:**
- Teste primeiro com pequenas quantidades de dados
- Inclua tratamento de erros
- Registe os pedidos importantes
- Documente a integração
- Monitorize a existência de falhas

❌ **Não faça:**
- Chamar o mesmo endpoint repetidamente se não for necessário
- Ignorar os erros de resposta
- Incluir dados sensíveis em texto simples
- Exceder os limites de taxa do serviço

---

## Cartões relacionados

- **CALL_API** - Integração de API mais avançada
- **CONDITION_HTTPS_REQUEST_STATUS** - Verifica se o pedido foi bem-sucedido
- **ACTION_SEND_EMAIL** - Enviar por e-mail em alternativa
- **ACTION_RUN_DOCOPERATOR_SCRIPT** - Scripts automatizados
