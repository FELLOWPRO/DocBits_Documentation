# Elektronski dokumenti

DocBits validira dolazne elektronske fakture (e-fakture) u odnosu na zvanične standarde — **XRechnung**, **ZUGFeRD** i **Factur-X** — i usmerava sve pronađene probleme do odgovarajućeg obrađivača. Grupa podešavanja **Elektronski dokumenti** (u okviru **Obrada dokumenata**) ima dve stranice:

* **[Pravila validacije](validation-rules.md)** — izaberite koje verzije i profile e-faktura prihvatate i podesite ozbiljnost svakog pravila validacije za svoju organizaciju.
* **[Rutiranje obaveštenja](notification-routing.md)** — povežite nalaze validacije sa AI Workforce agentom koji treba da ih obradi.

Zajedno vam omogućavaju da odlučite **šta se smatra problemom** na dolaznoj e-fakturi i **ko se time bavi**.

## Omogućavanje ili onemogućavanje validacije e-faktura

Dve stranice Elektronski dokumenti stupaju na snagu tek kada je **validacija e-faktura uključena za tip dokumenta**. Prekidač se nalazi na samom tipu dokumenta, a ne u meniju Elektronski dokumenti.

Idite na **Podešavanja → Tipovi dokumenata → Faktura → Napredna podešavanja** i otvorite odeljak **Validacija e-faktura**.

<figure><img src="../../../../.gitbook/assets/edoc_enable_validation_toggle.png" alt="Prekidači za validaciju e-faktura na tipu dokumenta Faktura"><figcaption><p>Uključite ili isključite validaciju e-faktura po tipu dokumenta, uz opciono obaveštenje dobavljaču</p></figcaption></figure>

* **Validiraj dolazne e-fakture** — glavni prekidač. Kada je **uključen**, svaka otpremljena faktura proverava se prema KoSIT XRechnung Schematron pravilima, kao i semantičkim proverama L0 (PDF/A-3) i L4 (IBAN/PDV), uz ozbiljnosti koje ste podesili na stranici [Pravila validacije](validation-rules.md). Nevažeće fakture se blokiraju. Kada je **isključen**, fakture potpuno preskaču validaciju e-faktura, a stranice Pravila validacije i Rutiranje obaveštenja nemaju efekta.
* **Obavesti dobavljača o odbijanju** — pojavljuje se kada je validacija omogućena. Kada je **uključen**, odbijena faktura pokreće e-poštu dobavljaču sa spiskom nedostajućih ili netačnih polja kako bi je ponovo izdao. Ko prima i obrađuje svaki nalaz podešava se na stranici [Rutiranje obaveštenja](notification-routing.md).

> Validacija e-faktura se konfiguriše **po tipu dokumenta**. Trenutno se primenjuje na tip dokumenta **Faktura**; omogućite je za svaki tip dokumenta koji treba validirati.
