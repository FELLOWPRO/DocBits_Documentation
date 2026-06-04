# Čvorovi

Napredni tok rada (Advanced Workflow) je graf **čvorova** povezanih ivicama. Čvorove dodajete iz menija **+ Add** (ili desnim klikom na platno) i povezujete ih da biste definisali tok izvršavanja.

<figure><img src="../../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Meni za dodavanje čvora sa dostupnim tipovima čvorova"><figcaption><p>Meni čvorova <strong>+ Add</strong> — dostupni tipovi čvorova.</p></figcaption></figure>

## Tipovi čvorova

- **Start** — ulazna tačka toka rada. Dodaje se automatski; svaki tok počinje ovde.
- **When** — kartica okidača, ista kao u standardnom graditelju.
- **And** — kartica uslova. Evaluira se na tačno ili netačno i može da grana tok.
- **Then** — akciona kartica koja obavlja posao (postavljanje polja, kreiranje zadataka, pozivanje API-ja, …).
- **Wait ALL** — čeka da se *sve* dolazne grane završe pre nego što se nastavi.
- **Wait ANY** — nastavlja čim se *bilo koja* dolazna grana završi.
- **OR** — grana tok niz alternativne putanje.
- **Note** — slobodna tekstualna napomena na platnu; ne utiče na izvršavanje.

Čvorovi **When / And / Then** koriste potpuno iste kartice opisane u odeljku [Kartice](../cards-overview.md).

## Povezivanje čvorova

Čvorovi se povezuju **obojenim ivicama**. Povucite od ručice na **desnoj** strani čvora do ulazne ručice na **levoj** strani drugog čvora da biste kreirali vezu. Svaka boja označava drugačiji ishod izvršavanja:

- **Success** (plava) — podrazumevana putanja koja se koristi kada se čvor uspešno završi. Dostupna na svim tipovima čvorova.
- **Failed Condition** (narandžasta) — koristi se kada se uslov evaluira na netačno. Dostupna na **And** (uslov) čvorovima.
- **Error** (crvena) — koristi se kada čvor naiđe na grešku tokom izvršavanja. Dostupna na **And** i **Then** (akcija) čvorovima.

## Isticanje putanje izvršavanja

Kliknite na bilo koji čvor da biste videli njegovu putanju izvršavanja. Svi čvorovi koji vode u njega i svi čvorovi koji slede iz njega se ističu — sve ostalo je zatamnjeno. Za **Wait ALL** čvorove prikazana je svaka dolazna grana, tako da možete tačno videti šta kapija čeka pre nego što se nastavi.

## Sledeći koraci

- Prosleđujte podatke između čvorova pomoću [Promenljivih](variables.md).
- Proverite i pokrenite svoj tok pomoću [Validacije i testiranja](validation-and-testing.md).
