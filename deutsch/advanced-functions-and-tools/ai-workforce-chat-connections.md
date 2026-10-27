# AI Workforce mit Teams und Discord verbinden

Sie benötigen ein aktives AI-Workforce-Abonnement, Rechte zur Verbindungsverwaltung und Zugriff auf den vorgesehenen Teams-Mandanten oder Discord-Server. Klären Sie eine angezeigte Abonnementanforderung zuerst mit dem Administrator.

## Microsoft Teams

1. Öffnen Sie **AI Workforce → Einstellungen → Integrationen**.
2. Wählen Sie **+ → Teams verbinden**. DocBits erzeugt einen Verbindungscode mit verbleibender Gültigkeitsdauer.
3. Folgen Sie der beim Code angezeigten Anweisung in der vorgesehenen Teams-Umgebung. Behandeln Sie den Code vertraulich und schließen Sie die Zuordnung vor Ablauf ab.
4. Warten Sie auf die Verbindungsbestätigung. Prüfen Sie Name und gemeinsamen oder eigenen Bot-Modus des neuen Eintrags.
5. Aktivieren Sie einen inaktiven Eintrag, wenn er Arbeit empfangen soll. Gespeichert und aktiv sind verschiedene Zustände.
6. Senden Sie eine unkritische Testanfrage aus dem vorgesehenen Teams-Kontext. Prüfen Sie in DocBits die zugehörige Mission, Quelle und Organisation sowie erforderliche Freigaben im Posteingang.

Für einen unternehmenseigenen Bot wählen Sie stattdessen die entsprechende Option. Geben Sie Verbindungsname, Mandanten-ID, App-ID und App-Geheimnis ein. Geheimnisse gehören in das Zugangsdatenformular, nicht in Prompts oder Screenshots.

## Discord

1. Wählen Sie unter **Integrationen → +** die Discord-Verbindung.
2. Fügen Sie den Bot bei angebotener Option mit einem berechtigten Serveradministrator zum richtigen Server hinzu.
3. Tragen Sie einen eindeutigen Namen und die richtige **Guild ID** ein. Dies ist die Serverkennung, nicht die Kanalkennung.
4. Erstellen Sie die Verbindung, prüfen Sie den Eintrag und aktivieren Sie ihn gegebenenfalls.
5. Testen Sie eine unkritische Anfrage und prüfen Sie entstandene Mission, Quelle und Organisation.

## Fehler eingrenzen

Erzeugen Sie bei abgelaufenem Teams-Code einen neuen Code und folgen Sie dessen aktueller Anweisung. Prüfen Sie bei fehlendem Eingang Aktivierung, Mandanten-/Serverkennung, Bot-Zugriff und Fehlermeldungen. Eine verbundene Integration belegt keine abgeschlossene Mission.

Siehe [AI Workforce](ai_workforce/README.md) für Missionen, Agentenrechte und Freigaben. Chat-Verbindungen sind von E-Mail-Import und Microsoft-Anmeldung getrennt.
