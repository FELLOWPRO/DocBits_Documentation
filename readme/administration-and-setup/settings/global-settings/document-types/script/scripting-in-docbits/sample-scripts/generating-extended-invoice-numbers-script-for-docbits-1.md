# DocBits için Genişletilmiş Fatura Numaraları Oluşturma Scripti

Bu belge, DocBits'te genişletilmiş fatura numaralarının oluşturulmasını otomatikleştiren "Genişletilmiş Fatura Numaraları Oluşturma" scriptini detaylı olarak açıklar. Genişletilmiş fatura numaraları, fatura ID'si ve satınalma belgesi numarası gibi birden fazla belge tanımlayıcısını tek bir kapsamlı tanımlayıcıda birleştirir. Bu script, belge izlenebilirliğini artırır ve kayıt tutmayı basitleştirir.

### Amaç

Bu scriptin amacı, fatura ID'si ve satınalma belgesi numarasını otomatik olarak birleştirerek genişletilmiş fatura numaraları oluşturma sürecini kolaylaştırmaktır, böylece her fatura belgesi için birleşik ve benzersiz bir tanımlayıcı sağlar.

### Script Genel Bakış

Script, belge içinde fatura ID'si ve satınalma belgesi numarası alanlarının varlığını kontrol eder, her ikisi de mevcutsa değerlerini birleştirir (tire ayırıcı ile) ve birleştirilmiş değeri saklamak için yeni bir alan günceller veya oluşturur.

#### Kod Parçası

```python
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Fatura ID'si ve satınalma belgesi numarasını tire ayırıcı ile birleştirme
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Ayarlanacak genişletilmiş numara olup olmadığını kontrol et
if extended_number:
    # 'invoice_extended_number' alanını birleştirilmiş değerle güncelleme
    if not 'invoice_extended_number' in fields_dict:
        new_field = create_new_field('invoice_extended_number', extended_number)
        fields_dict['invoice_extended_number'] = new_field
        document_json['fields'].append(new_field)
    else:
        set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```
