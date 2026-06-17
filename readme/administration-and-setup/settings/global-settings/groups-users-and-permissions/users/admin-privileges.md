# Admin-Privilegien

Die Rolle eines Administrators ist entscheidend für die Verwaltung von IT-Systemen, Netzwerken und digitalen Plattformen in einer Organisation. Ein Administrator verfügt über erweiterte Berechtigungen und Verantwortlichkeiten, mit denen er verschiedene Bereiche der technischen Infrastruktur steuern und sicherstellen kann, dass diese effizient und sicher betrieben wird. Hier sind einige der wichtigsten Aufgaben eines Administrators:

* **Benutzerverwaltung:** Administratoren verwalten Benutzerkonten, Zugriffsrechte und Berechtigungen. Sie erstellen neue Benutzerkonten, weisen ihnen die erforderlichen Berechtigungen zu und steuern die Zugriffskontrolle, damit nur autorisierte Benutzer auf bestimmte Ressourcen zugreifen können.
* **Sicherheit:** Administratoren sind für die Sicherheit der IT-Systeme verantwortlich, um vor Datenverlust und unbefugtem Zugriff zu schützen.
* **Fehlerbehebung und Support:** Der Administrator ist oft die erste Anlaufstelle bei technischen Problemen. Er unterstützt Benutzer bei der Fehlersuche und -behebung und sorgt dafür, dass das System reibungslos läuft.

Neben diesen Aufgaben sind Administratoren auch dafür zuständig, sensible Einstellungen zu verwalten und sicherzustellen, dass die Systeme den Compliance-Anforderungen und den bewährten Verfahren der Informationssicherheit entsprechen. Dazu gehören die Verwaltung sensibler Daten, die Konfiguration von Zugriffskontrollen und Berechtigungen sowie die Überwachung und Analyse von Systemprotokollen, um potenzielle Sicherheitsrisiken zu erkennen und zu beheben.

## Admin vs System Admin

DocBits kennt zwei Administratorrollen: **Admin** und **System Admin**. Sie klingen ähnlich, erfüllen aber unterschiedliche Aufgaben. Hier die einfache Erklärung.

### Admin – eine Person, die Ihre Organisation verwaltet

Ein **Admin** ist eine reale Person in Ihrem Team, die DocBits verwalten darf. Admins können:

* Alle Bereiche der **Einstellungen** öffnen und ändern, wie Ihre Organisation arbeitet.
* Neue Benutzer hinzufügen, bearbeiten, aktivieren oder deaktivieren und festlegen, wer ebenfalls Admin wird.
* Gruppen, Berechtigungen, Integrationen und Workflows einrichten.

Sie können **so viele Admins haben, wie Sie benötigen**, und die Admin-Rolle jederzeit jedem Benutzer zuweisen oder entziehen. Die meisten Administratoren in Ihrem Team sind von diesem Typ.

### System Admin – das Konto, mit dem DocBits selbstständig arbeitet

Ein **System Admin** ist **ein besonderes Konto pro Organisation**, das DocBits für Aktionen nutzt, die **automatisch und ohne Zutun einer Person ablaufen** – zum Beispiel, wenn Dokumente per E-Mail importiert, in ein anderes System exportiert oder im Hintergrund von einem verbundenen Dienst weitergereicht werden.

Stellen Sie es sich als das „Roboter“-Konto der Organisation vor. Wenn das System etwas von sich aus tut, geschieht dies **als System Admin**, damit automatische Aktivitäten leicht zu erkennen sind und nicht mit der Arbeit Ihrer realen Teammitglieder vermischt werden.

Ein System Admin ist in dreierlei Hinsicht besonders:

* **Er ist immer zugleich ein Admin.** Mit der Auswahl von System Admin erhält dieses Konto automatisch auch vollständige Admin-Rechte.
* **Es gibt nur einen pro Organisation.** Sobald ein System Admin existiert, können Sie keinen weiteren Benutzer als System Admin kennzeichnen.
* **Er wird nur beim Anlegen des Benutzers festgelegt.** Sie entscheiden dies im Moment des Anlegens. Er **kann später weder ein- noch ausgeschaltet werden**.

