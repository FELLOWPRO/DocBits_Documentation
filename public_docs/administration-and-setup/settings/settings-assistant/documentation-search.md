# Wie die Dokumentationssuche funktioniert

Der Settings Assistant sucht nach relevanten Informationen in den öffentlichen Seiten auf [docs.docbits.com](https://docs.docbits.com). Ergebnisse können einen Seitentitel, eine kurze Passage und einen Link auf die Quellseite enthalten. Öffnen Sie den Link, wenn Sie die vollständigen Anweisungen oder einen Screenshot brauchen.

## Die richtige Seite finden

Die Suche kombiniert Wortabgleich mit bedeutungsbasiertem Abgleich. Das hilft, wenn Ihre Frage andere Wörter verwendet als ein Seitentitel. Der Assistent kann außerdem die Einstellungsseite, die Sie gerade sehen, nutzen, um die Antwort relevanter zu machen.

Ist die bedeutungsbasierte Suche vorübergehend nicht verfügbar, kann die Dokumentationssuche weiterhin den Wortabgleich nutzen. Eine genaue Frage mit dem Namen der Einstellung ist der beste Weg für einen neuen Versuch.

## Sprachen

Die Dokumentationssuche verwendet derzeit die Hilfeseiten-Indizes für **Englisch** und **Deutsch**. Wenn Ihre DocBits-Oberfläche eine andere Sprache verwendet, greift der Assistent auf englische Dokumentationsergebnisse zurück. Die verlinkte Seite zeigt ihre eigene Sprache; prüfen Sie diese Sprache, bevor Sie Schritten folgen oder Screenshots vergleichen.

## Wann Änderungen durchsuchbar werden

Der Suchindex wird aktualisiert, wenn Änderungen an der englischen oder deutschen Dokumentation aus dem Dokumentations-Repository veröffentlicht werden. Ein regelmäßiger Abgleich entfernt außerdem Links auf Seiten, die nicht mehr in der Dokumentationsnavigation stehen. Eine neu veröffentlichte Seite kann kurze Zeit brauchen, bis sie im Assistenten erscheint.

### Technischer Überblick für Administratoren

Veröffentlichte Hilfeseiten werden in Abschnitte aufgeteilt und in einem eigenen **OpenSearch documentation index** je unterstützter Sprache gespeichert. Dieser Index ist getrennt von den Indizes, die für die hochgeladenen Dokumente einer Organisation verwendet werden. Ändert sich eine Seite, können unveränderte Abschnitte übersprungen und geänderte Abschnitte neu indexiert werden. Entfernte Seiten werden aus dem Dokumentationsindex gelöscht.

Für eine Frage kombiniert der Dienst Treffer nach Schlüsselwörtern mit Vektorähnlichkeit und ordnet dann die relevantesten Passagen. Ist der Embedding-Dienst nicht verfügbar, bleibt die Suche nach Schlüsselwörtern verfügbar. Der Settings Assistant erhält Quelllinks und kurze Passagen aus dieser Dokumentationssuche; er liest für diesen Zweck nicht den Dokumentindex einer Organisation.

Können Sie keine Seite finden, suchen Sie direkt auf [docs.docbits.com](https://docs.docbits.com), versuchen Sie eine genauere Frage oder wenden Sie sich an den DocBits-Support.

{% hint style="info" %}
Diese Suche umfasst die DocBits-Hilfeseiten. Die Funktion [Fulltext Search](../document-processing/module/fulltext-search.md) durchsucht die Dokumente Ihrer Organisation und hat eigene Einstellungen.
{% endhint %}

Zurück zur [Verwendung des Settings Assistant](README.md).
