# Klassifizierung und Extraktion

## Überblick

In den **Klassifizierung und Extraktion**-Einstellungen können Sie:

* Die **Aufteilung von Dokumenten** basierend auf QR-Codes aktivieren
* Die **Betragsformatierung** konfigurieren
* Die **Tabelle Extraktion** einrichten
* Die Verarbeitung nicht unterstützter **ZUGFeRD**-Dateien umschalten
* Spezielle Klassifizierungsregeln definieren
* Benutzerdefiniert trainierte **AI-Modelle** überwachen, die im Klassifizierungsprozess verwendet werden

Diese Seite bietet eine detaillierte Erklärung aller verfügbaren Einstellungen.

## **Zugriff auf die Einstellungen für Klassifizierung und Extraktion**

Um auf die **Klassifizierung und Extraktion**-Einstellungen zuzugreifen, gehen Sie zu:\
**Einstellungen → Verarbeitung von Dokumenten → Klassifizierung und Extraktion**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_classification_and_extraction.png)

## Aufteilung von Dokumenten

Im Abschnitt **Aufteilung von Dokumenten** können Sie konfigurieren, ob ein hochgeladenes Dokument in mehrere Dokumente aufgeteilt werden soll, sobald auf einer seiner Seiten ein **Barcode** erscheint.

So aktivieren Sie diese Funktion:

1. Gehen Sie zum Abschnitt **Aufteilung von Dokumenten**.
2.  Öffnen Sie das Dropdown-Menü.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_14.png)
3.  Wählen Sie **Aufteilung nach Barcode/QR-Code**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_15.png)

Anschließend haben Sie die Möglichkeit:

* Einen oder mehrere zu erkennende Barcode-Typen auszuwählen.
*   Ein regex-Muster anzugeben, dem der Barcode entsprechen muss, um die Aufteilung von Dokumenten auszulösen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_16.png)

## Betragsformatierung

Im Abschnitt **Betragsformatierung** haben Sie zwei Optionen:

* **Rundung beim Betragsvergleich zulassen:**\
  Ist dies aktiviert, ist beim Betragsvergleich eine Toleranz von ±0.5 zulässig.\
  Ist es deaktiviert, gilt eine Standardtoleranz von ±0.05.
* **Genaue Übereinstimmung für Betragsvergleich erforderlich:**\
  Ist dies aktiviert, müssen Beträge exakt ohne Toleranz übereinstimmen.\
  Ist es deaktiviert, ist eine Toleranz von ±0.05 zulässig.

<mark style="color:red;">**Hinweis**</mark>: Nur eine dieser Einstellungen kann jeweils aktiv sein.

## Tabelle Extraktion

{% hint style="info" %}
**Voraussetzungen für eine funktionierende Tabellenextraktion**

* Der Dokumenttyp hat **Tabellenspalten** (Einstellungen → Globale Einstellungen → Dokumenttypen → [Tabellenspalten](../../global-settings/document-types/table-columns.md)). Ohne Spalten gibt es nichts, wohin extrahiert werden kann.
* **Tabelle Extraktion** oder **AI-Tabellen-Extraktion** ist unten eingeschaltet, für die gesamte Organisation.
* Das Dokument hat lesbaren Text: OCR ist gelaufen, oder für digital erzeugte PDFs wird E-Text verwendet ([OCR-Einstellungen](../ocr-settings.md)).
* Training und AI-Modelle gelten **pro Lieferant**. Eine trainierte Tabelle gilt nur für Dokumente des Lieferanten, an dem sie trainiert wurde.
{% endhint %}

Sie können Tabellen aus Dokumenten extrahieren, indem Sie entweder **Tabelle Extraktion** oder **AI-Tabellen-Extraktion** aktivieren. Eine trainierte Tabelle (ob AI-basiert oder manuell) ist immer einem bestimmten Lieferanten zugeordnet.

**Tabelle Extraktion:** Aktiviert die regelbasierte Tabellenextraktion. Tabellen werden pro Lieferant im Validierungsbildschirm trainiert (*Zur Ansicht der Tabellenextraktion wechseln*).\
Mehr über das Training erfahren Sie [hier](../../../../administration-and-setup/setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).

**AI-Tabellen-Extraktion:** Verwendet AI, um die Tabelle jedes Lieferanten ohne Training zu extrahieren. Sind die Ergebnisse für einen Lieferanten nicht genau genug, trainieren Sie die Tabelle dieses Lieferanten; die gespeicherten Regeln haben für diesen Lieferanten dann Vorrang vor der AI.

**Tabellenextraktions-Vision (KI) verwenden:** Die AI liest das Seitenbild statt der Textebene. Hilft bei gescannten Dokumenten und Tabellen ohne klare Textstruktur; langsamer.

**Strukturierte Extraktion nutzen (KI):** Die AI liefert die Tabelle in einer festen Struktur, die direkt auf die konfigurierten Tabellenspalten abgebildet wird. Empfohlen, wenn die Spaltenüberschriften auf den Dokumenten stark variieren.

