# Enviar solicitação HTTPS

***

Adicione este cartão ao grupo **Então** do Workflow Builder — as ações que são executadas quando as condições Quando/E correspondem:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-pt.png" alt="Exemplo não guardado com cartões Quando, E e Então. Configure todos os campos antes da execução. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real."><figcaption><p>Exemplo não guardado com cartões Quando, E e Então. Configure todos os campos antes da execução. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

***

## 📌 Informações da versão

**Versão atual:** v2 (mais recente e recomendado) **Estado:** ✅ Ativo

**Histórico de versões:**

* v1 → Solicitação HTTP simples (não mais recomendado)
* **v2 → CURRENT** (adicionado suporte multilíngue)

**O que mudou:** v2 adicionou suporte à internacionalização (i18n). A funcionalidade principal de webhook/solicitação permanece inalterada.

📖 [Histórico e alterações da versão](../../release.md) | [Banco de dados completo do cartão](../../cards-overview/export-cards-guide.md)

***

## Objetivo

Este cartão envia uma mensagem segura para um site ou serviço e pode receber uma resposta. É mais simples que o cartão "Call API" e é útil para integrações rápidas.

**Exemplo do mundo real:** Envie os dados da fatura para o seu sistema contábil ou pergunte a um sistema externo se um funcionário está aprovado para processar esta compra.

***

## Quando usar este cartão

Use este cartão quando precisar:

* Envie notificações de webhook para serviços externos
* Acionar ações em outros sistemas
* Consulte um serviço web simples
* Envie atualizações de status para outros aplicativos
* Execute integrações simples sem requisitos complexos de API

***

## Como funciona

1. **Verificação de gatilho**: O sistema verifica se as condições "Quando" e "E" foram atendidas
2. **Solicitação de construção**: O sistema prepara a solicitação HTTPS com seus parâmetros
3. **Enviar com segurança**: Os dados são enviados usando uma conexão HTTPS segura
4. **Receber resposta**: Serviço externo responde
5. **Continuar**: O fluxo de trabalho prossegue com os dados de resposta

***

## Parâmetros

### URL

O endereço do site para enviar a solicitação

**Exemplo:** `https://webhook.company.com/process`

### Cabeçalhos

Instruções especiais para o destinatário

**Exemplo:**

```
Content-Type: application/json
Authorization: Bearer token123
```

### Método

* **GET**: Solicitar informações
* **POST**: Enviar dados
* **PUT**: Atualizar dados

### Parâmetros (string de consulta)

Dados adicionados ao URL

**Exemplo:** `?action=approve&user_id=123`

### Solicitar dados

As informações reais que estão sendo enviadas (em formato JSON)

**Exemplo:**

```json
{
  "invoice_number": "INV-2025-001",
  "amount": 5000,
  "currency": "EUR"
}
```

***

## Exemplo passo a passo

### Cenário: Enviar fatura para sistema contábil

**Configuração do cartão:**

* **URL:** `https://accounting.company.com/invoices/create`
* **Método:** POSTAR
* **Cabeçalhos:** `Authorization: Bearer YOUR-TOKEN`
* **Solicitar dados:**

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

***

## Casos de uso comuns

### 1. Notificações de webhook

Envie notificações em tempo real para outros sistemas sempre que algo acontecer no DocFlow

**Exemplo:**

* Documento aprovado → Enviar notificação para sistema de atendimento
* Fornecedor alterado → Notificar a equipe de compras via webhook do Slack/Teams

### 2. Integração de Sistema Externo

Conecte o DocFlow a outros sistemas empresariais para troca automática de dados

**Exemplo:**

* Depois que o documento for processado → Sincronizar com o sistema ERP
* Novo fornecedor adicionado → Criar registro de fornecedor no sistema de dados mestre

### 3. Fluxos de trabalho de aprovação

Enviar documento para sistema de aprovação externo e receber decisão

**Exemplo:**

* Fatura de alto valor → Enviar para Finanças para aprovação
* Devolver documento ao sistema externo com decisão

***

## Guia de configuração

### Etapa 1: obter informações do endpoint

Solicite ao sistema receptor:

* [ ] URL HTTPS
* [] Cabeçalhos obrigatórios
* [] Método de autenticação
* [] Formato de solicitação esperado
* [] Formato de resposta esperado

### Etapa 2: configurar o cartão

1. Insira o URL HTTPS
2. Definir método HTTP (geralmente POST)
3. Adicione autenticação, se necessário
4. Formatar dados de solicitação como JSON
5. Adicione quaisquer cabeçalhos personalizados

