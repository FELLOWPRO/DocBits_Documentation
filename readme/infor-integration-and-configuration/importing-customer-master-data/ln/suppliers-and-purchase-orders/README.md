# Dostawcy i zamówienia zakupu

## **Punkt połączenia**

Musisz utworzyć punkt połączenia DocBits API (Connection Point), aby później utworzyć przepływ danych.

Najpierw w InforOS przejdź do ION Desk → Connect → Connection Points

![Nawigacja ION Desk z rozwiniętą grupą Connect i pozycjami Data Flows, API Flows, Mappings, Connection Points i File Templates](https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE)

Następnie utwórz nowy punkt połączenia.

![Strona Connection Points w ION Desk z otwartą grupą Connect w nawigacji i ścieżką Home i Connection Points](https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs_Hjw3_NDT49XG_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU)

**Wybierz API**

Nadaj punktowi połączenia nazwę i opis, które odzwierciedlają jego charakter i środowisko. Na karcie Connection zaimportuj konto serwisowe utworzone dla środowiska, w którym pracujesz.

![Okno API Connection Point DocBits-DEV-Demo-Import z kartami Usage, Connection i Documents, nazwą DocBits-DEV-Demo-Import, pozycją uwierzytelniania DocBits-DEV-Demo-Import Service Account i Logical ID infor.api.docbits-dev-demo-import](https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89_6oJjuq0)

Następnie przełącz się na kartę Documents. Do punktu połączenia musisz dodać następujące BOD-y.

![Karta Documents punktu połączenia z wierszami Ack-SupplierInvoice, Sync.PurchaseOrder i Sync.ReceiveDelivery, każdy z kierunkiem In i BOD o tej samej nazwie](https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg)

* Ack-SupplierInvoice

Ten BOD służy do sygnalizowania w DocBits, że w Infor wystąpił błąd. Konfiguracja tych dwóch BOD-ów powinna wyglądać podobnie do poniższej (zmienia się nazwa wywołania API (API Call Name) dla każdego z nich)

![Konfiguracja BOD z kartami Input Document, ION API, Request Parameters, Request Body i Settings oraz API Call Name Ack-SupplierInvoice](https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ_K6qXbtu04AP67G8jrNwkdj32LCgAhy_m4tnFQJApQehnfX8w5Y)

* Sync.PurchaseOrder

Konfiguracja tego BOD-a powinna wyglądać podobnie do poniższej

![Konfiguracja BOD z kartami Input Document, ION API, Request Parameters, Request Body i Settings oraz polami API Call Name Sync.PurchaseOrder, Product DocBits-DEV i operacją POST CustomerApi/DocBits-DEV/prod/import/purchase_order_bod](https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul_3-wFjmiroYcchb5Ou5wBA0DF0)

* Sync.ReceiveDelivery

Konfiguracja tego BOD-a powinna wyglądać podobnie do poniższej

![Konfiguracja BOD z kartami Input Document, ION API, Request Parameters, Request Body i Settings oraz API Call Name Sync.ReceiveDelivery](https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc)

Po skonfigurowaniu tych BOD-ów możesz zapisać punkt połączenia, naciskając ikonę znajdującą się po prawej stronie przycisku Wstecz.

## **Przepływ danych (Data Flow)**

Przepływ danych będzie wyglądał podobnie do poniższego

![Przepływ danych w ION Desk z węzłem punktu połączenia DocBits po lewej i węzłem End po prawej](https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU)

(Powodem występowania wielu DocBits API jest to, że każde połączenie reprezentuje inne środowisko, więc w zależności od liczby posiadanych środowisk Twój przepływ danych może się nieznacznie różnić)

Na potrzeby tego wyjaśnienia użyjemy przykładu z czterema oddzielnymi środowiskami.

### **LN**

Początek przepływu danych stanowi Twoja aplikacja LN

### **API DocBits**

Tutaj dodajesz aplikację i wybierasz utworzone wcześniej DocBits API

### **Pliki**

Konfiguracja powinna wyglądać następująco

![Szczegół przepływu danych z węzłem DocBits DocBits-DEV-P, znacznikami Start i Ende oraz drugim węzłem DocBits pośrodku, a także panelem Dokumente z Sync.PurchaseOrder, Sync.ReceiveDelivery, Sync.RemitToPartyMaster i Sync.SupplierPartyMaster](https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU_TahhNxBugX_Bnu3QjZsKHX0Pafae-zU)

## **Wyzwalanie BOD-ów w LN**

Po zakończeniu wszystkich powyższych kroków należy przejść do Infor LN i wyzwolić BOD-y, aby różne dane podstawowe potrzebne dla dostawców i zamówień zakupu trafiły do DocBits.

![Strona startowa Infor LN z panelem ulubionych po lewej i kafelkami zamówień, faktur i zleceń magazynowych](https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y)

### **PurchaseOrder**

W powyższym menu, w lewej zakładce menu, wybierz Common → BOD-Messaging → Publish BODs → Publish Order Management Transactional Data

Wybierz kartę PurchaseOrder i zaznacz pole wyboru.

![Okno Publish Order Management Transactional Data z przyciskami PROCESS, CLOSE, SELECT ALL i CLEAR ALL, wybraną kartą PurchaseOrder i drzewem po lewej z rozwiniętymi BOD Messaging i Publish BODs](https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B__08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd_66GAySp3dC1ptYKBaqLqaP1TwJco)

### **Dostawcy**

Na stronie głównej LN, w lewej zakładce menu, przejdź do Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data

Wybierz kartę PartyMaster i zaznacz pole Supplier → Buy-from lub SupplierPartyMaster.

![Okno Publish Logistic Master Data z przyciskami PROCESS, CLOSE, SELECT ALL i CLEAR ALL, wybraną kartą PartyMaster i siatką z kolumnami Supplier, Buy-from PartyMaster, Pay-to PartyMaster, Pay-from PartyMaster i Remit-to PartyMaster](https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0)

### **Wyzwalanie BOD-ów**

Gdy wszystkie właściwe BOD-y zostaną zaznaczone do publikacji, wybierz kartę Options.

Należy wybrać następujące opcje.

![Okno Publish Logistic Master Data z selektorem Mode, sekcją Selection Range z firmą 0051 i sekcją BOD Messaging Settings](https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U)

Po zakończeniu naciśnij przycisk PROCESS, a BOD-y zostaną wyzwolone. Na ekranie pojawi się komunikat informujący o wyzwoleniu BOD-ów.

![Okno Publish Logistic Master Data z polami wyboru Show Verb, Logical IDxs, Use ProcessSync Verb i Logging w sekcji BOD Messaging Settings oraz przyciskami PROCESS, CLOSE, SELECT ALL i CLEAR ALL](https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM)

Jeśli operacja zakończyła się powodzeniem, tabele dostawców i zamówień zakupu powinny być teraz dostępne w Ustawienia → Master Data Lookup.

\\
