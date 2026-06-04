# Run Workflow

<figure><img src="../../../../.gitbook/assets/image (307).png" alt="" width="563"><figcaption></figcaption></figure>

## Svrha:

Kartica **"Run Workflow"** omogućava korisnicima da dinamično izvrše izabrani radni tok iz liste dostupnih radnih tokova. Ova kartica je korisna za automatizaciju procesa gde je više radnih tokova međusobno povezano, omogućavajući pojednostavljeno poslovanje.

## Komponente kartice:

1. **Workflow**
   * **Opis:** Navodi radni tok koji treba izvršiti kada se uslovi procene kao tačni.
   * **Detalj:** Za izbor je dostupna padajuća lista svih dostupnih radnih tokova.

## Funkcionalnost:

* **Procena uslova:** Kartica izvršava izabrani radni tok samo ako se oba odeljka, **"Where"** i **"And"**, procene kao tačna.
  * Ako je bilo koji uslov netačan, ne preduzima se nikakva akcija, i radni tok ostaje nepokrenut.
* **Izvršavanje radnog toka:**
  * Kada su uslovi ispunjeni, navedeni radni tok se pokreće automatski.
  * Ako uslovi nisu ispunjeni, nijedan radni tok se ne izvršava.

## Podešavanje i konfiguracija:

1. **Izbor radnog toka:** Izaberite radni tok koji treba pokrenuti iz **padajuće liste** dostupnih radnih tokova.
2. **Definisanje uslova:** Konfigurišite odeljke **"Where"** i **"And"** da navedete kriterijume koji moraju biti ispunjeni da bi se radni tok izvršio.

## Zaključak:

Kartica **"Run Workflow"** nudi pogodan i efikasan način za povezivanje radnih tokova, automatizujući višefazne procese sa lakoćom. Obezbeđivanjem da su uslovi u odeljcima **"Where"** i **"And"** ispunjeni, korisnici mogu dinamično izvršavati radne tokove i smanjiti ručnu intervenciju.
