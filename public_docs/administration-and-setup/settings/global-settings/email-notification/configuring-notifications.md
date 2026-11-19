# Benachrichtigungen konfigurieren

E-Mail-Benachrichtigungen können Empfänger informieren, wenn ein Dokument einen ausgewählten Status erreicht. Bevor Sie eine Benachrichtigung erstellen, stellen Sie sicher, dass für den Belegtyp, den Sie verwenden möchten, eine [E-Mail-Vorlage](../e-mail-templates.md) existiert.

## Benachrichtigungsliste öffnen

Wählen Sie in **Einstellungen** den Bereich **KOMMUNIKATION & BENACHRICHTIGUNGEN** und dort **E-Mail-Benachrichtigung**. Die Liste zeigt bestehende Regeln mit Belegtyp, Status, Priorität, Verzögerung, Empfänger und letzter Änderung. Wählen Sie **Neu**, um eine Regel zu erstellen.

<figure><img src="../../../../.gitbook/assets/configuring-notifications-list-de-20261112.png" alt="Liste der E-Mail-Benachrichtigungen mit der Schaltfläche Neu über der Regeltabelle"><figcaption><p>Wählen Sie Neu, um eine E-Mail-Benachrichtigung zu konfigurieren.</p></figcaption></figure>

## Eine Regel einrichten

Der Dialog **Neu** enthält folgende Bedienelemente:

| Bedienelement | Eingabe |
| --- | --- |
| **Name** | Ein Name, den Sie in der Benachrichtigungsliste wiedererkennen. Verwenden Sie Buchstaben, Ziffern und Leerzeichen. |
| **Dokumenttyp** | Der Belegtyp, für den diese Regel gilt. Wählen Sie ihn vor der E-Mail-Vorlage. |
| **Unterorganisation** | Die Unterorganisation, für die diese Regel gilt. |
| **E-Mail-Vorlage auswählen** | Eine Vorlage für den gewählten Belegtyp. Die Auswahl ist erst verfügbar, wenn passende Vorlagen geladen sind. |
| **Status** | Der Dokumentstatus, der die Benachrichtigung auslöst. |
| **Priorität** | Der Prioritätswert für diese Benachrichtigungsregel. |
| **Zeiteinheit** und **Verzögerung** | Wie lange vor dem Versand gewartet wird. In Minuten muss die Verzögerung mindestens fünf betragen; geben Sie eine ganze Zahl ein. |
| **Nicht wiederholen / Wiederholen Sie** | Schalten Sie **Wiederholen Sie** ein, wenn die Benachrichtigung erneut gesendet werden soll, solange die Bedingung zutrifft. |
| **E-Mail an zugewiesenen Benutzer/Gruppe senden** | An den dem Dokument zugewiesenen Empfänger senden statt an eine feste Adresse. Dadurch wird **E-Mail-Adresse** ausgeblendet. |
| **E-Mail-Adresse** | Geben Sie eine gültige Adresse ein, wenn die Option für den zugewiesenen Empfänger ausgeschaltet ist. |
| **Benachrichtigung bei Neuzuweisung erneut senden** | Erneut senden, wenn das Dokument einer anderen Person zugewiesen wird. |

<figure><img src="../../../../.gitbook/assets/configuring-notifications-create-de-20261112.png" alt="Dialog Neue E-Mail-Benachrichtigung mit den leeren Feldern Name, Dokumenttyp, Unterorganisation, E-Mail-Vorlage auswählen, Status, Priorität, Zeiteinheit, Verzögerung, E-Mail-Adresse sowie Abbrechen und Speichern"><figcaption><p>Wählen Sie einen Dokumenttyp und seine E-Mail-Vorlage und legen Sie dann Auslöser und Empfänger fest.</p></figcaption></figure>

Wenn **E-Mail an zugewiesenen Benutzer/Gruppe senden** ausgewählt ist, verschwindet das feste Feld **E-Mail-Adresse**. Der Schalter ändert seine Beschriftung von **Nicht wiederholen** in **Wiederholen Sie**.

<figure><img src="../../../../.gitbook/assets/configuring-notifications-recipient-repeat-de-20261112.png" alt="Benachrichtigungsformular mit eingeschalteter Wiederholung und ausgewählter Option E-Mail an zugewiesenen Benutzer/Gruppe senden; erfundene Beispieldaten: Name Rechnung freigegeben, Dokumenttyp Rechnung, Vorlage Docs Demo Invoice Notification, Priorität Mittel, 15 Minuten"><figcaption><p>Nutzen Sie die Option für zugewiesene Empfänger, wenn die für das Dokument verantwortliche Person die E-Mail erhalten soll. Die gezeigten Werte sind erfundene Beispieldaten.</p></figcaption></figure>

Wählen Sie **Speichern**, um die Regel zur Liste hinzuzufügen, oder **Abbrechen**, um den Entwurf zu verwerfen. Wenn **E-Mail-Vorlage auswählen** keine Auswahl anbietet, erstellen Sie zuerst eine Vorlage für den ausgewählten Belegtyp und kehren Sie dann in diesen Dialog zurück.
