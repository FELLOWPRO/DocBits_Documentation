# Spalten bearbeiten und löschen

Alles außer dem Titel wird direkt in der Liste geändert; es gibt keinen Bearbeiten-Dialog.

**Wo:** Settings → Global Settings → Document Types → Table Columns

## Ein Flag umschalten

Aktivieren oder deaktivieren Sie das Kontrollkästchen in der Zeile. Die Änderung wird sofort gespeichert (*Successfully saved*).

| Flag | An | Aus |
|---|---|---|
| **Is Required** | Die Freigabe ist blockiert, solange die Spalte in einer beliebigen Zeile leer ist; die Validierungsmaske markiert die Zelle. | Leere Zellen sind erlaubt. |
| **Read Only** | Der Wert wird angezeigt, kann aber nicht überschrieben werden. Verwenden Sie dies für Werte, die aus einem Lookup oder einem Skript stammen. | Benutzer können die Zelle bearbeiten. |
| **Hidden** | Die Spalte verschwindet aus der Validierungsmaske und aus dem Export. Ihre Daten bleiben erhalten. | Die Spalte wird angezeigt und exportiert. |
| **Use AI** | Die KI-Tabellenextraktion füllt diese Spalte, auch bei Lieferanten mit trainierten Regeln. | Die Spalte wird durch die trainierten Regeln gefüllt, oder durch die KI, wenn keine Regeln existieren. |

{% hint style="info" %}
Flags gelten für Dokumente, die **nach** der Änderung hochgeladen oder neu gestartet werden. Offene Dokumente behalten ihre aktuelle Tabelle, bis sie neu gestartet werden.
{% endhint %}

## Den Titel umbenennen

Klicken Sie in der Spalte *Actions* auf das Übersetzungs-Symbol (*Update translation key*), geben Sie die neue Bezeichnung ein und bestätigen Sie. Das Info-Symbol daneben zeigt, welche Bezeichnung aktuell gilt und woher sie stammt. Nur die Bezeichnung ändert sich; der technische *Column name* bleibt gleich, sodass Skripte, Export-Mappings und trainierte Regeln weiter funktionieren.

## Typ oder Tabelle ändern

Nicht möglich. Blenden Sie die Spalte aus (oder löschen Sie sie, wenn es Ihre eigene ist) und fügen Sie eine neue mit dem richtigen Typ hinzu.

## Eine Spalte löschen

Die Löschen-Aktion wird nur für Spalten angeboten, die Ihre Organisation angelegt hat. Standardspalten können nicht gelöscht werden; blenden Sie sie aus.

1. Öffnen Sie das Drei-Punkte-Menü in der Spalte *Actions* und wählen Sie **Delete**. Bei Standardspalten fehlt dieser Eintrag.
2. Bestätigen Sie.

Was passiert:

* Die Spalte wird aus der Konfiguration entfernt. Dokumente, die **ab jetzt** verarbeitet werden, haben sie nicht mehr.
* Bereits extrahierte Dokumente behalten die Spalte und ihre Werte, bis sie neu gestartet werden.
* Trainierte Regeln, die diese Spalte zugeordnet hatten, funktionieren für die anderen Spalten weiter; die Zuordnung zur gelöschten Spalte wird ignoriert.
* Wird die Spalte in einem Export-Mapping oder einem Skript referenziert, entfernen Sie diesen Verweis; andernfalls schlägt der Export oder das Skript mit einem Fehler wegen einer fehlenden Spalte fehl.

## Ein Löschen rückgängig machen

Eine gelöschte Spalte kann nicht aus der Liste wiederhergestellt werden. Fügen Sie sie mit demselben Titel erneut hinzu: Der technische Name wird aus dem Titel abgeleitet, daher erhält eine Spalte mit demselben Titel denselben *Column name*, und bestehende Mappings passen wieder.
