# Dokumenttypen

Dokumenttypen teilen DocBits mit, mit welchen Arten von Dokumenten Ihre Organisation arbeitet. Ein Administrator findet sie unter **Settings → Document Types** im Bereich **Document Processing** des Einstellungsmenüs.

Die Seite zeigt zuerst die **Default Document Types**, die DocBits bereitstellt und die Sie nicht löschen können, gefolgt von den **Custom Document Types**, die für Ihre Organisation erstellt wurden. Jeder Typ hat eine eigene Karte.

<figure><img src="../../../.gitbook/assets/document-types-overview-en-20260928.png" alt="Seite „Document Types“ mit der Karte für Rechnungen und weiteren Standard-Dokumenttypen, Schaltern für Aktivierung und Extraktion, Zahnrad für die Einstellungen und Konfigurationslinks"><figcaption><p>Wählen Sie eine Dokumenttyp-Karte aus, um diesen Typ zu konfigurieren.</p></figcaption></figure>

## Was Sie auf einer Karte tun können

| Steuerelement | Funktion |
| --- | --- |
| **Activate** | Macht diesen Dokumenttyp in Ihrer Organisation verfügbar oder nicht verfügbar. Ein blauer Schalter ist eingeschaltet, ein grauer ausgeschaltet. |
| **Extraction** | Legt den Extraktionsmodus fest: **Flex**, wenn eingeschaltet, oder **Fix**, wenn ausgeschaltet. Der Schalter schaltet die Extraktion nicht einfach ein oder aus. Bewegen Sie den Mauszeiger über den Schalter, um den aktuellen Modus anzuzeigen. |
| **Settings** (Zahnrad) | Öffnet **More Settings** für diesen Typ. Erweitern Sie dort eine Kategorie, um ihre Optionen anzuzeigen. Die Kategorien hängen vom Dokumenttyp ab. |
| **Layouts** | Öffnet die Layout-Konfiguration. Die nächsten Schritte finden Sie im [Layout Builder](layout-builder.md). |
| **Fields** | Öffnet die Feld- und Erkennungseinstellungen für diesen Typ. Wie Sie diese konfigurieren, erfahren Sie unter [Felder](../../settings/global-settings/document-types/fields/README.md). |
| **Tables** | Öffnet die Konfiguration der Tabellenspalten für diesen Typ. |
| **Scripts** | Öffnet die Verarbeitungsskripte, sofern diese Funktion verfügbar ist. |
| **Model Training** | Öffnet das Modelltraining für diesen Typ. |
| **E-Doc** | Öffnet die Einstellungen für elektronische Dokumente, sofern der Typ sie unterstützt. |
| **Document Sub Types** | Öffnet die Untertypen dieses Dokumenttyps. |

Je nach den Funktionen Ihrer Organisation sehen Sie möglicherweise weitere Links, etwa zu Validierungs- oder Transformationsregeln. Wählen Sie den Link auf der Karte des Typs, den Sie ändern möchten.

## Felder und Erkennungseinstellungen bearbeiten

Klicken Sie auf einer Karte auf **Fields**, um die Feldgruppen anzuzeigen. Oben auf dieser Seite legen **OCR** und **Match Score** die Schwellenwerte für die Erkennung fest, **Restore Defaults** setzt diese Schwellenwerte zurück und mit **Search by Name** finden Sie ein Feld. Mit **Create new group** ordnen Sie Felder in Gruppen, mit **Create field** fügen Sie innerhalb einer Gruppe ein Feld hinzu. **Master Data Settings** öffnet die zugehörige Stammdatenkonfiguration.

Jede Feldzeile enthält Steuerelemente wie **Required**, **Read Only**, **Hidden**, **Force Validation**, **Use AI**, OCR, Match Score und Formula. Lesen Sie die [Anleitung zu Feldern](../../settings/global-settings/document-types/fields/README.md), bevor Sie einzelne Werte ändern. Klicken Sie auf der Seite „Fields“ auf **Save Settings**, um Ihre Änderungen zu speichern.

<figure><img src="../../../.gitbook/assets/document-types-invoice-fields-en-20260928.png" alt="Seite „Fields“ für Rechnungen mit Erkennungseinstellungen, Feldgruppen, Steuerelementen pro Feld und Save Settings"><figcaption><p>Die Seite „Fields“ hat eine eigene Schaltfläche „Save Settings“.</p></figcaption></figure>

## Benutzerdefinierten Dokumenttyp erstellen

Scrollen Sie zu **Custom Document Types** und klicken Sie auf **+ New**. Folgen Sie der Anleitung [Dokumenttypen hinzufügen/bearbeiten](../../settings/global-settings/document-types/adding-editing-document-types.md), um den neuen Typ einzurichten.

<figure><img src="../../../.gitbook/assets/document-types-custom-new-en-20260928.png" alt="Unterer Bereich der Seite „Document Types“ mit dem Abschnitt „Custom Document Types“ und der Schaltfläche „New“"><figcaption><p>Mit „New“ unter „Custom Document Types“ beginnen Sie, einen Typ zu erstellen.</p></figcaption></figure>
