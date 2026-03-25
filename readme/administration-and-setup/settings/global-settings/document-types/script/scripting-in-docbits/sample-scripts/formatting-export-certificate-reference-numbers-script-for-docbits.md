# DocBits için İhracat Sertifikası Referans Numaralarını Biçimlendirme Scripti

Bu belge, DocBits'teki ihracat sertifikalarındaki referans numaralarını standartlaştırmayı amaçlayan "İhracat Sertifikası Referans Numaralarını Biçimlendirme" scriptini açıklar. Doğru biçimlendirme, referans numaralarının harici sistemler veya yasal gereksinimlerle uyumlu olmasını sağlar.

### Amaç

Scriptin temel amacı, ihracat sertifikalarındaki referans numaralarını biçimlendirerek, öndeki sıfırlarla doldurarak önceden tanımlanmış bir uzunluk gereksinimini karşılamalarını sağlamaktır. Bu tutarlılık, DocBits üzerinden işlenen tüm ihracat belgeleri için standart bir formatın korunmasına yardımcı olur.

### Script Genel Bakış

Script, ihracat sertifikasındaki `reference_number` alanını tanımlar, uzunluğunu kontrol eder ve gerekirse minimum uzunluk gereksinimini karşılamak için numarayı öndeki sıfırlarla doldurur.

#### Kod Parçası

```python
ref_number = get_field_value(fields_dict, 'reference_number')
# Referans numarasının en az 10 karakter uzunluğunda olmasını sağla
if len(ref_number) < 10:
    ref_number = ref_number.zfill(10)
    set_field_value(fields_dict, 'reference_number', ref_number)
```
