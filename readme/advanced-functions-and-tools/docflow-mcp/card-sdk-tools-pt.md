# Ferramentas do Card SDK

As ferramentas do Card SDK permitem criar, validar, testar e gerenciar cards de parceiros personalizados através do MCP. Os cards de parceiros estendem o DocFlow com lógica de negócios personalizada escrita em Python.

## Ciclo de Vida do Card

Um card de parceiro passa pelos seguintes estados de submissão (`partner_status`):

| Estado | Significado | Visibilidade no workflow |
|-------|---------|---------------------|
| `validating` | Submissão aceita; o pipeline de validação está em execução. | Apenas a organização que submeteu |
| `validated` | Todas as etapas de validação passaram. Aguardando aprovação do admin. | Apenas a organização que submeteu |
| `rejected` | Falha de validação ou um admin rejeitou o card. O código-fonte é mantido para inspeção. | Apenas a organização que submeteu |
| `approved` | O admin aprovou o card; `enabled = true`. | **Todas as organizações** |
| `disabled` | Card previamente aprovado que um admin desativou. | Apenas a organização que submeteu |
| `deleted` | Excluído de forma suave; não retornado nas listagens de submissões. | Oculto |

{% hint style="warning" %}
**Visibilidade entre organizações:** Um card de parceiro só fica disponível para os nós de workflow em `list_cards` depois de ter sido **aprovado**. Cards de parceiro aprovados são visíveis para todas as organizações na plataforma — a aprovação é uma ativação global, não uma ativação por organização. Cards não aprovados (validating, validated, rejected, disabled) são visíveis apenas para a organização que os submeteu.
{% endhint %}

Fluxo típico:

1. **Crie** um card com `sdk_create_card` ou `sdk_import_github` — executa o pipeline de validação e armazena o card com `partner_status = validated` (ou `rejected` em caso de falha).
2. **Valide** com `sdk_validate_card` para reverificar um card existente ou executar a seco um novo código-fonte sem persistir.
3. **Teste** com `sdk_test_card` para executar o card no sandbox contra um contexto mock.
4. **Aprove** com `sdk_approve_card` (apenas admin da organização) — reexecuta as validações AST e comportamental e, em seguida, define `partner_status = approved` e `enabled = true`.
5. Após a aprovação, o card aparece em `list_cards` para cada organização e pode ser referenciado pelos nós de workflow.

## Ferramentas de Desenvolvimento

### sdk\_create\_card

