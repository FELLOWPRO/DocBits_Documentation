# Lieferanten und Bestellungen

## **Verbindungspunkt**

Sie müssen den DocBits-API-Verbindungspunkt erstellen, um später den Datenfluss anzulegen.

Navigieren Sie in InforOS zu ION Desk → Connect → Connection Points

![](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH\_r3RAGOvJE6Ok67ST\_272zFfhB\_TTFYg3b-NwFq0CAv2o)

Hier angekommen müssen Sie einen neuen Verbindungspunkt erstellen.

![](https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE\_WQj-0ONoE7McRl-f6\_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI)

**Wählen Sie API**

Geben Sie dem Verbindungspunkt einen Namen und eine Beschreibung, die seine Art und seine Umgebung beschreiben. Importieren Sie unter dem Reiter „Connection" das Service-Konto, das Sie für die Umgebung erstellt haben, mit der Sie arbeiten.

![](https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0)

Wechseln Sie als Nächstes zum Reiter „Documents". Sie müssen die folgenden BODs zum Verbindungspunkt hinzufügen. Nicht alle sind für die Stammdaten zu Lieferanten und Bestellungen erforderlich, sie werden jedoch nützlich sein, wenn weitere Funktionen wie Auto Accounting implementiert werden müssen.

![](https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8\_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8)

Im Moment konzentrieren wir uns nur auf die erforderlichen BODs, diese sind: Sync.RemitToPartyMasterData, Sync.SupplierPartyMaster und Sync.PurchaseOrder.

* Sync.RemitToPartyMasterData und Sync.SupplierPartyMaster

Die Konfiguration für diese beiden BODs sollte ungefähr wie folgt aussehen (der API Call Name ändert sich für jedes)

![](https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ\_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU\_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk)

* Sync.PurchaseOrder

Die Konfiguration für dieses BOD sollte ungefähr wie folgt aussehen

![](https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4)

Sobald diese BODs konfiguriert sind, können Sie den Verbindungspunkt speichern, indem Sie auf das Symbol direkt rechts neben der Zurück-Schaltfläche klicken.

## **Datenfluss**

Der Datenfluss sieht ungefähr wie folgt aus

![](https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd\_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8)

(Der Grund für mehrere DocBits-APIs liegt darin, dass jede Verbindung eine andere Umgebung repräsentiert. Das bedeutet, dass Ihr Datenfluss je nach Anzahl Ihrer Umgebungen leicht abweichen kann.)

Für die Zwecke dieser Erläuterung verwenden wir das Beispiel von vier separaten Umgebungen.

### **M3**

Der Beginn des Datenflusses besteht aus Ihrer M3-Anwendung

### **Filter**

Die Konfiguration des Filters sieht wie folgt aus

![](https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374\_T2V0q\_\_QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY)

![](https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6\_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA)

![](https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3\_2DPj96aV0vLdZk2tzw)

(Die Buchungskreis-ID (Accounting Entity ID) ist selbstverständlich für Ihre Organisation einzigartig)

### **DocBits-API**

Hier fügen Sie eine Anwendung hinzu und wählen die zuvor erstellte(n) DocBits-API(s) aus

### **Dateien**

Die Konfiguration sollte wie folgt aussehen

![](https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY)

## **Auslösen der M3-BODs**

Navigieren Sie zur Infor M3-Anwendung

Geben Sie im Hauptmenü Command + R ein, um das Suchfeld der Befehlseingabe zu öffnen. Geben Sie dann evs006 ein und suchen Sie.

![](https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd\_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr\_o)

Auf dieser Seite müssen Sie SupplierPartyMaster, RemitToPartyMaster und PurchaseOrder zur Liste hinzufügen.

BOD Noun: SupplierPartyMaster

Table: CIDMAS

BOD Noun: RemitToPartyMaster

Table: CIDMAS

BOD Noun: PurchaseOrder

Table: MPHEAD

In jedem Fall müssen Sie auf das Plus-Symbol klicken, um sie zur Liste hinzuzufügen.

![](https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN\_ZlPk3W\_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k\_94\_pYjt6Uw)

Nachdem Sie jedes der BODs hinzugefügt haben, klicken Sie mit der rechten Maustaste auf das BOD Noun des BOD und wählen Sie Related → Run

![](https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH\_eIYzFj22XgFHZccEM9g2nVQ\_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo)

Sie werden zum folgenden Menü weitergeleitet, in dem Sie BOD Verb auf Sync ändern und dann NEXT drücken müssen, um die BODs auszulösen.

![](https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD\_ka--G1SFdzIhBAp7dq63\_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA)

Sobald Sie die BODs auslösen, erhalten Sie eine Benachrichtigung zur Bestätigung.

Bei erfolgreicher Durchführung sollten die Tabellen für Lieferanten und Bestellungen nun unter Settings → Master Data Lookup verfügbar sein.
