# Dostawcy i Zamówienia Zakupu

## **Punkt Połączenia**

Aby później utworzyć przepływ danych, musisz utworzyć punkt połączenia interfejsu API DocBits.

Najpierw w InforOS przejdź do ION Desk → Połącz → Punkty Połączenia

![](https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE)

Następnie musisz utworzyć nowy punkt połączenia.

![](https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs_Hjw3_NDT49XG_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU)

**Wybierz API**

Nadaj punktowi połączenia nazwę i opis, który opisuje jego charakter i środowisko. W zakładce Połączenie zaimportuj konto usługi utworzone dla środowiska, z którym pracujesz.

![](https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89_6oJjuq0)

Następnie przejdź do zakładki Dokumenty. Musisz dodać następujące BODy do punktu połączenia.

![](https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg)

* Ack-SupplierInvoice

Ten BOD służy do sygnalizowania w DocBits, że wystąpił błąd w Infor. Konfiguracja tych dwóch BODów powinna wyglądać podobnie do poniższej (Nazwa Wywołania API zmienia się dla każdego)

![](https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ_K6qXbtu04AP67G8jrNwkdj32LCgAhy_m4tnFQJApQehnfX8w5Y)

* Sync.PurchaseOrder

Konfiguracja tego BOD powinna wyglądać podobnie do poniższej

![](https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul_3-wFjmiroYcchb5Ou5wBA0DF0)

* Sync.ReceiveDelivery

Konfiguracja tego BOD powinna wyglądać podobnie do poniższej

![](https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc)

Gdy te BODy są skonfigurowane, możesz zapisać punkt połączenia, naciskając ikonę położoną tuż obok przycisku powrotu.

## **Przepływ Danych**

Przepływ danych będzie wyglądał podobnie do poniższego

![](https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU)

(Powód posiadania wielu interfejsów API DocBits wynika z tego, że każde połączenie reprezentuje inne środowisko, co oznacza, że w zależności od ilości środowisk, twój przepływ danych może się nieznacznie różnić)

W celu wyjaśnienia posłużymy się przykładem posiadania czterech oddzielnych środowisk.

### **LN**

Początek przepływu danych obejmuje twoją aplikację LN

### **Interfejs API DocBits**

Tutaj dodasz aplikację i wybierzesz wcześniej utworzone interfejsy API DocBits

### **Pliki**

Konfiguracja powinna wyglądać następująco

![](https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU_TahhNxBugX_Bnu3QjZsKHX0Pafae-zU)

## **Wywoływanie BOD w LN**

Po zakończeniu powyższych czynności, przejdź do Infor LN i wywołaj BODy, aby różne dane główne potrzebne do Dostawców i Zamówień Zakupu dotarły do DocBits.

![](https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y)

### **Zamówienie Zakupu**

Z powyższego menu, w lewym menu wybierz Ogólne → Komunikacja BOD → Publikuj BODy → Publikuj Dane Transakcyjne Zarządzania Zamówieniami

Wybierz zakładkę Zamówienie Zakupu i zaznacz pole wyboru.

![](https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B__08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd_66GAySp3dC1ptYKBaqLqaP1TwJco)
### **Dostawcy**

Z głównej strony LN przejdź do menu po lewej stronie, następnie wybierz Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data

Wybierz zakładkę PartyMaster i zaznacz pole Supplier → Buy-from lub SupplierPartyMaster.

![](https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0)

### **Wywoływanie BOD**

Po zaznaczeniu wszystkich poprawnych BODs do publikacji, wybierz zakładkę Opcje.

Następujące opcje powinny być zaznaczone.

![](https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U)

Po zakończeniu, naciśnij przycisk PROCESS, a BODs zostaną wywołane. Na ekranie pojawi się komunikat informujący, że BODs zostały wywołane.

![](https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM)

Jeśli wykonano poprawnie, tabele Dostawców i Zamówień Zakupu powinny teraz być dostępne w Ustawienia → Wyszukiwanie Danych Podstawowych.

\
