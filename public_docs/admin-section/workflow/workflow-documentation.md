# Dokumentacja przepływu pracy

**Dokumentacja przepływu pracy**

Aby zachować przegląd, możesz nadać różnym przepływom pracy różne nagłówki, dzięki czemu od razu będziesz wiedział, o jakie zadanie chodzi w danym przepływie pracy.

Utwórz nowy przepływ pracy: Kliknij + DODAJ PRZEPŁYW PRACY

![](<../../.gitbook/assets/0 (1).png>)

Możesz użyć tych przepływów (Test 1,2,3), aby automatycznie przypisać różne dokumenty odpowiedniemu pracownikowi w firmie.

![](<../../.gitbook/assets/1 (1).png>)

Jeśli faktura lub inny dokument przekracza określoną łączną kwotę, która wymaga wcześniejszej weryfikacji i zatwierdzenia, te dokumenty można natychmiast przypisać do właściwej osoby.

<figure><img src="../../.gitbook/assets/docbits_purchase_order_table.png" alt="DocBits Zakup Zamówienie Tabela"><figcaption></figcaption></figure>

**Test 1:              Karta logiczna**

Kiedy:             **Przypisany jest:**                    Amier Haider

I:                **Typ dokumentu to:**        Faktura

Wtedy:              **Przypisz dokument do:**   Stefan Reppermund

![](<../../.gitbook/assets/3 (1).png>)

**Test 2:              Karta logiczna**

Kiedy:              **Przypisany jest:**                    Amier Haider

I:                 **Typ dokumentu to:**        Nota dostawy

Wtedy:               **Przypisz dokument do:**   James Edwards

![](<../../.gitbook/assets/4 (1).png>)

**Test 3:             Karta logiczna**

**Kiedy:**             **Przypisany jest:**                    Amier Haider

**I:**                **Typ dokumentu to:**        Potwierdzenie zamówienia

**Wtedy:**              **Przypisz dokument do:**   Anian Sollinger

![](<../../.gitbook/assets/5 (1).png>)

Jest także możliwe, jeśli dokument nie jest przypisany do jednej osoby, przypisać go od razu do konkretnego pracownika.

<figure><img src="../../.gitbook/assets/docbits_db_access_creation.png" alt="Docbits Db Access Creation" width="375"><figcaption></figcaption></figure>

Dla łatwiejszego przeglądu tego, co powinno się stać z dokumentem, można ustawić status dla przychodzących dokumentów w tym przepływie pracy. Ten przepływ pracy pozwala natychmiast zobaczyć, czy na przykład istnieje oczekiwanie na zatwierdzenie.

**Test 4:             Karta logiczna**

**Kiedy:**             **Typ dokumentu to:**         Nota dostawy

**I:**                **Przypisany jest:**                     Amier Haider

**Wtedy:**              **Zmień status na:**         Oczekuje na zatwierdzenie

<figure><img src="../../.gitbook/assets/docbits_approval.png" alt="DocBits Zatwierdzenie"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/8 (1).png>)

**Test 5:                Karta logiczna**

Kiedy:                **Typ dokumentu to:**           Faktura

I:                   **Przypisany jest:**                       Stefan Reppermund

Wtedy:                 **Zmień status na:**           Oczekuje na drugie zatwierdzenie

<figure><img src="../../.gitbook/assets/docbits_settings_workflow_2.png" alt="DocBits Ustawienia Przepływ pracy 2"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/10 (1).png>)

Jeśli faktura lub inny dokument przekracza określoną łączną kwotę, która wymaga wcześniejszej weryfikacji i zatwierdzenia, te dokumenty można natychmiast przypisać do odpowiedniej osoby.

![](<../../.gitbook/assets/11 (1).png>)

**Test 6:                    Karta logiczna**

Kiedy:                   **Przypisany jest:**                   Amier Haider

I:                      Docfield        **total\_amount**     jest      **Większe niż       500**

Wtedy:                    **Przypisz dokument do:**   Asad Usman Khan

<figure><img src="../../.gitbook/assets/docbits_table_invoice_3.png" alt="DocBits Tabela Faktura 3"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/13 (1).png>)

Jest także możliwe wprowadzenie statusu do przepływu pracy, dzięki czemu przypisana osoba od razu widzi, jaki jest status tego dokumentu i co powinno się z nim dalej dziać.

**Test 7:                 Karta logiczna**

**Kiedy:** **Przypisany jest:**                     Amier Haider

**I:**                   Docfield           **total\_amount**      jest        **Większe niż      500**

**Wtedy:**                 **Przypisz dokument do:**     Asad Usman Khan

&#x20;                            **Zmień status na:**          Oczekuje na zatwierdzenie

<figure><img src="../../.gitbook/assets/docbits_approval_2.png" alt="DocBits Zatwierdzenie 2"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/docbits_workflow_purchase_order_2.png" alt="DocBits Przepływ pracy Zakup Zamówienie 2"><figcaption></figcaption></figure>

Na przykład, jeśli brakuje pewnych lub istotnych informacji w dokumencie, ale są one ważne i muszą być uwzględnione w dalszym przetwarzaniu, można skonfigurować przepływ pracy tak, aby te dokumenty były natychmiast przekazywane do kupującego i zastępcy.

<figure><img src="../../.gitbook/assets/docbits_workflow_5.png" alt="DocBits Przepływ pracy 5"><figcaption></figcaption></figure>

**Test 9:**

