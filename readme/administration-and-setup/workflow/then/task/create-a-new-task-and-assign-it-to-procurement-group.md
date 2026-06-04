# Create a New Task and assign it to Procurement Group

<figure><img src="../../../../.gitbook/assets/image (292).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Kartica radnog toka **"Create Task for Procurement Group"** kreira novi zadatak koji se dinamično dodeljuje nabavnoj grupi navedenoj u konfiguraciji. Ovaj zadatak se može dodeliti sa različitim nivoima prioriteta, a opciono obaveštenje putem e-pošte se može poslati da informiše grupu o zadatku. Ova kartica obezbeđuje da pravi tim bude upozoren na osnovu uslova radnog toka.

## **Komponente kartice:**

1. **Title**
   * **Opis:** Navodi naslov zadatka.
   * **Detalj:** Ovo polje identifikuje zadatak koji se kreira, pružajući sažet naslov za lako prepoznavanje.
2. **Description**
   * **Opis:** Pruža dodatne detalje o zadatku.
   * **Detalj:** Ovo polje se koristi za opisivanje cilja zadatka i bilo kog neophodnog konteksta ili uputstava.
3. **Priority**
   * **Opis:** Definiše hitnost zadatka.
   * **Opcije:**
     * **High:** Zadatak zahteva neposrednu pažnju.
     * **Medium:** Zadatak je važan ali ne hitan.
     * **Low:** Zadatak se može rešiti kasnije.
4. **Group Name**
   * **Opis:** Navodi nabavnu grupu kojoj će zadatak biti dodeljen.
   * **Detalj:** Ovo polje označava nabavnu grupu odgovornu za zadatak. Obezbeđuje da zadatak bude usmeren pravom timu.
5. **Email Notification**
   * **Opis:** Konfiguriše da li obaveštenje putem e-pošte treba poslati dodeljenoj nabavnoj grupi.
   * **Opcije:**
     * **True:** Šalje obaveštenje putem e-pošte nabavnoj grupi.
     * **False:** Ne šalje se obaveštenje putem e-pošte.

## **Funkcionalnost:**

* **Procena uslova:**\
  Kartica izvršava svoju akciju samo ako se oba odeljka, **"Where"** i **"And"**, procene kao tačna.
* **Kreiranje zadatka:**\
  Kartica kreira novi zadatak, dodeljujući ga nabavnoj grupi definisanoj u polju "Group Name". Ovaj zadatak će uključivati navedeni naslov, opis i nivo prioriteta.
* **Obaveštenje putem e-pošte:**\
  Ako je opcija obaveštenja putem e-pošte postavljena na true, e-pošta se šalje nabavnoj grupi koja je informiše o zadatku.

## **Podešavanje i konfiguracija:**

* **Definisanje detalja zadatka:**\
  Unesite naslov, opis i nivo prioriteta zadatka.
* **Izbor nabavne grupe:**\
  Izaberite nabavnu grupu koja će biti odgovorna za zadatak.
* **Omogućavanje obaveštenja putem e-pošte:**\
  Navedite da li obaveštenje putem e-pošte treba poslati grupi prilikom kreiranja zadatka.

## **Zaključak:**

Kartica radnog toka "Create Task for Procurement Group" obezbeđuje da se zadaci automatski dodeljuju odgovarajućoj nabavnoj grupi sa definisanim prioritetima. Ova kartica takođe može obavestiti grupu putem e-pošte kako bi se obezbedilo da se zadaci reše bez odlaganja, poboljšavajući efikasnost radnog toka i upravljanje zadacima.
