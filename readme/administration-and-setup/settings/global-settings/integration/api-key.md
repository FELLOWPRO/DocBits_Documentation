# API-Schlüssel

<figure><img src="../../../../.gitbook/assets/s150-api-key-list-row-de.png" alt="API-Schlüsselliste mit ausgeblendeten Schlüsseln und Kontodaten. Die Spaltenbezeichnung Actions ist in der Produktoberfläche noch englisch."><figcaption><p>API-Schlüsselliste mit ausgeblendeten Schlüsseln und Kontodaten. Die Spaltenbezeichnung Actions ist in der Produktoberfläche noch englisch.</p></figcaption></figure>

### API-Schlüsselliste

Ein API-Schlüssel erlaubt anderen Systemen den Zugriff auf DocBits ohne Benutzeranmeldung. Die Abbildung oben verbirgt Schlüssel und Kontodaten.

* **Schlüssel:** Die Liste zeigt nur das Präfix, gefolgt von `****`. Das Kopiersymbol kopiert dieses Präfix, nicht den vollständigen Schlüssel. Der vollständige Schlüssel wird nur einmal direkt nach seiner Erstellung angezeigt.
* **Name / Läuft Ab / Zuletzt Verwendet / Status:** Die Spalten zeigen Namen, Ablaufdatum, letzte Verwendung und Zustand des Schlüssels.
* **API-Schlüssel erstellen:** Öffnet den Dialog für einen neuen Schlüssel. Erst die Bestätigung im Dialog erstellt ihn. Die Anleitung [API-Schlüsselverwaltung](api-key-management.md) erklärt die Felder und die einmalige Anzeige des vollständigen Schlüssels.
* **Actions (Dreipunktmenü):** Für aktive Schlüssel bietet das Menü Bearbeiten von Name und Beschreibung sowie Widerrufen an. Für inaktive beziehungsweise widerrufene Schlüssel bietet es Löschen an. Die jeweilige Änderung wird im folgenden Dialog bestätigt.

### Einstellungen für SSO (Single Sign-On) Dienstanbieter

* **Entitäts-ID:** Dies ist die Kennung für DocBits als Dienstanbieter in der SSO-Konfiguration. Sie identifiziert DocBits eindeutig innerhalb des SSO-Frameworks.
* **SLO (Single Logout) URL:** Die URL, an die SSO-Sitzungen gesendet werden, um sich gleichzeitig von allen über SSO verbundenen Anwendungen abzumelden.
* **SSO URL:** Die URL, die zum Initiieren des Single Sign-On-Prozesses verwendet wird.
* Aktionen wie "Zertifikat herunterladen" und "Metadaten herunterladen" sind verfügbar, um notwendige Sicherheitszertifikate und Metadateninformationen zu erhalten, die beim Einrichten und Warten der SSO-Integration verwendet werden.

{% hint style="info" %}
Siehe SSO einrichten
{% endhint %}

### Einstellungen für Identitätsdienstanbieter

* **Tenant-ID:** Dies kann verwendet werden, wenn DocBits in Cloud-Dienste integriert wird, die eine Tenant-Kennung erfordern, um Daten und Zugriffskonfigurationen zu verwalten, die spezifisch für das Unternehmen sind, das DocBits verwendet.
* **Datei hochladen:** Wählen Sie die XML-Metadatendatei Ihres Identitätsanbieters aus.
* **Konfigurieren:** Wählen Sie zuerst die XML-Datei aus und klicken Sie anschließend auf Konfigurieren, um sie hochzuladen und die Konfiguration des Identitätsanbieters zu speichern.