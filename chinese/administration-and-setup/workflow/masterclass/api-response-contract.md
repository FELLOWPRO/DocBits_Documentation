---
description: "P1：验证 API 调用与后续响应使用"
---

# P1：验证 API 调用与后续响应使用

**Call API** v2 将配置路径接到 DocBits API 基础地址，并使用当前组织上下文。**Send HTTPS Request** v2 使用外部 URL 和自行配置的请求头。完整外部 URL 不能直接替代 Call API 路径。两张卡片在 Advanced Test 中都会模拟发送。

经检查的 HTTPS 动作记录状态和响应文本，但不向后续卡片暴露可自由命名的 JSON 响应存储。Call API 会把响应文本转换为布尔值。因此 HTTP 200、有效 JSON 和后续业务处理成功需要分别证明。不要编造 `api.response.cost_center` 之类的访问语法。

对于外部返回 `{"cost_center":"4711"}`，应约定明确受支持的回写操作或回调，将值写入文档字段。验证已保存字段，再在指定的后续运行中读取。直接传递响应数据需要具有明确输出契约的卡片或扩展。配置中填写 JSON 也不能自动证明实际发送的 JSON 字节。

使用自有测试目标，检查方法、请求头、实际请求体、状态及响应结构。覆盖 4xx、5xx、超时、无效 JSON 和重复触发。重试写请求前，应先检查第一次是否已经被接收。示例 URL 是保留占位地址，并未作为可访问服务测试。

## 卡片与示例参数

这些值描述单张卡片的参数，不是可直接导入的完整工作流。YOUR_* 必须替换为自有测试选项；隐藏的调用方 ID 由设计器管理。目录依据：Dev、DocFlow 2.10.38、2026 年 10 月 21 日。请另外核对本组织可用版本与授权。

### `call_api` · v2

标识: `6ca5e621-af72-4f55-aa2e-b3caa288722a`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `params` | `params:str` | `"{}"` |
| `api_endpoint` | `api_endpoint:str` | `"YOUR_RELATIVE_API_PATH"` |
| `data` | `data:str` | `"{}"` |
| `method` | `put / post / delete / get` | `"get"` |

### `action_https_request` · v2

标识: `18d06ca4-3aca-4e49-b75c-566ade2fcb10`

| 参数 | 类型 / 选项 | 示例 |
| --- | --- | --- |
| `data` | `data` | `"{}"` |
| `params` | `params` | `"{}"` |
| `url` | `url:str` | `"https://training.example.invalid/status"` |
| `headers` | `headers:str` | `"{}"` |
| `method` | `put / post / delete / get` | `"get"` |

## 业务测试用例

| 用例 | 输入 / 配置 | 预期结果 |
| --- | --- | --- |
| API-01 | Advanced Test | 经过模拟；没有送达证明 |
| API-02 | HTTPS: 4xx / 5xx | error |
| API-03 | timeout | 重试前检查是否收到 |
| API-04 | {"cost_center":"4711"} | 不会自动提供 api.response.cost_center |
| API-05 | POST × 2 | 检查目标侧重复处理 |

## 验证依据与限制

参数与行为已对照 Dev 目录和经检查的源码。业务用例是验收操作指引；本章未执行真实人工审批、实际数据更改或外部送达。

[继续学习](../workflow-learning-path.md) · [练习包](../workflow-training-kit.md)
