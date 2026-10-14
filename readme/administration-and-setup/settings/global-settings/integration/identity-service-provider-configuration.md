# Identity Service Provider Configuration

Die Konfiguration des Identity Service Providers (IdP) für die Integration mit DocBits erfordert einige spezifische Schritte. Hier finden Sie eine Anleitung dazu:

<figure><img src="../../../../.gitbook/assets/image (83).png" alt=""><figcaption></figcaption></figure>

**Zugriff auf die IdP-Konfigurationsoberfläche**

* Melden Sie sich als Administrator bei Ihrem Identity Service Provider (IdP) an.
* Navigieren Sie zur Einstellungs- oder Konfigurationsoberfläche für die Verwaltung von SAML-Integrationen.

**Die Tenant-ID eingeben:**

* Suchen Sie den Bereich, in dem neue SAML-Integrationen konfiguriert werden können.
* Geben Sie die DocBits-Tenant-ID ein. Diese ID identifiziert Ihr Docbits-Konto gegenüber dem IdP und ermöglicht die sichere Kommunikation zwischen den beiden Systemen.

**Die erforderlichen Dateien importieren:**

* DocBits verlangt in der Regel, Metadaten herunterzuladen oder bestimmte Konfigurationsdetails hinzuzufügen. Prüfen Sie in der Dokumentation Ihres IdP, welche Schritte erforderlich sind.
* Laden Sie die DocBits-Metadatendatei herunter oder importieren Sie sie in das Konfigurationsmenü Ihres IdP. Alternativ können Sie die erforderlichen Konfigurationsdetails je nach Unterstützung Ihres IdP manuell eingeben.

**Integrationseinstellungen konfigurieren:**

* Stellen Sie sicher, dass die Integrationseinstellungen wie SSO-URL, Entity ID und SAML-Zertifikat korrekt sind.
* Prüfen Sie, ob die Single-Log-Out-URL (SLO) und andere erforderliche Parameter korrekt konfiguriert sind. Sie sind entscheidend für eine reibungslose Authentifizierung und Abmeldung über SAML.

**Konfiguration verifizieren:**

* Nehmen Sie sich Zeit, um sicherzustellen, dass alle eingegebenen Informationen korrekt sind und keine Tippfehler oder Fehlkonfigurationen vorliegen.
* Führen Sie Tests durch, um sicherzustellen, dass sich Benutzer erfolgreich über SAML bei Docbits anmelden können und das Single Log-Out ordnungsgemäß funktioniert.

**Sicherheitsaspekte:**

* Stellen Sie sicher, dass alle übertragenen Dateien und Konfigurationsdetails sicher behandelt werden, um Datenlecks oder unbefugten Zugriff zu vermeiden.
* Schützen Sie sensible Informationen wie SAML-Zertifikate und Zugangsdaten vor unbefugtem Zugriff und bewahren Sie sie an einem sicheren Ort auf.
