# Erstellen und Bearbeiten von Skripten

{% embed url="https://youtu.be/n8NpWWIjmlA" %}
DocBits Document Scripts Explained: Automate Custom Logic in Your Document Workflow
{% endembed %}

## Um ein neues Skript in DocBits zu erstellen, folgen Sie dieser detaillierten Anleitung:

**Wählen Sie die Skriptsprache:**

Zuerst müssen Sie die Skriptsprache auswählen, die Sie verwenden möchten. DocBits unterstützt normalerweise gängige Skriptsprachen wie Python, JavaScript oder SQL. Die Wahl der Sprache hängt von den Anforderungen Ihres Projekts und Ihren eigenen Kompetenzen ab.

**Öffnen Sie die Skriptentwicklungsumgebung:**

Melden Sie sich bei DocBits an und navigieren Sie zur Skriptentwicklungsumgebung. Diese befindet sich im Administrationsbereich.

<figure><img src="../../../../../.gitbook/assets/docbits_script_example_2.png" alt="Docbits Script Dev Environment"><figcaption></figcaption></figure>

**Erstellen Sie ein neues Skript:**

Klicken Sie auf die Schaltfläche "+ Neu", um einen neuen Skripteditor zu öffnen.

<figure><img src="../../../../../.gitbook/assets/docbits_script_example_2.png" alt="Docbits New Script Editor"><figcaption></figcaption></figure>

**Skriptcode schreiben:**

Verwenden Sie den Editor, um den Code für Ihr Skript zu schreiben. Beginnen Sie mit der Basissyntax der gewählten Skriptsprache.

Wenn Sie beispielsweise Python verwenden, könnte Ihr Skript so aussehen:

## 1. Beispielskript in Python

<figure><img src="../../../../../.gitbook/assets/docbits_script_example_2.png" alt="Docbits Script Python Example"><figcaption></figcaption></figure>

## Funktion zum Bereinigen von Patientennamen

def clean\_patient\_name(name): cleaned\_name = name.strip().title() # Leerzeichen entfernen und Großschreibung anwenden

return cleaned\_name

## Hauptprogramm

if **name** == "**main**": patient\_name = " john doe " cleaned\_name = clean\_patient\_name(patient\_name) print("Bereinigter Patientenname:", cleaned\_name)

## 2. Beispielskript

<figure><img src="../../../../../.gitbook/assets/image (120).png" alt="Docbits Field Required Setting"><figcaption></figcaption></figure>

**Testen Sie das Skript:**

Überprüfen Sie den Code auf Fehler und testen Sie ihn in einer Testumgebung. Stellen Sie sicher, dass das Skript die erwarteten Ergebnisse liefert und korrekt funktioniert.

<figure><img src="../../../../../.gitbook/assets/image (120).png" alt="Docbits Field Readonly Setting"><figcaption></figcaption></figure>

**Speichern Sie das Skript:**

Speichern Sie das Skript in DocBits und geben Sie ihm einen aussagekräftigen Namen, der den Zweck des Skripts beschreibt.

<figure><img src="../../../../../.gitbook/assets/image (120).png" alt="Docbits Field Hidden Setting" width="84"><figcaption></figcaption></figure>

**Zuordnung des Skripts zu Belegtypen:**

Ein wichtiger Schritt ist die Zuordnung des Skripts zu den entsprechenden Belegtypen. Dies bestimmt, wann und wie das Skript angewendet wird. Dies kann normalerweise über eine Konfigurationsoberfläche in DocBits erfolgen, wo Sie das Skript einem bestimmten Belegtyp zuweisen und festlegen können, unter welchen Bedingungen es angewendet werden soll.

<figure><img src="../../../../../.gitbook/assets/image (120).png" alt="Docbits Field Ocr Setting"><figcaption></figcaption></figure>

**Überprüfung und Veröffentlichung:**

Nachdem Sie das Skript erstellt, getestet und zugeordnet haben, überprüfen Sie es erneut auf Fehler und Inkonsistenzen. Wenn alles in Ordnung ist, können Sie das Skript in der DocBits-Produktionsumgebung veröffentlichen.

<figure><img src="../../../../../.gitbook/assets/docbits_script_example_2.png" alt="Docbits Publish Script Button"><figcaption></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/image (120).png" alt="Docbits Field Forced Validation Setting"><figcaption></figcaption></figure>

Durch diese Schritte können Sie erfolgreich ein neues Skript in DocBits erstellen, testen und implementieren, um Prozesse zu automatisieren und die Effizienz der Dokumentation zu verbessern.