Criar um novo card de parceiro a partir do código-fonte e manifestos. Executa o pipeline de validação completo (consulte [Etapas de Validação](#sdk_validate_card) abaixo) e armazena o card no banco de dados. O card é colocado no estado `validated` e exige aprovação do admin antes de poder ser usado em workflows.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `app_manifest` | object | Sim | Manifesto da aplicação com id, name, version, info do parceiro |
| `card_manifest` | object | Sim | Manifesto do card com id, title, entry\_point, class\_name, args |
| `card_type` | string | Sim | `action` ou `condition` |
| `source_code` | string | Sim | Código-fonte Python (deve estender `PartnerCard`) |
| `test_code` | string | Sim | Código de teste Pytest para o card |
| `locales` | object | Não | Traduções de localização, ex. `{"en": {...}, "de": {...}}` |

**Exemplo de Manifesto da App:**

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
`CardStatus` tem três valores que mapeiam diretamente para as arestas do workflow:

| Status | Aresta tomada | Use para |
|--------|------------|------------|
| `SUCCESS` | `success` | O card foi bem-sucedido — aplica-se tanto a condições quanto a ações. |
| `FAILED` | `failed_condition` | **Apenas cards de condição.** A condição foi avaliada como false — o workflow toma o ramo "else". Cards de ação não têm um handle `failed_condition`, portanto retornar `FAILED` em uma ação deixa a execução sem saída. |
| `ERROR` | `error` | Uma falha de tempo de execução inesperada (exceção). Aplica-se tanto a condições quanto a ações. |

Em resumo: ações retornam `SUCCESS` ou `ERROR`; condições podem adicionalmente retornar `FAILED`.
{% endhint %}

### sdk\_validate\_card

Executar o pipeline de validação em um card de parceiro sem salvá-lo. Dois modos:

- **Modo A** — Validar um card existente por ID
- **Modo B** — Validar novo código-fonte em modo inline

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `card_id` | string | Não | UUID de um card existente (Modo A) |
| `app_manifest` | object | Não | Manifesto da aplicação (Modo B) |
| `card_manifest` | object | Não | Manifesto do card (Modo B) |
| `card_type` | string | Não | `action` ou `condition` (Modo B) |
| `source_code` | string | Não | Código-fonte Python (Modo B) |
| `test_code` | string | Não | Código de teste (Modo B) |

{% hint style="info" %}
Forneça apenas `card_id` (Modo A) ou `app_manifest` + `card_manifest` + `source_code` juntos (Modo B).
{% endhint %}

**Etapas de Validação:**

1. **Structure** — Verifica o layout dos arquivos, o esquema do manifesto (`app.json`, `.docflowcompose/flow/...`) e se os entry points declarados existem.
2. **Locales** — Concilia as chaves de tradução usadas no card com os arquivos `locales/<lang>.json`; falha se uma chave estiver ausente em um idioma declarado.
3. **AST Analysis** — Percorre cada arquivo `.py` sob `src/` e verifica imports proibidos, chamadas perigosas e requisitos de hierarquia de classe / assinatura de método.
4. **Dependencies** — Valida que todos os imports são resolvidos para módulos permitidos da allowlist do SDK.
5. **Tests** — Executa a suíte pytest do card sob rlimits reduzidos.
6. **Behavioral** — Executa o card no sandbox de produção contra um contexto mock mínimo para confirmar o comportamento em tempo de execução.

As etapas são executadas em ordem; a primeira etapa que falha curto-circuita as demais. A Etapa 6 (Behavioral) também é reexecutada no momento da aprovação como verificação de defesa em profundidade antes que o card seja ativado.

### sdk\_test\_card

Executar um card de parceiro em um ambiente sandbox com um contexto mock. O sandbox aplica builtins restritos, uma allowlist curada de imports, um timeout de execução e limites reduzidos de recursos de processo — as mesmas restrições sob as quais um card é executado depois de aprovado.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `card_id` | string | Não | UUID de um card existente (Modo A) |
| `source_code` | string | Não | Código-fonte para teste inline (Modo B) |
| `class_name` | string | Não | Nome da classe para teste inline (Modo B) |
| `variables` | object | Não | Variáveis a passar para o construtor do card |
| `mock_context` | object | Não | Contexto de execução mock |

**Campos do Mock Context:**

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

A ferramenta retorna `execution_success` (indica se o sandbox executou o card até o fim — um timeout, violação de import ou exceção lançada o define como `false`), `card_status` (o `CardStatus` retornado pelo próprio `execute()`), o `message` e `data` do card, os `logs` capturados e `execution_time_ms`.

### sdk\_import\_github

Importar um app de parceiro a partir de um repositório do GitHub. Clona o repo, lê `app.json` e importa todos os cards encontrados no diretório `.docflowcompose`.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `github_url` | string | Sim | URL HTTPS do GitHub (ex. `https://github.com/org/repo`) |
| `branch` | string | Não | Branch a clonar (padrão: `main`) |
| `token` | string | Não | Token do GitHub para repositórios privados |

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

## Ferramentas de Gerenciamento

### sdk\_list\_submissions

Listar todas as submissões de cards de parceiros para a organização atual.

**Parâmetros:** Nenhum

### sdk\_get\_submission\_status

Obter o status de validação e o relatório para uma submissão específica de card de parceiro.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `card_id` | string | Sim | UUID do card de parceiro |

### sdk\_approve\_card

Aprovar um card de parceiro validado e ativá-lo. A aprovação reexecuta as validações AST e comportamental como verificação de defesa em profundidade, define `partner_status = approved` e `enabled = true` e registra o card no registry de tempo de execução. Após a aprovação, o card aparece em `list_cards` para **todas as organizações**, não apenas para a que o submeteu.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `card_id` | string | Sim | UUID do card de parceiro |

{% hint style="warning" %}
Requer permissões de admin da organização. O card deve estar no estado `validated`. Cards rejeitados precisam ser reenviados e revalidados antes de poderem ser aprovados.
{% endhint %}

### sdk\_reject\_card

Rejeitar uma submissão de card de parceiro e desativá-la.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `card_id` | string | Sim | UUID do card de parceiro |
| `reason` | string | Não | Motivo da rejeição |

{% hint style="warning" %}
Requer permissões de admin da organização.
{% endhint %}

### sdk\_delete\_submission

Exclusão suave de uma submissão de card de parceiro, independentemente do seu estado atual. Define `partner_status = deleted`, `enabled = false` e `deprecated = true`. A linha é mantida para fins de auditoria, mas é ocultada das listagens de submissões e de `list_cards`.

**Parâmetros:**

| Parâmetro | Tipo | Obrigatório | Descrição |
|-----------|------|----------|-------------|
| `card_id` | string | Sim | UUID do card de parceiro |

{% hint style="warning" %}
Requer permissões de admin da organização.
{% endhint %}

### sdk\_list\_cards\_picker

Listar todos os cards habilitados e não obsoletos com flags de papel. Útil para determinar quais cards podem ser usados em quais tipos de nó ao construir workflows.

**Parâmetros:** Nenhum

## Capacidades Atuais e Roadmap

O Partner Card SDK está sendo lançado de forma incremental. Aqui está com o que seu card pode contar hoje e o que ainda está sendo integrado:

| Capacidade | Status |
|------------|--------|
| **Condições em campos** — ler campos de documento de `context.document_fields` e ramificar com base em seus valores em cards de condição | ✅ Implementado |
| **Requisições HTTP de saída** — chamar serviços externos de dentro de um card | 🚧 Sendo adicionado |
| **Informações estendidas do documento** — metadados adicionais do documento (além de `document_id`, `document_type` e `document_fields`) expostos em `ExecutionContext` | 🚧 Sendo adicionado |
| **Helpers de lookup em tabelas do banco de dados** — helpers integrados para ler de tabelas master-data / lookup do DocBits de dentro de um card | 📅 Planejado para 1.1 |
| **Visualizador do código da card de parceiro** — visualização somente leitura do código submetido da card de parceiro na interface do DocBits, para que os admins possam inspecionar o que estão aprovando | 📅 Planejado para 1.1 |

{% hint style="info" %}
Se seu card precisar de uma capacidade que ainda está em andamento, ele falhará na validação (import proibido, atributo de contexto ausente ou restrição de sandbox) até que a peça correspondente seja entregue. Esta página será atualizada conforme cada capacidade for sendo lançada.
{% endhint %}

{% hint style="danger" %}
**Cards de parceiros executam código de terceiros — uso por sua conta e risco.**

Cards enviados pelo Partner Card SDK são apenas **parcialmente validados pelo DocBits**. O pipeline de validação verifica estrutura, locales, imports, padrões AST, dependências, os próprios testes do card e uma execução comportamental de smoke no sandbox — ele **não** constitui uma auditoria de segurança completa nem uma garantia funcional da lógica de negócio do card.

Uma vez que um admin da organização aprove um card de parceiro, ele fica disponível para todas as organizações na plataforma e roda no sandbox de produção contra documentos reais. Aprovar e habilitar um card de parceiro é, portanto, uma decisão explícita de confiança do admin que aprova. O DocBits não aceita qualquer responsabilidade por perda de dados, roteamento incorreto, vazamento de informações ou qualquer outro resultado causado por um card de parceiro que você escolha instalar ou aprovar.

Se você não é o autor original do card, revise o código-fonte (e, depois que a 1.1 for lançada, use o visualizador do código da card de parceiro) antes de aprová-lo.
{% endhint %}
