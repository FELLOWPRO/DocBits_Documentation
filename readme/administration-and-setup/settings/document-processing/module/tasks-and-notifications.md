# Aufgaben und Benachrichtigungen

### Überblick

Die Einstellung **Aufgaben und Benachrichtigungen** aktiviert die integrierte Aufgabenverwaltung von DocBits. Wenn sie aktiviert ist, können Teammitglieder Aufgaben erstellen, sich gegenseitig Dokumente zuweisen (z. B. zur Validierung, Korrektur oder Genehmigung) und Benachrichtigungen dazu erhalten.

Diese Einstellung ist **standardmäßig deaktiviert**. Wenn sie aktiviert ist, erscheinen darunter vier weitere Optionen:

* **Aufgabenanzahl im Dashboard**: zeigt im Dashboard an, welche Dokumente offene Aufgaben haben.
* **„Alle“-Filter für Nicht-Admins erlauben**: Benutzer ohne Administratorrechte dürfen alle Aufgaben sehen.
* **Aufgabenlöschung durch Nicht-Administratoren**: legt fest, welche Aufgaben Benutzer ohne Administratorrechte löschen dürfen.
* **Erledigung von Aufgaben ohne Administratorrechte**: legt fest, welche Aufgaben Benutzer ohne Administratorrechte abschließen dürfen.

Für Administratoren der Organisation gelten diese Einschränkungen nie.

### Was bewirkt die Einstellung?

* **Aktiviert**: Die Funktionen für Aufgaben und Benachrichtigungen werden in DocBits verfügbar. Benutzer können Aufgaben zuweisen, ihren Status verfolgen und benachrichtigt werden, wenn etwas ihre Aufmerksamkeit erfordert.
* **Deaktiviert**: Aufgabenzuweisung und die zugehörigen Benachrichtigungen sind ausgeschaltet. Dabei wird auch **Aufgabenanzahl im Dashboard** ausgeschaltet.

### Aufgabenanzahl im Dashboard
Die Option **Aufgabenanzahl im Dashboard** steuert, ob das Dashboard anzeigt, welche Dokumente offene Aufgaben haben. Sie blendet keinen Zähler ein, sondern ein Aufgabensymbol am jeweiligen Dokument.

* **Aktiviert**: Ein Dokument mit Aufgaben im Status **Offen** oder **In Arbeit** zeigt in der Dashboard-Liste ein Aufgabensymbol. Wenn Sie mit der Maus über das Symbol fahren, sehen Sie, wie viele offene Aufgaben das Dokument hat, z. B. „2 Offene Aufgabe(n)“. Erledigte, abgelehnte und gelöschte Aufgaben werden nicht mitgezählt.
* **Deaktiviert**: Das Symbol wird ausgeblendet. Aufgaben funktionieren weiterhin normal.

{% hint style="info" %}
**Aufgabenanzahl im Dashboard** hängt von **Aufgaben und Benachrichtigungen** ab. Wenn Sie Aufgaben und Benachrichtigungen ausschalten, wird auch die Aufgabenanzeige im Dashboard ausgeschaltet.
{% endhint %}

### „Alle“-Filter für Nicht-Admins erlauben

Die Aufgabenübersicht hat einen Filter **Zugewiesen an** mit den Optionen **Alle** und **Mir zugewiesen**. Administratoren stehen immer beide Optionen zur Verfügung.

* **Aktiviert**: Auch Benutzer ohne Administratorrechte können **Alle** wählen und sehen dann alle Aufgaben der Organisation.
* **Deaktiviert** (Standard): Benutzer ohne Administratorrechte erhalten nur **Mir zugewiesen**; die Übersicht zeigt ihnen also die Aufgaben, die ihnen zugewiesen sind.

### Aufgabenlöschung durch Nicht-Administratoren

**Aufgabenlöschung durch Nicht-Administratoren** legt fest, welche Aufgaben und Benachrichtigungen Benutzer ohne Administratorrechte löschen dürfen. Administratoren können immer alle Aufgaben löschen.

| Option | Benutzer ohne Administratorrechte dürfen löschen |
| --- | --- |
| **Keine** | Keine Aufgaben. |
| **Nur erstellte Aufgaben** | Aufgaben, die sie selbst erstellt haben. |
| **Erstellte und zugewiesene Aufgaben** | Aufgaben, die sie selbst erstellt haben, sowie Aufgaben, die ihnen oder einer ihrer Gruppen zugewiesen sind. Das gilt, solange die Option nie geändert wurde. |
| **Alle Aufgaben** | Alle Aufgaben. |

