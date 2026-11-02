# 为 LN 导出配置默认税务国家/地区

### 概述

导出的默认税务国家/地区设置为 **DE（德国）**，以避免导出错误。您可以通过以下任一方式在映射文件中更改此设置：

* 定义其他静态值。
* 将其动态映射到 DocBits 中的字段。

<mark style="color:red;">**注意：**</mark>如果指定字段不存在或为空，导出时将回退为 **DE**。

### 修改税务国家/地区的步骤

#### 1. 获取映射文件

* 前往 **DocBits → 设置 → 文档处理 → 导出**。
* 打开要修改的导出配置。
*   点击 **下载**以获取映射文件。\\

    <figure><img src="../../../../.gitbook/assets/iScreen Shoter - Google Chrome - 250220120028.jpg" alt=""><figcaption></figcaption></figure>
* 在文本编辑器中打开该文件。

#### 2. 修改映射文件

选择以下两个选项之一，并进行相应修改。

**选项 1：静态值**

若要设置静态税务国家/地区值，请按以下步骤操作：

1.  在 `StaticFields` 行中添加 `,TaxCountry`，以定义新的静态字段。

    ```properties
    StaticFields=FinancialCompany...,TaxCountry
    ```
2.  添加以下行以设置国家/地区代码：

    ```properties
    SF_TaxCountry=CountryCode
    ```

    将 `CountryCode` 替换为实际的国家/地区代码，例如西班牙为 `ES`，德国为 `DE`：

    ```properties
    SF_TaxCountry=ES
    ```

**示例：**

```properties
StaticFields=FinancialCompany,TaxCountry
SF_TaxCountry=FR
```

<figure><img src="../../../../.gitbook/assets/image (418).png" alt=""><figcaption></figcaption></figure>

**选项 2：从 DocBits 字段动态映射**

若要从 DocBits 中的字段动态映射税务国家/地区：

1.  在 `HeaderFields` 行中添加 `,TaxCountry`：

    ```properties
    HeaderFields=SupplierCode,...,TaxCountry
    ```
2.  定义对应的字段映射：

    ```properties
    HF_TaxCountry=DocBits_Field_name
    ```

    将 `DocBits_Field_Name` 替换为 DocBits 中的实际字段名称：

    ```properties
    HF_TaxCountry=tax_country_1
    ```

**示例：**

```properties
HeaderFields=SupplierCode,TaxCountry
HF_TaxCountry=tax_country_1
```

<figure><img src="../../../../.gitbook/assets/image (167).png" alt=""><figcaption></figcaption></figure>

### 总结

* 如果**未定义税务国家/地区或字段为空**，则默认使用 **DE**。
* 如果所有导出的税务国家/地区都相同，**请使用静态值**。
* 如果税务国家/地区因文档而异，**请使用动态字段映射**。

按照这些步骤，您即可成功修改税务国家/地区映射，以满足您的需求。
