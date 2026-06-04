# Validacija i testiranje

Dok gradite napredni radni tok, dve kontrole u traci sa alatkama omogućavaju vam da ga proverite bez napuštanja alata za izradu. Ove kontrole su za *brze provere tokom izrade* — za sačuvane, ponovljive testove koristite [Test Manager](../test-manager.md).

## Validate

Kliknite na kontrolu **Validate** (ikonica čekiranog kruga ili pritisnite <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). Validacija proverava graf za probleme — nepovezane čvorove, nedostajuću konfiguraciju i nevažeće veze — i ukazuje na njih kako biste ih ispravili pre nego što se radni tok pokrene nad stvarnim dokumentima.

## Test

Kliknite na kontrolu **Test** (ikonica reprodukcije ili pritisnite <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>) da biste pokrenuli trenutni tok nad primerom i posmatrali kako se ponaša, bez uticaja na žive dokumente. Ovo je najbrži način da proverite ispravnost izmene koju ste upravo napravili na platnu.

## Kada koristiti šta

- **Validate / Test u alatu za izradu** (ova stranica) — trenutna povratna informacija dok dizajnirate tok.
- **[Test Manager](../test-manager.md)** — sačuvajte scenario kako biste ga kasnije mogli ponovo pokrenuti (i to zajedno sa svim ostalim scenarijima) radi otkrivanja regresija nakon budućih izmena.

## Sledeći koraci

- Pregledajte tipove čvorova i veze u [Čvorovi](nodes.md).
- Pogledajte sve kontrole trake sa alatkama i platna u [Traka sa alatkama i platno](toolbar-and-canvas.md).