Benutzer können die Aufgaben, die sie selbst erstellt haben, immer löschen, außer bei **Keine**. Eine Aufgabe, die niemandem zugewiesen ist, können daher nur der Benutzer, der sie erstellt hat, Administratoren oder Benutzer bei **Alle Aufgaben** löschen. Eine Aufgabe ohne gespeicherten Ersteller, zum Beispiel eine vom System erstellte, können nur die Benutzer, denen sie zugewiesen ist (bei **Erstellte und zugewiesene Aufgaben**), Administratoren oder Benutzer bei **Alle Aufgaben** löschen.

{% hint style="warning" %}
Wird eine Aufgabe gelöscht, verschwindet sie ohne Entscheidung aus der Aufgabenliste. Sollen Aufgaben nur durch eine Entscheidung abgeschlossen werden, stellen Sie **Aufgabenlöschung durch Nicht-Administratoren** auf **Keine** und **Erledigung von Aufgaben ohne Administratorrechte** (siehe unten) auf **Nur für Administratoren**.
{% endhint %}

### Erledigung von Aufgaben ohne Administratorrechte

**Erledigung von Aufgaben ohne Administratorrechte** legt fest, welche Benutzer ohne Administratorrechte eine Aufgabe abschließen, also auf **Fertig** oder **Abgelehnt** setzen dürfen. Administratoren können Aufgaben immer abschließen, unabhängig von der Auswahl hier.

| Option | Wer eine Aufgabe abschließen darf |
| --- | --- |
| **Standardverhalten** | Die Einstellung schränkt nichts ein. Benutzer können die Aufgaben abschließen, die ihnen oder einer ihrer Gruppen zugewiesen sind, wie vor Einführung der Einstellung. Das gilt, solange die Option nie geändert wurde. |
| **Administratoren und zugewiesene Benutzer** | Administratoren sowie die Benutzer, denen die Aufgabe direkt oder über eine ihrer Gruppen zugewiesen ist. Eine Aufgabe, die jemand anderem oder niemandem zugewiesen ist, können andere Benutzer nicht abschließen. DocBits prüft das auch, wenn eine Aufgabe über die API geändert wird. |
| **Nur für Administratoren** | Nur Administratoren. |

Bei **Administratoren und zugewiesene Benutzer** oder **Nur für Administratoren** gilt für einen Benutzer, der eine Aufgabe nicht abschließen darf:

* Er sieht auf der Aufgabenseite die grüne Schaltfläche **Fertig** nicht, und die Statusliste dort bietet nur **Offen** und **In Arbeit** an.
* Er kann im Aufgabenbereich des Dokuments nicht auf den Statuskreis der Aufgabe klicken. Beim Darüberfahren mit der Maus erscheint „Es ist Ihnen nicht gestattet, diese Aufgabe als erledigt oder abgelehnt zu markieren.“
* Er sieht in der Aufgabenliste **Als erledigt markieren** für diese Aufgabe nicht, und **Als erledigt markieren** für eine Auswahl ist ausgeblendet, solange eine solche Aufgabe ausgewählt ist.
* Er kann die Aufgabe im Aufgaben-Board nicht in die Spalte **Fertig** oder **Abgelehnt** ziehen. Die Karte springt in ihre Spalte zurück, und dieselbe Meldung wird angezeigt.

Die Einstellung schränkt nur das Abschließen ein. Alle anderen Rechte, die Benutzer vorher hatten, behalten sie: Benutzer, denen eine Aufgabe zugewiesen ist, können sie weiterhin bearbeiten, speichern, zwischen **Offen** und **In Arbeit** verschieben und nach dem Erledigen wieder öffnen. Benutzer, denen eine Aufgabe nicht zugewiesen ist, konnten ihren Status schon vorher nicht ändern und können es weiterhin nicht.

Bei Dokumenttypen mit aktiviertem **Genehmigungsverlauf** schließt **Genehmigen** weiterhin offene Aufgaben des Dokuments ab, unabhängig von der Auswahl hier: die Aufgaben, die dem Genehmiger oder einer seiner Gruppen zugewiesen sind, und die Aufgaben, die niemandem zugewiesen sind. Ist der Genehmiger Administrator, werden alle offenen Aufgaben des Dokuments abgeschlossen.

