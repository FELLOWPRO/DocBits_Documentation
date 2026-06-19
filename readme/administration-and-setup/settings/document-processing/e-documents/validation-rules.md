# Validierungsregeln

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_setup.png" alt="Validierungs-Setup und akzeptierte Versionen"><figcaption><p>Validierungs-Setup und akzeptierte XRechnung-Versionen</p></figcaption></figure>

Die Seite **Validierungsregeln** (**E-Dokumente → Regeln**) steuert, wie DocBits eingehende E-Rechnungen validiert. Sie basiert auf dem offiziellen **KoSIT XRechnung + ZUGFeRD**-Regelsatz sowie den internen Finding-Codes des Validators und ermöglicht es Ihnen, den Schweregrad jeder Regel für Ihre Organisation zu überschreiben.

## Validierungs-Setup

Die Karte **Validierungs-Setup** zeigt Ihr aktuelles Validierungsprofil (zum Beispiel *B2G – Public Sector Receiver*). Klicken Sie auf **Antworten bearbeiten**, um den Setup-Assistenten erneut auszuführen und den Standard zu ändern, gegen den validiert wird.

## Akzeptierte XRechnung-Versionen

Das Gate **Akzeptierte XRechnung-Versionen** listet jede XRechnung-Version auf. Markieren Sie die Versionen, die Sie akzeptieren – Dokumente, deren CustomizationID außerhalb dieser Liste liegt, werden bereits vor jeder weiteren Prüfung mit `VAL-VERSION-NOT-ALLOWED` abgelehnt. Eine leere Liste bedeutet „alles akzeptieren". Jede Version ist mit **current**, **deprecated** oder **EOL** sowie ihrem Veröffentlichungsdatum gekennzeichnet.

## Akzeptierte Profile und Schweregrad-Modell

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_severity.png" alt="Akzeptierte Profile und Schweregrad-Legende"><figcaption><p>Akzeptierte Profile und die Bedeutung der Schweregrade</p></figcaption></figure>

Wählen Sie über **Alle akzeptieren** / **Leeren** und anschließend **Speichern**, welche **Profile** Sie akzeptieren (BASIC WL, BASIC, EN 16931 / COMFORT, EXTENDED, XRECHNUNG (CIUS)).

Jede Validierungsregel hat einen **Schweregrad**, der bestimmt, was beim Auslösen geschieht:

| Schweregrad | Auswirkung |
|-------------|------------|
| **FATAL** | Stoppt die Verarbeitung sofort. Keine weitere Ebene wird geprüft; das Dokument geht in den Fehlerstatus. |
| **ERROR** | Das Dokument wird abgelehnt. Andere Findings desselben Dokuments werden weiterhin angezeigt; die Lieferantenbenachrichtigung (falls aktiviert) wird ausgelöst. |
| **WARNING** | Erscheint im Validierungsbericht, das Dokument durchläuft die Pipeline jedoch normal. |
| **INFO** | Nur Audit-Log. Keine nutzerseitige Auswirkung und keine Ablehnung. |

## Schweregrade überschreiben

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_table.png" alt="Die Validierungsregel-Tabelle"><figcaption><p>Die vollständige Regeltabelle mit Schweregrad-Override pro Regel</p></figcaption></figure>

Die Regeltabelle listet jede Validierungsregel auf (insgesamt über 1.600). Filtern Sie nach **Ebene (Layer)**, **Profil** oder **Version** oder suchen Sie nach Code oder Feld. Für jede Regel können Sie den **Schweregrad** über das Dropdown überschreiben, um ihn an die Richtlinien Ihrer Organisation anzupassen – zum Beispiel eine Regel von `ERROR` auf `WARNING` herabstufen, damit sie das Dokument nicht mehr ablehnt.
