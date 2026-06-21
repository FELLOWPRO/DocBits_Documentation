# Lieferanten und Bestellungen

## **Verbindungspunkt**

Sie müssen den DocBits-API-Verbindungspunkt erstellen, um später den Datenfluss anzulegen.

Navigieren Sie zunächst in InforOS zu ION Desk → Connect → Connection Points

![](https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6\_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC\_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE)

Hier angekommen müssen Sie einen neuen Verbindungspunkt erstellen.

![](https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs\_Hjw3\_NDT49XG\_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU)

**Wählen Sie API**

Geben Sie dem Verbindungspunkt einen Namen und eine Beschreibung, die seine Art und seine Umgebung beschreiben. Importieren Sie unter dem Reiter „Connection" das Service-Konto, das Sie für die Umgebung erstellt haben, mit der Sie arbeiten.

![](https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT\_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89\_6oJjuq0)

Wechseln Sie als Nächstes zum Reiter „Documents". Sie müssen die folgenden BODs zum Verbindungspunkt hinzufügen.

![](https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as\_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg)

* Ack-SupplierInvoice

Dieses BOD wird verwendet, um in DocBits zu signalisieren, dass innerhalb von Infor ein Fehler aufgetreten ist. Die Konfiguration für diese beiden BODs sollte ungefähr wie folgt aussehen (der API Call Name ändert sich für jedes)

![](https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X\_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ\_K6qXbtu04AP67G8jrNwkdj32LCgAhy\_m4tnFQJApQehnfX8w5Y)

* Sync.PurchaseOrder

Die Konfiguration für dieses BOD sollte ungefähr wie folgt aussehen

![](https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4\_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul\_3-wFjmiroYcchb5Ou5wBA0DF0)

* Sync.ReceiveDelivery

Die Konfiguration für dieses BOD sollte ungefähr wie folgt aussehen

![](https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc)

Sobald diese BODs konfiguriert sind, können Sie den Verbindungspunkt speichern, indem Sie auf das Symbol direkt rechts neben der Zurück-Schaltfläche klicken.

## **Datenfluss**

Der Datenfluss sieht ungefähr wie folgt aus

![](https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU)

(Der Grund für mehrere DocBits-APIs liegt darin, dass jede Verbindung eine andere Umgebung repräsentiert. Das bedeutet, dass Ihr Datenfluss je nach Anzahl Ihrer Umgebungen leicht abweichen kann.)

Für die Zwecke dieser Erläuterung verwenden wir das Beispiel von vier separaten Umgebungen.

### **LN**

Der Beginn des Datenflusses besteht aus Ihrer LN-Anwendung

### **DocBits-API**

Hier fügen Sie eine Anwendung hinzu und wählen die zuvor erstellte(n) DocBits-API(s) aus

### **Dateien**

Die Konfiguration sollte wie folgt aussehen

![](https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J\_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU\_TahhNxBugX\_Bnu3QjZsKHX0Pafae-zU)

## **Auslösen der LN-BODs**

Sobald alle oben genannten Schritte abgeschlossen sind, müssen Sie zu Infor LN navigieren und die BODs auslösen, damit die verschiedenen Stammdaten, die Sie für Lieferanten und Bestellungen benötigen, in DocBits ankommen.

![](https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n\_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y)

### **PurchaseOrder**

Wählen Sie aus dem oben gezeigten Menü im linken Menü-Reiter Common → BOD-Messaging → Publish BODs → Publish Order Management Transactional Data

Wählen Sie den Reiter PurchaseOrder und aktivieren Sie das Kontrollkästchen.

![](https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr\_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B\_\_08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd\_66GAySp3dC1ptYKBaqLqaP1TwJco)

### **Lieferanten**

Navigieren Sie von der LN-Startseite aus im linken Menü-Reiter zu Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data

Wählen Sie den Reiter PartyMaster und aktivieren Sie das Kontrollkästchen Supplier → Buy-from oder SupplierPartyMaster.

![](https://lh7-us.googleusercontent.com/KY\_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr\_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0)

### **Auslösen der BODs**

Sobald alle korrekten BODs für die Veröffentlichung angekreuzt wurden, wählen Sie den Reiter „Options".

Die folgenden Optionen sollten ausgewählt werden.

![](https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc\_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C\_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe\_4\_tXKy54nI8U)

Sobald dies abgeschlossen ist, drücken Sie die Schaltfläche PROCESS, und die BODs werden ausgelöst. Eine Meldung erscheint auf dem Bildschirm, um Sie darüber zu informieren, dass die BODs ausgelöst wurden.

![](https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN\_oeTBqz\_1knMoYsSxEA-\_NtGVx\_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9\_fzrTZUCMs\_vnoxbvM)

Bei erfolgreicher Durchführung sollten die Tabellen für Lieferanten und Bestellungen nun unter Settings → Master Data Lookup verfügbar sein.

\
