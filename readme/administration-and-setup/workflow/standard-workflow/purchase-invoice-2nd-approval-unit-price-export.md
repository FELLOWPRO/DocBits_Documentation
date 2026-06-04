# Purchase Invoice - 2nd Approval Unit Price Export

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.59.02 (1).png" alt=""><figcaption></figcaption></figure>

Ovaj naslov označava da je pravilo podešeno za upravljanje fazom drugog odobrenja faktura nabavke sa fokusom na jediničnu cenu, obezbeđujući da odgovara dogovorenim uslovima.

#### Konfiguracija pravila:

1. **When…**
   * **Document Type is Invoice**: Ovaj uslov obezbeđuje da se pravilo aktivira samo za dokumente identifikovane kao fakture, što je od ključnog značaja za tačno usmeravanje radnog toka.
2. **And…**
   * **Document Status is Pending Second Approval**: Ovo određuje da faktura čeka drugo odobrenje. Ova faza često pruža dodatni nadzor kako bi se obezbedila tačnost pre finalizacije transakcije.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Ovaj uslov dodatno određuje da se pravilo primenjuje samo na fakture kategorizovane posebno kao „Purchase Invoices“, razlikujući ih od drugih vrsta faktura.
   * **Logic Unit Price in order confirmation Equals purchase order**: Ovaj uslov proverava da li jedinična cena navedena u potvrdi porudžbine odgovara jediničnoj ceni u narudžbenici. Obezbeđuje da obrada fakture nastavlja dalje samo ako postoji konzistentnost u ceni, što je od ključnog značaja za budžetiranje i finansijsko izveštavanje.

#### Akcija (Then…):

* **Start Export**: Kada faktura ispuni navedene uslove (tj. jedinične cene se podudaraju između potvrde porudžbine i narudžbenice), pokreće se akcija „Start Export“. Ovo verovatno uključuje izvoz podataka fakture radi dalje obrade, moguće u drugi finansijski sistem ili u svrhu izveštavanja.

#### Svrha ovog pravila:

* **Ensure Accuracy and Consistency**: Verifikacijom da se jedinične cene podudaraju između potvrde porudžbine i narudžbenice, sistem pomaže u održavanju finansijske tačnosti i sprečava prekomerno ili nedovoljno naplaćivanje.
* **Streamline Financial Processing**: Automatizacija izvoza podataka kada se cene potvrde smanjuje ručnu obradu i ubrzava ciklus finansijske obrade.
* **Enhance Compliance and Oversight**: Zahtevanje drugog odobrenja za verifikaciju cena dodaje dodatni sloj nadzora, što je od ključnog značaja za usklađenost sa finansijskim politikama i kontrolama.

Ovo pravilo je primer kako se automatizacija radnog toka može efikasno iskoristiti za obezbeđivanje precizne i efikasne obrade finansijskih dokumenata u okviru organizacije, posebno u kontekstu velikih količina transakcija koje zahtevaju pažljivu validaciju.
