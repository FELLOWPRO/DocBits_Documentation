# Weitere Sicherheitsmaßnahmen

Geprüft am **16. Oktober 2026**. Diese Seite unterscheidet veröffentlichte Auditnachweise von einer aktuellen Bestandsaufnahme der Infrastruktur.

| Maßnahme | Dokumentierter Umfang |
| --- | --- |
| Netzwerk-Firewalls | Der SOC-2-Bericht beschreibt DigitalOcean-VPC-/Security-Group-Filter und die Kontrolle von Konfigurationsänderungen durch die IT-Sicherheit. Aktuelle, rein lesende Prüfungen bestätigen aktive Cloud-Firewalls, darunter Regeln für Kubernetes-Ressourcen. |
| Web Application Firewall (WAF) | Das DSGVO-Audit dokumentiert eine WAF zum Schutz des Produkts. Aktuelle verwaltete Regeln, Ausnahmen und die Abdeckung jedes Hostnamens wurden nicht unabhängig geprüft. Cloudflare-Bot-Schutz-Cookies wurden auf Website und App beobachtet; dies allein belegt nicht das WAF-Regelwerk. |
| Lastverteiler | Die aktuelle DigitalOcean-Bestandsaufnahme bestätigt aktive produktive Lastverteiler in Frankfurt mit eingerichteten Zustandsprüfungen. Anfragerouting und Sitzungsbindung sind Infrastrukturaufgaben. Siehe [Cookies und Browserspeicher](cookies-and-browser-storage.md). |
| IP-Freigabelisten | Infrastruktur-Firewallregeln unterstützen die Filterung nach Quelle. Eine kundenseitig einstellbare IP-Freigabeliste pro Mandant, ihr Umfang und Ausnahmen wurden nicht bestätigt. Vereinbaren Sie die gewünschte Einschränkung für Ihre Bereitstellung mit FELLOWPRO. |
| Lokale Tests und Sandbox | Die [Release-Lebenszyklus-Strategie](../overview-and-basics/docbits-release-lifecycle-strategy.md) beschreibt Entwicklung, QA/UAT und Sandbox-Prüfungen vor der Produktivverfügbarkeit. Lokale Integrationstests brauchen eine festgelegte Umgebung und geeignete Testdaten. Sandbox-Zugang allein erlaubt keine Penetrationstests. |
| Virtuelle Maschinen und Kubernetes | Der SOC-Bericht beschreibt Härtungsvorgaben, Zugriffskontrollen, eingeschränkte Ports sowie Betriebssystem- und Netzwerkpatches. Die aktuelle Bestandsaufnahme bestätigt verwaltete Kubernetes-Cluster. Dies garantiert keine identischen Härtungseinstellungen für jeden Workload. |
| Endgeräte und Mobilgeräte | Der SOC-Bericht beschreibt Schutz vor Schadsoftware, automatische Scans, Signaturupdates und Patchüberwachung auf Endgeräten. Der ISO-Überwachungsbericht nennt MDM als Verbesserungsmöglichkeit. Flächendeckendes MDM, Fernlöschung sowie Mobilgeräte-/BYOD-Regeln müssen daher aktuell bestätigt werden. Kunden verantworten die Sicherheit ihrer eigenen Browsergeräte. |
| Richtlinien und Verfahren | Der SOC-Bericht beschreibt formale Informationssicherheitsrichtlinien, Risikobewertung, Zugriffskontrollen, Änderungsmanagement, Vorfallbearbeitung und Mitarbeiterschulungen. Aktuelle Richtlinien und deren Geltungsbereich erhalten Sie beim Compliance-Kontakt. |

## Nachweise und weitere Informationen

Auditberichte und Prüfzeiträume finden Sie unter [Zertifizierungen](../overview-and-basics/architecture/certifications.md). Historische Audits belegen die beschriebenen Maßnahmen für ihren geprüften Umfang; die Infrastrukturprüfung bestätigt vorhandene Ressourcen am Prüftag und ist kein vollständiges Konfigurationsaudit.

Zur Verschlüsselung und Anmeldung siehe [Sichere Speicherung von Zugangsdaten](secure-storage-of-credentials.md) und [Verschlüsselung gespeicherter Daten](encryption-at-rest.md). Prüfungen, Updates und offene CVEs behandelt [Schwachstellenmanagement](vulnerability-management.md).

Für Einschränkungen Ihrer Bereitstellung, Mobilgeräteanforderungen oder aktuelle Richtliniennachweise: **compliance@fellowpro.com**.
