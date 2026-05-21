# Mapa Sajta

Mapa Sajta je kompletan, pretraživ indeks svega što DocBits nudi — svaka stranica, dijalog, stavka bočne trake, akcija i funkcija unutar stranice, grupisano po kategorijama. To je duža dopuna [Globalne Brze Pretrage](global-quick-search.md).

## Kako pristupiti

Otvorite Mapu Sajta iz bočne trake (stavka pri dnu) ili pritisnite <kbd>Cmd</kbd>/<kbd>Ctrl</kbd> + <kbd>K</kbd> i izaberite **Pogledaj sve rezultate**. Direktna URL adresa je `/sitemap`.

<figure><img src="../../.gitbook/assets/sitemap-overview.png" alt="Pregled Mape Sajta"><figcaption><p>Mapa Sajta sa pregledom kategorija i zaglavljem za pretragu.</p></figcaption></figure>

## Pregledanje kataloga

Mapa Sajta je grupisana u kategorije koje odražavaju strukturu aplikacije — Podešavanja, Obrada dokumenata, Workflow, Validacija i tako dalje. Svaka kategorija prvo navodi svoje stranice, a zatim funkcije unutar stranica grupisane po podkategorijama.

Stavke su obojene prema tipu:

* **Stranica** — kompletna ruta za navigaciju.
* **Dijalog** — modal koji se otvara iz drugog dela aplikacije.
* **Bočna traka / Panel / Meni** — navigaciona ili kontekstualna površina.
* **Akcija** — dugme ili prečica koja izvršava nešto bez navigacije.

Kliknite na bilo koju stavku da skočite direktno na nju. Stavke koje zahtevaju parametar (kao što su tip dokumenta ili ID) uključuju ugrađeni selektor — izaberite vrednost pre nego što kliknete.

## Pretraga i filteri

Zalepljeno zaglavlje na vrhu sadrži polje za pretragu i filter-pilule. Unesite nekoliko znakova da uživo filtrirate listu po nazivu i opisu. Koristite pilule tipova da suzite na jedan tip stavke — na primer samo **Dijalog**.

Trenutna pretraga i filter dodaju se URL-u, tako da se filtrirani prikaz može sačuvati kao oznaka ili podeliti.

<mark>Mapa Sajta poštuje iste dozvole kao i ostatak DocBits-a. Stranice kojima ne možete da pristupite ne pojavljuju se.</mark>

## Režim za programere

Prekidač **Korisnik / Dev** u zaglavlju uključuje dodatne informacije za partner-programere:

* Internu rutu svake stavke.
* Oznake parametara (`:docType`, `:docId`, ključeve dubokih linkova).

Režim za programere pamti se u vašem pregledaču. Prebacite se nazad u režim Korisnik za uobičajeni prikaz.

## Nazad na vrh

Mapa Sajta je duga. Kada prevučete preko prvog ekrana, dugme Nazad na vrh pojavljuje se u donjem desnom uglu.
