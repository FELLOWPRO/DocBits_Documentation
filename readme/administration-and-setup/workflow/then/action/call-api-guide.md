# Chamar API externa

***

Adicione este cartão ao grupo **Então** do Workflow Builder — as ações que são executadas quando as condições Quando/E correspondem:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-pt.png" alt="Exemplo não guardado com cartões Quando, E e Então. Configure todos os campos antes da execução. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real."><figcaption><p>Exemplo não guardado com cartões Quando, E e Então. Configure todos os campos antes da execução. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

***

## 📌 Informações da versão

**Versão atual:** v2 (mais recente e recomendado) **Estado:** ✅ Ativo

**Histórico de versões:**

* v1 → Chamada de API básica (não mais recomendada)
* **v2 → CURRENT** (adicionado suporte multilíngue)

**O que mudou:** v2 adicionou suporte à internacionalização (i18n) com chaves de tradução. A funcionalidade permanece idêntica.

📖 [Histórico e alterações da versão](../../release.md) | [Banco de dados completo do cartão](../../cards-overview/export-cards-guide.md)

***

## Objetivo

Este cartão permite enviar dados para um site ou serviço externo e receber informações de volta. Pense nisso como enviar uma pergunta a um serviço externo e obter uma resposta que você pode usar em seu fluxo de trabalho.

**Exemplo do mundo real:** Sua empresa usa um sistema de preços em outro site. Este cartão pode solicitar automaticamente ao sistema de preços o preço atual de um item e trazer esse preço para o seu documento.

***

## Quando usar este cartão

Use este cartão quando precisar:

* Obtenha informações de um serviço externo (como preços, validação ou dados de pesquisa)
* Envie informações do documento para outro sistema para processamento
* Integrar com serviços de terceiros
* Busque dados automaticamente sem pesquisas manuais
* Conecte vários sistemas de negócios juntos

**Cenários comuns:**

* Procure informações de fornecedores em um banco de dados
* Obtenha preços em tempo real de um serviço de preços
* Validar dados em um sistema externo
* Obtenha informações de envio de um provedor de logística

***

## Como funciona

1. **Verificação de condição**: O fluxo de trabalho primeiro verifica se as condições nas seções "Quando" e "E" foram atendidas
2. **Preparar dados**: O cartão coleta os parâmetros que você configurou
3. **Enviar solicitação**: Envia seus dados para a API/serviço externo
4. **Receber resposta**: O serviço externo responde com dados
5. **Continue**: O fluxo de trabalho usa esses dados em cartões subsequentes

***

## Parâmetros explicados

### URL do terminal da API

**O que é:** O endereço do serviço externo com o qual você deseja se comunicar

**Exemplo:** `https://api.supplier-system.com/product/pricing`

**Como encontrá-lo:** Pergunte à sua equipe de TI ou ao provedor de serviços o endpoint da API

***

### Método HTTP

**O que é:** O tipo de solicitação a ser enviada

**Opções:**

* **GET**: Solicitar informações (como fazer uma pergunta)
* **POST**: Enviar novos dados
* **PUT**: Atualizar dados existentes
* **DELETE**: Remover dados

**Mais comum:** GET (para buscar informações)

***

### Cabeçalhos

**O que é:** Instruções adicionais para o serviço que você está ligando

**Exemplo:**

```
Authorization: Bearer your-api-key
Content-Type: application/json
```

**Por que é necessário:** Os serviços geralmente exigem autenticação ou instruções de formato específico

***

### Parâmetros (parâmetros de consulta)

**O que é:** Informações extras passadas na URL

**Exemplo:**

```
?supplier_id=12345&currency=USD
```

**Exemplo real:** Se você estiver solicitando preços, os parâmetros podem incluir o ID do fornecedor e a moeda

***

### Solicitar dados (corpo)

**O que é:** As informações que você está enviando para o serviço

**Exemplo:**

```json
{
  "product_id": "ABC123",
  "quantity": 100,
  "currency": "EUR"
}
```

**Quando usado:** Ao usar métodos POST ou PUT

***

## Exemplo passo a passo

### Cenário: Obtenha preços de fornecedores em tempo real

**Configuração:**

1. **Tipo de cartão:** Chamar API
2. **Ponto final da API:** `https://api.suppliers.com/v1/prices`
3. **Método:** POSTAR
4. **Cabeçalhos:** `Authorization: Bearer YOUR-API-KEY`
5.  **Solicitar dados:**

    ```json
    {
      "product_id": "ABC123",
      "quantity": 100
    }
    ```

**O que acontece:**

1. O documento chega com ID do produto: ABC123, Quantidade: 100
2. Cartão envia solicitação para API do fornecedor
3. A API do fornecedor responde com: `{"unit_price": 25.50, "total_price": 2550}`
4. O fluxo de trabalho continua com essas informações de preço
5. O próximo cartão pode usar esses dados para validar o preço da fatura

***

## Etapas de configuração

### 1. Obtenha informações da API

Entre em contato com o provedor de serviços externo e solicite:

* [] URL do terminal da API
* [] Método de autenticação (chave API, nome de usuário/senha, OAuth)
* [ ] Parâmetros obrigatórios
* [] Formato de resposta esperado
* [] Limites de taxas ou cotas

### 2. Configure o cartão

1. Insira o URL do terminal da API
2. Selecione o método HTTP (geralmente GET ou POST)
3. Adicione cabeçalhos de autenticação, se necessário
4. Adicione quaisquer parâmetros necessários
5. Formate os dados da solicitação como JSON, se necessário

