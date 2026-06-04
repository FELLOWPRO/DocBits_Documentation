# Purchase Invoice - 2nd Approval Quantity Export

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 15.00.53 (1).png" alt=""><figcaption></figcaption></figure>

Ovaj naslov označava da je pravilo podešeno za upravljanje fazom drugog odobrenja za fakture nabavke sa naglaskom na detalje o količini, obezbeđujući da količine na fakturi odgovaraju onima na originalnoj narudžbenici.

#### Konfiguracija pravila:

1. **When…**
   * **Document Type is Invoice**: Ovaj uslov obezbeđuje da se pravilo aktivira samo za dokumente identifikovane kao fakture, što je od ključnog značaja za tačno usmeravanje radnog toka.
2. **And…**
   * **Document Status is Pending Second Approval**: Ovo određuje da faktura trenutno čeka drugo odobrenje. Ova faza često pruža dodatni nadzor kako bi se obezbedila tačnost pre finalizacije transakcije.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Ovaj uslov dodatno određuje da se pravilo primenjuje samo na fakture kategorizovane posebno kao „Purchase Invoices“, razlikujući ih od drugih vrsta faktura.
   * **Logic Quantity in order confirmation Equals purchase order**: Ovaj uslov proverava da li količina navedena u potvrdi porudžbine odgovara količini u narudžbenici. Obezbeđuje da obrada fakture nastavlja dalje samo ako su količine konzistentne, što je od ključnog značaja za upravljanje zalihama i finansijsku tačnost.

#### Akcija (Then…):

* **Start Export**: Kada faktura ispuni navedene uslove (tj. količine se podudaraju između potvrde porudžbine i narudžbenice), pokreće se akcija „Start Export“. Ovo verovatno uključuje izvoz podataka fakture radi dalje obrade, moguće u drugi finansijski sistem ili u svrhu izveštavanja.

#### Svrha ovog pravila:

* **Ensure Accuracy and Consistency**: Verifikacijom da se količine podudaraju između potvrde porudžbine i narudžbenice, sistem pomaže u održavanju tačnosti zaliha i sprečava neslaganja koja bi mogla uticati na finansijsko izveštavanje ili upravljanje zalihama.
* **Streamline Financial Processing**: Automatizacija izvoza podataka kada se količine potvrde smanjuje ručnu obradu i ubrzava ciklus finansijske obrade.
* **Enhance Compliance and Oversight**: Zahtevanje drugog odobrenja za verifikaciju količina dodaje dodatni sloj nadzora, ključan za usklađenost sa finansijskim politikama i kontrolama.

Ovo pravilo je jasan primer kako se automatizacija radnog toka može efikasno koristiti za obezbeđivanje precizne i efikasne obrade finansijskih dokumenata u okviru organizacije, posebno u kontekstu procesa nabavke koji uključuju velike količine transakcija koje zahtevaju pažljivu validaciju.
