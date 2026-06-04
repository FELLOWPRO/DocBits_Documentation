# Unit Price Combined with Fields

<figure><img src="../../../../.gitbook/assets/docbits_purchase_order_invoice_2.png" alt="DocBits Zakup Zamówienie Faktura 2"><figcaption></figcaption></figure>

Cel: Ta karta DocBits ułatwia szczegółowe porównanie cen jednostkowych na fakturach z cenami określonymi w odpowiadających im zamówieniach zakupu. Zwiększa dokładność raportowania finansowego, zapewniając przestrzeganie uzgodnionych cen.

Funkcjonalność:

* Unit Price Combined with Fields: Ta karta oblicza całkowitą kwotę dla określonej pozycji, łącząc cenę jednostkową z dodatkowymi określonymi polami z faktury. Połączona suma jest następnie porównywana z zapisaną w zamówieniu zakupu ceną jednostkową tej pozycji.
* Operator Value: Użytkownicy mogą ustawić konkretne warunki dotyczące sposobu porównania połączonej ceny jednostkowej faktury z ceną jednostkową zamówienia zakupu. Dostępne operatory obejmują:
*
  * Equals (=): Weryfikuje, czy połączona cena faktury odpowiada cenie na zamówieniu zakupu.
  * Not Equal (≠): Zapewnia, że połączona cena faktury nie odpowiada cenie na zamówieniu zakupu.
  * Greater Than (>): Sprawdza, czy połączona cena faktury przekracza cenę na zamówieniu zakupu.
  * Less Than (<): Potwierdza, że połączona cena faktury jest niższa niż cena na zamówieniu zakupu.

Zastosowanie: Ta karta jest szczególnie cenna dla menedżerów ERP i księgowych finansowych, których zadaniem jest utrzymanie ścisłej kontroli nad procesami zakupowymi i płatniczymi. Zapewnia, że ceny fakturowane są zgodne z tymi uzgodnionymi w zamówieniach zakupu, łagodząc tym samym rozbieżności finansowe.

Przykładowy scenariusz:

* Faktura przedstawia cenę jednostkową 50 USD za produkt. Określona "field name" obejmuje dodatkową opłatę manipulacyjną w wysokości 5 USD za jednostkę. Po połączeniu łączna kwota za jednostkę wynosi 55 USD. Przy użyciu operatora "Equals" z wartością ustawioną na 55 USD karta weryfikuje, czy cena fakturowana jest zgodna z zamówieniem zakupu, zapewniając zgodność z umową.

Wdrażając kartę "Compare with Purchase Order: Unit Price Combined", firmy mogą zautomatyzować weryfikację dokładności cen względem zamówień zakupu, usprawniając operacje finansowe i chroniąc przed zawyżonymi opłatami.

\
