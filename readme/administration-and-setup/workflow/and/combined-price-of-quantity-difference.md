# Combined Price of Quantity Difference

<figure><img src="../../../../.gitbook/assets/docbits_purchase_order_invoice.png" alt="DocBits Zakup Zamówienie Faktura"><figcaption></figcaption></figure>

Cel: Ta karta DocBits służy do usprawnienia procesu weryfikacji faktur poprzez porównanie całkowitej obliczonej ceny z faktury z odpowiadającym jej zamówieniem zakupu.

Funkcjonalność:

* Combined Price of Quantity Difference: Karta oblicza całkowitą cenę, mnożąc ilość każdej pozycji wymienionej na fakturze przez cenę jednostkową, a następnie odejmuje tę sumę od kwoty wskazanej na powiązanym zamówieniu zakupu.
* Operator Value: Użytkownicy mogą ustawić warunki określające, w jaki sposób obliczona różnica całkowitej ceny powinna być porównana z kwotą zamówienia zakupu. Dostępne są następujące operatory:
*
  * Equals (=): Sprawdza, czy całkowita kwota faktury jest dokładnie taka sama jak kwota zamówienia zakupu.
  * Not Equal (≠): Weryfikuje, czy całkowita kwota faktury różni się od kwoty zamówienia zakupu.
  * Greater Than (>): Zapewnia, że kwota faktury jest większa niż kwota zamówienia zakupu.
  * Less Than (<): Potwierdza, że kwota faktury jest mniejsza niż kwota zamówienia zakupu.

Zastosowanie: Ta karta jest szczególnie przydatna dla menedżerów ERP i księgowych finansowych, którzy muszą zautomatyzować i zabezpieczyć przed błędami uzgadnianie faktur z zamówieniami zakupu, zapewniając dokładność finansową i zapobiegając nadpłatom lub niedopłatom.

Przykładowy scenariusz:

* Faktura wymienia łącznie 100 jednostek produktu po 50 USD za jednostkę, co daje łącznie 5000 USD. Powiązane zamówienie zakupu autoryzowało zakup na kwotę 4500 USD. Przy użyciu operatora "Greater Than" karta identyfikuje i oznacza rozbieżność do przeglądu.

Korzystając z karty "Compare with Purchase Order", użytkownicy mogą automatycznie zapewnić zgodność płatności z umowami zakupu, oszczędzając czas i redukując błędy ludzkie w przetwarzaniu finansowym.

\
\
