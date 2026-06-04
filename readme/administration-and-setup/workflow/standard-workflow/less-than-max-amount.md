# Less than Max Amount

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.48.55 (1).png" alt=""><figcaption></figcaption></figure>

Ovaj naslov sugeriše da je pravilo ili uslov koji se podešava dizajniran za obradu faktura kod kojih je ukupan iznos manji ili jednak navedenom maksimalnom iznosu.

#### Konfiguracija pravila:

1. **When…**
   * **Document Type is Invoice**: Ovaj uslov proverava da li je dokument koji se obrađuje faktura. Ovo je ključno za obezbeđivanje da se pravilo primenjuje samo na fakture, a ne na druge vrste dokumenata.
2. **And…**
   * **Document Status is Pending Approval**: Ovo određuje da faktura mora biti u statusu „Pending Approval“. Ova provera statusa obezbeđuje da se pravilo primenjuje samo na fakture koje čekaju odobrenje.
   * **Compare two fields: Total Amount Less Or Equals Approver Max Amount**: Ovaj uslov upoređuje ukupan iznos fakture sa maksimalnim ovlašćenim iznosom odobravaoca. Ako je ukupan iznos fakture manji ili jednak ovom maksimalnom iznosu, pravilo se nastavlja na sledeći korak. Ovo verovatno uključuje nivo tolerancije koji dopušta manja odstupanja u okviru navedenih granica.

#### Akcija (Then…):

* **Assign user from field Approver Name, use user User as fallback**: Ako su navedeni uslovi ispunjeni, faktura se automatski dodeljuje odobravaocu čije je ime navedeno u polju. Ako je ovo polje prazno ili nedostupno, podrazumevani korisnik (verovatno administrator ili drugi određeni član osoblja) dodeljuje se kao rezervna opcija za obradu odobrenja.

#### Elementi interfejsa:

* **Add Card**: Ovo dugme verovatno omogućava korisnicima da dodaju više uslova ili akcija u pravilo, povećavajući fleksibilnost i specifičnost radnog toka.
* **Save**: Čuva konfigurisano pravilo u sistemu.

#### Svrha ovog pravila:

Ovo podešavanje je dizajnirano da pojednostavi proces odobravanja faktura automatskim usmeravanjem faktura odgovarajućem odobravaocu na osnovu iznosa i obezbeđivanjem da se samo one u okviru određenog praga obrađuju na ovaj automatizovan način. Pomaže u upravljanju finansijskim kontrolama i ubrzava radni tok smanjenjem ručnih provera za svaku fakturu.

\\
