# DocBits Operator

## Übersicht

Der **DocBits Operator** ist ein KI-gestützter Automatisierungsassistent, der entwickelt wurde, um wiederkehrende Aufgaben in Ihren Workflows zu vereinfachen. Benutzer erstellen _Prompts_ - schrittweise Anleitungen, die mit Variablen verbessert sind - die die KI anleiten, automatisch durch Oberflächen zu navigieren, Daten einzugeben und zu klicken. Dies reduziert den manuellen Aufwand und beschleunigt Routineoperationen.

## Aktivieren des DocBits Operators

Um den DocBits Operator zu aktivieren, befolgen Sie diese Schritte:

1. **Navigieren zu Einstellungen**:
   * Gehen Sie vom Dashboard zu **Einstellungen**.
   *   Wählen Sie **Dokumentenverarbeitung** und dann **Modul**.

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4Yyo7aXyVeWyfJHclHpK%252Fimage.png%3Falt%3Dmedia%26token%3D0071c149-3ea8-452b-a2e3-0fbbc9d3b496\&width=768\&dpr=4\&quality=100\&sign=23009aa7\&sv=2)
2. **Funktion aktivieren**:
   * Scrollen Sie nach unten, um die Option **DocBits Operator** zu finden.
   *   Schieben Sie den Regler, um den **DocBits Operator** zu aktivieren.

       <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FyqNyGI2OelO415pf3RHN%252Fimage.png%3Falt%3Dmedia%26token%3D8899a256-a1d6-486f-aaf6-b8e244f9b348&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=ce097a28&#x26;sv=2" alt="" width="563"></div>

## Zugriff auf die Oberfläche

*   Sobald die Funktion aktiviert ist, öffnen Sie den **DocBits Operator** im Hauptnavigationsmenü.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FS67AFPuaQ3CNXQ7Oe80V%252Fimage.png%3Falt%3Dmedia%26token%3D6b6d6782-cc16-48e6-8622-5c596ac54f57\&width=768\&dpr=4\&quality=100\&sign=e6d0fd8e\&sv=2)

### **1. Eingabe des Prompts**

Am unteren Bildschirmrand befindet sich ein Eingabefeld mit der Bezeichnung _"Geben Sie hier Ihren Prompt ein..."_. Hier schreiben Benutzer Anweisungen, denen der Operator folgen soll.

Neben dem Eingabefeld befinden sich mehrere Steuerungsschaltflächen:

* **Prompt-Variablen** - Öffnet ein Popup, in dem Sie Schlüssel-Wert-Paare eingeben können, die im Prompt verwendet werden. Variablen werden in geschweiften Klammern geschrieben, z. B. `{rechnungs_nummer}` oder `{url}`. Diese Werte gelten nur für den aktuellen Prompt im Eingabefeld.
* **Prompt speichern** - Speichert den aktuellen Prompt. Wählen Sie aus, ob Sie ihn speichern möchten als:
  * **Organisationsprompt** - Innerhalb Ihrer Organisation bearbeitbar; enthält sowohl den Prompt als auch definierte Variablenwerte.
  * **Globaler Prompt** - Über alle Mandanten hinweg gemeinsam genutzt; enthält nur den Prompt und Platzhalter für Variablen (keine Werte werden gespeichert).
* **Chat löschen** - Löscht das aktuelle Gespräch mit dem Operator, lässt den Prompt im Eingabefeld jedoch unverändert. Nützlich beim Wiederverwenden oder Verfeinern eines Prompts.

Für ausführliche Anleitungen zum Schreiben effektiver Prompts - einschließlich Syntax, Variablen und Beispielen - lesen Sie bitte den [**Leitfaden zum Schreiben von Prompts**](prompt-writing-guide.md).

### **2. Seitenleistennavigation**

Verwenden Sie das Symbol oben links, um die Seitenleiste zu öffnen oder zu schließen. Die Seitenleiste zeigt gespeicherte Prompts, die in zwei Kategorien organisiert sind:

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fm08uq4Kqj0SEZWSnlnoS%252Fimage.png%3Falt%3Dmedia%26token%3D4ba4542a-a707-4907-ae5e-b06286af8240&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=ef6b0706&#x26;sv=2" alt="" width="375"></div>

* **Organisationsprompts**: Bearbeitbar und wiederverwendbar innerhalb Ihrer Organisation.
* **Globale Prompts**: Über alle Mandanten hinweg gemeinsam genutzt. Diese können keine Variablen speichern und können nicht bearbeitet oder gelöscht werden.
  *   Ein globaler Prompt ist immer noch bearbeitbar und löschbar durch die **Organisation, die ihn erstellt hat**, wo er unter Organisationsprompts erscheint.

      <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlVnXjwtnxAtqsftRvYUi%252Fimage.png%3Falt%3Dmedia%26token%3D60b3d0dd-3eee-40a8-b447-c9e91087a27d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=f9b364a&#x26;sv=2" alt="" width="375"></div>
