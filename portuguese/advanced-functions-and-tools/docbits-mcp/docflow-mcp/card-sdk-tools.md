# Ferramentas do Card SDK

As ferramentas do Card SDK permitem criar, validar, testar e gerenciar cartões de parceiros personalizados por meio do MCP. Os cartões de parceiros estendem o DocFlow com lógica de negócio personalizada escrita em Python.

## Ciclo de vida do cartão

Um cartão de parceiro passa pelos seguintes estados de submissão (`partner_status`):

| Estado | Significado | Visibilidade no workflow |
|-------|---------|---------------------|
| `validating` | Submissão aceita; o pipeline de validação está em execução. | Somente a organização que submeteu |
| `validated` | Todas as etapas de validação foram aprovadas. Aguardando a aprovação de um administrador. | Somente a organização que submeteu |
| `rejected` | A validação falhou ou um administrador rejeitou o cartão. O código-fonte é mantido para inspeção. | Somente a organização que submeteu |
| `approved` | Um administrador aprovou o cartão; `enabled = true`. | **Todas as organizações** |
| `disabled` | Cartão aprovado anteriormente que um administrador desativou. | Somente a organização que submeteu |
| `deleted` | Excluído de forma lógica (soft delete); não é retornado nas listagens de submissões. | Oculto |

{% hint style="warning" %}
**Visibilidade entre organizações:** um cartão de parceiro só fica disponível para os nós de workflow em `list_cards` depois de ser **aprovado**. Os cartões de parceiros aprovados ficam visíveis para todas as organizações da plataforma — a aprovação é uma ativação global, não por organização. Os cartões não aprovados (validating, validated, rejected, disabled) ficam visíveis somente para a organização que os submeteu.
{% endhint %}

Fluxo típico:

1. **Crie** um cartão com `sdk_create_card` ou `sdk_import_github` — executa o pipeline de validação e armazena o cartão com `partner_status = validated` (ou `rejected` em caso de falha).
2. **Valide** com `sdk_validate_card` para verificar novamente um cartão existente ou testar um novo código-fonte sem persistir.
3. **Teste** com `sdk_test_card` para executar o cartão no sandbox com um contexto simulado.
4. **Aprove** com `sdk_approve_card` (somente administrador da organização) — executa novamente a validação AST e comportamental e depois define `partner_status = approved` e `enabled = true`.
5. Depois de aprovado, o cartão aparece em `list_cards` para todas as organizações e pode ser referenciado em nós de workflow.

## Ferramentas de desenvolvimento

### sdk\_create\_card

