# Cookies und Browserspeicher

Geprüft am **16. Oktober 2026** für Frage **4.15**. Die öffentliche Website, die DocBits-Anwendung und diese Dokumentation verwenden unterschiedliche Cookies und Dienste.

## Richtlinie und Verwendungszwecke

Die [DocBits-Datenschutzerklärung](https://docbits.com/en/privacy-policy/) enthält die Abschnitte **Cookies** und **Consent with Borlabs Cookie**. Sie beschreibt das Speichern von Einwilligungen, notwendige Funktionen, Bot-Schutz, Google Analytics, Werbung und Leadfeeder. Analysen können Berichte über Besuche, Seiten, Interaktionen und Leistung liefern; die Erfassung beschränkt sich jedoch nicht auf anonyme, zusammengefasste Daten. Aus der Website-Richtlinie ergibt sich nicht automatisch die Cookie-Liste der Anwendung.

## Cookie-Liste

**Beobachtet** bedeutet einen frischen Besuch ohne Anmeldung oder Auswahl optionaler Einwilligungen. **Quellcode** bezeichnet geprüften Anwendungscode oder Infrastruktureinstellungen; dies bestätigt nicht die Attribute jeder produktiven Antwort.

| Cookie / Bereich | Zweck und Speicherdauer | Nachweis und Sicherheitsattribute |
| --- | --- | --- |
| `__cf_bm` / Website und App | Cloudflare-Bot-Schutz; 30 Minuten Inaktivität | Beobachtet: `Secure`, `HttpOnly`, `SameSite=None`. [Cloudflare](https://developers.cloudflare.com/fundamentals/reference/policies-compliances/cloudflare-cookies/) verschlüsselt die Bot-Informationen mit Ausnahme der Zeitangaben. |
| `pll_language` / Website | Spracheinstellung; etwa ein Jahr | Beobachtet: `Secure`, per JavaScript lesbar, `SameSite=Lax`. |
| `_lfa` / Website | Leadfeeder-Analyse von Besuchern und Unternehmen; etwa ein Jahr | Beobachtet: per JavaScript lesbar, `SameSite=Lax`, **ohne `Secure`-Attribut** bei diesem Besuch. |
| Borlabs-Einwilligungscookie / Website | Speichert Einwilligungen und Widerrufe | In der Datenschutzerklärung genannt; Name, produktive Attribute und Laufzeit wurden bei diesem Besuch nicht geprüft. |
| `session` / Authentifizierungsdienst | Sitzungszustand für Authentifizierungsabläufe | Quellcode-Standard: `Secure`, `HttpOnly`, `SameSite=None`; signierte Flask-Sitzungsdaten, nicht verschlüsselt. Die Bereitstellung kann Standardwerte überschreiben. |
| `dbx_td` / Authentifizierungsdienst | Merkt nach erfolgreicher MFA auf Wunsch ein vertrauenswürdiges Gerät; 30 Tage | Quellcode: `Secure`, `HttpOnly`, `SameSite=None`; Zufallstoken, dessen Hash serverseitig gespeichert wird. |
| `prod-sticky` / produktive Lastverteilung | Leitet Anfragen an dasselbe Backend; konfigurierte Laufzeit 300 Sekunden | Infrastruktureinstellung bestätigt; Browserattribute nicht geprüft. |
| `dontAsk` / App | Merkt eine Einstellung zu einer Rückfrage; im geprüften Aufruf keine explizite Ablaufzeit | Quellcode: per JavaScript lesbar; beim Setzen keine explizite Option für `Secure` oder `SameSite`. |

Bei einem frischen Besuch der Dokumentation wurden keine Cookies beobachtet. Dies ist eine datierte Momentaufnahme, keine vollständige Liste für angemeldete Abläufe, optionale Funktionen oder externe Einbettungen. Die Richtlinie nennt weitere Analyse- und Werbedienste, deren Cookies dieser Besuch nicht bestätigt hat. Für eine vollständige Liste und die Prüfung der Einwilligungssteuerung müssen diese Abläufe gesondert untersucht werden.

## Sicherheit und Analysen

`Secure` beschränkt die Übertragung auf HTTPS. `HttpOnly` verhindert das Lesen durch JavaScript. `SameSite` steuert das Senden bei websiteübergreifenden Anfragen. Diese Attribute verschlüsseln den Cookie-Inhalt nicht. Die pauschale Aussage, alle Cookies seien verschlüsselt oder gleich abgesichert, wäre unzutreffend. Öffentliche Anwendungsendpunkte unterstützen TLS 1.2 und 1.3; siehe [Sichere Speicherung von Zugangsdaten](secure-storage-of-credentials.md).

Browserspeicher wird auch unabhängig von Cookies genutzt. Die Grafana-Faro-Konfiguration der Anwendung unterstützt dauerhafte Sitzungsverfolgung, Fehler, Leistungsmessungen und Traces sowie verfügbare Benutzer- und Organisationskennungen. Die Erfassung hängt von der bereitgestellten Collector-Konfiguration ab. Sie darf nicht als ausschließlich anonyme, zusammengefasste Cookie-Analyse beschrieben werden. Auch Spracheinstellungen nutzen lokalen Speicher.

Cookies und Browserspeicher lassen sich im Browser löschen. Dadurch können Einstellungen und die Erinnerung an vertrauenswürdige Geräte verloren gehen. Für eine aktuelle Liste oder Datenschutzfragen: **compliance@fellowpro.com**.
