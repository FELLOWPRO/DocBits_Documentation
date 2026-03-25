# Fonksiyonlar

Scripting fonksiyonları dokümantasyonu, daha kolay gezinme için odaklanmış kategorilere yeniden düzenlenmiştir.

## Fonksiyon Kategorileri

### [Alan Fonksiyonları](field-functions.md)

Belge alanlarını okuma, yazma ve kontrol etme — `get_field_value()`, `set_field_value()`, `set_date_value()`, `set_amount_value()`, `set_field_as_invalid()`, `set_is_required()`, `set_is_hidden()`, `set_is_readonly()` ve daha fazlası.

### [Tablo Fonksiyonları](table-functions.md)

Tabloları ve tablo satırlarını okuma, yazma ve işleme — `get_column_value()`, `set_column_value()`, `add_table_column()`, `remove_rows_from_table()`, `delete_tables()` ve daha fazlası.

### [İş Mantığı Fonksiyonları](business-logic-functions.md)

Aramalar, SB eşleştirme, görevler, kullanıcı/grup yönetimi ve durum değişiklikleri — `get_lookup_records()`, `auto_po_match_for_purchase_orders()`, `get_next_sequence_number()`, `create_document_task()`, `get_group_by_name()` ve daha fazlası.

### [Yardımcı Fonksiyonlar](utility-functions.md)

Python yerleşik fonksiyonları, string işlemleri, matematik, regex, tarih/saat ve veri yapıları — `re_search()`, `strptime()`, `levenshtein_distance()`, `parse_decimal()` ve daha fazlası.


### [Fulltext ve Vektör Arama Fonksiyonları](fulltext-search-functions.md)

Belge arşivlerini arayın, benzer belgeleri bulun ve ERP ana verilerini sorgulayın — `fulltext_search()`, `vector_search()`, `fulltext_search_erp()`, `fulltext_suggestions()`. **Sürüm 11.48.0'dan itibaren kullanılabilir**, `OPENSEARCH_ENABLED` lisansı gerektirir.

## Hızlı Başvuru

| Kategori | Temel Fonksiyonlar |
| -------- | ------------- |
| **Alanlar** | `get_field_value`, `set_field_value`, `set_date_value`, `set_amount_value`, `set_field_as_invalid`, `set_field_as_valid`, `set_is_required`, `set_is_readonly`, `set_is_hidden` |
| **Tablolar** | `get_column_value`, `set_column_value`, `set_column_date_value`, `set_column_amount_value`, `add_table_column`, `remove_rows_from_table` |
| **İş Mantığı** | `get_lookup_records`, `auto_po_match_for_purchase_orders`, `get_next_sequence_number`, `create_document_task`, `update_document_status_with_doc_id`, `get_group_by_name` |
| **Arama** | `fulltext_search`, `vector_search`, `fulltext_search_erp`, `fulltext_suggestions` |
| **Yardımcı** | `re_search`, `re_sub`, `re_findall`, `strptime`, `strftime`, `levenshtein_distance`, `parse_decimal`, `deepcopy` |
