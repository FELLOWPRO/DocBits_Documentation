# Dokumentacja przepływu pracy

**Dokumentacja przepływu pracy**

Aby zachować przejrzystość, możesz nadać przepływom pracy różne nagłówki, dzięki czemu od razu będziesz wiedzieć, czego dotyczy dany przepływ pracy.

Utwórz nowy przepływ pracy: Kliknij + ADD WORKFLOW

![](<../../.gitbook/assets/workflow_add_button.png>)

Możesz użyć tych przepływów pracy (Test 1,2,3), aby automatycznie przypisywać różne dokumenty do właściwego pracownika w firmie.

![](<../../.gitbook/assets/workflow_list_overview.png>)

Jeśli faktura lub inny dokument przekracza określoną kwotę całkowitą, która wymaga wcześniejszego przeglądu i zatwierdzenia, dokumenty te mogą zostać natychmiast przypisane do właściwej osoby.

<figure><img src="../../.gitbook/assets/workflow_amount_check.png" alt="Workflow Amount Check"><figcaption></figcaption></figure>

**Test 1: Logic Card**

When: **Assignee is:** Amier Haider

And: **Document type is:** Invoice

Then: **Assign document to:** Stefan Reppermund

![](<../../.gitbook/assets/3 (1).png>)

**Test 2: Logic Card**

When: **Assignee is:** Amier Haider

And: **Document type is:** Delivery Note

Then: **Assign document to:** James Edwards

![](<../../.gitbook/assets/4 (1).png>)

**Test 3: Logic Card**

**When:** **Assignee is:** Amier Haider

**And:** **Document type is:** Order Confirmation

**Then:** **Assign document to:** Anian Sollinger

![](<../../.gitbook/assets/5 (1).png>)

Możliwe jest również, jeśli dokument nie jest przypisany do pojedynczej osoby, przypisanie go do konkretnego pracownika od samego początku.

<figure><img src="../../.gitbook/assets/workflow_assign_to_employee_start.png" alt="Workflow Assign to Employee Start" width="375"><figcaption></figcaption></figure>

Aby ułatwić przegląd tego, co powinno stać się z dokumentem, możesz ustawić status dla dokumentów przychodzących w tym przepływie pracy. Ten przepływ pracy umożliwia natychmiastowe sprawdzenie, czy istnieje na przykład oczekujące zatwierdzenie.

**Test 4: Logic Card**

**When:** **Document type is:** Delivery Note

**And:** **Assignee is:** Amier Haider

**Then:** **Change Status to:** Pending Approval

<figure><img src="../../.gitbook/assets/workflow_test4_delivery_note_status.png" alt="Workflow Test 4 Delivery Note Status"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/8 (1).png>)

**Test 5: Logic Card**

When: **Document type is:** Invoice

And: **Assignee is:** Stefan Reppermund

Then: **Change Status to:** Pending Second Approval

<figure><img src="../../.gitbook/assets/workflow_test5_invoice_approval_status.png" alt="Workflow Test 5 Invoice Approval Status"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/10 (1).png>)

Jeśli faktura lub inny dokument przekracza określoną kwotę całkowitą, która wymaga wcześniejszego przeglądu i zatwierdzenia, dokumenty te mogą zostać natychmiast przypisane do właściwej osoby.

![](<../../.gitbook/assets/11 (1).png>)

**Test 6: Logic Card**

When: **Assignee is:** Amier Haider

And: Docfield **total\_amount** is **Greater than 500**

Then: **Assign document to:** Asad Usman Khan

<figure><img src="../../.gitbook/assets/workflow_test6_total_amount_assign.png" alt="Workflow Test 6 Total Amount Assign"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/13 (1).png>)

Możliwe jest również wprowadzenie statusu do przepływu pracy, dzięki czemu przypisana osoba może natychmiast zobaczyć, jaki status ma ten dokument i co powinno z nim dalej nastąpić.

**Test 7: Logic Card**

**When:** **Assignee is:** Amier Haider

**And:** Docfield **total\_amount** is **Greater then 500**

**Then:** **Assign document to:** Asad Usman Khan

**Change Status to:** Pending Approval

<figure><img src="../../.gitbook/assets/workflow_test7_status_update.png" alt="Workflow Test 7 Status Update"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/15 (1).png" alt=""><figcaption></figcaption></figure>

Na przykład, jeśli w dokumencie brakuje pewnych lub ważnych informacji, które są jednak istotne i muszą zostać uwzględnione do dalszego przetwarzania, możesz skonfigurować przepływ pracy tak, aby dokumenty te były natychmiast przekazywane do kupującego oraz osoby zastępującej (zastępcy).

<figure><img src="../../.gitbook/assets/workflow_test8_missing_info.png" alt="Workflow Test 8 Missing Info"><figcaption></figcaption></figure>

**Test 9:**

Przepływ pracy z tymi kartami logiki jest zaprojektowany tak, aby automatycznie weryfikować, czy ilość, cena jednostkowa lub rabat wyszczególnione w potwierdzeniu zamówienia są zgodne z odpowiadającymi im wartościami w zamówieniu zakupu. Ta weryfikacja zapewnia spójność i dokładność między tym, co zamówiono, a tym, co dostawca potwierdza dostarczyć.

