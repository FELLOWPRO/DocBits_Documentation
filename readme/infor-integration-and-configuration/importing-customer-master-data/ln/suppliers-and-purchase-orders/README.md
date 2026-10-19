# Lieferanten und Bestellungen

## **Connection Point**

Sie müssen den DocBits-API-Connection-Point erstellen, um später den Data Flow anlegen zu können.

Navigieren Sie zunächst in InforOS zu ION Desk → Connect → Connection Points

![](https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE)

Dort müssen Sie einen neuen Connection Point erstellen.

![](https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs_Hjw3_NDT49XG_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU)

**API auswählen**

Geben Sie dem Connection Point einen Namen und eine Beschreibung, die seine Art und seine Umgebung beschreiben. Importieren Sie auf der Registerkarte Connection den Service Account, den Sie für die jeweilige Umgebung erstellt haben.

![](https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89_6oJjuq0)

Wechseln Sie anschließend zur Registerkarte Documents. Dort müssen Sie dem Connection Point die folgenden BODs hinzufügen.

![](https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg)

* Ack-SupplierInvoice

Dieses BOD dient dazu, DocBits zu signalisieren, dass in Infor ein Fehler aufgetreten ist. Die Konfiguration für diese beiden BODs sollte ähnlich wie die folgende aussehen (der API Call Name ändert sich jeweils)

![](https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ_K6qXbtu04AP67G8jrNwkdj32LCgAhy_m4tnFQJApQehnfX8w5Y)

* Sync.PurchaseOrder

Die Konfiguration für dieses BOD sollte ähnlich wie die folgende aussehen

![](https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul_3-wFjmiroYcchb5Ou5wBA0DF0)

* Sync.ReceiveDelivery

Die Konfiguration für dieses BOD sollte ähnlich wie die folgende aussehen

![](https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc)

Sobald diese BODs konfiguriert sind, können Sie den Connection Point speichern, indem Sie auf das Symbol rechts neben der Zurück-Schaltfläche klicken.

## **Data Flow**

Der Data Flow sieht ähnlich wie der folgende aus

![](https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU)

(Der Grund für mehrere DocBits-APIs ist, dass jede Verbindung eine andere Umgebung repräsentiert. Je nach Anzahl Ihrer Umgebungen kann Ihr Data Flow daher leicht abweichen.)

Für diese Erklärung verwenden wir das Beispiel von vier getrennten Umgebungen.

### **Infor ERP / SAP**

Den Anfang des Data Flows bildet Ihre Infor-ERP-/SAP-Anwendung

### **DocBits API**

Hier fügen Sie eine Anwendung hinzu und wählen die zuvor erstellte(n) DocBits-API(s) aus

### **Files**

Die Konfiguration sollte wie folgt aussehen

![](https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU_TahhNxBugX_Bnu3QjZsKHX0Pafae-zU)

## **BOD-Auslösung in Infor ERP / SAP**

Sobald alle oben genannten Schritte abgeschlossen sind, müssen Sie in Infor ERP / SAP die BODs auslösen, damit die verschiedenen Stammdaten, die Sie für Lieferanten und Bestellungen benötigen, in DocBits ankommen.

![](https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y)

### **PurchaseOrder**

Wählen Sie im oben gezeigten Menü auf der linken Registerkarte Common → BOD-Messaging → Publish BODs → Publish Order Management Transactional Data

Wählen Sie die Registerkarte PurchaseOrder und aktivieren Sie das Kontrollkästchen.

![](https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B__08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd_66GAySp3dC1ptYKBaqLqaP1TwJco)

### **Suppliers**

Navigieren Sie auf der Startseite im linken Menü zu Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data

Wählen Sie die Registerkarte PartyMaster und aktivieren Sie das Kontrollkästchen Supplier → Buy-from oder SupplierPartyMaster.

![](https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0)

### **BOD-Auslösung**

Sobald alle richtigen BODs zur Veröffentlichung ausgewählt sind, wählen Sie die Registerkarte Options.

Die folgenden Optionen sollten ausgewählt sein.

![](https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U)

Klicken Sie anschließend auf die Schaltfläche PROCESS, damit die BODs ausgelöst werden. Eine Meldung auf dem Bildschirm informiert Sie darüber, dass die BODs ausgelöst wurden.

![](https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM)

Bei erfolgreicher Ausführung sollten die Tabellen für Lieferanten und Bestellungen nun unter Settings → Master Data Lookup verfügbar sein.

\\
