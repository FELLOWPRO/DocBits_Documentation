# Informacje o wersji

## **Release HotFix 2 31 marca 2026**

### Ulepszenia DocBits:

* **Hybrydowe przetwarzanie PDF — Ekstrakcja XML kontrolowana przez użytkownika:**\
  Gdy PDF zawiera osadzone dane XML, użytkownicy mogą teraz wybrać, czy DocBits powinien użyć osadzonego XML do ekstrakcji, czy przetworzyć dokument jako standardowy PDF. Daje to organizacjom pełną kontrolę nad sposobem obsługi dokumentów hybrydowych, zapewniając zastosowanie metody ekstrakcji najlepiej dopasowanej do ich przepływu pracy.

* **AP Assignment Code na ekranie Approval:**\
  Strona AP Manager Approval zawiera teraz pole AP Assignment Code, zintegrowane z Infor M3 CRS620. Umożliwia to osobom zatwierdzającym przeglądanie i potwierdzanie kodów przypisania bezpośrednio podczas procesu zatwierdzania bez przełączania się do systemów zewnętrznych.

* **Dopasowanie sumy PO z sumą dokumentu:**\
  DocBits obsługuje teraz porównywanie sumy zamówienia zakupu z sumą na dokumencie, zapewniając dodatkową warstwę walidacji podczas PO Matching w celu wcześniejszego wykrywania rozbieżności w procesie.

* **Aktualizacja numeru artykułu dostawcy i VPE:**\
  DocBits obsługuje teraz aktualizację pól numer artykułu dostawcy i VPE (Verpackungseinheit / jednostka opakowaniowa) podczas przetwarzania dokumentów, z synchronizacją wartości z powrotem do M3 podczas eksportu.

* **Ulepszona klasyfikacja layoutu dokumentu:**\
  Identyfikator layoutu dokumentu (tfidf_id) jest teraz generowany wyłącznie na podstawie tekstu nagłówka, z wykluczeniem tekstu stopki. Poprawia to dokładność klasyfikacji, zapobiegając wpływowi treści stopki na wykrywanie typu dokumentu.

* **Przycisk Export & Next:**\
  Dodano nowy przycisk "Export & Next", umożliwiający użytkownikom eksport bieżącego dokumentu i natychmiastowe przejście do następnego w kolejce, usprawniając przepływ pracy przeglądania i eksportu.

* **Proces zatwierdzania faktur kosztowych:**\
  Proces zatwierdzania faktur kosztowych został ulepszony dzięki zoptymalizowanej logice routingu i walidacji.

### Poprawki błędów:

