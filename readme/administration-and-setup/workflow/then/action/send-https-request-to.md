# Send HTTPS request to

<figure><img src="../../../../.gitbook/assets/Then_Send_HTTPS_1.png" alt="" width="563"><figcaption></figcaption></figure>

## Svrha:

Kartica radnog toka **"Send HTTPS Request"** omogućava korisnicima da šalju HTTPS zahteve navedenom URL-u sa prilagodljivim zaglavljima, parametrima i sadržajem podataka. Ova kartica je idealna za integraciju eksternih API-ja ili veb servisa direktno u radni tok.

## Komponente kartice:

1. **URL**
   * **Opis:** Navodi krajnju tačku na koju će se poslati HTTPS zahtev.
   * **Detalj:** Unesite potpuni URL API-ja ili veb servisa za povezivanje.
2. **Headers**
   * **Opis:** Definiše zaglavlja koja se uključuju u HTTPS zahtev.
   * **Detalj:** Navedite **parove ključ-vrednost** u **validnom JSON formatu** da biste naveli zaglavlja kao što su tokeni za autentifikaciju ili tipovi sadržaja. Primer: {"Authorization": "Bearer example\_value"}
3. **Method**
   * **Opis:** Navodi HTTP metodu koja se koristi za zahtev.
   * **Opcije:**
     * **GET:** Preuzima podatke sa krajnje tačke.
     * **POST:** Šalje podatke krajnjoj tački radi kreiranja ili ažuriranja resursa.
     * **PUT:** Ažurira postojeće resurse na krajnjoj tački.
     * **DELETE:** Uklanja resurse sa krajnje tačke.
4. **Parameters**
   * **Opis:** Parovi ključ-vrednost koji se uključuju u URL kao parametri upita.
   * **Detalj:** Koristite ovo za slanje filtera ili dodatnih podataka koje zahteva krajnja tačka u validnom JSON formatu. Pogledajte primer za Headers.
5. **Data**
   * **Opis:** Telo HTTPS zahteva.
   * **Detalj:** Navedite sadržaj u validnom JSON formatu. Pogledajte primer za Headers.

## Funkcionalnost:

* **Procena uslova:** Kartica šalje HTTPS zahtev samo ako se oba odeljka, **"Where"** i **"And"**, procene kao tačna.&#x20;
  * Ako je bilo koji uslov netačan, zahtev se ne šalje.
* **Izvršavanje zahteva:**
  * Kada su uslovi ispunjeni, sistem šalje HTTPS zahtev sa navedenim konfiguracijama.

## Podešavanje i konfiguracija:

1. **Definisanje URL-a:** Unesite krajnju tačku na koju treba poslati HTTPS zahtev.
2. **Postavljanje zaglavlja:** Navedite potrebna zaglavlja kao parove ključ-vrednost.
3. **Izbor HTTP metode:** Izaberite odgovarajuću metodu (**GET**, **POST**, **PUT** ili **DELETE**) na osnovu akcije koju treba izvršiti.
4. **Dodavanje parametara:** Navedite sve parametre upita koje zahteva krajnja tačka.
5. **Navođenje sadržaja podataka:** Unesite telo zahteva u traženom formatu (npr. JSON) ako je potrebno.
6. **Konfiguracija uslova:** Definišite odeljke **"Where"** i **"And"** da biste obezbedili da se zahtev šalje samo kada su određeni uslovi ispunjeni.

## Primer kartice:

<figure><img src="../../../../.gitbook/assets/Then_Send_HTTPS_2.png" alt="" width="375"><figcaption></figcaption></figure>

## Zaključak:

Kartica radnog toka **"Send HTTPS Request"** pojednostavljuje API integraciju omogućavajući korisnicima da upućuju prilagođene zahteve eksternim servisima direktno iz svojih radnih tokova. Automatizacijom procesa slanja HTTPS zahteva i upravljanja odgovorima, ova kartica poboljšava fleksibilnost i funkcionalnost radnog toka.
