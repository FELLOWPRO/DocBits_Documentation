# 布局构建器

{% embed url="https://youtu.be/-m45XGiIeig" %}
DocBits 布局构建器教程：创建自定义文档布局，让验证更快、更清晰
{% endembed %}

## **访问布局构建器**

首先，请确保已启用布局构建器功能。前往 Settings → Document Processing → Module → Document Type，并确认 Layout Builder 滑块已设置为启用，如下图所示。

![文档类型设置面板，包含Layout Builder滑块和已展开的Models & Labels部分](https://lh7-us.googleusercontent.com/I0VvFiFftKLoCB47jCAoosfTyqIQgXBoggMFp1QAeIj9xW4yiiIzyk5eIEHZ7duA251Yc4_ArUKA8e-LjDht13bckAnkAOHOvl1p5k1-Qj_UkEp2cSZwxHz_PXe8IQ4_jglzCtjAJg5pd9m_hNZEhXA)

### 编辑布局

完成上述操作后，您可以通过 Settings → Document Types 访问布局构建器。在此页面上，您可以从已创建的各类文档类型中进行选择，然后点击“**Edit** **Layout**”，如下图所示。

![文档类型选项卡栏，包含Edit layout、Document Sub Types、Table columns、Fields、Model Training、Regex和Scripts选项卡](https://lh7-us.googleusercontent.com/WMD8M0qugnc64ZuyLuEYH5P63qk-Vo86useg32-QyOsP63FJA_Xh7UzwlwmUR3K9oTd19aXexSitZqQLVEKo26-i8hYWUS9CChzwAS8TgbWoqweFucJcNIgKBruzSd0mxn8zrh9i46lPxKMNDh-YEJ8)

如果已创建的文档类型中包含子文档类型，也可以点击“Document Sub Types”，然后为要编辑布局的子文档类型选择“Edit Layout”，如下图所示。

![文档类型的标签栏，其中Edit layout高亮显示，旁边还有Document Sub Types、Table columns、Fields、Model Training、Regex和Scripts等标签](https://lh7-us.googleusercontent.com/KfmM8wMGnn5tzXRxF1yT0Efm7X6v0kYeGzgNG3RihERh_P71tjEVkJh4POMwgqnsCBoE736xI7oHkmpYNUbtAShhE-wAHsnLuxljDtmhGQUyljF_PmOF2y6c0gIdIk_jUD3sVNsq5viT2sb236OBYSA)

## **布局管理器基础**

完成前面的步骤后，您将进入类似下图的页面。

### **上传示例文档**

要将文档上传到布局构建器，只需前往屏幕右侧。

![Layout Builder画布，左侧为空的分组区域，右侧为文档预览面板](https://lh7-us.googleusercontent.com/I99BkFDTOloyKwwc0P8O3wf8FbKL3B5Zn5i3GfeRKSSkBdelQ_HNfI2oJzaXQUi_UU6R5Vr7jrgcAxIrDmmTKWgTZx90J7izOX0oczWt__qt9VmD1HqafZvqH8vb7xnZMR1m5pjwzsbcnalErYo6dIc)

点击“Upload Documents”按钮，或将所需文档拖放到指定区域。

![Layout Builder页面，左侧为Elements和Properties面板，旁边是空白的布局画布](https://lh7-us.googleusercontent.com/GHqGYqvwFvN3z2ojFz_i7ZLlZhy-A3vsKUmmzOC0NMkPd2-f6_t_0USF66W-N3XRqHlmx06QNSQ7U-VTPQPKWdzOhoNcN7LlMk45sKVC6bWN1O92G0r4dKyHQLlgmGZiINYjZ9vZnt89_BjgzbON2MI)

### **分组**

点击以下图标即可创建分组。

![布局生成器的上传区域，其中带有用于放置示例文档的拖放区域](https://lh7-us.googleusercontent.com/eb4jnCmezPFKPwgUisJKvicBqMWuGHW69WIFdtpmQiY-_78VWmMyMD4TqKMJXwjH1XDnS5RXX0DsJ2_ur_GG62L4F7OEzkLrpgwUkiuQjZQPJqQoHIBj6WM33zY0AkYXhI3mKLjZetbEQ2AlhPJ8KV8)

分组可用于在布局中创建不同的区块，从而更轻松地分隔不同的数据或信息组，让布局更易于浏览。您可以为每个分组设置标题，帮助用户了解其中包含的信息。

![Layout Builder页面，Elements面板已打开，显示用于创建分组的拖动手柄图标](https://lh7-us.googleusercontent.com/lWqIEC-TCOp4rKytTbhn2fYWY618_Yra2mjWHA9oMyWPqHXA5JKCLoZoEtM8xQHAkn4HFNTPYpbMePUYnQhQGL0KmgBfTEDWPDAMy7PjZinZl2s_kHQlsLAGjYbzSINWTme3qRO9tHLcpVaDVvS_8F4)

### **表单元素**

![布局生成器的元素面板，其中列出Text、Label、Check Box、Multi Check Box、Horizontal Separator、Table Of Checkboxes、Button和QR Code Fields](https://lh7-us.googleusercontent.com/OFBRSGdol7loocu5uGVe4Q8URMDojvXTN0xj3TCgL-jb-wUgt1fjEqfXCyMPz_HNh94LVVmg6ifQDhxvlQsgbbChRfrw2Ohx4ICOUwHix3iiAFY9hI3BPGBfcNABiHLhgXQJVZmGvEO_niVWkIXz_6g)

以下是一组默认字段，可拖放到布局构建器中，用于创建所需的布局。其中包括：

* 文本 – 文本框，可在布局中创建一个字段，用户在验证界面中可以在其中输入文本。
* 标签 – 可用于创建不可编辑文本的字段，例如在验证界面中创建小标题或其他所需的固定文本。
* 复选框 – 创建一个布尔类型字段，可选中或取消选中。
* 多选复选框 – 功能与“复选框”相同，但适用于用户需要在一个区块中添加多个复选框的情况。
* 水平分隔线 – 在布局中创建一条水平线，可用于分隔布局中同一分组内的不同区块。
* 复选框表格 – 可创建一个复选框表格，并自定义 x 轴和 y 轴的值，例如：

![标题为Please mark with a cross的复选框表格，列标题为A到J，行包括Test和Test 2](https://lh7-us.googleusercontent.com/lMZU68H4i8ELjgenpcNXeNhJ9iwzTWGRkjNMEdV3rqdGwnaRZ_tvG9mbx2ogXQ2hMciGSp-9m1c5KS9VwGJWzuxcRiaioVDSLTLvh-csHUho4aX25LXrtjhGSfK6yTukufwrjQvZR-JliuhiaPCCxpw)

* 按钮 – 在布局的验证界面中创建可点击的按钮，可设置为以下三种功能之一：导出、Export mit Sonderwunsch 或拒绝。
* 提取的表格 -此元素可在文档布局中放置一个区域，用于显示从文档中提取的表格。了解详情请点击此处。
* 发票按钮 – 此元素可让您拖放一组针对发票优化的按钮。在验证界面中选择发票类型（成本或采购）后，PO Matching 或 Auto Accounting 会相应地消失。

![发票按钮组，显示SAVE RULES、PO MATCH、AUTO ACCOUNTING和EXPORT](https://lh7-us.googleusercontent.com/-w5iTr9b_pcc6Y39osFmuzKQGRa_e4tAXvQOn1zN8T4HwcuTs_FP9mFPAJJeABvYKTyiQr3xZALsRgueIDksbswhnY-E9ioT1AIaf8xwAblBckX1f8xzi5v9mLxBRRUZoViDntKK6Nd5fy5sd5Bq5LU)

* QR 码字段 – 此元素可让您拖放一个区块；当文档中存在 QR 码时，该区块会显示从文档中提取的所有信息。

### **创建文档专属字段**

用户可以为某种文档类型创建自定义分组和字段。创建文档类型时即可进行设置，也可以在 Settings 的 Document Types 页面中点击“Fields”来创建。

![文档类型选项卡栏，Fields选项卡被圈出，旁边是Edit layout、Document Sub Types、Table columns、Model Training、Regex和Scripts](https://lh7-us.googleusercontent.com/N9i3KnGyXATf5jLVbPQGiPEG9rlz6WqHJ5c8FZnpw3EwmaMnl2cQhMwhug3d-A82caOS6Nxc7LgAVLMtBL404hKR7i39u2RfwzCnohqn1_mbkMtjzNKThnjGu2ivaFNqKDuobzA6kUdD8gGiQ_zs3z8)

### **空白区域**

#### **百分之百规则**

![布局生成器中的分组，包含Group Title、字段Test1和Test2以及DELETE GROUP按钮](https://lh7-us.googleusercontent.com/TwNA3gZrgzhSvZrZOGywGYz92fRkUtjIsr6sDCxEzYgWcfJ9kXuzJKkqNiFyp3H5XXoqUz76TzZ72r86YY_O3Vw_rvDKczD_hdMOIQOFWORr2bo8pGunrAtUklJ1ye7KEQJEjRNqNUNCnXM0boIICUA)

要在布局中创建上图所示的空白区域，必须以特殊方式使用“表单元素”中的“标签”。这是因为布局管理器采用每行 100 个单位的系统，其中 1 个单位代表该行的 1%。因此，每行中的字段总共只能占用 100 个单位，如下图所示。

![Layout Builder，包含名为Test的标签元素，属性面板显示Name字段和Element Width in Percentage](https://lh7-us.googleusercontent.com/YTqddzVQPWRuP5ylV6NnMc-KnEgCY0ZxZ8zn0In5d5dOxaWnwGDi4N2qohbobLNphLfVD61sMUE5QlmXJZ3e0tP7Y8no_wVRy9WTF0nWIN5Tg3t-zLJhs9M-kVYPFV3CyerRZZoK-iMXLmKGcuSY_Nw)

这意味着用户必须按照此规则逐行构建布局。例如，假设您想在同一行中添加“Name”和“Date”字段，并希望“Name”字段更宽。可以从“Field Elements”下拉列表中拖放“Text”字段，并分别将两个字段命名为“Name”和“Date”，如下图所示。

![Layout Builder行，包含Name和Date字段，旁边的属性面板显示Name和Element Width in Percentage](https://lh7-us.googleusercontent.com/2ru3pj0iD3V6ADqYBjeQPqDT3uvTH_Al2MV0gpUUQ9MpX0TSFtnjYL6JN0YOkBk9afx2q2YcMo4gWE2jItUAGSEfX79O_6sFgKwP5FGa98SwzgjGgee1G-2aO6NyqZusf27SbJoWoHmzu51Hx25kVmM)

现在的问题是，这两个字段的大小都为 33（这是所有拖放字段的默认大小），但您希望“Name”字段比“Date”字段更宽，并且两个字段都应占满布局的整行。因此，按照百分之百规则，您可以将“Name”和“Date”字段设置为总和为 100 的任意组合。具体取决于您希望每个字段有多宽。本例中，我们将“Name”字段设为 70，将“Date”字段设为 30，结果如下：

![布局生成器，其中包含Name和Date字段，Properties面板显示Element Width in Percentage设置为70](https://lh7-us.googleusercontent.com/m411QblkCfsQWllhX74QpANjuVEv3fgM1Nhg8cJjbkNQGcjym6v0JFHIrKyMOAu-MasQ4KH9ZPaxmqNWfhWmAuL6SOZE030NXebb7ERzYxF99hLJC6oGbM-YXp7bNdZuoTaPmsDt7EjpV5BOiflwA4g)

同一规则适用于布局构建器中的所有字段。

#### **创建空白区域**

了解此规则后，创建空白区域就更容易理解了。如前所述，要创建空白区域，必须使用“表单元素”中的“标签”。

例如，假设您想在以下两个字段之间创建一个空白区域。

![Layout Builder中标题为Test的分组，包含DELETE GROUP按钮以及两个字段之间的空行](https://lh7-us.googleusercontent.com/jOms6aTB3wCmX3L-MiUTrOb_-q3AiFC3Y75TsHJe8QFLru10H9aZKzbE5MfHPZ0v9fqycQeddNPJp7pnRjv17crkrYUymNA8u9bF-3u9IfR6ru_duavqrLCQocommljzLA00RXs_lQA4gDH6l_QvyTs)

第一步是在这两个字段之间拖放一个“标签”。添加后，点击刚添加的“标签”字段，左侧会显示该字段的属性。接下来，像之前创建或更改字段名称时一样，清除“Label”属性中的所有名称，如下所示。

![Layout Builder中选中一个Label元素，Properties面板显示生成的名称input_8b7cc2b8和Element Width in Percentage](https://lh7-us.googleusercontent.com/0Mma4wYIIfAkOyRIFLZtjug7pbWltfaiPm3r_WgbP5fCgKe2BGD6Qf5YJ5Ns7fBBTRfJ68NlOtmOQrvcOvjyWGxk9v_XmDj-8moEQhcDUugh_VO5DdrJLYYV08ftr8YdhuhEM0otWs_ljew18j7XJFQ)

操作后的结果如下。

![Layout Builder中标题为Test的组，两个字段之间有空白间隙以及DELETE GROUP按钮](https://lh7-us.googleusercontent.com/-HqoJUAbcHRCletgSg6gcKXpn6zto1Do8I5EmcEmPWL4qUrMREh-wZdhy7ZKtnbuGjypd7p2mjcIu6LbbfdjA3c1liT2reCQXWiP1VAji08eWc_bbF_a0Dd82rJRgCuD5yjdlXL_DNheMcw-fm6pQnA)

现在，两个字段之间就出现了空隙。您可以按照前面讨论的百分之百规则加宽或缩短该空隙，并利用这些功能创建所需的任意布局。



{% embed url="https://youtu.be/TyK4JIoC6rc?si=BKdCTzgogXnWLkx-" %}
