# Land im Feld prüfen

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_field_country_code_continue_v2-de-de.png" alt="Land im Feld prüfen, Version 2" width="634"><figcaption><p>Version 2</p></figcaption></figure>

Vorgesehener Einsatz: Ein zusätzlicher Verarbeitungsschritt hängt von einer Ländergruppe ab. Das folgende Beispiel beschreibt eine Regel für die Zugehörigkeit zur Europäischen Union.

## Aktuelle Einschränkung — Quellcodeprüfung vom 22. Oktober 2026

Lokale Quellcodetests mit dem nativen Typ der Regionsauswahl scheitern vor dem Ländervergleich und liefern `missing_variable` oder `error`. Vollständige Ländernamen umgehen dieses Problem nicht. Eine erfolgreiche Ausführung auf dem bereitgestellten Backend ist für diese Fassung nicht bestätigt.

**Ort:** Standard-Workflow → zusätzliche Bedingungen (Und) → Dokument Feld. Konfigurieren Sie die nachfolgende Aktion getrennt unter Dann.

## Konfiguration — Version 2

| Einstellung | Wert |
| --- | --- |
| Feld | Ein vorhandenes Textfeld mit dem Ländernamen |
| Operator | `is` |
| Region | Europäische Union (EU) |
| Fortsetzungswert | `true` |

<!-- workflow-card-practical-example-20261021 -->

## Beabsichtigtes Beispiel — Fehlerbehebung vor dem Einsatz prüfen

Prüfen Sie die Behebung und beide Beispielfälle in Ihrer installierten Version, bevor Sie diese Regel aktivieren. Die Tabelle beschreibt die beabsichtigte Geschäftsregel, keine bestätigte erfolgreiche Ausführung.

| Landwert im Feld | Beabsichtigte Länderzuordnung |
| --- | --- |
| `Germany` | Innerhalb der EU |
| `United States` | Außerhalb der EU |

Die Ländernamen in Codeformat sind feste Eingabewerte für dieses Beispiel.

## Grenzen und Prüfungen

`false` kehrt den Vergleich nicht um. Auch ein passendes Land erzeugt mit dieser Einstellung kein positives Bedingungsergebnis. Wählen Sie für die Gegenbedingung `isnot` mit `true`.

Behandeln Sie fehlende Felder und leere Länderwerte gesondert; sie können einen Status für fehlende Daten statt einer normalen Nichtübereinstimmung liefern.

Der ISO-Umwandlungsfehler bei Eingaben wie `DE` und `DEU` ist davon unabhängig. Der Wechsel zu vollständigen Ländernamen behebt den Fehler der Regionsauswahl nicht.

Die angebotenen Gruppen, darunter EU, Schengen und NAFTA, stammen aus der Kartenimplementierung. Prüfen Sie die Länderzuordnung Ihrer Version, bevor Sie eine Gruppe für eine Geschäftsregel verwenden.
