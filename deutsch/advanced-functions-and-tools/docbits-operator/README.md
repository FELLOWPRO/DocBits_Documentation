# DocBits Operator

## Übersicht

Der **DocBits Operator** ist ein KI-gestützter Automatisierungsassistent, der entwickelt wurde, um wiederkehrende Aufgaben in Ihren Workflows zu vereinfachen. Benutzer erstellen _Prompts_ – schrittweise Anleitungen, die mit Variablen erweitert sind –, die die KI anleiten, automatisch durch Oberflächen zu navigieren, Daten einzugeben und zu klicken. Dies reduziert den manuellen Aufwand und beschleunigt Routineaufgaben.

## Den DocBits Operator aktivieren

Um den DocBits Operator zu aktivieren, befolgen Sie diese Schritte:

1. **Zu den Einstellungen navigieren**:
   * Gehen Sie vom Dashboard zu **Settings**.
   *   Wählen Sie **Document Processing** und dann **Module**.

       <figure><img src="../../.gitbook/assets/docbits_operator_module_selection.png" alt="Modulauswahl des DocBits Operators"><figcaption></figcaption></figure>
2. **Funktion aktivieren**:
   * Scrollen Sie nach unten, um die Option **DocBits Operator** zu finden.
   *   Schieben Sie den Regler, um den **DocBits Operator** zu aktivieren.

       <div align="left"><figure><img src="../../.gitbook/assets/docbits_operator_enable_toggle.png" alt="Schalter zum Aktivieren des DocBits Operators" width="563"><figcaption></figcaption></figure></div>

## Zugriff auf die Oberfläche

* Sobald die Funktion aktiviert ist, öffnen Sie den **DocBits Operator** im Hauptnavigationsmenü.

### **1. Prompt-Eingabe**

Am unteren Bildschirmrand befindet sich ein Eingabefeld mit der Bezeichnung _„Enter your prompt here…“_. Hier schreiben Benutzer Anweisungen, denen der Operator folgen soll.

Neben dem Eingabefeld befinden sich mehrere Schaltflächen:

* **Prompt Variables** – Öffnet ein Popup, in dem Sie Schlüssel-Wert-Paare eingeben können, die im Prompt verwendet werden. Variablen werden in geschweiften Klammern geschrieben, z. B. `{invoice_number}` oder `{url}`. Diese Werte gelten nur für den aktuellen Prompt im Eingabefeld.
* **Save Prompt** – Speichert den aktuellen Prompt. Wählen Sie, ob Sie ihn speichern möchten als:
  * **Organization Prompt** – Innerhalb Ihrer Organisation bearbeitbar; enthält sowohl den Prompt als auch die definierten Variablenwerte.
  * **Global Prompt** – Über alle Mandanten hinweg gemeinsam genutzt; enthält nur den Prompt und Platzhalter für Variablen (es werden keine Werte gespeichert).
* **Clear Chat** – Löscht das aktuelle Gespräch mit dem Operator, lässt den Prompt im Eingabefeld jedoch unverändert. Nützlich beim Wiederverwenden oder Verfeinern eines Prompts.

Ausführliche Anleitungen zum Schreiben effektiver Prompts – einschließlich Syntax, Variablen und Beispielen – finden Sie im [**Leitfaden zum Schreiben von Prompts**](prompt-writing-guide.md).

### **2. Navigation in der Seitenleiste**

Verwenden Sie das Symbol oben links, um die Seitenleiste zu öffnen oder zu schließen. Die Seitenleiste zeigt gespeicherte Prompts, die in zwei Kategorien organisiert sind:

* **Organization Prompts**: Bearbeitbar und wiederverwendbar innerhalb Ihrer Organisation.
* **Global Prompts**: Über alle Mandanten hinweg gemeinsam genutzt. Diese können keine Variablen speichern und weder bearbeitet noch gelöscht werden.
  * Ein globaler Prompt ist jedoch weiterhin durch die **Organisation, die ihn erstellt hat**, bearbeit- und löschbar; dort erscheint er unter Organization Prompts.
