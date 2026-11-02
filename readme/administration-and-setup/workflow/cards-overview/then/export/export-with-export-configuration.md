# Export with Export Configuration

**Start Export** verwendet den eingerichteten Exportweg. **Export with Export Configuration** führt eine ausgewählte Konfiguration aus. Die verzögerte Variante merkt diese Konfiguration für den finalen Export am Ende des aktuellen Laufs vor. Vormerken heißt nicht „nach allen späteren Benutzerfreigaben automatisch senden“.

Die geprüften neuen Versionen bieten `status=finished` oder `status=exported`: finished schließt das Dokument, exported lässt die weitere Bearbeitung zu. Start Export trägt die Auswahl ab v4, konfigurierter und verzögerter Export ab v3. Ältere Versionen verwenden finished. Fehlt die Auswahl in den neuen Versionen, sieht der Code ebenfalls finished vor; ein ungültiger Wert ist ein Konfigurationsfehler.

Mit `ignore_pending_tasks=false` werden offene Aufgaben berücksichtigt. Beim unmittelbaren konfigurierten Export kann der Dienst den Export deshalb verweigern. Die Karte belegt keine automatische Wiederaufnahme nach späterer Erledigung. Klären Sie den erneuten Ausführungsanlass und prüfen Sie vor einem neuen Versand, ob bereits ein Zielbeleg existiert. Aktivieren Sie das Ignorieren nicht als Ersatz für die Freigabe.

Schließen Sie den Export erst an eine ausdrücklich geprüfte Freigabebedingung an. Die Abnahme umfasst offene Aufgabe, erledigte Aufgabe, fehlende Freigabe, erfolgreichen Testziel-Empfang und erneuten Lauf. Unterscheiden Sie Export angefordert, vom Empfänger erhalten und im ERP verarbeitet. Das Übungspaket enthält keine echten Exportziele; seine Testergebnisse belegen keine Zustellung.

[P1: Exportvarianten, offene Aufgaben und Abschlussstatus](../../../masterclass/export-lifecycle.md)

<figure><img src="../../../../../.gitbook/assets/And1.png" alt="" width="563"><figcaption></figcaption></figure>
