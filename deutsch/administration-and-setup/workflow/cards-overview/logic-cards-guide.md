# Logikkarten: Variablen, Konvertierungen, JSON und Trigger

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-e019409102f9-de.png" alt="Konvertierungs- und JSON-Karten in der Kartenbibliothek. Karten für Organisationsvariablen benötigen den Advanced Builder; sichtbare Vorlagen hängen außerdem vom Release ab. Einzelne Feldbeschriftungen dieser Kartenversion sind in der Oberfläche derzeit noch englisch. Die Erläuterungen auf dieser Seite sind übersetzt."><figcaption><p>Konvertierungs- und JSON-Karten in der Kartenbibliothek. Karten für Organisationsvariablen benötigen den Advanced Builder; sichtbare Vorlagen hängen außerdem vom Release ab. Einzelne Feldbeschriftungen dieser Kartenversion sind in der Oberfläche derzeit noch englisch. Die Erläuterungen auf dieser Seite sind übersetzt.</p></figcaption></figure>

Verwenden Sie diese Karten im Advanced Workflow Builder, wo die ausgewählte Karte verfügbar ist. Die Sichtbarkeit der Karte hängt von Ihrer Version und den aktivierten Vorlagen ab. Die folgenden Referenzen beschreiben Version 2. Berücksichtigen Sie die in einem vorhandenen Workflow gespeicherte Version, wenn Sie deren Felder mit diesem Handbuch vergleichen.

## Wählen Sie den richtigen Wertspeicher

Eine aus dem Bedienfeld „Variablen“ ausgewählte Workflow-Variable der Organisation wird in allen Workflows gemeinsam genutzt und unabhängig von der Canvas gespeichert. Ein benanntes Tag, das von Konvertierungs-, JSON- und Tag-Vergleichskarten verwendet wird, gehört zum aktuellen Ausführungskontext. Durch das Erstellen eines Tags wird keine Organisationsvariable erstellt. Geben Sie den Tag-Namen ohne internes Speicherpräfix ein. Ein Dokumentfeld ist eine dritte, separate Datenquelle.

Eine Organisationsvariable und ein Ausführungstag bleiben getrennt, auch wenn ihre Namen übereinstimmen. Wählen Sie ein kompatibles Variablenfeld aus oder geben Sie explizit den Wert an, den die empfangende Karte erwartet. Siehe [Variablen](../advanced-workflow/variables.md) für Organisationsumfang und sofortiges Speichern.

## Aktionen für Organisationsvariablen

Erstellen Sie zunächst die Variable mit dem richtigen Typ und wählen Sie sie auf der Karte aus. Eine fehlende Variablenreferenz meldet `MISSING_VARIABLE`. Die Karten, die Variablen setzen, zeichnen den vorherigen und neuen Wert im Kartenprotokoll auf. Vermeiden Sie echte persönliche oder vertrauliche Daten in Testwerten und freigegebenen Protokollen.

| Karte | Erforderliche Eingabe | Ergebnis und Beispiel | Fehler- oder Grenzfall |
| --- | --- | --- | --- |
| `ACTION_LOGIC_SET_TEXT_VAR` | Textvariable und `value` | Speichert Text; Legen Sie beispielsweise ein Routing-Label auf `review` fest. | Ein fehlender Wert unterscheidet sich von einem absichtlich leeren Textwert. |
| `ACTION_LOGIC_SET_NUMBER_VAR` | Variable vom Typ Zahl und numerisch `value` | Speichert eine endliche Zahl; Legen Sie beispielsweise einen Schwellenwert auf `1000.50` fest. | Ungültiger numerischer Text, Unendlich und NaN werden abgelehnt. Verwenden Sie einen Dezimalpunkt ohne Währungssymbol. |
| `ACTION_LOGIC_CALC_NUMBER` | Zahlenvariable und `expression` | Speichert das arithmetische Ergebnis; `(100 + 20) / 2` ergibt `60`. | Unterstützt numerische Literale, Klammern, `+`, `-`, `*`, `/`, `%` und `**`. Namen, Funktionsaufrufe und Referenzen auf Dokumentfelder werden im Ausdruck nicht akzeptiert. Ungültige Ausdrücke oder Division durch Null schlagen fehl. |
| `ACTION_LOGIC_SET_BOOLEAN_VAR` | Ja/Nein-Variable und `value` | Setzt das Flag auf Ja oder Nein. | Verwenden Sie den von der Karte angebotenen booleschen Wert anstelle eines übersetzten Freitext-Synonyms. |
| `ACTION_LOGIC_INVERT_BOOLEAN` | Ja/Nein-Variable | Kehrt seinen aktuellen Wert um; Aus Ja wird Nein. | Initialisieren Sie die Variable, bevor Sie sich auf ein bestimmtes erstes Ergebnis verlassen. |