Cria um novo cartão de parceiro a partir de código-fonte e manifestos. Executa o pipeline de validação completo (veja [Etapas de validação](#sdk_validate_card) abaixo) e armazena o cartão no banco de dados. O cartão fica no estado `validated` e precisa da aprovação de um administrador antes de poder ser usado em workflows.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `app_manifest` | object | Sim | Manifesto do aplicativo com id, nome, versão e dados do parceiro |
| `card_manifest` | object | Sim | Manifesto do cartão com id, título, entry\_point, class\_name e args |
| `card_type` | string | Sim | `action` ou `condition` |
| `source_code` | string | Sim | Código-fonte Python (deve estender `PartnerCard`) |
| `test_code` | string | Sim | Código de teste pytest do cartão |
| `locales` | object | Não | Traduções por idioma, por exemplo `{"en": {...}, "de": {...}}` |

**Exemplo de manifesto do aplicativo:**

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

**Exemplo de manifesto do cartão:**

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

**Exemplo de código-fonte:**

```python
from api.sdk.base import PartnerCard
from api.sdk.context import ExecutionContext
from api.sdk.result import CardResult, CardStatus

class AmountThreshold(PartnerCard):
    def execute(self, context: ExecutionContext) -> CardResult:
        threshold = float(self.variables.get("threshold", 0))
        total = context.document_fields.get("total_amount", 0)
        if float(total) > threshold:
            return CardResult(
                status=CardStatus.SUCCESS,
                message=f"Amount {total} exceeds threshold {threshold}",
            )
        return CardResult(
            status=CardStatus.FAILED,
            message=f"Amount {total} below threshold {threshold}",
        )
```

{% hint style="info" %}
`CardStatus` tem três valores, que correspondem diretamente às arestas do workflow:

| Status | Aresta seguida | Use para |
|--------|------------|------------|
| `SUCCESS` | `success` | O cartão foi bem-sucedido — vale para condições e ações. |
| `FAILED` | `failed_condition` | **Somente cartões de condição.** A condição foi avaliada como falsa — o workflow segue o ramo "else". Os cartões de ação não têm o ponto de conexão `failed_condition`; por isso, retornar `FAILED` em uma ação deixa a execução sem caminho a seguir. |
| `ERROR` | `error` | Uma falha inesperada em tempo de execução (exceção). Vale para condições e ações. |

Em resumo: as ações retornam `SUCCESS` ou `ERROR`; as condições também podem retornar `FAILED`.
{% endhint %}

### sdk\_validate\_card

Executa o pipeline de validação em um cartão de parceiro sem salvá-lo. Há dois modos:

- **Modo A** — Validar um cartão existente pelo ID
- **Modo B** — Validar um novo código-fonte inline

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `card_id` | string | Não | UUID de um cartão existente (Modo A) |
| `app_manifest` | object | Não | Manifesto do aplicativo (Modo B) |
| `card_manifest` | object | Não | Manifesto do cartão (Modo B) |
| `card_type` | string | Não | `action` ou `condition` (Modo B) |
| `source_code` | string | Não | Código-fonte Python (Modo B) |
| `test_code` | string | Não | Código de teste (Modo B) |

{% hint style="info" %}
Informe `card_id` sozinho (Modo A) ou `app_manifest` + `card_manifest` + `source_code` juntos (Modo B).
{% endhint %}

**Etapas de validação:**

1. **Structure** — Verifica a estrutura de arquivos, o esquema do manifesto (`app.json`, `.docflowcompose/flow/...`) e se os pontos de entrada declarados existem.
2. **Locales** — Concilia as chaves de tradução usadas no cartão com os arquivos `locales/<lang>.json`; falha se faltar uma chave em um idioma declarado.
3. **AST Analysis** — Percorre todos os arquivos `.py` em `src/` e verifica importações proibidas, chamadas perigosas e requisitos de hierarquia de classes e assinatura de métodos.
4. **Dependencies** — Valida que todas as importações são resolvidas para módulos permitidos da lista de permissões do SDK.
5. **Tests** — Executa a suíte pytest do cartão com rlimits reduzidos.
6. **Behavioral** — Executa o cartão no sandbox de produção com um contexto simulado mínimo para confirmar o comportamento em tempo de execução.

As etapas são executadas em ordem; a primeira que falhar interrompe as demais. A etapa 6 (Behavioral) também é executada novamente no momento da aprovação, como verificação de defesa em profundidade antes de o cartão ser ativado.

### sdk\_test\_card

Executa um cartão de parceiro em um ambiente isolado (sandbox) com um contexto simulado. O sandbox impõe builtins restritos, uma lista de permissões de importação, um tempo limite de execução e limites reduzidos de recursos do processo — as mesmas restrições sob as quais o cartão é executado depois de aprovado.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `card_id` | string | Não | UUID de um cartão existente (Modo A) |
| `source_code` | string | Não | Código-fonte para teste inline (Modo B) |
| `class_name` | string | Não | Nome da classe para teste inline (Modo B) |
| `variables` | object | Não | Variáveis passadas ao construtor do cartão |
| `mock_context` | object | Não | Contexto de execução simulado |

**Campos do contexto simulado:**

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

A ferramenta retorna `execution_success` (se o sandbox executou o cartão até o fim — um tempo limite excedido, uma violação de importação ou uma exceção lançada o define como `false`), `card_status` (o `CardStatus` retornado pelo próprio `execute()`), a `message` e os `data` do cartão, os `logs` capturados e `execution_time_ms`.

### sdk\_import\_github

Importa um aplicativo de parceiro de um repositório do GitHub. Clona o repositório, lê o `app.json` e importa todos os cartões encontrados no diretório `.docflowcompose`.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `github_url` | string | Sim | URL HTTPS do GitHub (por exemplo, `https://github.com/org/repo`) |
| `branch` | string | Não | Branch a clonar (padrão: `main`) |
| `token` | string | Não | Token do GitHub para repositórios privados |

**Estrutura de repositório esperada:**

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

## Ferramentas de gerenciamento

### sdk\_list\_submissions

Lista todas as submissões de cartões de parceiros da organização atual.

**Parâmetros:** nenhum

### sdk\_get\_submission\_status

Obtém o status de validação e o relatório de uma submissão específica de cartão de parceiro.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `card_id` | string | Sim | UUID do cartão de parceiro |

### sdk\_approve\_card

Aprova um cartão de parceiro validado e o ativa. A aprovação executa novamente a validação AST e comportamental como verificação de defesa em profundidade, define `partner_status = approved` e `enabled = true` e registra o cartão no registro de execução. Depois de aprovado, o cartão aparece em `list_cards` para **todas as organizações**, e não apenas para a que o submeteu.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `card_id` | string | Sim | UUID do cartão de parceiro |

{% hint style="warning" %}
Exige permissões de administrador da organização. O cartão deve estar no estado `validated`. Os cartões rejeitados precisam ser reenviados e validados novamente antes de poderem ser aprovados.
{% endhint %}

### sdk\_reject\_card

Rejeita uma submissão de cartão de parceiro e a desativa.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `card_id` | string | Sim | UUID do cartão de parceiro |
| `reason` | string | Não | Motivo da rejeição |

{% hint style="warning" %}
Exige permissões de administrador da organização.
{% endhint %}

### sdk\_delete\_submission

Exclui de forma lógica (soft delete) uma submissão de cartão de parceiro, independentemente do estado atual. Define `partner_status = deleted`, `enabled = false` e `deprecated = true`. A linha é mantida para fins de auditoria, mas fica oculta das listagens de submissões e de `list_cards`.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `card_id` | string | Sim | UUID do cartão de parceiro |

{% hint style="warning" %}
Exige permissões de administrador da organização.
{% endhint %}

### sdk\_list\_cards\_picker

Lista todos os cartões habilitados e não obsoletos com indicadores de função. Útil para determinar quais cartões podem ser usados em quais tipos de nó ao construir workflows.

**Parâmetros:** nenhum

## Recursos atuais e roteiro

O Partner Card SDK está sendo lançado de forma incremental. Veja o que seu cartão já pode usar hoje e o que ainda está sendo implementado:

| Recurso | Status |
|------------|--------|
| **Condições de campo** — ler campos do documento em `context.document_fields` e ramificar com base nos valores deles dentro de cartões de condição | ✅ Implementado |
| **Requisições HTTP de saída** — chamar serviços externos de dentro de um cartão | 🚧 Em implementação |
| **Informações estendidas do documento** — metadados adicionais do documento (além de `document_id`, `document_type` e `document_fields`) expostos no `ExecutionContext` | 🚧 Em implementação |
| **Auxiliares de consulta a tabelas do banco de dados** — auxiliares nativos para ler tabelas de dados mestres / de consulta do DocBits dentro de um cartão | 📅 Previsto para a 1.1 |
| **Visualizador de código-fonte do cartão de parceiro** — visualização somente leitura do código do cartão de parceiro submetido na interface do DocBits, para que os administradores possam inspecionar o que estão aprovando | 📅 Previsto para a 1.1 |

{% hint style="info" %}
Se o seu cartão precisar de um recurso que ainda está em andamento, ele falhará na validação (importação proibida, atributo de contexto ausente ou restrição do sandbox) até que a parte correspondente seja entregue. Esta página será atualizada à medida que cada recurso for lançado.
{% endhint %}

{% hint style="danger" %}
**Os cartões de parceiros executam código de terceiros — use por sua conta e risco.**

Os cartões enviados pelo Partner Card SDK são apenas **parcialmente validados pelo DocBits**. O pipeline de validação verifica a estrutura, os idiomas, as importações, os padrões AST, as dependências, os testes do próprio cartão e uma execução comportamental básica no sandbox — ele **não** constitui uma auditoria de segurança completa nem uma garantia funcional da lógica de negócio do cartão.

Depois que um administrador da organização aprova um cartão de parceiro, ele passa a ficar disponível para todas as organizações da plataforma e é executado no sandbox de produção com documentos reais. Aprovar e habilitar um cartão de parceiro é, portanto, uma decisão explícita de confiança do administrador que aprova. O DocBits não assume nenhuma responsabilidade por perda de dados, roteamento incorreto, vazamento de informações ou qualquer outro resultado causado por um cartão de parceiro que você decida instalar ou aprovar.

Se você não for o autor original do cartão, revise o código-fonte (e, quando a 1.1 for lançada, use o visualizador de código-fonte do cartão de parceiro) antes de aprová-lo.
{% endhint %}
