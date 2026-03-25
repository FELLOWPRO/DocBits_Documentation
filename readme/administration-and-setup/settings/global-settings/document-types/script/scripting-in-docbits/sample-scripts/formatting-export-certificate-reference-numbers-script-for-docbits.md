# Skripta za formatiranje referentnih brojeva izvoznih sertifikata u DocBits-u

Ovaj dokument opisuje skriptu "Formatiranje referentnih brojeva izvoznih sertifikata", koja ima za cilj standardizaciju referentnih brojeva na izvoznim sertifikatima u DocBits-u. Pravilno formatiranje osigurava da referentni brojevi odgovaraju zahtevima eksternih sistema ili regulatornim zahtevima.

### Svrha

Primarni cilj skripte je formatiranje referentnih brojeva na izvoznim sertifikatima, osiguravajuci da ispunjavaju unapred definisani zahtev za duzinu dopunjavanjem vodecim nulama. Ova konzistentnost pomaze u odrzavanju standardizovanog formata za sve izvozne dokumente obradjene kroz DocBits.

### Pregled skripte

Skripta identifikuje polje `reference_number` u izvoznom sertifikatu, proverava njegovu duzinu i, ako je potrebno, dopunjava broj vodecim nulama kako bi ispunio minimalni zahtev za duzinu.

#### Isecak koda

```python
ref_number = get_field_value(fields_dict, 'reference_number')
# Osigurava da referentni broj ispunjava minimalnu duzinu od 10 karaktera
if len(ref_number) < 10:
    ref_number = ref_number.zfill(10)
    set_field_value(fields_dict, 'reference_number', ref_number)
```

