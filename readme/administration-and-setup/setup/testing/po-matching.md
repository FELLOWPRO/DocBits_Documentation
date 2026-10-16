# PO 匹配

测试 PO 匹配配置时，需要在 LN/M3 中创建一张采购订单，以检查 INFOR 是否已与 DocBits 同步。

## 在 INFOR 中创建采购订单

* LN: https://docs.infor.com/ln/10.4/en-us/lnolh/docs/ln\_10.4\_procpoug\_\_en-us.pdf
* M3: https://docs.infor.com/m3udi/16.x/en-us/m3beud/default.html?helpcontent=ois610.html

创建采购订单后，前往 Settings → Master Data Lookup，搜索刚创建的采购订单编号。此时，该订单应已显示在 DocBits 的采购订单主数据中。

<figure><img src="../../../.gitbook/assets/dbdc206-purchase-order-bod-input-en.png" alt="主数据查找页面，显示已导入采购订单的 Purchase Order 表格。"><figcaption><p>采购订单显示在主数据查找中。</p></figcaption></figure>

您应能在此处看到唯一的 PO 编号，这表示 DocBits 与 INFOR 已正确同步。

现在上传一张发票，其数量和单价与您创建的采购订单相符。验证文档，并在验证界面选择 PO Matching。

PO 和发票的行项目应自动匹配。然后选择导出选项，并检查文档能否无误导出。如果遇到导出错误，请创建工单联系 DocBits 支持团队寻求帮助。如果您不确定如何在 DocBits 中创建工单，请参阅 DocBits Overview 文档以获取帮助。

\\
