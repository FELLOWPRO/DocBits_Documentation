# Operator DocBits

## Przegląd

**Operator DocBits** to asystent automatyzacji zasilany sztuczną inteligencją, zaprojektowany do upraszczania powtarzalnych zadań w twoich procesach. Użytkownicy tworzą _prompty_ - instrukcje krok po kroku wzbogacone zmiennymi - które prowadzą AI do nawigacji, wprowadzania danych i automatycznego klikania przez interfejsy. To zmniejsza wysiłek manualny i przyspiesza rutynowe operacje.

## Włączanie Operatora DocBits

Aby włączyć Operatora DocBits, wykonaj następujące kroki:

1. **Przejdź do Ustawień**:
   * Z Pulpitu przejdź do **Ustawień**.
   *   Wybierz **Przetwarzanie Dokumentów**, a następnie wybierz **Moduł**.

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4Yyo7aXyVeWyfJHclHpK%252Fimage.png%3Falt%3Dmedia%26token%3D0071c149-3ea8-452b-a2e3-0fbbc9d3b496\&width=768\&dpr=4\&quality=100\&sign=23009aa7\&sv=2)
2. **Włącz Funkcję**:
   * Przewiń w dół, aby znaleźć opcję **Operator DocBits**.
   *   Przełącz suwak, aby włączyć **Operatora DocBits**.

       <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FyqNyGI2OelO415pf3RHN%252Fimage.png%3Falt%3Dmedia%26token%3D8899a256-a1d6-486f-aaf6-b8e244f9b348&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=ce097a28&#x26;sv=2" alt="" width="563"></div>

## Dostęp do Interfejsu

*   Gdy funkcja jest włączona, otwórz **Operatora DocBits** z menu głównego nawigacji.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FS67AFPuaQ3CNXQ7Oe80V%252Fimage.png%3Falt%3Dmedia%26token%3D6b6d6782-cc16-48e6-8622-5c596ac54f57\&width=768\&dpr=4\&quality=100\&sign=e6d0fd8e\&sv=2)

### **1. Wprowadzanie Promptu**

Na dole ekranu znajduje się pole wprowadzania oznaczone jako _"Wprowadź swój prompt tutaj..."_. Tutaj użytkownicy piszą instrukcje, które operator ma wykonać.

Obok pola wprowadzania znajduje się kilka przycisków kontrolnych:

* **Zmienne Promptu** - Otwiera okno, w którym można wprowadzić pary klucz-wartość używane w promptach. Zmienne są zapisywane w nawiasach klamrowych, np. `{numer_faktury}` lub `{url}`. Te wartości dotyczą tylko bieżącego promptu w polu wprowadzania.
* **Zapisz Prompt** - Zapisuje bieżący prompt. Wybierz, czy zapisać go jako:
  * **Prompt Organizacji** - Edytowalny w twojej organizacji; zawiera zarówno prompt, jak i zdefiniowane wartości zmiennych.
  * **Prompt Globalny** - Udostępniony wszystkim najemcom; zawiera tylko prompt i miejsca na zmienne (wartości nie są zapisywane).
* **Wyczyść Czat** - Czyści bieżącą rozmowę z operatorem, ale pozostawia prompt w polu wprowadzania niezmieniony. Przydatne przy ponownym użyciu lub udoskonalaniu promptu.

Dla szczegółowych wskazówek dotyczących pisania efektywnych promptów - w tym składni, zmiennych i przykładów - zapoznaj się z [**Przewodnikiem po Pisaniu Promptów**](prompt-writing-guide.md).

### **2. Nawigacja Bocznego Paska**

Użyj ikony w lewym górnym rogu, aby otworzyć lub zamknąć pasek boczny. Pasek boczny pokazuje zapisane prompty, zorganizowane w dwóch kategoriach:

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fm08uq4Kqj0SEZWSnlnoS%252Fimage.png%3Falt%3Dmedia%26token%3D4ba4542a-a707-4907-ae5e-b06286af8240&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=ef6b0706&#x26;sv=2" alt="" width="375"></div>

* **Prompty Organizacji**: Edytowalne i wielokrotnego użytku w twojej organizacji.
* **Prompty Globalne**: Udostępnione wszystkim najemcom. Nie mogą przechowywać zmiennych i nie mogą być edytowane ani usuwane.
  *   Globalny prompt nadal jest edytowalny i usuwalny przez **organizację, która go utworzyła**, gdzie pojawia się pod Promptami Organizacji.

      <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlVnXjwtnxAtqsftRvYUi%252Fimage.png%3Falt%3Dmedia%26token%3D60b3d0dd-3eee-40a8-b447-c9e91087a27d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=f9b364a&#x26;sv=2" alt="" width="375"></div>
