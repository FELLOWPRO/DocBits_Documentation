# Przypisanie i status — Przykłady praktyczne

Aby zachować przejrzystość, możesz nadać przepływom pracy różne nagłówki, dzięki czemu od razu będziesz wiedzieć, czego dotyczy dany przepływ pracy.

Utwórz nowy przepływ pracy: Kliknij + ADD WORKFLOW

![](<../../.gitbook/assets/workflow_add_button.png>)

Możesz użyć tych przepływów pracy (Test 1,2,3), aby automatycznie przypisywać różne dokumenty do właściwego pracownika w firmie.

![](<../../.gitbook/assets/workflow_list_overview.png>)

Jeśli faktura lub inny dokument przekracza określoną kwotę całkowitą, która wymaga wcześniejszego przeglądu i zatwierdzenia, dokumenty te mogą zostać natychmiast przypisane do właściwej osoby.

<figure><img src="../../.gitbook/assets/workflow_amount_check.png" alt="Workflow Amount Check"><figcaption></figcaption></figure>

**Test 1: Karta logiczna**

When: **Assignee is:** Osoba odpowiedzialna za odbiór

Oraz: **Typ dokumentu to:** Faktura

Then: **Assign document to:** Osoba sprawdzająca fakturę

![](<../../.gitbook/assets/3 (1).png>)

**Test 2: Karta logiczna**

When: **Assignee is:** Osoba odpowiedzialna za odbiór

Oraz: **Typ dokumentu to:** Dowód dostawy

Then: **Assign document to:** Osoba sprawdzająca dostawę

![](<../../.gitbook/assets/4 (1).png>)

**Test 3: Karta logiczna**

**When:** **Assignee is:** Osoba odpowiedzialna za odbiór

**And:Typ dokumentu to:** Potwierdzenie zamówienia

**Then:** **Assign document to:** Osoba sprawdzająca zamówienie

![](<../../.gitbook/assets/5 (1).png>)

Możliwe jest również, jeśli dokument nie jest przypisany do pojedynczej osoby, przypisanie go do konkretnego pracownika od samego początku.

<figure><img src="../../.gitbook/assets/workflow_assign_to_employee_start.png" alt="Workflow Assign to Employee Start" width="375"><figcaption></figcaption></figure>

Aby ułatwić przegląd tego, co powinno stać się z dokumentem, możesz ustawić status dla dokumentów przychodzących w tym przepływie pracy. Ten przepływ pracy umożliwia natychmiastowe sprawdzenie, czy istnieje na przykład oczekujące zatwierdzenie.

**Test 4: Karta logiczna**

**Kiedy:Typ dokumentu to:** Dowód dostawy

**And:** **Assignee is:** Osoba odpowiedzialna za odbiór

**Następnie:Zmień status na:** Oczekuje na zatwierdzenie

<figure><img src="../../.gitbook/assets/s150-workflow_test4_delivery_note_status-pl.png" alt="Niezapisany projekt przepływu zmieniającego status."><figcaption><p>Niezapisany projekt przepływu zmieniającego status.</p></figcaption></figure>

![](<../../.gitbook/assets/8 (1).png>)

**Test 5: Karta logiczna**

Kiedy: **Typ dokumentu to:** Faktura

And: **Assignee is:** Osoba sprawdzająca fakturę

Następnie: **Zmień status na:** Oczekuje na drugie zatwierdzenie

<figure><img src="../../.gitbook/assets/workflow_test5_invoice_approval_status.png" alt="Workflow Test 5 Invoice Approval Status"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/10 (1).png>)

Jeśli faktura lub inny dokument przekracza określoną kwotę całkowitą, która wymaga wcześniejszego przeglądu i zatwierdzenia, dokumenty te mogą zostać natychmiast przypisane do właściwej osoby.

![](<../../.gitbook/assets/11 (1).png>)

**Test 6: Karta logiczna**

When: **Assignee is:** Osoba odpowiedzialna za odbiór

