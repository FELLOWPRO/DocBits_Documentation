---
hidden: true
---

# Fuzzy-Daten mit Wertelisten konfigurieren

### **Überblick**

Jeder Dokumenttyp hat eigene Konfigurationen für Wertelisten (List of Values, LoV), die separat eingerichtet werden müssen. Anders als bei **Fuzzy Data with Master Data** werden bei **List of Values** keine Standard-Lookup-Gruppen mitgeliefert.

### Um List of Values zu konfigurieren, navigieren Sie zu:

Settings → Global Settings → Document Types → Invoice → Fields → Master Data Settings → LOV Master Data

### **Neue List-of-Values-Konfiguration erstellen**

Es gibt zwei Möglichkeiten, eine List-of-Values-Konfiguration zu erstellen:

**1. Vorhandenen Lookup duplizieren**

* Dabei werden alle Informationen und Felder einer vorhandenen Gruppe kopiert.
* Sie müssen nur einen **neuen Namen** angeben.

**2. Lookup von Grund auf neu erstellen**

* Klicken Sie auf **„Create List of Values“**.
* Füllen Sie die erforderlichen Angaben aus:
  * **Configuration Name** → Name der List of Values.
  * **Lookup Table** → Die Tabelle, aus der die Werte abgerufen werden.
  * **Conflict Handler** → Wählen Sie eine Option:
    * Best Score
    * Return None
    * Return First
  * **Context Type** → Legt fest, ob die LoV auf **Header**- oder **Line**-Ebene gilt.
  * **Match All** → _(Weitere Details erforderlich)_

### **Felder innerhalb einer List-of-Values-Gruppe verwalten**

Jede LoV-Gruppe enthält Felder, die **hinzugefügt, entfernt oder bearbeitet** werden können.

**Neues Feld hinzufügen**

Um ein neues Feld in einer Gruppe hinzuzufügen:

* Klicken Sie in der betreffenden Gruppe auf **„Create“**.
* Geben Sie die folgenden Details an:
  * **Lookup Field** → Der Spaltenname aus der Lookup-Tabelle.
  * **Validation Field** → Das entsprechende DocBits-Feld.
  * **Parent Field** → _(Weitere Details erforderlich)_
  * **Search Operator** → Wählen Sie eine Option:
    * Smart
    * Contains
    * Exact
    * Starts with
    * Ends with
  * **Kontrollkästchen:**
    * **Auto Trigger** → Wenn aktiviert und ein Feld in einer anderen Lookup-Konfiguration dieselbe Spalte verwendet, wird dieses Feld **automatisch** aktualisiert, sobald das andere Feld aktualisiert wird.
    * **Searchable** → Aktiviert das Feld als **List-of-Values**-Feld und ermöglicht Suchen in der Lookup-Tabelle.

#### **Letzter Schritt: Felder zum Layout hinzufügen**

Nachdem Sie die List-of-Values-Felder konfiguriert haben, **fügen Sie sie unbedingt mit dem Layout Builder zum Layout hinzu**. Felder, die nicht zum Layout hinzugefügt wurden, stehen nicht zur Verfügung.
