# Card SDK 工具

Card SDK 工具可通过 MCP 创建、验证、测试和管理自定义合作伙伴卡片。合作伙伴卡片通过以 Python 编写的自定义业务逻辑扩展 DocFlow。

## 卡片生命周期

合作伙伴卡片会经历以下提交状态（`partner_status`）：

| 状态 | 含义 | 工作流可见性 |
|-------|----------|---------------------|
| `validating` | 已接受提交；正在运行验证流程。 | 仅提交组织 |
| `validated` | 已通过所有验证阶段。等待管理员审批。 | 仅提交组织 |
| `rejected` | 验证失败，或管理员拒绝了卡片。保留源代码以供检查。 | 仅提交组织 |
| `approved` | 管理员已批准卡片；`enabled = true`。 | **所有组织** |
| `disabled` | 先前已批准、后被管理员停用的卡片。 | 仅提交组织 |
| `deleted` | 已软删除；提交列表不会返回该卡片。 | 隐藏 |

{% hint style="warning" %}
**组织可见性：** 只有获得 **approved** 状态后，合作伙伴卡片才会在 `list_cards` 中对工作流节点可用。已批准的合作伙伴卡片对平台上的每个组织都可见——审批是全局激活，而非针对单个组织的激活。未获批准的卡片（validating、validated、rejected、disabled）仅对提交它们的组织可见。
{% endhint %}

典型流程：

1. 使用 `sdk_create_card` 或 `sdk_import_github` **创建**卡片——运行验证流程，并将卡片存储为 `partner_status = validated`（失败时为 `rejected`）。
2. 使用 `sdk_validate_card` **验证**卡片，重新检查现有卡片，或对新源代码进行试运行而不持久化。
3. 使用 `sdk_test_card` **测试**卡片，在沙箱中通过模拟上下文执行卡片。
4. 使用 `sdk_approve_card` **批准**卡片（仅限组织管理员）——重新运行 AST 和行为验证，然后设置 `partner_status = approved` 和 `enabled = true`。
5. 获批后，卡片会显示在每个组织的 `list_cards` 中，并可从工作流节点引用。

## 开发工具

### sdk\_create\_card

