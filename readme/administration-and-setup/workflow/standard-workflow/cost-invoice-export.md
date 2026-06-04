# Cost Invoice - Export

<figure><img src="../../../.gitbook/assets/Bildschirmfoto 2024-05-03 um 14.53.28 (1).png" alt=""><figcaption></figcaption></figure>

Ovaj naslov označava da je pravilo posebno konfigurisano za upravljanje fakturama troškova i uključuje akciju izvoza, moguće radi izveštavanja, dalje obrade ili integracije sa drugim sistemima.

#### Konfiguracija pravila:

1. **When…**
   * **Document Type is Invoice**: Ovaj uslov obezbeđuje da se pravilo pokreće samo za dokumente kategorizovane kao fakture, čime se održava specifičnost radnog toka za upravljanje fakturama.
2. **And…**
   * **Document Field Invoice Sub Type is Equals Cost Invoice**: Ovo određuje da se pravilo primenjuje samo na one fakture koje su izričito označene kao „Cost Invoices“ u određenom polju unutar dokumenta. Ovo pomaže u njihovom razlikovanju od drugih vrsta faktura.
   * **Document Status is Pending Second Approval**: Faktura mora biti u statusu „Pending Second Approval“. Ovo ukazuje na to da je faktura već prošla početno odobrenje i da čeka drugi, moguće konačni, pregled.

#### Akcija (Then…):

* **Start Export**: Kada faktura ispuni navedene uslove (da je faktura troškova i da čeka drugo odobrenje), izvršava se akcija „Start Export“. Ovo može uključivati slanje podataka fakture u drugi sistem radi finansijske analize, izveštavanja ili usklađenosti.

#### Svrha ovog pravila:

* **Workflow Efficiency**: Ovo pravilo pomaže u automatizaciji obrade faktura troškova obezbeđujući da prolaze kroz neophodne faze odobravanja bez ručne intervencije, povećavajući brzinu i tačnost finansijskih operacija.
* **Control and Compliance**: Zahtevanjem drugog odobrenja, sistem sprovodi mehanizam kontrole koji obezbeđuje da se fakture troškova temeljno pregledaju, poboljšavajući finansijski nadzor.
* **Integration and Reporting**: Akcija izvoza sugeriše da se, kada se fakture u potpunosti odobre, one mogu integrisati u druge sisteme radi dalje obrade ili analize, što je od ključnog značaja za finansijsko izveštavanje i revizije.

Ova vrsta pravila je od ključnog značaja za organizacije koje rade sa različitim vrstama faktura i koje moraju da obezbede da se svaka vrsta obrađuje prema određenim protokolima. Smanjuje rizik od grešaka i obezbeđuje usklađenost sa internim kontrolama i spoljnim propisima.