Przepływ pracy z tymi kartami logicznymi został zaprojektowany do automatycznego sprawdzania, czy ilość, cena jednostkowa lub rabat szczegółowo opisane w potwierdzeniu zamówienia zgadzają się z odpowiadającymi wartościami w zamówieniu zakupu. Ta weryfikacja zapewnia spójność i dokładność między tym, co zostało zamówione, a tym, co dostawca potwierdza dostarczenie.

Możesz nadać tym dokumentom określony status lub przypisać je do konkretnego pracownika.

<div align="center">

<figure><img src="../../.gitbook/assets/docbits_approval_permission.png" alt="DocBits Zatwierdzenie Uprawnienie"><figcaption></figcaption></figure>

</div>

<figure><img src="../../.gitbook/assets/docbits_purchase_order_4.png" alt="DocBits Zakup Zamówienie 4"><figcaption></figcaption></figure>

**Karta logiczna: Ilość lub Cena jednostkowa lub Rabat pasują**

Ta karta logiczna została zaprojektowana do automatycznego sprawdzania, czy ilość, cena jednostkowa lub rabat szczegółowo opisane w potwierdzeniu zamówienia zgadzają się z odpowiadającymi wartościami w zamówieniu zakupu. Ta weryfikacja zapewnia spójność i dokładność między tym, co zostało zamówione, a tym, co dostawca potwierdza dostarczenie.

**Warunek wyzwalający**

Logika jest aktywowana, gdy którykolwiek z następujących warunków jest spełniony w potwierdzeniu zamówienia w odniesieniu do pierwotnego zamówienia zakupu:

* **Ilość**: Ilość zamówionych przedmiotów zgadza się z ilością potwierdzoną przez dostawcę.
* **Cena jednostkowa**: Cena za każdy przedmiot uzgodniona zgadza się z potwierdzeniem dostawcy.
* **Rabat**: Wszelkie zastosowane rabaty są zgodne między zamówieniem zakupu a potwierdzeniem zamówienia.

* **Zdefiniuj parametry porównania**: Skonfiguruj konkretne pola (ilość, cena jednostkowa, rabat), które karta logiczna będzie sprawdzać pod kątem dopasowania.
* **Automatyzuj weryfikację**: Skonfiguruj system do automatycznego porównywania tych szczegółów po otrzymaniu potwierdzenia zamówienia.
* **Dostosuj alerty**: Zdecyduj o przepływie pracy w przypadku różnic, w tym dostosowanie alertów do ręcznej weryfikacji.

Ta karta logiczna jest kluczowa dla zapewnienia, że szczegóły potwierdzenia zamówienia są zgodne z pierwotnym zamówieniem zakupu, chroniąc integralność cyklu zamówień.

**Test 10:**

Jeśli masz inną kalkulację dla dopłat lub masz je tylko dla niektórych pozycji, możesz użyć ogólnych kart kalkulacji tabelarycznych, niektóre z nich pozwalają także filtrować za pomocą wyrażeń regularnych.

<figure><img src="../../.gitbook/assets/docbits_table_invoice.png" alt="DocBits Tabela Faktura"><figcaption></figcaption></figure>

Powyżej znajduje się przykład kalkulacji dla MTZ z filtrem dla numerów pozycji rozpoczynających się od 01, 06, 9, 001 lub 000.

Przy ręcznej konfiguracji zaleca się podzielenie kalkulacji, które zależą od nowych kolumn, na osobny przepływ pracy. Aby kontynuować kalkulację, można użyć karty Uruchom przepływ pracy.

**Uruchom przepływ pracy**

<figure><img src="../../.gitbook/assets/docbits_workflow_2.png" alt="DocBits Przepływ pracy 2"><figcaption></figcaption></figure>

Z tą kartą można określić nazwę przepływu pracy, który ma zostać uruchomiony po bieżącym przepływie pracy, jeśli jego warunki są spełnione i po poprzednich kartach then bieżącego przepływu pracy. Chociaż priorytetem są uruchamialne, aktywne przepływy pracy, umożliwia również uruchomienie dezaktywowanych przepływów pracy, jeśli dokument spełnia warunki przepływów pracy.
### **Dodawanie obliczonych dopłat do istniejącej kolumny** <a href="#pekg4i18rshn" id="pekg4i18rshn"></a>

<figure><img src="https://lh7-us.googleusercontent.com/XYY1xsFpp7_-Bi0WOSbotiVzspDLdaufx_xgoopMHmxdZnSDhroLpb0AE_si5PhwMq1jHfndc9FwOte9MOoCoTP5_JUYawO5cr4uIctIDHmwVjz3KacQrLJd8iBQy5KY4N-dMaWEi3IeTcc5OBRNJk4" alt=""><figcaption></figcaption></figure>

Jeśli chcesz dodać wszystkie dopłaty jako ujemne zniżki do kolumny zniżek, możesz skorzystać z karty obliczeń. Mogą być wpisy w tej kolumnie, możesz ustawić ją jako jedną z zmiennych na karcie, odjąć od niej MTZ i dodać wynik z powrotem do tej kolumny. W przypadku pustych pól (dopłaty tylko dla niektórych pozycji) przyjmuje się 0 dla obliczeń.

**Powiadom użytkownika, aby autoryzował potwierdzenie zamówienia w DocBits**

Po obliczeniu dopłat możesz chcieć powiadomić określonego użytkownika o autoryzacji potwierdzenia zamówienia. W tym celu możesz skorzystać z karty powiadomień

<figure><img src="../../.gitbook/assets/docbits_settings_email.png" alt="DocBits Ustawienia E-mail"><figcaption></figcaption></figure>

W zależności od ustawień, użytkownik otrzymuje nowe zadanie w DocBits i opcjonalnie e-mail informujący go o nowym zadaniu.