### Dokumentreferenzaktion

`ACTION_LOGIC_SET_DOCUMENT_VAR` speichert die aktuelle Dokument-ID in einer ausgewählten Dokumentvariablen. Es benötigt ein aktuelles Dokument; ohne eins meldet es `NO_DOCUMENT`. Ein ausgelöster Workflow erhält die Dokument-ID, kein serialisiertes Dokumentobjekt. Die überprüfte Implementierung verfügt über keine vordefinierte UI-Kartenvorlage für diese Aktion. Erwarten Sie daher nicht, dass sie in jeder Kartenauswahl angezeigt wird. Verwenden Sie es nur, wenn Ihr Administrator bestätigt, dass eine passende Vorlage verfügbar ist; Die Eingabe einer Dokument-ID in das Variablenerstellungsformular ist kein Ersatz.

## Tags und Typkonvertierungen

Diese Aktionen verwenden Tag-Namen im aktuellen Ausführungskontext. Erstellen Sie das Eingabe-Tag, bevor Sie es lesen. Ein fehlendes Eingabe-Tag oder ein fehlender Name meldet `MISSING_VARIABLE`; Eine ungültige numerische Konvertierung meldet einen Konfigurationsfehler. Die Ausgabe ist ein neues oder überschriebenes Tag, kein extrahiertes Dokumentfeld.

| Karte | Eingaben | Ausgabe und Beispiel |
| --- | --- | --- |
| `ACTION_LOGIC_CREATE_TEXT_TAG` | `tag_name`, `value` | Erstellt ein Text-Tag; `raw_amount` mit Wert `125.50`. Ein leerer Textwert ist zulässig. |
| `ACTION_LOGIC_CONVERT_TO_NUMBER` | `input_tag`, `output_tag` | Konvertiert `125.50` in die Zahl `125.5`. Ein Boolescher Wert wird zu `1` oder `0`. Text wie `EUR 125,50` ist keine gültige numerische Eingabe. |
| `ACTION_LOGIC_CONVERT_TO_TEXT` | `input_tag`, `output_tag` | Wandelt den gespeicherten Wert in Text um. Es formatiert keine Währung und lokalisiert keine Dezimaltrennzeichen. |
| `ACTION_LOGIC_CONVERT_TO_BOOLEAN` | `input_tag`, `output_tag` | Konvertiert einen vorhandenen Booleschen Wert direkt; Eine Zahl ungleich Null wird wahr und Null wird falsch. Verwenden Sie `true` oder `false` für die vorhersehbare Texteingabe und testen Sie andere akzeptierte Darstellungen. |

### Konvertierungsbeispiel

1. Erstellen Sie ein Text-Tag `raw_amount` mit dem Wert `125.50`.
2. Wandeln Sie `raw_amount` in eine Zahl um und schreiben Sie in `amount_number`.
3. Verwenden Sie „Zahl größer als“, wobei `tag_name` auf `amount_number` und `value` auf `100` eingestellt ist.
4. Überprüfen Sie, ob die Bedingung für `125.50` erfolgreich ist, für `100` fehlschlägt und in Schritt 2 einen Konvertierungsfehler für `EUR 125,50` meldet.

## Werte aus JSON lesen

Alle drei Lesekarten nehmen `json_text`, `json_path` und `output_tag` an. Trotz seines Namens ist `json_text` der Name eines Tags, das JSON enthält, und kein Feld zum Einfügen eines wörtlichen JSON-Dokuments. Erstellen Sie zuerst dieses Tag, zum Beispiel mit „Text-Tag erstellen“.

