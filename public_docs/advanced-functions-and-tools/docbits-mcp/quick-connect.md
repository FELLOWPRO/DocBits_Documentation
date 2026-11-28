# Quick Connect

三步即可将 AI 助手连接到 DocBits：选择环境、复制一条命令、登录一次。无需 API key。

## 1. 选择环境

请使用与你所在组织相匹配的 **区域**（EU 或 US）和 **环境**（Sandbox 或 Production）对应的 Endpoint。

| 环境 | 区域 | Endpoint |
| --- | --- | --- |
| Sandbox | EU | `https://eu.sandbox.api.docbits.com/v3/mcp` |
| Sandbox | US | `https://us.sandbox.api.docbits.com/v3/mcp` |
| Production | EU | `https://eu.api.docbits.com/v3/mcp` |
| Production | US | `https://us.api.docbits.com/v3/mcp` |

{% hint style="warning" %}
助手以你登录账号的权限运行，并且可以更改数据。**Production** 中的更改会影响你的实时文档。请先在 Sandbox 中试用新的提示词。
{% endhint %}

## 2. 一键或一条命令即可连接

使用按钮将服务器添加到 **Cursor** 或 **VS Code**，或复制命令供终端客户端使用。每个环境使用各自的服务器名称，因此你可以同时连接 Sandbox 和 Production 而不会混淆。

{% tabs %}
{% tab title="Sandbox EU" %}
<a href="https://cursor.com/en/install-mcp?name=docbits-sandbox-eu&config=eyJ1cmwiOiAiaHR0cHM6Ly9ldS5zYW5kYm94LmFwaS5kb2NiaXRzLmNvbS92My9tY3AifQ%3D%3D" class="button primary">Add to Cursor</a> <a href="https://vscode.dev/redirect/mcp/install?name=docbits-sandbox-eu&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Feu.sandbox.api.docbits.com%2Fv3%2Fmcp%22%7D" class="button secondary">Add to VS Code</a>

{% code title="Claude Code" %}
```bash
claude mcp add --transport http docbits-sandbox-eu https://eu.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="OpenAI Codex" %}
```bash
codex mcp add docbits-sandbox-eu --url https://eu.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits-sandbox-eu https://eu.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}
{% endtab %}

{% tab title="Sandbox US" %}
<a href="https://cursor.com/en/install-mcp?name=docbits-sandbox-us&config=eyJ1cmwiOiAiaHR0cHM6Ly91cy5zYW5kYm94LmFwaS5kb2NiaXRzLmNvbS92My9tY3AifQ%3D%3D" class="button primary">Add to Cursor</a> <a href="https://vscode.dev/redirect/mcp/install?name=docbits-sandbox-us&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fus.sandbox.api.docbits.com%2Fv3%2Fmcp%22%7D" class="button secondary">Add to VS Code</a>

{% code title="Claude Code" %}
```bash
claude mcp add --transport http docbits-sandbox-us https://us.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="OpenAI Codex" %}
```bash
codex mcp add docbits-sandbox-us --url https://us.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits-sandbox-us https://us.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}
{% endtab %}

{% tab title="Production EU" %}
<a href="https://cursor.com/en/install-mcp?name=docbits-prod-eu&config=eyJ1cmwiOiAiaHR0cHM6Ly9ldS5hcGkuZG9jYml0cy5jb20vdjMvbWNwIn0%3D" class="button primary">Add to Cursor</a> <a href="https://vscode.dev/redirect/mcp/install?name=docbits-prod-eu&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Feu.api.docbits.com%2Fv3%2Fmcp%22%7D" class="button secondary">Add to VS Code</a>

{% code title="Claude Code" %}
```bash
claude mcp add --transport http docbits-prod-eu https://eu.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="OpenAI Codex" %}
```bash
codex mcp add docbits-prod-eu --url https://eu.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits-prod-eu https://eu.api.docbits.com/v3/mcp
```
{% endcode %}
{% endtab %}

{% tab title="Production US" %}
<a href="https://cursor.com/en/install-mcp?name=docbits-prod-us&config=eyJ1cmwiOiAiaHR0cHM6Ly91cy5hcGkuZG9jYml0cy5jb20vdjMvbWNwIn0%3D" class="button primary">Add to Cursor</a> <a href="https://vscode.dev/redirect/mcp/install?name=docbits-prod-us&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fus.api.docbits.com%2Fv3%2Fmcp%22%7D" class="button secondary">Add to VS Code</a>

{% code title="Claude Code" %}
```bash
claude mcp add --transport http docbits-prod-us https://us.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="OpenAI Codex" %}
```bash
codex mcp add docbits-prod-us --url https://us.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits-prod-us https://us.api.docbits.com/v3/mcp
```
{% endcode %}
{% endtab %}
{% endtabs %}

对于 **Claude Desktop** 和 **claude.ai**，请改为添加自定义连接器：打开连接器设置，选择 **添加自定义连接器**，然后粘贴表格中的 Endpoint。

## 3. 登录一次

首次连接会在浏览器中打开 DocBits 登录页面。如果你已登录 DocBits，会直接进入授权页面。批准后即可连接。

{% tabs %}
{% tab title="Claude Code" %}
启动 Claude Code，运行`/mcp`，选择 DocBits 服务器，然后选择 **Authenticate**。
{% endtab %}

{% tab title="OpenAI Codex" %}
将`docbits-sandbox-eu`替换为你添加的服务器名称：

```bash
codex mcp login docbits-sandbox-eu
```
{% endtab %}

{% tab title="Gemini CLI" %}
Gemini CLI 在首次使用该服务器时打开登录。你也可以从`/mcp`菜单中再次启动它。
{% endtab %}
{% endtabs %}

你只需登录一次。客户端会在 30 天的使用期内自动续期访问权限。

## 4. 检查连接

开始一个新对话并发送以下提示词：

```text
Read only. Call get_api_info and get_current_user. Show the API host and my
organization name. Do not change any setting and do not process documents.
```

回答中的 API host 必须与你选择的 Endpoint 匹配，例如 Sandbox EU 的`eu.sandbox.api.docbits.com`。如果不匹配，请移除该服务器并使用正确的 Endpoint 重新添加。

## 后续步骤

* [示例](examples.md)：用于文档、搜索和分析的现成提示词
* [使用 Claude 或 Codex 配置 DocBits](configuration-with-claude-or-codex.md)：通过预览、确认和撤销安全地更改设置
* [设置与配置](setup-and-configuration.md)：用于自动化的 API key 登录以及 OAuth 登录的工作方式

## 疑难解答

| 症状 | 解决方法 |
| --- | --- |
| 登录页面未打开 | 重新执行登录步骤。在没有浏览器的机器上，请按[设置与配置](setup-and-configuration.md)中所述使用 API key。 |
| 连接后出现`401` | 登录已过期。请重新对服务器进行身份验证。 |
| 助手显示的组织数据不正确 | 你选择了错误的区域或环境。请移除该服务器并添加正确的 Endpoint。 |
| 工具缺失 | 你的 DocBits 角色不允许使用这些功能。请联系管理员。 |