* Naprawiono problem, w którym eksport Infor SFTP kończył się błędem z powodu nieprawidłowego polecenia biblioteki.
* Naprawiono problem, w którym pola wyboru typu boolean nie mogły być wyświetlane na ekranie zatwierdzania.
* Naprawiono problem, w którym wiadomości UNMU były wysyłane nawet gdy nie było rozbieżności w jednostce zakupu.
* Naprawiono problem, w którym podatek od sprzedaży był nieprawidłowo klasyfikowany jako opłata na ekranie PO Matching, co skutkowało ujemną kwotą nierozliczoną.
* Naprawiono problem, w którym eksport kończył się niepowodzeniem, gdy jednostka zakupu nie była ustawiona w potwierdzeniu zamówienia, ale była obecna w zamówieniu zakupu.
* Naprawiono problem, w którym treść e-maila brakowała dla kilku dokumentów.
* Naprawiono problem, w którym numer artykułu dostawcy nie był widoczny na ekranie zatwierdzania, a aktualizacje nie były wysyłane do M3.
* Naprawiono problem, w którym eksport dostawców do Infor zwracał błąd.
* Naprawiono problem, w którym PO Matching generował błędy podczas przetwarzania.
* Naprawiono problem, w którym funkcja `findAll` nie działała poprawnie w skryptach dokumentów.
* Naprawiono problem, w którym kolumna "Updated By" w Watchdog nieprawidłowo pokazywała użytkownika Fellow Admin zamiast rzeczywistego użytkownika.
* Naprawiono problem, w którym BOD-Mapping nie mógł być konfigurowany w interfejsie Watchdog.
* Naprawiono problem, w którym opłaty były nieprawidłowo wyświetlane jako kwoty nierozliczone zamiast jako opłaty.
* Naprawiono problem, w którym automatyczne dopasowywanie nie działało dla faktur wieloliniowych pomimo posiadania konfiguracji dopasowania.
* Naprawiono problem, w którym myślnik ("-") w numerze artykułu był uwzględniany podczas PO Matching dla zamówienia zakupu, ale ignorowany na fakturze, powodując fałszywą rozbieżność.
* Naprawiono problem, w którym zarówno pliki PDF, jak i XML były przesyłane do folderu eksportu nawet gdy przełącznik "Export PDF" był wyłączony.
* Naprawiono problem, w którym brakujący status na karcie workflow uniemożliwiał dokumentom przechodzenie przez przepływ pracy.
* Naprawiono problem, w którym jakość dokumentu była znacząco pogorszona po imporcie.
* Naprawiono problem, w którym ekran PO Match generował błąd ("Cannot read properties of null").
* Naprawiono problem, w którym domyślna lista wartości nie mogła być edytowana.
* Naprawiono problem, w którym workflow nie mógł prawidłowo odczytać statusu pola, powodując nieprawidłowy routing.
* Naprawiono problem, w którym import przychodzących e-maili kończył się błędem.
* Naprawiono problem, w którym brakujące linie nie docierały prawidłowo do M3 podczas eksportu.
* Naprawiono problem, w którym zakodowane i zatwierdzone faktury sporadycznie nie były aktualizowane do statusu "zatwierdzone" w M3 przez API APS110.
* Naprawiono problem z konfiguracją Multi Banking, która nie działała prawidłowo.
* Naprawiono wiele problemów z wyświetlaniem i zachowaniem zapisu udostępnionych dashboardów.
* Naprawiono problem, w którym pole numer artykułu dostawcy było ograniczone do 30 znaków, uniemożliwiając przechowywanie dłuższych wartości.
* Naprawiono problem, w którym wartości ceny jednostkowej i ceny jednostkowej za jednostkę powodowały błąd podczas eksportu.
* Naprawiono problem, w którym linie PO z wykluczonym statusem (np. "Closed") nadal mogły być przeciągane i dopasowywane na ekranie PO Matching pomimo wykluczenia przez reguły dopasowania.

### Zmiany konfiguracji:

* Zaktualizowano szablony e-mail, usuwając przycisk "Go to Task".
* Dostosowano skrypty i ustawienia pól obowiązkowych dla elementów kosztowych.

## **Release HotFix 1 16 marca 2026**

### Ulepszenia DocBits:

* **Historia dokumentów w eksporcie SFTP:**\
  DocBits obsługuje teraz dołączanie pełnej historii dokumentu jako części eksportowanego ładunku XML podczas eksportu do SFTP. Funkcja ta jest konfigurowalna w Export Settings i zapewnia systemom downstream pełny ślad audytu każdej zmiany statusu i akcji wykonanej na dokumencie w DocBits — w tym kto dokonał zmiany, kiedy nastąpiła oraz jakie były poprzedni i bieżący status. Jest to szczególnie wartościowe dla zgodności, identyfikowalności i analizy operacyjnej.
* **Aktualizacja opłat w potwierdzeniu zamówienia dla Infor On Premise:**\
  Klienci Infor On Premise mogą teraz przetwarzać potwierdzenia zamówień zawierające opłaty bezpośrednio w DocBits. Opłaty są w pełni aktualizowane poprzez eksport, dzięki czemu kompleksowy proces potwierdzania zamówień jest płynny i eliminuje potrzebę ręcznych korekt w systemach downstream.
*   **Zastosuj domyślny Layout do wszystkich Origins:**\
    Nowy przycisk **Apply Default Layout to Origins** został wprowadzony na ekranie konfiguracji layoutu. Administratorzy mogą teraz przekazać domyślny layout do wszystkich origins w organizacji jedną akcją, eliminując czasochłonny ręczny proces kopiowania i wklejania JSON layoutu dla każdego origin osobno. Jest to szczególnie przydatne podczas wdrażania nowych klientów, gdzie wiele origins musi być skonfigurowanych spójnie.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(5).png)