Pfade sind durch Punkte getrennte Schlüssel und nullbasierte Listenindizes: `invoice.lines.0.amount`. Verwenden Sie keine JSONPath-Syntax wie `$.invoice.lines[0].amount`. Wenn ein Schlüssel fehlt, ein Index ungültig ist oder JSON ungültig ist, ist das Ergebnis `ERROR_CARD_SETUP`; ein fehlendes Quell-Tag meldet `MISSING_VARIABLE`.

| Karte | Ausgabe |
| --- | --- |
| `ACTION_LOGIC_JSON_TO_NUMBER` | Numerischer Wert; Numerischer Text wird konvertiert und ein boolescher Wert wird zu `1` oder `0`. Ungültiger numerischer Text schlägt fehl. |
| `ACTION_LOGIC_JSON_TO_TEXT` | Textdarstellung des ausgewählten Werts. Dies ist kein Versprechen der JSON-Serialisierung für verschachtelte Objekte. |
| `ACTION_LOGIC_JSON_TO_BOOLEAN` | Ein Boolescher Wert; Text `true`, `1` oder `yes` ist nach Kleinschreibung wahr, während anderer Text falsch ist. Zahlen folgen ihrem Null-/Nicht-Null-Wert. |

Für ein Tag `payload`, das den folgenden JSON enthält, führt das Einlesen von `invoice.lines.0.amount` in `amount` mit JSON zu Zahl zu `125.5`:

```json
{"invoice":{"lines":[{"amount":"125.50"}],"approved":false}}
```

Testen Sie auch einen nicht vorhandenen Pfad, einen Index außerhalb des gültigen Bereichs und fehlerhaftes JSON. Ein fehlgeschlagener Lesevorgang darf nicht als gültige Null oder erfolgreiche Genehmigung behandelt werden.

## JSON aktualisieren

Die vier Schreibkarten nehmen `json_tag`, `json_path` und `value` auf. `json_tag` benennt ein vorhandenes Tag, das JSON enthält. Sie aktualisieren dieses Tag mit serialisiertem JSON. Es gilt die gleiche durch Punkte getrennte Pfadsyntax. Fehlende Zwischenobjektschlüssel können erstellt werden, Listenindizes müssen jedoch vorhandene Elemente identifizieren. Sie erweitern keine Liste und unterstützen keine Platzhalterpfade.

| Karte | Wert und Wirkung |
| --- | --- |
| `ACTION_LOGIC_JSON_SET_NUMBER` | Ein numerischer Wert, z. B. `125.5`; speichert eine JSON-Nummer. Ungültiger numerischer Text schlägt fehl. |
| `ACTION_LOGIC_JSON_SET_TEXT` | Text, z. B. `review`; speichert einen JSON-String. |
| `ACTION_LOGIC_JSON_SET_BOOLEAN` | Text `true`, `1` oder `yes` wird nach Kleinschreibung auf true gesetzt; Anderer Text wird auf „falsch“ gesetzt. Bevorzugen Sie `true` und `false`. |
| `ACTION_LOGIC_JSON_SET_JSON` | Gültiges JSON, z. B. `{"status":"review"}`; fügt diesen analysierten Wert ein, nicht seinen zitierten Text. Ungültiges JSON schlägt fehl. |

Legen Sie beispielsweise den Pfad `invoice.approved` auf `true` in `payload` fest, wobei JSON den Wert „Boolean“ verwendet. Lesen Sie dann denselben Pfad mit JSON in Boolean ein und überprüfen Sie, ob er wahr ist. Bevor Sie fortfahren, muss im Kartenprotokoll ein fehlendes Quell-Tag, ein ungültiger JSON-Code oder ein ungültiger Pfad diagnostiziert werden.

## Bedingungen

Alle unten aufgeführten sechs Bedingungen sind Version 2. Eine falsche Bedingung ist ein Geschäftsergebnis, keine erfolgreiche Aktion oder ein Ausführungsfehler. In einer Bedingungssequenz im Standardstil werden die folgenden Aktionen verhindert: Verbinden Sie in einem erweiterten Workflow das Ergebnis mit dem vorgesehenen Zweig.

