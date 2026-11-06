# 面向开发人员

本页面向编写 JSON 模板或通过代码启动测试的开发人员和 CI 负责人。

## 模板 JSON 概览

模板是一个 JSON 文档（schema 版本 1；schema 1.1 至 1.3 增加了更多步骤和设置）。使用下载图标导出任意模板，即可查看完整示例。

```json
{
  "schemaVersion": 1,
  "id": "my-testing-page-check",
  "name": "Testing page check",
  "category": "smoke",
  "version": "1.0.0",
  "timeoutMs": 60000,
  "allowWrites": false,
  "params": {
    "document_id": { "type": "string", "required": true, "description": "Document to open" }
  },
  "steps": [
    { "id": "open", "action": "navigate", "route": "/settings/testing" },
    { "id": "badge", "action": "waitFor", "target": "testing.environment-badge", "state": "visible" }
  ]
}
```

* `id` 和 `version` 用于标识模板；已保存的版本不会再改变，更改请以新的 `version` 保存。
* `params` 声明输入所提供的值；步骤以 `{{params.<name>}}` 引用它们。从 schema 1.3 起，步骤可以记住一个值（`captureValue`、`as`），后续步骤以 `{{vars.<name>}}` 使用它。
* `section`（`prepare`、`check`、`cleanup`）将步骤归入某个阶段。从 schema 1.3 起，`cleanup` 步骤必须是最后的步骤，即使在失败之后也会运行。`reload`（schema 1.3）会重新加载页面，之后运行继续进行。
* 上传、导出、删除或批准的模板必须设置 `allowWrites: true`。
* 步骤通过稳定的测试 ID（`target`）定位元素，而不是通过可见文本，因此模板适用于所有界面语言。
* 保存前请先验证：**导入 JSON → 验证**，或 `POST /live-tests/validate`。

## 通过 REST 或 Playwright 启动输入

前提条件：组织管理员令牌、组织 ID、输入 ID，以及已开启 **允许从外部启动** 的浏览器标签页的 `session_id`。

```http
POST https://eu.api.docbits.com/testing/start
Authorization: Bearer <token>
X-ORG-ID: <organisation id>
Content-Type: application/json

{ "input_id": "<input id>", "session_id": "<session id>", "source": "playwright" }
```

响应为 `202`，包含 `log_id`、`run_id` 和 `status`。轮询 `GET /testing/logs/<log_id>`，直到结果最终确定。
仅对会写入数据的模板才添加 `"confirm_writes": true`，并且仅在确属本意时添加。

```ts
// Playwright test (API request context)
const res = await request.post(`${API}/testing/start`, {
  headers: { Authorization: `Bearer ${token}`, 'X-ORG-ID': orgId },
  data: { input_id: inputId, session_id: sessionId, source: 'playwright' },
});
expect(res.status()).toBe(202);
const { log_id } = await res.json();
// poll `${API}/testing/logs/${log_id}` until the result is PASS, FAIL or BLOCKED
```

请使用您所在区域的 API 主机（主机列表请参阅 [DocBits MCP](https://docs.docbits.com/advanced-functions-and-tools/docbits-mcp)）。
日志的 CSV：`GET /testing/logs/export.csv`（筛选条件与列表相同）和 `GET /testing/logs/<log_id>/export.csv`。

## 通过打开开始链接启动

如果您的自动化程序控制的是已登录的浏览器，请打开模板的开始链接，而不是调用 API：

`https://<your-environment>/settings/testing?run=<template>&version=<version>&input=<input>&autostart=1`

`run` 是模板键（必填），`version` 固定使用某个已保存版本（默认：最新版本），`input` 按名称或 ID 指定已保存的输入，`autostart=1` 可让只读取数据的模板无需点击即可启动。会写入数据的模板仍保留确认步骤，因此运行会等待 `testing-start-confirm`。该链接仅在组织管理员已登录的浏览器中有效；点击操作发生在该标签页中。

```ts
// signed in as an organisation admin (your login helper)
await page.goto('https://<your-environment>/settings/testing?run=default-smoke-analytics&version=1.0.0');
const start = page.getByTestId('testing-start-confirm');
const status = page.getByTestId('testing-run-status');
await start.or(status).first().waitFor();
if (await start.isVisible()) await start.click();
await expect(status).toHaveAttribute('data-status', /(passed|failed|blocked|cancelled)$/);
```

`data-status` 的值为 `running`、`passed`、`failed`、`blocked` 或 `cancelled`。`blocked` 表示规则在测试步骤运行之前阻止了本次运行。参数被读取后会从 URL 中移除，因此重新加载页面不会再次启动测试。可在启动对话框的 **从外部开始 → 开始链接** 下复制该链接。

## 通过 MCP 启动

DocBits MCP 服务器提供 Testing 工具 `testing_list_templates`、`testing_list_inputs`、`testing_start`、
`testing_get_log` 和 `testing_list_logs`，以及用于已注册标签页的 `list_test_sessions`。`testing_start` 需要
明确指定 `session_id`；只有在用户同意之后才会设置 `confirm_writes`。敏感值仅在该次运行中传递，
绝不会被存储。

## 浏览器内运行器的限制

* 测试以注册该标签页的用户身份运行：不登录，也不切换角色。
* 整页重新加载会结束运行，但模板自身的 `reload` 步骤（schema 1.3）除外。
* 无法操作浏览器原生对话框（文件选择器、打印、警告框）；文件上传使用组织文件或服务器测试文件。
* 截屏步骤会被跳过（运行变为 **已阻止**）。
如需更多功能，请直接使用 Playwright。
