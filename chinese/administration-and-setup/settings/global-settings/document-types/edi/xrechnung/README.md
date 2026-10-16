# XRechnung 概览

## 简介

XRechnung 是一种面向公共行政机构的德国电子发票标准。它基于欧洲标准 EN 16931，包含两种技术格式：**UBL**（通用商业语言）和 **CII**（跨行业发票）。

DocBits 全面支持 XRechnung，可提取结构化数据并将其无缝导出到 Infor ERP 系统。

## 支持的 XRechnung 版本（CII）

DocBits 支持以下 XRechnung CII 版本：

* [XRechnung 1.2](xrechnung-1-2.md)
* [XRechnung 2.1](xrechnung-2-1.md)
* [XRechnung 3.0](xrechnung-3-0.md)
* [XRechnung 3.0.1](xrechnung-3-0-1.md)
* [XRechnung 3.0.2](xrechnung-3-0-2.md)

## 数据流

XRechnung 文档到 ERP 系统的数据流包括以下步骤：

1. **提取**：DocBits 根据 XRechnung 版本和格式（CII 或 UBL）解析 XML 数据。
2. **DocBits 字段映射**：将提取的数据映射到标准 DocBits 字段。
3. **ERP 对齐**：将 DocBits 字段映射到 Infor BOD（业务对象文档）字段，通常使用 `SyncSupplierInvoice` BOD。
4. **导出**：将映射后的数据导出到 Infor 系统。

## 映射标准

映射基于以下标准：

* **UN/CEFACT CII**：XRechnung CII XML 结构的基础。
* **OAGIS/OASIS**：Infor BOD 所采用的标准。
* **EN 16931**：欧洲电子发票标准。