*   **Wybór typu dokumentu dla importu FTP:**\
    Konfiguracje importu FTP obsługują teraz przypisywanie typu dokumentu na poziomie folderu. Podczas konfigurowania importu FTP użytkownicy mogą określić, jaki typ dokumentu — taki jak Faktura lub Potwierdzenie Zamówienia — powinien być stosowany do wszystkich dokumentów importowanych z danego folderu. Dokumenty są automatycznie klasyfikowane przy imporcie, eliminując potrzebę ręcznego przypisywania typu dokumentu po pozyskaniu. Wspiera to organizacje zarządzające wieloma typami dokumentów w różnych podorganizacjach i folderach.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(4).png)
* **Eksport do GLS840 dla Infor On Premise:**\
  DocBits obsługuje teraz eksport dokumentów do programu GLS840 dla klientów Infor On Premise, rozszerzając zakres obsługiwanych celów eksportu dla środowisk on-premise.
*   **Ulepszenia interfejsu dla Watchdog i konfiguracji eksportu:**\
    Ekrany konfiguracji Watchdog i konfiguracji eksportu zostały odświeżone z ulepszonym interfejsem użytkownika, oferując czystszy układ i bardziej intuicyjne doświadczenie dla administratorów zarządzających tymi ustawieniami.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(1).png)

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(2).png)

### Poprawki błędów:

* Naprawiono problem, w którym użytkownicy z ważnymi uprawnieniami do przeglądania nie mogli wyświetlać dokumentów — logika uprawnień została przebudowana z kontrolą poziomu dostępu zastępującą poprzednie podejście filtrowania opartego na grupach.
* Poprawiono obsługę wyjątków w wielu obszarach aplikacji dla większej stabilności.
* Rozwiązano problem, w którym kolumny typu boolean nie były prawidłowo obsługiwane podczas ekstrakcji pól.
* Naprawiono problem z asynchroniczną autentykacją w endpoincie przesyłania plików.
* Rozwiązano problemy z wyświetlaniem interfejsu dla tabeli PO na ekranie walidacji.
* Zaktualizowano szablon skryptu o komentarze śledzenia zmian dla lepszej możliwości audytu.
* Naprawiono problem z polami rozwijanymi, które nie zachowywały się prawidłowo na ekranie walidacji.
* Naprawiono problem, w którym pole podorganizacji nie było wstępnie wypełniane podczas aktualizowania przypisań dokumentów z dashboardu.

## **Wydanie Winter Summit 10 grudnia 2025**

### Ulepszenia DocBits:

*   **Ulepszona personalizacja reguł dopasowania zamówień:**\
    DocBits zapewnia teraz bardziej szczegółową i konfigurowalną kontrolę nad regułami dopasowania zamówień zakupu. Administratorzy mogą precyzyjnie skonfigurować, które kolumny powinny być oceniane podczas procesu dopasowania dla każdego typu dokumentu, zapewniając, że brane są pod uwagę tylko najbardziej istotne pola. Ponadto tolerancje mogą być definiowane na poziomie kolumny, co pozwala na większą elastyczność w obsłudze drobnych rozbieżności. Każda reguła może być również skonfigurowana tak, aby dotyczyła dopasowania ręcznego, dopasowania automatycznego lub obu, dając zespołom możliwość dostosowania przepływu pracy dopasowania do ich dokładnych wymagań operacyjnych. Te ulepszenia znacząco poprawiają adaptowalność i precyzję procesu dopasowania zamówień zakupu.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_3.png)
*   **Wsparcie dla wielu kont finansowych dostawców:**\
    DocBits obsługuje teraz zarządzanie wieloma kontami finansowymi dla dostawców za pośrednictwem RemitToPartyMaster BOD dostarczonego przez Infor. To ulepszenie umożliwia organizacjom utrzymywanie kilku rekordów kont płatności dla jednego dostawcy, poprawiając elastyczność i dokładność przetwarzania płatności. Wprowadzono nowe ustawienie konfiguracyjne umożliwiające włączenie lub wyłączenie tej funkcji, pozwalając administratorom aktywować funkcjonalność w oparciu o ich potrzeby operacyjne.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_1.png)
