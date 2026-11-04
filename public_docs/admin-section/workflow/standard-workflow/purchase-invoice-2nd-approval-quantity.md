# Faktura zakupu - 2. zatwierdzenie ilości

<figure><img src="../../../.gitbook/assets/docbits_rule_purchase_invoice_quantity.png" alt="DocBits Reguła Zakup Faktura Quantity"><figcaption></figcaption></figure>

Ten tytuł wskazuje, że reguła dotyczy konkretnie obsługi faktur zakupowych podczas wtórnej fazy zatwierdzania, z naciskiem na weryfikację dokładności podanych ilości.

#### Konfiguracja reguły:

1. **Gdy…**
   * **Typ dokumentu to Faktura**: Ten warunek zapewnia, że reguła jest aktywowana tylko dla dokumentów sklasyfikowanych jako faktury. Jest to niezbędne dla zachowania specyfiki i trafności w przepływie pracy.
2. **Oraz…**
   * **Status dokumentu to Oczekuje na drugie zatwierdzenie**: Określa to, że faktura oczekuje obecnie na drugie zatwierdzenie. Ten etap ma zazwyczaj na celu zapewnienie dodatkowego nadzoru przed sfinalizowaniem faktury.
   * **Pole dokumentu Podtyp faktury to Faktura zakupu**: Ten warunek dodatkowo zawęża regułę, aby stosowała się wyłącznie do faktur zidentyfikowanych jako „Faktury zakupu”. Ta kategoryzacja pomaga odróżnić je od innych typów faktur.
   * **Logika: Ilość w potwierdzeniu zamówienia nie równa się zamówieniu zakupu**: Ten krytyczny warunek sprawdza, czy ilość podana w potwierdzeniu zamówienia zgadza się z ilością w oryginalnym zamówieniu zakupu. Akcja jest uruchamiana, jeśli występuje rozbieżność, co wskazuje na potencjalny błąd lub problem wymagający rozwiązania.

#### Akcja (Wtedy…):

* **Przypisz użytkownika z pola Nazwisko nabywcy, użyj użytkownika Użytkownik jako rezerwowego**: Jeśli warunki reguły zostaną spełnione (tj. występuje rozbieżność w ilościach), faktura jest automatycznie przypisywana do osoby wymienionej w polu „Nazwisko nabywcy” w celu dalszego przeglądu. Jeśli to pole jest puste lub wskazana osoba jest niedostępna, kontrolę przejmuje użytkownik domyślny (prawdopodobnie administrator lub inny wyznaczony pracownik), aby zapewnić terminowy przegląd i rozwiązanie problemu.

#### Cel tej reguły:

* **Dokładność i zgodność**: Reguła ta ma kluczowe znaczenie dla zapewnienia, że proces fakturowania jest dokładny i zgodny z warunkami uzgodnionymi w zamówieniu zakupu. Pomaga zapobiegać rozbieżnościom finansowym i potencjalnym błędom w inwentarzu.
* **Usprawnione zatwierdzenia**: Automatyzacja procesu przeglądu pod kątem konkretnych rozbieżności pomaga usprawnić zatwierdzenia i zapewnia szybkie rozwiązanie wszelkich problemów przez odpowiedni personel.
* **Zwiększony nadzór finansowy**: Wymaganie wtórnego zatwierdzenia weryfikacji ilości wzmacnia kontrolę finansową i odpowiedzialność w organizacji.

Taka konfiguracja stanowi przykład tego, jak można wykorzystać automatyzację przepływu pracy w celu zwiększenia wydajności operacyjnej i zapewnienia integralności finansowej, szczególnie w zarządzaniu złożonymi procesami zakupowymi w firmie.