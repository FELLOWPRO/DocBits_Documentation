# AI Calculation for Cost Increase Surcharges

<figure><img src="../../../../.gitbook/assets/image (309).png" alt="" width="563"><figcaption></figcaption></figure>

## Svrha:

Kartica radnog toka **"AI Calculation for Cost Increase Surcharges"** koristi AI za automatsko izračunavanje iznosa doplata na osnovu povećanja troškova. Obezbeđuje dosledne i tačne obračune doplata, pojednostavljujući radne tokove i smanjujući ručni rad.

## Komponente kartice:

* **Cost Increase Factor**
  * **Opis:** Množilac ili procenat koji se primenjuje na osnovni trošak za izračunavanje doplate.
  * **Detalj:** Određuje iznos doplate na osnovu povećanja troškova (npr. faktor 1.10 za povećanje od 10%).
* **Base Cost Field**
  * **Opis:** Polje koje sadrži originalnu vrednost troška koja se koristi kao osnova za obračun doplate.
  * **Detalj:** Bira se automatski ili se definiše unutar radnog toka radi reference tokom obračuna.
* **Surcharge Field**
  * **Opis:** Polje u kojem se čuva vrednost doplate izračunata pomoću AI.
  * **Detalj:** Ovo polje odražava izračunatu doplatu, čineći je dostupnom za dalju obradu ili izveštavanje.

## Funkcionalnost:

**Procena uslova:**

* Kartica se aktivira samo ako se uslovi u oba odeljka, **"Where"** i **"And"**, procene kao tačni.
* Ako se bilo koji uslov proceni kao netačan, ne vrši se nikakav obračun doplate.

**Obračun vođen AI:**

* Sistem primenjuje **Cost Increase Factor** na **Base Cost Field** da izračuna doplatu.
* Rezultat se čuva u **Surcharge Field**, obezbeđujući dostupnost za naredne korake radnog toka.

## Zaključak:

Kartica radnog toka **"AI Calculation for Cost Increase Surcharges"** automatizuje primenu doplata na osnovu povećanja troškova. Korišćenjem AI za preciznost i doslednost, ova kartica eliminiše ručne obračune, poboljšava efikasnost i podržava tačno upravljanje troškovima u automatizovanim radnim tokovima.
