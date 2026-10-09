# Bestellabgleich

Um Ihre PO-Matching-Konfiguration zu testen, müssen Sie in LN/M3 einen Purchase Order anlegen, um zu prüfen, ob INFOR mit DocBits synchronisiert ist.

## Einen Purchase Order in INFOR anlegen

* LN: https://docs.infor.com/ln/10.4/en-us/lnolh/docs/ln\_10.4\_procpoug\_\_en-us.pdf
* M3: https://docs.infor.com/m3udi/16.x/en-us/m3beud/default.html?helpcontent=ois610.html

Sobald Sie den Purchase Order angelegt haben, öffnen Sie Einstellungen → Stammdaten und suchen Sie dort nach der Purchase-Order-Nummer des Purchase Orders, den Sie gerade angelegt haben. Er sollte jetzt in Ihren Purchase-Order-Stammdaten in DocBits erscheinen.

<figure><img src="../../.gitbook/assets/a-testing-po-matching-master-data-de-20261009.png" alt="Seite Stammdaten mit der Tabelle Bestellung und den importierten Purchase Orders."><figcaption><p>Die Purchase Orders erscheinen in der Stammdaten-Übersicht.</p></figcaption></figure>

Sie sollten hier Ihre eindeutige Purchase-Order-Nummer sehen. Das bedeutet, dass DocBits und INFOR korrekt synchronisiert sind.

Laden Sie nun Ihre Rechnung hoch, deren Mengen und Einzelpreise zu dem Purchase Order passen, den Sie angelegt haben. Prüfen Sie das Dokument und wählen Sie im Validierungsbildschirm Bestellabgleich aus.

Die Positionen des Purchase Orders und der Rechnung sollten automatisch zusammengeführt werden. Wählen Sie dann einfach die Export-Option aus und prüfen Sie, ob das Dokument ohne Fehler exportiert wird. Falls beim Export ein Fehler auftritt, erstellen Sie ein Ticket für das DocBits-Support-Team, damit Ihnen geholfen wird. Wenn Sie nicht wissen, wie Sie in DocBits ein Ticket erstellen, finden Sie in unserer Übersichtsdokumentation zu DocBits eine Anleitung dazu.

\