**Tabellenextraktion für Kalkulationselement:** Wenn aktiviert, kann DocBits Kalkulationselemente auf Zeilenebene aus Tabellen extrahieren und entsprechend klassifizieren.\
Ausführliche Erläuterung [hier](table-extraction-for-costing-element.md).

**Steuercode automatisch extrahieren:** Wenn aktiviert, füllt das System automatisch das Feld **Steuercode** im Validierungsbildschirm aus, vorausgesetzt, ein Steuercode-Feld ist konfiguriert.\
Weitere Informationen zu dieser Einstellung [hier](../../../../administration-and-setup/settings/document-processing/classification-and-extraction/auto-extract-tax-code.md).

**Extraktionsregeln speichern (nur für Administratoren):** Nur Administratoren können im Tabellentraining auf *Regeln speichern* klicken. Schalten Sie die Option ein, wenn Benutzer immer wieder Regeln speichern, die die Extraktion eines Lieferanten beschädigen.

**AI-Modell:** Wählt die AI-Stufe für die Tabellenextraktion: **Fast** (Standard), **Full** (höchste Genauigkeit, langsamer) oder **Nexus** (optionale dritte Stufe). Die Tabelle unter der Auswahl zeigt:

* Welche **Lieferanten** welches AI-Modell verwenden
* Ob sie E-Text verwenden
* Optionen, um einen Eintrag zu löschen oder die Trainingsdaten zurückzusetzen

Diese Einstellung wird im Detail [hier](../../../../administration-and-setup/settings/document-processing/classification-and-extraction/ai-model.md) erklärt.

### Warum sieht die Tabelle je Lieferant anders aus?

Alles, was DocBits über eine Tabelle lernt, wird **pro Lieferant** gespeichert:

* **Gespeicherte Regeln** (Tabellentraining): Position der Tabelle und Zuordnung ihrer Spalten im Layout dieses Lieferanten.
* **AI-Tabellen-Tags und Formatierungsregeln**: Hinweise, die der Benutzer für die AI-Tabelle dieses Lieferanten gespeichert hat.
* **Lieferantenspezifisches AI-Modell**: die Stufe, die für diesen Lieferanten unter *Weitere Einstellungen* im Validierungsbildschirm gewählt wurde.

Lieferant A mit gespeicherten Regeln zeigt also eine deterministische Tabelle im Tab *Extrahierte Tabelle* des Validierungsbildschirms, während Lieferant B ohne Regeln die *KI Extrahierte Tabelle* erhält. Damit sich Lieferant B wie A verhält, trainieren Sie die Tabelle von B einmal. Um einen Lieferanten zurückzusetzen, löschen Sie seine Regeln im Validierungsbildschirm oder setzen Sie seine Trainingsdaten in der Tabelle unter AI-Modell zurück.

### Präferenzschlüssel

Jeder Schalter in diesem Abschnitt wird als Organisationspräferenz gespeichert. Verwenden Sie den Schlüssel, wenn Sie den Wert über die API (`/preferences/set_preference`), ein Skript oder das DocBits MCP (`get_preference` / `set_preference`) setzen.

| Einstellung (UI-Beschriftung) | Präferenzschlüssel | Werte |
|---|---|---|
| Tabelle Extraktion | `TABLE_EXTRACTION_SETTING` | `true` / `false` |
| AI-Tabellen-Extraktion | `USE_AI_TABLE_EXTRACTION` | `true` / `false` |
| Tabellenextraktions-Vision (KI) verwenden | `TABLE_EXTRACTION_USE_VISION` | `true` / `false` |
| Strukturierte Extraktion nutzen (KI) | `USE_STRUCTURED_EXTRACTION` | `true` / `false` |
| Tabellenextraktion für Kalkulationselement | `CHARGES_TABLE_EXTRACTION` | `true` / `false` |
| Steuercode automatisch extrahieren | `AUTO_EXTRACT_TAX_CODE` | `true` / `false` |
| Extraktionsregeln speichern (nur für Administratoren) | `ONLY_ADMIN_CAN_SAVE_RULES` | `true` / `false` |
| AI-Modell | `AI_MODEL` | `gpt-5.4-mini` (Fast), `gpt-5.5` (Full), `qwen3.8-max` (Nexus) |
| Version der Tabellenextraktion (Bestätigungsdialog) | `TBL_EXT_VERSION` | Versionszeichenfolge |
| OCR-Einstellungen → Verwenden Sie AI-Daten für Tabellen, falls verfügbar | `USE_AI_DATA_FOR_TABLE` | `true` / `false` |
| OCR-Einstellungen → E-Text verwenden, falls verfügbar | `USE_ETEXT_IF_AVAILABLE` | `true` / `false` |

Hinweise:

* Boolesche Präferenzen werden als Zeichenfolgen `true` / `false` gespeichert; ein nie gesetzter Schlüssel zählt als `false`. Wenn Sie `1` oder `0` senden, speichert DocBits `true` / `false`.
* Ein nicht gesetztes `AI_MODEL` bedeutet **Fast**.
* Eine Änderung eines Schlüssels wirkt auf Dokumente, die danach verarbeitet werden. Starten Sie ein Dokument neu, um es mit der neuen Einstellung erneut zu extrahieren.
* Lieferantenspezifische Entscheidungen (E-Text, AI-Modell, gespeicherte Regeln) sind keine Organisationspräferenzen; sie werden im Validierungsbildschirm unter *Weitere Einstellungen* für ein Dokument des jeweiligen Lieferanten gesetzt.