* **Suchfunktion:** Eine Suchleiste oben in der Seitenleiste ermöglicht es Benutzern, gespeicherte Prompts schnell nach Namen oder Stichwort zu finden.
* **Symbolreferenz:** Jeder gespeicherte Prompt hat eine Reihe von Aktionssymbolen
  * **Pfeil** – Startet den Prompt
  * **Stift** – Bearbeitet den Prompt (nur für die Prompts Ihrer eigenen Organisation verfügbar)
  * **Mülleimer** – Löscht den Prompt (nur für die Prompts Ihrer eigenen Organisation verfügbar)

### 3. Prompt speichern

Ein Klick auf die Schaltfläche **Save Prompt** öffnet ein Popup, in dem Sie den aktuellen Prompt für die künftige Verwendung speichern können.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_notification_card_overview.png" alt="Popup „Save Prompt“"><figcaption></figcaption></figure></div>

#### **Felder im Popup „Save Prompt“**

* **Prompt Name:** Geben Sie einen Namen ein, um den Prompt zu identifizieren.
* **Save Prompt Publicly (Checkbox):** Wenn aktiviert, wird der Prompt als **Global Prompt** gespeichert. Globale Prompts werden über alle Mandanten hinweg geteilt und können keine Variablen**werte** speichern (nur Variablen**namen**).
* **Edit Variables:** Öffnet das [**Popup für Prompt-Variablen**](prompt-writing-guide.md#popup-fur-aufforderungsvariablen), um Variablendefinitionen vor dem Speichern zu prüfen oder anzupassen.

**Aktionen**

* **Cancel:** Schließt das Popup, ohne zu speichern.
* **Save:** Speichert den Prompt unter dem angegebenen Namen und mit der gewählten Sichtbarkeit.

### 4. Steuerelemente zur Prompt-Ausführung

Während ein Prompt läuft, stehen Benutzern mehrere Steuerungsoptionen zur Verfügung, um die Ausführung zu verwalten oder einzugreifen:

* **Pause Prompt:** Hält die aktuelle Ausführung vorübergehend an. Nützlich, wenn Sie den aktuellen Zustand beobachten oder das System auf die nächsten Schritte vorbereiten möchten.&#x20;
* **Resume Prompt:** Setzt die Ausführung an dem Punkt fort, an dem sie pausiert wurde. ![](<../../.gitbook/assets/image (3) (1).png>)
* **Cancel Prompt:** Beendet die Ausführung vollständig und setzt die Sitzung zurück. Dies ist hilfreich, wenn der Prompt wegen falschen Verhaltens oder geänderter Eingaben abgebrochen oder neu gestartet werden muss.&#x20;
* **Take Control:** Ermöglicht es dem Benutzer, manuell einzugreifen, indem er direkt mit dem System interagiert. Dies ist nützlich, wenn der Operator hängen bleibt oder einen Schritt falsch interpretiert. Die Übernahme der Kontrolle **pausiert den Prompt automatisch** und wechselt in den manuellen Modus, bis Sie sich entscheiden fortzufahren oder abzubrechen.

### 5. Detailansicht des Operators

Sobald ein Prompt gestartet ist, steht eine zusätzliche Schaltfläche zur Verfügung, mit der Benutzer zu einer **detaillierten Ausführungsansicht** wechseln können. ![](<../../.gitbook/assets/Detailed view .jpg>)

* **Open Detail View:** Diese Schaltfläche führt Sie zu einer eigenen Ansicht, die Schritt für Schritt zeigt, was der Operator in Echtzeit tut.

In der Detailansicht können Benutzer:

* jede ausgeführte Aktion überwachen (z. B. Klicks, Eingaben, Wartezeiten),
* sehen, welcher Schritt gerade aktiv ist,
* erkennen, wo Probleme auftreten, wenn der Prompt auf Schwierigkeiten stößt,
* dieselben Aktionen **Pause**, **Resume**, **Cancel** und **Take Control** verwenden.

<div align="left"><figure><img src="../../.gitbook/assets/detailed view 2 .jpg" alt="" width="563"><figcaption></figcaption></figure></div>