### Etapa 3: teste

Envie uma solicitação de teste e verifique a resposta

***

## Tratamento de respostas

Sua solicitação HTTPS receberá uma resposta. Respostas comuns:

### Sucesso (200, 201)

```json
{
  "success": true,
  "id": "REC-12345",
  "status": "processed"
}
```

### Solicitação incorreta (400)

```json
{
  "error": "Missing required field: invoice_number"
}
```

### Não autorizado (401)

```json
{
  "error": "Invalid authentication token"
}
```

### Erro do servidor (500)

O sistema receptor tem um problema interno

***

## Solução de problemas

### "Erro de certificado"

**Causa:** Problema no certificado de segurança HTTPS

**Solução:**

* Verifique se o URL está correto
* Verifique se o certificado do site é válido
* Verifique se você está usando HTTPS (não HTTP)

### "Conexão recusada"

**Causa:** Não é possível conectar ao servidor

**Solução:**

* Verifique se o URL/endereço IP está correto
* Verifique se o serviço está em execução
* Verifique as regras do firewall
* Verifique a conectividade com a Internet

### "Sem resposta/Tempo limite"

**Causa:** Servidor não responde dentro do prazo

**Solução:**

* Verifique se o serviço está disponível
* Verifique o URL do terminal
* Verifique se há limites de taxas
* Entre em contato com o administrador do sistema

### "JSON inválido"

**Causa:** Os dados da solicitação estão mal formados

**Solução:**

* Verifique se há vírgulas faltando em JSON
* Verifique se todas as cotações estão corretas
* Valide o formato JSON (use o validador JSON online)
* Verifique se há caracteres especiais

***

## Exemplos

### Exemplo 1: Enviar para serviço Webhook

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

### Exemplo 2: Atualizar sistema externo

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

### Exemplo 3: Consultar serviço externo

```
URL: https://lookup.company.com/validate?id=SUP-789
Method: GET
Headers: Authorization: Bearer token
```

***

## Diferença do cartão "Call API"

| Recurso        | Solicitação HTTPS      | Chamar API          |
| -------------- | ------------------ | ----------------- |
| Simplicidade     | Simples             | Mais complexo      |
| Parâmetros     | Básico              | Avançado          |
| Tratamento de erros | Básico              | Detalhado          |
| Usar para        | Integrações rápidas | APIs complexas      |
| Melhor para       | Webhooks           | APIs profissionais |

***

## Considerações de segurança

✅ **Sempre use HTTPS** (conexão segura)

⚠️ **Nunca:**

* Coloque senhas na URL
* Expor chaves de API em registros
* Incluir dados pessoais nos parâmetros
* Use HTTP para dados confidenciais

***

## Melhores Práticas

✅ **Fazer:**

* Teste primeiro com pequenas quantidades de dados
* Incluir tratamento de erros
* Registrar solicitações importantes
* Documente a integração
* Monitore falhas

❌ **Não:**

* Chame o mesmo endpoint repetidamente se não for necessário
* Ignorar erros de resposta
* Incluir dados confidenciais em texto simples
* Exceder os limites de taxa de serviço

***

## Cartões Relacionados

* **CALL\_API** - Integração de API mais avançada
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - Verifique se a solicitação foi bem-sucedida
* **ACTION\_SEND\_EMAIL** - Enviar por e-mail
* **ACTION\_RUN\_DOCOPERATOR\_SCRIPT** - Scripts automatizados

<!-- workflow-card-complete-example-20261021 action_https_request -->

### Exemplo de ação HTTPS

**Configuração:** Selecione o método `POST`, substitua `DEMO_WEBHOOK_URL` pelo seu endpoint de teste autorizado, adicione o cabeçalho `Content-Type: application/json` e o corpo `{"document_number":"DEMO-001"}`. Configure a autenticação apenas conforme exigido por esse endpoint; nunca copie um segredo real na documentação.

**Resultado esperado e contra-exemplo:** A ação envia a solicitação configurada quando sua rota de fluxo de trabalho é executada. Inspecione a resposta HTTP e o serviço de teste de recebimento. Um tempo limite não é prova de que o serviço não fez nada, e essa ação Then é separada do cartão And que verifica um status HTTP. Esta solicitação ilustrativa não foi enviada.

Esta é uma configuração de teste ilustrativa e resultado esperado; não foi executado. Use dados e destinatários configurados na sua organização de teste.
