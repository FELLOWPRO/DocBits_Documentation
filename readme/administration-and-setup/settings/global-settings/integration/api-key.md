# API-Schlüssel

<figure><img src="../../../../.gitbook/assets/s150-api-key-list-row-de.png" alt="API-Schlüsselliste mit ausgeblendeten Schlüsseln und Kontodaten. Die Spaltenbezeichnung Actions ist in der Produktoberfläche noch englisch."><figcaption><p>API-Schlüsselliste mit ausgeblendeten Schlüsseln und Kontodaten. Die Spaltenbezeichnung Actions ist in der Produktoberfläche noch englisch.</p></figcaption></figure>

### API-Schlüssel

* **Schlüssel:** Dies ist die eindeutige Kennung, die von externen Anwendungen verwendet wird, um auf die API von DocBits zuzugreifen. Sie ist entscheidend für die Authentifizierung von Anfragen, die von anderer Software an DocBits gestellt werden.
* Aktionen wie Anzeigen, Neugenerieren oder Kopieren des API-Schlüssels können hier durchgeführt werden, abhängig von den spezifischen Bedürfnissen und Sicherheitsprotokollen.

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
* **Datei hochladen:** Ermöglicht es dem Administrator, Konfigurationsdateien oder andere notwendige Dateien hochzuladen, die die Integration mit einem Identitätsanbieter erleichtern.
* **Konfigurieren:** Eine Schaltfläche, um die Einstellungen nach dem Vornehmen von Änderungen oder dem Hochladen neuer Konfigurationen anzuwenden oder zu aktualisieren.