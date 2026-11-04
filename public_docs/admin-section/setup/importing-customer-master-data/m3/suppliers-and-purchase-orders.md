# Dostawcy i Zamówienia Zakupu

## **Punkt Połączenia**

Aby później utworzyć przepływ danych, będziesz musiał/a utworzyć punkt połączenia API DocBits.

W InforOS przejdź do ION Desk → Połącz → Punkty Połączenia

![](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH\_r3RAGOvJE6Ok67ST\_272zFfhB\_TTFYg3b-NwFq0CAv2o)

Następnie musisz utworzyć nowy punkt połączenia.

![](https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE\_WQj-0ONoE7McRl-f6\_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI)

**Wybierz API**

Nadaj punktowi połączenia nazwę i opis, który opisuje jego charakter i środowisko. W zakładce Połączenie zaimportuj konto usługi utworzone dla środowiska, z którym pracujesz.

![](https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0)

Następnie przejdź do zakładki Dokumenty. Będziesz musiał dodać następujące BOD-y do punktu połączenia, nie wszystkie są konieczne dla danych głównych dostawców i zamówień zakupu, ale będą przydatne, gdy zostaną wdrożone inne funkcje, takie jak Automatyczne Księgowanie.

![](https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8\_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8)

Na razie skupimy się tylko na koniecznych BOD-ach, czyli: Sync.RemitToPartyMasterData, Sync.SupplierPartyMaster i Sync.PurchaseOrder.

* Sync.RemitToPartyMasterData i Sync.SupplierPartyMaster

Konfiguracja tych dwóch BOD-ów powinna wyglądać podobnie do poniższej (Nazwa Wywołania API zmienia się dla każdego)

![](https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ\_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU\_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk)

* Sync.PurchaseOrder

Konfiguracja tego BOD-a powinna wyglądać podobnie do poniższej

![](https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4)

Gdy te BOD-y są skonfigurowane, możesz zapisać punkt połączenia, naciskając ikonę znajdującą się obok przycisku powrotu.

## **Przepływ Danych**

Przepływ danych będzie wyglądał podobnie do poniższego

![](https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd\_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8)

(Powód posiadania wielu interfejsów API DocBits wynika z tego, że każde połączenie reprezentuje inne środowisko, co oznacza, że w zależności od ilości środowisk, twój przepływ danych może się nieco różnić)

W celu wyjaśnienia posłużymy się przykładem posiadania czterech oddzielnych środowisk.

### **M3**

Początek przepływu danych obejmuje Twoją aplikację M3

### **Filtr**

Konfiguracja filtra wygląda następująco

![](https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374\_T2V0q\_\_QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY)

![](https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6\_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA)

![](https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3\_2DPj96aV0vLdZk2tzw)

(ID jednostki księgowej oczywiście jest unikalne dla Twojej organizacji)

### **API DocBits**

Tutaj dodasz aplikację i wybierzesz wcześniej utworzone interfejsy API DocBits
### **Pliki**

Konfiguracja powinna wyglądać następująco

![](https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY)

## **M3 BOD Wywoływanie**

Przejdź do aplikacji Infor M3

Po dotarciu do głównego menu, wpisz Command + R, aby otworzyć pole wyszukiwania wiersza poleceń. Następnie wpisz evs006 i wyszukaj.

![](https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd\_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr\_o)

Po dotarciu na tę stronę, będziesz musiał dodać SupplierPartyMaster, RemitToPartyMaster i PurchaseOrder do listy.

Rzeczownik BOD: SupplierPartyMaster

Tabela: CIDMAS

Rzeczownik BOD: RemitToPartyMaster

Tabela: CIDMAS

Rzeczownik BOD: PurchaseOrder

Tabela: MPHEAD

Dla każdego przypadku będziesz musiał nacisnąć ikonę plus, aby dodać je do listy.

![](https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN\_ZlPk3W\_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k\_94\_pYjt6Uw)

Po dodaniu każdego z BOD, kliknij prawym przyciskiem myszy na rzeczownik BOD danego BOD i wybierz Powiązane → Uruchom

![](https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH\_eIYzFj22XgFHZccEM9g2nVQ\_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo)

Zostaniesz przeniesiony do następnego menu, gdzie będziesz musiał zmienić czasownik BOD na Synchronizuj, a następnie naciśnij DALEJ, aby wywołać BODs.

![](https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD\_ka--G1SFdzIhBAp7dq63\_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA)

Po wywołaniu BODs, otrzymasz powiadomienie potwierdzające to.

Jeśli wykonano pomyślnie, tabele Dostawcy i Zamówienia zakupu powinny teraz być dostępne w Ustawienia → Wyszukiwanie danych podstawowych.
