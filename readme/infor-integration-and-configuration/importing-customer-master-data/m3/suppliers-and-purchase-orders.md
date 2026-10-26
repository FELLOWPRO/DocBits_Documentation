# Lieferanten und Bestellungen

## **Verbindungspunkt**

Sie müssen den DocBits-API-Verbindungspunkt erstellen, um später den Datenfluss anzulegen.

Navigieren Sie in InforOS zu ION Desk → Connect → Connection Points

![Navigation in ION Desk mit aufgeklappter Gruppe Connect und den Einträgen Data Flows, API Flows, Mappings, Connection Points und File Templates](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH\_r3RAGOvJE6Ok67ST\_272zFfhB\_TTFYg3b-NwFq0CAv2o)

Hier angekommen müssen Sie einen neuen Verbindungspunkt erstellen.

![Seite Connection Points in ION Desk mit geöffneter Gruppe Connect in der Navigation und dem Pfad Home und Connection Points](https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE\_WQj-0ONoE7McRl-f6\_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI)

**Wählen Sie API**

Geben Sie dem Verbindungspunkt einen Namen und eine Beschreibung, die seine Art und seine Umgebung beschreiben. Importieren Sie unter dem Reiter „Connection" das Service-Konto, das Sie für die Umgebung erstellt haben, mit der Sie arbeiten.

![Dialog API Connection Point DocBits-DEV-Demo-Import mit den Tabs Usage, Connection und Documents, dem Namen DocBits-DEV-Demo-Import, dem Authentifizierungseintrag DocBits-DEV-Demo-Import Service Account und der Logical ID infor.api.docbits-dev-demo-import](https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0)

Wechseln Sie als Nächstes zum Reiter „Documents". Sie müssen die folgenden BODs zum Verbindungspunkt hinzufügen. Nicht alle sind für die Stammdaten zu Lieferanten und Bestellungen erforderlich, sie werden jedoch nützlich sein, wenn weitere Funktionen wie Auto Accounting implementiert werden müssen.

![Tab Documents des Verbindungspunkts mit den BODs Acknowledge.SupplierInvoice, Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster und Sync.SupplierPartyMaster und je einem Kontrollkästchen pro Zeile](https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8\_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8)

Im Moment konzentrieren wir uns nur auf die erforderlichen BODs, diese sind: Sync.RemitToPartyMasterData, Sync.SupplierPartyMaster und Sync.PurchaseOrder.

* Sync.RemitToPartyMasterData und Sync.SupplierPartyMaster

Die Konfiguration für diese beiden BODs sollte ungefähr wie folgt aussehen (der API Call Name ändert sich für jedes)

![BOD-Konfiguration mit den Tabs Input Document, ION API, Request Parameters, Request Body und Settings sowie den Feldern API Call Name Sync.SupplierPartyMaster, Product DocBits-DEV und der Operation POST CustomerApi/DocBits-DEV/prod/import/supplier_bod](https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ\_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU\_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk)

* Sync.PurchaseOrder

Die Konfiguration für dieses BOD sollte ungefähr wie folgt aussehen

![BOD-Konfiguration mit den Tabs Input Document, ION API, Request Parameters, Request Body und Settings sowie den Feldern API Call Name Sync.PurchaseOrder, Product DocBits-DEV und der Operation POST CustomerApi/DocBits-DEV/prod/import/purchase_order_bod](https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4)

Sobald diese BODs konfiguriert sind, können Sie den Verbindungspunkt speichern, indem Sie auf das Symbol direkt rechts neben der Zurück-Schaltfläche klicken.

## **Datenfluss**

Der Datenfluss sieht ungefähr wie folgt aus

![Datenfluss in ION Desk mit einem M3-Knoten links, mehreren DocBits-Knoten mit den Bezeichnungen DocBits-DEV-P, DocBits-DEV-S und DocBits-DEV-D in der Mitte, einem End-Knoten und einer Bedingung mit den Zweigen Yes und No](https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd\_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8)

(Der Grund für mehrere DocBits-APIs liegt darin, dass jede Verbindung eine andere Umgebung repräsentiert. Das bedeutet, dass Ihr Datenfluss je nach Anzahl Ihrer Umgebungen leicht abweichen kann.)