*   **Dodano dostęp użytkowników do wyników ekstrakcji OCR:**\
    Przycisk **Widok OCR** na ekranie walidacji pól jest teraz dostępny dla wszystkich użytkowników, którzy mają dostęp do walidacji, zamiast być ograniczonym tylko do administratorów. Dzięki tej aktualizacji każdy autoryzowany użytkownik może bezpośrednio przeglądać wyniki ekstrakcji OCR, ułatwiając walidację dokładności danych i monitorowanie ogólnej wydajności OCR. To ulepszenie promuje większą przejrzystość i poprawia efektywność przepływu pracy walidacji.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_2.png)
* **Dynamiczne renderowanie kolumn na ekranach zatwierdzania:**\
  Ulepszone widoki zatwierdzania, aby dynamicznie wyświetlać tylko kolumny skonfigurowane do porównania w preferencjach bazy danych każdej organizacji. Wcześniej niektóre kolumny specyficzne dla organizacji pojawiały się puste, gdy nie były skonfigurowane do porównania, powodując zamieszanie. Teraz widoki zatwierdzania pokazują tylko pola, które są aktywnie porównywane. Zapewnia to jaśniejsze, specyficzne dla organizacji ekrany zatwierdzania bez pustych lub nieistotnych kolumn.
* **Pole typu zamówienia dodane do wyszukiwania danych głównych**:\
  Lista nagłówków zamówień zakupu zawiera teraz kolumnę "Order Type" w wyszukiwaniu danych głównych, zapewniając dodatkowe możliwości kategoryzacji.
* **Ulepszenia panelu filtrów niestandardowych:**\
  Funkcjonalność udostępniania pulpitu została ulepszona, aby zapewnić większą elastyczność użytkownikom, którym udostępniono pulpit. Osoby, którym udostępniono pulpity, mogą teraz dostosowywać i edytować filtry pulpitu, umożliwiając im dostosowanie wyświetlanych informacji do ich konkretnych potrzeb. To ulepszenie wspiera bardziej spersonalizowane i interaktywne doświadczenie przeglądania, zapewniając, że użytkownicy mogą łatwo udoskonalać informacje o danych najbardziej istotne dla ich zadań.
* **Konfigurowalne prefiksy dla kolumn ekranu zatwierdzania:**\
  Wprowadzono nową konfigurowalną opcję wyświetlania prefiksów przed kolumnami dokumentów na ekranach zatwierdzania. Ta funkcja może być zarządzana bezpośrednio w konstruktorze układu, dając administratorom pełną kontrolę nad tym, czy prefiksy są wyświetlane i do jakich typów dokumentów mają zastosowanie. Włączając tę opcję, użytkownicy uzyskują jaśniejszy kontekst i lepszą czytelność podczas przeglądania dokumentów w procesie zatwierdzania.

### Ogólne ulepszenia

* Ulepszone rejestrowanie błędów dla źle wyszkolonych tabel w ekstrakcji tabel.
* Dodano limit udostępniania dla paneli do 10 użytkowników lub 5 grup, wraz z wyraźnym komunikatem o błędzie po osiągnięciu limitu.
* Ulepszona obsługa błędów dla niestandardowych paneli, gdy użytkownik próbuje utworzyć panel z nazwą, która już istnieje.

### Poprawki Błędów:

