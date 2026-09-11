# Fuzzy Data Konfiguration mit Masterdaten

## **Überblick**

Jeder Dokumententyp hat seine eigenen Standardkonfigurationen und muss separat eingerichtet werden. Während dieses Beispiel die Einrichtung für **Rechnungen** erläutert, gilt derselbe Prozess für alle Dokumententypen.

## Um Fuzzy-Daten zu konfigurieren, navigieren Sie zu:

Einstellungen → Globale Einstellungen → Dokumententypen → Rechnung → Felder → Masterdateneinstellungen → Masterdaten nachschlagen

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fhnn2NcPGzVkUO0mLQWTy%252Fimage.png%3Falt%3Dmedia%26token%3De2f87385-fc48-4149-9bef-ca917a7328bd\&width=768\&dpr=4\&quality=100\&sign=116ee1da\&sv=2)

## **Standardnachschlagen**

Es gibt **vier Standardnachschlagegruppen** für Rechnungen:

1. **Firmendaten**
2. **Kopf der Bestellung**
3. **Lieferant**
4. **Steuercode**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4VxYFu8M62dXi6qGsPl3%252Fimage.png%3Falt%3Dmedia%26token%3Db2bc4690-805b-4b19-aa89-73f315889d88\&width=768\&dpr=4\&quality=100\&sign=835f513a\&sv=2)

Jede Gruppe enthält spezifische Felder. Klicken Sie auf eine Gruppe, um sie zu **erweitern** und die Felder anzuzeigen. Standardnachschlagegruppen sind mit einem **"Standard" Tag** gekennzeichnet.

## **Status der Nachschlagekonfiguration**

* **Aktive Konfigurationen** sind mit einem **"Aktiviert" Tag** markiert.
* **Deaktivierte Konfigurationen** sind mit einem **"Deaktiviert" Tag** markiert.

## **Voraussetzung: Import von Masterdaten**

Damit Fuzzy-Daten korrekt funktionieren, müssen die relevanten **Masterdaten** importiert werden. Ohne dies hat das System keine Referenzdaten zur Verwendung. Hier erfahren Sie, wie Sie Masterdaten importieren:

{% content-ref url="../../../setup/importing-customer-master-data/" %}
[importing-customer-master-data](../../../setup/importing-customer-master-data/)
{% endcontent-ref %}

## **Verwalten von Nachschlagegruppen**

Jede Nachschlagegruppe ist standardmäßig **aktiviert**, kann jedoch durch Klicken auf die drei Punkte geändert werden:

* **Deaktivieren** → Deaktiviert eine Gruppe. _(Nur für aktivierte Gruppen verfügbar)_
* **Aktivieren** → Aktiviert eine Gruppe. _(Nur für deaktivierte Gruppen verfügbar)_
* **Duplizieren** → Erstellt eine Kopie, die modifiziert werden kann, ohne das Original zu beeinflussen.
* **Anzeigen** → Zeigt Informationen wie den **Dokumententyp**, zu dem es gehört, und die **Nachschlagetabelle**, die verwendet wird. _(Nur für Standardgruppen verfügbar)_
* **Bearbeiten** → Verfügbar für **nicht standardmäßige** Gruppen. Ermöglicht das Ändern von Gruppendetails.
* **Löschen** → Entfernt die Gruppe vollständig. _(Nur für nicht standardmäßige Gruppen)_

## **Erstellen einer neuen Nachschlagekonfiguration**

Es gibt **zwei Möglichkeiten**, eine Nachschlagekonfiguration zu erstellen:

1.  **Duplizieren einer vorhandenen Nachschlagegruppe**\


    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZUlPcWGrx1oITQS3tgZP%252Fimage.png%3Falt%3Dmedia%26token%3D59fb300d-836e-40d0-84b7-4a405cf7f321\&width=768\&dpr=4\&quality=100\&sign=3442db8f\&sv=2)

    * Dies kopiert alle Informationen und Felder aus einer vorhandenen Gruppe.
    * Es muss nur ein **neuer Name** angegeben werden.
2.  **Erstellen einer Nachschlagegruppe von Grund auf neu**\


    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FNbEpo2p5Q8D1d7DUchBF%252Fimage.png%3Falt%3Dmedia%26token%3D401314b5-44d0-47df-b3e6-69fea83cce82\&width=768\&dpr=4\&quality=100\&sign=1d0ce322\&sv=2)

    * Klicken Sie auf **"Nachschlagekonfiguration erstellen"**.
    * Füllen Sie die erforderlichen Details aus:
      * **Konfigurationsname**
      * **Nachschlagetabelle** (Zu verwendende Masterdatentabelle)
      * **Konflikthandler** (Wählen Sie einen: Beste Punktzahl, Keine Rückgabe, Erste Rückgabe)
      * **Kontexttyp** (Kopf oder Zeile) benötigt Kontext
      * **Alles finden** (Kontrollkästchenoption) benötigt Kontext

