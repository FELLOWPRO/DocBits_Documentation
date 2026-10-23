# Statusy wyłączenia zamówienia zakupu

## **Przegląd**

Ustawienie **Statusy Wyłączenia PO** pozwala użytkownikom określić statusy zamówienia zakupu (PO), które uniemożliwiają dopasowanie faktur do tych PO. Jeśli zamówienie zakupu ma status wymieniony w tym ustawieniu, **nie może** być używane do dopasowywania faktur na ekranie dopasowywania PO, co wstrzymuje dalsze przetwarzanie powiązanych faktur, aż status PO zmieni się na taki, który nie jest wyłączony.\
\
Korzystając z tego ustawienia, użytkownicy mogą zapewnić, że zamówienia zakupu o określonych statusach nie będą poddawane dalszemu przetwarzaniu faktur, co zmniejsza błędy i zapobiega niepotrzebnym płatnościom.

## **Kroki aktywacji**

1.  Przejdź do **Ustawienia → Ustawienia globalne → Typy dokumentów**

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_1.png" alt="Hiszpańska nawigacja ustawień DocBits z grupami Global Settings i Document Processing oraz pozycjami informacji o firmie i uprawnień użytkowników"><figcaption></figcaption></figure>
2.  Wybierz żądany typ dokumentu i kliknij **Więcej ustawień**.

    <figure><img src="../../../../../../.gitbook/assets/Calculate_PO_unit_price_2.png" alt="Strona Document Types z listą Invoice, Credit Note, Delivery Note, Order Confirmation i Contract oraz zakładkami Edit layout, Document Sub Types, Table columns i Fields"><figcaption></figcaption></figure>
3.  W sekcji **Zamówienie zakupu** przejdź do opcji **Statusy Wyłączenia PO**.

    <figure><img src="../../../../../../.gitbook/assets/disable_po_status_3.png" alt="Strona More Settings dla typów dokumentów z sekcją Purchase Order i wyróżnioną opcją PO disable statuses"><figcaption></figcaption></figure>

### **Jak zidentyfikować wyłączone zamówienie zakupu**

Na ekranie **Dopasowanie PO** wyłączone zamówienie zakupu pojawia się **przekreślone**. To wizualnie wskazuje, że PO jest obecnie ograniczone w dopasowywaniu z powodu swojego statusu.

<figure><img src="../../../../../../.gitbook/assets/disable_po_status_6.png" alt="Tabela na ekranie PO Matching z kolumnami LINE NUMBER, ITEM ID, STATUS, QUANTITY, UNIT PRICE i MATCHED QUANTITY"><figcaption></figcaption></figure>

### **Jak to skonfigurować**

1. W ustawieniu **Statusy Wyłączenia PO** zobaczysz pole wyboru po lewej stronie.
2.  Kliknięcie tego pola otwiera rozwijane menu dostępnych statusów PO.

    <figure><img src="../../../../../../.gitbook/assets/disable_po_status_4.png" alt="Lista rozwijana statusów wyłączania PO z opcjami Canceled, Deleted, Invoiced, Open, Partially Invoiced, Partially Received, Received, Rejected, Unapproved, Hold i Closed" width="372"><figcaption></figcaption></figure>
3. Wybierz jeden lub więcej statusów, klikając na nie. Kliknij ponownie, aby odznaczyć.
4.  Kliknij przycisk **Zastosuj**, aby zapisać zmiany.

    <figure><img src="../../../../../../.gitbook/assets/disable_po_status_5.png" alt="Ustawienie statusów wyłączonych dla PO z wybranymi wartościami Canceled, Deleted i Invoiced oraz przyciskiem Apply"><figcaption></figcaption></figure>

**Dostępne statusy**

* Anulowane
* Usunięte
* Fakturowane
* Otwarte
* Częściowo fakturowane
* Częściowo odebrane
* Odebrane
* Odrzucone
* Niezatwierdzone
* Hold
* Zamknięte
