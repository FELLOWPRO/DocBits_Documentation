# 工作流示例：条件导出触发器

<figure><img src="../../../.gitbook/assets/image (3) (2).png" alt=""><figcaption></figcaption></figure>

此工作流概述了启动导出流程的条件。它确保只有符合所有指定条件的文档才会进入导出处理，从而提升数据完整性，并确保符合业务规则。

### 何时：

* 系统评估某个文档是否符合导出条件时。

### 逻辑：

1. **文档类型检查**
   * 文档必须属于特定类型（例如“发票”或“收据”）。请指定符合导出流程条件的文档类型。
2. **状态验证**
   * 文档当前状态必须符合预定义条件（例如“已批准”或“可导出”），以表明文档已准备好进行后续处理。
3. **上下文条件**
   * 执行其他检查，以确保文档详情符合特定要求。这些检查可能包括验证订单确认单或采购订单中的信息。请指定必须满足的具体条件。例如：
     * 订单确认单中列出的所有项目均与采购订单中的项目一致。
     * 订单确认单中的总金额与采购订单中的总金额一致。
     * 订单确认单中指定的交货日期与采购订单中的交货日期一致。

### 然后：

#### 操作：

* **启动导出**
  * 如果满足上述所有条件，系统将自动启动该文档的导出流程。
  * 这可能包括生成导出文件、向外部系统发送数据，或在其他应用程序中触发工作流。

#### 实施示例：

```yaml
rules:
  - description: "Conditional Export Trigger"
    conditions:
      - type: "DocumentType"
        criteria: "<SpecifyDocumentType>"
      - type: "Status"
        criteria: "<SpecifyStatus>"
      - type: "DetailMatch"
        criteria:
          - "ItemMatch"
          - "AmountMatch"
          - "DateMatch"
    actions:
      - operation: "StartExport"
```