## **Verwalten von Feldern innerhalb einer Nachschlagegruppe**

Jede Gruppe enthält Felder, die je nachdem, ob es sich um Standardfelder oder benutzerdefinierte Felder handelt, **hinzugefügt, entfernt, bearbeitet oder angezeigt** werden können.

### **Standardfelder**

*   Gekennzeichnet mit einem **"Standard" Tag**.\


    <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fh37McVpB0tBo5wqiAttR%252Fimage.png%3Falt%3Dmedia%26token%3Dcabce083-83a5-4881-a64f-88a8757df49b&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=b3739019&#x26;sv=2" alt="" width="375"></div>
* **Kann nur angezeigt**, nicht bearbeitet oder gelöscht werden.

### **Nicht-Standardfelder**

* Können durch Klicken auf die drei Punkte und Auswahl von **Bearbeiten** oder **Entfernen** **bearbeitet oder gelöscht** werden.

### **Hinzufügen eines neuen Feldes**

**Hinweis:** Sie können Felder innerhalb von Standard-Nachschlagekonfigurationen erstellen.

Um ein neues Feld innerhalb einer Gruppe hinzuzufügen:

1.  Klicken Sie innerhalb der relevanten Gruppe auf **"Erstellen"**.\


    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FvmIXTEQQHKKNbvTJj1b4%252Fimage.png%3Falt%3Dmedia%26token%3D8569867b-9f5b-4865-90bd-f2e41e846979\&width=768\&dpr=4\&quality=100\&sign=603cb7df\&sv=2)
2. Geben Sie die folgenden Details an:
   * **Nachschlagefeld** → Spaltenname aus der Masterdaten-Nachschlagetabelle.
   * **Validierungsfeld** → Entsprechendes DocBits-Feld.
   * **Übergeordnetes Feld** → _(Weitere Details erforderlich)_
   * **Suchoperator** → Wählen Sie einen:
     * Smart
     * Enthält
     * Genau
     * Beginnt mit
     * Endet mit
   * **Kontrollkästchen:**
     * **Automatischer Auslöser** → Wenn aktiviert, wird dieses Feld automatisch aktualisiert, wenn ein anderes Feld in einer anderen Nachschlagekonfiguration dieselbe Spalte teilt.
     * **Durchsuchbar** → Aktiviert das Feld als **Fuzzy-Daten**-Feld, das Suchen im Masterdaten-Nachschlagen ermöglicht (blaues Symbol im Validierungsbildschirm).

## **Letzter Schritt: Hinzufügen von Feldern zum Layout**

Nachdem Sie die Fuzzy-Datenfelder konfiguriert haben, **stellen Sie sicher, dass Sie sie mithilfe des Layout-Editors zum Layout hinzufügen**. Wenn Felder nicht zum Layout hinzugefügt werden, stehen sie nicht zur Verfügung.\


{% content-ref url="../../settings/global-settings/document-types/layout-manager/" %}
[layout-manager](../../settings/global-settings/document-types/layout-manager/)
{% endcontent-ref %}

## **Wie DocBits einen Lieferanten auswählt**

Wenn ein Dokument ankommt, sucht DocBits den Lieferanten in Ihren Stammdaten. Drei Einstellungen bestimmen das Ergebnis. Dieser Abschnitt erklärt sie Schritt für Schritt, mit Beispielen.

### **Schritt 1 — Welche Felder für die Suche verwendet werden**

DocBits verwendet ein Feld nur dann für die Suche, wenn beide Punkte zutreffen:

* das Feld ist in der Nachschlagekonfiguration als **Durchsuchbar (Searchable)** oder **Auto Trigger** markiert, und
* das Feld hat auf dem Dokument einen Wert.

Woher der Wert kommt, spielt keine Rolle. Ein trainiertes Feld, ein von der KI gefülltes Feld und ein von Hand eingetippter Wert werden gleich behandelt.

{% hint style="warning" %}
**Durchsuchbar bewirkt zwei Dinge.** Es zeigt das blaue Suchsymbol im Validierungsbildschirm, **und** es nimmt das Feld in die automatische Lieferantensuche auf. Ein Feld, das nur von Hand durchsucht werden soll, bleibt unmarkiert.
{% endhint %}

### **Schritt 2 — Eine Suche, nicht eine Suche pro Feld**

DocBits sucht **nicht** je Feld einzeln. Es baut **eine** Suche über alle verwendeten Felder. **Alle abgleichen (Match All)** bestimmt, wie sie verknüpft werden:

