# Łączna cena różnicy ilości

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_invoice.png" alt="DocBits Zakup Zamówienie Faktura"><figcaption></figcaption></figure>

Cel: Ta karta DocBits została zaprojektowana w celu usprawnienia procesu weryfikacji faktur poprzez porównanie całkowitej obliczonej ceny z faktury z odpowiadającym zamówieniem zakupu.

Funkcjonalność:

* Łączna cena różnicy ilości: Karta oblicza całkowitą cenę, mnożąc ilość każdego przedmiotu wymienionego na fakturze przez cenę za sztukę, a następnie odejmuje tę sumę od kwoty podanej w powiązanym zamówieniu zakupu.
* Wartość operatora: Użytkownicy mogą ustawić warunki określające, w jaki sposób różnica obliczonej całkowitej ceny powinna być porównana z kwotą zamówienia zakupu. Dostępne są następujące operatory:
*
* Równa się (=): Sprawdza, czy całkowita kwota faktury jest dokładnie taka sama jak kwota zamówienia zakupu.
* Nie równa się (≠): Weryfikuje, czy całkowita kwota faktury różni się od kwoty zamówienia zakupu.
* Większa niż (>): Zapewnia, że kwota faktury jest większa niż kwota zamówienia zakupu.
* Mniejsza niż (<): Potwierdza, że kwota faktury jest mniejsza niż kwota zamówienia zakupu.

Użycie: Ta karta jest szczególnie przydatna dla menedżerów ERP i księgowych finansowych, którzy potrzebują zautomatyzować i zabezpieczyć przed błędami proces rekonsyliacji faktur z zamówieniami zakupu, zapewniając dokładność finansową i zapobiegając nadpłatom lub niedopłatom.

Przykładowy scenariusz:

* Faktura wymienia łącznie 100 sztuk produktu po $50 za sztukę, co daje łącznie $5000. Powiązane zamówienie zakupu zatwierdziło zakup na $4500. Korzystając z operatora "Większa niż", karta identyfikuje i oznacza rozbieżność do przeglądu.

Korzystając z karty "Porównaj z zamówieniem zakupu", użytkownicy mogą automatycznie zapewnić, że płatności są zgodne z umowami zakupowymi, oszczędzając czas i redukując błędy ludzkie w procesach finansowych.

\
\
