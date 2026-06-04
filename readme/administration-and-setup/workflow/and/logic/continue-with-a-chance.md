# Continue with a chance

<figure><img src="../../../../.gitbook/assets/image (49).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova DocBits kartica uvodi probabilistički uslov, omogućavajući radnim tokovima da se nastave sa zadatom verovatnoćom. Kartica je korisna za testne scenarije, nasumične izbore ili kontrolisanu varijabilnost unutar procesa.

## **Funkcionalnost:**

* **Uslovni nastavak:** Ova kartica nastavlja radni tok na osnovu navedene verovatnoće, koju korisnik postavlja kao procentualnu vrednost. Kartica generiše nasumičan ishod i upoređuje ga sa datim procentom, stvarajući kontrolisanu šansu za nastavak radnog toka.
* **Procenat šanse:** Korisnici navode procentualnu vrednost (0-100%) koja predstavlja verovatnoću nastavka radnog toka. Na primer:
  * **0%:** Radni tok se nikada neće nastaviti.
  * **50%:** Radni tok ima 50/50 šansu da se nastavi.
  * **100%:** Radni tok će se uvek nastaviti.

## **Upotreba:**

Ova kartica je korisna u scenarijima gde su potrebne nasumične putanje radnog toka, kao što su A/B testiranje, kontrolisano uzorkovanje ili simulacija procesa. Takođe se može primeniti za dodavanje varijabilnosti u automatizovane radne tokove.

## **Primer scenarija:**

* Korisnik konfiguriše karticu sa **šansom od 30%**. Kada radni tok stigne do ove kartice, postoji 30% verovatnoće da će se radni tok nastaviti na sledeći korak. Ovo podešavanje je idealno za scenarije gde se želi nasumično uzorkovanje ili delimična obrada.

Korišćenjem kartice "Conditional Continuation", organizacije mogu uvesti kontrolisanu nasumičnost u radne tokove, olakšati eksperimente sa procesima i poboljšati donošenje odluka sa probabilističkim uslovima.
