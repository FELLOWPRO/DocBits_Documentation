# Dostawcy i zamówienia zakupu z Infor M3

Ten przykład łączy BOD dostawców i zamówień zakupu z M3 z DocBits poprzez Infor ION. Piętnaście poniższych obrazów Infor to historyczne przykłady z dzierżawy, a nie bieżące potwierdzenie Twojej konfiguracji M3. Przed uruchomieniem zadania poproś administratora Infor o potwierdzenie nazw BOD, tabel źródłowych, firmy, działu, nazw wywołań API i środowiska docelowego. W ramach tej aktualizacji nie wykonano ładowania początkowego M3 ani importu w DocBits.

Przewodnik Infor dotyczący [ładowania początkowego](https://docs.infor.com/m3udi/16.x/en-us/m3beud/appfoundhs/spl1567531742751.html) opisuje definicje EVS006, czasownik i wybór EVS007, wysyłanie oraz historię. Zacznij od ograniczonego wyboru; nieograniczone uruchomienie może wygenerować wiele zdarzeń.

## **Punkt połączenia**

Aby później utworzyć przepływ danych, konieczne będzie utworzenie punktu połączenia DocBits API.

W InforOS przejdź do ION Desk → Connect → Connection Points

<figure><img src="https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o" alt="Historyczna nawigacja ION Desk z rozwiniętą grupą Connect i wyróżnionym elementem Connection Points."><figcaption><p>Historyczna nawigacja: ION Desk → Connect → Connection Points.</p></figcaption></figure>

Po dotarciu na tę stronę musisz utworzyć nowy punkt połączenia.

<figure><img src="https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE_WQj-0ONoE7McRl-f6_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI" alt="Historyczna strona Connection Points ze zieloną strzałką wskazującą opcję Add."><figcaption><p>Historyczna czynność Add służąca do utworzenia punktu połączenia.</p></figcaption></figure>

**Select API**

Nadaj punktowi połączenia nazwę i opis określający jego charakter i środowisko. Na karcie Connection zaimportuj konto usługi utworzone dla środowiska, z którym pracujesz.

<figure><img src="https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0" alt="Historyczny punkt połączenia DocBits-DEV-Demo-Import typu API z wybraną kartą Connection i elementem Import konta usługi."><figcaption><p>Historyczna karta Connection. Wyświetlone nazwy dotyczą środowiska przykładowego; użyj własnego konta usługi.</p></figcaption></figure>

Następnie przejdź na kartę Documents. Do punktu połączenia musisz dodać następujące BOD; nie wszystkie są potrzebne dla danych podstawowych dostawców i zamówień zakupu, ale będą przydatne przy wdrażaniu innych funkcji, takich jak automatyczne księgowanie.

<figure><img src="https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8" alt="Historyczna karta Documents z listą Acknowledge.SupplierInvoice, Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster i Sync.SupplierPartyMaster."><figcaption><p>Historyczna lista dokumentów przychodzących. Przedstawiony BOD dostawcy to Sync.RemitToPartyMaster, bez przyrostka Data.</p></figcaption></figure>

Ten historyczny układ wykorzystuje Sync.RemitToPartyMaster, Sync.SupplierPartyMaster i Sync.PurchaseOrder. Potwierdź, które BOD są potrzebne do Twojego mapowania w DocBits; konfiguracja może różnić się w zależności od dzierżawy i funkcji.

* Sync.RemitToPartyMaster i Sync.SupplierPartyMaster

Poniższy historyczny obraz przedstawia Sync.SupplierPartyMaster. Skonfiguruj każdy wymagany BOD dostawcy z nazwą wywołania API i operacją odbioru potwierdzoną dla Twojego środowiska; druga trasa dostawcy nie jest pokazana na obrazie.

<figure><img src="https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk" alt="Historyczna karta ION API z wybraną opcją Send to API, nazwą wywołania API Sync.SupplierPartyMaster i operacją POST."><figcaption><p>Historyczna trasa SupplierPartyMaster. Obraz pokazuje jedną trasę dostawcy; potwierdź operację odbioru osobno dla każdego wymaganego BOD.</p></figcaption></figure>

* Sync.PurchaseOrder

Poniższy historyczny obraz przedstawia jedną operację odbioru zamówienia zakupu. Potwierdź jej aktualny punkt końcowy i format żądania dla Twojego środowiska.

<figure><img src="https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4" alt="Historyczna karta ION API z wybraną opcją Send to API dla Sync.PurchaseOrder i operacją POST."><figcaption><p>Historyczna trasa PurchaseOrder. Stara ścieżka pośrednicząca API Gateway jest przykładem, a nie uniwersalnym adresem DocBits.</p></figcaption></figure>

Po skonfigurowaniu tych BOD możesz zapisać punkt połączenia, naciskając ikonę znajdującą się po prawej stronie przycisku powrotu.

## **Przepływ danych**

Ten historyczny przepływ danych jest jednym z możliwych rozwiązań; sprawdź jego trasy i organizację odbierającą w swojej dzierżawie.

<figure><img src="https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8" alt="Historyczny przepływ od M3 przez filtr z gałęziami Yes i No, a następnie równoległy podział do czterech węzłów API DocBits, z węzłami łączenia i końca."><figcaption><p>Historyczny przepływ. Gałąź No kończy się przed węzłami API; gałąź Yes dociera do czterech przykładowych środowisk.</p></figcaption></figure>

W tym przykładzie wiele węzłów API DocBits reprezentuje osobne środowiska. Twój projekt może się różnić; sprawdź, czy komunikaty testowe nie mogą dotrzeć do środowiska produkcyjnego.

Cztery środowiska pokazano wyłącznie jako przykład.

### **M3**

Początek przepływu danych stanowi Twoja aplikacja M3

### **Filtr**

Konfiguracja filtra wygląda następująco

<figure><img src="https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374_T2V0q__QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY" alt="Historyczny panel Filter Properties z wybraną kartą Properties oraz polami Name i Description ustawionymi na Division."><figcaption><p>Historyczna nazwa i opis filtra. Sama nazwa Division nie określa, które rekordy są filtrowane.</p></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA" alt="Historyczna karta Attributes panelu Filter Properties z atrybutami AccountingEntityID dla ChartOfAccounts, PurchaseOrder, RemitToPartyMaster i SupplierPartyMaster."><figcaption><p>Historyczne atrybuty: każdy BOD ma ścieżkę AccountingEntityID. Sprawdź ścieżkę dla każdego dokumentu w swojej dzierżawie.</p></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3_2DPj96aV0vLdZk2tzw" alt="Historyczna karta Conditions panelu Filter Properties z dokumentem ChartOfAccounts, warunkiem Not Filtered i przykładowym wyrażeniem dla AccountingEntityID_3."><figcaption><p>Historyczny przykład Conditions. Pole Used Condition ma wartość Not Filtered, mimo że podano wyrażenie; sprawdź wybrany warunek i jego działanie, zamiast zakładać, że wyrażenie jest aktywne.</p></figcaption></figure>

(Identyfikator jednostki księgowej jest oczywiście unikalny dla Twojej organizacji)

### **API DocBits**

Tutaj dodasz aplikację i wybierzesz utworzone wcześniej API DocBits

### **Dokumenty**

Wybierz dokumenty przypisane do źródła M3 i do węzłów odbierających. Potwierdź, że atrybuty filtra i trasy odbioru obejmują każdy wymagany dokument.

<figure><img src="https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY" alt="Historyczny przepływ M3 z wyróżnioną ikoną dokumentu i panelem Documents z listą Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster i Sync.SupplierPartyMaster."><figcaption><p>Historyczny wybór dokumentów dla przepływu M3. To lista dokumentów BOD, a nie konfiguracja węzła plików.</p></figcaption></figure>

## **Wyzwalanie BOD w M3**

Przejdź do aplikacji Infor M3

Otwórz kontrolkę **Search and Start** w M3, wpisz **EVS006** i potwierdź program. Użyj nawigacji obsługiwanej przez Twój klient M3.

<figure><img src="https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr_o" alt="Historyczne okno dialogowe Search and Start w M3 z wpisanym evs006 i przyciskiem OK."><figcaption><p>Historyczne wyszukiwanie programu: wpisz EVS006 w Search and Start.</p></figcaption></figure>

W EVS006 zdefiniuj nazwy BOD wymagane dla zatwierdzonego mapowania. Historyczny przykład używa SupplierPartyMaster, RemitToPartyMaster i PurchaseOrder. Przed utworzeniem definicji ładowania początkowego potwierdź ich nazwy tabel M3 w swojej wersji.

BOD noun: SupplierPartyMaster

Table: CIDMAS

BOD noun: RemitToPartyMaster

Table: CIDMAS

BOD noun: PurchaseOrder

Table: MPHEAD

Dla każdej zatwierdzonej definicji użyj czynności dodawania. Przed kontynuowaniem sprawdź firmę i dział.

<figure><img src="https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN_ZlPk3W_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k_94_pYjt6Uw" alt="Wycinek historycznego paska narzędzi EVS006 z wyróżnioną opcją Add nad pustymi polami BOD noun, BOD variant, BOD i Table."><figcaption><p>Historyczna czynność Add w EVS006. Wycinek nie pokazuje wypełnionych definicji ładowania początkowego.</p></figcaption></figure>

Po dodaniu wszystkich BOD kliknij prawym przyciskiem myszy nazwę BOD i wybierz Related → Run

<figure><img src="https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH_eIYzFj22XgFHZccEM9g2nVQ_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo" alt="Historyczne menu kontekstowe z rozwiniętą pozycją Related i wyróżnioną opcją Run; poniżej znajduje się pozycja History."><figcaption><p>Historyczna czynność Related → Run. Później użyj pozycji History, aby sprawdzić wynik ładowania początkowego.</p></figcaption></figure>

Powiązana czynność **Run** otwiera EVS007. Wybierz **Sync** tylko wtedy, gdy przepływ ION odbierający tego oczekuje. Przed ostatecznym wysłaniem sprawdź wybór i filtry; przejście do następnego ekranu nie dowodzi dostarczenia danych.

<figure><img src="https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD_ka--G1SFdzIhBAp7dq63_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA" alt="Historyczny ekran EVS007 Initial Load Job dla CIDMAS i SupplierPartyMaster ze statusem Pending, otwartym menu czasownika BOD i zaznaczoną opcją Sync, podczas gdy widoczne jest jeszcze pole Show."><figcaption><p>Historyczny wybór czasownika w EVS007 przed uruchomieniem. Obraz pokazuje oczekujące zadanie i zaznaczoną opcję Sync; nie dowodzi, że wybrano Sync ani że dane zostały zaimportowane.</p></figcaption></figure>

Powiadomienie o wysłaniu potwierdza, że zadanie zostało zlecone. W **History** w EVS006 sprawdź liczbę przetworzonych rekordów i błędy. Następnie sprawdź komunikat i miejsce docelowe w Infor ION.

## Sprawdź w DocBits

W docelowej organizacji DocBits otwórz **Ustawienia → Przetwarzanie dokumentów → Wyszukaj dane główne → Dane wejściowe BOD → Dostawca**. W polu **Szukaj według kolumny** wybierz pole identyfikatora, w polu **Szukaj Tekst** wpisz znany numer lub nazwę dostawcy i użyj lupy, aby wyszukać. Następnie otwórz **Zamówienie zakupu** i wyszukaj znany numer zamówienia zakupu; jeśli mapowanie rozdziela dane nagłówka i pozycji, sprawdź **Nagłówek Zamówienia Zakupu**. Porównaj identyfikatory i firmę ze źródłem M3. Samo udane żądanie EVS007 nie dowodzi, że dotarły wszystkie rekordy.

<figure><img src="../../../.gitbook/assets/dbdc-1141-supplier-pl-20261112.png" alt="Polski widok DocBits Wyszukaj Dane Główne z kartą Dostawca, polami Szukaj według kolumny i Szukaj Tekst oraz dziesięcioma wymyślonymi wierszami dostawców od SUP-1001 do SUP-1010."><figcaption><p>Widok dostawców w sandboxie 11.27.7 z wymyślonymi danymi przykładowymi. Wyszukaj znany identyfikator testowy i porównaj go z M3 i ION.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/dbdc-1141-purchase-order-pl-20261112.png" alt="Polski widok DocBits Wyszukaj Dane Główne z kartami Dostawca i Zamówienie zakupu, tymi samymi polami wyszukiwania i dziesięcioma wymyślonymi wierszami zamówień zakupu od PO-4500 do PO-4509."><figcaption><p>Widok zamówień zakupu w sandboxie 11.27.7 z wymyślonymi danymi przykładowymi. Wiersze nie dowodzą importu z M3.</p></figcaption></figure>

Widoki Dev w języku angielskim sprawdzono 29 października 2026 r. bez uruchamiania zadania M3, importowania pliku i zmiany danych podstawowych; w tych obrazach pominięto wiersze rekordów. Dwa polskie obrazy pochodzą z sandboxa 11.27.7 i pokazują wymyślone wiersze przykładowe zamiast rzeczywistych danych podstawowych; wskazują, gdzie sprawdzić dane, a nie że transfer został zakończony. Jeśli brakuje oczekiwanego rekordu, przed ponownym uruchomieniem sprawdź historię w EVS006, routing w ION, mapowanie BOD i organizację DocBits.