Oraz: Docfield **total\_amount** jest **Większy niż 500**

Then: **Assign document to:** Osoba odpowiedzialna za zatwierdzenie

<figure><img src="../../.gitbook/assets/workflow_test6_total_amount_assign.png" alt="Workflow Test 6 Total Amount Assign"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/13 (1).png>)

Możliwe jest również wprowadzenie statusu do przepływu pracy, dzięki czemu przypisana osoba może natychmiast zobaczyć, jaki status ma ten dokument i co powinno z nim dalej nastąpić.

**Test 7: Karta logiczna**

**When:** **Assignee is:** Osoba odpowiedzialna za odbiór

**And:** Docfield **total\_amount** jest **Większy niż 500**

**Then:** **Assign document to:** Osoba odpowiedzialna za zatwierdzenie

**Zmień status na:** Oczekuje na zatwierdzenie

<figure><img src="../../.gitbook/assets/s150-workflow_test7_status_update-pl.png" alt="Działanie zmiany statusu w projekcie przepływu."><figcaption><p>Działanie zmiany statusu w projekcie przepływu.</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/15 (1).png" alt="Kreator przepływów pracy z trzema kartami logiki przypisującymi dokumenty według osoby przypisanej i typu dokumentu do Invoice reviewer, Delivery-note reviewer i Order reviewer"><figcaption></figcaption></figure>

Na przykład, jeśli w dokumencie brakuje pewnych lub ważnych informacji, które są jednak istotne i muszą zostać uwzględnione do dalszego przetwarzania, możesz skonfigurować przepływ pracy tak, aby dokumenty te były natychmiast przekazywane do kupującego oraz osoby zastępującej (zastępcy).

<figure><img src="../../.gitbook/assets/workflow_test8_missing_info.png" alt="Workflow Test 8 Missing Info"><figcaption></figcaption></figure>

**Test 9:**

Przepływ pracy z tymi kartami logiki jest zaprojektowany tak, aby automatycznie weryfikować, czy ilość, cena jednostkowa lub rabat wyszczególnione w potwierdzeniu zamówienia są zgodne z odpowiadającymi im wartościami w zamówieniu zakupu. Ta weryfikacja zapewnia spójność i dokładność między tym, co zamówiono, a tym, co dostawca potwierdza dostarczyć.

Możesz nadać tym dokumentom określony status lub przypisać je do konkretnego pracownika.

<div align="center"><figure><img src="../../.gitbook/assets/s150-workflow_test9_match_check_overview-pl.png" alt="Projekt przepływu z warunkiem porównania z zamówieniem zakupu."><figcaption><p>Projekt przepływu z warunkiem porównania z zamówieniem zakupu.</p></figcaption></figure></div>

<figure><img src="../../.gitbook/assets/s150-workflow_test9_match_check_detail-pl.png" alt="Wybór warunków porównania z zamówieniem zakupu."><figcaption><p>Wybór warunków porównania z zamówieniem zakupu.</p></figcaption></figure>

**Karta logiczna: ilość, cena jednostkowa lub rabat**

Ta karta logiki jest zaprojektowana tak, aby automatycznie weryfikować, czy ilość, cena jednostkowa lub rabat wyszczególnione w potwierdzeniu zamówienia są zgodne z odpowiadającymi im wartościami w zamówieniu zakupu. Ta weryfikacja zapewnia spójność i dokładność między tym, co zamówiono, a tym, co dostawca potwierdza dostarczyć.

**Warunek wyzwalający**

Logika jest aktywowana, gdy w potwierdzeniu zamówienia w odniesieniu do oryginalnego zamówienia zakupu spełniony jest którykolwiek z następujących warunków:

