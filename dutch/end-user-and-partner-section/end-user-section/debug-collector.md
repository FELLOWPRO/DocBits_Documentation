# Debug Collector

De Debug Collector legt een volledige momentopname van uw DocBits-sessie vast — netwerkactiviteit, fouten, browseromgeving en prestatiestatistieken — verpakt deze als een JSON-rapport en kan desgewenst direct vanuit hetzelfde dialoogvenster een supportticket aanmaken.

## Hoe te openen

Druk op <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> op Windows en Linux, of <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> op macOS. Het Performance Report-dialoogvenster opent direct.

<figure><img src="../../.gitbook/assets/debug-collector-dialog.png" alt="Debug Collector dialoogvenster"><figcaption><p>Het Performance Report dialoogvenster toont de vastgelegde momentopname en een ingebouwd formulier voor supportticket.</p></figcaption></figure>

## Wat wordt vastgelegd

* **API-aanroepen** — de laatste 60 REST- en WebSocket-aanroepen, met tijden, statuscodes en de aangesproken URLs. Aanroepen van meer dan twee seconden worden apart gemarkeerd.
* **Fouten** — recente JavaScript-fouten en niet-afgehandelde promise rejections uit de browserconsole.
* **Console-logs** — de meest recente logberichten van de toepassing.
* **Omgeving** — browserversie, besturingssysteem, schermgrootte en actieve feature flags.
* **Gebruikerscontext** — uw rol, organisatie en de pagina waarop u was toen de momentopname werd gemaakt.
* **Prestatiestatistieken** — laadtijden van de pagina (LCP, FCP), geheugengebruik en DOM-grootte.
* **Trace-ID's** — correlatie-ID's die de momentopname koppelen aan backend-logregels.

## Een supportticket aanmaken vanuit het dialoogvenster

U hoeft niets handmatig te downloaden of bij te voegen — het dialoogvenster bevat een ingebouwd formulier **Create Support Ticket**.

1. Vul uw e-mailadres in, behoud het voorgestelde onderwerp of vervang het, kies een prioriteit en voeg notities toe over wat u deed toen het probleem optrad.
2. Klik op **Send Report**. De JSON-momentopname wordt bijgevoegd en het ticket wordt in één stap aangemaakt.

Dat is alles — support ontvangt het ticket met alle gegevens die nodig zijn om de situatie te reproduceren.

Wilt u een lokale kopie van de momentopname, gebruik dan **Copy Debug Data** om de JSON naar het klembord te kopiëren, of gebruik Opslaan als van uw browser om het rapport als `.json`-bestand te bewaren.

## Privacy en gegevensafhandeling

* Authenticatietokens en gevoelige headers worden uit de vastgelegde API-aanroepen verwijderd voordat de momentopname wordt opgebouwd.
* Er verlaat niets uw browser totdat u op **Send Report** klikt — de sneltoets opent alleen het dialoogvenster.

<mark>Controleer de momentopname voordat u deze verstuurt als u met documenten werkte die klantgegevens bevatten. Document-ID's die zichtbaar zijn in URLs verschijnen in het rapport.</mark>
