# Change Status to

<figure><img src="../../../../.gitbook/assets/image (283).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Kartica radnog toka **"Change Status"** se koristi za promenu statusa dokumenta u jedno od unapred definisanih stanja — **Error, Rejected, Ready for Validation, Pending Approval, Pending Second Approval** — i opcionalno pokretanje povezanih radnih tokova na osnovu promene statusa. Ova kartica automatizuje proces ažuriranja statusa i pokretanja radnih tokova, obezbeđujući efikasno upravljanje dokumentima i rukovanje greškama.

## **Komponente kartice:**

1. **Status**
   * **Opis**: Navodi novi status koji se primenjuje na dokument.
   * **Opcije**:
     * **Error**: Označava da je dokument naišao na grešku.
     * **Rejected**: Ukazuje da je dokument odbijen i da neće ići dalje.
     * **Ready for Validation**: Postavlja dokument da bude pregledan i proveren od strane sledećeg korisnika ili sistemskog procesa.
     * **Pending Approval**: Postavlja dokument u stanje čekanja na odobrenje.
     * **Pending Second Approval**: Stavlja dokument na čekanje za drugi nivo odobrenja ako je primenljivo.
2. **Trigger Workflows**
   * **Opis**: Određuje da li bi bilo koji naredni radni tok trebalo pokrenuti nakon promene statusa.
   * **Opcije**:
     * **True**: Pokreće sve relevantne radne tokove na osnovu promene statusa.
     * **False**: Sprečava izvršavanje radnog toka nakon promene statusa.

## **Funkcionalnost:**

* **Procena uslova**: Sistem procenjuje uslove postavljene u odeljcima **"Where"** i **"And"**. Ako su ovi uslovi tačni, kartica nastavlja da promeni status dokumenta na izabranu vrednost.
* **Ažuriranje statusa**: Kada su uslovi zadovoljeni, status dokumenta se ažurira u jednu od unapred definisanih opcija (Error, Rejected, Ready for Validation, Pending Approval, Pending Second Approval), u zavisnosti od izbora korisnika.
* **Akcija pokretanja radnog toka**: Ako je **Trigger Workflows** postavljeno na **True**, sistem automatski pokreće sve povezane radne tokove nakon ažuriranja statusa. Ako je postavljeno na **False**, ne pokreću se dodatni radni tokovi, i proces se završava promenom statusa.

## **Podešavanje i konfiguracija:**

Da bi konfigurisali ovu karticu, korisnici treba da:

1. Navedu željeni **Status** na koji će dokument biti postavljen nakon procene uslova (Error, Rejected, Ready for Validation, Pending Approval ili Pending Second Approval).
2. Izaberu da li će **Trigger Workflows** nakon promene statusa izborom **True** ili **False**.
3. Kartica izvršava svoju akciju samo ako su oba uslova u odeljcima **"Where"** i **"And"** procenjena kao tačna.

## **Zaključak:**

Kartica radnog toka **"Change Status"** nudi pojednostavljen pristup upravljanju statusima dokumenata i pokretanju povezanih radnih tokova. Obezbeđuje da se dokumenti automatski usmeravaju na ispravan status i da se preduzimaju neophodne akcije, u zavisnosti od promene statusa. Postavljanjem jasnih uslova za izvršavanje, ona smanjuje ručni rad i poboljšava efikasnost radnog toka.