### 3. Teste o cartão

1. Use um documento de teste
2. Execute o fluxo de trabalho
3. Verifique se a resposta foi recebida corretamente
4. Verifique se o formato dos dados corresponde às expectativas

***

## Cenários de resposta comuns

### Resposta bem-sucedida (código de status 200)

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

✅ Os dados estão disponíveis para os próximos cartões a serem usados

### Resposta de erro (código de status 404)

```json
{
  "error": "Product not found"
}
```

⚠️ A API não encontrou o que você procura

### Tempo limite

O serviço externo não respondeu dentro do prazo ⚠️ Verifique se o serviço está disponível ou se a URL do endpoint está correta

***

## Exemplos de fluxos de trabalho

### Exemplo 1: Validação Automática de Preço

**Cenário:** Validar preços de fatura em relação aos preços atuais do fornecedor

**Fluxo:**

1. O documento chega com item de fatura (Produto: A123, Preço: €50)
2. **Call API Card** → Pergunta ao fornecedor API: "Qual é o preço atual do A123?"
3. Fornecedor responde: "€48"
4. **Cartão de condição** → Verifica se o preço da fatura (€50) está dentro de 5% do preço atual (€48)
5. **Cartão de Aprovação** → Aprova se estiver dentro da tolerância

### Exemplo 2: pesquisa automática de fornecedores

**Cenário:** Obtenha dados mestre do fornecedor do banco de dados central

**Fluxo:**

1. A fatura chega com o Código do Fornecedor: SUPP-789
2. **Call API Card** → Solicita ao sistema: "Dê-me detalhes do fornecedor SUPP-789"
3. O sistema responde com: Nome, Contato, Termos, etc.
4. **Definir cartões de campo** → Preencher os campos do documento com estes dados
5. **Exportar cartão** → Exportar com informações completas

### Exemplo 3: Custos de envio em tempo real

**Cenário:** Obtenha custo de envio automático com base no destino

**Fluxo:**

1. O documento tem endereço de entrega
2. **Call API Card** → Pergunte ao fornecedor de remessa: "Qual é o custo para \[endereço]?"
3. O fornecedor responde com o custo de envio
4. **Calcular cartão** → Adicionar frete ao valor total da fatura
5. **Exportar Cartão** → Enviar com total atualizado

***

## Solução de problemas

### Erro "Tempo limite de conexão"

**Causa:** O serviço API não está respondendo

**Soluções:**

* [ ] Verifique se o serviço está disponível (acesse o site)
* [] Verifique se o URL do endpoint está correto (sem erros de digitação)
* [] Verifique a conexão com a internet
* [] Entre em contato com o provedor de serviços
* [] Verifique se o serviço tem limites de taxa (você está enviando muitas solicitações)

### Erro "Não autorizado" ou "403 Proibido"

**Causa:** Falha na autenticação

**Soluções:**

* [] Verifique se sua chave de API está correta
* [] Verifique se sua chave API expirou
* [] Certifique-se de que o cabeçalho de autenticação esteja formatado corretamente
* [] Verifique se você tem permissões para este endpoint

### "Solicitação incorreta" ou "Erro 400"

**Causa:** O formato dos dados da solicitação está incorreto

**Soluções:**

* [] Verifique a sintaxe JSON (faltando vírgulas, aspas, etc.)
* [] Verifique se todos os campos obrigatórios estão incluídos
* [] Verifique se os nomes dos parâmetros correspondem ao que o serviço espera
* [ ] Consulte a documentação da API

### "A resposta não funciona conforme o esperado"

**Soluções:**

* [] Teste a API usando uma ferramenta como Postman
* [] Compare o formato de resposta real com o formato esperado
* [ ] Verifique se a documentação da API mudou
* [] Verifique se os dados que você está enviando estão corretos

***

## Uso de dados de resposta

Depois de recuperar os dados da API, os próximos cartões poderão usá-los:

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

***

## Notas de segurança

⚠️ **Importante:** Nunca coloque informações confidenciais na configuração do cartão que possam ser visíveis para outros usuários

* Não codifique senhas
* Use chaves de API com segurança
* Não inclua dados pessoais nos registros
* Use pontos de extremidade HTTPS (não HTTP)

***

## Dicas e práticas recomendadas

✅ **Fazer:**

* Teste primeiro com uma pequena amostra de documentos
* Mantenha as chamadas de API simples e focadas
* Adicione tratamento de erros com cartões de condição
* Monitore o uso/custos da API
* Documente os requisitos da API para sua equipe

❌ **Não:**

* Chame APIs para cada solicitação se você puder armazenar dados em cache
* Ignorar códigos de erro de resposta
* Use APIs de teste em produção
* Esqueci de adicionar cabeçalhos de autenticação
* Suponha que a API estará sempre disponível

***

## Cartões Relacionados

* **ACTION\_HTTPS\_REQUEST** - Solicitações HTTPS semelhantes, mas mais simples
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - Verifique se a chamada da API foi bem-sucedida
* **ACTION\_SEND\_EMAIL** - Enviar dados por e-mail em vez de API
* **CALL\_API** (versão diferente) - Método alternativo de chamada de API

***

## Precisa de ajuda?

* Peça à sua equipe de TI/Integração a documentação da API
* Use a ferramenta Postman para testar os endpoints da API primeiro
* Verifique o portal de suporte do provedor de serviços
* Revise a documentação da API para obter os formatos necessários
