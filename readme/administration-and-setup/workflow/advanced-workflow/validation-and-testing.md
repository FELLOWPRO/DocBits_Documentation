# Validacija i testiranje

Pre nego što se oslonite na napredni tok rada, koristite kontrole na traci sa alatkama da biste potvrdili da je ispravan i da se ponaša kako se očekuje.

## Validate

Kliknite na kontrolu **validate** (ikona kruga sa kvačicom, ili pritisnite <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). Validacija proverava graf za probleme — nepovezane čvorove, nedostajuću konfiguraciju i nevažeće veze — tako da ih možete ispraviti pre nego što se tok rada pokrene na stvarnim dokumentima.

## Test

Kliknite na kontrolu **test** (ikona reprodukcije, ili pritisnite <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>) da biste pokrenuli tok rada na uzorku i videli kako se ponaša, bez uticaja na žive dokumente.

## Test scenariji

Za ponovljive provere, sačuvajte **test scenarije** u **Test Manager**-u (pogledajte [Komandnu tablu](../workflow-dashboard.md)). Svaki scenario beleži očekivani ishod i prikazuje rezultat prošlo/palo, a **Run All Tests** ih ponovo pokreće zajedno — tako da možete potvrditi da se vaši tokovi rada i dalje ponašaju ispravno nakon promene.

<figure><img src="../../../.gitbook/assets/workflow_test_manager.png" alt="Lista Workflow Test Manager-a sa test scenarijima i Run All Tests"><figcaption><p>Test Manager — sačuvani scenariji sa rezultatima prošlo/palo i opcijom <strong>Run All Tests</strong>.</p></figcaption></figure>

## Sledeći koraci

- Pregledajte tipove čvorova i veze u odeljku [Čvorovi](nodes.md).
- Pogledajte sve kontrole trake sa alatkama i platna u [Traci sa alatkama i platnu](toolbar-and-canvas.md).