根据源代码和清单创建新的合作伙伴卡片。运行完整的验证流程（见下文[验证阶段](#sdk_validate_card)），并将卡片存储在数据库中。卡片会进入 `validated` 状态，必须经管理员审批后才能在工作流中使用。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
|-----------|------|----------|-------------|
| `app_manifest` | object | 是 | 应用清单，包含 id、name、version 和合作伙伴信息 |
| `card_manifest` | object | 是 | 卡片清单，包含 id、title、entry\_point、class\_name 和 args |
| `card_type` | string | 是 | `action` 或 `condition` |
| `source_code` | string | 是 | Python 源代码（必须扩展 `PartnerCard`） |
| `test_code` | string | 是 | 卡片的 Pytest 测试代码 |
| `locales` | object | 否 | 本地化翻译，例如 `{"en": {...}, "de": {...}}` |

**应用清单示例：**

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

**卡片清单示例：**

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

**源代码示例：**

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
`CardStatus` 有三个值，它们直接映射到工作流边：

| 状态 | 采用的边 | 用途 |
|--------|------------|------------|
| `SUCCESS` | `success` | 卡片执行成功——适用于条件卡片和操作卡片。 |
| `FAILED` | `failed_condition` | **仅限条件卡片。** 条件求值结果为 false——工作流会进入“else”分支。操作卡片没有 `failed_condition` 端口，因此操作卡片返回 `FAILED` 时，运行流程将无路可走。 |
| `ERROR` | `error` | 意外的运行时故障（异常）。适用于条件卡片和操作卡片。 |

简而言之：操作卡片返回 `SUCCESS` 或 `ERROR`；条件卡片还可以返回 `FAILED`。
{% endhint %}

### sdk\_validate\_card <a id="sdk_validate_card"></a>

对合作伙伴卡片运行验证流程，但不保存卡片。有两种模式：

- **模式 A** — 按 ID 验证现有卡片
- **模式 B** — 内联验证新源代码

**参数：**

| 参数 | 类型 | 必填 | 描述 |
|-----------|------|----------|-------------|
| `card_id` | string | 否 | 现有卡片的 UUID（模式 A） |
| `app_manifest` | object | 否 | 应用清单（模式 B） |
| `card_manifest` | object | 否 | 卡片清单（模式 B） |
| `card_type` | string | 否 | `action` 或 `condition`（模式 B） |
| `source_code` | string | 否 | Python 源代码（模式 B） |
| `test_code` | string | 否 | 测试代码（模式 B） |

{% hint style="info" %}
请仅提供 `card_id`（模式 A），或同时提供 `app_manifest` + `card_manifest` + `source_code`（模式 B）。
{% endhint %}

**验证阶段：**

1. **结构** — 验证文件布局、清单架构（`app.json`、`.docflowcompose/flow/...`），以及声明的入口点是否存在。
2. **本地化** — 核对卡片中使用的翻译键与 `locales/<lang>.json` 文件；如果某个声明语言缺少翻译键，则验证失败。
3. **AST 分析** — 遍历 `src/` 下的每个 `.py` 文件，检查是否包含禁止的导入、危险调用，以及类层次结构和方法签名是否符合要求。
4. **依赖项** — 验证所有导入是否都能解析为 SDK 白名单中的允许模块。
5. **测试** — 在降低的 rlimits 下运行卡片的 pytest 测试套件。
6. **行为** — 在生产沙箱中通过最小化的模拟上下文执行卡片，以确认其运行时行为。

各阶段按顺序运行；首个失败阶段会导致后续阶段不再运行。阶段 6（行为）也会在审批时重新运行，在激活卡片前进行纵深防御检查。

### sdk\_test\_card

在沙箱环境中通过模拟上下文执行合作伙伴卡片。沙箱会强制限制内置功能、使用经过筛选的导入允许列表、设置执行超时并降低进程资源限制——卡片获批后运行时也会受到相同限制。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
|-----------|------|----------|-------------|
| `card_id` | string | 否 | 现有卡片的 UUID（模式 A） |
| `source_code` | string | 否 | 用于内联测试的源代码（模式 B） |
| `class_name` | string | 否 | 用于内联测试的类名（模式 B） |
| `variables` | object | 否 | 传递给卡片构造函数的变量 |
| `mock_context` | object | 否 | 模拟执行上下文 |

**模拟上下文字段：**

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

该工具会返回 `execution_success`（沙箱是否将卡片运行至完成——超时、违反导入限制或抛出异常都会使其值为 `false`）、`card_status`（`execute()` 本身返回的 `CardStatus`）、卡片的 `message` 和 `data`、捕获的 `logs`，以及 `execution_time_ms`。

### sdk\_import\_github

从 GitHub 仓库导入合作伙伴应用。该工具会克隆仓库、读取 `app.json`，并导入 `.docflowcompose` 目录中的所有卡片。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
|-----------|------|----------|-------------|
| `github_url` | string | 是 | GitHub HTTPS URL（例如 `https://github.com/org/repo`） |
| `branch` | string | 否 | 要克隆的分支（默认：`main`） |
| `token` | string | 否 | 私有仓库的 GitHub 令牌 |

**预期的仓库结构：**

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

## 管理工具

### sdk\_list\_submissions

列出当前组织提交的所有合作伙伴卡片。

**参数：** 无

### sdk\_get\_submission\_status

获取指定合作伙伴卡片提交的验证状态和报告。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
|-----------|------|----------|-------------|
| `card_id` | string | 是 | 合作伙伴卡片的 UUID |

### sdk\_approve\_card

批准已验证的合作伙伴卡片并将其激活。审批会重新运行 AST 和行为验证，以进行纵深防御检查；设置 `partner_status = approved` 和 `enabled = true`；并将卡片注册到运行时注册表中。获批后，卡片会显示在**每个组织**的 `list_cards` 中，而不只是提交它的组织。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
|-----------|------|----------|-------------|
| `card_id` | string | 是 | 合作伙伴卡片的 UUID |

{% hint style="warning" %}
需要组织管理员权限。卡片必须处于 `validated` 状态。被拒绝的卡片必须重新上传并重新验证后才能获批。
{% endhint %}

### sdk\_reject\_card

拒绝合作伙伴卡片提交并将其停用。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
|-----------|------|----------|-------------|
| `card_id` | string | 是 | 合作伙伴卡片的 UUID |
| `reason` | string | 否 | 拒绝原因 |

{% hint style="warning" %}
需要组织管理员权限。
{% endhint %}

### sdk\_delete\_submission

软删除合作伙伴卡片提交，无论其当前状态如何。此操作会设置 `partner_status = deleted`、`enabled = false` 和 `deprecated = true`。数据库行会保留以供审计，但不会显示在提交列表和 `list_cards` 中。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
|-----------|------|----------|-------------|
| `card_id` | string | 是 | 合作伙伴卡片的 UUID |

{% hint style="warning" %}
需要组织管理员权限。
{% endhint %}

### sdk\_list\_cards\_picker

列出所有已启用且未弃用的卡片及其角色标记。构建工作流时，可用它确定哪些卡片能用于哪些节点类型。

**参数：** 无

## 当前功能与路线图

Partner Card SDK 正在分阶段推出。以下是卡片目前可依赖的功能，以及仍在接入中的功能：

| 功能 | 状态 |
|------------|--------|
| **字段条件** — 从 `context.document_fields` 读取文档字段，并在条件卡片中根据其值进行分支判断 | ✅ 已实现 |
| **外发 HTTP 请求** — 从卡片内部调用外部服务 | 🚧 正在接入 |
| **扩展文档信息** — 在 `ExecutionContext` 上公开其他文档元数据（除 `document_id`、`document_type` 和 `document_fields` 之外） | 🚧 正在接入 |
| **数据库表查询辅助工具** — 可在卡片内部读取 DocBits 主数据/查询表的内置辅助工具 | 📅 计划在 1.1 版推出 |
| **合作伙伴卡片源代码查看器** — 在 DocBits UI 中以只读方式查看已提交的合作伙伴卡片代码，以便管理员检查待审批内容 | 📅 计划在 1.1 版推出 |

{% hint style="info" %}
如果卡片需要仍在开发中的功能，在相应功能上线前，验证会失败（导入被禁止、上下文属性缺失或沙箱限制）。随着各项功能推出，本页面也会更新。
{% endhint %}

{% hint style="danger" %}
**合作伙伴卡片会运行第三方代码——使用风险由你自行承担。**

通过 Partner Card SDK 上传的卡片仅由 DocBits **部分验证**。验证流程会检查结构、本地化、导入、AST 模式、依赖项、卡片自身的测试，以及在沙箱中的行为冒烟测试——但这**不构成完整的安全审计，也不保证卡片业务逻辑正常运行**。

组织管理员批准合作伙伴卡片后，该卡片即对平台上的每个组织开放，并会在生产沙箱中针对真实文档运行。因此，批准并启用合作伙伴卡片是审批管理员明确作出的信任决定。对于你选择安装或批准的合作伙伴卡片所导致的数据丢失、路由错误、信息泄露或任何其他后果，DocBits 概不负责。

如果你不是卡片的原作者，请在批准前检查源代码（1.1 版推出后，也可使用合作伙伴卡片源代码查看器）。
{% endhint %}
