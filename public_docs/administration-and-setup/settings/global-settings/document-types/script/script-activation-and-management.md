# Skriptaktivierung und -verwaltung

Administratoren können **Skripte** verwenden, um Verarbeitungsregeln für einen Dokumenttyp zu verwalten. Diese Anleitung zeigt, wo Sie Skripte finden, wie Sie sie ein- oder ausschalten und wie Sie ein veröffentlichtes Skript sicher ändern.

## Videoanleitung: Skripte verwalten

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/doc-config-manage-scripts/v4/de.mp4" %}
Skripte eines Dokumenttyps verwalten
{% endembed %}

Das Video zeigt die Skriptliste mit Filter und Sortierung, das Aktivieren und Deaktivieren, das Kopieren, den Versionsverlauf und das Löschen mit Rückfrage.

## Ein Skript finden

1. Öffnen Sie **Einstellungen → Dokumenttypen**.
2. Wählen Sie beim gewünschten Dokumenttyp **Skripte** aus. Die Seite listet die Skripte für diesen Dokumenttyp auf.
3. Suchen Sie nach Name oder grenzen Sie die Liste mit **Alle**, **Aktiv** und **Inaktiv** ein. Sie können sie auch nach Name oder Änderungsdatum sortieren.

Jede Karte zeigt den Skriptnamen, seine Ausführungsreihenfolge als nummerierten Chip, den Auslöser, die Version und den Status. Das Stift-Symbol öffnet den Editor; das Kopieren-Symbol dupliziert das Skript. **Neu** öffnet den Editor für ein neues Skript.

<figure><img src="../../../../../.gitbook/assets/dbdc-653-script-scripts-list-de-20261110.png" alt="Skriptliste des Dokumenttyps Rechnung mit Suchfeld, den Filtern Alle, Aktiv und Inaktiv, der Sortierung und drei Skriptkarten; jede Karte zeigt neben dem Skriptnamen einen nummerierten Chip mit der Ausführungsreihenfolge 10, 20 oder 30"><figcaption><p>Der nummerierte Chip auf jeder Karte ist die Ausführungsreihenfolge des Skripts.</p></figcaption></figure>

## Ausführungsreihenfolge festlegen

Mit dem Feld **Execution order** steuern Sie, in welcher Reihenfolge Skripte laufen: kleinere Zahlen laufen zuerst. Das Feld ist auch in der deutschen Oberfläche englisch beschriftet.

1. Öffnen Sie das Skript im Editor.
2. Geben Sie im Feld **Execution order** eine ganze Zahl ab 0 ein. Lassen Sie das Feld leer, um 0 zu behalten.
3. Speichern Sie das Skript. Buchstaben, Dezimalzahlen und negative Zahlen werden mit einer Fehlermeldung am Feld abgelehnt, und es wird nichts gespeichert.

Wenn Sie die Ausführungsreihenfolge ändern und danach eine Version aktivieren, speichert DocBits zuerst das Skript und aktiviert die Version erst, wenn dieses Speichern erfolgreich war.

<figure><img src="../../../../../.gitbook/assets/dbdc-653-script-execution-order-field-de-20261110.png" alt="Feldzeile im Skript-Editor mit Name, Dokumenttyp, Auslöser, dem Feld Execution order mit dem Wert 10 und der Auswahl für den Unterdokumenttyp"><figcaption><p>Die Ausführungsreihenfolge steht im Feld <strong>Execution order</strong>.</p></figcaption></figure>

## Ein Skript aktivieren oder deaktivieren

Verwenden Sie den Schalter **Aktiv/Inaktiv** auf der Skriptkarte. Die Änderung wird sofort gespeichert; die Zähler der Liste aktualisieren sich entsprechend. Ein inaktives Skript bleibt zum Ansehen oder Bearbeiten verfügbar, läuft aber während der Dokumentenverarbeitung nicht.

**Prüfen Sie den Status nach dem Erstellen eines Skripts.** In der aktuellen Sandbox-Oberfläche wurde beim Speichern eines neuen Skripts eine aktive Version angelegt und die Karte auf **Aktiv** gesetzt. Stellen Sie den Schalter auf **Inaktiv**, wenn es nur ein Entwurf oder ein Testbeispiel ist.

<figure><img src="../../../../../.gitbook/assets/dbdc-653-script-card-status-de-20261110.png" alt="Eine Skriptkarte mit dem Chip für die Ausführungsreihenfolge, dem Auslöser Nach der Extraktion, der Version v2, den Symbolen für Bearbeiten, Kopieren und Löschen sowie dem Schalter Inaktiv"><figcaption><p>Rechts auf der Karte: Stift zum Bearbeiten, Kopieren, Papierkorb zum Löschen und der Schalter <strong>Aktiv/Inaktiv</strong>.</p></figcaption></figure>

## Ein bestehendes Skript ändern

1. Wählen Sie die Skriptkarte oder ihr Stift-Symbol aus. Eine veröffentlichte Version ist schreibgeschützt, Sie können sie nicht direkt überschreiben.
2. Wählen Sie im **Versionsverlauf** das Stift-Symbol der Version aus, die Sie ändern möchten. Dadurch wird ein **Entwurf** auf Grundlage dieser Version erstellt.
3. Bearbeiten Sie den Entwurf und wählen Sie das Speichern-Symbol. Prüfen Sie vor dem Speichern Name, Dokumenttyp, Auslöser und Code.
4. Testen Sie das geänderte Skript mit repräsentativen Dokumenten in einer Testumgebung. Wenn es bereit ist, wählen Sie das Häkchen-Symbol für den Entwurf im **Versionsverlauf**, um diese Version aktiv zu machen.
5. Kehren Sie zur Skriptliste zurück und prüfen Sie den Schalter **Aktiv/Inaktiv** der Karte. Die im Versionsverlauf mit **AKTIV** markierte Version bezeichnet die ausgewählte Version; der Kartenschalter steuert, ob das Skript ausgeführt wird.

<figure><img src="../../../../../.gitbook/assets/dbdc-653-script-published-version-de-20261110.png" alt="Veröffentlichte Skriptversion als schreibgeschützt dargestellt, mit dem Hinweis, sie als Entwurf zu kopieren, und dem Versionsverlauf rechts"><figcaption><p>Eine veröffentlichte Version kann nicht direkt bearbeitet werden. Verwenden Sie den Stift im Versionsverlauf, um einen Entwurf zu erstellen.</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/dbdc-653-script-editable-draft-de-20261110.png" alt="Bearbeitbarer Entwurf im Versionsverlauf neben der aktuell aktiven Skriptversion"><figcaption><p>Speichern und prüfen Sie den Entwurf, bevor Sie ihn zur aktiven Version machen.</p></figcaption></figure>

Beispielskripte und verfügbare Funktionen finden Sie unter [Skripterstellung in DocBits](scripting-in-docbits/README.md).

Wie Sie ein Skript erstellen, den Editor bedienen (Formatierung, Zurücksetzen des Entwurfs, KI-Assistent) und den Code eingeben, beschreibt die Seite [Erstellen und Bearbeiten von Skripten](creating-and-editing-scripts.md).

Das Papierkorb-Symbol in der Skriptliste löscht ein Skript endgültig; das Pfeil-Symbol in einer Versionszeile des Versionsverlaufs lädt eine ältere Version als Entwurf in den Editor.
