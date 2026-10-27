# AI Calculation for Cost Increase Surcharges

<figure><img src="../../../../.gitbook/assets/image (309).png" alt="" width="563"><figcaption></figcaption></figure>

## Kada koristiti ovu karticu

Koristite ovu akciju da zatražite konfigurisani MTZ/ETZ obračun doplate za materijal i energiju za trenutni dokument. Prvo pripremite podatke dokumenta i konfiguraciju servisa za obračun koji su potrebni vašoj organizaciji.

## Stvarna konfiguracija

Prikazana kartica nema unose Cost Increase Factor, Base Cost Field ili Surcharge Field. Ona delegira obračun konfigurisanom servisu. Ne tražite ove nepostojeće kontrole kartice i ne pretpostavljajte fiksnu procentnu formulu na osnovu naziva kartice.

## Rezultat i provera

Uspešan odgovor servisa označava karticu kao uspešnu. Istek vremena (timeout) ili neuspešan odgovor proizvodi grešku kartice. Proverite log kartice i rezultujuće podatke o doplati u dokumentu; sam uspeh poziva ne dokumentuje određeni iznos.

U režimu testiranja kartice poziv se preskače i uspeh se simulira. Ovo je korisno za testiranje strukture radnog toka, ali ne dokazuje da je servis pokrenut niti da je doplata izračunata.

<!-- workflow-card-practical-example-20261021 -->

## Praktičan primer

**Kada koristiti:** Zatražite konfigurisani obračun doplate za materijal/energiju za pripremljenu fakturu.

**Konfiguracija:** Koristite sintetičku fakturu `DEMO-001` sa podacima koje zahteva vaš konfigurisani MTZ/ETZ servis. Dodajte ovu akciju nakon uslova validacije dokumenta.

**Očekivani rezultat i kontraprimer:** Uspešan odgovor servisa označava karticu kao uspešnu; istek vremena ili neuspešan odgovor proizvodi grešku kartice. Proverite polja dokumenta i rezultat obračuna zasebno. Režim testiranja kartice simulira uspeh i ne poziva servis, pa ne može dokazati stvaran rezultat doplate.

Ovo je ilustrativna konfiguracija i očekivani ishod. Koristite polja, korisnike i grupe konfigurisane u vašoj test organizaciji; ovo nije tvrdnja da je primer izvršen.
