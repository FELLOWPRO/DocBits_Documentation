# Dostawcy i zamówienia zakupu z Infor LN

Ten przykład opisuje trasę Infor ION dla BOD-ów dostawców i zamówień zakupu oraz miejsca, w których można je sprawdzić w DocBits. Czternaście zrzutów ekranu Infor poniżej to historyczne przykłady z dzierżawy. Punkty połączenia, nazwy wywołań API i opcje publikowania w LN potwierdź z administratorem integracji; nie zostały sprawdzone w dzierżawie Infor na potrzeby tej aktualizacji. Podczas tej aktualizacji nie opublikowano ani nie zaimportowano żadnego BOD-a.

Infor opisuje [wydawcę danych głównych logistyki LN](https://docs.infor.com/ln/latest/en-us/lnolh/tcolh/help/tc/bod/tcbod0200m000.html) oraz [wydawcę transakcyjnego Order Management](https://docs.infor.com/ln/2025.x/en-us/lnolh/tdolh/help/td/bod/tdbod0200m000.html). Ich tryby działają inaczej: **Count** raportuje liczby rekordów bez publikowania; **Simulate** tworzy wynik próbny bez zatwierdzania publikacji; **Publish** wysyła wybrane dane. Publikacja może dotrzeć do wszystkich subskrybentów, więc przed jej uruchomieniem sprawdź zakres firm i subskrybentów.

## **Punkt połączenia**

Aby później utworzyć przepływ danych, musisz utworzyć punkt połączenia DocBits API.

Najpierw w InforOS przejdź do ION Desk → Connect → Connection Points

<figure><img src="https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE" alt="Historyczna nawigacja Infor ION Desk z rozwiniętą grupą Connect i wyróżnionym punktem Connection Points."><figcaption><p>Historyczny przykład nawigacji: ION Desk → Connect → Connection Points.</p></figcaption></figure>

Następnie utwórz nowy punkt połączenia.

<figure><img src="https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs_Hjw3_NDT49XG_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU" alt="Historyczny ekran Connection Points ze zieloną strzałką wskazującą przycisk Add."><figcaption><p>Wybierz Add, aby utworzyć punkt połączenia; zielona adnotacja oznacza tę czynność w historycznym interfejsie.</p></figcaption></figure>

**Wybierz API**

Nadaj punktowi połączenia nazwę i opis, które określają jego charakter i środowisko. Na karcie Connection zaimportuj konto usługi utworzone dla środowiska, w którym pracujesz.

<figure><img src="https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89_6oJjuq0" alt="Historyczny punkt połączenia API DocBits-DEV-Demo-Import z wybraną kartą Connection i kontrolką Import konta usługi."><figcaption><p>Historyczna karta Connection. Widoczne nazwy konta usługi i połączenia należą do środowiska przykładowego.</p></figcaption></figure>

Następnie przełącz się na kartę Documents. Do punktu połączenia musisz dodać następujące BOD-y.

<figure><img src="https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg" alt="Historyczna niemiecka karta Dokumente (Documents) z wywołaniami API Ack-SupplierInvoice, Sync.PurchaseOrder i Sync.ReceiveDelivery oraz odebranymi BOD-ami."><figcaption><p>Historyczna karta Dokumente (Documents). Ten wycinek pokazuje trzy trasy; nie pokazuje pełnej konfiguracji dostawców.</p></figcaption></figure>

* Ack-SupplierInvoice

Ten BOD służy do sygnalizowania w DocBits, że w Infor wystąpił błąd. Trasa Acknowledge.SupplierInvoice pokazana poniżej jest przykładem potwierdzania faktur. Potwierdź nazwę wywołania API oraz to, czy ta trasa jest potrzebna w Twoim przepływie dostawców i zamówień zakupu.

<figure><img src="https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ_K6qXbtu04AP67G8jrNwkdj32LCgAhy_m4tnFQJApQehnfX8w5Y" alt="Historyczna niemiecka karta ION API dla Ack-SupplierInvoice z wybraną operacją POST."><figcaption><p>Historyczna trasa potwierdzania. Ack-SupplierInvoice to przykładowa nazwa wywołania API; Acknowledge.SupplierInvoice to odebrany BOD.</p></figcaption></figure>

* Sync.PurchaseOrder

Historyczny przykład poniżej pokazuje jedną operację odbioru; potwierdź aktualną operację i format żądania dla swojego środowiska.

<figure><img src="https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul_3-wFjmiroYcchb5Ou5wBA0DF0" alt="Historyczna karta ION API z wybraną opcją Send to API dla Sync.PurchaseOrder i skonfigurowaną operacją POST."><figcaption><p>Historyczna trasa zamówień zakupu. Sprawdź operację odbioru dla swojego środowiska DocBits, zamiast kopiować starą ścieżkę proxy.</p></figcaption></figure>

* Sync.ReceiveDelivery

Historyczny przykład poniżej pokazuje jedną operację odbioru; potwierdź aktualną operację i format żądania dla swojego środowiska.

<figure><img src="https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc" alt="Historyczna niemiecka karta ION API dla Sync.ReceiveDelivery ze skonfigurowaną operacją POST."><figcaption><p>Historyczna trasa danych odbioru. Sprawdź, czy ReceiveDelivery jest potrzebne w Twojej integracji i która operacja je odbiera.</p></figcaption></figure>

Po skonfigurowaniu tych BOD-ów możesz zapisać punkt połączenia, wybierając ikonę po prawej stronie przycisku wstecz.

## **Przepływ danych**

Przepływ danych będzie wyglądał podobnie do poniższego

<figure><img src="https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU" alt="Historyczny przepływ dokumentów od węzła LN przez równoległy podział do czterech węzłów DocBits API, a następnie połączenie i węzeł końcowy."><figcaption><p>Historyczny przepływ z czterema środowiskami. Podział i połączenie są widoczne; liczba i cele węzłów zależą od Twojego projektu integracji.</p></figcaption></figure>

Wiele węzłów DocBits API w tym historycznym przykładzie reprezentuje osobne środowiska. Twój projekt produkcyjny może używać innej liczby węzłów; nigdy nie kieruj danych testowych do organizacji produkcyjnej.

Poniższa ilustracja używa czterech środowisk wyłącznie jako przykład.

### **LN**

Początek przepływu danych stanowi Twoja aplikacja LN

### **DocBits API**

Tutaj dodajesz aplikację i wybierasz utworzone wcześniej DocBits API

### **Dokumenty**

Sprawdź listę dokumentów przypisanych do przepływu. Komunikaty dostawców pokazane tutaj również wymagają odpowiednich tras odbioru w punkcie połączenia API. Ich konfiguracja wywołań API nie jest widoczna na wcześniejszym wycinku z trzema trasami; potwierdź wymagane operacje z administratorem integracji.

<figure><img src="https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU_TahhNxBugX_Bnu3QjZsKHX0Pafae-zU" alt="Historyczne pole robocze przepływu z niemieckim panelem Dokumente poniżej, który wymienia Sync.PurchaseOrder, Sync.ReceiveDelivery, Sync.RemitToPartyMaster i Sync.SupplierPartyMaster."><figcaption><p>Historyczna lista dokumentów przepływu. Komunikaty dostawców występują tutaj obok komunikatów zamówień zakupu i odbiorów.</p></figcaption></figure>

## **Wyzwalanie BOD-ów w LN**

Gdy administrator integracji sprawdzi punkt połączenia, trasy dokumentów i aktywny przepływ danych, użyj odpowiedniej sesji publikowania w LN. Śledź każdy identyfikator testowy przez LN, ION i DocBits; samo wyzwolenie BOD-a nie dowodzi, że rekord dotarł.

<figure><img src="https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y" alt="Historyczna niemiecka strona główna Infor LN z listą ulubionych; menu Publish BODs nie jest otwarte."><figcaption><p>Historyczna strona startowa LN. Skorzystaj z nawigacji opisanej poniżej, aby znaleźć odpowiednią sesję publikowania.</p></figcaption></figure>

### **PurchaseOrder**

W powyższym menu, w lewej karcie menu, wybierz Common → BOD-Messaging → Publish BODs → Publish Order Management Transactional Data

Wybierz kartę PurchaseOrder i zaznacz pole wyboru.

<figure><img src="https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B__08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd_66GAySp3dC1ptYKBaqLqaP1TwJco" alt="Historyczna sesja Publish Order Management Transactional Data z wybraną kartą PurchaseOrder i zaznaczonym polem wyboru oraz widocznymi polami zakresu zamówień."><figcaption><p>Historyczne zaznaczenie PurchaseOrder. Przed publikacją sprawdź zakres zamówień i statusy.</p></figcaption></figure>

### **Dostawcy**

Na stronie głównej LN, w lewej karcie menu, przejdź do Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data

Wybierz kartę PartyMaster i zaznacz pole Supplier → Buy-from lub SupplierPartyMaster.

<figure><img src="https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0" alt="Historyczna sesja Publish Logistic Master Data z wybraną kartą PartyMaster i zaznaczonym polem Supplier Buy-from."><figcaption><p>Historyczne zaznaczenie dostawców na karcie PartyMaster. Wybierz role partnerów potrzebne w Twojej integracji i sprawdź zakres zaznaczenia.</p></figcaption></figure>

### **Wyzwalanie BOD-ów**

Gdy wszystkie właściwe BOD-y są zaznaczone do publikacji, wybierz kartę Options.

Sprawdź opcje dla swojej dzierżawy. Historyczny przykład wyróżnia Publish i Use Process/Sync Verb; nie są to uniwersalne ustawienia każdej integracji.

<figure><img src="https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U" alt="Historyczna karta Options w LN z wyróżnionymi opcjami Publish i Use Process/Sync Verb oraz widocznym zakresem firm."><figcaption><p>Historyczny przykład karty Options. Tutaj wybrano Publish i Use Process/Sync Verb; sprawdź tryb, zakres firm i subskrybentów dla własnego uruchomienia.</p></figcaption></figure>

Przed **Process** użyj **Count** lub **Simulate** i sprawdź liczbę rekordów oraz zakres firm, jeśli Twoja wersja LN oferuje te tryby. Publikuj wyłącznie za zgodą administratora integracji. Potwierdzenie, że BOD-y zostały wyzwolone, nie dowodzi dostarczenia ich do DocBits.

<figure><img src="https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM" alt="Historyczna karta Options w LN z wyróżnionym przyciskiem Process przed wykonaniem."><figcaption><p>Historyczna czynność Process przed wykonaniem. Ten zrzut ekranu nie zawiera wyniku publikacji ani potwierdzenia, że DocBits otrzymał dane.</p></figcaption></figure>

## Sprawdź w DocBits

Sprawdź w Infor ION, czy dane dotarły do właściwej organizacji DocBits. Następnie otwórz **Ustawienia → Przetwarzanie dokumentów → Wyszukaj dane główne**. W sekcji **Dane wejściowe BOD** otwórz **Dostawca**. W polu **Szukaj według kolumny** wybierz pole identyfikatora, w polu **Szukaj Tekst** wpisz znany numer lub nazwę dostawcy i użyj lupy, aby wyszukać. Otwórz **Zamówienie Zakupu** i wyszukaj znany numer zamówienia. Sprawdź także **Nagłówek Zamówienia Zakupu**, jeśli Twoje mapowanie rozdziela nagłówek i pozycje. Porównaj identyfikatory i firmę z LN; nie zakładaj, że wszystkie rekordy dotarły, tylko dlatego że komunikat o publikacji zakończył się powodzeniem. W polskim interfejsie nagłówki kolumn tabeli pozostają w języku angielskim, na przykład Supplier Id i Supplier Name.

<figure><img src="../../../../.gitbook/assets/dbdc-1148-supplier-pl-20261112.png" alt="Widok Dostawca w Wyszukaj Dane Główne w DocBits po polsku z polami Szukaj według kolumny i Szukaj Tekst oraz dziesięcioma wymyślonymi przykładowymi wierszami dostawców od SUP-1001 do SUP-1010."><figcaption><p>Widok weryfikacji dostawców w wersji sandbox 11.27.7 z wymyślonymi przykładowymi wierszami. Wyszukaj znany identyfikator testowy i porównaj go z LN i ION.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/dbdc-1148-purchase-order-pl-20261112.png" alt="Widok Zamówienie zakupu w Wyszukaj Dane Główne w DocBits po polsku z otwartymi kartami Dostawca i Zamówienie zakupu, tymi samymi polami wyszukiwania oraz dziesięcioma wymyślonymi przykładowymi wierszami zamówień od PO-4500 do PO-4509."><figcaption><p>Widok weryfikacji zamówień zakupu w wersji sandbox 11.27.7 z wymyślonymi przykładowymi wierszami. Wiersze nie dowodzą importu z LN.</p></figcaption></figure>

Angielskie widoki w Dev sprawdzono 29 października 2026 bez publikowania BOD-a, importowania pliku i zmiany danych głównych; w tamtych obrazach wiersze rekordów zostały pominięte. Oba polskie zrzuty ekranu pochodzą z wersji sandbox 11.27.7 i pokazują wymyślone przykładowe wiersze zamiast rzeczywistych danych głównych; pokazują, gdzie sprawdzić dane, a nie zakończony transfer z LN. Jeśli oczekiwany rekord nie występuje, sprawdź logi publikowania w LN, routing ION, organizację i mapowanie BOD-ów przed ponownym uruchomieniem.