> **Empfehlung:** Legen Sie für diesen Zweck ein eigenes Konto an – zum Beispiel `system@your-company.com` – und kennzeichnen Sie es als System Admin. So erscheint alles, was DocBits automatisch erledigt, in Ihren Protokollen und im Dokumentenverlauf eindeutig als **System Admin**, getrennt von Ihren realen Benutzern.

### Auf einen Blick

| | Admin | System Admin |
|---|---|---|
| Voller Zugriff zur Verwaltung der Organisation | Ja | Ja |
| Wie viele möglich sind | So viele wie nötig | Nur einer |
| Nach dem Anlegen des Benutzers änderbar | Ja, jederzeit | Nein, nur beim Anlegen festgelegt |
| Für automatische Aktionen im Hintergrund genutzt | Nein | Ja |
| Verfügt immer über Admin-Rechte | – | Ja |

## Bewährte Sicherheitspraktiken

Sicherheit ist ein wesentlicher Aspekt jeder Organisation, insbesondere wenn es um die Verwaltung von Benutzerkonten und Zugriffsrechten geht. Hier sind einige bewährte Verfahren, um ein sicheres Benutzerverwaltungsprotokoll aufrechtzuerhalten:

* **Regelmäßige Passwortaktualisierungen:** Ermutigen Sie Benutzer, ihre Passwörter regelmäßig zu aktualisieren, um ihre Konten zu schützen. Legen Sie Richtlinien zur Passwortkomplexität fest und verlangen Sie die Verwendung sicherer Passwörter, die eine Kombination aus Buchstaben, Zahlen und Sonderzeichen enthalten.
* **Administratoraktionen überwachen:** Richten Sie Mechanismen ein, um Administratoraktivitäten zu überwachen und verdächtige oder ungewöhnliche Aktivitäten zu erkennen. Protokollieren Sie alle Administratoraktionen, einschließlich des Zugriffs auf sensible Daten oder Einstellungen, um Nachvollziehbarkeit zu gewährleisten und mögliche Sicherheitsverletzungen zu erkennen.
* **Anzahl der Administratoren begrenzen:** Halten Sie die Anzahl der Administratoren möglichst gering und gewähren Sie Administratorrechte nur denjenigen, die sie wirklich benötigen. Indem Sie die Zahl der Administratoren begrenzen, minimieren Sie das Risiko von Sicherheitsverletzungen und erleichtern die Verwaltung und Überwachung von Benutzerkonten.
* **Zwei-Faktor-Authentifizierung (2FA):** Implementieren Sie eine Zwei-Faktor-Authentifizierung für Administratorkonten, um die Sicherheit zusätzlich zu erhöhen. Dadurch wird ein zusätzlicher Sicherheitsschritt eingeführt, der sicherstellt, dass selbst bei Kompromittierung eines Kennworts ein Angreifer keinen unbefugten Zugriff auf das Konto erhält.
* **Regelmäßige Sicherheitsüberprüfungen:** Führen Sie regelmäßige Sicherheitsüberprüfungen und Audits durch, um potenzielle Sicherheitslücken oder Schwachstellen zu identifizieren und zu beheben. Überprüfen Sie die Zugriffsrechte und Berechtigungen von Benutzerkonten, um sicherzustellen, dass sie den aktuellen Anforderungen und Best Practices entsprechen.
* **Schulung und Sensibilisierung:** Schulen Sie Mitarbeiter und Administratoren regelmäßig zu bewährten Sicherheitspraktiken und zum Bewusstsein für Phishing-Angriffe und andere Cyberbedrohungen. Machen Sie ihnen die Bedeutung von Sicherheit bewusst und ermutigen Sie sie, verdächtige Aktivitäten zu melden.

Durch die Umsetzung dieser bewährten Verfahren können Organisationen die Sicherheit ihres Benutzerverwaltungsprotokolls verbessern und das Risiko von Sicherheitsverletzungen und Datenverlust minimieren. Es ist wichtig, Sicherheit als fortlaufenden Prozess zu betrachten und regelmäßige Aktualisierungen und Anpassungen vorzunehmen, um mit den sich ständig ändernden Bedrohungen und Sicherheitsanforderungen Schritt zu halten.
