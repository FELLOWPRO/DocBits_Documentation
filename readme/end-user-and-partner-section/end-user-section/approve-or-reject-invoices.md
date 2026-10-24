# 批准或拒绝发票

此视频从审核员的角度展示了审批流程。

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/invoice-approval-customer/v1/zh.mp4" %}
批准或拒绝发票
{% endembed %}

[观看带字幕的视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/invoice-approval-customer/v1/zh.html)

显示的是实际应用程序；选项的措辞可能取决于部署的版本。

使用审批功能记录您对已验证发票的业务决定。您需要访问该文档并拥有其当前审批阶段的权限。视频使用普通审核账号。

## 审核并决定

1. 打开分配给您的发票并检查当前的审批阶段。
2. 将发票号码、供应商、日期和总额与原件进行比较。同时检查明细行和税额。技术验证不能取代您的业务审核。
3. 填写清晰的审核备注。批准正确的发票，或在需要澄清时填写具体原因后拒绝发票。等待操作完成。
4. 重新打开文档并检查其审批历史记录。确认审核人员、操作时间、决定和完整备注均已正确保存。

<figure><img src="../../.gitbook/assets/customer-check-zh-433b0b338197.png" alt="填写的发票表单与原件的比较。"><figcaption><p>填写的发票表单与原件的比较。</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/customer-rejected-zh-433b0b338197.png" alt="已保存的拒绝结果及其原因。"><figcaption><p>已保存的拒绝结果及其原因。</p></figcaption></figure>

## 检查下一阶段

当配置了二次审批时，您的首次审批会使发票等待另一位授权审核员。它尚未完全获得批准。被拒绝的发票需要进行业务核实；更正和重新提交遵循您配置的流程。

审批历史记录条目并不能证明数据已到达ERP系统。在这个独立的测试示例中，数据读取通道没有外部ERP目标。当显示技术状态 `pending_data_fetch` 时，表示文档正在等待数据读取。

## 相关页面

- [验证屏幕](validation-screen/README.md)
- [文档任务](tasks.md)
