# Lieferanten und Bestellungen aus Infor LN

Dieses Beispiel behandelt die Infor-ION-Route für Lieferanten- und Bestell-BODs und wo Sie sie in DocBits prüfen. Die vierzehn Infor-Screenshots unten sind historische Beispiele aus einem Kundenmandanten. Bestätigen Sie Verbindungspunkte, API-Call-Namen und Veröffentlichungsoptionen von LN mit Ihrem Integrationsadministrator; sie wurden für diese Aktualisierung nicht in einem Infor-Mandanten geprüft. Bei dieser Aktualisierung wurde kein BOD veröffentlicht oder importiert.

Infor beschreibt den [Publisher für logistische Stammdaten in LN](https://docs.infor.com/ln/latest/en-us/lnolh/tcolh/help/tc/bod/tcbod0200m000.html) und den [Transactional Publisher für das Auftragsmanagement](https://docs.infor.com/ln/2025.x/en-us/lnolh/tdolh/help/td/bod/tdbod0200m000.html). Ihre Modi wirken unterschiedlich: **Count** meldet die Anzahl der Datensätze, ohne zu veröffentlichen; **Simulate** erzeugt ein Test-Ergebnis, ohne die Veröffentlichung zu übernehmen; **Publish** sendet die ausgewählten Daten. Eine Veröffentlichung kann alle Abonnenten erreichen; prüfen Sie daher Firmenbereich und Abonnenten, bevor Sie sie ausführen.

## **Verbindungspunkt**

Sie müssen den DocBits-API-Verbindungspunkt anlegen, um später den Datenfluss erstellen zu können.

Navigieren Sie in InforOS zunächst zu ION Desk → Connect → Connection Points.

<figure><img src="https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE" alt="Historische Infor-ION-Desk-Navigation mit grün markiertem ION Desk, aufgeklappter Gruppe Connect und hervorgehobenen Connection Points."><figcaption><p>Historisches Navigationsbeispiel: ION Desk → Connect → Connection Points.</p></figcaption></figure>

Anschließend müssen Sie hier einen neuen Verbindungspunkt anlegen.

<figure><img src="https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs_Hjw3_NDT49XG_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU" alt="Historische Seite Connection Points mit einem grünen Pfeil, der auf die Schaltfläche Add zeigt."><figcaption><p>Wählen Sie Add, um einen Verbindungspunkt anzulegen; die grüne Markierung kennzeichnet die Aktion in dieser historischen Oberfläche.</p></figcaption></figure>

**API auswählen**

Geben Sie dem Verbindungspunkt einen Namen und eine Beschreibung, die seine Art und seine Umgebung beschreiben. Importieren Sie auf der Registerkarte Connection das Servicekonto, das Sie für die jeweilige Umgebung erstellt haben.

<figure><img src="https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89_6oJjuq0" alt="Historischer API-Verbindungspunkt DocBits-DEV-Demo-Import mit geöffnetem Tab Connection und dem Import eines Servicekontos."><figcaption><p>Historischer Tab Connection. Die sichtbaren Namen von Dienstkonto und Verbindung gehören zur Beispielumgebung.</p></figcaption></figure>

Wechseln Sie anschließend zur Registerkarte Documents. Dort müssen Sie dem Verbindungspunkt die folgenden BODs hinzufügen.

<figure><img src="https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg" alt="Historischer Tab Documents mit den Routen Ack-SupplierInvoice, Sync.PurchaseOrder und Sync.ReceiveDelivery, jeweils mit Richtung In und dem empfangenen BOD."><figcaption><p>Historischer Tab Documents. Dieser Ausschnitt zeigt drei Routen; er zeigt nicht die vollständige Lieferantenkonfiguration.</p></figcaption></figure>

* Ack-SupplierInvoice

Dieses BOD dient dazu, DocBits zu signalisieren, dass in Infor ein Fehler aufgetreten ist. Die unten gezeigte Route Acknowledge.SupplierInvoice ist ein Beispiel für Rechnungsbestätigungen. Bestätigen Sie ihren API-Call-Namen und ob diese Route für Ihren Lieferanten- und Bestellablauf nötig ist.

<figure><img src="https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ_K6qXbtu04AP67G8jrNwkdj32LCgAhy_m4tnFQJApQehnfX8w5Y" alt="Historischer Tab ION API für Ack-SupplierInvoice mit ausgewählter POST-Operation."><figcaption><p>Historische Bestätigungsroute. Ack-SupplierInvoice ist ein Beispiel für einen API-Call-Namen; Acknowledge.SupplierInvoice ist das empfangene BOD.</p></figcaption></figure>

* Sync.PurchaseOrder

Das historische Beispiel unten zeigt eine empfangende Operation; bestätigen Sie die aktuelle Operation und das Anforderungsformat für Ihre Umgebung.

<figure><img src="https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul_3-wFjmiroYcchb5Ou5wBA0DF0" alt="Historischer Tab ION API mit der Auswahl Send to API für Sync.PurchaseOrder und einer konfigurierten POST-Operation."><figcaption><p>Historische Bestellroute. Prüfen Sie die empfangende Operation für Ihre DocBits-Umgebung, statt den alten Proxy-Pfad zu übernehmen.</p></figcaption></figure>

* Sync.ReceiveDelivery

Das historische Beispiel unten zeigt eine empfangende Operation; bestätigen Sie die aktuelle Operation und das Anforderungsformat für Ihre Umgebung.

<figure><img src="https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc" alt="Historischer Tab ION API für Sync.ReceiveDelivery mit einer konfigurierten POST-Operation."><figcaption><p>Historische Route für Lieferdaten. Prüfen Sie, ob ReceiveDelivery für Ihre Integration nötig ist und welche Operation sie empfängt.</p></figcaption></figure>

Sobald diese BODs konfiguriert sind, können Sie den Verbindungspunkt speichern, indem Sie auf das Symbol rechts neben der Zurück-Schaltfläche klicken.

## **Datenfluss**

Der Datenfluss sieht ähnlich wie der folgende aus.

<figure><img src="https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU" alt="Historischer Datenfluss von einem LN-Knoten über eine Aufteilung zu vier DocBits-API-Knoten und danach über eine Zusammenführung zum Ende."><figcaption><p>Historischer Ablauf mit vier Umgebungen. Aufteilung und Zusammenführung sind sichtbar; Anzahl und Ziele der Knoten hängen von Ihrem Integrationsentwurf ab.</p></figcaption></figure>

Die mehreren DocBits-API-Knoten in diesem historischen Beispiel stehen für getrennte Umgebungen. Ihr Produktionsentwurf kann eine andere Anzahl von Knoten verwenden; leiten Sie Testdaten niemals in eine Produktionsorganisation.

Die folgende Darstellung verwendet vier Umgebungen nur als Beispiel.

### **LN**

Den Anfang des Datenflusses bildet Ihre LN-Anwendung.

### **DocBits-API**

Hier fügen Sie eine Anwendung hinzu und wählen die zuvor erstellten DocBits-APIs aus.

### **Dokumente**

Prüfen Sie die dem Datenfluss zugeordnete Dokumentliste. Die hier gezeigten Lieferantennachrichten benötigen ebenfalls passende empfangende Routen im API-Verbindungspunkt. Ihre API-Call-Konfiguration ist im früheren Ausschnitt mit drei Routen nicht zu sehen; bestätigen Sie die erforderlichen Operationen mit Ihrem Integrationsadministrator.

<figure><img src="https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU_TahhNxBugX_Bnu3QjZsKHX0Pafae-zU" alt="Historische Datenflussfläche mit dem Bereich Dokumente, der Sync.PurchaseOrder, Sync.ReceiveDelivery, Sync.RemitToPartyMaster und Sync.SupplierPartyMaster auflistet."><figcaption><p>Historische Dokumentliste des Datenflusses. Lieferantennachrichten erscheinen hier neben Bestell- und Wareneingangsnachrichten.</p></figcaption></figure>

## **BOD-Auslösung in LN**

Nachdem der Integrationsadministrator Verbindungspunkt, Dokumentrouten und aktiven Datenfluss geprüft hat, verwenden Sie die passende Veröffentlichungssitzung in LN. Verfolgen Sie jede Testkennung durch LN, ION und DocBits; das Auslösen eines BOD allein belegt nicht, dass ein Datensatz angekommen ist.

<figure><img src="https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y" alt="Historische Startseite von Infor LN mit einer Favoritenliste; das Menü Publish BODs ist nicht geöffnet."><figcaption><p>Historische LN-Startseite. Nutzen Sie die unten beschriebene Navigation, um die passende Veröffentlichungssitzung zu öffnen.</p></figcaption></figure>

### **PurchaseOrder**

Wählen Sie im oben gezeigten linken Menü Common → BOD-Messaging → Publish BODs → Publish Order Management Transactional Data.

Wählen Sie die Registerkarte PurchaseOrder und aktivieren Sie das Kontrollkästchen.

<figure><img src="https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B__08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd_66GAySp3dC1ptYKBaqLqaP1TwJco" alt="Historische Sitzung Publish Order Management Transactional Data mit ausgewähltem Tab PurchaseOrder, gesetztem Kontrollkästchen und sichtbaren Feldern für den Bestellbereich."><figcaption><p>Historische Auswahl PurchaseOrder. Prüfen Sie Bestellbereich und Status, bevor Sie veröffentlichen.</p></figcaption></figure>

### **Suppliers**

Navigieren Sie auf der Startseite von LN im linken Menü zu Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data.

Wählen Sie die Registerkarte PartyMaster und aktivieren Sie das Kontrollkästchen Supplier → Buy-from oder SupplierPartyMaster.

<figure><img src="https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0" alt="Historische Sitzung Publish Logistic Master Data mit ausgewähltem Tab PartyMaster und gesetztem Kontrollkästchen Supplier Buy-from."><figcaption><p>Historische Lieferantenauswahl auf PartyMaster. Wählen Sie die Partnerrollen, die Ihre Integration benötigt, und prüfen Sie den Auswahlbereich.</p></figcaption></figure>

### **BOD-Auslösung**

Sobald alle richtigen BODs zur Veröffentlichung ausgewählt sind, wählen Sie die Registerkarte Options.

Prüfen Sie die Optionen für Ihren Mandanten. Das historische Beispiel hebt Publish und Use Process/Sync Verb hervor; das sind keine allgemeingültigen Einstellungen für jede Integration.

<figure><img src="https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U" alt="Historischer Tab Options mit hervorgehobenen Publish und Use Process/Sync Verb und einem sichtbaren Firmenbereich."><figcaption><p>Historisches Optionsbeispiel. Publish und Use Process/Sync Verb sind hier ausgewählt; prüfen Sie Modus, Firmenbereich und Abonnenten für Ihren eigenen Lauf.</p></figcaption></figure>

Prüfen Sie vor **Process** mit **Count** oder **Simulate** die Datensatzanzahl und den Firmenbereich, sofern Ihre LN-Version diese Modi anbietet. Veröffentlichen Sie nur mit Zustimmung des Integrationsadministrators. Eine Bestätigung, dass BODs ausgelöst wurden, belegt keine Zustellung an DocBits.

<figure><img src="https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM" alt="Historischer Tab Options mit hervorgehobener Schaltfläche Process vor der Ausführung."><figcaption><p>Historische Aktion Process vor der Ausführung. Dieser Screenshot enthält kein Veröffentlichungsergebnis und keine Bestätigung, dass DocBits Daten erhalten hat.</p></figcaption></figure>

## In DocBits prüfen

Prüfen Sie in Infor ION, ob die Zustellung an die gewünschte DocBits-Organisation erfolgreich war. Öffnen Sie dann **Einstellungen → Dokumentenverarbeitung → Stammdaten**. Öffnen Sie unter **BOD Eingangsdaten** den Eintrag **Lieferant**. Wählen Sie das Kennungsfeld unter **Suche nach Spalte**, geben Sie eine bekannte Lieferantennummer oder einen Namen unter **Suche Zeichenfolge** ein und suchen Sie über das Lupensymbol. Öffnen Sie **Bestellung** und suchen Sie nach einer bekannten Bestellnummer. Prüfen Sie zusätzlich **Purchase Order Header**, wenn Ihre Zuordnung Kopf und Positionen trennt. Vergleichen Sie Kennungen und Firma mit LN; schließen Sie aus einer erfolgreichen Veröffentlichungsmeldung nicht, dass alle Datensätze angekommen sind. Für die Prüfung genügen die Suchfelder; die Schaltfläche **Aktionen** bleibt dabei ungenutzt.

<figure><img src="../../../../.gitbook/assets/dbdc-1143-supplier-de-20261112.png" alt="Deutsche Ansicht Stammdaten mit dem Breadcrumb Einstellungen und Stammdaten, dem Tab Lieferant, den Suchfeldern Suche nach Spalte und Suche Zeichenfolge sowie den erfundenen Beispielzeilen SUP-1001 bis SUP-1010."><figcaption><p>Lieferantenansicht in der Sandbox, Version 11.27.7 (unten links). Die sichtbaren Zeilen sind erfundene Beispieldaten und belegen keinen LN-Import.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/dbdc-1143-purchase-order-de-20261112.png" alt="Deutsche Ansicht Stammdaten mit dem Tab Bestellung, den Suchfeldern Suche nach Spalte und Suche Zeichenfolge, der Abschnittsliste Lieferant, Bestellung und Purchase Order Header sowie den erfundenen Beispielzeilen PO-4500 bis PO-4509."><figcaption><p>Bestellansicht in der Sandbox, Version 11.27.7. Die Zeilen sind erfundene Beispieldaten; vergleichen Sie Testbestellung und Firma mit LN und ION.</p></figcaption></figure>

Bei dieser Aktualisierung wurde kein BOD veröffentlicht, keine Datei importiert und keine Stammdaten geändert. Die beiden deutschen Aufnahmen zeigen die Sandbox in der Version 11.27.7 mit erfundenen Beispieldaten; sie zeigen, wo Sie prüfen, nicht einen abgeschlossenen LN-Transfer. Wenn der erwartete Datensatz fehlt, prüfen Sie Veröffentlichungsprotokolle in LN, ION-Routing, Organisation und BOD-Zuordnung, bevor Sie erneut ausführen.
