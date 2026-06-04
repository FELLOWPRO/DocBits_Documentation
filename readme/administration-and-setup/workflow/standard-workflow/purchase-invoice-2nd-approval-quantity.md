# Purchase Invoice - 2nd Approval Quantity

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.56.54 (1).png" alt=""><figcaption></figcaption></figure>

Ovaj naslov označava da se pravilo odnosi posebno na obradu faktura za nabavku tokom faze sekundarnog odobravanja, sa fokusom na verifikaciju tačnosti navedenih količina.

#### Konfiguracija pravila:

1. **When…**
   * **Document Type is Invoice**: Ovaj uslov obezbeđuje da se pravilo aktivira samo za dokumente klasifikovane kao fakture. Ovo je od suštinskog značaja za održavanje specifičnosti i relevantnosti u radnom toku.
2. **And…**
   * **Document Status is Pending Second Approval**: Ovo određuje da faktura trenutno čeka drugo odobrenje. Ova faza je obično namenjena pružanju dodatnog nadzora pre finalizacije fakture.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Ovaj uslov dodatno precizira pravilo tako da se primenjuje isključivo na fakture identifikovane kao „Purchase Invoices“. Ova kategorizacija pomaže u njihovom razlikovanju od drugih vrsta faktura.
   * **Logic Quantity in order confirmation Not Equals purchase order**: Ovaj kritičan uslov proverava da li količina navedena u potvrdi porudžbine odgovara količini na originalnoj narudžbenici. Akcija se pokreće ako postoji neslaganje, što ukazuje na potencijalnu grešku ili problem koji treba rešiti.

#### Akcija (Then…):

* **Assign user from field Buyer Name, use user User as fallback**: Ako su uslovi pravila ispunjeni (tj. postoji neslaganje u količinama), faktura se automatski dodeljuje osobi navedenoj u polju „Buyer Name“ na dalji pregled. Ako je ovo polje prazno ili navedena osoba nije dostupna, podrazumevani korisnik (verovatno administrator ili drugi određeni član osoblja) preuzima zadatak kako bi se obezbedio blagovremen pregled i rešavanje.

#### Svrha ovog pravila:

* **Accuracy and Compliance**: Pravilo je od ključnog značaja za obezbeđivanje da proces fakturisanja bude tačan i usklađen sa uslovima dogovorenim u narudžbenici. Pomaže u sprečavanju finansijskih neslaganja i potencijalnih grešaka u zalihama.
* **Streamlined Approvals**: Automatizacija procesa pregleda za određena neslaganja pomaže u pojednostavljivanju odobravanja i obezbeđuje da odgovarajuće osoblje brzo reši sve probleme.
* **Enhanced Financial Oversight**: Zahtevanje sekundarnog odobrenja za verifikaciju količina jača finansijske kontrole i odgovornost u okviru organizacije.

Ovo podešavanje ilustruje kako se automatizacija radnog toka može iskoristiti za poboljšanje operativne efikasnosti i obezbeđivanje finansijskog integriteta, posebno u upravljanju složenim procesima nabavke u okviru kompanije.
