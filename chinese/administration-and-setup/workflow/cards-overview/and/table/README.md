# 表格

此类别中的卡片会显示在 Workflow Builder 的 **添加卡** 库中：

<figure><img src="../../../../../.gitbook/assets/workflow-card-qa-20261021-category-526dc164847b-zh.png" alt="所选类别中的可用卡片。使用前请填写所需字段。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。"><figcaption><p>所选类别中的可用卡片。使用前请填写所需字段。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。</p></figcaption></figure>

<!-- workflow-card-example-condition_table_column_exists-20261021 -->

### 文档表包含一列

<figure><img src="../../../../../.gitbook/assets/workflow-card-qa-20261021-card-extra-bf66d05be645-zh.png" alt="所示版本的卡片字段。占位字段尚未配置。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。" width="563"><figcaption><p>所示版本的卡片字段。占位字段尚未配置。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。</p></figcaption></figure>

`CONDITION_TABLE_COLUMN_EXISTS`·版本2

选择表 `lines`、列 `article_number` 和存在运算符。包含该列的填充表通过；没有该列的同一个表无法进行存在性比较。不存在或为空的表可能会产生缺失数据的结果，并且不能证明否定比较成功。

<!-- workflow-card-example-condition_compare_table_date_to_current_date-20261021 -->

### 表格中的日期与参考日期

<figure><img src="../../../../../.gitbook/assets/workflow-card-qa-20261021-card-extra-05a199670bd2-zh.png" alt="所示版本的卡片字段。占位字段尚未配置。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。" width="563"><figcaption><p>所示版本的卡片字段。占位字段尚未配置。 此版本界面的部分标签尚未翻译或翻译不准确。本页说明使用正确术语；图片保留了实际界面。</p></figcaption></figure>

`CONDITION_COMPARE_TABLE_DATE_TO_CURRENT_DATE`·版本2

对于参考日期 `2026-10-21`，比较表 `lines`、列 `delivery_date`、晚于、全部和零日容差。日期为 `2026-10-22` 和 `2026-10-23` 的行满足比较。日期为 `2026-10-20` 的行使全部失败。分别测试缺失日期和无效日期。
