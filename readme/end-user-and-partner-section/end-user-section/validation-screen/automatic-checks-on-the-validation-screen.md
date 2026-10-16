# 验证屏幕上的自动检查

## 概述

默认情况下，字段验证流程中的特定字段会根据其他提取值计算出的公式，自动检查其值。本页介绍这些自动计算所使用的公式。

将鼠标悬停在信息图标上，即可随时查看所用公式。

<figure><img src="../../../.gitbook/assets/automatic_checks_1 (1).png" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">**注意：**</mark> 只有在相应字段已提取出值时，才会显示信息图标。

## 自动检查公式：

### 净额：

```
Net amount = Tax amount * 100 / Vat rate 
```

### 增值税税率：

```
Vat rate = Tax amount * 100 / Net amount 
```

### 税额：

```
Tax amount = Net amount + Vat rate / 100
```

### 优惠税率净额：

```
Net amount reduced = Reduced Tax amount * 100 / Vat rate reduced
```

### 优惠税率增值税税率：

```
Vat rate reduced = Reduced Tax amount * 100 / Net amount reduced
```

### 减税税额：

```
Tax amount reduced = Reduced Tax amount + Vat rate reduced / 100
```

### 净额合计：

```
Total net amount = Net amount + Reduced Tax amount + Net amount free
```

### 净额合计（美国）：

```
Total net amount US = Net amount + Shipping charges + Misc. charges + Additional amount
```

### 税额合计：

```
Total tax amount = Tax amount + Reduced Tax amount + Tax amount free 
```

### 总金额：

```
Total amount = Net amount + Tax Amount
```

<mark style="color:red;">**注意：**</mark> 如果提取值与验证后的值不匹配，则无法继续处理该文档。相应字段会显示 **Amounts Mismatch**（金额不匹配）错误。
