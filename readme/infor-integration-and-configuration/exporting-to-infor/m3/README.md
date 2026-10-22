# M3

## Schritt 1: Einen Connection Point erstellen

1. Navigieren Sie zu **OS > ION > Connect > Connection Points**
2. Klicken Sie auf **Add** und wählen Sie **IMS via API Gateway** als Connection Type.
3. Konfigurieren Sie die folgenden Einstellungen:
   * **Name**: Setzen Sie auf `DocBits_Export`.
   * **Description**: Setzen Sie auf `DocBits_Export`.
   * **Uncheck**: _Application has IMS End Point_.
   * **ION API Client ID**:
     * Öffnen Sie die ION API Datei.
     * Suchen Sie nach `"ci"` innerhalb der Datei.
     * Kopieren Sie den Wert innerhalb der Anführungszeichen (ohne die Anführungszeichen).

![Dialog Infor Application Connection Point IMS via API Gateway mit den Tabs Usage, Connection und Documents, dem Namen DocBits_Export, der nicht gesetzten Option Application has IMS End Point, dem Feld ION API Client ID und der Logical ID inforims.docbits_export](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_1.png)

4. Fügen Sie unter **Documents** `Sync.CaptureDocument` hinzu.

![Tab Connection des Anwendungspunktes mit dem Namen DocBits_Export, dem Dokument sync.captureDocument als Send from Application und der Logical ID inforims.docbits_export](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_2.png)

5. Klicken Sie auf **Save**, um die Konfiguration abzuschließen.

## Schritt 2: Mappings hochladen

{% file src="../../../.gitbook/assets/CaptureDocument_to_ProcessSupplierInvoice.xml" %}

1. Laden Sie die M3 Mapping Datei herunter.
2. Navigieren Sie zu **Infor** > **OS** > **ION** > **Connect** > **Mappings**.
3. Klicken Sie auf **Import** und wählen Sie die entsprechende Mapping Datei für **M3**.

![Seite Mappings in ION Desk mit dem Suchfeld, den Filtersteuerelementen und der Schaltfläche Add](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_3.png)

4. Sobald die Dateien importiert sind, bestätigen Sie die Mappings, um sie zu aktivieren.

![Importierte Zuordnung mit der Quelle Sync.CaptureDocument und dem Ziel Process.SupplierInvoice](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_4.png)

## Schritt 3: Den Data Flow erstellen

1. Navigieren Sie zu **OS** -> **ION** -> **Connect** -> **Data Flows**.
2. Klicken Sie auf **Add** und wählen Sie **Document Flow**.
3. Geben Sie die Details ein:
   * **Name**: `DocBits_Export_to_M3`
4. Fügen Sie Nodes zum Flow hinzu:

#### Application Node

1. Fügen Sie einen **Application Node** zum Flow hinzu.
   * **Name**: `DocBits` oder `DocBits-Export`.
2. Klicken Sie auf **Add** und wählen Sie den **Connection Point**, der in Schritt 1 erstellt wurde.

![Datenfluss in ION Desk mit der Knotenauswahl oben und dem Bereich Application Activity Properties rechts mit dem Namen DocBits-Dev-Demo-Export](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_5.png)

3. Klicken Sie auf das **Document Icon** neben dem Application Node.
   * Klicken Sie auf **Add** und wählen Sie `Sync.CaptureDocument`.

![Datenfluss in ION Desk mit ausgewähltem Anwendungsknoten und geöffnetem Bereich Documents mit dem Eintrag Sync.CaptureDocument](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_6.png)

#### Mapping Node

1. Fügen Sie einen **Mapping Node** rechts vom Application Node hinzu.
   * **Name**: `Capt2process`.
   * **Mapping**: `CaptureDocument_to_ProcessSupplierInvoice`.

![Datenfluss in ION Desk mit ausgewähltem Mapping-Knoten und dem Bereich Mapping Properties rechts mit dem Namen und der Zuordnung SyncCaptDoc_SyncSuppInv](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_7.png)

#### Application Node

1. Fügen Sie einen **Application Node** rechts vom vorherigen Mapping Node hinzu.
   * **Name**: `M3`.
2. Klicken Sie auf **Add** und wählen Sie die **M3 Application** vom Kunden.

![Datenfluss in ION Desk mit ausgewähltem M3-Anwendungsknoten und dem Bereich Application Activity Properties rechts mit dem Eintrag M3 BODs](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_8.png)

3. Klicken Sie auf das **Document Icon** neben dem Application Node.
   * Klicken Sie auf **Add** und wählen Sie `Acknowledge.SupplierInvoice`.

![Datenfluss in ION Desk mit ausgewähltem M3-Anwendungsknoten und geöffnetem Bereich Documents mit dem Eintrag Acknowledge.SupplierInvoice](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_9.png)

#### API Node

