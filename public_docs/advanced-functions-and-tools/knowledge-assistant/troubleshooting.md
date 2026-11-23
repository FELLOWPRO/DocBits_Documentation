# Fehlerbehebung

Die meisten Probleme lösen Sie mit **Rebuild Document** (das Dokument erneut verarbeiten) oder mit einer genaueren Frage. Die Tabellen nennen nur Fälle, die wir in unseren Tests beobachtet haben. Wie Sie jede Funktion erreichen, steht unter [Aufgaben und wo Sie sie finden](tasks-and-where-to-find-them.md).

## Dokumente und Verarbeitung

| Symptom | Ursache (kurz) | Maßnahme |
| --- | --- | --- |
| Das Dokument zeigt **May be stuck**; die Zeitleiste meldet „No progress for N minutes“ | Die Verarbeitung hat lange nichts gemeldet. | Dokument öffnen, **Stop parsing** wählen, dann **Rebuild Document**. Tun Sie nichts, setzt das System das Dokument nach einer Weile selbst auf Failed. |
| Das Dokument zeigt **Failed** mit „task stuck in processing…“ | Ein Stillstand wurde automatisch beendet. | **Rebuild Document**. Bleibt es dabei, melden Sie den Dokumentnamen dem Support. |
| Ein gescanntes PDF hat nach der Verarbeitung keinen Text oder zeigt Failed, und die Meldung nennt die Texterkennung | Die Texterkennung war nicht erreichbar, oder das Bild deckt nur einen Teil der Seite ab und die Seite wird als Textseite behandelt. | Etwas später **Rebuild Document**. Scans nach Möglichkeit ganzseitig erstellen. Besteht das Problem weiter, wenden Sie sich an Ihren Administrator. |
| Eine beschädigte Datei zeigt **Failed** | Die Datei lässt sich nicht lesen. Bei beschädigten Word-Dateien kann es bis zu etwa 3 Minuten dauern, bis Failed erscheint. | Datei im Originalprogramm öffnen, erneut speichern und erneut hochladen. |
| Der Upload wird abgewiesen | E-Mail-Dateien (.eml), XML-Dateien, leere Dateien und eine Datei, die schon in der Wissensdatenbank liegt, werden nicht angenommen. Der Import über Web-Adresse ist abgeschaltet. | Datei in ein unterstütztes Format umwandeln, zum Beispiel PDF. Bei einem Duplikat bleibt das vorhandene Dokument unverändert. |
| Der Upload bricht mit **Storage quota exceeded** ab | Das Speicherkontingent Ihrer Organisation ist erreicht. | Nicht mehr benötigte Dokumente löschen; der Platz wird frei. Für mehr Platz wenden Sie sich an Ihren Administrator. Auch ein mit **Online Edit** geschriebenes Dokument kann später auf Failed enden, wenn das Kontingent erreicht ist. |
| Ein Foto lässt sich nicht hochladen, **Upload and parse** ist grau | <!-- CHECK-DEV FIX-FOTO --> Für Fotos muss die Bildverarbeitung („Multimodal“) eingeschaltet und ein Modell gewählt sein. | Bildverarbeitung einschalten und ein Modell wählen (Administrator). |
| Nach **Save and Close** in den Einstellungen der Wissensdatenbank stimmen die Werte nicht | <!-- CHECK-DEV FIX-CHUNK --> Das Speichern der Abschnittsgröße funktioniert derzeit nicht zuverlässig; vorhandene Einstellungen können zurückgesetzt werden. | Diese Werte vorerst nicht ändern. Ansehen und Schließen ohne Speichern ist unbedenklich. |
| Ein Excel-Dokument ist durchsuchbar, hat aber keine Kurzbeschreibung | Die automatische Beschreibung von Tabellendokumenten schlägt manchmal fehl. Der Inhalt wird trotzdem gelesen. | Keine Maßnahme nötig, Fragen funktionieren. Tragen Sie bei Bedarf eine Beschreibung von Hand ein. |

## Fragen und Antworten

