# Aufgaben und wo Sie sie finden

Alles beginnt im DocBits-Client unter **Knowledge Assistant**. Links finden Sie **Chat**, **Knowledge Base**, **Agents**, **Automations** und **Settings**. Im **Chat** stellen Sie Fragen, in der **Knowledge Base** verwalten Sie Dokumente, und ein Administrator schaltet unter **Settings** die Branchenvorlage ein.

Die Oberfläche des Knowledge Assistant ist derzeit englisch, deshalb stehen die Bezeichnungen unten genau so, wie sie auf dem Bildschirm erscheinen. <!-- CHECK-DEV: UI-Sprache des Knowledge Assistant auf dev; Satz anpassen -->

Spalte Status: **Verfügbar** funktioniert in unseren Tests. **Eingeschränkt** funktioniert mit der genannten Einschränkung. **Nicht verfügbar** ist bewusst abgeschaltet oder wird nicht angeboten. **In Vorbereitung** ist für Anwender noch nicht freigegeben.

## Aufgabe und Klickweg

| Aufgabe | Klickweg | Was passiert | Status |
| --- | --- | --- | --- |
| Knowledge Assistant einschalten | Settings → Modules → Document Integration → Karte **Knowledge Assistant** (Administrator) | Der Menüpunkt **Knowledge Assistant** erscheint. | Verfügbar <!-- CHECK-DEV: Pfad und Wortlaut der Modulkarte prüfen --> |
| Branchenvorlage einschalten | Knowledge Assistant → Settings → **Industry templates** (nur Administrator) | Drei Wissensdatenbanken und drei Assistenten werden angelegt. | Verfügbar |
| Eine Frage stellen | Knowledge Assistant → Chat → unter **Custom Agents** einen Assistenten wählen → Frage eintippen | Sie erhalten eine Antwort mit Quellenhinweisen. | Verfügbar |
| Eine Quelle öffnen | Chat → Quellenhinweis unter der Antwort anklicken | Das Dokument öffnet sich rechts an der Stelle, an der die Antwort gefunden wurde. | Verfügbar; eingeschränkt bei Excel und Bildern |
| Neues Gespräch beginnen | Chat → **New chat** | Ein leeres Gespräch ohne den früheren Verlauf. | Verfügbar |
| Wissensdatenbank anlegen | Knowledge Base → **Create Knowledge Base** | Sie wählen Typ und Indexierung und geben einen Namen ein. | Verfügbar |
| Dokumente hochladen | Knowledge Base → Wissensdatenbank öffnen → **Add Document** → **Upload Document** | Die Dateien werden gelesen und durchsuchbar gemacht. | Verfügbar; Fotos eingeschränkt |
| Ganzen Ordner hochladen | Knowledge Base → **Add Document** → **Upload Folder** | Die Ordnerstruktur bleibt erhalten. | Eingeschränkt: Die Struktur wurde getestet, der Auswahldialog nicht |
| Text direkt schreiben | Knowledge Base → **Add Document** → **Online Edit** | Sie schreiben ein Markdown-Dokument und geben es mit **Publish** frei. | Verfügbar |
| Verarbeitungsstatus lesen | Knowledge Base → Wissensdatenbank → Dokumentliste, Spalte **Status** | Completed, Failed oder May be stuck; ein Klick zeigt die Parsing-Zeitleiste. | Verfügbar |
| Dokument erneut verarbeiten | Dokument auswählen → **Rebuild Document** | Das Dokument wird erneut gelesen. | Verfügbar |
| Ordner und Tags | Knowledge Base → Wissensdatenbank → Ordnerbaum links; **Add tags** in der Dokumentzeile | Dokumente lassen sich sortieren und filtern. | Verfügbar |
| Dokumente zwischen Ordnern verschieben | Dokumente auswählen → **Move to folder** | Das Dokument wechselt den Ordner, ohne neu gelesen zu werden. | Verfügbar |
| Mehrere Dokumente herunterladen | Dokumente auswählen → **Download selected** | Sie erhalten eine ZIP-Datei mit den Originalen. | Verfügbar |
| Textabschnitte bearbeiten | Dokument öffnen → Abschnittsliste → Stift am Abschnitt | Der geänderte Text wird sofort für Antworten genutzt. | Verfügbar |
| Metadaten pflegen | Dokument öffnen → Stift bei den Metadaten | Bis zu 20 eigene Felder je Dokument. | Verfügbar |
| Änderungen nachvollziehen | Wissensdatenbank → Settings (Zahnrad) → **Management & Audit** → **Activity** | Eine Liste von Anlage, Upload und Änderungen mit Zeit und Person. | Verfügbar |
| Bilder aus Dokumenten ansehen | Wissensdatenbank → Reiter **Gallery** | Zeigt in Dokumente eingebettete Bilder. | Eingeschränkt |
| Wochenübersicht | Knowledge Assistant → **Automations** | Ein Assistent stellt eine Übersicht ablaufender Dokumente zusammen. | Eingeschränkt |
| Wissensdatenbank kopieren | Funktion **Copy** der Wissensdatenbank | Die Kopie entsteht im Hintergrund, samt Ordnern. | Eingeschränkt: Der Weg in der Oberfläche wurde nicht gesondert geprüft |
| Dokumente zwischen Wissensdatenbanken verschieben | – | In der Mehrfachauswahl nicht angeboten. | Nicht verfügbar |
| Dokument über Web-Adresse holen | – | Der Import über Web-Adresse ist abgeschaltet. | Nicht verfügbar |
| DocBits-Dokumente als Wissensquelle nutzen | – | Rechnungen und Verträge aus DocBits ohne erneutes Hochladen verwenden. | In Vorbereitung |