1. Fügen Sie einen **API Node** rechts vom Application Node hinzu.
   * **Name**: `DocBits-Error`.
   * **ION API Connector**: `DocBits_Import`.
   * Wenn `DocBits_Import` nicht existiert, siehe **Schritt 1** und **Schritt 2** der Import from M3 Dokumentation, um den Connection Point zu erstellen.

![Datenfluss in ION Desk mit ausgewähltem API-Knoten und dem Bereich ION API Activity Properties rechts mit dem ION API Connector DocBits Dev Demo-Import](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_10.png)

#### Flow speichern und aktivieren

* Sobald alle Nodes hinzugefügt und konfiguriert sind, klicken Sie auf **Save**.
* Aktivieren Sie den Flow, um die Einrichtung abzuschließen.

![Datenfluss in ION Desk mit den in einer Reihe verbundenen Knoten DocBits_Demo_to_M3, dem Mapping-Knoten, dem M3-Knoten und dem Fehlerknoten sowie der Schaltfläche REMOVE CONNECTION POINTS über der Zeichenfläche](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_11%20\(1\).png)

## Schritt 4: Export in DocBits konfigurieren

### On-Premise:

1. Öffnen Sie **DocBits**.
2.  Navigieren Sie zu **Einstellungen > Dokumentenverarbeitung > Export**.

    ![Einstellungsseite in DocBits mit der aufgeklappten Navigationsgruppe Document Processing und den Einträgen Documents, Expiry, Import, Rule Management, OCR Settings, Classification and Extraction, Master Data Lookup, List of Values und Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Erstellen Sie einen neuen Export:
   * **Auswählen**: **Infor IDM + ION BOD**.
   * **Titel**: Wählen Sie einen aussagekräftigen Titel.
   * **Dokumenttyp**: Setzen Sie auf **Rechnung**.
   * **Unterorganisation**: Kann leer gelassen werden oder auf eine bestimmte Unterorganisation gesetzt werden, falls erforderlich.
4. **Laden Sie die erforderlichen Dateien hoch**:
   * **ION Mapping File**: Diese finden Sie unter **Infor OS → API Gateway → Authorized Apps**. Suchen Sie nach der **DocBits** App, öffnen Sie sie und laden Sie die Credentials herunter.
   * **IDM Mapping File**: (Geben Sie den relevanten Dateipfad oder Speicherort an).
   * **BOD Mapping File**: (Geben Sie den relevanten Dateipfad oder Speicherort an).

### Cloud:

1. Öffnen Sie **DocBits**.
2.  Navigieren Sie zu **Einstellungen > Dokumentenverarbeitung > Export**.

    ![Einstellungsseite in DocBits mit der aufgeklappten Navigationsgruppe Document Processing und den Einträgen Documents, Expiry, Import, Rule Management, OCR Settings, Classification and Extraction, Master Data Lookup, List of Values und Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Erstellen Sie einen neuen Export:
   * **Auswählen**: **Infor IDM + M3 (API)**.
   * **Titel**: Wählen Sie einen aussagekräftigen Titel.
   * **Dokumenttyp**: Setzen Sie auf **Rechnung**.
   * **Unterorganisation**: Kann leer gelassen werden oder auf eine bestimmte Unterorganisation gesetzt werden, falls erforderlich.
4. **Laden Sie die erforderlichen Dateien hoch**:
   * **ION Mapping File**: Diese finden Sie unter **Infor OS → API Gateway → Authorized Apps**. Suchen Sie nach der **DocBits** App, öffnen Sie sie und laden Sie die Credentials herunter.
   * **IDM Mapping File**: (Geben Sie den relevanten Dateipfad oder Speicherort an).
   * **M3 Mapping File**: (Geben Sie den relevanten Dateipfad oder Speicherort an).

### Cloud mit toml:

1. Öffnen Sie **DocBits**.
2.  Navigieren Sie zu **Einstellungen > Dokumentenverarbeitung > Export**.

    ![Einstellungsseite in DocBits mit der aufgeklappten Navigationsgruppe Document Processing und den Einträgen Documents, Expiry, Import, Rule Management, OCR Settings, Classification and Extraction, Master Data Lookup, List of Values und Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Erstellen Sie einen neuen Export:
   * **Auswählen**: **Infor IDM + M3 (API)**.
   * **Titel**: Wählen Sie einen aussagekräftigen Titel.
   * **Dokumenttyp**: Setzen Sie auf **Rechnung**.
   * **Unterorganisation**: Kann leer gelassen werden oder auf eine bestimmte Unterorganisation gesetzt werden, falls erforderlich.
4. **Laden Sie die erforderlichen Dateien hoch**:
   * **ION Mapping File**: Diese finden Sie unter **Infor OS → API Gateway → Authorized Apps**. Suchen Sie nach der **DocBits** App, öffnen Sie sie und laden Sie die Credentials herunter.
   * **IDM Mapping File**: (Geben Sie den relevanten Dateipfad oder Speicherort an).
   * **M3 toml Mapping File**: (Geben Sie den relevanten Dateipfad oder Speicherort an).