Możesz nadać tym dokumentom określony status lub przypisać je do konkretnego pracownika.

<div align="center"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="Workflow Test 9 Match Check Overview"><figcaption></figcaption></figure></div>

<figure><img src="../../.gitbook/assets/workflow_test9_match_check_detail.png" alt="Workflow Test 9 Match Check Detail"><figcaption></figcaption></figure>

**Logic Card: Quantity or Unit Price or Discount Match**

Ta karta logiki jest zaprojektowana tak, aby automatycznie weryfikować, czy ilość, cena jednostkowa lub rabat wyszczególnione w potwierdzeniu zamówienia są zgodne z odpowiadającymi im wartościami w zamówieniu zakupu. Ta weryfikacja zapewnia spójność i dokładność między tym, co zamówiono, a tym, co dostawca potwierdza dostarczyć.

**Warunek wyzwalający**

Logika jest aktywowana, gdy w potwierdzeniu zamówienia w odniesieniu do oryginalnego zamówienia zakupu spełniony jest którykolwiek z następujących warunków:

* **Quantity**: Ilość zamówionych pozycji jest zgodna z ilością potwierdzoną przez dostawcę.
* **Unit Price**: Uzgodniona cena za pozycję jest zgodna z potwierdzeniem dostawcy.
* **Discount**: Wszelkie zastosowane rabaty są spójne między zamówieniem zakupu a potwierdzeniem zamówienia.
* **Define Comparison Parameters**: Skonfiguruj konkretne pola (ilość, cena jednostkowa, rabat), których zgodność będzie sprawdzać karta logiki.
* **Automate Verification**: Skonfiguruj system tak, aby automatycznie porównywał te szczegóły po otrzymaniu potwierdzenia zamówienia.
* **Customize Alerts**: Zdecyduj o przepływie pracy do obsługi rozbieżności, w tym o dostosowaniu alertów do przeglądu ręcznego.

Ta karta logiki jest niezbędna do zapewnienia, że szczegóły potwierdzenia zamówienia są zgodne z oryginalnym zamówieniem zakupu, chroniąc integralność cyklu zakupowego.

**Test 10:**

Jeśli masz inne obliczenie dla dopłat lub masz je tylko na niektórych pozycjach, możesz użyć generycznych kart obliczeń tabeli, z których niektóre umożliwiają również filtrowanie według wyrażeń regularnych.

<figure><img src="../../.gitbook/assets/19 (1).png" alt=""><figcaption></figcaption></figure>

Powyżej znajduje się przykład obliczenia dla MTZ z filtrem dla numerów pozycji zaczynających się od 01, 06, 9, 001 lub 000.

W przypadku konfiguracji ręcznej zaleca się podzielenie obliczeń, które zależą od nowych kolumn, na osobny przepływ pracy. Aby kontynuować obliczenia, możesz użyć karty Run Workflow.

**Run Workflow**

<figure><img src="../../.gitbook/assets/20 (1).png" alt=""><figcaption></figcaption></figure>

Za pomocą tej karty możesz określić nazwę przepływu pracy, który ma zostać uruchomiony po bieżącym przepływie pracy, jeśli jego warunki są spełnione, oraz po poprzednich kartach then bieżącego przepływu pracy. Chociaż priorytetowo traktuje uruchamialne, aktywne przepływy pracy, umożliwia również uruchamianie dezaktywowanych przepływów pracy, jeśli dokument spełnia warunki przepływów pracy.

### **Dodawanie obliczonych dopłat do istniejącej kolumny** <a href="#pekg4i18rshn" id="pekg4i18rshn"></a>

<figure><img src="https://lh7-us.googleusercontent.com/XYY1xsFpp7_-Bi0WOSbotiVzspDLdaufx_xgoopMHmxdZnSDhroLpb0AE_si5PhwMq1jHfndc9FwOte9MOoCoTP5_JUYawO5cr4uIctIDHmwVjz3KacQrLJd8iBQy5KY4N-dMaWEi3IeTcc5OBRNJk4" alt=""><figcaption></figcaption></figure>

Jeśli chcesz dodać wszystkie dopłaty jako ujemny rabat do kolumny rabatu, możesz użyć karty obliczeń. W tej kolumnie mogą istnieć wpisy, możesz ustawić ją jako jedną ze zmiennych na karcie, odjąć od niej MTZ i dodać wynik z powrotem do tej kolumny. W przypadku gdy istnieją puste pola (dopłaty tylko dla niektórych pozycji), na potrzeby obliczeń przyjmie wartość 0

**Notify user to authorize the order confirmation in DocBits**

Po obliczeniu dopłat możesz chcieć powiadomić konkretnego użytkownika, aby autoryzował potwierdzenie zamówienia. W tym celu możesz użyć karty powiadomień

<figure><img src="../../.gitbook/assets/workflow_notification_card_overview.png" alt="Workflow Notification Card"><figcaption></figcaption></figure>

W zależności od ustawień użytkownikowi zostaje przypisane nowe zadanie w DocBits oraz opcjonalnie wiadomość e-mail powiadamiająca go o nowym zadaniu.