* **Suchfunktion**: Eine Suchleiste oben in der Seitenleiste ermöglicht es Benutzern, gespeicherte Prompts schnell nach Namen oder Stichworten zu finden.
* **Symbolreferenz**: Jeder gespeicherte Prompt hat eine Reihe von Aktionsymbolen
  * **Pfeil** - Startet den Prompt
  * **Stift** - Bearbeitet den Prompt (nur für die Prompts Ihrer eigenen Organisation verfügbar)
  * **Mülleimer** - Löscht den Prompt (nur für die Prompts Ihrer eigenen Organisation verfügbar)

### 3. Prompt speichern

Durch Klicken auf die Schaltfläche **Prompt speichern** wird ein Popup geöffnet, in dem Sie den aktuellen Prompt für zukünftige Verwendung speichern können.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FgrBpDnbo80nPkozFhgCE%252Fimage.png%3Falt%3Dmedia%26token%3Dd31c06fc-dcd0-4fbe-9e1e-6c5bc001e4bb&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=900c948&#x26;sv=2" alt="" width="375"></div>

#### **Felder im Popup zum Speichern des Prompts**

* **Prompt-Name:** Geben Sie einen Namen ein, um den Prompt zu identifizieren.
* **Prompt öffentlich speichern (Checkbox):** Wenn aktiviert, wird der Prompt als **Globaler Prompt** gespeichert. Globale Prompts werden über alle Mandanten hinweg geteilt und können keine Variablen **Werte** speichern (nur Variablen **Namen**).
* **Variablen bearbeiten:** Öffnet das [**Popup für Prompt-Variablen**](prompt-writing-guide.md), um Variablendefinitionen vor dem Speichern zu überprüfen oder anzupassen.

**Aktionen**

* **Abbrechen:** Schließt das Popup, ohne zu speichern.
* **Speichern:** Speichert den Prompt unter dem angegebenen Namen und Sichtbarkeitseinstellung.

### 4. Steuerung der Prompt-Ausführung

Wenn ein Prompt läuft, haben Benutzer mehrere Steuerungsoptionen, um den Ausführungsprozess zu verwalten oder einzugreifen:

* **Prompt pausieren:** Stoppt vorübergehend die aktuelle Ausführung. Nützlich, wenn Sie den aktuellen Zustand beobachten oder das System auf die nächsten Schritte vorbereiten möchten. ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzG9U15jmVTb202efDR5l%252Fimage.png%3Falt%3Dmedia%26token%3Dee52f250-15d4-4139-b612-ba5ff1876841\&width=300\&dpr=4\&quality=100\&sign=329efe81\&sv=2)
* **Prompt fortsetzen:** Setzt die Ausführung ab dem Punkt fort, an dem sie pausiert wurde. ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FewGCZ9wSXt7VsvS8RjZH%252Fimage.png%3Falt%3Dmedia%26token%3D92ec27df-07b4-4e9f-a125-6f0a87d9db47\&width=300\&dpr=4\&quality=100\&sign=8e03589c\&sv=2)
* **Prompt abbrechen:** Stoppt die Ausführung vollständig und setzt die Sitzung zurück. Dies ist hilfreich, wenn der Prompt aufgrund falschen Verhaltens oder Änderungen in der Eingabe abgebrochen oder neu gestartet werden muss.\
  ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FYUKk03iazolJlx6reOO3%252Fimage.png%3Falt%3Dmedia%26token%3Da722c82b-e4c1-4c23-8c56-a31f2685cce7\&width=300\&dpr=4\&quality=100\&sign=170c122e\&sv=2)
* **Steuerung übernehmen:** Ermöglicht es dem Benutzer, manuell einzugreifen, indem er direkt mit dem System interagiert. Dies ist nützlich, wenn der Operator stecken bleibt oder einen Schritt falsch interpretiert. Die Übernahme der Kontrolle **pausiert automatisch** den Prompt und wechselt in den manuellen Modus, bis Sie wählen, fortzufahren oder abzubrechen.

### 5. Detailansicht des Operators

Sobald ein Prompt gestartet ist, wird eine zusätzliche Schaltfläche verfügbar, die es Benutzern ermöglicht, zu einer **detaillierten Ausführungsansicht** zu wechseln. ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9kObRWZFb3woomL045KL%252FDetailed%2520view%2520.jpg%3Falt%3Dmedia%26token%3Dbd0f94e2-84f2-4fd0-ae89-82408e85e03a\&width=300\&dpr=4\&quality=100\&sign=3aefc79\&sv=2)

* **Detailansicht öffnen:** Diese Schaltfläche führt Sie zu einer dedizierten Ansicht, die Schritt für Schritt zeigt, was der Operator in Echtzeit tut.

In der Detailansicht können Benutzer:

* Überwachen Sie jede durchgeführte Aktion (z. B. Klicks, Eingaben, Wartezeiten).
* Sehen Sie, welcher Schritt gerade aktiv ist.
* Identifizieren Sie, wo Probleme auftreten, wenn der Prompt auf Probleme stößt.
* Verwenden Sie die gleichen **Pause**, **Fortsetzen**, **Abbrechen** und **Steuerung übernehmen** Aktionen.
