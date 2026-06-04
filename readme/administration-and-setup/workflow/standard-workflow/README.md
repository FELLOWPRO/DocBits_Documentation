# Standard Workflow

<figure><img src="../../../../.gitbook/assets/docbits_workflow_purchase_order_4.svg" alt="DocBits Przepływ pracy Zakup Zamówienie 4"><figcaption></figcaption></figure>

#### Przegląd komponentów przepływu pracy:

* **AP Invoice Email**: Proces prawdopodobnie rozpoczyna się od faktury otrzymanej za pośrednictwem wiadomości e-mail.
* **DocBits**: To narzędzie może być używane do początkowych zadań zarządzania dokumentami, takich jak przechwytywanie i digitalizacja faktur.
* **Finance Review**: Faktury przechodzą przegląd finansowy, podczas którego podejmowane są decyzje dotyczące ich ważności i dokładności.

#### Kroki w przepływie pracy:

1. **Wstępny przegląd**:
   * Faktury są otrzymywane i wstępnie przetwarzane przy użyciu DocBits.
   * Następnie są sprawdzane przez zespół finansowy, aby zapewnić ich usunięcie z przepływu pracy, jeśli są kompletne, lub przekazanie do dalszego przetwarzania.
2. **Faktury PO a faktury bez PO**:
   * Przepływ pracy rozróżnia faktury związane z PO i faktury bez PO.
   * Faktury bez PO są kierowane do dalszego zatwierdzenia lub odrzucenia na podstawie wstępnie zdefiniowanych kryteriów, takich jak identyfikator dostawcy, ilość, cena jednostkowa i numer pozycji.
3. **Zgodność i niezgodność**:
   * Faktury są sprawdzane względem przyjęć towarów, aby upewnić się, że szczegóły są zgodne (jak identyfikator dostawcy i ilość).
   * W przypadku wystąpienia niezgodności faktura podlega dalszemu przeglądowi i ewentualnemu odrzuceniu.
4. **Przegląd finansowy i przegląd kupującego**:
   * W przypadku faktur związanych z PO przeprowadzany jest szczegółowy proces dopasowania z udziałem przeglądu kupującego.
   * Mogą być wymagane korekty zamówień zakupu lub przyjęć towarów.
5. **Decyzje końcowe**:
   * Faktury, które przejdą wszystkie kontrole, są zatwierdzane i integrowane z systemami finansowymi na potrzeby ewidencji.
   * Odrzucone faktury wyzwalają powiadomienia, a kupujący może zażądać nowej faktury.
6. **Integracja z Infor IDM & LN+M3**:
   * Zatwierdzone faktury są prawdopodobnie wysyłane do Infor IDM w celu zarządzania dokumentami oraz do LN w celu ich zaksięgowania.
   * Ta integracja zapewnia, że wszystkie zapisy finansowe są aktualne i że przepływ pracy bezproblemowo zasila szerszy system ERP.

#### Punkty decyzyjne:

* W całym przepływie pracy znajdują się różne punkty decyzyjne, w których faktura może zostać zatwierdzona, odrzucona lub odesłana w celu uzyskania dodatkowych informacji. Powiadomienia są wysyłane po opóźnieniach, zapewniając terminowe przetwarzanie.

Te przepływy pracy zostaną uwzględnione w Standard Workflow