* Naprawiono problem, w którym e-maile wydawały się być wysyłane pomyślnie z sekcji Szczegóły Dostawcy, ale nie były dostarczane do odbiorców.
* Naprawiono problem, w którym pola rozwijane dodane do ekranów zatwierdzania/odrzucania nie były wyświetlane.
* Naprawiono problem, w którym wszystkie eksportowane dokumenty były oznaczone jako ostatnio zaktualizowane przez niewłaściwego użytkownika.
* Naprawiono problem, w którym dokumenty pokazywały status "Workflow w toku", ale nie wykonywały się żadne workflow, a dziennik pozostawał pusty.
* Naprawiono problem, w którym niepowiązani użytkownicy byli przypisywani do dokumentów w momencie eksportu bez wykonywania jakiejkolwiek pracy nad nimi.
* Naprawiono problem, w którym użytkownicy z poprawnymi uprawnieniami nie mogli odrzucić przypisanych dokumentów i otrzymywali błędy.
* Naprawiono problem, w którym ikony przepływu dokumentów nie były wyświetlane dla niektórych organizacji.
* Naprawiono problem, w którym pojawiało się okienko pop-up podczas przesyłania dokumentów metodą przeciągnij i upuść na pulpit.
* Naprawiono problem, w którym flagi E-TEXT były wyświetlane jako włączone w interfejsie użytkownika, mimo że odpowiedź API pokazywała wszystkie wartości jako fałszywe.
* Naprawiono problem, w którym występował błąd podczas przesyłania dokumentów zawierających puste strony.
* Rozwiązano problem, w którym hiperłącza zadań w powiadomieniach e-mail nie przekierowywały użytkowników na właściwy ekran zatwierdzania.
* Rozwiązano problem, w którym wybranie podorganizacji cross powodowało, że Wyszukiwanie Danych Głównych nie pokazywało żadnych dostawców. Użytkownicy mogą teraz poprawnie przeglądać dane dostawców międzyorganizacyjnych.

## Release Autumn Summit 22 października 2025

### Usprawnienia DocBits:

*   #### Usprawnienia Projektowania Szablonów Email:

    Edytor szablonów email został przeprojektowany, aby zapewnić klarowną strukturę i płynniejsze doświadczenie. Wybieranie pól dokumentów jest teraz bardziej intuicyjne, a załączniki można teraz dołączać bezpośrednio do szablonów. Te usprawnienia sprawiają, że tworzenie profesjonalnych, spersonalizowanych wiadomości e-mail jest szybsze i łatwiejsze.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fdv4oDlfkRyD0W9yWGAA4%252Fimage.png%3Falt%3Dmedia%26token%3D14bf7ebd-d886-4758-8184-d7b94447518a\&width=768\&dpr=4\&quality=100\&sign=88405d9c\&sv=2)
*   #### Usprawnienia Panelu:

    Panel został rozszerzony, aby poprawić nawigację i dostosowanie. Dzięki nowym zakładkom użytkownicy mogą szybciej przełączać się między różnymi typami dokumentów, skracając czas spędzony na szukaniu odpowiedniego widoku.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmpO7WSIrkL0I8Rje3HQt%252Fimage.png%3Falt%3Dmedia%26token%3D77d03fe7-e626-4645-b191-e332715a25fb\&width=768\&dpr=4\&quality=100\&sign=93fa9925\&sv=2)
*   #### Niestandardowe Filtry Paneli:

    Ponadto panele można teraz dostosowywać i filtrować zgodnie z indywidualnymi preferencjami. Te niestandardowe panele można również udostępniać współpracownikom, ułatwiając tworzenie spójnych widoków raportowania dla całego zespołu.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn5rPvGnRltT3mTIDoJwV%252Fimage.png%3Falt%3Dmedia%26token%3D22d065e3-81eb-4f16-828c-7f9134c25b1b\&width=768\&dpr=4\&quality=100\&sign=eb11d3a3\&sv=2)
*   #### Logi Powiadomień Email:

    Dostępna jest nowa funkcja logowania dla wszystkich powiadomień email. Użytkownicy mogą teraz przejrzeć historię wysłanych powiadomień, co ułatwia weryfikację dostaw i rozwiązywanie problemów, jeśli wiadomości nie zostały odebrane.
*   #### Wsparcie dla Faktur Elektronicznych: e-SLOG 1.6 & 2.0:

    Wprowadzono obsługę dodatkowych formatów faktur elektronicznych. System może teraz przetwarzać i generować wersje e-SLOG 1.6 i 2.0, poszerzając zgodność z partnerami i wymaganiami regulacyjnymi.
