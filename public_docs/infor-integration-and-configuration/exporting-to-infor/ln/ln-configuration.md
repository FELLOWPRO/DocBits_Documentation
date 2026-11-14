# LN-Konfiguration

Diese Anleitung verbindet historische Beispiele aus Infor ION mit dem aktuellen LN-Exportformular von DocBits. Die Infor-Bilder veranschaulichen die einzelnen Schritte; Mandanten-, Zuordnungs- und Aufbauangaben darin sind Beispiele. Lassen Sie Verbindungspunkte, Zuordnungspaket und BOD-Berechtigungen von Ihrer Infor-Administration für Ihre LN-Gesellschaft prüfen, bevor Sie einen Datenfluss aktivieren. Für diese Aktualisierung der Dokumentation wurden weder eine Infor-Mandantenverbindung noch ein Rechnungsexport getestet.

## Voraussetzungen

Sie haben Folgendes erstellt:

* einen ION-API-Endpunkt;
* eine ION-API-Datei;
* eine BOD-Zuordnungsdatei;
* eine IDM-Zuordnungsdatei.

## Zuordnungsdateien importieren

Importieren Sie die Zuordnungsdateien in Infor OS, bevor Sie den Datenfluss einrichten.

Öffnen Sie in **ION Desk → Connect** den Bereich **Mappings**.

<figure><img src="https://lh7-us.googleusercontent.com/fAUUcBUSxIWqLjYEHH78O2Mfq0P4d4D42OgCNFPdpUQTM5ZHu_BcKz9DmWe0AlHe3--ff7z9mfYTrt7oAkf2uknBwkV2VWayEpiJ_aAIxcJil5LNiep4U6KZr3_tBfs1RRwXoW749q3FUxurXy_pT_k" alt="Historisches Beispiel: Navigation in ION Desk mit aufgeklappter Gruppe Connect und den Einträgen Data Flows, API Flows, Connection Points, File Templates und Enterprise Locations."><figcaption><p>Historisches Beispiel: Navigation in ION Desk mit aufgeklappter Gruppe Connect und den Einträgen Data Flows, API Flows, Connection Points, File Templates und Enterprise Locations. Prüfen Sie die entsprechenden Einstellungen in Ihrem Infor-Mandanten.</p></figcaption></figure>

Klicken Sie auf das Importsymbol.

<figure><img src="https://lh7-us.googleusercontent.com/d_KYA9LgiiW1A95CH9hwU1AC1u5x25T4ET-4sAqpZkVOexHc4WcbwPXUaKt3O9fR3Btvv-NEGbCWwnnb8SfomnnO22M8YTIqWdvan-SkbG0cu1MWkjwOn_Vd_b6rJaQng8A92JTa5YKBms4RuIvwmb0" alt="Historisches Beispiel: Symbolleiste der Seite Mappings in ION Desk mit dem markierten Import-Symbol."><figcaption><p>Historisches Beispiel: Symbolleiste der Seite Mappings in ION Desk mit dem markierten Import-Symbol. Prüfen Sie die entsprechenden Einstellungen in Ihrem Infor-Mandanten.</p></figcaption></figure>

* Wählen Sie die benötigten Zuordnungsdateien aus: SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice und LoadSupplierInvoice\_ProcessSupplierInvoice.
* Genehmigen Sie nach dem Import jede Zuordnung über das Häkchensymbol in ihrer Kachel im Zuordnungs-Dashboard.

## Von DocBits nach LN

Richten Sie anschließend den Datenfluss in ION Desk ein. Öffnen Sie die Anwendung und wählen Sie **Data Flow → + ADD → Document Flow**, wie unten gezeigt.

<figure><img src="https://lh7-us.googleusercontent.com/rjPVR1EFKw_gZI1Ztg9Aqt4pFw10rii7WU-yddLIz22a_Fn3s1HSYDRmQVvgZtX_85nb2ipNqJ1JU49NIE8a57TIur7jqoMuKFKlb-RrfnRFxiA1TefzofKPJ32fzIdDWI8PmnD-aDw4qhQj4e0dd9I" alt="Historisches Beispiel: Seite Data Flows in ION Desk mit der Navigation links, dem Fluss DF_SLTStAPI in der Liste und den Menüeinträgen Document Flow und Data Lake Flow."><figcaption><p>Historisches Beispiel: Seite Data Flows in ION Desk mit der Navigation links, dem Fluss DF_SLTStAPI in der Liste und den Menüeinträgen Document Flow und Data Lake Flow. Prüfen Sie die entsprechenden Einstellungen in Ihrem Infor-Mandanten.</p></figcaption></figure>

