# KI-Assistent im Skript-Editor

Der Skript-Editor hat einen eingebauten **KI-Assistenten**, der DocBits-Skripte für Sie schreibt und erklärt. Sie beschreiben in einfachen Worten, was das Skript tun soll, und der Assistent antwortet mit Python-Code, den Sie in den Editor übernehmen können.

{% hint style="info" %}
Der KI-Assistent gehört zu **DocNet**. Ihre Organisation braucht ein aktives DocNet-Abonnement, um ihn zu nutzen. Siehe [Abonnement-Plan](../../subscription-plan/README.md) und [Module](../../../document-processing/module/README.md).
{% endhint %}

## Assistenten öffnen

1. Öffnen Sie **Einstellungen → Dokumenttypen**, wählen Sie den Dokumenttyp und klicken Sie auf **Skripte**.
2. Klicken Sie auf **Neu** oder öffnen Sie eine vorhandene Skriptversion als Entwurf.
3. Klicken Sie auf das Roboter-Symbol neben dem Skriptnamen. Rechts im Editor öffnet sich das Panel **KI-Assistent**.

## Was der Assistent kennt

Mit jeder Frage übergibt DocBits dem Assistenten:

* die **Skript-Referenz** (die Funktionen aus [Skripterstellung in DocBits](scripting-in-docbits/README.md)),
* den **Dokumenttyp** des Skripts,
* das **aktuelle Skript** aus dem Editor,
* die **Feldnamen und Tabellenspalten**, die Ihre Organisation für diesen Dokumenttyp verwendet.

Dank der Feldnamen verwendet der Assistent Ihre echten Felder, zum Beispiel `invoice_date` oder `purchase_order`, in `get_field_value()` und `set_field_value()`.

## Skript mit dem Assistenten schreiben

1. Geben Sie Ihre Anfrage unten im Panel ein, zum Beispiel: *Setze die Währung auf EUR, wenn sie leer ist.*
2. Drücken Sie **Enter** oder klicken Sie auf das Senden-Symbol. Die Antwort erscheint nach und nach.
3. Klicken Sie neben einem Code-Block auf das Kopier-Symbol (Tooltip **An den Redakteur senden**), um den Code in den Skript-Editor zu übernehmen.
4. Prüfen Sie den Code, vergeben Sie einen Namen und speichern Sie das Skript als Entwurf.

Nachfragen funktionieren im selben Panel. Fügen Sie eine Fehlermeldung ein oder fragen Sie *Warum setzt dieses Skript das Fälligkeitsdatum nicht?*, dann sieht der Assistent das aktuelle Skript im Editor.

## Ergebnis immer prüfen

{% hint style="warning" %}
Der Assistent kann sich irren. Lesen Sie den erzeugten Code, prüfen Sie, ob die Feldnamen zu Ihrem Dokumenttyp passen, und testen Sie das Skript mit einem Testdokument, bevor Sie es aktivieren. Siehe [Testen von Skripten](testing-scripts.md).
{% endhint %}

Skripte laufen nur mit den freigegebenen Skriptfunktionen. Ruft ein Skript eine Funktion auf, die es nicht gibt, lehnt DocBits es mit der Meldung *Unknown function* ab.

## Nutzung und Grenzen

* Unter jeder Antwort steht, wie viele Token sie verbraucht hat (Eingabe, Ausgabe und gesamt).
* Die Nutzung wird als DocNet-Nutzung Ihrer Organisation erfasst.
* DocBits lehnt die Anfrage ab, wenn das DocNet-Abonnement fehlt (*DocNet subscription required*), abgelaufen ist (*DocNet subscription expired*) oder das Kontingent aufgebraucht ist (*DocNet quota exhausted*).

## Verwandte Seiten

* [Erstellen und Bearbeiten von Skripten](creating-and-editing-scripts.md)
* [Feldfunktionen](scripting-in-docbits/field-functions.md)
* [Beispielskripte](scripting-in-docbits/sample-scripts/README.md)
