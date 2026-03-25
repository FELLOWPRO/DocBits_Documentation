# Boş miktar ve tutarlı satırları silme

#### Bölüm 1: Boş Miktar ve Tutarlı Satırları Silme

Scriptin bu bölümü, hem miktar hem de toplam tutarın sıfır olduğu veya sağlanmadığı satırları kaldırmak için bir fatura tablosunu işler.

* **INVOICE\_TABLE kontrolü:** `tables_dict` sözlüğünde `INVOICE_TABLE` anahtarının olup olmadığını kontrol ederek başlar.
* **Satırları yineleme:** Tablodaki her satır için, `TOTAL_AMOUNT` ve `QUANTITY` sütunlarının mevcut olup olmadığını belirlemek ve değerlerini almak için bayraklar ve değişkenler başlatır.
* **Sütun adlarını kontrol etme:** Her satırdaki sütunları yinelerken `TOTAL_AMOUNT` ve `QUANTITY` adlı sütunları arar.
  * `TOTAL_AMOUNT` bulunursa değeri alınır. Değer sıfırdan farklıysa float'a dönüştürülür.
  * Benzer şekilde `QUANTITY` için de değer alınır ve sıfırdan farklıysa dönüştürülür.
* **Satırı silmek için işaretle:** Her iki sütunu kontrol ettikten sonra, hem toplam tutar hem de miktar fiilen sıfırsa (sıfır olarak veya mevcut olmayarak), satır `row['is_deleted']` `True` olarak ayarlanarak silinmek üzere işaretlenir.

#### Bölüm 2: Satır Toplamını Fatura Toplamına Karşı Doğrulama

Bu bölüm, bir faturadaki tüm satırlardan toplam tutarı hesaplar ve tutarlılıklarını doğrulamak için faturanın bildirilen toplamıyla karşılaştırır.

* **Satır toplamını başlat:** Tüm satırlardan toplam tutarı biriktirmek için `lines_total` değişkenini 0.0 olarak ayarlar.
* **Satır tutarlarını topla:** `INVOICE_TABLE` içindeki her satırı yineleyerek her birinden `TOTAL_AMOUNT`'ı çıkarır ve `lines_total`'a ekler.
* **Fatura toplamını al ve dönüştür:** Toplam fatura tutarını `get_field_value` yardımcı fonksiyonuyla alır ve float'a dönüştürür.
* **Toplamları karşılaştır:** Son olarak, hesaplanan satır toplamı (`lines_total`) ile bildirilen fatura toplamı (`total_amount`) arasındaki mutlak farkın 0.05 eşiğini aşıp aşmadığını kontrol eder. Aşıyorsa, uyumsuzluk belirterek fatura toplamı alanını `set_field_as_invalid` yardımcı fonksiyonuyla geçersiz olarak işaretler.

```python
##################################################
# Boş miktar ve tutarlı satırları sil
##################################################


if tables_dict.get('INVOICE_TABLE'):
    for row in tables_dict['INVOICE_TABLE']['rows']:
        amount_col_found = False
        quantity_col_found = False
        line_amount = 0.0
        line_quantity = 0.0
        for col in row['columns']:
            if col['name'] == 'TOTAL_AMOUNT':
                amount_col_found = True
                line_amount = col.get('value', 0)
                if line_amount:
                    line_amount = float(line_amount)
            if col['name'] == 'QUANTITY':
                quantity_col_found = True
                line_quantity = col.get('value', 0)
                if line_quantity:
                    line_quantity = float(line_quantity)
            if amount_col_found and quantity_col_found:
                break
        if amount_col_found and quantity_col_found and (not line_amount and not line_quantity or (line_amount + line_quantity) == 0):
            row['is_deleted'] = True

##################################################
# Son: Boş miktar ve tutarlı satırları sil
##################################################

##################################################
# Satır toplamını fatura toplamına karşı doğrulama
##################################################
lines_total = 0.0
# Satır toplamını alma
if tables_dict.get('INVOICE_TABLE'):
    for row in tables_dict['INVOICE_TABLE']['rows']:
        line_amount = 0.0
        for col in row['columns']:
            if col['name'] == 'TOTAL_AMOUNT':
                line_amount = col.get('value', 0)
                if line_amount:
                    line_amount = float(line_amount)
                break
        lines_total += line_amount

# Fatura toplamını alma
total_amount = get_field_value(fields_dict, "net_amount", "0.0")
if total_amount:
    total_amount = float(total_amount)

# Satır toplamını fatura toplamıyla karşılaştırma
if abs(total_amount - lines_total) > 0.05:
    set_field_as_invalid(fields_dict, "net_amount", "Invoice total mismatches lines total", "AMOUNTS_MISMATCH")

##################################################
# Son: Satır toplamını fatura toplamına karşı doğrulama
##################################################





```

#### Özet

Script, veri bütünlüğünü etkili bir şekilde sağlar:

1. Miktar veya tutarlarının olmaması nedeniyle faturanın mali toplamına katkıda bulunmayan veri satırlarını kaldırma.
2. Bireysel satır tutarlarının toplamı ile genel fatura toplamı arasındaki tutarlılığı doğrulama ve tutarsızlıkları daha fazla işlem için vurgulama.

Bu otomasyon, doğru mali kayıtların tutulmasına yardımcı olur ve muhasebe ve mali raporlama için kesin veri gerektiren ERP gibi sistemler için kritik olabilir.