Auf der folgenden Seite erstellen Sie den Informationsfluss von DocBits nach LN.

<figure><img src="https://lh7-us.googleusercontent.com/9C7BaoiHWRaav0ytCbYkxEYG12f-64qyagsl8H2eq5TXUySRE1s3x_-lVRbK6tpTxvbRYKvwyWO_6ASSQ6Rn62LQR9ZvMRpRXq9UymZLS0I8IZ-hOzX58iYtTruqSo5WdgIXwEPjMlb1dnuFuhN8IS8" alt="Historisches Beispiel: Neuer Document Flow mit leerem Eigenschaftenbereich und den Meldungen Document flow name must be specified und The document flow has no activities."><figcaption><p>Historisches Beispiel: Neuer Document Flow mit leerem Eigenschaftenbereich und den Meldungen Document flow name must be specified und The document flow has no activities. Prüfen Sie die entsprechenden Einstellungen in Ihrem Infor-Mandanten.</p></figcaption></figure>

Ein LN-Datenfluss sieht etwa wie unten gezeigt aus. Die verschiedenen Pfade dienen jeweils einem bestimmten Dokumenttyp. Diese Anleitung konzentriert sich auf den Rechnungsdatenfluss.

<figure><img src="https://lh7-us.googleusercontent.com/gltDE9JxeGb7Ufg9Ldl-JIJ95zfWHnQtyOqys2QKCiTlIn_PdAyBLFYmTVCh9c-TxF5xNQR3G8Hmn4EXK94t6MJ-1WzlZg1Zl7HNoxfR56zC8dT1skmxLTj7rtnSl0JTQJD_3myQY4Qcd9motySYh9U" alt="Historisches Beispiel: Datenfluss-Arbeitsfläche mit mehreren Pfaden für verschiedene Dokumenttypen, jeder Pfad aus einem DocBits-Verbindungspunkt, einer Zuordnung und einem LN-Verbindungspunkt."><figcaption><p>Historisches Beispiel: Datenfluss-Arbeitsfläche mit mehreren Pfaden für verschiedene Dokumenttypen, jeder Pfad aus einem DocBits-Verbindungspunkt, einer Zuordnung und einem LN-Verbindungspunkt. Prüfen Sie die entsprechenden Einstellungen in Ihrem Infor-Mandanten.</p></figcaption></figure>

Ziehen Sie die Bestandteile der Verarbeitungskette aus dem oberen Bereich an die gewünschte Position.

In der Kette sind DocBits und LN als Anwendungen eingebunden. Die dazwischenliegenden Zuordnungen wandeln die Daten in das Format um, das der jeweils nächste Abschnitt erwartet, und ordnen die Informationen ihren Zielpositionen zu.

<figure><img src="https://lh7-us.googleusercontent.com/Gwk0C0gsnMSlgEwRx0_1GDMJEu8Z1TAhKo8gxHN8GxFFKGgb257a684Hj0eNSLTIK5v8F7yzJ1hIHrC_3I9RLY0S-u3ZDhmkD6iJbYAvtCAeFPWHBVLOqyCH7FKsl2SKAfXL-AdtNowqdol9PzS4qJM" alt="Historisches Beispiel: Aktivitätenpalette und Ablauf in ION, in denen Anwendungsaktivitäten DocBits und LN darstellen und Zuordnungsaktivitäten dazwischenliegen."><figcaption><p>Historisches Beispiel: Aktivitätenpalette und Ablauf in ION, in denen Anwendungsaktivitäten DocBits und LN darstellen und Zuordnungsaktivitäten dazwischenliegen. Prüfen Sie die entsprechenden Einstellungen in Ihrem Infor-Mandanten.</p></figcaption></figure>

### DocBits-Anwendung

Vergeben Sie einen passenden Namen, beispielsweise „DocBits“. Klicken Sie auf das Pluszeichen, suchen Sie den zuvor erstellten Verbindungspunkt, etwa DocBits\_Export, und wählen Sie ihn aus.

Um diesen Verbindungspunkt zu erstellen, öffnen Sie **ION Desk → Connect → Connection Points**.