* **Funkcja Wyszukiwania:** pasek wyszukiwania na górze paska bocznego pozwala użytkownikom szybko znaleźć zapisane prompty według nazwy lub słowa kluczowego.
* **Odwołanie do Ikony:** Każdy zapisany prompt ma zestaw ikon akcji
  * **Strzałka** - Uruchom prompt
  * **Długopis** - Edytuj prompt (dostępne tylko dla promptów twojej własnej organizacji)
  * **Kosz** - Usuń prompt (dostępne tylko dla promptów twojej własnej organizacji)

### 3. Zapisz Prompt

Kliknięcie przycisku **Zapisz Prompt** otwiera okno, w którym można zapisać bieżący prompt do późniejszego użycia.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FgrBpDnbo80nPkozFhgCE%252Fimage.png%3Falt%3Dmedia%26token%3Dd31c06fc-dcd0-4fbe-9e1e-6c5bc001e4bb&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=900c948&#x26;sv=2" alt="" width="375"></div>

#### **Pola Okna Zapisywania Promptu**

* **Nazwa Promptu:** Wprowadź nazwę, aby zidentyfikować prompt.
* **Zapisz Prompt Publicznie (Pole Wyboru):** Po zaznaczeniu, prompt zostanie zapisany jako **Globalny Prompt**. Prompty Globalne są udostępnione wszystkim najemcom i nie mogą przechowywać **wartości** zmiennych (tylko **nazwy** zmiennych).
* **Edytuj Zmienne:** Otwiera [**Okno Zmiennych Promptu**](prompt-writing-guide.md), aby przejrzeć lub dostosować definicje zmiennych przed zapisaniem.

**Działania**

* **Anuluj:** Zamyka okno bez zapisywania.
* **Zapisz:** Zapisuje prompt, używając określonej nazwy i ustawienia widoczności.

### 4. Kontrole Wykonywania Promptu

Kiedy prompt jest uruchomiony, użytkownicy mają kilka opcji kontrolowania lub interweniowania w procesie wykonawczym:

* **Wstrzymaj Prompt:** Tymczasowo zatrzymuje bieżące wykonanie. Przydatne, jeśli chcesz obserwować bieżący stan lub przygotować system do kolejnych kroków. ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzG9U15jmVTb202efDR5l%252Fimage.png%3Falt%3Dmedia%26token%3Dee52f250-15d4-4139-b612-ba5ff1876841\&width=300\&dpr=4\&quality=100\&sign=329efe81\&sv=2)
* **Wznów Prompt:** Kontynuuje wykonanie od momentu, w którym zostało wstrzymane. ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FewGCZ9wSXt7VsvS8RjZH%252Fimage.png%3Falt%3Dmedia%26token%3D92ec27df-07b4-4e9f-a125-6f0a87d9db47\&width=300\&dpr=4\&quality=100\&sign=8e03589c\&sv=2)
* **Anuluj Prompt:** Zatrzymuje wykonanie całkowicie i resetuje sesję. To pomocne, jeśli prompt musi zostać przerwany lub uruchomiony ponownie z powodu nieprawidłowego zachowania lub zmian wejściowych.\
  ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FYUKk03iazolJlx6reOO3%252Fimage.png%3Falt%3Dmedia%26token%3Da722c82b-e4c1-4c23-8c56-a31f2685cce7\&width=300\&dpr=4\&quality=100\&sign=170c122e\&sv=2)
* **Przejmij Kontrolę:** Pozwala użytkownikowi ręcznie interweniować, bezpośrednio współdziałając z systemem. Jest to przydatne, jeśli operator utknie lub błędnie zinterpretuje krok. Przejście pod kontrolę **automatycznie wstrzymuje** prompt i przełącza się w tryb manualny, dopóki nie zdecydujesz się wznowić lub anulować.

### 5. Widok Szczegółowy Operatora

Po uruchomieniu promptu staje się dostępny dodatkowy przycisk, który umożliwia użytkownikom przejście do **szczegółowego widoku wykonania**.\
![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9kObRWZFb3woomL045KL%252FDetailed%2520view%2520.jpg%3Falt%3Dmedia%26token%3Dbd0f94e2-84f2-4fd0-ae89-82408e85e03a\&width=300\&dpr=4\&quality=100\&sign=3aefc79\&sv=2)

* **Otwórz Widok Szczegółowy:** Ten przycisk przenosi cię do dedykowanego widoku, który pokazuje, krok po kroku, co operator robi w czasie rzeczywistym.

W widoku szczegółowym użytkownicy mogą:

* Monitorować każdą wykonywaną akcję (np. kliknięcia, wprowadzanie danych, oczekiwania).
* Zobaczyć, który krok jest obecnie aktywny.
* Zidentyfikować miejsca, w których występują problemy, jeśli prompt napotyka trudności.
* Korzystać z tych samych działań **Wstrzymaj**, **Wznów**, **Anuluj** i **Przejmij Kontrolę**.
