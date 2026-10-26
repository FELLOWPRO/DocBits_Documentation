# Erstellen und Bearbeiten von Skripten

{% embed url="https://youtu.be/n8NpWWIjmlA" %}
DocBits-Dokumentskripte: individuelle Logik im Dokumenten-Workflow automatisieren
{% endembed %}

## Um ein neues Skript in DocBits zu erstellen, folgen Sie dieser detaillierten Anleitung:

**Wählen Sie die Skriptsprache:**

Wählen Sie einen Scripttyp und eine Sprache, die der Editor und die Runtime Ihrer DocBits-Installation tatsächlich anbieten. Verfügbare Typen und Ausführungskontexte hängen von der eingesetzten Version ab.

**Öffnen Sie die Skriptentwicklungsumgebung:**

Melden Sie sich bei DocBits an und navigieren Sie zur Skriptentwicklungsumgebung. Diese befindet sich im Administrationsbereich.

<figure><img src="../../../../../.gitbook/assets/s150-bildschirmfoto-2024-05-08-um-09-43-25-de.png" alt="Scriptliste mit ausgeblendeten Namen, Datumsangaben und Organisationsdaten."><figcaption><p>Scriptliste mit ausgeblendeten Namen, Datumsangaben und Organisationsdaten.</p></figcaption></figure>

**Erstellen Sie ein neues Skript:**

Klicken Sie auf die Schaltfläche "+ Neu", um einen neuen Skripteditor zu öffnen.

<figure><img src="../../../../../.gitbook/assets/s150-bildschirmfoto-2024-05-08-um-09-43-37-de.png" alt="Editor für ein neues Script mit der bereitgestellten Startvorlage; sie ist vom eigenständigen Python-Beispiel unten zu unterscheiden."><figcaption><p>Editor für ein neues Script mit der bereitgestellten Startvorlage; sie ist vom eigenständigen Python-Beispiel unten zu unterscheiden.</p></figcaption></figure>

**Skriptcode schreiben:**

Verwenden Sie den Editor, um den Code für Ihr Skript zu schreiben. Beginnen Sie mit der Basissyntax der gewählten Skriptsprache.

Wenn Sie beispielsweise Python verwenden, könnte Ihr Skript so aussehen:

## 1. Beispielskript in Python



## Funktion zum Bereinigen von Patientennamen

Dieses eigenständige Python-Beispiel zeigt die Syntax. Es ist kein verifizierter DocBits-Lifecycle-Hook; passen Sie es vor der Verwendung an den dokumentierten Scriptkontext an.

```python
def clean_patient_name(name):
    cleaned_name = name.strip().title()
    return cleaned_name

if __name__ == "__main__":
    patient_name = " john doe "
    cleaned_name = clean_patient_name(patient_name)
    print("Cleaned patient name:", cleaned_name)
```

## 2. Beispielskript



**Testen Sie das Skript:**

Überprüfen Sie den Code auf Fehler und testen Sie ihn in einer Testumgebung. Stellen Sie sicher, dass das Skript die erwarteten Ergebnisse liefert und korrekt funktioniert.



**Speichern Sie das Skript:**

Speichern Sie das Skript in DocBits und geben Sie ihm einen aussagekräftigen Namen, der den Zweck des Skripts beschreibt.



**Zuordnung des Skripts zu Belegtypen:**

Ein wichtiger Schritt ist die Zuordnung des Skripts zu den entsprechenden Belegtypen. Dies bestimmt, wann und wie das Skript angewendet wird. Dies kann normalerweise über eine Konfigurationsoberfläche in DocBits erfolgen, wo Sie das Skript einem bestimmten Belegtyp zuweisen und festlegen können, unter welchen Bedingungen es angewendet werden soll.



**Überprüfung und Veröffentlichung:**

Nachdem Sie das Skript erstellt, getestet und zugeordnet haben, überprüfen Sie es erneut auf Fehler und Inkonsistenzen. Wenn alles in Ordnung ist, können Sie das Skript in der DocBits-Produktionsumgebung veröffentlichen.





Durch diese Schritte können Sie erfolgreich ein neues Skript in DocBits erstellen, testen und implementieren, um Prozesse zu automatisieren und die Effizienz der Dokumentation zu verbessern.
