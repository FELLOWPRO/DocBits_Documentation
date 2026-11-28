# 以基本计量单位导出数量

**Export quantity in base unit of measure** 开关位于文档类型 **More Settings** 的 **Purchase Order** 部分。它改变 Infor LN 导出为已匹配采购订单行写入的数量和单价。

在 **Settings → Document Types** 中打开它：在文档类型卡片上选择齿轮图标（**More Settings**），然后展开 **Purchase Order**。

## 开关的作用

* **Off:** DocBits 按发票单位导出数量和单价。
* **On:** DocBits 使用每条已匹配采购订单行的换算系数，将其数量和单价换算为该行的基本计量单位，并写入基本单位代码而不是开票单位代码。

没有换算系数的行按原样导出，因此缺少系数不会阻止导出。

{% hint style="info" %}
该换算仅适用于 Infor LN 导出。其他导出目标保留开票单位。
{% endhint %}

## 何时使用

当 Infor LN 实例要求以基本计量单位提供订单数量时，请打开该开关。换算使用采购订单行上存储的系数，而不是 DocBits 根据物料主数据计算的系数。

设置可能影响正在使用的文档。请先用测试文档检查结果，再在生产环境中保存更改。该开关改变导出的值；它不改变发票行与采购订单行的匹配方式。

## 相关页面

* [采购订单](README.md)
* [导出未匹配的采购订单行](export-not-matched-po-lines.md)
* [备用导出](alternate-export.md)

<!-- Documentation review 2026-11-27: switch label, help text and behaviour checked against DocBits_Web src/pages/Settings/Components/DocTypes/PO.vue on origin/sandbox-nova (DOP-53, commit feb262ab89, contained in the deployed NOVA build 11.24.8). -->
