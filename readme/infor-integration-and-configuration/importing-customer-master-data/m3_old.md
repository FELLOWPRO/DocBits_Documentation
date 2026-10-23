---
hidden: true
noIndex: true
---

# M3\_OLD

## API-Connection-Template in Infor M3 importieren

Diese Anleitung erklärt, wie Sie ein API-Connection-Template importieren, um wichtige Einstellungen für die Integration mit Infor M3 schnell zu konfigurieren. Mit einem Template können Sie eine vordefinierte Verbindungseinrichtung herstellen, die den Vorgang vereinfacht und für Konsistenz sorgt.

<mark style="color:red;">**Hinweis**</mark>: Detaillierte Informationen zur Konfiguration einzelner Bereiche wie Auto Accounting, Lieferantenintegration, Bestellungen oder Tabellenextraktion für Kostenelemente finden Sie in der jeweiligen Dokumentation:

* [Automatische Kontierung](m3/auto-accounting.md)
* [Lieferanten und Bestellung](m3/suppliers-and-purchase-orders.md)
* [So importieren Sie alle Lieferanten](m3/how-to-import-all-suppliers.md)
* [Tabellenextraktion für Kostenelemente](m3/table-extraction-for-costing-element.md)

### **Template herunterladen**

Laden Sie vor dem Import das erforderliche Connection-Template über die folgende Datei herunter:

{% file src="../../.gitbook/assets/DocBits-Dev-Import-Template (1).xml" %}

### Template importieren

#### Schritte zum Importieren eines Connection-Templates

1. **Auf Infor ION Desk zugreifen:**
   *   Navigieren Sie zu **InforOS** → **ION Desk** → **Connect** → **Connection Points**.

       ![Navigationsmenü des Infor ION Desk mit den Einträgen Home, Data Flows, API Flows und Mappings](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o)
2. **Template importieren:**
   *   Klicken Sie auf die Schaltfläche **Import**.

       <figure><img src="../../.gitbook/assets/m3_import_2.png" alt="Seite Connect in Infor ION Desk mit der Ansicht Connection Points samt Suche und Symbolleiste"><figcaption></figcaption></figure>
   * Wählen Sie die passende **Template File** von Ihrem lokalen System aus.
   *   Klicken Sie auf **OK**, um den Importvorgang zu starten.

       <figure><img src="../../.gitbook/assets/m3_import_3.png" alt="Dialogfeld Upload Local File in Infor ION Desk mit der für den Upload ausgewählten Datei DocBits-Dev-Prod-Import-Template" width="327"><figcaption></figcaption></figure>
3. **Bestätigung:**
   *   Wenn der Import erfolgreich war, wird eine Bestätigungsmeldung angezeigt.

       <figure><img src="../../.gitbook/assets/m3_import_4.png" alt="Importbestätigung in Infor ION Desk mit der Meldung, dass der Import von DocBits-Dev-Prod-Import-Template erfolgreich war"><figcaption></figcaption></figure>
4. **Konfiguration nach dem Import:**
   * Nach dem Import des Templates können Sie bestimmte Verbindungseinstellungen nach Bedarf anpassen.
   * Vergessen Sie nicht, Ihren **Service Account** für Authentifizierung und Zugriffskontrolle zu importieren oder zu konfigurieren.

<figure><img src="../../.gitbook/assets/m3_import_5.png" alt="Seite API Connection Point für DocBits-Dev-Prod-Import-Template mit Name, logischer ID und Authentifizierungsdetails"><figcaption></figcaption></figure>
