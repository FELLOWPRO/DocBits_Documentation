# Ferramentas do SDK de Cards

As ferramentas do Card SDK permitem criar, validar, testar e gerenciar cards de parceiros personalizados através do MCP. Os cards de parceiros estendem o DocFlow com lógica de negócios personalizada escrita em Python.

## Ciclo de Vida do Card

```
Criar → Validar → Testar → Aprovar → Usar em Workflows
```

1. **Crie** um card com `sdk_create_card` ou `sdk_import_github`
2. **Valide** com `sdk_validate_card` (validação em 5 etapas)
3. **Teste** com `sdk_test_card` (execução em sandbox)
4. **Aprove** com `sdk_approve_card` (requer admin)
5. O card agora está disponível em `list_cards` e pode ser usado em workflows

## Ferramentas de Desenvolvimento

### sdk\_create\_card

Cria um novo card de parceiro a partir de código-fonte e manifestos. Executa a validação completa em 5 etapas e armazena o card no banco de dados. O card começa em estado pendente e requer aprovação de administrador para ser ativado.

**Parâmetros:**

| Parâmetro       | Tipo   | Obrigatório | Descrição                                                         |
| --------------- | ------ | ----------- | ----------------------------------------------------------------- |
| `app_manifest`  | object | Sim         | Manifesto do app com id, nome, versão, info do parceiro           |
| `card_manifest` | object | Sim         | Manifesto do card com id, título, entry\_point, class\_name, args |
| `card_type`     | string | Sim         | `action` ou `condition`                                           |
| `source_code`   | string | Sim         | Código-fonte Python (deve estender `PartnerCard`)                 |
| `test_code`     | string | Sim         | Código de teste Pytest para o card                                |
| `locales`       | object | Não         | Traduções de idioma, ex.: `{"en": {...}, "de": {...}}`            |

**Exemplo de Manifesto do App:**

```json
{
  "id": "com.acme.invoice-tools",
  "name": "Invoice Tools",
  "version": "1.0.0",
  "partner": {
    "id": "acme",
    "name": "Acme Corp"
  }
}
```

**Exemplo de Manifesto do Card:**

```json
{
  "id": "amount-threshold",
  "title": {"en": "Amount Threshold Check"},
  "entry_point": "src/amount_threshold.py",
  "class_name": "AmountThreshold",
  "args": [
    {
      "id": "threshold",
      "title": {"en": "Threshold Amount"},
      "type": "number",
      "required": true
    }
  ]
}
```

**Exemplo de Código-Fonte:**

```python
from api.sdk.base import PartnerCard
from api.sdk.result import CardResult, CardStatus

class AmountThreshold(PartnerCard):
    def execute(self, context):
        threshold = float(self.variables.get("threshold", 0))
        total = context.document_fields.get("total_amount", 0)
        if float(total) > threshold:
            return CardResult(
                status=CardStatus.SUCCESS,
                message=f"Amount {total} exceeds threshold {threshold}"
            )
        return CardResult(
            status=CardStatus.FAILURE,
            message=f"Amount {total} below threshold {threshold}"
        )
```

**Exemplo de Resposta:**

```json
{
  "success": true,
  "cards": ["amount-threshold"],
  "validation_report": {
    "status": "validated",
    "stages": {
      "structure": {"passed": true},
      "ast_analysis": {"passed": true},
      "dependencies": {"passed": true},
      "tests": {"passed": true},
      "behavioral": {"passed": true}
    }
  }
}
```

### sdk\_validate\_card

Executa a validação em 5 etapas em um card de parceiro sem salvar. Dois modos:

* **Modo A** — Validar um card existente por ID
* **Modo B** — Validar novo código-fonte inline

**Parâmetros:**

| Parâmetro       | Tipo   | Obrigatório | Descrição                        |
| --------------- | ------ | ----------- | -------------------------------- |
| `card_id`       | string | Não         | UUID do card existente (Modo A)  |
| `app_manifest`  | object | Não         | Manifesto do app (Modo B)        |
| `card_manifest` | object | Não         | Manifesto do card (Modo B)       |
| `card_type`     | string | Não         | `action` ou `condition` (Modo B) |
| `source_code`   | string | Não         | Código-fonte Python (Modo B)     |
| `test_code`     | string | Não         | Código de teste (Modo B)         |

{% hint style="info" %}
Forneça apenas `card_id` isolado (Modo A) ou `app_manifest` + `card_manifest` + `source_code` juntos (Modo B).
{% endhint %}

**Etapas de Validação:**

1. **Estrutura** — Verifica layout de arquivos, esquema do manifesto, arquivos obrigatórios
2. **Análise AST** — Verifica sintaxe Python, hierarquia de classes, assinaturas de métodos
3. **Dependências** — Valida imports contra módulos permitidos
4. **Testes** — Executa a suíte de testes do card
5. **Comportamental** — Executa o card em sandbox para verificar comportamento em tempo de execução

### sdk\_test\_card

Executa um card de parceiro em um ambiente isolado (sandbox) com um contexto simulado. Usa o mesmo modelo de segurança da produção (builtins restritos, lista de imports permitidos, timeout de 10 segundos).

**Parâmetros:**

