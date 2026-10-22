# Operator DocBits

## Przegląd

**DocBits Operator** to asystent automatyzacji zasilany sztuczną inteligencją, zaprojektowany do upraszczania powtarzalnych zadań w Twoich procesach. Użytkownicy tworzą _prompty_ — instrukcje krok po kroku wzbogacone o zmienne — które prowadzą AI do nawigowania, wprowadzania danych i automatycznego klikania w interfejsach. Zmniejsza to nakład pracy ręcznej i przyspiesza rutynowe operacje.

## Włączanie DocBits Operator

Aby włączyć DocBits Operator, wykonaj następujące kroki:

1. **Przejdź do ustawień**:
   * Z Dashboard przejdź do **Settings**.
   *   Wybierz **Document Processing**, a następnie **Module**.

       <figure><img src="../../.gitbook/assets/site-extra-modules-document-integration-pl.png" alt="Moduły integracji dokumentów: skrypty, skanowanie, kody kreskowe i niestandardowe dane podstawowe. W przedstawionej wersji etykieta wyboru kodów kreskowych „Select” pozostaje angielska."><figcaption><p>Moduły integracji dokumentów: skrypty, skanowanie, kody kreskowe i niestandardowe dane podstawowe. W przedstawionej wersji etykieta wyboru kodów kreskowych „Select” pozostaje angielska.</p></figcaption></figure>
2. **Włącz funkcję**:
   * Przewiń w dół, aby znaleźć opcję **DocBits Operator**.
   *   Przełącz suwak, aby włączyć **DocBits Operator**.

       <div align="left"></div>

## Dostęp do interfejsu

* Po włączeniu funkcji otwórz **DocBits Operator** z głównego menu nawigacji.

### **1. Wprowadzanie promptu**

Na dole ekranu znajduje się pole do wpisania polecenia. Tutaj użytkownicy wpisują instrukcje, które ma wykonać operator.

Obok pola wprowadzania znajduje się kilka przycisków sterujących:

* **Prompt Variables** – Otwiera okno, w którym można wprowadzić pary klucz-wartość używane w prompcie. Zmienne zapisuje się w nawiasach klamrowych, na przykład `{invoice_number}` lub `{url}`. Wartości te dotyczą tylko bieżącego promptu w polu wprowadzania.
* **Save Prompt** – Zapisuje bieżący prompt. Możesz zapisać go jako:
  * **Organization Prompt** – Edytowalny w obrębie Twojej organizacji; zawiera zarówno prompt, jak i zdefiniowane wartości zmiennych.
  * **Global Prompt** – Współdzielony przez wszystkich najemców; zawiera tylko prompt i symbole zastępcze zmiennych (wartości nie są zapisywane).
* **Clear Chat** – Czyści bieżącą rozmowę z operatorem, ale pozostawia prompt w polu wprowadzania bez zmian. Przydatne przy ponownym użyciu lub dopracowywaniu promptu.

Szczegółowe wskazówki dotyczące pisania skutecznych promptów — w tym składnię, zmienne i przykłady — znajdziesz w [**Przewodniku po pisaniu promptów**](prompt-writing-guide.md).

### **2. Nawigacja na pasku bocznym**

Użyj ikony w lewym górnym rogu, aby otworzyć lub zamknąć pasek boczny. Pasek boczny pokazuje zapisane prompty, uporządkowane w dwóch kategoriach:

* **Organization Prompts**: Edytowalne i wielokrotnego użytku w obrębie Twojej organizacji.
* **Global Prompts**: Współdzielone przez wszystkich najemców. Nie mogą przechowywać zmiennych i nie można ich edytować ani usuwać.
  * Globalny prompt nadal może być edytowany i usuwany przez **organizację, która go utworzyła**, gdzie jest widoczny w sekcji Organization Prompts.
* **Wyszukiwanie:** pasek wyszukiwania u góry paska bocznego pozwala szybko znaleźć zapisane prompty według nazwy lub słowa kluczowego.
* **Opis ikon:** Każdy zapisany prompt ma zestaw ikon akcji
  * **Strzałka** – Uruchom prompt
  * **Długopis** – Edytuj prompt (dostępne tylko dla promptów Twojej własnej organizacji)
  * **Kosz** – Usuń prompt (dostępne tylko dla promptów Twojej własnej organizacji)

### 3. Zapisywanie promptu

Kliknięcie przycisku **Save Prompt** otwiera okno, w którym możesz zapisać bieżący prompt do późniejszego użycia.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_notification_card_overview.png" alt="Okno Save Prompt"><figcaption></figcaption></figure></div>

#### **Pola okna Save Prompt**

* **Prompt Name:** Wpisz nazwę, która identyfikuje prompt.
* **Save Prompt Publicly (pole wyboru):** Po zaznaczeniu prompt zostanie zapisany jako **Global Prompt**. Global Prompts są współdzielone przez wszystkich najemców i nie mogą przechowywać **wartości** zmiennych (tylko **nazwy** zmiennych).
* **Edit Variables:** Otwiera [**okno Prompt Variables**](prompt-writing-guide.md#okno-dialogowe-zmiennych-polecenia), aby przejrzeć lub dostosować definicje zmiennych przed zapisaniem.

**Akcje**

* **Cancel:** Zamyka okno bez zapisywania.
* **Save:** Zapisuje prompt z użyciem podanej nazwy i ustawienia widoczności.

### 4. Elementy sterujące wykonywaniem promptu

Gdy prompt jest uruchomiony, użytkownicy mają do dyspozycji kilka opcji sterowania procesem wykonania lub interweniowania w nim:

* **Pause Prompt:** Tymczasowo wstrzymuje bieżące wykonanie. Przydatne, gdy chcesz przyjrzeć się bieżącemu stanowi lub przygotować system do kolejnych kroków.&#x20;
* **Resume Prompt:** Kontynuuje wykonanie od miejsca, w którym zostało wstrzymane. ![](<../../.gitbook/assets/image (3) (1).png>)
* **Cancel Prompt:** Całkowicie zatrzymuje wykonanie i resetuje sesję. Jest to pomocne, gdy prompt trzeba przerwać lub uruchomić ponownie z powodu nieprawidłowego zachowania lub zmian w danych wejściowych.&#x20;
* **Take Control:** Pozwala użytkownikowi ręcznie interweniować, wchodząc w bezpośrednią interakcję z systemem. Jest to przydatne, gdy operator utknie lub błędnie zinterpretuje krok. Przejęcie kontroli **automatycznie wstrzymuje** prompt i przełącza w tryb ręczny, dopóki nie zdecydujesz się wznowić lub anulować.

### 5. Widok szczegółowy operatora

Po uruchomieniu promptu pojawia się dodatkowy przycisk, który pozwala użytkownikom przełączyć się na **szczegółowy widok wykonania**. ![](<../../.gitbook/assets/Detailed view .jpg>)

* **Open Detail View:** Ten przycisk przenosi do dedykowanego widoku, który w czasie rzeczywistym pokazuje krok po kroku, co robi operator.

W widoku szczegółowym użytkownicy mogą:

* Monitorować każdą wykonywaną akcję (np. kliknięcia, wprowadzanie danych, oczekiwania).
* Zobaczyć, który krok jest aktualnie aktywny.
* Zidentyfikować, gdzie występują problemy, jeśli prompt napotka trudności.
* Korzystać z tych samych akcji **Pause**, **Resume**, **Cancel** i **Take Control**.

<div align="left"><figure><img src="../../.gitbook/assets/detailed view 2 .jpg" alt="" width="563"><figcaption></figcaption></figure></div>