*   #### Usprawnienia Wykrywania Duplikatów:

    Wykrywanie duplikatów zostało ulepszone dzięki dwóm potężnym opcjom konfiguracji. **Interwał Wykrywania Duplikatów** pozwala zdefiniować zakres czasowy w celu dokładniejszego sprawdzania duplikatów, podczas gdy ustawienie **Zabronić Eksportu Duplikatów** automatycznie uniemożliwia eksport dokumentów uznanych za duplikaty. Te usprawnienia zapewniają większą kontrolę i zapewniają wyższą dokładność danych.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXHRKTmuSxTlDt9lDEkE7%252Fimage.png%3Falt%3Dmedia%26token%3D96b56af6-c644-4b0f-a488-8bc16a03c11f\&width=768\&dpr=4\&quality=100\&sign=9b723b7f\&sv=2)
*   #### Usprawnienia Drzew Decyzyjnych:

    Drzewa decyzyjne są teraz bardziej wszechstronne, umożliwiając zwracanie wartości pól dokumentów. Pozwala to na bardziej zaawansowaną logikę automatyzacji, umożliwiając przeprowadzanie decyzji na podstawie rzeczywistych danych dokumentów.
*   #### Nowe Karty Przepływu Roboczego:

    Dwie nowe karty przepływu roboczego poszerzają możliwości automatyzacji. Pierwsza pozwala sprawdzić, czy dokument należy do określonej podorganizacji, ułatwiając obsługę konfiguracji wielu jednostek. Druga wprowadza sprawdzenie tolerancji daty dostawy, porównując daty dostawy z bieżącą datą w dniach roboczych, aby pomóc lepiej zarządzać i egzekwować wymagania dotyczące dostawy.
*   #### Usprawnienia Eksportu CSV:

    Funkcja eksportu CSV została znacząco ulepszona. Zamiast eksportować tylko dokumenty wyświetlane na bieżącej stronie, system teraz eksportuje wszystkie dokumenty w zestawie danych. Każdy eksport tworzy wpis w dzienniku, a wynikowy plik CSV jest automatycznie wysyłany pocztą elektroniczną, zapewniając bardziej kompletny i niezawodny proces eksportu.
*   #### Ramy Czasowe Usuwania Zamówienia Zakupu:

    Nowa opcja konfiguracji pozwala administratorom zdefiniować ramy czasowe dla usuwania zamówienia zakupu. To usprawnienie dodaje elastyczność i kontrolę nad politykami retencji danych, zapewniając, że zamówienia zakupu są usuwane tylko w odpowiednim momencie.

### Poprawki Błędów

* Naprawiono problem, w którym stare dane były uwzględniane podczas eksportowania dokumentów.
* Poprawiono filtr dla Błędów Eksportu, który wcześniej pokazywał również inne statusy.
* Rozwiązano niezgodność walidacji tabeli, gdzie "Cena Jednostkowa" powodowała błędy, ale "Cena Jednostkowa Za" nie, mimo że wartości były poprawne.
* Naprawiono problem, w którym dodanie nowej kolumny do panelu nie powiodło się.
* Poprawiono problem, w którym zadania nie były widoczne w kolumnie zadań panelu.
* Naprawiono losowe zachowanie sortowania, dzięki czemu listy teraz podążają za spójnym porządkiem.
* Rozwiązano problem, w którym zmiana rozmiaru kolumny nie mogła zostać zatrzymana.
* Naprawiono błąd uniemożliwiający ręczne dopasowanie linii w ekranie Dopasowywania PO.
* Poprawiono problem, w którym opcja załącznika email została zresetowana po zapisaniu.
* Naprawiono problem, w którym początkowo wyświetlane były identyfikatory bazy danych w automatycznym rozliczaniu.
* Poprawiono zachowanie pola rozmytego, dzięki czemu wartości nie są już niewłaściwie nadpisywane.
* Naprawiono problem, w którym pola w automatycznym rozliczeniu zniknęły po usunięciu zawartości.
* Poprawiono błąd, w którym użytkownik nie mógł zmienić nazwy "Imię" i "Nazwisko" w oknie dialogowym ustawień.
* Rozwiązano problem, w którym dokumenty mogły utknąć w "przepływie roboczym w toku".
* Naprawiono problem z kolorem ikony menu, gdzie wybrane kolory organizacji nie były poprawnie stosowane.
* Poprawiono problem, w którym czasami kody QR nie były rozpoznawane.
* Naprawiono problem, w którym konta nie mogły być usunięte za pomocą klawisza backspace do wprowadzenia innego.
* Rozwiązano problem z mieszanym językiem po zalogowaniu się po wdrożeniu produkcji.

