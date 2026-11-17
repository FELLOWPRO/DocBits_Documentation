# Dokumentfeld mit Referenzwert vergleichen

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_docfield_operator_value_v1-de-de.png" alt="Dokumentfeld mit Referenzwert vergleichen, Version 1" width="634"><figcaption><p>Version 1</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_docfield_operator_value_v2-de-de.png" alt="Dokumentfeld mit Referenzwert vergleichen, Version 2" width="634"><figcaption><p>Version 2</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-field-value/v1/de.mp4" %}

**Video:** Karte: Dokumentfeld mit einem Wert verglichen · 0:47 · [Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-field-value/v1/de.vtt)

<details>

<summary>Transkript</summary>

**Dokumentfeld mit einem Wert verglichen** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-field-value/v1/de.mp4#t=0.25)

Die Karte Dokumentfeld vergleicht ein Feld des Dokuments mit einem Wert, den Sie eingeben. Wählen Sie das Feld, zum Beispiel Gesamtbetrag, dann den Operator, hier Größer als, und den Wert, zehntausend.

**Text, Zahlen, Datumswerte** · [0:19](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-field-value/v1/de.mp4#t=19.016)

Textfelder können nur gleich oder ungleich sein, und Groß- und Kleinschreibung spielt keine Rolle. Zahlen und Datumswerte können auch größer oder kleiner als der Wert sein. Fehlt das Feld im Dokument, nimmt die Karte ihren Fehlerpfad.

**Beispiel: große Rechnungen brauchen eine zweite Freigabe** · [0:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-field-value/v1/de.mp4#t=34.35)

Zum Beispiel eine zweite Freigabe für große Rechnungen: Gesamtbetrag größer als zehntausend, dann die Zuweisungskarte für die Finanzabteilung. Kleinere Rechnungen erreichen diesen Schritt nicht.

</details>

## **Zweck:**

Diese Workflow-Karte ist darauf ausgelegt, Aktionen zu automatisieren, indem sie den Wert eines angegebenen Dokumentfelds mit einem Referenzwert oder einer Bedingung vergleicht. Sie sorgt für eine dynamische und präzise Entscheidungsfindung in Workflows auf Basis der Validierung von Dokumentdaten.

## **Bestandteile der Karte:**

1. **Feldname**
   * **Beschreibung:** Gibt den Namen des auszuwertenden Dokumentfelds an.
   * **Detail:** Dieser muss exakt mit dem Bezeichner des Feldes innerhalb des Dokuments übereinstimmen.
2. **Operatoren**
   * **Beschreibung:** Legt die Art des Vergleichs fest, der zwischen dem Feldwert und dem Referenzwert durchgeführt wird.
   * **Optionen:**
     * **Gleich (=):** Prüft, ob der Feldwert mit dem Referenzwert übereinstimmt.
     * **Ungleich (≠):** Stellt sicher, dass sich der Feldwert vom Referenzwert unterscheidet.
     * **Größer als (>):** Bestätigt, dass der Feldwert größer als der Referenzwert ist.
     * **Größer oder gleich (≥):** Überprüft, dass der Feldwert gleich oder größer als der Referenzwert ist.
     * **Kleiner als (<):** Prüft, ob der Feldwert kleiner als der Referenzwert ist.
     * **Kleiner oder gleich (≤):** Stellt sicher, dass der Feldwert kleiner oder gleich dem Referenzwert ist.

## **Funktionalität:**

* **Bedingungsauswertung:** Das System prüft, ob der Wert des Dokumentfelds in Bezug auf seine zugehörige Spalte die durch den Operator und den Referenzwert angegebene Vergleichsbedingung erfüllt.
* **Ausführung der Aktion:**
  * **Bedingung erfüllt (True):**\
    Erfüllt der Wert des Dokumentfelds die angegebene Bedingung (z. B. ist er gleich dem Referenzwert), löst das System die zugehörigen Aktionen aus. Dazu können das Aktualisieren von Datensätzen, das Fortführen des Workflows oder das Erzeugen von Benachrichtigungen gehören.
  * **Bedingung nicht erfüllt (False):**\
    Erfüllt der Wert des Dokumentfelds die angegebene Bedingung nicht, werden je nach Workflow-Konfiguration alternative oder keine Aktionen ausgeführt.

## **Einrichtung und Konfiguration:**

* Der Benutzer wählt den Feldnamen des relevanten Dokuments aus und wählt den Operator aus dem Dropdown-Menü. Anschließend gibt der Benutzer den Referenzfeldwert an, um die Konfiguration abzuschließen.

## **Fazit:**

Die Workflow-Karte "DocField Comparison Validation" ist ein robustes Werkzeug für die dynamische Dokumentverarbeitung. Indem sie Aktionen auf Basis von Feldvergleichen automatisiert, optimiert diese Karte Workflows, erhöht die Genauigkeit und unterstützt datengestützte Entscheidungen.

<!-- workflow-card-practical-example-20261021 -->

## Praxisbeispiel

**Wann zu verwenden:** Überprüfen Sie Rechnungen über einem definierten Betrag.

**Konfiguration:** Wählen Sie das numerische Feld „Gesamtbetrag“ (`total_amount`), den Operator „Größer als“ (`gt`) und den Referenzwert `1000`.

**Erwartetes Ergebnis und Gegenbeispiel:** Ein Wert von `1200` erfüllt die Bedingung. `1000` und `900` erfüllen sie nicht. „Größer als“ schließt den Grenzwert `1000` selbst aus.

Dies ist eine beispielhafte Konfiguration und ein erwartetes Ergebnis. Verwenden Sie in Ihrer Testorganisation konfigurierte Felder, Benutzer und Gruppen. Es wird nicht behauptet, dass dieses Beispiel ausgeführt wurde.

## Admin-Beispielvideo

Die Rechenergebnisse sind erwartete Beispiele; ein Workflow wurde nicht ausgeführt.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-numeric-comparison-admin/v2/de.mp4" %}

[Video mit deutschen Untertiteln öffnen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-numeric-comparison-admin/v2/de-theme-v4.html)

[Transkript lesen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-numeric-comparison-admin/v2/de.txt)
