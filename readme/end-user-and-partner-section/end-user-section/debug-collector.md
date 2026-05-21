# Debug Collector

Debug Collector beleži kompletan snimak vaše DocBits sesije — mrežnu aktivnost, greške, okruženje pregledača i metrike performansi — pakuje ih kao JSON izveštaj i opcionalno otvara tiket podrške direktno iz istog prozora.

## Kako pristupiti

Pritisnite <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> na Windows-u i Linuxu, ili <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> na macOS-u. Prozor Performance Report se otvara odmah.

<figure><img src="../../.gitbook/assets/debug-collector-dialog.png" alt="Debug Collector prozor"><figcaption><p>Prozor Performance Report prikazuje snimak i ugrađenu formu za kreiranje tiketa.</p></figcaption></figure>

## Šta se beleži

* **API pozivi** — poslednjih 60 REST i WebSocket poziva, sa vremenima, statusnim kodovima i URL-ovima. Pozivi duži od dve sekunde označeni su posebno.
* **Greške** — nedavne JavaScript greške i nepohvatana odbacivanja obećanja iz konzole pregledača.
* **Konzolni logovi** — najnoviji log zapisi aplikacije.
* **Okruženje** — verzija pregledača, operativni sistem, veličina ekrana i aktivne zastavice funkcija.
* **Kontekst korisnika** — vaša uloga, organizacija i stranica na kojoj ste bili kada je snimak napravljen.
* **Metrike performansi** — vremena učitavanja stranice (LCP, FCP), upotreba memorije i veličina DOM-a.
* **Trace ID-jevi** — identifikatori korelacije koji povezuju snimak sa zapisima na pozadini.

## Kreiranje tiketa podrške iz prozora

Ne morate ručno ništa preuzimati ili prilagati — prozor sadrži ugrađenu formu **Create Support Ticket**.

1. Unesite svoj e-mail, ostavite predloženu temu ili je zamenite, izaberite prioritet i dodajte beleške koje opisuju šta ste radili kada se problem pojavio.
2. Kliknite na **Send Report**. JSON snimak se prilaže, a tiket kreira u jednom koraku.

To je sve — podrška dobija tiket sa svim podacima potrebnim za reprodukovanje slučaja.

Ako želite lokalnu kopiju snimka, koristite **Copy Debug Data** da kopirate JSON u privremenu memoriju ili Sačuvaj kao iz pregledača da zadržite izveštaj kao `.json` fajl.

## Privatnost i rukovanje podacima

* Tokeni autentifikacije i osetljiva zaglavlja maskiraju se iz snimljenih API poziva pre nego što se snimak napravi.
* Ništa ne napušta vaš pregledač dok ne kliknete na **Send Report** — prečica samo otvara prozor.

<mark>Pregledajte snimak pre slanja ako ste radili sa dokumentima koji sadrže podatke klijenata. ID-jevi dokumenata vidljivi u URL-ovima pojaviće se u izveštaju.</mark>
