# 测试模型

## 运行分类测试以评估模型准确性和运行就绪情况的步骤

要测试训练好的模型并评估其准确性和运行就绪情况，请按照以下步骤操作：

**准备测试数据：**

* 收集具有代表性的测试数据样本，涵盖模型在实际使用中需要处理的不同文档类型和场景。确保测试数据质量高且标注正确。

**运行分类测试：**

* 使用准备好的测试数据运行分类测试。
* 将测试数据输入模型，并让模型预测文档类别。

<figure><img src="../../../../../.gitbook/assets/image (206).png" alt="DocBits中的Settings导航，Documents条目已展开，可见Ocr Settings和Master Data Lookup" width="375"><figcaption><p>设置</p></figcaption></figure>

* 添加新的分类规则，或编辑现有规则。

<figure><img src="../../../../../.gitbook/assets/image (207).png" alt="Classification And Extraction设置页面，Classification Rules标签页中列出了Invoice和Delivery Note的E-Mail规则"><figcaption><p>设置：分类和提取</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (205).png" alt="配置分类规则的对话框，其中包含Pattern、Type、Sub Organization、Document Type和Sub Document Type字段" width="276"><figcaption><p>配置分类规则</p></figcaption></figure>

**评估模型准确性：**

* 将模型的预测结果与测试数据的实际分类进行比较。计算准确率、精确率、召回率和 F1 分数等指标，以评估模型的性能。这些指标有助于了解模型对文档分类的效果及其可靠性。

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto 2024-05-22 um 08.53.41.png" alt="Classification And Extraction设置页面，AI Models标签页显示No Record Found"><figcaption></figcaption></figure>

**分析错误：**

* 检查模型在测试数据分类过程中出现的错误，并分析原因。识别错误中的模式或趋势，并在必要时调整模型以提升其性能。

**优化模型**：

* 根据分类测试和错误分析的结果，您可以通过添加训练数据、调整训练参数或更改模型架构来优化模型。重复测试流程，检查优化是否提升了模型性能。

**记录结果：**

* 记录分类测试的结果，以及对模型所做的任何调整或优化。这有助于跟踪模型随时间的进展，并确保其持续改进。

定期运行分类测试并评估模型性能，可以确保模型适用于生产环境并提供准确结果。
