# ZUGFeRD Konfiguration

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits E-Invoice Tutorial: Process XRechnung / ZUGFeRD (Factur-X), Validate Data & Automate Workflows
{% endembed %}

## **Unterstützte ZUGFeRD-Versionen**

DocBits unterstützt alle wichtigen Versionen von ZUGFeRD, einschließlich:

* **1.0**
* **2.0**
* **2.1** (entspricht FACTUR-X 1.0.05)
* **2.2**
* **2.3** (entspricht FACTUR-X 1.07.2)
* **2.3.2**

#### Standard-Aktivierung und Änderung

Der ZUGFeRD-Standard ist standardmäßig immer aktiv, Sie können ihn jedoch bei Bedarf anpassen.

### **Schritte zur Änderung der ZUGFeRD-Einstellungen:**

1. Navigieren Sie zu **Einstellungen → Globale Einstellungen → Dokumententypen → Rechnung**.
2. Klicken Sie auf **E-Doc**.\\
3. Eine Liste aller verfügbaren E-Docs wird angezeigt.
4. Suchen Sie die **ZUGFeRD**-Version, die Sie ändern möchten.\\

## **Konfiguration von Transformation und XML-Pfad:**

In den **Transformations-Einstellungen** können Sie den Pfad definieren, um bestimmte Informationen innerhalb der XML-Datei zu finden und in einer neuen Struktur zu speichern, was den Zugriff auf die Daten erleichtert.\
<mark style="color:red;">**Hinweis**</mark>: Wenn Sie diese Funktionalität nutzen, müssen Sie in der **Vorschau** und im **Extraktionspfad** die neu erstellten XML-Pfade verwenden, nicht die ursprünglichen XML-Pfade.

### **Schritte zur Änderung der Transformationsdatei:**

1. Öffnen Sie die **Transformation**.
2. Erstellen Sie einen neuen Entwurf, indem Sie auf das **Stiftsymbol** klicken.
3. Wählen Sie den neu erstellten Entwurf aus.
4. Erstellen Sie entweder ein neues Feld oder ändern Sie ein bestehendes.
5. Legen Sie den gewünschten Pfad für die Datenextraktion fest.
6. Klicken Sie auf **Speichern**.

### Wichtige Hinweise:

* Die **Vorschaudatei** wird nur für **FACTUR-X** verwendet und nicht für **ZUGFeRD**. ZUGFeRD verwendet das Original-**PDF**.

## Vorschau-PDF-Konfiguration

Die **Vorschau-PDF-Konfiguration** wird verwendet, um eine für Benutzer lesbare Version des Dokuments zu erzeugen. Sie können sie mit HTML an Ihre Bedürfnisse anpassen.

### **Schritte zur Änderung der Vorschaudatei:**

1. Öffnen Sie die **Vorschau**.
2. Erstellen Sie einen neuen Entwurf, indem Sie auf das **Stiftsymbol** klicken.
3. Wählen Sie den neu erstellten Entwurf aus.
4. Erstellen Sie entweder ein neues Feld oder ändern Sie ein bestehendes.
5. Legen Sie den gewünschten Pfad für die Datenextraktion fest.
6. Klicken Sie auf **Speichern**.

## Konfiguration der Extraktionspfade

Die **Konfiguration der Extraktionspfade** wird verwendet, um Daten zu extrahieren und Felder in der **Validierungsmaske** zu füllen, wie z. B. die Rechnungstabelle oder die im Rechnungslayout konfigurierten Felder.

### **Schritte zur Änderung der** **Extraktionspfade**:

1. Öffnen Sie die **Extraktionspfade**.
2. Erstellen Sie einen neuen Entwurf, indem Sie auf das **Stiftsymbol** klicken.
3. Wählen Sie den neu erstellten Entwurf aus.
4. Erstellen Sie ein neues Feld oder ändern Sie ein bestehendes.
5. Die linke Seite steht für die **DocBits-Feld-ID**, die Sie unter **Einstellungen → Globale Einstellungen → Dokumententypen → Rechnung → Felder** finden.\\
6. Die rechte Seite steht für den **Pfad zum Feld**, das in der Transformation erstellt wurde.
7. Klicken Sie auf **Speichern**.

Wenn Sie diese Schritte befolgen, stellen Sie eine genaue Datenextraktion und Validierung für ZUGFeRD-Rechnungen sicher.

## Verwendete Regeln und Aktivierung

Organisationsspezifische Regeln haben Vorrang vor den Standardregeln für das erkannte eDoc-Format. Prüfen Sie die aktive TRANSFORMATION und prüfen Sie, welcher Knoten im transformierten XML invoice_type liefert; der Pfad hängt vom Format ab. Speichern sichert einen Entwurf; aktivieren Sie ihn nach dem Testen über das Häkchen. Eine gerenderte Preview belegt nicht den gespeicherten Dokumenttyp. Die [Anleitung zur Fehlerbehebung bei der Klassifizierung](../credit-note-recognized-as-invoice.md) erläutert die Codes 381/261, spätere Skripte und Vorsichtsmaßnahmen bei der erneuten Verarbeitung.