#### Aufgaben an Dokumenten, die zur Validierung zurückgeschickt werden

Da Benutzer bei **Administratoren und zugewiesene Benutzer** oder **Nur für Administratoren** ihre eigenen Aufgaben nicht selbst abschließen können, schließt DocBits die offenen Aufgaben eines Dokuments selbst ab, wenn ein Dokument, das auf Genehmigung wartet, zur Validierung zurückgeschickt wird:

* **Workflow neu starten** in der Genehmigungsansicht: Alle offenen Aufgaben des Dokuments werden abgelehnt.
* **Ablehnen und korrigieren**: Alle offenen Aufgaben des Dokuments werden abgelehnt.
* **Genehmigen und korrigieren**: Die Aufgaben, die **Genehmigen** abschließen würde (siehe oben), werden abgeschlossen, nur bei Dokumenttypen mit aktiviertem **Genehmigungsverlauf**. Alle übrigen offenen Aufgaben werden abgelehnt.

Die offenen Aufgaben werden abgeschlossen, bevor das Dokument zur Validierung zurückkehrt. Workflows, die bei der Statusänderung laufen, können anschließend neue Aufgaben für alles anlegen, was noch Aufmerksamkeit erfordert.

Bei **Standardverhalten** bleiben offene Aufgaben offen, wenn ein Dokument zurückgeschickt wird, wie bisher.

### Vorteile

* **Klare Zuständigkeiten**: Dokumente können der richtigen Person zugewiesen werden, statt sich auf E-Mails zu verlassen.
* **Nichts wird vergessen**: Benachrichtigungen erinnern Benutzer an Dokumente, die ihr Handeln erfordern.
* **Offene Arbeit auf einen Blick**: Mit **Aufgabenanzahl im Dashboard** zeigt das Dashboard, welche Dokumente noch offene Aufgaben haben.
* **Entscheidungen bleiben nachvollziehbar**: Mit den Optionen zum Löschen und Abschließen verlassen Aufgaben die Warteschlange nur durch eine Entscheidung oder durch einen Administrator.

### Verwendung

1. Gehen Sie zu **Einstellungen**.
2. Wählen Sie **Verarbeitung von Dokumenten**.
3. Wählen Sie **Module**.
4. Öffnen Sie den Abschnitt **Dokumenttyp**.
5. Schalten Sie **Aufgaben und Benachrichtigungen** ein.
6. (Optional) Schalten Sie **Aufgabenanzahl im Dashboard** ein, um das Aufgabensymbol im Dashboard anzuzeigen.
7. (Optional) Schalten Sie **„Alle“-Filter für Nicht-Admins erlauben** ein, wenn alle Benutzer alle Aufgaben sehen sollen.
8. (Optional) Wählen Sie unter **Aufgabenlöschung durch Nicht-Administratoren**, welche Aufgaben Benutzer löschen dürfen.
9. (Optional) Wählen Sie unter **Erledigung von Aufgaben ohne Administratorrechte**, wer Aufgaben abschließen darf.

Die Optionen zum Löschen und Abschließen werden gespeichert, sobald Sie einen Wert auswählen.

### Wann diese Funktion nutzen

* **Teams, die sich Dokumentarbeit teilen**: Aktivieren Sie sie, wenn mehrere Personen Dokumente validieren oder genehmigen und Arbeit aneinander übergeben müssen.
* **Sichtbarkeit der Arbeitslast**: Aktivieren Sie zusätzlich **Aufgabenanzahl im Dashboard**, wenn das Team im Dashboard sehen soll, welche Dokumente noch offene Aufgaben haben.
* **Aufgaben, die nur Administratoren oder eine Entscheidung abschließen sollen**: Stellen Sie **Erledigung von Aufgaben ohne Administratorrechte** auf **Nur für Administratoren** oder **Administratoren und zugewiesene Benutzer** und **Aufgabenlöschung durch Nicht-Administratoren** auf **Keine**, wenn Benutzer Aufgaben, die nicht tatsächlich erledigt wurden, nicht entfernen dürfen.
* **Einzelnutzer- oder vollautomatische Setups**: Sie können sie ausgeschaltet lassen, wenn niemand Dokumente zuweisen oder Aufgaben verfolgen muss.