## Wydanie Spring Bloom – 23 kwietnia 2025

### Ulepszenia DocBits:

* **Opcja filtrowania dla dziennika importu e-maili:** Użytkownicy mają teraz możliwość filtrowania dzienników importu i sortowania tabeli, co zapewnia jaśniejszy i bardziej efektywny przegląd. To ulepszenie usprawnia proces identyfikacji i zarządzania wpisami e-mail, poprawiając rozwiązywanie problemów i ogólne zarządzanie dziennikami.
* **Wsparcie wielojęzyczne dla Listy Wartości:** Rozszerzyliśmy możliwości wielojęzyczne dla funkcji Listy Wartości. Administratorzy mogą teraz definiować etykiety w wielu językach, zapewniając, że odpowiednia etykieta jest automatycznie wyświetlana w zależności od ustawień językowych systemu użytkownika. To ulepszenie promuje większą dostępność i lokalizację, ułatwiając użytkownikom na całym świecie interakcję z platformą w ich rodzimym języku.
* **Ulepszenia szczegółów użytkownika w ustawieniach:** Interfejs ustawień teraz wyświetla kompleksowe informacje o użytkownikach. Administratorzy mogą łatwo przeglądać przynależności do grup, szczegóły podorganizacji i dodatkowe kluczowe dane, co umożliwia lepsze zarządzanie rolami użytkowników i jaśniejsze zrozumienie struktur zespołowych.
* **Informacje o automatycznym księgowaniu na ekranie zatwierdzania:** Ekran zatwierdzania teraz prezentuje szczegóły automatycznego księgowania obok informacji o fakturze. To ulepszenie zapewnia głębszy wgląd w dane transakcyjne, ułatwiając płynniejsze procesy przeglądowe i bardziej świadome podejmowanie decyzji dotyczących faktur.
* **Licznik zadań dla dokumentów w widoku pulpitu:** Dokumenty na pulpicie mogą teraz wskazywać otwarte zadania związane z nimi oraz wyświetlać łączną liczbę oczekujących zadań. Ta funkcja zapewnia użytkownikom szybki przegląd zaległych działań, poprawiając zarządzanie zadaniami i efektywność przepływu pracy.
* **Wybór modelu AI opartego na dostawcy:** Użytkownicy mogą teraz wybierać model AI używany do ekstrakcji danych na podstawie dostawcy. To ulepszenie pozwala na precyzyjną optymalizację, zapewniając lepszą dokładność ekstrakcji dla różnych dostawców i poprawiając ogólne wyniki przetwarzania danych.
* **Ulepszone dzienniki przepływu pracy dla kart drzewa decyzyjnego:** Dzienniki teraz wyświetlają wyniki drzewa decyzyjnego, co ułatwia śledzenie i zrozumienie, jak podejmowane były decyzje w ramach przepływów pracy.
*   **Wprowadzenie nowego ustawienia automatycznego testowania w celu poprawy funkcjonalności i stabilności systemu:**

    Z radością ogłaszamy wdrożenie nowego systemu automatycznego testowania, zaprojektowanego w celu poprawy ogólnej funkcjonalności i niezawodności naszej platformy. To nowe ustawienie będzie przeprowadzać regularne, dokładne kontrole naszego systemu, aby zidentyfikować wszelkie problemy, zanim wpłyną na Twoje doświadczenia. Automatyzując te testy, możemy zapewnić szybsze reakcje na potencjalne problemy i utrzymać najwyższe standardy jakości naszego systemu.

    ​

### Poprawki błędów