## Den Knowledge Assistant einschalten (Administrator)

<!-- CHECK-DEV: durch echten Screenshot und genauen Wortlaut der Modulkarte ersetzen, sobald dev grün ist -->

1. Öffnen Sie **Settings** → **Modules** → **Document Integration**.
2. Suchen Sie die Karte **Knowledge Assistant** und schalten Sie sie ein.
3. Laden Sie DocBits neu. Der Menüpunkt **Knowledge Assistant** erscheint nun im Menü.

{% hint style="info" %}
Fehlt der Menüpunkt **Knowledge Assistant**, ist das Modul für Ihre Organisation nicht eingeschaltet. Fragen Sie Ihren Administrator.
{% endhint %}

## Eine Branchenvorlage einschalten (Administrator)

Öffnen Sie **Knowledge Assistant** → **Settings** → **Industry templates**. Vorlagen gibt es für Construction, Chemicals, Electrical, Trade, Food, Life sciences, Mechanical engineering und Transport. Was jede Vorlage bietet, steht unter [Branchenvorlagen](industry-templates/README.md).

1. Öffnen Sie die Karte Ihrer Branche und schalten Sie sie ein. Die Karte zeigt dann „On · 3 agents · 3 knowledge bases“.
2. Laden Sie Dokumente in die Wissensdatenbanken hoch.
3. Zum Ausschalten wählen Sie **Switch off**. Die Assistenten verschwinden; Wissensdatenbanken und Dokumente bleiben. Beim erneuten Einschalten entstehen keine Duplikate.

Nur Administratoren sehen den Reiter **Industry templates**. Mitglieder ohne Administratorrechte nutzen den Chat und die vorhandenen Assistenten.

## Eine Frage stellen und die Quelle öffnen

Öffnen Sie den **Chat**, wählen Sie unter **Custom Agents** einen Assistenten und stellen Sie Ihre Frage. Jede Antwort mit Fundstelle zeigt einen Quellenhinweis. Ein Klick öffnet die Vorschau rechts. PDF, gescanntes PDF, Word, Markdown und Text zeigen die Stelle, an der die Antwort gefunden wurde.

* **Excel:** Die Datei öffnet sich, die Zeile wird nicht markiert. Die Vorschau meldet „Could not pinpoint the cited passage; the original is open“.
* **Bilder und Fotos:** Die Vorschau zeigt das Bild. Der darin enthaltene Text ist nicht bestätigt („exact text not confirmed“).
* Quellenhinweise können auch neben „nicht in den Unterlagen“ erscheinen. Sie nennen Dokumente, die der Assistent geprüft hat; sie sind kein Beleg für einen Wert.
* **Fragen Sie genau**, zum Beispiel mit der Dokumentnummer. Fragen Sie nach einer Nummer, die es nicht gibt, antwortet der Assistent „nicht in den Unterlagen“, statt den Wert einer ähnlichen Nummer zu nennen.

<!-- screenshot: chat answer with source reference (dev) -->

## Dokumente hochladen und den Status lesen