| Karte | Felder | Bewertung und wichtige Grenze |
| --- | --- | --- |
| `CONDITION_LOGIC_VALUE_EQUALS` | `tag_name`, `value` | Vergleicht Textdarstellungen genau, einschließlich Groß- und Kleinschreibung. Verwenden Sie dies nicht als Prüfung auf Vorhandensein: Ein fehlendes Tag wird nicht automatisch als Fehler gemeldet. |
| `CONDITION_LOGIC_BOOLEAN_IS` | `tag_name` | Überprüft, ob das Tag wahr ist. Ein fehlendes Tag wird als falsch ausgewertet. Verwenden Sie einen echten Booleschen Wert, um zuverlässige Ergebnisse zu erhalten. |
| `CONDITION_LOGIC_TEXT_CONTAINS` | `tag_name`, `value` | Suche nach Teilzeichenfolgen unter Berücksichtigung der Groß- und Kleinschreibung. Ein fehlendes Tag wird als leerer Text behandelt. Eine leere Suchzeichenfolge entspricht; Legen Sie den Suchwert immer bewusst fest. |
| `CONDITION_LOGIC_NUMBER_LESS` | `tag_name`, numerisch `value` | Streng weniger als. Ein fehlendes Tag oder ein ausgelassener Vergleichswert wird standardmäßig auf Null gesetzt; Ungültige numerische Daten sind ein Konfigurationsfehler. |
| `CONDITION_LOGIC_NUMBER_GREATER` | `tag_name`, numerisch `value` | Streng größer als. Ein Wert gleich dem Schwellenwert erfüllt diese Bedingung nicht. Es gelten die gleichen Null-Standardwerte und das gleiche Verhalten bei numerischen Fehlern. |
| `CONDITION_LOGIC_EXPRESSION` | `value1`, `operator`, `value2` | Unterstützt `==`, `!=`, `<`, `<=`, `>`, `>=`, `contains`, `not_contains`. Es versucht zunächst einen numerischen Vergleich und vergleicht ansonsten Text. Es handelt sich nicht um ein beliebiges Python-Ausdrucksfeld. |

Für eine Zahl größer als `100` testen Sie `99`, `100` und `101`. Für Text enthält `ABC`, testen Sie `ABC`, `abc` und eine leere Suche. Überprüfen Sie sowohl den Zweig als auch das Protokoll. Ein grauer Knoten wurde übersprungen und weist darauf hin, dass der Vergleich nicht erfolgreich war.

## Auslöser

| Karte | Konfiguration | Wenn es passt |
| --- | --- | --- |
| `CONDITION_LOGIC_VAR_CHANGED` | Wählen Sie eine Organisationsvariable aus. Die gespeicherte Referenz verwendet ihre ID, sodass das Umbenennen der Variablen nicht absichtlich das Ziel ändert. | Die bereitgestellten aktuellen und vorherigen Variablenwerte unterscheiden sich. Das Wiederholen desselben Werts stellt keine Änderung dar. Eine fehlende Variablenreferenz meldet `MISSING_VARIABLE`. |
| `CONDITION_LOGIC_WEBHOOK_EVENT` | Optional `event_name`. | Im Workflow-Ausführungskontext ist eine Webhook-Nutzlast vorhanden. Bei einem Namen muss der `event`-Wert der Nutzlast genau übereinstimmen; Ohne Namen stimmt jedes angegebene Webhook-Ereignis überein. Kein Ereignis bedeutet falsch. |

Durch die Auswahl eines Webhook-Ereignisses wird weder ein öffentlicher Webhook-Endpunkt noch dessen Authentifizierung erstellt. Ihre Integration muss das Ereignis über einen konfigurierten Einstiegspunkt bereitstellen. Testen Sie das passende Ereignis, ein anderes Ereignis und kein Ereignis. Testen Sie für einen Variablentrigger eine echte Wertänderung und einen unveränderten Wert und vermeiden Sie eine Kette, die dieselbe gemeinsam genutzte Variable wiederholt neu schreibt.

## Testen und diagnostizieren

Validieren Sie das Diagramm, testen Sie jeden Zweig mit repräsentativen Eingaben und überprüfen Sie [Workflow-Protokolle](../workflow-logs.md). Berücksichtigen Sie fehlende Tags, ungültiges JSON, falsche Variablentypen, numerische Grenzen und falsche Bedingungen. Ein Test ohne Dokument kann keine dokumentabhängige Aktion nachweisen. Überprüfen Sie die gespeicherte Kartenversion und den Aktivierungsstatus noch einmal, bevor Sie sich auf die automatische Ausführung verlassen.
