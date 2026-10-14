# Purchase Invoice - 2nd Approval Quantity

<figure><img src="../../../../.gitbook/assets/docbits_approval_invoice_4.png" alt="DocBits Zatwierdzenie Faktura 4"><figcaption></figcaption></figure>

Ten tytuł wskazuje, że reguła dotyczy konkretnie obsługi faktur zakupowych podczas drugiego etapu zatwierdzania, z naciskiem na weryfikację dokładności wymienionych ilości.

#### Konfiguracja reguły:

1. **When…**
   * **Document Type is Invoice**: Ten warunek zapewnia, że reguła jest aktywowana tylko dla dokumentów sklasyfikowanych jako faktury. Jest to niezbędne do utrzymania specyficzności i trafności w przepływie pracy.
2. **And…**
   * **Document Status is Pending Second Approval**: To określa, że faktura aktualnie oczekuje na drugie zatwierdzenie. Ten etap ma zwykle zapewnić dodatkowy nadzór przed sfinalizowaniem faktury.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Ten warunek dodatkowo zawęża regułę, aby miała zastosowanie wyłącznie do faktur zidentyfikowanych jako "Purchase Invoices". Ta kategoryzacja pomaga odróżnić je od innych typów faktur.
   * **Logic Quantity in order confirmation Not Equals purchase order**: Ten kluczowy warunek sprawdza, czy ilość podana w potwierdzeniu zamówienia jest zgodna z ilością w oryginalnym zamówieniu zakupu. Akcja jest wyzwalana, jeśli występuje rozbieżność, wskazując na potencjalny błąd lub problem wymagający rozwiązania.

#### Action (Then…):

* **Assign user from field Buyer Name, use user User as fallback**: Jeśli warunki reguły są spełnione (tj. występuje rozbieżność w ilościach), faktura jest automatycznie przypisywana do osoby wymienionej w polu 'Buyer Name' w celu dalszego przeglądu. Jeśli to pole jest puste lub określona osoba jest niedostępna, domyślny użytkownik (prawdopodobnie administrator lub inny wyznaczony pracownik) przejmuje obowiązki, aby zapewnić terminowy przegląd i rozwiązanie.

#### Cel tej reguły:

* **Dokładność i zgodność**: Reguła jest niezbędna do zapewnienia, że proces fakturowania jest dokładny i zgodny z warunkami uzgodnionymi w zamówieniu zakupu. Pomaga zapobiegać rozbieżnościom finansowym i potencjalnym błędom w stanach magazynowych.
* **Usprawnione zatwierdzenia**: Automatyzacja procesu przeglądu dla określonych rozbieżności pomaga usprawnić zatwierdzenia i zapewnia, że wszelkie problemy są szybko rozwiązywane przez odpowiedni personel.
* **Wzmocniony nadzór finansowy**: Wymaganie drugiego zatwierdzenia dla weryfikacji ilości wzmacnia kontrole finansowe i odpowiedzialność w organizacji.

Ta konfiguracja stanowi przykład, jak automatyzacja przepływu pracy może być wykorzystana do zwiększenia wydajności operacyjnej i zapewnienia integralności finansowej, szczególnie w zarządzaniu złożonymi procesami zakupowymi w firmie.
