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

#### Standard-Aktivierung und Modifikation

Der ZUGFeRD-Standard ist standardmäßig immer aktiv, Sie können jedoch bei Bedarf Änderungen daran vornehmen.

### **Schritte zur Änderung der ZUGFeRD-Einstellungen:**

1. Navigieren Sie zu **Einstellungen → Globale Einstellungen → Dokumententypen → Rechnung**.
2. Klicken Sie auf **E-Doc**.
3. Eine Liste aller verfügbaren E-Docs wird angezeigt.
4. Suchen Sie die **ZUGFeRD**-Version, die Sie ändern möchten.

## **Konfiguration von Transformation und XML-Pfad:**

In den **Transformations-Einstellungen** können Sie den Pfad definieren, um bestimmte Informationen innerhalb der XML-Datei zu finden und in einer neuen Struktur zu speichern, was den Zugriff auf die Daten erleichtert. <mark style="color:red;">**Hinweis**</mark>: Wenn Sie diese Funktionalität nutzen, müssen Sie die neu erstellten XML-Pfade verwenden, nicht die ursprünglichen XML-Pfade, in der **Vorschau** und dem **Extraktionspfad**.

### **Schritte zur Änderung der Transformationsdatei:**

1. Öffnen Sie die **Transformation**.
2. Erstellen Sie einen neuen Entwurf, indem Sie auf das **Stiftsymbol** klicken.
3. Wählen Sie den neu erstellten Entwurf aus.
4. Erstellen Sie entweder ein neues Feld oder ändern Sie ein bestehendes.
5. Legen Sie den gewünschten Pfad für die Datenextraktion fest.
6. Klicken Sie auf **Speichern**.

### Wichtige Hinweise:

* Die **Vorschaudatei** wird nur für **FACTUR-X** verwendet und nicht für **ZUGFeRD**. ZUGFeRD verwendet das Original-**PDF**.

## Vorschau PDF Konfiguration

Die **Vorschau PDF Konfiguration** wird verwendet, um eine benutzerlesbare Version des Dokuments zu erstellen. Sie können sie mit HTML an Ihre Bedürfnisse anpassen.

### **Schritte zur Änderung der Vorschaudatei:**

1. Öffnen Sie die **Vorschau**.
2. Erstellen Sie einen neuen Entwurf, indem Sie auf das **Stiftsymbol** klicken.
3. Wählen Sie den neu erstellten Entwurf aus.
4. Erstellen Sie entweder ein neues Feld oder ändern Sie ein bestehendes.
5. Legen Sie den gewünschten Pfad für die Datenextraktion fest.
6. Klicken Sie auf **Speichern**.

## Extraktionspfade Konfiguration

Die **Extraktionspfade Konfiguration** wird verwendet, um Daten zu extrahieren und Felder in der **Validierungsmaske** zu füllen, wie z.B. die Rechnungstabelle oder die im Rechnungslayout konfigurierten Felder.

### **Schritte zur Änderung der** **Extraktionspfade**:

1. Öffnen Sie die **Extraktionspfade**.
2. Erstellen Sie einen neuen Entwurf, indem Sie auf das **Stiftsymbol** klicken.
3. Wählen Sie den neu erstellten Entwurf aus.
4. Erstellen Sie ein neues Feld oder ändern Sie ein bestehendes.
5. Die linke Seite stellt die **DocBits-Feld-ID** dar, die unter **Einstellungen → Globale Einstellungen → Dokumententypen → Rechnung → Felder** zu finden ist.
6. Die rechte Seite stellt den in der Transformation erstellten **Pfad zum Feld** dar.
7. Klicken Sie auf **Speichern**.

Durch Befolgen dieser Schritte können Sie eine genaue Datenextraktion und Validierung für ZUGFeRD-Rechnungen sicherstellen.
