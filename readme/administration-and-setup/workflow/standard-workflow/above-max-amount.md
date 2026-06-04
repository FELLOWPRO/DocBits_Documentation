# Above Max Amount

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.51.42 (1).png" alt=""><figcaption></figcaption></figure>

Ovaj naslov označava da je pravilo dizajnirano za upravljanje slučajevima u kojima ukupan iznos fakture prelazi maksimalan iznos koji je odobravalac ovlašćen da obradi.

#### Konfiguracija pravila:

1. **When…**
   * **Document Type is Invoice**: Ovaj uslov obezbeđuje da se pravilo primenjuje samo na fakture, što je od suštinskog značaja za pravilno usmeravanje radnog toka.
2. **And…**
   * **Document Status is Pending Approval**: Faktura mora biti u statusu „Pending Approval“. Ovaj status je ključan da bi se obezbedilo da se pravilo primenjuje na fakture koje su još uvek u obradi i koje još nisu finalizovane.
   * **Compare two fields: Total Amount Greater Than Approver Max Amount**: Ovaj uslov proverava da li ukupan iznos fakture prelazi maksimalan iznos koji je odobravaocu dozvoljeno da obradi. Ovo poređenje može uključivati i podešavanje tolerancije, dopuštajući manje varijacije na osnovu unapred definisanih kriterijuma.

#### Akcija (Then…):

* **Assign user from field Next Level Approver, use user User as fallback**: Ako faktura prelazi navedeni maksimalan iznos, automatski se dodeljuje odobravaocu višeg nivoa, naznačenom u polju „Next Level Approver“. Ako ovo polje nije popunjeno ili navedeni korisnik nije dostupan, podrazumevani korisnik (verovatno administrator ili drugi određeni član osoblja) koristi se kao rezervna opcija kako bi se obezbedilo da faktura bude pregledana bez odlaganja.

#### Elementi interfejsa:

* **Add Card**: Ova opcija omogućava dodavanje dodatnih uslova ili akcija u pravilo, pružajući fleksibilnost za rešavanje složenih scenarija.
* **Save**: Ovo dugme čuva konfiguraciju pravila u sistemu.

#### Svrha ovog pravila:

Svrha ovog pravila je da se obezbedi da fakture koje prelaze određene finansijske pragove pregledaju odobravaoci sa odgovarajućim nivoima ovlašćenja. Ovo pomaže u održavanju finansijske kontrole i nadzora, obezbeđujući da troškove pregledaju osobe sa potrebnim limitima odobrenja, čime se organizacija štiti od neovlašćenih ili neprimerenih troškova.

Ovo pravilo, kao i prethodno, pomaže u automatizaciji radnog toka, smanjujući ručni rad i poboljšavajući usklađenost sa finansijskim politikama organizacije. To je primer kako se automatizacija radnog toka može efikasno koristiti za upravljanje složenim finansijskim procesima u okviru kompanije.
