# M3

## API Connection Template in Infor M3 importieren

Diese Anleitung erklärt, wie Sie ein API Connection Template importieren, um wichtige Einstellungen für die Integration mit Infor M3 schnell zu konfigurieren. Die Verwendung eines Templates ermöglicht eine vordefinierte Connection-Einrichtung, vereinfacht den Prozess und sorgt für Konsistenz.

<mark style="color:red;">**Hinweis**</mark>: Für die detaillierte Konfiguration spezieller Bereiche wie Auto Accounting, Supplier Integration, Purchase Orders oder Table Extraction for costing elements verweisen wir auf die entsprechende Dokumentation:

* [Auto Accounting](auto-accounting.md)
* [Lieferanten und Bestellungen](suppliers-and-purchase-orders.md)
* [So importieren Sie alle Lieferanten](../../../infor-integration-and-configuration/importing-customer-master-data/m3/how-to-import-all-suppliers.md)
* [Tabellenextraktion für Kostenelement](../../../admin-section/setup/importing-customer-master-data/m3/table-extraction-for-costing-element.md)

### **Template herunterladen**

Laden Sie vor dem Import das benötigte Connection Template über die folgende Datei herunter:

### Template importieren

#### Schritte zum Import eines Connection Template

1. **Infor ION Desk öffnen:**
   *   Navigieren Sie zu **InforOS** → **ION Desk** → **Connect** → **Connection Points**.

       ![](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o)
2. **Template importieren:**
   *   Klicken Sie auf die Schaltfläche **Import**.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_2.png)
   * Wählen Sie die passende **Template File** aus Ihrem lokalen System aus.
   *   Klicken Sie auf **OK**, um den Importvorgang zu starten.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_3.png)
3. **Bestätigung:**
   *   Wenn der Import erfolgreich war, wird eine Bestätigungsmeldung angezeigt.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_4.png)
4. **Konfiguration nach dem Import:**
   * Nach dem Import des Templates können Sie bei Bedarf spezifische Verbindungseinstellungen anpassen.
   * Vergessen Sie nicht, Ihren **Service Account** für Authentifizierung und Zugriffskontrolle zu importieren bzw. zu konfigurieren.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/m3_import_5.png)