1. Knowledge Base → Wissensdatenbank öffnen → **Add Document** → **Upload Document**.
2. Wählen Sie Dateien. Auf der Bestätigungsseite können Sie Tags und Optionen setzen, zum Beispiel ob eine Zusammenfassung erstellt wird. Wählen Sie dann **Upload and parse**.
3. Das Upload-Panel zeigt Zähler („Parsing 0 of 7“) und Zwischenstände („Waiting to parse“, „Generating summary...“, „Searchable, still optimizing“, „Done“). Sie können die Seite verlassen; die Verarbeitung läuft weiter.

Hinweise zu Dateien:

* Die Oberfläche nennt höchstens **50 MB je Datei** für PDF, Office-Formate, Text und Markdown. Dateien dieser Größe haben wir nicht getestet.
* In unseren Tests wurden PDF, gescanntes PDF, Word, Excel, Markdown, Text und Fotos gelesen. E-Mail-Dateien (.eml) und XML-Dateien werden abgewiesen, ebenso leere Dateien.
* Dieselbe Datei erneut hochzuladen wird abgewiesen; die vorhandene bleibt unverändert.
* **Fotos:** <!-- CHECK-DEV: Foto-Upload nach Fix (FIX-FOTO). Folgende Sätze durch geprüftes Verhalten ersetzen. --> **Upload and parse** bleibt für Fotos gesperrt, bis die Bildverarbeitung („Multimodal“) eingeschaltet und ein Modell gewählt ist. Das ist eine bekannte Einschränkung.

### Status

| Anzeige | Bedeutung | Was zu tun ist |
| --- | --- | --- |
| Completed | Gelesen und durchsuchbar. | Nichts. |
| Failed | Die Verarbeitung ist fehlgeschlagen; die Meldung steht auf der Karte. | Dokument auswählen → **Rebuild Document**. Schlägt es erneut fehl, siehe [Fehlerbehebung](troubleshooting.md). |
| May be stuck | Seit einer Weile kein Fortschritt. | Zeitleiste öffnen, **Stop parsing** wählen, dann **Rebuild Document**. Ohne Eingriff wird das Dokument nach einer Weile automatisch auf Failed gesetzt. |

Die **Parsing-Zeitleiste** öffnen Sie mit einem Klick auf das Dokument. Sie zeigt die Phasen (Dokument lesen, Abschnitte bilden, Vektoren, Nachbearbeitung) mit ihrer Dauer. Bei einem Stillstand erscheint ein Hinweis: „No progress for N minutes; this may be stuck“.

Endet ein Stillstand automatisch, lautet die Fehlermeldung „task stuck in processing…“. Versuchen Sie es mit **Rebuild Document** erneut.

<!-- CHECK-DEV: Zeitleisten-Tooltip (FIX-TOOLTIP). Zeigt er noch rohe Schlüssel, Satz behalten; sonst löschen. -->
Im Tooltip der Zeitleiste zeigen einzelne Verarbeitungseinstellungen noch technische Namen statt lesbarem Text. Die Verarbeitung ist davon nicht betroffen.

## Wissensdatenbank anlegen

Knowledge Base → **Create Knowledge Base**. Sie wählen:

* **Inhaltstyp:** Documents oder FAQ.
* **Indexierung (Indexing Strategy):** „RAG Search“ zum Durchsuchen von Dokumenten, „Wiki“ für verknüpfte Wiki-Seiten. Der Wissensgraph ist ein eigener Reiter (**Knowledge Graph**).
* **Bilder:** Der Reiter **Image Processing** steuert, wie Bilder in Dokumenten verarbeitet werden.

Die Modelle für Embedding, Zusammenfassung und Bildverarbeitung sind vorgegeben; ein Embedding-Modell wählen Sie nicht. Die Indexierung können Sie ändern, solange die Wissensdatenbank leer ist, danach nicht mehr („The indexing strategy cannot be changed once the knowledge base contains content“).

<!-- CHECK-DEV: Chunk-Größe speichern (FIX-CHUNK). Warnung durch geprüftes Verhalten ersetzen. -->
{% hint style="warning" %}
**Abschnittsgröße speichern:** Das Speichern der Abschnittsgröße (**Chunking Settings**) mit **Save and Close** funktioniert derzeit nicht zuverlässig: Die Änderung kann wirkungslos bleiben, und vorhandene Einstellungen können zurückgesetzt werden. Ändern Sie diese Werte vorerst nicht. Ansehen und Schließen ohne Speichern ist unbedenklich.
{% endhint %}

## Ordner und Tags

