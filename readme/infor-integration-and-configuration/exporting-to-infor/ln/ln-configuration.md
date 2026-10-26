# LN 配置

## 先决条件

您已创建：

* ION API 端点
* ION API 文件
* BOD 映射文件
* IDM 映射文件

## 导入映射文件

设置数据流之前，需要将映射文件导入 InforOS。

在 ION Desk → Connect 中，打开 Mappings。

![ION Desk 导航，Connect 分组已展开，列出 Data Flows、API Flows、Connection Points、File Templates 和 Enterprise Locations 条目](https://lh7-us.googleusercontent.com/fAUUcBUSxIWqLjYEHH78O2Mfq0P4d4D42OgCNFPdpUQTM5ZHu\_BcKz9DmWe0AlHe3--ff7z9mfYTrt7oAkf2uknBwkV2VWayEpiJ\_aAIxcJil5LNiep4U6KZr3\_tBfs1RRwXoW749q3FUxurXy\_pT\_k)

点击 Import 图标。

![ION Desk 中 Mappings 页面的工具栏，显示绿色的圆形导入图标](https://lh7-us.googleusercontent.com/d\_KYA9LgiiW1A95CH9hwU1AC1u5x25T4ET-4sAqpZkVOexHc4WcbwPXUaKt3O9fR3Btvv-NEGbCWwnnb8SfomnnO22M8YTIqWdvan-SkbG0cu1MWkjwOn\_Vd\_b6rJaQng8A92JTa5YKBms4RuIvwmb0)

* 在这里选择所需的映射文件，包括：SyncCaptDoc\_SyncSuppInv、SyncSupplierInvoice\_LoadSupplierInvoice 和 LoadSupplierInvoice\_ProcessSupplierInvoice。
* 导入所有映射文件后，请在 Mappings 仪表板中点击每个映射方框内的勾选图标，逐一批准这些映射。

## DocBits 到 LN

下一步是在 ION Desk 中设置数据流。进入 ION Desk 应用，选择 Data Flow → + ADD → Document Flow，如下所示。

![ION Desk 中的 Data Flows 页面，左侧为导航，列表中显示流程 DF_SLTStAPI，菜单中显示 Document Flow 和 Data Lake Flow 条目](https://lh7-us.googleusercontent.com/rjPVR1EFKw\_gZI1Ztg9Aqt4pFw10rii7WU-yddLIz22a\_Fn3s1HSYDRmQVvgZtX\_85nb2ipNqJ1JU49NIE8a57TIur7jqoMuKFKlb-RrfnRFxiA1TefzofKPJ32fzIdDWI8PmnD-aDw4qhQj4e0dd9I)

随后会看到此页面，您可以在此构建从 DocBits 到 M3 的信息流。

![新建的 Document Flow，属性面板为空，并显示 Document flow name must be specified 和 The document flow has no activities 两条提示](https://lh7-us.googleusercontent.com/9C7BaoiHWRaav0ytCbYkxEYG12f-64qyagsl8H2eq5TXUySRE1s3x\_-lVRbK6tpTxvbRYKvwyWO\_6ASSQ6Rn62LQR9ZvMRpRXq9UymZLS0I8IZ-hOzX58iYtTruqSo5WdgIXwEPjMlb1dnuFuhN8IS8)

LN 数据流的样式应与下图相似（由于每条路径都对应一种特定的文档类型，因此包含多条路径。本说明将重点介绍发票数据流）。

![数据流画布上有多条针对不同文档类型的路径，每条路径由 DocBits 连接点、一个映射和 LN 连接点组成](https://lh7-us.googleusercontent.com/gltDE9JxeGb7Ufg9Ldl-JIJ95zfWHnQtyOqys2QKCiTlIn\_PdAyBLFYmTVCh9c-TxF5xNQR3G8Hmn4EXK94t6MJ-1WzlZg1Zl7HNoxfR56zC8dT1skmxLTj7rtnSl0JTQJD\_3myQY4Qcd9motySYh9U)

链中的所有部分都从顶部区域拖放到画布上。

在这条链中，DocBits 和 LN 都是应用程序；它们之间的节点是映射，用于将数据转换为下一个节点能够理解的格式，并将信息“映射”到所需或指定的位置。

![数据流画布局部，显示 DocBits-DEV、MappingDeliver、Load Supplier、PurchaseOrder 节点以及 LN-200-41 和 LN-200-4 连接点](https://lh7-us.googleusercontent.com/Gwk0C0gsnMSlgEwRx0\_1GDMJEu8Z1TAhKo8gxHN8GxFFKGgb257a684Hj0eNSLTIK5v8F7yzJ1hIHrC\_3I9RLY0S-u3ZDhmkD6iJbYAvtCAeFPWHBVLOqyCH7FKsl2SKAfXL-AdtNowqdol9PzS4qJM)

### DocBits 应用程序

为其指定合适的名称，例如“DocBits”，然后选择加号并搜索之前创建的连接点，例如 DocBits\_Export 或类似名称，再点击该连接点。

要创建此连接点，请前往 ION Desk → Connect → Connection Points。

![ION Desk 导航，Connect 分组已展开，列出 Data Flows、API Flows、Mappings 和 Connection Points 条目](https://lh7-us.googleusercontent.com/1SZJN-GW7BP-fvUHZ-tCJ4xNXx0ABRP3J9eMzF3BTKIY54J-pK4bYy4fOVHCaI6A2sdrYekWJsY9ky8dXz36l\_FwwzzEnO1IjxNkMqlV-Y4UvyFIei73Z9C19m9bzTr3gCL3IpTUqiV280id1vJE530)

点击“+ Add”。

![ION Desk 中的 Connection Points 页面，导航中的 Connect 分组处于展开状态](https://lh7-us.googleusercontent.com/ZJ1212Gwdk-b2-LVbEd2ZDzc\_AqaEEYtIN0fC6d6P4EaWdTKj6nOzGDbA5sxdBtMcTrWopfDmd7GTahbwkDpj3uvmMYgvEUQa6qmi58NFGvtcgAtIwYr952Yu7Lcj802iHtQ\_vj\_-XPdegP1P0ySdos)

选择“IMS via API Gateway”，并填写以下信息。

![IMS via API Gateway 的 Infor Application Connection Point 对话框，包含名称 DocBits-Sandbox-Export、ION API Client Id 和 Logical ID infor.ims.docbits-sandbox-export](https://lh7-us.googleusercontent.com/H4YCH-324EzrxKkrbRs0SFTsHch5eK74gXleSpfI03uJ5frIEFjwofu7p6bsYO1lS7sVqamWDZMXrGfEgewdROyhTYLkn7MuCgwb7oQxOLJoH3NsnMsqTOgT3WxlihUkJdNy-WTai5kPz8ZjdtTDQ9I)

ION API Client ID 位于您在“如何创建 ION API 文件”中创建的 ION API 文件内，对应“ci”值。

切换到 document 标签页，并将 Sync.CaptureDocument BOD 添加到 DocBits 连接点，如下所示。

![连接点 DocBits-Sandbox-Export，Documents 选项卡已打开，并已分配文档 Sync.CaptureDocument](https://lh7-us.googleusercontent.com/Wy2BIr1z\_RqU-yMkXo6vOu64QC6c66OdHOxdI6PPy0yJv1jIAJF0OYITULxTFoPUK93SK3jvNm67tcxqjiEBIk0Wbu1Q1s-mSIUuPjJorcYyXY7vjsHOnoutn6tE8r6yE\_333uCWuKvKiVoo99FrXVg)

然后点击左上角的磁盘图标，保存连接点。

返回 ION Desk 的 Dataflow 部分，打开您的数据流。DocBits 应用程序应与下图相似。

![DocBits 应用程序的 Application Activity Properties 面板，名称为 DocBits-Sandbox-Export，描述为 DocBits-Sandbox-Export](https://lh7-us.googleusercontent.com/cDWHmRP85YNLu7JRzq4CSezncTgP2ZOkEfZSqXK9JEq4bSwsddU7VKg8leoxaJ5zeFAbDzXrNkztmeWDIXbHwjxfUa\_IpATDDwykv-OlZ2zaOVGHVqRZZpVLJ5Cq5Qla1pZk5sBV39I98lUfGao65Mw)

### 映射 1

第一个映射节点应如下所示。

![第一个映射节点的 Mapping Properties 面板，包含 Name 和 Description 字段以及 Mapping 下拉列表](https://lh7-us.googleusercontent.com/9tlIun\_ipbTp15aMX3xN2DGlDjAZ1oI4AFWXwbP7yoFLeQNqcw\_L3Z1djaqcbxP1tsp1R-nq6ZJqEzsoKe1-SmLrJNmYrJ4HJircLEwMxfmif-p2T8nqbuuxHLLLzQJ6E6tNG6MzghOpoEAt41ea2GY)

### 映射 2

第二个映射节点应如下所示。

![第二个映射节点的 Mapping Properties 面板，包含 Name 和 Description 字段以及 Mapping 下拉列表](https://lh7-us.googleusercontent.com/ZDYzTAfm3MHnEIKHa2tDl7NPbjzxv8jH-KL8O0pRhi1JYtqiiVz0-GQv5N4roVWi1STopQkFV9YHbEXdyzwYxK2Oq6mUv6tuqKDp-2bc-aPVgEXdEBd2hmW-6j6JRhEympyw9yUTrCDQRKlDQ41C5Ao)

### LN 应用程序

Infor 中应该已为相应的 LN 公司创建了 LN 或类似名称的连接点。因此，与 DocBits 应用程序的操作相同，点击“+”号并选择该连接点，显示应如下所示。

![LN 应用程序的 Application Activity Properties 面板，名称为 LN-200，描述为 In01_0200 LN Farm](https://lh7-us.googleusercontent.com/mRXL11f68EtQHHjl40QmCisy7S1aUezqCzufPTZWgYHhWLK2Yw0UY82O\_dgbAhBChFHHYUMBDSWWb-PEKyohJWOp5gvufat431ezpA2cIHMtry7XEDxhnNzPB68uSMkFAXhX1x4GyiH6Cxp-USxDnHE)

### BOD

![数据流画布，显示 DocBits-DEV、MappingDeliver、Load Supplier、PurchaseOrder、SalesOrder 和 AdvancedShip 节点，下方为 End 条目](https://lh7-us.googleusercontent.com/de8OyDF4yMoHaXsxM9weJdm8mKDzL97kFRr00fhoHAxxKXb2BgMcMM2shyxi1S7cBwzSAUy2u8bZV4sJOVqgXt8Mcge6L2CXxbfVGiqXUwKwF6A5mgt4zfGPYltaZuLazOJYu2u7arszJE6IonMOskk)

以下配置应如下所示：

#### 第一项

![第一个节点的 Documents 下拉列表，显示 Sync.CaptureDocument 条目](https://lh7-us.googleusercontent.com/rj\_qpiML1a2dNxj6ItiRxescymVtD6LHIAum3UPrPERAavhkt81lpjcyAFmn\_lmxtqUDVTm\_kiZ9f02Lqh9w-SAWmcxvGuxWITVvhv9qg04HaJXGH7VfRiO4Iv1LtDxfKYFyUWPLzCE4L3yP4hcdGnY)

#### 第二项

![第二个节点的 Documents 下拉列表，显示 Load.SupplierInvoice 条目](https://lh7-us.googleusercontent.com/TCxMS-RhoJcUyBko36Lfpa8D71qk-ZSN-lME7Oq8cfPACVV0Ci7Lnv6y\_MF\_53U763ZA74xq6icEfgDUwYYJ9UJK0kCiLHQZpJYmc\_ywjB32UGrpDnh7AjoHpI5AtWd3yZR3RsMaki1AYenpdG4X9X8)

#### 第三项

![第三个节点的 Documents 下拉列表，显示 Process.SupplierInvoice 条目](https://lh7-us.googleusercontent.com/VPYJyfpO0RZueW46s2Y8W2H-tQFlMfIdP1Sf8qMB8BfTxefgQ5dhsaAxL36R7cdvmKR26Q\_epAj9\_i6CzUO6C-PHjStEynBDkjtwId4BSuH6-zJklmsr25XcNH2AY7pSwOQ\_rbCCixhWcaJg2kHyyYw)

最后一个图标应为空，因为它不承载任何文档或信息。

将所有必要节点添加到数据流后，点击此按钮以激活数据流。

![Document Flow 工具栏，包含添加和移除连接点的按钮以及激活数据流的按钮，上方名称为 DocBits-Export-M3](https://lh7-us.googleusercontent.com/WjQeGz\_effl\_RlkWC4CdJS9Dg\_9DpsIz3meKOsa7GbU9RFSrYMw3PpbXFat6cGsA4gvEGS-0D-YFrZj9K2wK3Irap-30mcQ5kr5k4Gy2gm7DLJdYpzJgeBRVInyAYfGmGXu2dCQvmX9ballRbSwyq3o)
