# Export with Export Configuration

<figure><img src="../../../../.gitbook/assets/image (284).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Kartica radnog toka **"Export Document with Export Configuration"** je dizajnirana da izveze dokument korišćenjem navedene konfiguracije izvoza. Pruža fleksibilnost da se zanemare svi zadaci na čekanju povezani sa dokumentom, obezbeđujući neometan proces izvoza bez obzira na njegovo trenutno stanje.

## **Komponente kartice:**

1. **Export Configuration**
   * **Opis**: Navodi konfiguraciju izvoza koja se koristi za obradu dokumenta.
   * **Detalj**: Ova konfiguracija određuje format, strukturu i odredište izvezenog dokumenta.
2. **Ignore Pending Tasks**
   * **Opis**: Određuje da li zadatke na čekanju povezane sa dokumentom treba zanemariti tokom procesa izvoza.
   * **Opcije**:
     * **True**: Izvozi dokument bez obzira na zadatke na čekanju.
     * **False**: Obezbeđuje da se zadaci na čekanju završe pre izvoza.

## **Funkcionalnost:**

* **Procena uslova**: Sistem procenjuje uslove postavljene u odeljcima **"Where"** i **"And"** radnog toka. Ako su oba uslova tačna, proces izvoza se pokreće.
* **Izvoz dokumenta**: Korišćenjem navedene **Export Configuration**, dokument se obrađuje i izvozi u definisanom formatu i odredištu.
* **Rukovanje zadacima na čekanju**: Ako je **Ignore Pending Tasks** postavljeno na **True**, proces izvoza zaobilazi sve neizvršene zadatke povezane sa dokumentom. Ako je postavljeno na **False**, izvoz se odlaže dok se svi zadaci ne reše.

## **Podešavanje i konfiguracija:**

Da bi konfigurisali ovu karticu, korisnici treba da:

1. Izaberu željenu **Export Configuration** da definišu kako će dokument biti izvezen.
2. Izaberu da li će **Ignore Pending Tasks** postavljanjem vrednosti na **True** ili **False**.
3. Obezbede da su uslovi u odeljcima **"Where"** i **"And"** ispravno postavljeni, jer kartica izvršava svoju akciju samo kada su ovi uslovi tačni.

## **Zaključak:**

Kartica radnog toka **"Export Document with Export Configuration"** obezbeđuje da se dokumenti izvoze efikasno i u skladu sa unapred definisanim konfiguracijama. Sa mogućnošću zanemarivanja zadataka na čekanju, ova kartica nudi fleksibilnost u rukovanju dokumentima u različitim fazama, smanjujući kašnjenja i pojednostavljujući proces izvoza.