* **Ilość**: Ilość zamówionych pozycji jest zgodna z ilością potwierdzoną przez dostawcę.
* **Cena jednostkowa**: Uzgodniona cena za pozycję jest zgodna z potwierdzeniem dostawcy.
* **Rabat**: Wszelkie zastosowane rabaty są spójne między zamówieniem zakupu a potwierdzeniem zamówienia.
* **Określenie parametrów porównania**: Skonfiguruj konkretne pola (ilość, cena jednostkowa, rabat), których zgodność będzie sprawdzać karta logiki.
* **Automate Verification**: Skonfiguruj system tak, aby automatycznie porównywał te szczegóły po otrzymaniu potwierdzenia zamówienia.
* **Customize Alerts**: Zdecyduj o przepływie pracy do obsługi rozbieżności, w tym o dostosowaniu alertów do przeglądu ręcznego.

Ta karta logiki jest niezbędna do zapewnienia, że szczegóły potwierdzenia zamówienia są zgodne z oryginalnym zamówieniem zakupu, chroniąc integralność cyklu zakupowego.

**Test 10:**

Jeśli masz inne obliczenie dla dopłat lub masz je tylko na niektórych pozycjach, możesz użyć generycznych kart obliczeń tabeli, z których niektóre umożliwiają również filtrowanie według wyrażeń regularnych.

<figure><img src="../../.gitbook/assets/19 (1).png" alt="Karta obliczeń dla kolumny MTZ z regułą Material Surcharge i filtrem regex pola Item Number dla numerów pozycji zaczynających się od 01, 06, 9, 001 lub 000"><figcaption></figcaption></figure>

Powyżej znajduje się przykład obliczenia dla MTZ z filtrem dla numerów pozycji zaczynających się od 01, 06, 9, 001 lub 000.

W przypadku konfiguracji ręcznej zaleca się podzielenie obliczeń, które zależą od nowych kolumn, na osobny przepływ pracy. Aby kontynuować obliczenia, możesz użyć karty Run Workflow.

**Uruchom przepływ**

<figure><img src="../../.gitbook/assets/20 (1).png" alt="Karta Run workflow Mtz Into Discount w kreatorze przepływów pracy z sekcją Conditions do uruchamiania kolejnego przepływu pracy"><figcaption></figcaption></figure>

Za pomocą tej karty możesz określić nazwę przepływu pracy, który ma zostać uruchomiony po bieżącym przepływie pracy, jeśli jego warunki są spełnione, oraz po poprzednich kartach then bieżącego przepływu pracy. Chociaż priorytetowo traktuje uruchamialne, aktywne przepływy pracy, umożliwia również uruchamianie dezaktywowanych przepływów pracy, jeśli dokument spełnia warunki przepływów pracy.

### **Dodawanie obliczonych dopłat do istniejącej kolumny** <a href="#pekg4i18rshn" id="pekg4i18rshn"></a>



Jeśli chcesz dodać wszystkie dopłaty jako ujemny rabat do kolumny rabatu, możesz użyć karty obliczeń. W tej kolumnie mogą istnieć wpisy, możesz ustawić ją jako jedną ze zmiennych na karcie, odjąć od niej MTZ i dodać wynik z powrotem do tej kolumny. W przypadku gdy istnieją puste pola (dopłaty tylko dla niektórych pozycji), na potrzeby obliczeń przyjmie wartość 0

**Powiadom użytkownika o konieczności zatwierdzenia potwierdzenia zamówienia w DocBits**

Po obliczeniu dopłat możesz chcieć powiadomić konkretnego użytkownika, aby autoryzował potwierdzenie zamówienia. W tym celu możesz użyć karty powiadomień

<figure><img src="../../.gitbook/assets/workflow_notification_card_overview.png" alt="Workflow Notification Card"><figcaption></figcaption></figure>

W zależności od ustawień użytkownikowi zostaje przypisane nowe zadanie w DocBits oraz opcjonalnie wiadomość e-mail powiadamiająca go o nowym zadaniu.

Zaktualizowane obrazy pokazują niezapisane projekty warunków i działań. Dostosuj role oraz warunki do własnej organizacji.
