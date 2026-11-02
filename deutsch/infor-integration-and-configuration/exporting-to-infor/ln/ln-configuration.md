# LN-Konfiguration

## Voraussetzungen

Sie haben Folgendes erstellt:

* einen ION-API-Endpunkt;
* eine ION-API-Datei;
* eine BOD-Zuordnungsdatei;
* eine IDM-Zuordnungsdatei.

## Zuordnungsdateien importieren

Importieren Sie die Zuordnungsdateien in Infor OS, bevor Sie den Datenfluss einrichten.

Öffnen Sie in **ION Desk → Connect** den Bereich **Mappings**.

![ION Desk Navigation mit aufgeklappter Gruppe Connect und den Einträgen Data Flows, API Flows, Connection Points, File Templates und Enterprise Locations](https://lh7-us.googleusercontent.com/fAUUcBUSxIWqLjYEHH78O2Mfq0P4d4D42OgCNFPdpUQTM5ZHu_BcKz9DmWe0AlHe3--ff7z9mfYTrt7oAkf2uknBwkV2VWayEpiJ_aAIxcJil5LNiep4U6KZr3_tBfs1RRwXoW749q3FUxurXy_pT_k)

Klicken Sie auf das Importsymbol.

![Symbolleiste der Seite Mappings in ION Desk mit dem grünen runden Import-Symbol](https://lh7-us.googleusercontent.com/d_KYA9LgiiW1A95CH9hwU1AC1u5x25T4ET-4sAqpZkVOexHc4WcbwPXUaKt3O9fR3Btvv-NEGbCWwnnb8SfomnnO22M8YTIqWdvan-SkbG0cu1MWkjwOn_Vd_b6rJaQng8A92JTa5YKBms4RuIvwmb0)

* Wählen Sie die benötigten Zuordnungsdateien aus: SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice und LoadSupplierInvoice\_ProcessSupplierInvoice.
* Genehmigen Sie nach dem Import jede Zuordnung über das Häkchensymbol in ihrer Kachel im Zuordnungs-Dashboard.

## Von DocBits nach LN

Richten Sie anschließend den Datenfluss in ION Desk ein. Öffnen Sie die Anwendung und wählen Sie **Data Flow → + ADD → Document Flow**, wie unten gezeigt.

![Seite Data Flows in ION Desk mit der Navigation links, dem Flow DF_SLTStAPI in der Liste und den Menüeinträgen Document Flow und Data Lake Flow](https://lh7-us.googleusercontent.com/rjPVR1EFKw_gZI1Ztg9Aqt4pFw10rii7WU-yddLIz22a_Fn3s1HSYDRmQVvgZtX_85nb2ipNqJ1JU49NIE8a57TIur7jqoMuKFKlb-RrfnRFxiA1TefzofKPJ32fzIdDWI8PmnD-aDw4qhQj4e0dd9I)

Auf der folgenden Seite erstellen Sie den Informationsfluss von DocBits nach LN.

![Neuer Document Flow mit leerem Eigenschaftenbereich und den Meldungen Document flow name must be specified und The document flow has no activities](https://lh7-us.googleusercontent.com/9C7BaoiHWRaav0ytCbYkxEYG12f-64qyagsl8H2eq5TXUySRE1s3x_-lVRbK6tpTxvbRYKvwyWO_6ASSQ6Rn62LQR9ZvMRpRXq9UymZLS0I8IZ-hOzX58iYtTruqSo5WdgIXwEPjMlb1dnuFuhN8IS8)

Ein LN-Datenfluss sieht etwa wie unten gezeigt aus. Die verschiedenen Pfade dienen jeweils einem bestimmten Dokumenttyp. Diese Anleitung konzentriert sich auf den Rechnungsdatenfluss.

![Datenfluss-Arbeitsfläche mit mehreren Pfaden für verschiedene Dokumenttypen, jeder Pfad aus einem DocBits-Verbindungspunkt, einem Mapping und einem LN-Verbindungspunkt](https://lh7-us.googleusercontent.com/gltDE9JxeGb7Ufg9Ldl-JIJ95zfWHnQtyOqys2QKCiTlIn_PdAyBLFYmTVCh9c-TxF5xNQR3G8Hmn4EXK94t6MJ-1WzlZg1Zl7HNoxfR56zC8dT1skmxLTj7rtnSl0JTQJD_3myQY4Qcd9motySYh9U)

Ziehen Sie die Bestandteile der Verarbeitungskette aus dem oberen Bereich an die gewünschte Position.

In der Kette sind DocBits und LN als Anwendungen eingebunden. Die dazwischenliegenden Zuordnungen wandeln die Daten in das Format um, das der jeweils nächste Abschnitt erwartet, und ordnen die Informationen ihren Zielpositionen zu.

![Ausschnitt der Datenfluss-Arbeitsfläche mit den Knoten DocBits-DEV, MappingDeliver, Load Supplier, PurchaseOrder und den LN-Verbindungspunkten LN-200-41 und LN-200-4](https://lh7-us.googleusercontent.com/Gwk0C0gsnMSlgEwRx0_1GDMJEu8Z1TAhKo8gxHN8GxFFKGgb257a684Hj0eNSLTIK5v8F7yzJ1hIHrC_3I9RLY0S-u3ZDhmkD6iJbYAvtCAeFPWHBVLOqyCH7FKsl2SKAfXL-AdtNowqdol9PzS4qJM)

### DocBits-Anwendung

Vergeben Sie einen passenden Namen, beispielsweise „DocBits“. Klicken Sie auf das Pluszeichen, suchen Sie den zuvor erstellten Verbindungspunkt, etwa DocBits\_Export, und wählen Sie ihn aus.

Um diesen Verbindungspunkt zu erstellen, öffnen Sie **ION Desk → Connect → Connection Points**.

![ION Desk Navigation mit aufgeklappter Gruppe Connect und den Einträgen Data Flows, API Flows, Mappings und Connection Points](https://lh7-us.googleusercontent.com/1SZJN-GW7BP-fvUHZ-tCJ4xNXx0ABRP3J9eMzF3BTKIY54J-pK4bYy4fOVHCaI6A2sdrYekWJsY9ky8dXz36l_FwwzzEnO1IjxNkMqlV-Y4UvyFIei73Z9C19m9bzTr3gCL3IpTUqiV280id1vJE530)

Klicken Sie auf **+ Add**.

![Seite Connection Points in ION Desk mit geöffneter Gruppe Connect in der Navigation](https://lh7-us.googleusercontent.com/ZJ1212Gwdk-b2-LVbEd2ZDzc_AqaEEYtIN0fC6d6P4EaWdTKj6nOzGDbA5sxdBtMcTrWopfDmd7GTahbwkDpj3uvmMYgvEUQa6qmi58NFGvtcgAtIwYr952Yu7Lcj802iHtQ_vj_-XPdegP1P0ySdos)

Wählen Sie **IMS via API Gateway** und tragen Sie die folgenden Informationen ein.

![Dialog Infor Application Connection Point für IMS via API Gateway mit dem Namen DocBits-Sandbox-Export, der ION API Client Id und der Logical ID infor.ims.docbits-sandbox-export](https://lh7-us.googleusercontent.com/H4YCH-324EzrxKkrbRs0SFTsHch5eK74gXleSpfI03uJ5frIEFjwofu7p6bsYO1lS7sVqamWDZMXrGfEgewdROyhTYLkn7MuCgwb7oQxOLJoH3NsnMsqTOgT3WxlihUkJdNy-WTai5kPz8ZjdtTDQ9I)

Die ION-API-Client-ID finden Sie in der zuvor erstellten ION-API-Datei unter dem Schlüssel „ci“. Die zugehörige Anleitung beschreibt das Erstellen einer ION-API-Datei.

Öffnen Sie die Registerkarte für Dokumente und fügen Sie dem DocBits-Verbindungspunkt das BOD **Sync.CaptureDocument** hinzu, wie unten gezeigt.

![Verbindungspunkt DocBits-Sandbox-Export mit geöffnetem Tab Documents und dem zugeordneten Dokument Sync.CaptureDocument](https://lh7-us.googleusercontent.com/Wy2BIr1z_RqU-yMkXo6vOu64QC6c66OdHOxdI6PPy0yJv1jIAJF0OYITULxTFoPUK93SK3jvNm67tcxqjiEBIk0Wbu1Q1s-mSIUuPjJorcYyXY7vjsHOnoutn6tE8r6yE_333uCWuKvKiVoo99FrXVg)

Speichern Sie den Verbindungspunkt über das Diskettensymbol oben links.

Kehren Sie zum Bereich **Dataflow** in ION Desk zurück und öffnen Sie Ihren Datenfluss. Die DocBits-Anwendung sollte etwa wie unten gezeigt aussehen.

![Bereich Application Activity Properties der DocBits-Anwendung mit dem Namen DocBits-Sandbox-Export und der Beschreibung DocBits-Sandbox-Export](https://lh7-us.googleusercontent.com/cDWHmRP85YNLu7JRzq4CSezncTgP2ZOkEfZSqXK9JEq4bSwsddU7VKg8leoxaJ5zeFAbDzXrNkztmeWDIXbHwjxfUa_IpATDDwykv-OlZ2zaOVGHVqRZZpVLJ5Cq5Qla1pZk5sBV39I98lUfGao65Mw)

### Zuordnung 1

Der erste Zuordnungsknoten sollte so aussehen:

![Bereich Mapping Properties des ersten Mapping-Knotens mit den Feldern Name und Description sowie der Auswahlliste Mapping](https://lh7-us.googleusercontent.com/9tlIun_ipbTp15aMX3xN2DGlDjAZ1oI4AFWXwbP7yoFLeQNqcw_L3Z1djaqcbxP1tsp1R-nq6ZJqEzsoKe1-SmLrJNmYrJ4HJircLEwMxfmif-p2T8nqbuuxHLLLzQJ6E6tNG6MzghOpoEAt41ea2GY)

### Zuordnung 2

Der zweite Zuordnungsknoten sollte so aussehen:

![Bereich Mapping Properties des zweiten Mapping-Knotens mit den Feldern Name und Description sowie der Auswahlliste Mapping](https://lh7-us.googleusercontent.com/ZDYzTAfm3MHnEIKHa2tDl7NPbjzxv8jH-KL8O0pRhi1JYtqiiVz0-GQv5N4roVWi1STopQkFV9YHbEXdyzwYxK2Oq6mUv6tuqKDp-2bc-aPVgEXdEBd2hmW-6j6JRhEympyw9yUTrCDQRKlDQ41C5Ao)

### LN-Anwendung

In Infor sollte bereits ein Verbindungspunkt für die entsprechende LN-Gesellschaft vorhanden sein, beispielsweise mit dem Namen „LN“. Wählen Sie ihn wie bei der DocBits-Anwendung über das Pluszeichen aus. Das Ergebnis sollte so aussehen:

![Bereich Application Activity Properties der LN-Anwendung mit dem Namen LN-200 und der Beschreibung In01_0200 LN Farm](https://lh7-us.googleusercontent.com/mRXL11f68EtQHHjl40QmCisy7S1aUezqCzufPTZWgYHhWLK2Yw0UY82O_dgbAhBChFHHYUMBDSWWb-PEKyohJWOp5gvufat431ezpA2cIHMtry7XEDxhnNzPB68uSMkFAXhX1x4GyiH6Cxp-USxDnHE)

### BODs

![Datenfluss-Arbeitsfläche mit den Knoten DocBits-DEV, MappingDeliver, Load Supplier, PurchaseOrder, SalesOrder und AdvancedShip über dem Eintrag End](https://lh7-us.googleusercontent.com/de8OyDF4yMoHaXsxM9weJdm8mKDzL97kFRr00fhoHAxxKXb2BgMcMM2shyxi1S7cBwzSAUy2u8bZV4sJOVqgXt8Mcge6L2CXxbfVGiqXUwKwF6A5mgt4zfGPYltaZuLazOJYu2u7arszJE6IonMOskk)

Die folgenden Konfigurationen sollten so aussehen:

#### Erste Konfiguration

![Auswahlliste Documents des ersten Knotens mit dem Eintrag Sync.CaptureDocument](https://lh7-us.googleusercontent.com/rj_qpiML1a2dNxj6ItiRxescymVtD6LHIAum3UPrPERAavhkt81lpjcyAFmn_lmxtqUDVTm_kiZ9f02Lqh9w-SAWmcxvGuxWITVvhv9qg04HaJXGH7VfRiO4Iv1LtDxfKYFyUWPLzCE4L3yP4hcdGnY)

#### Zweite Konfiguration

![Auswahlliste Documents des zweiten Knotens mit dem Eintrag Load.SupplierInvoice](https://lh7-us.googleusercontent.com/TCxMS-RhoJcUyBko36Lfpa8D71qk-ZSN-lME7Oq8cfPACVV0Ci7Lnv6y_MF_53U763ZA74xq6icEfgDUwYYJ9UJK0kCiLHQZpJYmc_ywjB32UGrpDnh7AjoHpI5AtWd3yZR3RsMaki1AYenpdG4X9X8)

#### Dritte Konfiguration

![Auswahlliste Documents des dritten Knotens mit dem Eintrag Process.SupplierInvoice](https://lh7-us.googleusercontent.com/VPYJyfpO0RZueW46s2Y8W2H-tQFlMfIdP1Sf8qMB8BfTxefgQ5dhsaAxL36R7cdvmKR26Q_epAj9_i6CzUO6C-PHjStEynBDkjtwId4BSuH6-zJklmsr25XcNH2AY7pSwOQ_rbCCixhWcaJg2kHyyYw)

Das letzte Symbol sollte leer sein, da es weder ein Dokument noch Informationen überträgt.

Wenn alle erforderlichen Knoten hinzugefügt wurden, aktivieren Sie den Datenfluss über die folgende Schaltfläche:

![Symbolleiste des Document Flow mit den Schaltflächen zum Hinzufügen und Entfernen von Verbindungspunkten und der Schaltfläche zum Aktivieren des Datenflusses unter dem Namen DocBits-Export-M3](https://lh7-us.googleusercontent.com/WjQeGz_effl_RlkWC4CdJS9Dg_9DpsIz3meKOsa7GbU9RFSrYMw3PpbXFat6cGsA4gvEGS-0D-YFrZj9K2wK3Irap-30mcQ5kr5k4Gy2gm7DLJdYpzJgeBRVInyAYfGmGXu2dCQvmX9ballRbSwyq3o)
