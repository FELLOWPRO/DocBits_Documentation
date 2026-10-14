# Fehlerbehebung bei Zugriffssteuerung und Berechtigungsproblemen

Wenn Benutzer unerwartete Zugriffsbeschränkungen erleben - wie fehlende Dokumente, Unfähigkeit, Felder zu bearbeiten oder verweigerte Aktionen -, verwenden Sie die folgende Checkliste, um das Problem basierend darauf zu identifizieren und zu lösen, wie Berechtigungen in DocBits konfiguriert sind.

### 1. Überprüfen Sie, ob die Zugriffssteuerung aktiviert ist

Zugriffssteuerungseinstellungen gelten nur, wenn die Funktion **aktiviert** ist.

* Navigieren Sie zu: `Einstellungen` > `Dokumentenverarbeitung` > `Modul`.
* Stellen Sie sicher, dass der **Zugriffssteuerung**-Schalter **aktiviert** ist.
* Wenn deaktiviert, haben in der Regel alle Benutzer uneingeschränkten Zugriff, unabhängig von Gruppen- oder Feldberechtigungen.

### 2. Überprüfen Sie Gruppenzuweisungen

Stellen Sie sicher, dass der Benutzer korrekt den entsprechenden Gruppen zugeordnet ist:

* Navigieren Sie zu: `Einstellungen` > `Globale Einstellungen` > `Gruppen, Benutzer und Berechtigungen`.
* Wählen Sie **Gruppen und Berechtigungen** aus.
* Bestätigen Sie, dass der Benutzer unter der erwarteten Gruppe aufgeführt ist.
* Wenn die Gruppe spezifische Zugriffssteuerung verwendet, blockiert eine fehlende Gruppenzuweisung den Zugriff auf Dokumente und Aktionen.

### 3. Überprüfen Sie Gruppenzugriffsberechtigungen

Der Zugriff wird pro Dokumententyp und pro Aktion gewährt:

* Überprüfen Sie im **Zugriffssteuerung**-Bildschirm für die Gruppe den Dokumententyp (z. B. Rechnung, Bestellung).
* Validieren Sie Berechtigungen wie:
  * **Auflisten**, **Anzeigen**, **Bearbeiten**, **Löschen**, **Massenaktualisierung**
  * **Genehmigungsstufen** (1., 2.), **Dokument entsperren**
* Stellen Sie sicher, dass die Zugriffsebene nicht auf **Besitzer** oder **Admin** beschränkt ist, es sei denn, dies ist angemessen.

### 4. Bestätigen Sie Feldberechtigungen

Der Zugriff kann auch auf Felderebene eingeschränkt sein, was das Bearbeiten oder die Sichtbarkeit blockieren kann:

* Navigieren Sie in der Zugriffskontiguration der Gruppe zum Dokumententyp und überprüfen Sie die Einstellungen auf Felderebene.
* Bestätigen Sie, ob Felder auf Folgendes eingestellt sind:
  * **Lesen/Schreiben**, **Nur Lesen**, **Besitzer Schreiben**, **Keine**
* Passen Sie bei Bedarf basierend auf der Benutzerrolle an.

### 5. Überprüfen Sie die Einstellung "Nur zugewiesene Dokumente"

Diese globale Einstellung beschränkt die Dokumentsichtbarkeit:

* Navigieren Sie zu: `Einstellungen` > `Globale Einstellungen` > `Gruppen, Benutzer und Berechtigungen`.
* Wenn **Nur zugewiesene Dokumente** aktiviert ist, können Benutzer nur Dokumente sehen, die ihnen oder ihrer Gruppe explizit zugewiesen sind.
* Wenn Benutzer erwartete Dokumente nicht sehen können:
  * Überprüfen Sie die Dokumentenzuweisungen.
  * Deaktivieren Sie die Einstellung vorübergehend, um zu testen, ob sie die Ursache ist.

### 6. Testen mit einem bekannten funktionierenden Benutzer oder einer Gruppe

Um das Problem zu isolieren:

* Melden Sie sich mit einem Benutzer aus einer Gruppe an, der Zugriff bestätigt hat.
* Vergleichen Sie die Dokumentsichtbarkeit und verfügbaren Aktionen.
* Dies hilft festzustellen, ob das Problem benutzerspezifisch, gruppenspezifisch oder systemweit ist.

### 7. Überprüfen Sie Dokumentenzuweisungen erneut

Wenn "Nur zugewiesene Dokumente" aktiviert ist, stellen Sie sicher:

* Das Dokument ist dem Benutzer oder einer ihrer Gruppen **zugewiesen**.
* Verwenden Sie die Zuweisungssteuerelemente in der Dokumentendetailansicht, um Zuweisungen zu erstellen oder zu überprüfen.

### 8. Berechtigungen zurücksetzen oder neu konfigurieren

Wenn Berechtigungen kürzlich geändert wurden oder Benutzer zwischen Gruppen verschoben wurden:

* Bestätigen Sie erneut, dass die Zugriffssteuerungseinstellungen die neuen Gruppenkonfigurationen widerspiegeln.
* Passen Sie Feld- und Dokumentenberechtigungen bei Bedarf an.
* Wenn Sie unsicher sind, erstellen Sie eine Testgruppe mit umfangreichen Berechtigungen und testen Sie das Zugriffsverhalten, bevor Sie Änderungen an Live-Gruppen vornehmen.
