# Send HTTPS Request

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova DocBits kartica je dizajnirana da olakša interakciju sa eksternim sistemima slanjem HTTPS zahteva na navedene URL-ove. Omogućava radnim tokovima da izvršavaju akcije kao što su preuzimanje, ažuriranje ili brisanje podataka pozivanjem API-ja, obezbeđujući neometanu integraciju sa eksternim servisima.

## **Funkcionalnost:**

* **Izvršavanje HTTPS zahteva:** Kartica šalje zahtev na navedeni URL koristeći konfigurisanu HTTP metodu (npr. GET, POST, PUT, DELETE).
* **Zaglavlja i parametri:** Korisnici mogu uključiti prilagođena zaglavlja i parametre upita kako bi obezbedili da zahtev ispunjava zahteve eksternog API-ja.
* **Podaci zahteva:** Omogućava korisnicima da definišu sadržaj podataka (ako je primenljivo) koji se šalje sa zahtevom, kao što su JSON ili podaci kodirani u formularu.
* **Procena odgovora:** Radni tok proverava da li se primljeni statusni kod poklapa sa očekivanom vrednošću, obezbeđujući uspešnu komunikaciju pre nastavka.
* **Podržane HTTP metode:**
  * GET: Preuzima podatke sa navedenog URL-a.
  * POST: Šalje podatke na navedeni URL radi kreiranja resursa.
  * PUT: Ažurira postojeće resurse na navedenom URL-u.
  * DELETE: Uklanja resurse sa navedenog URL-a.

## **Upotreba:**

Ova kartica je posebno korisna u scenarijima gde radni tokovi treba da komuniciraju sa eksternim API-jima radi razmene podataka, kao što su slanje ažuriranja CRM-u, preuzimanje statusa porudžbina ili objavljivanje novih unosa u bazu podataka.

## **Primer scenarija:**

* Korisnik konfiguriše karticu da pošalje POST zahtev eksternom sistemu za upravljanje porudžbinama sa sadržajem koji obuhvata detalje nove porudžbine. Prilagođena zaglavlja se dodaju da bi se uključili tokeni za autentifikaciju API-ja. Kartica je podešena da se nastavi samo ako je statusni kod odgovora 201 (Created). Ako se statusni kod razlikuje, radni tok pokreće obaveštenje o grešci za ručnu intervenciju.

Korišćenjem kartice "Send HTTPS Request", organizacije mogu automatizovati eksterne integracije, poboljšati komunikaciju između sistema i pojednostaviti složene radne tokove.