<figure><img src="https://lh7-us.googleusercontent.com/1SZJN-GW7BP-fvUHZ-tCJ4xNXx0ABRP3J9eMzF3BTKIY54J-pK4bYy4fOVHCaI6A2sdrYekWJsY9ky8dXz36l_FwwzzEnO1IjxNkMqlV-Y4UvyFIei73Z9C19m9bzTr3gCL3IpTUqiV280id1vJE530" alt="Historisches Beispiel: Navigation in ION Desk mit aufgeklappter Gruppe Connect und den Einträgen Data Flows, API Flows, Mappings und Connection Points."><figcaption><p>Historisches Beispiel: Navigation in ION Desk mit aufgeklappter Gruppe Connect und den Einträgen Data Flows, API Flows, Mappings und Connection Points. Prüfen Sie die entsprechenden Einstellungen in Ihrem Infor-Mandanten.</p></figcaption></figure>

Klicken Sie auf **+ Add**.

<figure><img src="https://lh7-us.googleusercontent.com/ZJ1212Gwdk-b2-LVbEd2ZDzc_AqaEEYtIN0fC6d6P4EaWdTKj6nOzGDbA5sxdBtMcTrWopfDmd7GTahbwkDpj3uvmMYgvEUQa6qmi58NFGvtcgAtIwYr952Yu7Lcj802iHtQ_vj_-XPdegP1P0ySdos" alt="Historisches Beispiel: Seite Connection Points in ION Desk mit geöffneter Gruppe Connect in der Navigation."><figcaption><p>Historisches Beispiel: Seite Connection Points in ION Desk mit geöffneter Gruppe Connect in der Navigation. Prüfen Sie die entsprechenden Einstellungen in Ihrem Infor-Mandanten.</p></figcaption></figure>

Wählen Sie **IMS via API Gateway** und tragen Sie die folgenden Informationen ein.

<figure><img src="https://lh7-us.googleusercontent.com/H4YCH-324EzrxKkrbRs0SFTsHch5eK74gXleSpfI03uJ5frIEFjwofu7p6bsYO1lS7sVqamWDZMXrGfEgewdROyhTYLkn7MuCgwb7oQxOLJoH3NsnMsqTOgT3WxlihUkJdNy-WTai5kPz8ZjdtTDQ9I" alt="Historisches Beispiel: Verbindungspunkt IMS via API Gateway mit einer beispielhaften Logical ID und einem unkenntlich gemachten Feld ION API Client Id."><figcaption><p>Historisches Beispiel: Verbindungspunkt IMS via API Gateway mit einer beispielhaften Logical ID und einem unkenntlich gemachten Feld ION API Client Id. Prüfen Sie die entsprechenden Einstellungen in Ihrem Infor-Mandanten.</p></figcaption></figure>

