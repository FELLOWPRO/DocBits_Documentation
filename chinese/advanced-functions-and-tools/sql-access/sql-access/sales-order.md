# 销售订单

## 表 `public.sales_order`

### 列

* `id`：内部字段
* `org_id`：组织 ID
* `sub_org_id`：内部字段
* `location_id`：内部字段
* `order_number`：内部字段
* `customer_purchase_order`：内部字段
* `customer_id`：内部字段
* `customer_name`：内部字段
* `warehouse_id`：内部字段
* `warehouse_name`：内部字段
* `transportation_method`：内部字段
* `requested_delivery_date`：带时区的时间戳
* `order_date`：带时区的时间戳
* `sales_person_id`：内部字段
* `sales_person_name`：内部字段
* `ship_to_party_id`：内部字段
* `ship_to_party_name`：内部字段
* `ship_to_party_city`：内部字段
* `ship_to_party_state`：内部字段
* `ship_to_party_country`：内部字段
* `ship_to_party_zip`：内部字段
* `status`：内部字段
* `created_by`：整数
* `created_on`：带时区的时间戳
* `last_modified_on`：带时区的时间戳
* `is_deleted`：布尔值
* `deleted_on`：带时区的时间戳
* `preview_path`：内部字段
* `last_modified_by`：内部字段
* `deleted_by`：内部字段

### 分析与说明

## `public.sales_order` 表技术文档

### 简介

`public.sales_order` 表用于在业务场景中记录和存储与销售订单相关的信息，包括订单、客户、物流详情，以及与订单生命周期相关的各种元数据。该表是跟踪销售交易状态和历史记录的中央存储库。

### 列说明

#### id

* **含义**：每个销售订单的唯一标识符。
* **作用**：主键。
* **典型内容**：UUID 字符串（例如：`'6ffe4673-7563-44dc-8e71-855e8f25534a'`）。

#### org\_id

* **含义**：创建销售订单的组织的标识符。
* **作用**：外键。
* **典型内容**：表示组织的 UUID 字符串（例如：`'23f3d697-7411-4c95-981d-faf089d266be'`）。

#### sub\_org\_id

* **含义**：子组织的标识符（如适用）。
* **作用**：外键。
* **典型内容**：如果不适用，则可能为 `NULL`。

#### location\_id

* **含义**：与销售订单关联的位置标识符。
* **作用**：外键。
* **典型内容**：表示位置的字符串代码（例如：`'028'`）。

#### order\_number

* **含义**：分配给销售订单的唯一编号。
* **作用**：用于跟踪订单的技术字段。
* **典型内容**：字符串（例如：`'0010174175'`）。

#### customer\_purchase\_order

* **含义**：客户采购订单的参考编号。
* **作用**：用于交叉引用的技术字段。
* **典型内容**：字符串（例如：`'1YFNC3'`）。

#### customer\_id

* **含义**：下单客户的标识符。
* **作用**：外键。
* **典型内容**：字符串代码（例如：`'35623000'`）。

#### customer\_name

* **含义**：客户名称。
* **作用**：描述性字段。
* **典型内容**：字符串（例如：`'DOLLAR GENERAL'`）。

#### warehouse\_id

* **含义**：负责履行订单的仓库的标识符。
* **作用**：外键。
* **典型内容**：字符串代码（例如：`'028'`）。

#### warehouse\_name

* **含义**：仓库名称。
* **作用**：描述性字段。
* **典型内容**：字符串（例如：`'USCS - DENTON, TX'`）。

#### transportation\_method

* **含义**：交付订单所采用的运输方式。
* **作用**：描述性字段。
* **典型内容**：字符串代码（例如：`'001'`）。

#### requested\_delivery\_date

* **含义**：客户要求的交付日期。
* **作用**：描述性字段。
* **典型内容**：时间戳（例如：`None`）。

#### order\_date

* **含义**：订单下达日期。
* **作用**：描述性字段。
* **典型内容**：时间戳（例如：`datetime.datetime(2024, 1, 29, 0, 0, tzinfo=datetime.timezone.utc)`）。

#### sales\_person\_id

* **含义**：负责处理订单的销售人员的标识符。
* **作用**：外键。
* **典型内容**：字符串（例如：`'ROBERTDOCK'`）。

#### sales\_person\_name

* **含义**：销售人员姓名。
* **作用**：描述性字段。
* **典型内容**：字符串（例如：`'ROBERT DOCKINS'`）。

#### ship\_to\_party\_id

* **含义**：订单收货方的标识符。
* **作用**：外键。
* **典型内容**：字符串（例如：`'35623000 009'`）。

#### ship\_to\_party\_name

* **含义**：订单收货方名称。
* **作用**：描述性字段。
* **典型内容**：字符串（例如：`'DOLLAR GENERAL DC 98061/96460'`）。

#### ship\_to\_party\_city

* **含义**：收货地址所在城市。
* **作用**：描述性字段。
* **典型内容**：字符串（例如：`'SAN ANTONIO'`）。

#### ship\_to\_party\_state

* **含义**：收货地址所在州。
* **作用**：描述性字段。
* **典型内容**：可能为 `NULL`。

#### ship\_to\_party\_country

* **含义**：收货地址所在国家/地区。
* **作用**：描述性字段。
* **典型内容**：字符串（例如：`'US'`）。

#### ship\_to\_party\_zip

* **含义**：收货地址的邮政编码。
* **作用**：描述性字段。
* **典型内容**：字符串（例如：`'78218'`）。

#### status

* **含义**：销售订单的当前状态。
* **作用**：描述性字段。
* **典型内容**：字符串（例如：`'Allocated'`）。

#### created\_by

* **含义**：创建该条目的用户标识符。
* **作用**：技术字段。
* **典型内容**：整数（例如：`1`）。

#### created\_on

* **含义**：创建该条目的时间戳。
* **作用**：技术字段。
* **典型内容**：时间戳（例如：`datetime.datetime(2024, 3, 6, 11, 48, 43, 237208, tzinfo=datetime.timezone.utc)`）。

#### last\_modified\_on

* **含义**：最后一次修改的时间戳。
* **作用**：技术字段。
* **典型内容**：时间戳（例如：`datetime.datetime(2024, 9, 4, 8, 42, 32, 912247, tzinfo=datetime.timezone.utc)`）。

#### is\_deleted

* **含义**：指示订单是否已标记为删除的标志。
* **作用**：技术字段。
* **典型内容**：布尔值（例如：`False`）。

#### deleted\_on

* **含义**：订单标记为删除时的时间戳。
* **作用**：技术字段。
* **典型内容**：未删除时的默认日期（例如：`datetime.datetime(2, 1, 1, 11, 0, tzinfo=datetime.timezone.utc)`）。

#### preview\_path

* **含义**：销售订单预览文档的路径。
* **作用**：描述性字段。
* **典型内容**：表示文件路径的字符串（例如：`'previews/sales_order/23f3d697-7411-4c95-981d-faf089d266be/0010174175/0010174175_preview.pdf'`）。

#### last\_modified\_by

* **含义**：最后修改该条目的用户标识符。
* **作用**：技术字段。
* **典型内容**：可能为 `NULL`。

#### deleted\_by

* **含义**：将该条目标记为删除的用户标识符。
* **作用**：技术字段。
* **典型内容**：可能为 `NULL`。
