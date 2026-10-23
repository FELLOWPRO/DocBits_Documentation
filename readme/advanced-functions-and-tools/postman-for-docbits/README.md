# DocBits 的 Postman 使用指南

本指南将介绍如何通过 Postman 向您的 DocBits 组织发送 HTTP 请求。Postman 易于使用，对组织管理员也非常实用。

## 设置

首先，将 Postman 下载到您的系统中，然后登录或注册。

现在，按照以下分步指南了解如何在 Postman 中发送 HTTP 请求。

Postman 中的授权

在创建 HTTP 请求之前，您需要输入 DocBits 的 API 密钥进行授权。

* 点击 `Authorization` 选项卡，并选择 `API Key` 作为授权类型。

![Postman请求标签页，选中Authorization标签，Auth Type列表展开，显示API Key以及Bearer Token、Basic Auth和OAuth 2.0](https://lh7-us.googleusercontent.com/L3GaBZJvReeINaKbkq3VYQ9UHTBoKUA3nJkfyLqk61q5xaOJnmMLhbrEbgUgLEyYRkewHuLIAVzoYCZ6quHq0pwx\_69FEYJjzYllivB8WzdAtTFSrzl8VeFthbMsEB9sGjcGlVN38DXEXUwuNEPL6hg)

* 填写相应的值。在 `Key` 字段中输入“X-API-key”，并将您的 API 密钥作为值输入（可在 DocBits 的“设置”菜单中的“集成”下找到）。选择将其添加到 `Header`。

&#x20;

* 界面应如下所示：

![Postman的Authorization标签页，Type设置为API Key，Key字段设置为X-API-key，下拉菜单中选择Add to Header](https://lh7-us.googleusercontent.com/SmNfci4z8ECTeXzFPE9YQ8nCzCRHglc\_7RR1cN8a8F7KvYWjJcBnY5wpl7q0AV8bfNLkMk8F4F4aw8j4xMK50HJweBRBPo8EasTn-FG-fmlUJQ41aUX-dvTeWP\_xJQThi8A6EwJl3qIc-Dw1B5W9fVE)

### DocBits API

可通过 https://api.polydocs.io 访问

* 点击右上角的 Authorize

![DocBits API的Swagger页面，右上角突出显示Authorize按钮](https://lh7-us.googleusercontent.com/kuztHpkmRWlOYSU27r97KH15SJHPF\_hn\_eX3C1DYLVYCwMHXfLjYSyFubUCvlQiBt5q3xY0XBPmkcP6AnKF2C0Mdtx3tg\_dU\_qxqAmI6axYIsXR36\_YBz6j455K3-c2SBu4YzmYIXq8VXQxzgL-0j90)

* 输入您的 API 密钥，然后点击 `Authorize` 确认

![Available authorizations对话框，包含APIKeyHeader (apiKey)方案、Name为X-API-KEY、In header以及空的Value字段](https://lh7-us.googleusercontent.com/zLhgpdjMnxqNBdjgtDxFEKglICIZul7dgmfFFm2hSnsDQ-HsZHRKRikZ0lcanGYkkZj4waC85mEUFO951ydVnY\_\_m\_TrMrsK3vrDv9FKL-adgWL4lJqp3cSxPeClBm9IHG2cXinRsv12xTeh3psQfO4)

### 在 Postman 中创建新工作区

* 点击 Workspaces 并创建新工作区（名称可任意设置）

![Postman主屏幕，打开的Workspaces菜单列出My Workspace、More workspaces和View all workspaces链接](https://lh7-us.googleusercontent.com/3rZw7jhOgVpkZuer58fPEKqDspJjK3S1lp3XpQuvE4c9212a0ALB-p7oLRwPqEbj10MpoCWsb7V9fPqiAdVvigE00x9mN5-lHFXZVVxlkeroBJd2ratgkJVJDM4LJkUJsycyl6tnFKazcFPY-vWtH2Q)

* 您需要选择可见性，以确定哪些人可以访问此工作区。

![Create workspace对话框，包含Name和Summary字段、Personal、Private、Team、Partner和Public可见性选项，以及Create Workspace和Cancel按钮](https://lh7-us.googleusercontent.com/ZajvDtMvfM5J\_Go3n\_PgzD3RXTMQAlST8\_3WnsTQ4-iw7e0QdAa3wqFk7Y0gt78IJVjNTN-5E72c1127CpXJWb8WbfDolxENLqxg5VZLPEK7-hxsNwbAyMceSHfeVy6v-b9QT0kFwnMibWndEAJ2lXA)

* 选择完成并点击 `Create Workspace` 后，在应用左侧选择 Collections，然后点击 `+` 为 HTTP 请求创建一个新集合。

![Postman侧边栏，Collections选项卡处于激活状态，显示New Collection，并弹出带加号按钮的Create new collection窗口](https://lh7-us.googleusercontent.com/mbC5t86vaB2G7FQp-40XN-SHc019LKitfUeXRzbcG4HpNai5FPapShx9swHX3mz0va8QFsUQiYn-bhjvER0XYOEDRJpI9x3wG4NgRZCd4beU1NyKJd86bSGubxVbRCtz8HkTDZd28Z7Ice3rmscFMMo)

在此集合中，您可以添加多个 HTTP 请求。操作方法是点击集合旁边的三个点，然后选择 `Add request`。

![Postman集合菜单已打开，包含Share、Move、Run collection、Edit、Add request、Add folder和Monitor collection操作](https://lh7-us.googleusercontent.com/S5W75clJz7JqoIWPbKBjrJqpTAwjS51Pu4dTU160Q7i6oW-HPnb7aN8WRK2AyAb6-HEqTYMZTy9563P0sq53MAjGpVg1JivZX2ATHa6GeFbTX2UCjud7ot8Y\_ksBuUbUfyEfxIDziV8TN3zDfX9Se58)

## “GET” 方法示例

GET 方法非常实用，可用于获取用户、子组织、已处理文档等信息。

* 在 HTTP 请求中选择 GET 方法。
* 按照上述说明进行授权。
* 打开 https://api.polydocs.io，并在 Polydocs URL 后添加相应功能的路径。例如：

![GET /orgs/get_users端点的Swagger页面，列出DocBits API的用户路由](https://lh7-us.googleusercontent.com/pIdgyqP7g1UwZbY5yaz1KAnKe\_ESs\_kQyiWAXXM-ukRKakS\_\_OL\_LS9J-07hZnZDf8QqtoN\_lKyuhvOIIIF-4Wp0dkofZYQwXZ0hu2RM0YogRxJah-zf8W\_cDNFf8xsec1tYIsfe0SpBuvdCG4WHMU0)

* 现在，将此链接粘贴到 Postman 中 GET 方法旁边的文本框内。

点击 `Send`，您应该会收到组织中每位用户的所有信息。

## “POST” 方法示例

POST 方法通常用于创建用户或组织等对象。此方法会将信息写入数据库。

创建用户

* 选择 POST 方法。
* 按照上述说明进行授权
* 打开 https://api.polydocs.io，并在 Polydocs URL 后添加相应功能的路径。本例中：

![POST create user请求体的Swagger页面，显示必填字段first_name、last_name、email、password和is_admin](https://lh7-us.googleusercontent.com/Gwabl4pN0k0NanHsFOzJj9s2H7ExS-JcWr-Y4EW0FLUYHfnaOZoMWvldJ6yDI33p\_DThVx0Rd5bi59XdOK11l1knc5rd-E5HXMw6v5E3qvHvKVWHlp21S728SVye6KU2W5ZeXtCIOzxBAcMlA2UNFfQ)

* 现在，将此链接粘贴到 Postman 中 POST 方法旁边的文本框内。
* 在 HTTP 请求中选择 `Body` 选项卡，并为名称旁带有红色星号的每项凭据输入键和值。

完成后，界面应如下所示：

![Postman的Body选项卡，选中form-data，包含firstname、lastname、email、password和is_admin的键值行](https://lh7-us.googleusercontent.com/lSExzZSbTcSRvuLDw0HNYE62yI7xs0eUewKuOcABCGYfsRBRbGz1lJxopR4QdUEoniCnZ83FKpz-AHLORP5cXGPrPhgouzE6zO920jA7A3r-Y14wY\_Gc3C98R2fcxXsWRMcle9qT981YWhCnjlUukPE)

如果要创建管理员账户，请将 `is_admin` 值设为 true。

&#x20;最后，点击 `Send`，即可在下方的响应中查看您设置的所有凭据。这表示用户已创建。

### 上传文档

您也可以使用 POST 方法将文档上传到 DocBits。

* 选择 POST 方法。
* 按照上述说明进行授权。
* 打开 https://api.polydocs.io，并在 Polydocs URL 后添加相应功能的路径。&#x20;

本例中：

![POST /document/process端点的Swagger页面，列出source、priority和sub_org_id等参数，并带有Send empty value复选框](https://lh7-us.googleusercontent.com/-EwhMeH\_WXYVmMKus1-IZKLZNyTcYktcf\_YUT\_m2nfStfKXuBxKBb1MZfUIQCN4ZxNKQkNhvO\_pgnt1EUhNB34qG5AOe4wM0OxGRMQsV9a8h0XUgabqq8mLQhza\_AE7gxBetmb9bJmaWBQqEXrWT0VI)

* 现在，将此链接粘贴到 Postman 中 POST 方法旁边的文本框内。
* 在 HTTP 请求中选择 `Body` 选项卡，然后选择 `form-data`

![向/document/process端点发送的Postman请求，其中Body标签页处于打开状态，选中form-data，并有一个空的文件键行](https://lh7-us.googleusercontent.com/TNrKlyorn\_5YrIu5r4vcfyYgAnfhsl-SRVqWg9RoN0X1pUjXtn6J0EI7aeQ-oc2ZtFeTj8POcMXy6CwXzI1jhv-ufb2u7d80SC-lbGXmnx\_jVDunAbRw1jqAsB4PPsEzcFIOPeH5PJZvytUW2kIDYZ4)

![向https://api.polydocs.io/document/process发送的Postman请求，选中form-data，键file设置为值Mango-invoice.pdf](https://lh7-us.googleusercontent.com/scAJpTSCqYSKYNNGPIrEsL0zDJIa7Dhe9tpqv\_zDjdLyAydugzdGA1s93njbFOOVbVbQf7oDEtRc14Kt4p1TXX8A--WjvRgeXWsAxDNWdrCN2-QDeya6-FFEG4\_-dhYgrj4yrVYllJs8eZsUgKOPvzo)

在 `KEY` 字段中输入 file，即可看到隐藏的 File 下拉菜单。选择 `File`，然后转到 `VALUE` 字段，点击 `Select Files` 选择文件。

点击 `Send` 后，您应该会在响应中看到 “success”: true。

界面应如下所示：

![已上传文档的Postman响应，状态为200 OK，JSON正文显示success为true、一个doc_id以及文件名Mango_invoice.pdf](https://lh7-us.googleusercontent.com/hNtG\_uTWgxww7iOmHLhnDqdrTlHCI1rk31LozG4l2DLPqxzSn9HoKn8CQIjeBgJLV4bxrGCjWOMRykJ3qBdZLYwxrZJGq\_S3tjVwSZmGTiMgVoqM97TTQjmW8CegEL2FV309NBmV0Fv\_vciSdQRFiOI)

## “DELETE” 方法示例

DELETE 方法用于删除用户、组织等对象。

* 选择 DELETE 方法
* 按照上述说明进行授权。
* 打开 https://api.polydocs.io，并在 Polydocs URL 后添加相应功能的路径。

&#x20;例如：

![DocBits API的DELETE /users/delete/{user_id}端点的Swagger页面](https://lh7-us.googleusercontent.com/-QqSVIELl1IkxYK\_gGDa7nIv\_B1IvO3OjT3Ge6bAXwPl6jVDETuzXwtYJdRSmqLEP2d6B0L6MuwZvgJpI968pzp1APmJmuQ\_qlqYgZZhesocYCJVMCHhIZAKmlvMybUkUGXYZtySrnEbRTwWTritvKo)

* 现在，将此链接粘贴到 Postman 中 DELETE 方法旁边的文本框内。
* 将 URL 末尾的 {user\_id} 替换为要删除的实际用户 ID。（您可以使用 GET 方法获取 user\_id）。
* 如果已在 URL 中加入 user\_id，就不需要再为它添加正文键和值。
* 点击 `Send` 后，您应该会在响应中看到 “success”: true。

&#x20;界面应如下所示：

![Postman的Delete User请求，发送DELETE调用后响应面板中显示Status 200 OK](https://lh7-us.googleusercontent.com/X8WNtsC9v7jqDIiaVhauJUgZK0yTC1GVz9rBptdiCxyLUiEEfbpIoYHpK7NvlDMTkhgiPyBb22H9GOfDdvmL-dakouTjuRDPwX4YX0Jz5IIo6eHu-wnw1S4jJd5ylHyffUXWKwX6ovDnp\_2WEAtSha4)

## “PUT” 方法示例

PUT 方法主要用于更新用户或组织数据。它非常容易理解和使用。

* 选择 PUT 方法。
* 按照上述说明进行授权。
* 打开 https://api.polydocs.io，并在 Polydocs URL 后添加相应功能的路径。

&#x20;例如：

![PUT /users/update/{user_id}端点的Swagger页面，包含Update User请求正文字段first_name、last_name和email](https://lh7-us.googleusercontent.com/tC3qtPbFb1GsK6dBmB5Jrv5HqFOYLxNR1XB0PEuA8ipkHnH2ZQ6xrrkImNgbGSMoA6aAGvLr6K3cI4u\_qM96BOvR7AnQzmX17HBMBneNpLBc6RIzspfTYgrCWSj0fSE9mSWLIex3hc\_R-m-PI6zT6Rs)

* 现在，将此链接粘贴到 Postman 中 PUT 方法旁边的文本框内。
* 将 URL 末尾的 {user\_id} 替换为要删除的实际用户 ID。（您可以使用 GET 方法获取 user\_id）。

## 更改用户的电子邮件地址

* 在正文中，将“email”作为键输入，并将新的电子邮件地址作为值输入。
* 然后点击 `Send`，您应该会在响应中看到 “success”。