Die ION-API-Client-ID ist der Wert `ci` in Ihrer `.ionapi`-Datei. Fordern Sie die mandantenspezifische Datei bei der zuständigen Infor-Administration an. Sie enthält Zugangsdaten; halten Sie sie aus Screenshots, Tickets und Git heraus. Siehe die [Erläuterung der ION-API-Zugangsfelder von Infor](https://docs.infor.com/crm/9.4.x/en-us/webclient/upi1639111995644.html).

Öffnen Sie die Registerkarte für Dokumente und fügen Sie dem DocBits-Verbindungspunkt das BOD **Sync.CaptureDocument** hinzu, wie unten gezeigt.

<figure><img src="https://lh7-us.googleusercontent.com/Wy2BIr1z_RqU-yMkXo6vOu64QC6c66OdHOxdI6PPy0yJv1jIAJF0OYITULxTFoPUK93SK3jvNm67tcxqjiEBIk0Wbu1Q1s-mSIUuPjJorcYyXY7vjsHOnoutn6tE8r6yE_333uCWuKvKiVoo99FrXVg" alt="Historisches Beispiel: Verbindungspunkt DocBits-Sandbox-Export mit geöffnetem Tab Documents und dem zugeordneten Dokument Sync.CaptureDocument."><figcaption><p>Historisches Beispiel: Verbindungspunkt DocBits-Sandbox-Export mit geöffnetem Tab Documents und dem zugeordneten Dokument Sync.CaptureDocument. Prüfen Sie die entsprechenden Einstellungen in Ihrem Infor-Mandanten.</p></figcaption></figure>

Speichern Sie den Verbindungspunkt über das Diskettensymbol oben links.

Kehren Sie zum Bereich **Dataflow** in ION Desk zurück und öffnen Sie Ihren Datenfluss. Die DocBits-Anwendung sollte etwa wie unten gezeigt aussehen.

<figure><img src="https://lh7-us.googleusercontent.com/cDWHmRP85YNLu7JRzq4CSezncTgP2ZOkEfZSqXK9JEq4bSwsddU7VKg8leoxaJ5zeFAbDzXrNkztmeWDIXbHwjxfUa_IpATDDwykv-OlZ2zaOVGHVqRZZpVLJ5Cq5Qla1pZk5sBV39I98lUfGao65Mw" alt="Historisches Beispiel: Application Activity Properties mit dem Anwendungsnamen DocBits-Sandbox und dem gewählten Verbindungspunkt DocBits-Sandbox-Export."><figcaption><p>Historisches Beispiel: Application Activity Properties mit dem Anwendungsnamen DocBits-Sandbox und dem gewählten Verbindungspunkt DocBits-Sandbox-Export. Prüfen Sie die entsprechenden Einstellungen in Ihrem Infor-Mandanten.</p></figcaption></figure>

### Zuordnung 1

Der erste Zuordnungsknoten sollte so aussehen:

<figure><img src="https://lh7-us.googleusercontent.com/9tlIun_ipbTp15aMX3xN2DGlDjAZ1oI4AFWXwbP7yoFLeQNqcw_L3Z1djaqcbxP1tsp1R-nq6ZJqEzsoKe1-SmLrJNmYrJ4HJircLEwMxfmif-p2T8nqbuuxHLLLzQJ6E6tNG6MzghOpoEAt41ea2GY" alt="Historisches Beispiel: Eigenschaften der ersten Zuordnung, Capture2sync, mit der Beispielzuordnung LN_CaptureDocumentToSupplierInvoice_1."><figcaption><p>Historisches Beispiel: Eigenschaften der ersten Zuordnung, Capture2sync, mit der Beispielzuordnung LN_CaptureDocumentToSupplierInvoice_1. Prüfen Sie die entsprechenden Einstellungen in Ihrem Infor-Mandanten.</p></figcaption></figure>

### Zuordnung 2

Der zweite Zuordnungsknoten sollte so aussehen:

<figure><img src="https://lh7-us.googleusercontent.com/ZDYzTAfm3MHnEIKHa2tDl7NPbjzxv8jH-KL8O0pRhi1JYtqiiVz0-GQv5N4roVWi1STopQkFV9YHbEXdyzwYxK2Oq6mUv6tuqKDp-2bc-aPVgEXdEBd2hmW-6j6JRhEympyw9yUTrCDQRKlDQ41C5Ao" alt="Historisches Beispiel: Eigenschaften der zweiten Zuordnung, Load2Process, mit der Beispielzuordnung LoadSupplierToProcessSupplierInvoice."><figcaption><p>Historisches Beispiel: Eigenschaften der zweiten Zuordnung, Load2Process, mit der Beispielzuordnung LoadSupplierToProcessSupplierInvoice. Prüfen Sie die entsprechenden Einstellungen in Ihrem Infor-Mandanten.</p></figcaption></figure>

### LN-Anwendung

In Infor sollte bereits ein Verbindungspunkt für die entsprechende LN-Gesellschaft vorhanden sein, beispielsweise mit dem Namen „LN“. Wählen Sie ihn wie bei der DocBits-Anwendung über das Pluszeichen aus. Das Ergebnis sollte so aussehen:

<figure><img src="https://lh7-us.googleusercontent.com/mRXL11f68EtQHHjl40QmCisy7S1aUezqCzufPTZWgYHhWLK2Yw0UY82O_dgbAhBChFHHYUMBDSWWb-PEKyohJWOp5gvufat431ezpA2cIHMtry7XEDxhnNzPB68uSMkFAXhX1x4GyiH6Cxp-USxDnHE" alt="Historisches Beispiel: LN Application Activity Properties mit dem Beispielnamen LN-200 und der gewählten Anwendungsverbindung In01_0200."><figcaption><p>Historisches Beispiel: LN Application Activity Properties mit dem Beispielnamen LN-200 und der gewählten Anwendungsverbindung In01_0200. Prüfen Sie die entsprechenden Einstellungen in Ihrem Infor-Mandanten.</p></figcaption></figure>

### BODs

<figure><img src="https://lh7-us.googleusercontent.com/de8OyDF4yMoHaXsxM9weJdm8mKDzL97kFRr00fhoHAxxKXb2BgMcMM2shyxi1S7cBwzSAUy2u8bZV4sJOVqgXt8Mcge6L2CXxbfVGiqXUwKwF6A5mgt4zfGPYltaZuLazOJYu2u7arszJE6IonMOskk" alt="Historisches Beispiel: Datenfluss-Arbeitsfläche mit den Knoten DocBits-DEV, MappingDeliver, Load Supplier, PurchaseOrder, SalesOrder und AdvancedShip über dem Eintrag End."><figcaption><p>Historisches Beispiel: Datenfluss-Arbeitsfläche mit den Knoten DocBits-DEV, MappingDeliver, Load Supplier, PurchaseOrder, SalesOrder und AdvancedShip über dem Eintrag End. Prüfen Sie die entsprechenden Einstellungen in Ihrem Infor-Mandanten.</p></figcaption></figure>

Die folgenden Konfigurationen sollten so aussehen:

#### Erste Konfiguration

<figure><img src="https://lh7-us.googleusercontent.com/rj_qpiML1a2dNxj6ItiRxescymVtD6LHIAum3UPrPERAavhkt81lpjcyAFmn_lmxtqUDVTm_kiZ9f02Lqh9w-SAWmcxvGuxWITVvhv9qg04HaJXGH7VfRiO4Iv1LtDxfKYFyUWPLzCE4L3yP4hcdGnY" alt="Historisches Beispiel: Dokumentliste des ersten Schritts mit Sync.CaptureDocument."><figcaption><p>Historisches Beispiel: Dokumentliste des ersten Schritts mit Sync.CaptureDocument. Prüfen Sie die entsprechenden Einstellungen in Ihrem Infor-Mandanten.</p></figcaption></figure>

#### Zweite Konfiguration

<figure><img src="https://lh7-us.googleusercontent.com/TCxMS-RhoJcUyBko36Lfpa8D71qk-ZSN-lME7Oq8cfPACVV0Ci7Lnv6y_MF_53U763ZA74xq6icEfgDUwYYJ9UJK0kCiLHQZpJYmc_ywjB32UGrpDnh7AjoHpI5AtWd3yZR3RsMaki1AYenpdG4X9X8" alt="Historisches Beispiel: Dokumentliste des zweiten Schritts mit Load.SupplierInvoice."><figcaption><p>Historisches Beispiel: Dokumentliste des zweiten Schritts mit Load.SupplierInvoice. Prüfen Sie die entsprechenden Einstellungen in Ihrem Infor-Mandanten.</p></figcaption></figure>

#### Dritte Konfiguration

<figure><img src="https://lh7-us.googleusercontent.com/VPYJyfpO0RZueW46s2Y8W2H-tQFlMfIdP1Sf8qMB8BfTxefgQ5dhsaAxL36R7cdvmKR26Q_epAj9_i6CzUO6C-PHjStEynBDkjtwId4BSuH6-zJklmsr25XcNH2AY7pSwOQ_rbCCixhWcaJg2kHyyYw" alt="Historisches Beispiel: Dokumentliste des dritten Schritts mit Process.SupplierInvoice."><figcaption><p>Historisches Beispiel: Dokumentliste des dritten Schritts mit Process.SupplierInvoice. Prüfen Sie die entsprechenden Einstellungen in Ihrem Infor-Mandanten.</p></figcaption></figure>

Das letzte Symbol sollte leer sein, da es weder ein Dokument noch Informationen überträgt.

Nachdem Ihre Infor-Administration alle Knoten, Zuordnungen und Dokumentabonnements geprüft hat, aktivieren Sie den vorgesehenen Datenfluss über das Bedienelement zum Aktivieren. Das historische Bild unten kennzeichnet dieses Bedienelement; sein alter Flussname enthält M3 und darf nicht als Name oder Ziel Ihrer LN-Einrichtung verwendet werden.

<figure><img src="https://lh7-us.googleusercontent.com/WjQeGz_effl_RlkWC4CdJS9Dg_9DpsIz3meKOsa7GbU9RFSrYMw3PpbXFat6cGsA4gvEGS-0D-YFrZj9K2wK3Irap-30mcQ5kr5k4Gy2gm7DLJdYpzJgeBRVInyAYfGmGXu2dCQvmX9ballRbSwyq3o" alt="Historisches Beispiel: Symbolleiste des Document Flow mit dem markierten Bedienelement zum Aktivieren. Der alte Beispielname lautet DocBits-Export-M3; wählen Sie in Ihrem Mandanten den richtigen LN-Datenfluss."><figcaption><p>Historisches Beispiel: Symbolleiste des Document Flow mit dem markierten Bedienelement zum Aktivieren. Der alte Beispielname lautet DocBits-Export-M3; wählen Sie in Ihrem Mandanten den richtigen LN-Datenfluss. Prüfen Sie die entsprechenden Einstellungen in Ihrem Infor-Mandanten.</p></figcaption></figure>

## Export in DocBits konfigurieren

Öffnen Sie in der vorgesehenen DocBits-Organisation **Einstellungen → Export**. Die Seite **Exportieren** listet die vorhandenen Exportkonfigurationen; die Spalten heißen Typ, Unter-Organisationen, Titel und Methode Exportieren. Wählen Sie **Neu**, um eine neue Konfiguration vorzubereiten.

<figure><img src="../../../.gitbook/assets/ln-configuration-export-list-de-20261112.png" alt="Aktuelle deutsche Exportliste in DocBits mit dem Knopf Neu, den Spalten Typ, Unter-Organisationen, Titel, Methode Exportieren und Aktionen und der Meldung, dass keine Konfigurationen gefunden wurden."><figcaption><p>Die Liste enthält in diesem erfundenen Beispielmandanten keine Exportkonfiguration und zeigt die Meldung, dass noch keine angelegt wurde. Neu öffnet das Konfigurationsformular; eine gespeicherte Konfiguration wurde nicht geöffnet oder geändert.</p></figcaption></figure>

Tragen Sie unter **Grundinformationen** einen **Konfigurationstitel** ein, wählen Sie den **Dokumenttyp** (für die Rechnungsübertragung Rechnung) und nur dann eine **Unterorganisation**, wenn Ihre Einrichtung eine benötigt. Wählen Sie bei **Export** den Wert **Infor** und bei **Infotyp** den Wert **Infor IDM + LN**; die deutsche Oberfläche beschriftet dieses Feld mit „Infotyp“, gemeint ist der Infor-Typ.

Stellen Sie alle drei für eine neue LN-Konfiguration erforderlichen Dateien bereit: die **ION API-Datei** (.ionapi), die **IDM-Mapping-Datei** (.properties) und die **LN-Mapping-Datei** (.properties). Klicken Sie dazu auf **Zum Hochladen klicken** oder ziehen Sie die Datei in das Feld. Fordern Sie die Dateien für diesen Mandanten und diese LN-Gesellschaft bei der zuständigen Infor-Administration an. Das Bild lässt alle Upload-Felder bewusst leer und enthält keine Zugangsdaten.

<figure><img src="../../../.gitbook/assets/ln-configuration-export-ln-de-20261112.png" alt="Aktuelles deutsches Formular in DocBits mit den Bereichen Grundinformationen und Exportkonfiguration, dem Infotyp Infor IDM + LN, einem noch nicht gewählten Dokumenttyp und drei leeren Upload-Feldern für ION API-Datei, IDM-Mapping-Datei und LN-Mapping-Datei."><figcaption><p>Das aktuelle LN-Formular trennt die drei Upload-Felder. Unter Grundinformationen werden Zieltyp und Dokumenttyp festgelegt; in diesem Beispiel wurden keine Dateien hochgeladen und keine Konfiguration gespeichert.</p></figcaption></figure>

Nachdem Ihre Administration den ION-Datenfluss und die Dateien bestätigt hat, speichern Sie die Konfiguration über **Speichern** und testen Sie eine freigegebene Rechnung außerhalb des Produktivbetriebs. Prüfen Sie das Ergebnis in DocBits, in Infor ION und in LN. Eine gespeicherte Konfiguration allein belegt nicht, dass LN eine Rechnung erhalten hat. Brechen Sie das Formular mit **Abbrechen** ab, wenn Sie nur die verfügbaren Felder ansehen möchten.

Zu den Aufgaben von Verbindungspunkten und Dokumentflüssen siehe die [Erläuterung von Infor ION](https://docs.infor.com/ln/10.8/en-us/lnesolvh/lnoshybridng/wxa1699288671147.html).
