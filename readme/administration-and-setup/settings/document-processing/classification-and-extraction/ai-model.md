# AI-Modell

## Übersicht

Die Einstellung **AI-Modell** ermöglicht es Ihnen zu definieren, welches AI-Modell standardmäßig für die **Feldextraktion** und **Tabelle Extraktion** während der Dokumentenverarbeitung verwendet wird.\
In diesem Abschnitt können Sie die Token-Kosten für jedes Modell einsehen und sehen, welches Modell derzeit jedem Lieferanten zugewiesen ist.

## So greifen Sie zu

1.  Navigieren Sie zu **Einstellungen** → **Verarbeitung von Dokumenten** → **Klassifizierung und Extraktion**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_classification_and_extraction.png)
2.  Scrollen Sie nach unten zum Abschnitt **Tabelle Extraktion**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_1.png)

## AI-Modell-Optionen

DocBits bietet drei AI-Modell-Optionen für die Feld- und Tabellenextraktion. Sie unterscheiden sich im Gleichgewicht zwischen **Extraktionsgenauigkeit**, **Verarbeitungsgeschwindigkeit** und **Token-Kosten pro Dokument** – so können Sie die Option an die Art Ihrer Dokumente anpassen. Fahren Sie mit der Maus über das Informationssymbol neben der Einstellung, um die Token-Kosten der aktuell gewählten Option zu sehen.

* **Full** – Die gründlichste Option mit der höchsten Extraktionsgenauigkeit. Am besten für komplexe Layouts, Scans schlechter Qualität oder Dokumente, bei denen Präzision am wichtigsten ist. Als leistungsstärkste Option ist sie auch die langsamste, bei **2 Token pro Dokument**.
* **Fast** – Eine ausgewogene Option, die starke Genauigkeit mit schnellerer Verarbeitung bei geringeren Kosten verbindet. Empfohlener Standard für die meisten alltäglichen Dokumente, bei **1 Token pro Dokument**.
* **Turbo** – Die schnellste und wirtschaftlichste Option. Am besten geeignet für große Mengen einfacher, sauberer, gut strukturierter Dokumente, bei denen Geschwindigkeit und niedrige Kosten wichtiger sind als maximale Genauigkeit, bei **1 Token pro Dokument**.

| Option | Am besten für | Genauigkeit | Geschwindigkeit | Token-Kosten |
|--------|---------------|-------------|-----------------|--------------|
| **Full** | Komplexe Layouts, schlechte Scans, hohe Präzision | Höchste | Langsamste | 2 / Dokument |
| **Fast** | Alltägliche Dokumente (empfohlener Standard) | Hoch | Schnell | 1 / Dokument |
| **Turbo** | Große Mengen einfacher, sauberer Dokumente | Gut | Schnellste | 1 / Dokument |

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_2.png)

## AI-Modell-Zuweisungstabelle

Sie können lieferantenspezifische **AI-Modelle** auch direkt im **Validierung**-Bildschirm konfigurieren, wodurch Sie die Extraktionsgenauigkeit für einzelne Lieferanten feinabstimmen können.\
\
Weitere Informationen finden Sie in der entsprechenden Dokumentation [hier](../../../../end-user-and-partner-section/end-user-section/validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

Die Zuweisungstabelle zeigt die AI-Modell-Einstellungen für jeden Lieferanten an und enthält die folgenden Details:

* **Supplier ID** – Die eindeutige Kennung des Lieferanten
* **AI Model** – Das derzeit dem Lieferanten zugewiesene AI-Modell
* **E-Text**: Gibt an, ob die E-Text-Funktion aktiviert ist
* **Action** – Enthält die Option zum Löschen des Eintrags

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_3.png)

### Eintrag löschen – Lieferantenspezifische Einstellungen zurücksetzen

Um die AI-Modell-Einstellung eines Lieferanten auf die Standardeinstellung zurückzusetzen:

1.  Klicken Sie auf das Mülleimer-Symbol in der **Action**-Spalte neben dem Lieferanteneintrag.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_4.png)
2.  Ein Bestätigungsdialog wird angezeigt – bestätigen Sie, dass Sie den Eintrag löschen möchten.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ai_model_5.png)

Nach dem Löschen verwendet der Lieferant wieder das Standard-**AI-Modell** für die **Feldextraktion** und **Tabelle Extraktion**.
