# Primeri skripti

Produkcijski spremni primeri skripti za uobicajene slucajeve automatizacije u DocBits-u. Svaki primer ukljucuje kompletnu skriptu, objasnjenje korak po korak i linkove ka koriscenim funkcijama.

## Primeri prema slucajevima koriscenja

### Validacija podataka
- [Validacija dobavljaca putem Lookup-a](lookup-supplier-validation.md) -- Validacija dobavljaca prema maticnim podacima
- [Validacija zbira tabele](table-sum-validation.md) -- Verifikacija da ukupni iznosi stavki odgovaraju neto iznosu

### Automatizacija
- [Automatsko uparivanje narudzbenica](auto-po-matching.md) -- Pokretanje automatskog uparivanja narudzbenica
- [Auto-izvoz na osnovu uslova](status-auto-export.md) -- Preskakanje validacije za fakture niskog rizika
- [Obracun datuma dospeca](due-date-calculation.md) -- Izracunavanje uslova placanja sa preskakanjem vikenda

### Poslovna pravila
- [Detekcija poreskog koda](tax-code-detection.md) -- Odredjivanje poreskog koda iz celokupnog teksta i iznosa
- [Zadatak za visok iznos](task-high-amount.md) -- Kreiranje zadatka za odobrenje velikih faktura
- [Dinamicka obavezna polja](dynamic-required-fields.md) -- Prilagodjavanje obaveznih polja na osnovu valute

### Fulltext и векторска претрага
- [Детекција дупликата фактура](duplicate-invoice-detection.md) — Проналажење дупликата фактура коришћењем fulltext претраге
- [Детекција сличних докумената](similar-document-detection.md) — Означавање сличних докумената коришћењем векторске претраге
- [Претрага текста усклађености](compliance-text-search.md) — Претрага кључних речи усклађености (нпр. Reverse Charge)
- [ERP валидација добављача](erp-vendor-validation.md) — Валидација добављача према ERP главним подацима
- [Попуњавање недостајућих поља из историје](fill-missing-fields-from-history.md) — Аутоматско попуњавање поља из сличних претходних докумената

### Stari primeri
- [Obracun ukupnih troskova](calculating-total-charges-script-for-docbits-1.md) -- Sabiranje troskova prevoza i pakovanja
- [Brisanje praznih redova](delete-lines-with-empty-quantity-and-amount.md) -- Uklanjanje redova sa nultom kolicinom/iznosom
- [Brojevi izvoznih sertifikata](formatting-export-certificate-reference-numbers-script-for-docbits.md) -- Dopunjavanje referentnih brojeva vodecim nulama
- [Prosireni brojevi faktura](generating-extended-invoice-numbers-script-for-docbits-1.md) -- Spajanje ID-a fakture i broja narudzbenice
- [USD kao podrazumevana valuta](usd-as-default-currency.md) -- Postavljanje USD kao podrazumevane valute
