# Dostawcy i zamówienia zakupu

## **Punkt połączenia**

Aby później utworzyć przepływ danych, konieczne będzie utworzenie punktu połączenia DocBits API.

W InforOS przejdź do ION Desk → Połącz → Punkty połączenia

![Nawigacja ION Desk z rozwiniętą grupą Connect i pozycjami Data Flows, API Flows, Mappings, Connection Points i File Templates](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH\_r3RAGOvJE6Ok67ST\_272zFfhB\_TTFYg3b-NwFq0CAv2o)

Gdy już tu dotrzesz, będziesz musiał utworzyć nowy punkt połączenia.

![Strona Connection Points w ION Desk z otwartą grupą Connect w nawigacji i ścieżką Home i Connection Points](https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE\_WQj-0ONoE7McRl-f6\_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI)

**Select API**

Nadaj punktowi połączenia nazwę i opis opisujący jego charakter i otoczenie. Na karcie Połączenie zaimportuj konto usługi utworzone dla środowiska, z którym pracujesz.

![Okno API Connection Point DocBits-DEV-Demo-Import z kartami Usage, Connection i Documents, nazwą DocBits-DEV-Demo-Import, pozycją uwierzytelniania DocBits-DEV-Demo-Import Service Account i Logical ID infor.api.docbits-dev-demo-import](https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0)

Następnie przejdź do zakładki Dokumenty. Będziesz musiał dodać następujące BOD do punktu połączenia. Nie wszystkie są niezbędne dla danych podstawowych dostawcy i zamówienia zakupu, ale będą przydatne, gdy trzeba wdrożyć inne funkcje, takie jak automatyczne rozliczanie.

![Karta Documents punktu połączenia z BOD Acknowledge.SupplierInvoice, Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster i Sync.SupplierPartyMaster oraz polem wyboru w każdym wierszu](https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8\_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8)

Na razie skupimy się tylko na niezbędnych komunikatów BOD, czyli: Sync.RemitToPartyMasterData, Sync.SupplierPartyMaster i Sync.PurchaseOrder.

* Sync.RemitToPartyMasterData and Sync.SupplierPartyMaster

Konfiguracja tych dwóch BOD powinna wyglądać podobnie do poniższej (API zmiana nazwy wywołania dla każdego)

![Konfiguracja BOD z kartami Input Document, ION API, Request Parameters, Request Body i Settings oraz polami API Call Name Sync.SupplierPartyMaster, Product DocBits-DEV i operacją POST CustomerApi/DocBits-DEV/prod/import/supplier_bod](https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ\_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU\_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk)

* Sync.PurchaseOrder

Konfiguracja tego BOD powinna wyglądać podobnie do poniższej

![Konfiguracja BOD z kartami Input Document, ION API, Request Parameters, Request Body i Settings oraz polami API Call Name Sync.PurchaseOrder, Product DocBits-DEV i operacją POST CustomerApi/DocBits-DEV/prod/import/purchase_order_bod](https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4)

Po skonfigurowaniu tych BOD-ów możesz zapisać punkt połączenia, naciskając ikonę znajdującą się tuż przy przycisku Wstecz.

## **Przepływ danych**

Przepływ danych będzie wyglądał podobnie do poniższego

![Przepływ danych w ION Desk z węzłem M3 po lewej, kilkoma węzłami DocBits o nazwach DocBits-DEV-P, DocBits-DEV-S i DocBits-DEV-D pośrodku, węzłem End i warunkiem z gałęziami Yes i No](https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd\_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8)

(Powodem istnienia wielu interfejsów API DocBits jest to, że każde połączenie reprezentuje inne znaczenie środowiska, w zależności od liczby posiadanych środowisk przepływ danych może się nieznacznie różnić)

Na potrzeby tego wyjaśnienia posłużymy się przykładem czterech oddzielnych środowisk.

### **M3**

Początek przepływu danych stanowi Twoja aplikacja M3

### **Filtr**

Konfiguracja filtra wygląda następująco

![Panel Filter Properties z kartami Properties, Attributes i Conditions oraz pustymi polami Name i Description](https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374\_T2V0q\_\_QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY)

![Panel Filter Properties z otwartą kartą Attributes i wierszami AccountingEntityID_3 dla ChartOfAccounts, AccountingEntityID dla PurchaseOrder, AccountingEntityID_1 dla RemitToPartyMaster i AccountingEntityID_2 dla SupplierPartyMaster, wszystkie typu STRING ze ścieżką DataArea/*/AccountingEntityID](https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6\_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA)

![Panel Filter Properties z otwartą kartą Conditions, dokumentem ChartOfAccounts, warunkiem Not Filtered i wierszem DIV780AAA z wyrażeniem AccountingEntityID_3 równa się 780_AAA](https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3\_2DPj96aV0vLdZk2tzw)

(Podmiot księgowy ID jest oczywiście unikalny dla Twojej organizacji)

### **API DocBits**

Tutaj dodasz aplikację i wybierzesz utworzone wcześniej DocBits API(y)

### **Pliki**

Konfiguracja powinna wyglądać następująco

![Szczegół przepływu danych z węzłem M3 po lewej, węzłem warunku i węzłami DocBits, znacznikami Start i End oraz panelem Documents z Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster i Sync.SupplierPartyMaster](https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY)

## **Wyzwalanie BOD w M3**

Przejdź do aplikacji Infor M3

W menu głównym wpisz Command + R, aby otworzyć pole wyszukiwania wiersza poleceń. Następnie wpisz evs006 i wyszukaj.

![Okno Search and Start w Infor M3 z polem wyszukiwania polecenia](https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd\_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr\_o)

Będąc na tej stronie, będziesz musiał dodać do listy SupplierPartyMaster, RemitToPartyMaster i PurchaseOrder.

BOD noun: SupplierPartyMaster

Table: CIDMAS

BOD noun: RemitToPartyMaster

Table: CIDMAS

BOD noun: PurchaseOrder

Table: MPHEAD

W każdym przypadku należy nacisnąć ikonę plusa, aby dodać go do listy.

![Nagłówek panelu EVS006 z menu ACTIONS, OPTIONS, RELATED i TOOLS oraz kolumnami BOD noun, BOD variant i BOD description](https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN\_ZlPk3W\_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k\_94\_pYjt6Uw)

Po dodaniu wszystkich komunikatów BOD kliknij prawym przyciskiem właściwy obiekt BOD i wybierz Related → Run.

![Menu Related w Infor M3 z pozycjami Drill down, Select, Run, Change, History, Copy, Delete, Display i odpowiadającymi im skrótami klawiszowymi](https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH\_eIYzFj22XgFHZccEM9g2nVQ\_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo)

Zostaniesz przeniesiony do następującego menu, gdzie będziesz musiał zmienić czasownik BOD na Sync, a następnie nacisnąć NEXT, aby uruchomić BOD.

![Panel EVS007 Initial Load Job Open z tabelą CIDMAS, BOD noun SupplierPartyMaster, numerem zadania 243249962976569068, statusem 1-Pending i BOD verb ustawionym na Sync](https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD\_ka--G1SFdzIhBAp7dq63\_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA)

Po uruchomieniu BOD otrzymasz powiadomienie potwierdzające to.

Jeśli wszystko się powiedzie, tabele dostawców i zamówień zakupu powinny być teraz dostępne w obszarze Ustawienia → Wyszukiwanie danych podstawowych.