Für die Zwecke dieser Erläuterung verwenden wir das Beispiel von vier separaten Umgebungen.

### **M3**

Der Beginn des Datenflusses besteht aus Ihrer M3-Anwendung

### **Filter**

Die Konfiguration des Filters sieht wie folgt aus

![Bereich Filter Properties mit den Tabs Properties, Attributes und Conditions sowie den leeren Feldern Name und Description](https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374\_T2V0q\_\_QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY)

![Bereich Filter Properties mit geöffnetem Tab Attributes und den Zeilen AccountingEntityID_3 für ChartOfAccounts, AccountingEntityID für PurchaseOrder, AccountingEntityID_1 für RemitToPartyMaster und AccountingEntityID_2 für SupplierPartyMaster, alle vom Typ STRING mit dem Pfad DataArea/*/AccountingEntityID](https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6\_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA)

![Bereich Filter Properties mit geöffnetem Tab Conditions, dem Dokument ChartOfAccounts, der Bedingung Not Filtered und der Zeile DIV780AAA mit dem Ausdruck AccountingEntityID_3 gleich 780_AAA](https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3\_2DPj96aV0vLdZk2tzw)

(Die Buchungskreis-ID (Accounting Entity ID) ist selbstverständlich für Ihre Organisation einzigartig)

### **DocBits-API**

Hier fügen Sie eine Anwendung hinzu und wählen die zuvor erstellte(n) DocBits-API(s) aus

### **Dateien**

Die Konfiguration sollte wie folgt aussehen

![Ausschnitt des Datenflusses mit dem M3-Knoten links, dem Bedingungsknoten und den DocBits-Knoten, den Markern Start und End sowie dem Bereich Documents mit Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster und Sync.SupplierPartyMaster](https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY)

## **Auslösen der M3-BODs**

Navigieren Sie zur Infor M3-Anwendung

Geben Sie im Hauptmenü Command + R ein, um das Suchfeld der Befehlseingabe zu öffnen. Geben Sie dann evs006 ein und suchen Sie.

![Dialog Search and Start in Infor M3 mit dem Suchfeld für einen Befehl](https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd\_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr\_o)

Auf dieser Seite müssen Sie SupplierPartyMaster, RemitToPartyMaster und PurchaseOrder zur Liste hinzufügen.

BOD Noun: SupplierPartyMaster

Table: CIDMAS

BOD Noun: RemitToPartyMaster

Table: CIDMAS

BOD Noun: PurchaseOrder

Table: MPHEAD

In jedem Fall müssen Sie auf das Plus-Symbol klicken, um sie zur Liste hinzuzufügen.

![Kopfbereich des EVS006-Panels mit den Menüs ACTIONS, OPTIONS, RELATED und TOOLS und den Spalten BOD noun, BOD variant und BOD description](https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN\_ZlPk3W\_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k\_94\_pYjt6Uw)

Nachdem Sie jedes der BODs hinzugefügt haben, klicken Sie mit der rechten Maustaste auf das BOD Noun des BOD und wählen Sie Related → Run

![Menü Related in Infor M3 mit den Einträgen Drill down, Select, Run, Change, History, Copy, Delete, Display und den jeweiligen Tastenkürzeln](https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH\_eIYzFj22XgFHZccEM9g2nVQ\_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo)

Sie werden zum folgenden Menü weitergeleitet, in dem Sie BOD Verb auf Sync ändern und dann NEXT drücken müssen, um die BODs auszulösen.

![Panel EVS007 Initial Load Job Open mit der Tabelle CIDMAS, dem BOD noun SupplierPartyMaster, der Jobnummer 243249962976569068, dem Status 1-Pending und dem auf Sync gesetzten BOD verb](https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD\_ka--G1SFdzIhBAp7dq63\_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA)

Sobald Sie die BODs auslösen, erhalten Sie eine Benachrichtigung zur Bestätigung.

Bei erfolgreicher Durchführung sollten die Tabellen für Lieferanten und Bestellungen nun unter Settings → Master Data Lookup verfügbar sein.
