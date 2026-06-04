# Start Export

<figure><img src="../../../../.gitbook/assets/image (285).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Kartica radnog toka **"Start Export"** je dizajnirana da pokrene proces izvoza dokumenta. Ova kartica funkcioniše kao okidač unutar radnog toka da neometano pokrene operaciju izvoza kada su uslovi u prethodnim odeljcima zadovoljeni.

## **Komponente kartice:**

1. **Action**
   1. **Opis**: Pokreće proces izvoza dokumenta.
   2. **Detalj**: Kartica koristi konfigurisana podešavanja izvoza u sistemu za obradu i izvoz dokumenta.

## **Funkcionalnost:**

* **Procena uslova**: Sistem procenjuje uslove postavljene u odeljcima **"Where"** i **"And"** radnog toka. Ako su svi uslovi tačni, proces izvoza počinje.
* **Izvoz dokumenta**: Dokument se obrađuje i izvozi korišćenjem podrazumevane ili prethodno definisane konfiguracije izvoza.

## **Podešavanje i konfiguracija:**

Ova kartica ne zahteva posebnu konfiguraciju jer koristi podešavanja izvoza već definisana u sistemu. Korisnici treba da obezbede da:

1. Uslovi u odeljcima **"Where"** i **"And"** budu ispravno konfigurisani, jer se kartica izvršava samo ako se ovi uslovi procene kao tačni.
2. Validna konfiguracija izvoza bude povezana sa dokumentom u sistemu.

## **Zaključak:**

Kartica radnog toka **"Start Export"** pruža pojednostavljen i automatizovan način za pokretanje procesa izvoza. Oslanjajući se na unapred konfigurisana podešavanja i uslovne procene, ona obezbeđuje efikasnu i tačnu obradu dokumenata.