* **Alle abgleichen aus** (Standard) → "finde jeden Lieferanten, der zur Steuernummer **ODER** zum Lieferantennamen passt". Das ergibt eine **längere** Liste.
* **Alle abgleichen ein** → "finde jeden Lieferanten, der zur Steuernummer **UND** zum Lieferantennamen passt". Das ergibt eine **kürzere** Liste.

Beachten Sie außerdem: Die Suchoperatoren **Smart** und **Contains** suchen nach einem Textteil. Der Name "Meier" findet auch "Meier Bau GmbH" und "Meier & Sons Ltd". Ein Lieferantenname findet deshalb oft mehrere Lieferanten.

### **Schritt 3 — Was passiert, wenn die Liste mehrere Lieferanten enthält**

Die **Konfliktverarbeitung (Conflict Handler)** entscheidet:

* **Best Score** → nimmt den Lieferanten, der zu den meisten Feldern passt. Lässt den Lieferanten nie leer.
* **Return None** → lässt den Lieferanten leer, damit ein Benutzer ihn auswählt.
* **Return First** → nimmt den ersten Lieferanten der Liste.

### **Beispiele**

In allen Beispielen hat das Dokument eine Steuernummer und einen Lieferantennamen, und beide Felder sind **Durchsuchbar**.

<table><thead><tr><th width="150">Steuernummer findet</th><th width="150">Name findet</th><th width="150">Alle abgleichen aus + Return None</th><th width="150">Alle abgleichen ein + Return None</th><th width="150">Alle abgleichen aus + Best Score</th></tr></thead><tbody>
<tr><td>nur A</td><td>A und B</td><td>leer</td><td><strong>A</strong></td><td><strong>A</strong></td></tr>
<tr><td>A und B</td><td>nur B</td><td>leer</td><td><strong>B</strong></td><td><strong>B</strong></td></tr>
<tr><td>A, B und C</td><td>C, D und E</td><td>leer</td><td><strong>C</strong></td><td><strong>C</strong></td></tr>
<tr><td>A, B und C</td><td>B, C und D</td><td>leer</td><td>leer</td><td>B oder C, nicht verlässlich</td></tr>
<tr><td>nur A</td><td>nichts</td><td><strong>A</strong></td><td>leer</td><td><strong>A</strong></td></tr>
</tbody></table>

So lesen Sie die Tabelle:

* **Zeile 1 bis 3** sind der Normalfall. Ein Feld ist eindeutig, das andere nicht. Mit **Alle abgleichen aus** enthält die Liste mehrere Lieferanten und **Return None** lässt das Feld leer. **Alle abgleichen ein** behält nur den Lieferanten, der zu beiden Feldern passt, und findet ihn.
* **Zeile 4** hat überhaupt keinen eindeutigen Lieferanten. Das Feld leer zu lassen ist richtig. **Best Score** wählt trotzdem einen aus, und das kann der falsche sein.
* **Zeile 5** ist das Risiko von **Alle abgleichen ein**. Siehe die Warnung unten.

{% hint style="warning" %}
**Alle abgleichen kann einen Lieferanten verlieren.** Mit **Alle abgleichen ein** muss jedes verwendete Feld passen. Trägt ein Feld einen Wert, den es in Ihren Stammdaten nicht gibt — ein Tippfehler, ein alter Firmenname, ein vom Beleg gelesener Wert — liefert die gesamte Suche nichts und es wird kein Lieferant gefunden, obwohl die Steuernummer allein den richtigen gefunden hätte.
{% endhint %}

### **Ein Lieferant wurde früher erkannt und wird jetzt nicht mehr erkannt**

Fast immer liefert ein weiteres Feld jetzt einen Wert. Prüfen Sie in dieser Reihenfolge:

1. Öffnen Sie das Dokument. Welches Feld der Nachschlagegruppe trägt jetzt einen Wert, der früher leer war?
2. Öffnen Sie die Nachschlagekonfiguration. Ist dieses Feld als **Durchsuchbar** oder **Auto Trigger** markiert? Wenn ja, nimmt es jetzt an der Suche teil und macht die Trefferliste länger.
3. Wählen Sie einen der drei Wege:
   * **Das Feld soll nicht an der Suche teilnehmen** → entfernen Sie **Durchsuchbar** und **Auto Trigger** bei diesem Feld. Das Feld behält seinen Wert auf dem Dokument und wird dem Benutzer weiterhin angezeigt. Das ist die kleinste Änderung.
   * **Das Feld soll teilnehmen** → schalten Sie **Alle abgleichen** ein, lesen Sie aber zuerst die Warnung oben.
   * **Sie wollen in jedem Fall einen Lieferanten** → setzen Sie die **Konfliktverarbeitung** auf **Best Score**. Nehmen Sie in Kauf, dass statt eines leeren Feldes auch der falsche Lieferant gewählt werden kann.
