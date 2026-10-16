# 创建和编辑脚本

{% embed url="https://youtu.be/n8NpWWIjmlA" %}
DocBits 文档脚本说明：自动化文档工作流中的自定义逻辑
{% endembed %}

## 按照以下详细说明在 DocBits 中创建新脚本：

**选择脚本语言：**

首先，选择要使用的脚本语言。DocBits 通常支持 Python、JavaScript 或 SQL 等常用脚本语言。语言的选择取决于项目需求和您自身的熟练程度。

**打开脚本开发环境：**

登录 DocBits 并导航到脚本开发环境。该环境位于管理区域。

<figure><img src="../../../../../.gitbook/assets/script_development_environment_overview.png" alt="脚本开发环境概览"><figcaption></figcaption></figure>

**创建新脚本：**

点击“+ New”按钮，打开新的脚本编辑器。

<figure><img src="../../../../../.gitbook/assets/create_new_script_button.png" alt="创建新脚本按钮"><figcaption></figcaption></figure>

**编写代码：**

使用编辑器编写脚本代码。请从所选脚本语言的基本语法开始。

例如，如果使用 Python，脚本可能如下所示：

## 1. Python 脚本示例

<figure><img src="../../../../../.gitbook/assets/python_script_example_1.png" alt="Python 脚本示例 1"><figcaption></figcaption></figure>

## 清理患者姓名的函数

def clean\_patient\_name(name): cleaned\_name = name.strip().title() # 删除空格并应用首字母大写

return cleaned\_name

## 主程序

if **name** == "**main**": patient\_name = " john doe " cleaned\_name = clean\_patient\_name(patient\_name) print("清理后的患者姓名：", cleaned\_name)

## 2. 脚本示例

<figure><img src="../../../../../.gitbook/assets/python_script_example_2.png" alt="Python 脚本示例 2"><figcaption></figcaption></figure>

**测试脚本：**

检查代码是否存在错误，并在测试环境中进行测试。确保脚本能产生预期结果并正常运行。

<figure><img src="../../../../../.gitbook/assets/script_testing_interface.png" alt="脚本测试界面"><figcaption></figcaption></figure>

**保存脚本：**

在 DocBits 中保存脚本，并为其指定一个能描述脚本用途的名称。

<figure><img src="../../../../../.gitbook/assets/save_script_button.png" alt="保存脚本按钮" width="84"><figcaption></figcaption></figure>

**将脚本映射到文档类型：**

重要的一步是将脚本映射到相应的文档类型。这决定了脚本何时以及如何应用。通常可以通过 DocBits 中的配置界面完成此操作：将脚本分配给特定文档类型，并指定应用脚本的条件。

<figure><img src="../../../../../.gitbook/assets/script_document_type_mapping.png" alt="脚本与文档类型的映射"><figcaption></figcaption></figure>

**审核并发布：**

创建、测试并映射脚本后，再次检查是否存在错误或不一致之处。如果一切正常，就可以将脚本发布到 DocBits 生产环境。

<figure><img src="../../../../../.gitbook/assets/script_review_and_publish.png" alt="审核并发布脚本"><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/script_publish_confirmation.png" alt="脚本发布确认"><figcaption></figcaption></figure>

按照这些步骤，您可以在 DocBits 中成功创建、测试并实施新脚本，从而实现流程自动化并提高医疗文档处理的效率。
