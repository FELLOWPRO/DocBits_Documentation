# 故障排查

如果验证屏幕上缺少某个值，请先检查文档中是否能看到相应文本，以及 DocBits 是否识别了该文本。这有助于判断问题出在读取过程，还是字段或规则设置。

1. 在 **Validation（验证）** 中打开受影响的文档。
2. 将原始文档与 **OCR view（OCR 视图）** 进行比较。检查相同的页面，以及值应该出现的相同区域。
3. 如果 OCR 视图中缺少该文本，请参阅 [OCR 提取中缺少文本](missing-text-in-ocr-extraction.md)。
4. 如果 OCR 视图中存在该文本，但字段仍为空，请让管理员检查该文档类型的字段设置。请提供文档类型、字段名称、页面以及一个安全的测试示例。

<figure><img src="../../../../.gitbook/assets/dbdc238-validation-ocr-en.png" alt="Validation 中合成发票的英文 OCR 视图"><figcaption>当前 Sandbox Test A 合成发票的英文 OCR 视图。此示例仅供参考，并不表示提取失败。</figcaption></figure>

请勿在支持截图中包含客户文档或个人数据。如果您刚开始使用此屏幕，[验证屏幕概览](../README.md)介绍了主要控件。
