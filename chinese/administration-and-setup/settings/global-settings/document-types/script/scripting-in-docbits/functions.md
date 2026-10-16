# 函数

脚本函数文档已重新整理为多个专题类别，方便导航。

## 函数类别

### [字段函数](field-functions.md)

读取、写入和控制文档字段——`get_field_value()`、`set_field_value()`、`set_date_value()`、`set_amount_value()`、`set_field_as_invalid()`、`set_is_required()`、`set_is_hidden()`、`set_is_readonly()` 等。

### [表格函数](table-functions.md)

读取、写入和操作表格及表格行——`get_column_value()`、`set_column_value()`、`add_table_column()`、`remove_rows_from_table()`、`delete_tables()` 等。

### [业务逻辑函数](business-logic-functions.md)

查询、采购订单匹配、任务、用户/组管理和状态变更——`get_lookup_records()`、`auto_po_match_for_purchase_orders()`、`get_next_sequence_number()`、`create_document_task()`、`get_group_by_name()` 等。

### [实用工具函数](utility-functions.md)

Python 内置函数、字符串操作、数学、正则表达式、日期/时间和数据结构——`re_search()`、`strptime()`、`levenshtein_distance()`、`parse_decimal()` 等。

### [全文和向量搜索函数](fulltext-search-functions.md)

搜索文档存档、查找相似文档并查询 ERP 主数据——`fulltext_search()`、`vector_search()`、`fulltext_search_erp()`、`fulltext_suggestions()`。**从版本 11.48.0 起提供**，需要 `OPENSEARCH_ENABLED` 许可证。

## 快速参考

| 类别 | 主要函数 |
| -------- | ------------- |
| **字段** | `get_field_value`、`set_field_value`、`set_date_value`、`set_amount_value`、`set_field_as_invalid`、`set_field_as_valid`、`set_is_required`、`set_is_readonly`、`set_is_hidden` |
| **表格** | `get_column_value`、`set_column_value`、`set_column_date_value`、`set_column_amount_value`、`add_table_column`、`remove_rows_from_table` |
| **业务逻辑** | `get_lookup_records`、`auto_po_match_for_purchase_orders`、`get_next_sequence_number`、`create_document_task`、`update_document_status_with_doc_id`、`get_group_by_name` |
| **搜索** | `fulltext_search`、`vector_search`、`fulltext_search_erp`、`fulltext_suggestions` |
| **实用工具** | `re_search`、`re_sub`、`re_findall`、`strptime`、`strftime`、`levenshtein_distance`、`parse_decimal`、`deepcopy` |
