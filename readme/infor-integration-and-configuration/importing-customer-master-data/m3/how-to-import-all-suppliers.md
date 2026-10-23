# 如何导入所有供应商

* [ ] 登录 Infor OS 环境并进入 M3 应用。建议：请确保您拥有管理员权限，以便运行所有程序。

<figure><img src="../../../.gitbook/assets/6cf93500-2e90-4cfc-a9fb-5873e5dcb953.png" alt="Infor OS中的Infor M3开始菜单，包含程序列表、Favorites和Recent面板以及打开的evs006搜索字段"><figcaption></figcaption></figure>

* [ ] 运行程序 _**evs006**_。按 command + R，您将看到用于搜索和启动程序的打开标签页。

<figure><img src="../../../.gitbook/assets/f77b242e-eb2f-43b6-8a2e-03d264198e0c.png" alt="Infor M3开始菜单，搜索框中显示evs006 Initial Load，可在Recent下方随时打开"><figcaption><p><em><strong>evs006</strong></em></p></figcaption></figure>

* [ ] 打开 _**evs006**_ 后，您会看到一个空表格。请填写 “BOD noun” 和 “Table” 列。“BOD noun” 填写 “SupplierPartyMaster”，“Table” 填写 M3 供应商表 “CIDMAS”。

<figure><img src="../../../.gitbook/assets/827a9dbb-c974-4da7-9bd3-f8e87adad60f.png" alt="Infor M3菜单界面，其中搜索字段已打开，用于启动程序"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/e30c7b86-dcfb-41d2-bd32-447b60e4581b.png" alt="EVS006 Initial Load表格，包含BOD noun、BOD variant、Table和BOD description列"><figcaption></figcaption></figure>

* [ ] 填写这些列后，点击屏幕上方栏中的 CREATE 按钮。随后会进入以下屏幕。

<figure><img src="../../../.gitbook/assets/30eee6b2-24ed-4e1f-8812-1304e7dede8e.png" alt="空的EVS006 Initial Load表格，列标题为BOD noun、BOD variant、Table和BOD description"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/461b72d3-d576-4c92-95c2-d175183088af.png" alt="EVS006 Initial Load面板，包含Table CIDMAS Supplier、BOD noun SupplierPartyMaster以及Details和Table keys部分"><figcaption></figcaption></figure>

* [ ] 在 “BOD Description” 中填写 SupplierPartyMaster。

<figure><img src="../../../.gitbook/assets/4dc345a8-8eca-4e03-800a-37a670f8792e.png" alt="EVS006 Initial Load面板，其中Details下已填写BOD描述SupplierPartyMaster"><figcaption></figcaption></figure>

* [ ] 点击 Next。（位于屏幕左下方）。

<figure><img src="../../../.gitbook/assets/315aa54b-f0bd-4057-a1ed-e476c9000725.png" alt="表CIDMAS的EVS006 Initial Load面板，BOD名词为SupplierPartyMaster，Next按钮位于左下角"><figcaption></figcaption></figure>

* [ ] 在此窗口中点击 Next。

<figure><img src="../../../.gitbook/assets/c0ff3fe1-a393-43cc-96a5-3e0cb1d878b7.png" alt="M3中的Text对话框，包含Text block和Language列，名称为InvExt"><figcaption></figcaption></figure>

* [ ] 现在，您会看到一个已填入 BOD SupplierPartyMaster 的表格。右键点击该 BOD，然后选择 Related > Run。

<figure><img src="../../../.gitbook/assets/d819fdd5-5b4a-48ef-9412-f211c0d2355f.png" alt="EVS006 Initial Load表格，包含SupplierPartyMaster行及其右键上下文菜单，其中有Related、Run和Change"><figcaption></figcaption></figure>

* [ ] 在下一个窗口中选择 “Sync”，然后点击 Next。

<figure><img src="../../../.gitbook/assets/8fbed442-7deb-4c1e-9295-5038fe124331.png" alt="Infor M3中的BOD Processor Administration面板，显示SupplierPartyMaster作业、动词Sync和状态Pending"><figcaption></figcaption></figure>

完成上述所有步骤后，您便已激活用于从 CIDMAS 表导入所有供应商的 BOD。几分钟后，您应该就能在 DocBits 中看到供应商。
