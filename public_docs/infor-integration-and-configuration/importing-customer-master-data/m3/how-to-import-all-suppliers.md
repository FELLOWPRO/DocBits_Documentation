# Lieferanten-Initiallast aus Infor M3 starten

Verwenden Sie dieses Verfahren erst, nachdem Ihr Infor-Administrator Firma, Division, den BOD `SupplierPartyMaster` und die DocBits-ION-Route bestätigt hat. Eine uneingeschränkte Initiallast kann jeden geeigneten Lieferanten senden; vereinbaren Sie deshalb zuerst eine kleine Auswahl. Die elf Infor-M3-Screenshots unten sind historische Beispiele; vergleichen Sie sie vor dem Start eines Jobs mit Ihrem Mandanten. Bei dieser Aktualisierung der Seite wurde kein M3-Job ausgeführt und es wurden keine Lieferanten in DocBits importiert.

Infor beschreibt das [EVS006-Verfahren für die Initiallast](https://docs.infor.com/m3core/latest/en-us/useradminlib_cloud/m3cecoreag_cloud/hmo1553266924239.html) und die [EVS007-Auswahl- und Ausführungsoptionen](https://docs.infor.com/m3udi/16.x/en-us/m3beud/appfoundhs/spl1567531742751.html). Wenn Bezeichnungen abweichen, folgen Sie dem freigegebenen Verfahren Ihres Mandanten.

* [ ] Öffnen Sie Infor OS und die M3-Anwendung mit einem für Initiallasten berechtigten Konto. Bestätigen Sie die vorgesehene Firma und Division, bevor Sie fortfahren.

<figure><img src="../../../.gitbook/assets/6cf93500-2e90-4cfc-a9fb-5873e5dcb953.png" alt="Historischer Infor-M3-Startbildschirm mit Modulmenü auf der linken Seite und der Liste Recent mit EVS006 Initial Load und BOD Processor Administration"><figcaption><p>Historischer Infor-M3-Startbildschirm mit EVS006 Initial Load und BOD Processor Administration in der Liste Recent.</p></figcaption></figure>

* [ ] Öffnen Sie **Initial Load. Open (EVS006)** über die Programmsuche Ihres Mandanten.

<figure><img src="../../../.gitbook/assets/f77b242e-eb2f-43b6-8a2e-03d264198e0c.png" alt="Historischer Infor-M3-Dialog Search and Start mit leerem Eingabefeld und der Schaltfläche OK"><figcaption><p>Historischer Infor-M3-Dialog Search and Start mit Eingabefeld und Schaltfläche OK.</p></figcaption></figure>

* [ ] Erstellen Sie in EVS006 eine Definition für die Initiallast von **SupplierPartyMaster**. Das historische Beispiel verwendet **CIDMAS** als Tabelle. Lassen Sie vom M3-Administrator bestätigen, dass diese Kombination aus BOD und Tabelle in Ihrer Version und Integration gültig ist.

<figure><img src="../../../.gitbook/assets/827a9dbb-c974-4da7-9bd3-f8e87adad60f.png" alt="Historischer Dialog Search and Start mit dem eingegebenen Text evs006 im Eingabefeld"><figcaption><p>Historisches Beispiel für Search and Start mit EVS006 im Eingabefeld.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/e30c7b86-dcfb-41d2-bd32-447b60e4581b.png" alt="Historische EVS006-Initiallastliste mit SupplierPartyMaster als BOD noun und CIDMAS als Tabelle"><figcaption><p>Historische EVS006-Initiallastliste mit SupplierPartyMaster als BOD noun und CIDMAS als Tabelle.</p></figcaption></figure>

* [ ] Wählen Sie **Create** und prüfen Sie die Definition, bevor Sie fortfahren.

<figure><img src="../../../.gitbook/assets/30eee6b2-24ed-4e1f-8812-1304e7dede8e.png" alt="Historische EVS006-Liste mit der rot hervorgehobenen Schaltfläche Create (Plus) in der Symbolleiste"><figcaption><p>Historische EVS006-Liste mit hervorgehobener Schaltfläche Create.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/461b72d3-d576-4c92-95c2-d175183088af.png" alt="Historischer EVS006-Erstellungsbereich für die Tabelle CIDMAS mit noch leerem Feld BOD Description"><figcaption><p>Historischer EVS006-Erstellungsbereich für CIDMAS mit noch leerem Feld BOD Description.</p></figcaption></figure>

* [ ] Geben Sie eine eindeutige **BOD Description** ein, zum Beispiel **SupplierPartyMaster initial load for DocBits**.

<figure><img src="../../../.gitbook/assets/4dc345a8-8eca-4e03-800a-37a670f8792e.png" alt="Historischer EVS006-Erstellungsbereich mit SupplierPartyMaster im Feld BOD Description"><figcaption><p>Historischer EVS006-Erstellungsbereich mit SupplierPartyMaster als BOD Description.</p></figcaption></figure>

* [ ] Wählen Sie **Next** und legen Sie, soweit verfügbar, eine abgestimmte Auswahl fest. Infor empfiehlt Auswahlkriterien, damit nicht zu viele Ereignisse ausgelöst werden.

<figure><img src="../../../.gitbook/assets/315aa54b-f0bd-4057-a1ed-e476c9000725.png" alt="Historischer EVS006-Erstellungsbereich mit der hervorgehobenen Schaltfläche Next unten rechts"><figcaption><p>Historischer EVS006-Erstellungsbereich mit hervorgehobener Schaltfläche Next.</p></figcaption></figure>

* [ ] Fahren Sie mit den Einstellungen für die Ausführung fort. Prüfen Sie Firma, Division und Auswahl erneut.

<figure><img src="../../../.gitbook/assets/c0ff3fe1-a393-43cc-96a5-3e0cb1d878b7.png" alt="Historischer Textdialog in EVS006 mit leeren Textblockfeldern und der Schaltfläche Next"><figcaption><p>Historischer EVS006-Textdialog mit Textblockfeldern und einer Schaltfläche Next.</p></figcaption></figure>

* [ ] Wählen Sie in der Definition SupplierPartyMaster **Related → Run**. Damit öffnet sich **Initial Load Job. Open (EVS007)**; das allein belegt noch nicht, dass DocBits die Daten erhalten hat.

<figure><img src="../../../.gitbook/assets/d819fdd5-5b4a-48ef-9412-f211c0d2355f.png" alt="Historische EVS006-Liste mit geöffnetem Kontextmenü auf der Zeile SupplierPartyMaster und dem Eintrag Related &gt; Run"><figcaption><p>Historische EVS006-Liste mit geöffnetem Menü Related → Run auf der Zeile SupplierPartyMaster.</p></figcaption></figure>

* [ ] Wählen Sie **Sync** nur, wenn der empfangende ION-Flow Sync.SupplierPartyMaster erwartet. Bestätigen Sie Filter und Ziel, bevor Sie EVS007 absenden. Eine vollständige Initiallast kann viele Ereignisse erzeugen.

<figure><img src="../../../.gitbook/assets/m3-supplier-initial-load-job-historical-id-masked-20261102.png" alt="Historischer EVS007 Initial Load Job für CIDMAS und SupplierPartyMaster mit BOD-Verb Sync und Status 1-Pending; die Job-Kennung ist maskiert"><figcaption><p>Historischer EVS007 Initial Load Job mit CIDMAS, SupplierPartyMaster, Sync und Status 1-Pending. Die Job-Kennung ist maskiert; der Status Pending belegt keinen abgeschlossenen Import.</p></figcaption></figure>

## Ergebnis prüfen

Prüfen Sie nach einer freigegebenen Ausführung in EVS006 unter **Related → History** die verarbeitete Anzahl und eventuelle Fehler. Prüfen Sie anschließend die SupplierPartyMaster-Nachricht in Infor ION und bestätigen Sie, dass sie die konfigurierte DocBits-Organisation erreicht hat. Erst danach suchen Sie einen erwarteten Lieferanten in DocBits unter **Einstellungen → Stammdaten → Lieferant**. Nutzen Sie die Suche mit Lieferantennummer oder Name; gehen Sie nicht davon aus, dass alle M3-Lieferanten angekommen sind, nur weil der Job abgesendet wurde.

<figure><img src="../../../.gitbook/assets/m3-supplier-master-data-de-20261112.png" alt="Deutsche DocBits-Sandbox-Ansicht Einstellungen, Stammdaten mit der Registerkarte Lieferant, dem Filter Suche nach Spalte, dem Suchfeld für die Zeichenfolge und erfundenen Lieferantenzeilen"><figcaption><p>DocBits Sandbox 11.27.7: Einstellungen → Stammdaten mit der Registerkarte Lieferant sowie dem Filter Suche nach Spalte und dem Suchfeld für die Zeichenfolge. Die Zeilen SUP-1001 bis SUP-1010 sind erfundene Beispieldaten und kein Nachweis für einen M3-Import.</p></figcaption></figure>

Der Screenshot zeigt erfundene Sandbox-Daten, die in Test A bereits vorhanden sind. Bei dieser Aktualisierung der Dokumentation war kein M3-Mandant verbunden. Fehlt der erwartete Lieferant, vergleichen Sie die EVS006-Historie, das ION-Routing und die DocBits-Organisation, bevor Sie die Last erneut starten.

### Alternative: Lieferantenverwaltung

Wenn das Lieferantenportal im Einsatz ist und im Hauptmenü ein Eintrag zur Lieferantenverwaltung erscheint, sehen Sie die importierten Lieferanten auch dort, weil beide Ansichten dieselben Lieferantenstammdaten lesen. Suchen Sie mit **Suche nach Name, Nummer** nach Lieferantenname oder Lieferantennummer. Die Bedienung dieser Ansicht beschreibt die Anleitung zum [Lieferantenportal](../../../administration-and-setup/setup/supplier-portal/README.md).

<figure><img src="../../../.gitbook/assets/m3-supplier-management-search-de-20261112.png" alt="Deutsches Lieferanten-Dashboard der DocBits-Sandbox mit den Statusreitern Alle Lieferanten, Genehmigung ausstehend und Anstehende Registrierung, dem Suchfeld Suche nach Name, Nummer und erfundenen Lieferantenzeilen"><figcaption><p>DocBits Sandbox 11.27.7: Dashboard Für Lieferanten mit dem Suchfeld Suche nach Name, Nummer und den Statusreitern. Die acht Zeilen sind erfundene Beispieldaten und belegen keinen M3-Import.</p></figcaption></figure>