* Rozwiązano problem, w którym zadania nie pojawiały się na ekranie walidacji/zatwierdzania.
* Naprawiono pozycjonowanie przycisku Następny/Poprzedni, aby pozostał statyczny.
* Naprawiono problemy z przewijaniem w widokach skryptu i drzewa decyzyjnego, zapewniając, że przyciski akcji pozostają nieruchome podczas przewijania.
* Usunięto pole kraju pochodzenia z e-faktur.
* Naprawiono problem z licznikiem zadań wyświetlającym nieprawidłową liczbę zadań.
* Dodano brakujące tłumaczenia.
* Skorygowano pola niestandardowe, aby wyświetlały opisowe nazwy zamiast identyfikatorów.
* Zaktualizowano listę skrótów dla ekranu dopasowywania zamówień.
* Rozwiązano problem, w którym dokumenty były pobierane z nieprawidłową nazwą pliku.
* Naprawiono niespójności sortowania w tabeli linii faktury w ramach dopasowywania zamówień.
* Naprawiono problem wpływający na funkcjonalność tworzenia zadań.
* Naprawiono problem w dopasowywaniu zamówień, w którym sortowanie tabeli faktur resetowało się podczas dopasowywania linii.
* Rozwiązano problemy z automatycznym księgowaniem, zapewniając, że odniesienia do rezerwacji są poprawnie dzielone, gdy kwota jest dzielona.
* Zaktualizowano informacje o hoście ClickHouse.
* Rozwiązano problem, w którym zduplikowane dokumenty nie były rozpoznawane jako duplikaty.
* Naprawiono problemy z eksportem spowodowane zbyt długimi odniesieniami do rezerwacji.
* Rozwiązano problem, w którym pola wyboru tylko do odczytu nie były tylko do odczytu.
* Naprawiono problem, w którym użytkownicy mogli być dodawani do podorganizacji dwukrotnie.
* Naprawiono problem, w którym zmiana podorganizacji dla dokumentu powodowała zresetowanie przypisanego użytkownika lub grupy.

​

## Wydanie Hot Fix Winter Frost 10 kwietnia 2025

### Ulepszenia DocBits:

* **Ulepszona** **`set_column_date_value`** **Funkcja Skryptu:** Funkcja `set_column_date_value` teraz obsługuje opcję `skip_weekend`, co pozwala na automatyczne pomijanie weekendów przy stosowaniu wartości daty.
* **Poprawione wsparcie dla przesyłania plików:** Pliki PNG i JPEG mogą teraz być przesyłane bezpośrednio i są automatycznie konwertowane na format PDF w celu uproszczenia obsługi dokumentów.
* **Ulepszenia funkcjonalności Watchdog:**
  * Teraz obsługuje eksport do **Enaio** dla lepszej integracji systemowej.
  * Ulepszone możliwości analizy w celu wydobywania informacji z struktur XML `Sync.ContentDocument`, co umożliwia bardziej efektywne przetwarzanie danych.

### Poprawki błędów

* Naprawiono problem z funkcją skryptu.
* Rozwiązano problem, w którym zamówienia zakupu miały błędny status po ich aktualizacji.

## Wydanie Hot Fix Winter Frost 11 marca 2025

### Ulepszenia DocBits:

* **Ulepszona ekstrakcja danych:** Dodano opcję ekstrakcji **Zamówienia Zakupu** lub **Numeru Przedmiotu** z linii powyżej lub poniżej.
* **Rozszerzony dostęp do podorganizacji:** Użytkownicy niebędący administratorami mogą teraz również uzyskać dostęp do funkcji **Cross Sub-Organizations**.

### **Poprawki błędów:**

* Naprawiono problem, w którym użytkownicy nie mogli zostać dodani do grupy.
* Naprawiono problem z niepowodzeniami importu e-maili.
* Rozwiązano problem z treningiem w terenie na dokumentach z więcej niż jedną stroną.
* Naprawiono problem, w którym skrypty nie działały poprawnie.
* Rozwiązano problem, w którym dane dokumentu nie były wyświetlane poprawnie.
* Naprawiono problem z ustawieniem automatycznej aktualizacji zamówienia zakupu.
* Naprawiono problem, w którym tokeny subskrypcyjne były wyświetlane nieprawidłowo.
* Rozwiązano problem, w którym ekran zadań wyświetlał nieaktualną wersję dokumentu.
* Naprawiono problem, który powodował, że dokumenty nie zmieniały swojego statusu.
