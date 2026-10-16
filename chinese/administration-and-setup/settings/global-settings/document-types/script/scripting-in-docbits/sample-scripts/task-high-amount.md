# 高额发票任务

## 此脚本的作用是什么？

当发票总额超过某个阈值（例如 100,000）时创建一个审批任务。任务会分配给“财务审批”组，并触发电子邮件通知，以确保及时审核。

## 触发器

文档类型 **INVOICE** 上的 `AFTER_FORMATTING`

## 完整脚本

```python
# Read total amount from the document
total = get_field_value(document_data, "total_amount", "0")

try:
    if float(total) > 100000:
        # Find the Finance Approval group by name
        finance_group = get_group_by_name(org_id, "Finance Approval")

        # Create an approval task
        create_document_task(
            user,
            document_data,
            title="Amount > 100,000 - Approval required",
            description=f"Total amount: {total}",
            priority="HIGH",
            assigned_to_user_id=None,
            assigned_to_group_id=str(finance_group.id) if finance_group else None,
            send_email=True
        )
except ValueError:
    pass
```

## 分步说明

1. **读取总金额**，从文档中获取总金额
2. **检查阈值** — 仅当金额超过 100,000 时继续
3. 使用 `get_group_by_name()` **按名称查找组**，以动态获取组 ID
4. **创建任务**，将任务分配给财务组，并设置高优先级和电子邮件通知

## 使用的函数

- [get\_field\_value()](../field-functions.md#get\_field\_value) — 读取字段值
- [get\_group\_by\_name()](../business-logic-functions.md#get\_group\_by\_id--get\_group\_by\_name) — 按名称查找组
- [create\_document\_task()](../business-logic-functions.md#create\_document\_task) — 创建审批任务
