# 接收交货行

## 表 `public.receive_delivery_line`

### 列

* `id`：内部字段
* `org_id`：组织 ID
* `receive_delivery_id`：内部字段
* `delivery_number`：内部字段
* `line_number`：内部字段
* `item_id`：内部字段
* `description`：内部字段
* `shipped_quantity`：双精度
* `status`：内部字段
* `created_by`：整数
* `created_on`：带时区的时间戳
* `last_modified_on`：带时区的时间戳
* `deleted_on`：带时区的时间戳
* `is_deleted`：布尔值
* `purchase_order`：内部字段
* `sequence_number`：内部字段
* `sub_org_id`：内部字段
* `shipped_quantity_unit_code`：内部字段
* `packing_slip_quantity`：双精度
* `packing_slip_quantity_unit_code`：内部字段
* `received_quantity`：双精度
* `received_quantity_unit_code`：内部字段
* `purchase_order_line_number`：内部字段
* `status_effective_from`：带时区的时间戳
* `purchase_order_sub_line_number`：内部字段
* `invoiced_quantity`：双精度
* `invoice_matching_status`：内部字段
* `open_quantity`：双精度
* `last_modified_by`：内部字段
* `deleted_by`：内部字段

### 分析与描述

## 表文档：`public.receive_delivery_line`

### 简介

`public.receive_delivery_line` 表看起来是组织物流和供应链运营中交货行与收货行的详细记录。表中的每一行代表某次交货中的一个特定行项目，记录项目描述、发运和收货数量以及各种状态字段等信息。该表是跟踪货物从发运到收货全过程的重要组成部分，也涵盖发票和订单管理。

### 列说明

#### id

* **含义**：每个交货行项目的唯一标识符。
* **作用**：主键。
* **典型内容**：唯一的通用唯一标识符（UUID）。

#### org\_id

* **含义**：与交货相关的组织标识符。
* **作用**：外键。
* **典型内容**：表示组织的 UUID。

#### receive\_delivery\_id

* **含义**：关联到整笔交货交易的标识符。
* **作用**：外键。
* **典型内容**：与特定交货交易关联的 UUID。

#### delivery\_number

* **含义**：分配给交货的唯一编号。
* **作用**：引用字段。
* **典型内容**：表示交货编号的字符串。

#### line\_number

* **含义**：交货中的具体行号。
* **作用**：引用字段。
* **典型内容**：表示行项目顺序的数字字符串。

#### item\_id

* **含义**：待发运项目的标识符。
* **作用**：引用字段。
* **典型内容**：与项目对应的数字字符串。

#### description

* **含义**：项目描述。
* **作用**：描述字段。
* **典型内容**：项目的文本描述，例如“面粉、小麦、未漂白、富含营养成分、散装”。

#### shipped\_quantity

* **含义**：已发运的项目数量。
* **作用**：数量字段。
* **典型内容**：表示发运数量的十进制数。

#### status

* **含义**：交货行项目的当前状态。
* **作用**：状态字段。
* **典型内容**：例如“已收货”这样的文本。

#### created\_by

* **含义**：创建该记录的用户或系统标识符。
* **作用**：审计字段。
* **典型内容**：表示用户 ID 的整数。

#### created\_on

* **含义**：记录的创建时间戳。
* **作用**：审计字段。
* **典型内容**：带时区的日期和时间。

#### last\_modified\_on

* **含义**：记录最近一次修改的时间戳。
* **作用**：审计字段。
* **典型内容**：带时区的日期和时间。

#### deleted\_on

* **含义**：记录被标记为已删除的时间戳。
* **作用**：审计字段。
* **典型内容**：带时区的日期和时间；记录未删除时通常为 null。

#### is\_deleted

* **含义**：指示记录是否被标记为已删除。
* **作用**：技术字段。
* **典型内容**：布尔值 true 或 false。

#### purchase\_order

* **含义**：关联采购订单的引用。
* **作用**：引用字段。
* **典型内容**：表示采购订单编号的字母数字字符串。

#### sequence\_number

* **含义**：交货行的序号。
* **作用**：引用字段。
* **典型内容**：数字字符串，通常为 null。

#### sub\_org\_id

* **含义**：相关子组织的标识符。
* **作用**：外键。
* **典型内容**：UUID，通常为 null。

#### shipped\_quantity\_unit\_code

* **含义**：发运数量的计量单位。
* **作用**：引用字段。
* **典型内容**：表示计量单位的代码，例如“LBP”。

#### packing\_slip\_quantity

* **含义**：装箱单所列的数量。
* **作用**：数量字段。
* **典型内容**：十进制数，通常为 null。

#### packing\_slip\_quantity\_unit\_code

* **含义**：装箱单数量的单位代码。
* **作用**：引用字段。
* **典型内容**：表示计量单位的代码，通常为 null。

#### received\_quantity

* **含义**：实际收到的项目数量。
* **作用**：数量字段。
* **典型内容**：表示收货数量的十进制数。

#### received\_quantity\_unit\_code

* **含义**：收货数量的单位代码。
* **作用**：引用字段。
* **典型内容**：表示计量单位的代码，例如“LBP”。

#### purchase\_order\_line\_number

* **含义**：采购订单中的行号。
* **作用**：引用字段。
* **典型内容**：数字字符串。

#### status\_effective\_from

* **含义**：状态开始生效的日期和时间。
* **作用**：状态字段。
* **典型内容**：带时区的日期和时间，通常为 null。

#### purchase\_order\_sub\_line\_number

* **含义**：采购订单中的子行号。
* **作用**：引用字段。
* **典型内容**：数字字符串，通常为“000”。

#### invoiced\_quantity

* **含义**：已开票的数量。
* **作用**：数量字段。
* **典型内容**：十进制数。

#### invoice\_matching\_status

* **含义**：发票匹配流程的状态。
* **作用**：状态字段。
* **典型内容**：文本状态代码，例如“9.0”。

#### open\_quantity

* **含义**：尚未处理或仍未结清的数量。
* **作用**：数量字段。
* **典型内容**：十进制数。

#### last\_modified\_by

* **含义**：最近一次修改该记录的用户标识符。
* **作用**：审计字段。
* **典型内容**：用户的 UUID，通常为 null。

#### deleted\_by

* **含义**：将记录标记为已删除的用户标识符。
* **作用**：审计字段。
* **典型内容**：用户的 UUID，通常为 null。