| Symptom | Ursache (kurz) | Maßnahme |
| --- | --- | --- |
| Die Antwort lautet „nicht in den Unterlagen“, obwohl Sie das Dokument kennen | Das Dokument ist noch nicht Completed, wurde gelöscht, oder die Nummer in Ihrer Frage weicht ab. Der Assistent verwechselt ähnliche Nummern nicht. | Status prüfen, die Nummer exakt aus dem Dokument kopieren und die Frage wiederholen. |
| Eine Gültigkeitsfrage („Ist … noch gültig?“) endet mit „To be clarified“ oder „Not unambiguous“ statt mit Ja oder Nein | Das Dokument nennt ein abgelaufenes Gültig-bis-Datum, trägt selbst aber den Vermerk „gültig“. Die Antwort fällt dann vorsichtig aus. | Ergänzen Sie: **„Antworte mit Ja oder Nein und nenne das Gültig-bis-Datum.“** Mit dieser Formulierung gab der Assistent in den geprüften Fällen ein klares Nein mit Datum. |
| Eine Antwort hat keinen anklickbaren Quellenhinweis | In seltenen Einzelfällen war der Wert richtig, der Hinweis fehlte. | Die Frage wiederholen oder ergänzen: „Nenne die Quelle.“ Prüfen Sie den Wert immer im Dokument. |
| Eine Seitenangabe bei einem langen Dokument ist um eins daneben | In einem Testlauf nannte die Antwort Seite 8; die Stelle stand auf Seite 7. | Öffnen Sie immer die Vorschau und bestätigen Sie die Seite dort. |
| Eine Frage zu einem Foto bleibt unbeantwortet, oder die Gallery ist leer („No caption“) | Einzeln hochgeladene Fotos werden per Texterkennung gelesen: Fragen Sie nach dem **Text** im Foto, nicht danach, was das Bild zeigt. Die Gallery zeigt nur in Dokumente eingebettete Bilder, und die Beschreibungen sind derzeit leer. | Fragen Sie nach im Foto geschriebenen Werten, zum Beispiel Zahlen, Klassen oder Mengen. Für die Gallery muss die Bildverarbeitung der Wissensdatenbank eingeschaltet sein. |
| Excel als Quelle öffnet sich, die Zeile ist aber nicht markiert | Die Vorschau kann in Tabellen nicht zu einer Zeile springen. | Die Datei öffnet sich; suchen Sie dort nach dem genannten Wert. |
| Eine Antwort dauert länger | In unseren Tests dauerten Antworten im Mittel 6 bis 9 Sekunden, einzelne bis zu 25 Sekunden; Fragen zu Widersprüchen dauerten am längsten. | Warten, die Frage nicht erneut absenden. |

## Branchenvorlage und Berechtigungen

| Symptom | Ursache (kurz) | Maßnahme |
| --- | --- | --- |
| Der Reiter **Industry templates** fehlt in den Settings | Sie sind kein Administrator. Nur Administratoren sehen den Reiter. | Bitten Sie Ihren Administrator, die Vorlage einzuschalten. |
| Die Vorlage ist an, aber die Assistenten fehlen im Chat | Sie sind in einer anderen Organisation angemeldet, oder die Vorlage wurde mit **Switch off** ausgeschaltet. Vorlagen gelten je Organisation; beim Ausschalten verschwinden die Assistenten, die Dokumente bleiben. | Organisation oben rechts prüfen und prüfen, ob die Karte unter **Industry templates** „On“ zeigt. |
| Hochladen, Bearbeiten, Löschen und Herunterladen werden nicht angeboten | Ihre Rolle ist Viewer. | Bitten Sie Ihren Administrator, Ihre Rolle auf Contributor zu ändern. |

## Bedienung

| Symptom | Ursache (kurz) | Maßnahme |
| --- | --- | --- |
| Ein Ordner lässt sich nicht verschieben; die Meldung erscheint auf Chinesisch | Der Zielordner liegt innerhalb des Ordners, der verschoben wird. Die Meldung ist noch nicht übersetzt. | Wählen Sie einen Zielordner außerhalb des verschobenen Ordners. Auch andere Meldungen, zum Beispiel beim Abbrechen der Verarbeitung, sind teils noch nicht übersetzt. |
| Beim Speichern von Metadaten erscheint ein Fehler | Es sind höchstens 20 Felder je Dokument möglich. | Nicht benötigte Felder entfernen. |
| Beim Bearbeiten eines Abschnitts erscheint „Chunk was modified by another user“ | Eine zweite Person hat denselben Abschnitt geändert. | Seite neu laden und die Änderung erneut vornehmen. |
| Ein Mermaid-Diagramm in einem Markdown-Dokument erscheint als eine Textzeile | Diagramme in Markdown werden nicht gezeichnet. | Legen Sie die Information zusätzlich als Text oder Tabelle ab. |
| Die Kopie einer Wissensdatenbank ist vom Original nicht zu unterscheiden | Die Kopie trägt denselben Namen. | Kopie umbenennen. |

## Vorsorgliche Hinweise

Diese Fälle sind in unseren Tests nicht aufgetreten:

* **Ein Dokument bleibt lange auf „In queue“.** Bei großen Importen warten Dokumente der Reihe nach. Warten Sie einige Minuten; erscheint **May be stuck**, gehen Sie wie oben vor.
* **Zahlen aus PDF-Tabellen wirken falsch.** Prüfen Sie den Wert in der Vorschau (siehe [Was er kann und was nicht](what-it-can-and-cannot-do.md#pdf-tabellen)).
* **Die Antwort kommt in der falschen Sprache.** In allen Tests folgte die Antwort der Sprache der Frage, auch bei Dokumenten in einer anderen Sprache. Das ist nicht garantiert. Nennen Sie bei Bedarf in der Frage die gewünschte Sprache der Antwort.
* **Der Menüpunkt Knowledge Assistant fehlt.** Das Modul muss für Ihre Organisation eingeschaltet sein. Wenden Sie sich an Ihren Administrator.
