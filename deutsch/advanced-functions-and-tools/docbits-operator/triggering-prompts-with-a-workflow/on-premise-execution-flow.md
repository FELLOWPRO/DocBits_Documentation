# On-Premise Ausführungsablauf

Für Kunden, die den DocBits Operator lokal ausführen, beschreibt die folgende Sequenz, wie ein verarbeitetes Dokument einen Operator-Prompt über den lokalen DocBits-Agenten auslöst und ausführt.

1. **Dokumenten-Upload & Verarbeitung** Ein Dokument wird in DocBits hochgeladen und durchläuft die Standardverarbeitung (Extraktion, Validierung, usw.).
2. **Workflow-Auslöser** Nach Abschluss der Verarbeitung bewertet ein konfigurierter Workflow in DocBits seine Auslösebedingungen. Wenn diese Bedingungen erfüllt sind, erstellt der Workflow eine neue **Operator-Aufgabe**.
3. **Aufgabenerstellung & -versand**
   * Der Workflow sendet den Skripttext, Variablen, Max-Schritte, Max-Wiederholungen als Aufgaben-Payload an den gemeinsamen Arbeitspool.
4. **Agent-Polling-Schleife**
   * Ein lokal installierter DocBits-Agent (installiert in der Kundenumgebung) überprüft alle 5 Minuten den Arbeitspool. Wenn keine Aufgaben gefunden werden, bleibt der Agent untätig und versucht es nach dem Intervall erneut.
5. **Aufgaben-Ausführung**
   * Wenn eine Aufgabe im Arbeitspool erscheint, ruft der Agent sie ab und beginnt mit der Ausführung.
6. **Loggenerierung**
   * Für jeden Schritt - Erfolg oder Misserfolg - zeichnet der Agent detaillierte Protokolle auf (Aktionen, Status, Zeitstempel). Nach Abschluss erstellt er das vollständige Protokoll und den endgültigen Status.
7. **Ergebnisrückgabe & Anzeige**
   * Der Agent sendet die Protokolle und den Status an DocBits zurück. Die Laufhistorie des ursprünglichen Workflows wird aktualisiert, und Benutzer können Details im **Workflow-Protokoll**-Tab überprüfen.
