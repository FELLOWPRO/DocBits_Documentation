# 成本要素表格提取

前往 **Settings → Document Processing → Classification and Extraction**

<figure><img src="../../../.gitbook/assets/image (430).png" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">**注意：**</mark> 要启用 **Costing Elements** 的表格提取，必须先将相关的 Costing Element 表导入 **DocBits**。如果未进行此配置，用户打开文档时会遇到以下错误：

_**“成本要素配置不正确。请联系管理员进行配置。”**_

## 从 M3 导入 Costing Elements 的步骤

1. **在 M3 中打开 PPS280：**
   * 在 M3 主页中，按 `Command + R` 并搜索 **PPS280**。
   * 选择结果中的任意一行或所有行。
2. **导出数据：**
   * 在下一个菜单中，点击 **TOOLS → Export to Excel**。\\

       <figure><img src="../../../.gitbook/assets/image (431).png" alt=""><figcaption></figcaption></figure>
   * 选择 **Export All Rows**，然后点击 **EXPORT**。

       <figure><img src="../../../.gitbook/assets/image (432).png" alt=""><figcaption></figcaption></figure>
3. **修改 Excel 文件：**\
   打开下载的 Excel 文件，并进行以下修改：
   * **重命名列：**
     * A 列 → `costing_element`
     * B 列 → `description`
     * H 列 → `charge_operator`
     * J 列 → `charge_type`
     * K 列 → `distribution_method`
     * L 列 → `distribution_type`
     * N 列 → `charge_sequence_number`。
       * 输入相应的序号。
       * 如果留空，系统默认使用 **10**。
   * **删除上方未列出的所有其他列**，无论这些列**是否包含数据或非空**。
4. **修改前后示例：**\
   以下示例展示了应用所需修改前后的 Excel 文件：
   * **修改前：**

       <figure><img src="../../../.gitbook/assets/image (106).png" alt=""><figcaption></figcaption></figure>
   * **修改后：**

       <figure><img src="../../../.gitbook/assets/image (107).png" alt=""><figcaption></figcaption></figure>
5. **转换为 CSV：**
   * 将修改后的 Excel 文件另存为 `.csv`
6. **上传到 DocBits：**

* 前往 **Settings → Document Processing → Master Data Lookup**
* 点击 imported 旁边的加号

    <figure><img src="../../../.gitbook/assets/image (433).png" alt=""><figcaption></figcaption></figure>
* 填写所需信息
  * **Data Type**：`costing_element`
  * **File**：选择修改后的 `.csv` 文件
  * **Delimiter**：`comma`
  * **On Conflict**：选择冲突解决策略
  * **Auto-generate ID**：确保已**勾选**此选项\\

      <figure><img src="../../../.gitbook/assets/image (434).png" alt=""><figcaption></figcaption></figure>
