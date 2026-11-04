# Docbits 出口证书参考编号格式化脚本

本文介绍“出口证书参考编号格式化”脚本，该脚本旨在统一 Docbits 中各出口证书的参考编号格式。正确的格式可确保参考编号符合外部系统或法规要求。

### 用途

该脚本的主要目标是格式化出口证书上的参考编号，通过在编号前补零，确保其达到预设长度要求。这种一致性有助于为 Docbits 处理的所有出口文档保持统一格式。

### 脚本概览

该脚本会识别出口证书中的 `reference_number` 字段，检查其长度，并在必要时在编号前补零，以确保其达到最小长度要求。

#### 代码片段

```python
ref_number = get_field_value(fields_dict, 'reference_number')
# Ensure the reference number meets a minimum length of 10 characters
if len(ref_number) < 10:
    ref_number = ref_number.zfill(10)
    set_field_value(fields_dict, 'reference_number', ref_number)
```
