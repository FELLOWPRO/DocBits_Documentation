# Document Status Condition List

<figure><img src="../../../../.gitbook/assets/userlmn_e9d6da331deceed4f330358635d6b605 (1).png" alt="" width="521"><figcaption></figcaption></figure>

**Svrha**

Ova kartica je dizajnirana da kontroliše akcije radnog toka na osnovu trenutnog statusa dokumenta, koristeći uslovnu logiku da pokrene ili ograniči određene procese. Obezbeđuje da dokumenti prolaze kroz radne tokove samo kada ispunjavaju unapred definisane statusne kriterijume.

**Komponente kartice**

1. **Operator**
   * **Opis**: Određuje kako će se status dokumenta procenjivati u odnosu na navedeni uslov.
   * **Opcije**:
     * **is**: Pokreće povezane akcije ako se trenutni status dokumenta poklapa sa jednim od navedenih statusa.
     * **is not**: Pokreće akcije ako se status dokumenta ne poklapa ni sa jednim od navedenih statusa.
2. **Status ( List )**
   * **Opis**: Navodi određene statuse sa kojima će se uporediti trenutni status dokumenta.
   * **Primeri**: "Error", "Export Error", "Ready in Validation", "Ready in Review", "Pending Approval", "Pending Second Approval". Oni predstavljaju različite faze ili stanja u kojima dokument može biti unutar procesa radnog toka.

**Funkcionalnost**

* **Identifikacija statusa**: Automatski identifikuje trenutni status dokumenta dok se kreće kroz radni tok ERP sistema.
* **Procena uslova**: Primenjuje izabrani operator (is ili is not) na status dokumenta u poređenju sa navedenim statusima:
  * Ako je **is**, proverava da li se status dokumenta poklapa sa bilo kojim statusom u listi.
  * Ako je **is not**, proverava da li se status dokumenta ne pojavljuje u listi.
* **Izvršavanje akcije**: U zavisnosti od ishoda procene uslova:
  * **True**: Izvršava unapred definisane akcije ili radne tokove ako je uslov ispunjen.
  * **False**: Preskače ili pokreće alternativne radne tokove ako uslov nije ispunjen.
* **Integracija radnog toka**: Neometano se integriše sa drugim komponentama radnog toka, obezbeđujući da rukovanje dokumentima bude koordinisano u celom sistemu.

**Korisničke interakcije**

* **Podešavanje i konfiguracija**: Korisnici konfigurišu karticu izborom operatora i navođenjem relevantnih statusa. Ovo podešavanje može uključivati jednostavne padajuće menije ili polja za potvrdu za izbor statusa i operatora.
* **Praćenje i upravljanje**: Korisnici mogu pratiti aktivnost kartice preko kontrolne table, koja pruža uvid u statusne uslove koji se prate i akcije koje se preduzimaju na osnovu tih uslova.
* **Rukovanje greškama i upozorenja**: Podržava postavljanje upozorenja za neuspehe procesa ili nepodudaranja u očekivanim statusima dokumenata, omogućavajući brze odgovore na operativne probleme.

#### Zaključak

Kartica radnog toka "Document Status Condition" je od vitalnog značaja za obezbeđivanje da se dokumenti ispravno obrađuju u skladu sa svojim trenutnim statusom, poboljšavajući kontrolu i efikasnost unutar ERP sistema. Jasno dokumentovanje ove kartice u priručniku sistema pomoći će korisnicima da je efikasno implementiraju i njome upravljaju, koristeći njenu funkcionalnost za održavanje neometanih i usklađenih radnih tokova dokumenata. Ova kartica je posebno korisna u upravljanju životnim ciklusima dokumenata i obezbeđivanju da samo dokumenti koji ispunjavaju određene kriterijume napreduju u naredne faze poslovnih procesa.