* Der **Ordnerbaum** steht links in der Wissensdatenbank. Dokumente verschieben Sie mit **Move to folder**; sie werden nicht neu gelesen.
* Einen Ordner in seinen eigenen Unterordner zu verschieben wird abgewiesen. Umbenennen, Verschieben und Zusammenführen von Ordnern haben wir über die DocBits-Schnittstelle für Entwickler (API) getestet, nicht gesondert in der Oberfläche.
* **Tags:** Nutzen Sie **Add tags** in der Dokumentzeile, oder wählen Sie mehrere Dokumente und dann **Batch Tag**. Vorsicht: **Batch Tag ersetzt die vorhandenen Tags** der gewählten Dokumente.
* Filtern Sie nach mehreren Tags, erscheinen Dokumente, die irgendeinen dieser Tags tragen (ODER).
* Automatische Tags (Auto-Tag, höchstens 3 je Dokument) sind optional, standardmäßig aus und wirken nur auf Dokumente, die nach dem Einschalten verarbeitet werden.

## Textabschnitte bearbeiten

In einem Dokument zeigt die Abschnittsliste je Abschnitt einen Stift, den Verlauf und einen Schalter. Nach dem Speichern wird der Abschnitt neu indexiert, und Antworten nutzen den neuen Text. Frühere Fassungen bleiben im Verlauf und lassen sich wiederherstellen. Bearbeiten zwei Personen gleichzeitig denselben Abschnitt, erhält die zweite eine Konfliktmeldung („Chunk was modified by another user“) und muss neu laden. Nach einer Änderung können Sie die Zusammenfassung des Dokuments neu erzeugen oder von Hand eintragen.

## Metadaten

Jedes Dokument kann bis zu 20 eigene Felder haben (Anzeige „20/20“). Ein 21. Feld wird abgewiesen.

## Kopieren, verschieben und herunterladen

* **Wissensdatenbank kopieren** läuft im Hintergrund und übernimmt Dokumente und Ordner. Die Kopie hat denselben Namen wie das Original; benennen Sie sie um, damit Sie beide unterscheiden können.
* **Mehrfach-Download:** Dokumente auswählen → **Download selected**. Sie erhalten eine ZIP-Datei mit den Originaldateinamen. Nur Rollen mit Bearbeitungsrecht (Contributor und höher) dürfen herunterladen; Viewer nicht.
* Den Download von mehr als 200 Dokumenten oder sehr großen Mengen haben wir nicht getestet.

## Wiki, Wissensgraph und Gallery

* **Gallery** (Reiter neben Documents): zeigt **in Dokumente eingebettete** Bilder (zum Beispiel in PDF oder Word), sofern die Bildverarbeitung eingeschaltet ist. Einzeln hochgeladene Fotos erscheinen dort nicht; sie werden per Texterkennung gelesen und stehen für Fragen bereit. Die Beschreibungen der Bilder sind derzeit leer („No caption“).
* **Wiki und Wissensgraph:** Ein Graph-Assistent nennt zu einem Dokument die zugehörigen Dokumente mit Quellen, zum Beispiel welche Berichte auf einen Frachtbrief verweisen. Wir haben das an einer eigenen Demo-Wissensdatenbank getestet, noch nicht an den Branchenvorlagen. Betrachten Sie es als gebaut, aber noch nicht durchgängig getestet.

## Wochenübersicht (Automations)

**Automations** enthält je Branchenvorlage einen Assistenten, der zusammenstellt, was laut Ihren Dokumenten bald abläuft, mit Fundstelle und einem Hinweis, wo ein Datum fehlt. In unseren Tests lief die Übersicht bei manuellem Start in allen acht Branchen erfolgreich.

Einschränkungen: Sie ist standardmäßig ausgeschaltet. Das Ergebnis erscheint im Verlauf des Assistenten; es gibt keinen E-Mail-Versand. Den Start über die Oberfläche **Automations** haben wir nicht gesondert getestet. Wir haben das Ergebnis auf Erfolg und Form geprüft, nicht jede Zeile auf Richtigkeit.

## Rollen

* **Administrator:** schaltet das Modul und die Branchenvorlagen ein und aus.
* **Contributor (Standardrolle für Mitglieder):** lädt hoch, bearbeitet und löscht eigene Wissensdatenbanken und legt neue an.
* **Viewer:** liest und fragt. Hochladen, Bearbeiten, Löschen, Anlegen und Herunterladen sind für Viewer gesperrt und werden in der Oberfläche nicht angeboten.

Siehe auch: [Fehlerbehebung](troubleshooting.md) und [Was er kann und was nicht](what-it-can-and-cannot-do.md).
