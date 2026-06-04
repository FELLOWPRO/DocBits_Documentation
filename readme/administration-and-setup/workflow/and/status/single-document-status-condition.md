# Single Document Status Condition

<figure><img src="../../../../.gitbook/assets/userlmn_928e514bc0e2aa775894e4ec5f992bd9 (1).png" alt="" width="528"><figcaption></figcaption></figure>

**Svrha**

Ova kartica radnog toka je prilagođena za upravljanje operacijama nad dokumentima na osnovu jednog, navedenog statusa dokumenta. Pojednostavljivanjem uslova na jedan status, kartica je fokusirana na vrlo specifične okidače radnog toka, što je čini idealnom za ciljane aktivnosti obrade dokumenata unutar ERP sistema.

**Komponente kartice**

1. **Operator**
   * **Opis**: Navodi metod za procenu statusa dokumenta u odnosu na izabrani uslov.
   * **Opcije**:
     * **is**: Pokreće operaciju ako se trenutni status dokumenta poklapa sa izabranim statusom.
     * **is not**: Pokreće operaciju ako se trenutni status dokumenta ne poklapa sa izabranim statusom.
2. **Status**
   * **Opis**: Omogućava izbor jednog statusa dokumenta za postavljanje uslova.
   * **Primeri statusa**: "Error", "Export Error", "Ready in Validation", "Ready in Review", "Pending Approval", "Pending Second Approval".
   * **Detalj**: Korisnici biraju jedan status iz padajuće liste ili skupa radio dugmadi. Ovaj status zatim služi kao kriterijum za operaciju kartice.

**Funkcionalnost**

* **Identifikacija statusa dokumenta**: Identifikuje trenutni status dokumenta dok se obrađuje kroz ERP sistem.
* **Procena uslova**:
  * Na osnovu izabranog operatora (`is` ili `is not`), kartica proverava da li je trenutni status dokumenta usklađen sa izabranim statusnim kriterijumom.
* **Izvršavanje akcije**:
  * **Tačan uslov**: Ako se status poklapa (ili ne poklapa, na osnovu operatora), pokreće se odgovarajuća akcija. Ovo može biti usmeravanje na dalju obradu, generisanje obaveštenja ili drugi unapred definisani radni tokovi.
  * **Netačan uslov**: Ako uslov nije ispunjen, ne preduzima se nikakva akcija, ili se pokreće alternativna putanja.
* **Integracija sa drugim radnim tokovima**: Iako je dizajnirana za procenu jednog statusa, ova kartica se može efikasno integrisati u šire sekvence radnih tokova radi obezbeđivanja preciznog rukovanja dokumentima.

**Korisničke interakcije**

* **Podešavanje i konfiguracija**: Korisnici podešavaju karticu izborom operatora i zatim izborom jednog statusa iz dostupnih opcija. Ovaj proces izbora je jednostavan i dizajniran da spreči zabunu.
* **Praćenje i izveštavanje**: Omogućava praćenje preko izveštaja ili kontrolnih tabli koje generiše sistem, a koji prate obradu dokumenata na osnovu njihovog statusa, pomažući u nadzoru efikasnosti implementiranih radnih tokova.
* **Rukovanje greškama i obaveštenja**: Može se konfigurisati da upozorava korisnike na bilo kakve anomalije u obradi ili da označi dokumente koji ne ispunjavaju postavljene uslove, obezbeđujući brzu pažnju i rešavanje.

#### Zaključak

Kartica radnog toka "Single Document Status Condition" pojednostavljuje upravljanje dokumentima fokusiranjem na pojedinačne statusne uslove. Ova specifikacija pomaže u slučajevima gde je neophodna precizna kontrola nad tokovima dokumenata, posebno u okruženjima sa strogim kriterijumima obrade. Jasno dokumentovanje ove verzije kartice obezbediće da korisnici u potpunosti razumeju njenu primenu i da je mogu efikasno integrisati u svoje svakodnevno poslovanje, poboljšavajući i usklađenost i efikasnost u obradi dokumenata.