| Parâmetro      | Tipo   | Obrigatório | Descrição                                   |
| -------------- | ------ | ----------- | ------------------------------------------- |
| `card_id`      | string | Não         | UUID do card existente (Modo A)             |
| `source_code`  | string | Não         | Código-fonte para teste inline (Modo B)     |
| `class_name`   | string | Não         | Nome da classe para teste inline (Modo B)   |
| `variables`    | object | Não         | Variáveis para passar ao construtor do card |
| `mock_context` | object | Não         | Contexto de execução simulado               |

**Campos do Contexto Simulado:**

```json
{
  "document_id": "doc-uuid",
  "document_type": "INVOICE",
  "document_fields": {
    "total_amount": "1500.00",
    "currency": "EUR",
    "vendor_name": "Acme Corp"
  },
  "metadata": {
    "custom_key": "custom_value"
  }
}
```

**Exemplo de Resposta:**

```json
{
  "success": true,
  "status": "CardStatus.SUCCESS",
  "message": "Amount 1500.00 exceeds threshold 1000",
  "data": {},
  "logs": ["Checking threshold...", "Amount exceeds threshold"]
}
```

### sdk\_import\_github

Importa um app de parceiro de um repositório GitHub. Clona o repositório, lê o `app.json` e importa todos os cards encontrados no diretório `.docflowcompose`.

**Parâmetros:**

| Parâmetro    | Tipo   | Obrigatório | Descrição                                                |
| ------------ | ------ | ----------- | -------------------------------------------------------- |
| `github_url` | string | Sim         | URL HTTPS do GitHub (ex.: `https://github.com/org/repo`) |
| `branch`     | string | Não         | Branch a ser clonado (padrão: `main`)                    |
| `token`      | string | Não         | Token do GitHub para repositórios privados               |

**Estrutura Esperada do Repositório:**

```
repo/
  app.json
  .docflowcompose/
    flow/
      actions/
        my-action.json
      conditions/
        my-condition.json
  src/
    my_action.py
    my_condition.py
  tests/
    test_card.py
```

**Exemplo de Resposta:**

```json
{
  "success": true,
  "message": "Imported 2 cards from GitHub. Status: validated",
  "app_id": "com.acme.invoice-tools",
  "cards_created": ["my-action", "my-condition"],
  "validation_report": {"status": "validated"}
}
```

## Ferramentas de Gerenciamento

### sdk\_list\_submissions

Lista todas as submissões de cards de parceiros da organização atual.

**Parâmetros:** Nenhum

**Exemplo de Resposta:**

```json
[
  {
    "card_id": "card-uuid",
    "card_name": "Amount Threshold Check",
    "partner_app_id": "com.acme.invoice-tools",
    "partner_status": "validated",
    "version": "1.0.0",
    "card_type": "condition",
    "enabled": false,
    "submitted_at": "2025-03-20T10:00:00"
  }
]
```

### sdk\_get\_submission\_status

Obtém o status de validação e o relatório de uma submissão específica de card de parceiro.

**Parâmetros:**

| Parâmetro | Tipo   | Obrigatório | Descrição                |
| --------- | ------ | ----------- | ------------------------ |
| `card_id` | string | Sim         | UUID do card de parceiro |

**Exemplo de Resposta:**

```json
{
  "card_id": "card-uuid",
  "status": "validated",
  "validation_report": {
    "status": "validated",
    "stages": {
      "structure": {"passed": true},
      "ast_analysis": {"passed": true},
      "dependencies": {"passed": true},
      "tests": {"passed": true},
      "behavioral": {"passed": true}
    }
  }
}
```

### sdk\_approve\_card

Aprova um card de parceiro validado e o ativa para uso em workflows. O card é registrado no registro de tempo de execução e fica disponível em `list_cards`.

**Parâmetros:**

| Parâmetro | Tipo   | Obrigatório | Descrição                |
| --------- | ------ | ----------- | ------------------------ |
| `card_id` | string | Sim         | UUID do card de parceiro |

{% hint style="warning" %}
Requer permissões de administrador da organização. O card deve estar no estado `validated` ou `rejected`.
{% endhint %}

### sdk\_reject\_card

Rejeita uma submissão de card de parceiro e o desativa.

**Parâmetros:**

| Parâmetro | Tipo   | Obrigatório | Descrição                |
| --------- | ------ | ----------- | ------------------------ |
| `card_id` | string | Sim         | UUID do card de parceiro |
| `reason`  | string | Não         | Motivo da rejeição       |

{% hint style="warning" %}
Requer permissões de administrador da organização.
{% endhint %}

### sdk\_delete\_submission

Desativa ou exclui uma submissão de card de parceiro. Cards rejeitados ou desabilitados são excluídos fisicamente do banco de dados. Cards ativos são desativados primeiro.

**Parâmetros:**

| Parâmetro | Tipo   | Obrigatório | Descrição                |
| --------- | ------ | ----------- | ------------------------ |
| `card_id` | string | Sim         | UUID do card de parceiro |

{% hint style="warning" %}
Requer permissões de administrador da organização.
{% endhint %}

### sdk\_list\_cards\_picker

Lista todos os cards habilitados e não obsoletos com flags de função. Útil para determinar quais cards podem ser usados em quais tipos de nó ao construir workflows.

**Parâmetros:** Nenhum

**Exemplo de Resposta:**

```json
[
  {
    "card_id": "card-uuid",
    "card_name": "Document Type Is",
    "category": "Document",
    "card_type": "document_type_is",
    "is_when": true,
    "is_and": false,
    "is_then": false,
    "is_partner_card": false
  }
]
```
