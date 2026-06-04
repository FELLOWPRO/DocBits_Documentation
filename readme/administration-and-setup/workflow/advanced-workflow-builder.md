# Advanced Workflow

**Advanced Workflow** alat za izradu je editor grafa čvorova za radne tokove kojima su potrebni grananje, paralelne putanje i kontrola toka — iznad linearnog When/And/Then modela Standard alata. Raspoređujete čvorove na platnu i povezujete ih da definišete tok izvršavanja.

## Kako pristupiti

Otvorite Advanced Workflow dizajner iz oblasti radnih tokova (platno naprednog alata za izradu). Počinjete od **Start** čvora i gradite tok dodavanjem čvorova.

<figure><img src="../../.gitbook/assets/workflow_advanced_canvas.png" alt="Advanced Workflow platno grafa čvorova sa trakom alata"><figcaption><p>Advanced Workflow platno — graf čvorova sa kontrolama za zumiranje, pokretanje, mrežu i čuvanje. Dajte radnom toku ime u traci alata.</p></figcaption></figure>

## Dodavanje čvorova

Kliknite na **+ Add** da otvorite meni čvorova. Pored poznatih **When**, **And** i **Then** kartica, napredni alat za izradu dodaje i čvorove za kontrolu toka:

<figure><img src="../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Advanced Workflow Add meni sa tipovima čvorova"><figcaption><p><strong>+ Add</strong> meni čvorova: When / And / Then plus Wait ALL, Wait ANY, OR i Note.</p></figcaption></figure>

- **When / And / Then** — iste kartice uslova i akcija kao u Standard alatu za izradu.
- **Wait ALL** — čeka dok se *sve* dolazne grane ne završe pre nego što nastavi.
- **Wait ANY** — nastavlja čim se *bilo koja* dolazna grana završi.
- **OR** — grana tok niz alternativne putanje.
- **Note** — slobodna tekstualna napomena na platnu (ne utiče na izvršavanje).

Pokrenite tok pomoću kontrole za reprodukciju, proverite ga, i sačuvajte dugmetom za čuvanje u traci alata.

## Sledeći koraci

- Pogledajte šta svaka kartica radi u odeljku **Cards**.
- Za jednostavne linearne automatizacije, **Standard Workflow** alat za izradu se brže podešava.
