# DocBits için Toplam Masrafları Hesaplama Scripti

"Toplam Masrafları Hesaplama" scripti, fatura belgeleri içindeki çeşitli masrafları ve ek tutarları toplama işlemini otomatikleştirir. Bu rehber, belgelerinizde doğru toplam masraf hesaplamalarını sağlamak için script kurulumunu, mantığını ve uygulamasını adım adım açıklar.

### Amaç

Bu script, temel masraflar, navlun (Fracht) ve paketleme (Verpackung) gibi farklı masraf türlerini toplayarak bir faturadaki toplam masrafları dinamik olarak hesaplamayı amaçlar. Ardından faturanın toplam masraflar alanını hesaplanan toplam ile güncelleyerek doğru fatura bilgilerini sağlar.

### Script Genel Bakış

Script, belirtilen alanlardan değerleri alır, bunları float'a dönüştürür, toplar ve ardından `total_charges` alanını sonuçla günceller. `total_charges` alanı mevcut değilse, script bu alanı oluşturur ve değerini buna göre ayarlar.

#### Kod Parçası

```python
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Toplamı 0 olarak başlat
total = 0

# Navlun varsa toplama ekle
if fracht:
    fracht = float(fracht)
    total += fracht

# Paketleme varsa toplama ekle
if verpackung:
    verpackung = float(verpackung)
    total += verpackung

# Toplamı iki ondalık basamağa biçimlendir
formatted_total = "{0:.2f}".format(total)

# total_charges alanının mevcut olup olmadığını kontrol et ve buna göre güncelle veya oluştur
if 'total_charges' not in fields_dict:
    new_field = create_new_field('total_charges', formatted_total)
    fields_dict['total_charges'] = new_field
    document_json['fields'].append(new_field)
else:
    set_field_value(fields_dict, 'total_charges', formatted_total)
```
