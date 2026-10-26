# Bestellabgleich

Um Ihre PO-Matching-Konfiguration zu testen, müssen Sie in LN/M3 eine Bestellung (Purchase Order) anlegen, um zu prüfen, ob INFOR mit DocBits synchronisiert ist.&#x20;

## Bestellung in INFOR anlegen

* LN: https://docs.infor.com/ln/10.4/en-us/lnolh/docs/ln\_10.4\_procpoug\_\_en-us.pdf&#x20;
* M3: https://docs.infor.com/m3udi/16.x/en-us/m3beud/default.html?helpcontent=ois610.html&#x20;

Nachdem Sie Ihre Bestellung angelegt haben, gehen Sie zu Settings → Master Data Lookup und suchen Sie nach der Bestellnummer der soeben angelegten Bestellung. Sie sollte nun in Ihren Bestellstammdaten in DocBits erscheinen.

![](https://lh7-us.googleusercontent.com/JKGJdww6uF6U5mc1s1X\_uCcEMPYeqcikfrFOFjxpxpuaNjw-XmzNmIV2G2x6R-ZpwN2KlZACQe5Hs\_UB26klGU5XZyu6srVVLPVkS9AgEDZ1SO75YF-4ZTIt-aAuxoyyoW5sNPLsl0UxXwk193QNrFs)

Hier sollte Ihre eindeutige Bestellnummer angezeigt werden. Das bedeutet, dass DocBits und INFOR korrekt synchronisiert sind.

Laden Sie nun eine Rechnung hoch, die in Menge und Einzelpreisen mit der von Ihnen angelegten Bestellung übereinstimmt. Validieren Sie das Dokument und wählen Sie auf dem Validierungsbildschirm PO Matching.

Die Positionen von Bestellung und Rechnung sollten automatisch zugeordnet werden. Wählen Sie anschließend die Exportoption und prüfen Sie, ob das Dokument ohne Fehler exportiert wird. Wenn ein Exportfehler auftritt, erstellen Sie ein Ticket für das DocBits-Support-Team, das Ihnen weiterhilft. Falls Sie nicht wissen, wie Sie in DocBits ein Ticket erstellen, lesen Sie bitte unsere Dokumentation „DocBits Overview“.

\


