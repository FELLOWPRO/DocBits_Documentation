# 根据决策表依次分配给用户/组

<figure><img src="../../../../../.gitbook/assets/workflow_card_action_assign_doc_decision_table_sequential_v2-zh-cn.png" alt="根据决策表依次分配给用户/组, 版本 2" width="634"><figcaption><p>版本 2</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/workflow_card_action_assign_doc_decision_table_sequential_no_variables_v2-zh-cn.png" alt="根据决策表将文档按顺序分配给用户/组。 — 版本 2" width="428"><figcaption><p>根据决策表将文档按顺序分配给用户/组。 — 版本 2</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-sequential-dt/v1/zh.mp4" %}

**视频:** 卡片: 按决策表依次分配 · 0:38 · [字幕 (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-sequential-dt/v1/zh.vtt)

<details>

<summary>文字稿</summary>

**按决策表依次分配** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-sequential-dt/v1/zh.mp4#t=0.25)

按决策表依次分配卡片会把文档依次交给决策表返回的用户和组。这张卡片没有设置：一切都来自决策表。

**卡片需要什么** · [0:10](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-sequential-dt/v1/zh.mp4#t=10.683)

它前面需要一张保存返回数据的决策表卡片。它使用决策表返回的所有用户和组，优先级数字最小的最先收到文档。没有优先级的行按优先级一计算。如果决策表没有返回任何人，卡片会走它的错误路径。

**示例：两位审批人依次审批** · [0:27](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-assign-sequential-dt/v1/zh.mp4#t=27.783)

例如，决策表 Example approvers 返回两位审批人，优先级为一和二。发票先交给第一位，审批后再交给第二位。

</details>

## **用途**

“**根据决策表将文档依次分配给用户/组**”工作流卡片会根据决策表的评估结果，动态地将文档分配给用户或组。这样可以确保文档按照预定义规则正确路由。

## **卡片组件**

1. **优先级（值）**
   * **说明**：指定分配的优先级，数值越小，优先级越高。
   * **详细信息**：数值输入字段，可设置优先级值以控制分配顺序。

## **功能**

* **决策表评估**：\
  决策表会评估预定义条件，以确定将文档分配给用户还是组。
* **文档分配**：
  * 如果决策表返回用户，文档会直接分配给该用户。
  * 如果决策表返回组，文档会按照指定的优先级值依次分配给该组成员。

## **设置与配置**

1. 将 **依次分配文档** 卡片添加到工作流中。
2. 配置 **优先级（值）** 字段：
   * 输入数值以设置分配优先级。
3. 保存并激活工作流以应用配置。

## **结论**

“**根据决策表将文档依次分配给用户/组**”工作流卡片可确保高效、动态地路由文档。通过利用决策表逻辑和优先级值，该卡片可将文档准确分配给用户或组，从而简化文档工作流。

<!-- workflow-card-practical-example-20261021 -->

## 实际例子

**何时使用：** 使用决策表选择优先文档分配对象。

**配置：** 配置返回预期用户或组的匹配演示决策表规则，然后选择卡上的该表。

**预期结果及反例：** 返回的分配对象用于顺序文档分配。如果没有匹配的回报，请勿假定默认分配对象；检查此版本的结果和配置的回退行为。

这是说明性配置和预期结果。使用测试组织中配置的字段、用户和组；这并不是说这个例子已经被执行了。
