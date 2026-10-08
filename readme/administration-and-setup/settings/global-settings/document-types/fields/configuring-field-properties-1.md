# Konfigurisanje Svojstava Polja

Koristite **Podešavanja → Tipovi dokumenata → Polja** da kontrolišete kako se polja ponašaju za jedan tip dokumenta. Prvo izaberite tip dokumenta; primer ispod prikazuje **Fakturu** na engleskom interfejsu.

<figure><img src="../../../../../.gitbook/assets/configuring-field-properties-1-overview-en-20261008.png" alt="Podešavanja polja fakture u engleskoj Sandbox test organizaciji: pragovi prepoznavanja, pretraga, kolone svojstava polja i dugme Save Settings. Engleski jezik interfejsa — srpski jezik još nije dostupan u Sandbox UI."><figcaption>Podešavanja polja fakture u DocBits Sandbox test organizaciji (engleski interfejs; srpski jezik u aplikaciji još ne postoji).</figcaption></figure>

## Pronađite polje i promenite njegova svojstva

1. U polju **Search by Name** unesite naziv ili oznaku polja. Ovo filtrira listu; ne menja samo polje.
2. Pronađite red tog polja. Na primer, **Invoice number** (broj fakture) ima tehnički naziv `invoice_number`.
3. Podesite kontrole u tom redu, zatim izaberite **Save Settings**. Isti dugme za čuvanje nalazi se i iznad i ispod tabele.

<figure><img src="../../../../../.gitbook/assets/configuring-field-properties-1-filtered-en-20261008.png" alt="Red Invoice number u engleskom interfejsu sa kontrolama Required, Read Only, Hidden, Force Validation, Use AI, OCR i Match Score. Engleski jezik interfejsa — srpski jezik još nije dostupan u Sandbox UI."><figcaption>Red Invoice number nakon pretrage po `invoice_number` (engleski interfejs).</figcaption></figure>

| Kontrola | Čemu služi |
| --- | --- |
| **Required** (obavezno) | Označava podatke koji moraju postojati radi validacije. Nakon promene proverite rezultat validacije dokumenta. |
| **Read Only** (samo za čitanje) | Prikazuje polje bez mogućnosti da korisnici menjaju njegovu vrednost. |
| **Hidden** (skriveno) | Drži polje van uobičajenog prikaza dokumenta. |
| **Force Validation** (obavezna validacija) | Zahteva da polje prođe validaciju. Detaljna pravila se podešavaju odvojeno; ovo polje za štikliranje nije uređivač pravila. |
| **Use AI** (koristi veštačku inteligenciju) | Uključuje ili isključuje AI ekstrakciju za ovo polje. Red prikazuje da li je ekstrakcija zatražena. |
| **OCR** | Unosi prag OCR pouzdanosti za polje. Ovo je broj, a ne prekidač za uključivanje/isključivanje ili podešavanje jezika. |
| **Match Score** (rezultat uparivanja) | Unosi prag uparivanja za polje. Ovo je broj, a ne prekidač za uključivanje/isključivanje. |

Klizači **OCR** i **Match Score** u odeljku **Recognition Settings** primenjuju vrednosti na celu listu polja. Polja za štikliranje odmah ispod naziva kolona primenjuju **Required**, **Read Only**, **Hidden** ili **Force Validation** na celu listu. Pregledajte zahvaćene redove pre nego što izaberete **Save Settings**. **Restore Defaults** resetuje konfiguraciju polja; koristite ga samo kada namerno želite da zamenite svoje izmene.

## Ostale kontrole u ovom prikazu

- **Create new group** i **Create field** dodaju grupu ili polje. Odgovarajuća stranica na srpskom još nije prevedena (posebno potzadatke).
- **Master Data Settings** otvara podešavanja matičnih podataka. Odgovarajuća stranica na srpskom još nije prevedena (posebno potzadatke).
- Polja za štikliranje krajnje levo biraju polja. Obližnji meni nudi **Reassign Field Group** za izabrana polja.
- Dugme sa plus pored **Formula** otvara uređivač formula za to polje. Ikona **info** prikazuje informacije o polju. Ikona za brisanje nije dostupna za standardna polja.

Za više o validaciji i uparivanju videće se na stranici Podešavanje validacije i rezultata uparivanja; ona na srpskom još nije prevedena (posebno potzadatke).