## Elektronisches Dokument

**Nicht unterstützte ZUGFeRD PDF verarbeiten:** Wenn aktiviert, werden nicht unterstützte **ZUGFeRD**-Versionen als Standard-PDFs verarbeitet und das eingebettete XML wird ignoriert.

Die Liste der unterstützten **ZUGFeRD**-Versionen finden Sie [hier](../../../../administration-and-setup/settings/global-settings/document-types/edi/zugferd/README.md).

## **Klassifizierungsregeln**

Im Abschnitt **Klassifizierungsregeln** können Sie spezifische **regex**-Muster und Kriterien definieren, um dem System zu helfen, Dokumente während der Verarbeitung automatisch zu klassifizieren.

Um auf diesen Abschnitt zuzugreifen, klicken Sie oben auf der Seite auf den Tab **Klassifizierungsregeln**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_1.png)

### **Neue Klassifizierungsregel hinzufügen**

So erstellen Sie eine neue Regel:

1.  Klicken Sie oben rechts auf **Hinzufügen**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_2.png)
2. Füllen Sie die folgenden Felder aus:
   * **Muster**: Das regex-Muster, nach dem das System suchen soll, um die Klassifizierung auszulösen.
   * **Typ**: Wo nach dem Muster gesucht werden soll (z. B. **Barcode**).
   * **Unterorganisation** _(optional)_: Geben Sie an, für welche Unterorganisation die Regel gilt.
   * **Dokumenttyp**: Definieren Sie den Dokumenttyp, der zugewiesen werden soll, wenn das Muster gefunden wird.
   *   **Unterdokument Typ** _(optional)_: Geben Sie einen Untertyp für eine detailliertere Klassifizierung an.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_3.png)
3.  Klicken Sie auf **Speichern**, um Ihre Klassifizierungsregel zu speichern.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_4.png)

### **Eine Klassifizierungsregel bearbeiten**

So bearbeiten Sie eine bestehende Regel:

1.  Klicken Sie in der Spalte **Aktionen** auf die drei Punkte.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_5.png)
2.  Wählen Sie **Bearbeiten**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_6.png)
3. Nehmen Sie die gewünschten Änderungen vor.
4.  Klicken Sie auf **Speichern**, um die Aktualisierungen zu übernehmen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_4.png)

### **Eine Klassifizierungsregel löschen**

So löschen Sie eine Regel:

1.  Klicken Sie in der Spalte **Aktionen** auf die drei Punkte.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_5.png)
2.  Wählen Sie **Löschen**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_7.png)

## AI-Modelle

Der Bereich **AI-Modelle** zeigt alle benutzerdefiniert trainierten Modelle an, die speziell für Ihre Anforderungen feinabgestimmt wurden.

### Zugriff auf den Bereich AI-Modelle

Um diesen Bereich zu öffnen, klicken Sie oben auf der Seite auf den Tab **AI-Modelle**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_8.png)

### Modellkategorien

Modelle sind in Kategorien organisiert. Unter jedem Kategorienamen wird die Anzahl der enthaltenen Modelle angezeigt.\
Klicken Sie auf eine Kategorie, um ihre Details anzuzeigen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_9.png)

Oben auf der Seite der ausgewählten Kategorie sehen Sie wichtige Informationen zu jedem Modell:

* **Typ**: Der Typ des Modells.
* **Nur erste Seite**: Gibt an, ob das Modell nur die erste Seite eines Dokuments verarbeitet.
* **Version**: Die Versionsnummer des Modells.

### Modelltabelle

Alle Modelle innerhalb einer Kategorie werden in einer Tabelle aufgeführt, die folgende Informationen enthält:

* **Name**: Der Name des Modells.
* **Nächstes Modell**: Das Modell, das die Ausgabe des aktuellen Modells weiterverarbeitet.
* **Dokumenttyp**: Der primäre Dokumenttyp, der vom Modell während der Klassifizierung zugewiesen wird.
* **Untertypen von Dokumenten**: Die Untertypen, in die das Dokument weiter klassifiziert wird.
* **Priorität**: Die Prioritätsstufe, die die Position des Modells in der Klassifizierungswarteschlange bestimmt.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_11.png)

### Ein Modell bearbeiten

So bearbeiten Sie ein Modell:

1.  Klicken Sie in der Spalte **Aktionen** neben dem Modell, das Sie bearbeiten möchten, auf das Stiftsymbol.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_10.png)
2. Aktualisieren Sie die verfügbaren Felder:
   * **Nächstes Modell**: Wählen Sie das Modell, das die Ausgabe des aktuellen Modells verarbeiten soll.
   * **Dokumenttyp**: Wählen Sie den Dokumenttyp, als den das Modell die Eingabe klassifizieren soll.
3.  Klicken Sie auf **Speichern**, um Ihre Änderungen zu übernehmen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_12.png)
