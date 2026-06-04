# Purchase Invoice - 2nd Approval Unit Price

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.55.09 (1).png" alt=""><figcaption></figcaption></figure>

Ovaj naslov označava da je pravilo podešeno za upravljanje fazom drugog odobrenja fakture nabavke, sa posebnim fokusom na validaciju jedinične cene.

#### Konfiguracija pravila:

1. **When…**
   * **Document Type is Invoice**: Ovaj uslov obezbeđuje da se pravilo pokreće samo za dokumente koji su identifikovani kao fakture, filtrirajući druge vrste dokumenata i održavajući relevantnost radnog toka.
2. **And…**
   * **Document Status is Pending Second Approval**: Ovo određuje da je faktura u fazi u kojoj čeka drugo odobrenje. Ovo je obično korak dizajniran da obezbedi dodatni nadzor pre konačne obrade.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Ovo dodatno sužava primenu ovog pravila samo na one fakture koje su klasifikovane kao „Purchase Invoices“, razlikujući ih od drugih podtipova faktura.
   * **Logic Unit Price in order confirmation Not Equals purchase order**: Ova logička provera je ključna jer upoređuje jediničnu cenu navedenu u potvrdi porudžbine sa jediničnom cenom u originalnoj narudžbenici. Akcija se pokreće ako se ove vrednosti ne podudaraju, što bi moglo ukazivati na neslaganje koje treba rešiti.

#### Akcija (Then…):

* **Assign user from field Buyer Name, use user User as fallback**: Ako su navedeni uslovi ispunjeni (tj. postoji neslaganje u jediničnim cenama), faktura se automatski dodeljuje kupcu (ime navedeno u polju „Buyer Name“) na dalji pregled. Ako je polje „Buyer Name“ prazno ili nije navedeno, podrazumevani korisnik (verovatno administrator ili drugi određeni član osoblja) dodeljuje se kao rezervna opcija za obradu odobrenja.

#### Svrha ovog pravila:

* **Ensure Accuracy and Compliance**: Ovo pravilo je od ključnog značaja za obezbeđivanje da proces fakturisanja bude tačan i usklađen sa dogovorenim uslovima. Pokretanjem pregleda kada postoji neslaganje u jediničnim cenama, sistem pomaže u sprečavanju finansijskih grešaka ili potencijalne prevare.
* **Streamline Approvals**: Automatizacija dodeljivanja na pregled na osnovu određenih neslaganja pomaže u pojednostavljivanju procesa odobravanja i obezbeđuje da odgovarajuće osoblje brzo reši probleme.
* **Financial Oversight**: Zahtevanje drugog odobrenja, posebno na osnovu podudaranja cena, jača finansijske kontrole i odgovornost u okviru organizacije.
