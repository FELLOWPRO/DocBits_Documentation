# Invert Checkbox

<figure><img src="../../../../.gitbook/assets/image (280).png" alt=""><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica radnog toka je dizajnirana da invertuje trenutno stanje polja za potvrdu. Ako je polje za potvrdu označeno (true), biće odznačeno (false), i obrnuto. Inverzija se dešava na osnovu uslova postavljenih u odeljcima **"Where"** i **"And"**. Ova kartica pomaže u automatizaciji radnih tokova gde uslov zahteva prebacivanje polja za potvrdu na osnovu određenih kriterijuma.

## **Komponente kartice:**

1. **Field Name**
   * **Opis**: Navodi polje za potvrdu koje treba invertovati.&#x20;
   * **Detalj**: Izabranom polju za potvrdu će se stanje prebaciti iz true u false ili iz false u true na osnovu njegovog trenutnog stanja.

## **Funkcionalnost:**

* **Procena uslova**: Sistem procenjuje uslove definisane u odeljcima **"Where"** i **"And"**:
  * Ako su **oba uslova tačna**, izvršiće se akcija iz odeljka **"Then"**, što u ovom slučaju znači da će se polje za potvrdu prebaciti.
  * Ako je **bilo koji uslov netačan**, kartica se neće izvršiti i neće biti izvršena nikakva promena polja za potvrdu.
* **Izvršavanje akcije**: Ako se uslovi u odeljcima **"Where"** i **"And"** procene kao tačni, stanje polja za potvrdu će biti invertovano:
  * Ako je polje za potvrdu označeno (true), biće odznačeno (false).
  * Ako je polje za potvrdu odznačeno (false), biće označeno (true).

## **Podešavanje i konfiguracija:**

Da bi konfigurisali ovu karticu, korisnici treba da:

1. **Izaberu polje za potvrdu** (Field Name) koje će biti invertovano. Dostupna polja za potvrdu u dokumentu su navedena za izbor.
2. Polje za potvrdu će biti invertovano samo ako su uslovi u oba odeljka, **"Where"** i **"And"**, tačni.

## **Zaključak:**

Kartica radnog toka **"Invert checkbox \[Field Name]"** nudi jednostavan ali moćan alat za automatizaciju prebacivanja vrednosti polja za potvrdu na osnovu određenih uslova. Smanjivanjem potrebe za ručnim podešavanjima polja za potvrdu, ova kartica poboljšava efikasnost u obradi dokumenata i obezbeđuje doslednost u radnim tokovima.
