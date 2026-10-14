# Purchase Invoice - 2nd Approval Unit Price

<figure><img src="../../../../.gitbook/assets/docbits_approval_invoice_3.png" alt="DocBits Zatwierdzenie Faktura 3"><figcaption></figcaption></figure>

Ten tytuł wskazuje, że reguła została skonfigurowana do zarządzania drugim etapem zatwierdzania faktury zakupowej, ze szczególnym naciskiem na walidację ceny jednostkowej.

#### Konfiguracja reguły:

1. **When…**
   * **Document Type is Invoice**: Ten warunek zapewnia, że reguła jest wyzwalana tylko dla dokumentów zidentyfikowanych jako faktury, odfiltrowując inne typy dokumentów i utrzymując trafność przepływu pracy.
2. **And…**
   * **Document Status is Pending Second Approval**: To określa, że faktura znajduje się w fazie, w której oczekuje na drugie zatwierdzenie. Jest to zwykle krok zaprojektowany w celu zapewnienia dodatkowego nadzoru przed ostatecznym przetwarzaniem.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: To dodatkowo zawęża zastosowanie tej reguły tylko do tych faktur, które są sklasyfikowane jako "Purchase Invoices", odróżniając je od innych podtypów faktur.
   * **Logic Unit Price in order confirmation Not Equals purchase order**: Ta kontrola logiczna jest kluczowa, ponieważ porównuje cenę jednostkową wymienioną w potwierdzeniu zamówienia z ceną jednostkową w oryginalnym zamówieniu zakupu. Akcja jest wyzwalana, jeśli te wartości nie są zgodne, co może wskazywać na rozbieżność wymagającą rozwiązania.

#### Action (Then…):

* **Assign user from field Buyer Name, use user User as fallback**: Jeśli określone warunki są spełnione (tj. występuje niezgodność w cenach jednostkowych), faktura jest automatycznie przypisywana do kupującego (nazwa określona w polu 'Buyer Name') w celu dalszego przeglądu. Jeśli pole 'Buyer Name' jest puste lub nieokreślone, przypisywany jest domyślny użytkownik (prawdopodobnie administrator lub inny wyznaczony pracownik) jako rozwiązanie zapasowe do obsługi zatwierdzenia.

#### Cel tej reguły:

* **Zapewnienie dokładności i zgodności**: Ta reguła jest kluczowa dla zapewnienia, że proces fakturowania jest dokładny i zgodny z uzgodnionymi warunkami. Wyzwalając przegląd w przypadku rozbieżności w cenach jednostkowych, system pomaga zapobiegać błędom finansowym lub potencjalnym oszustwom.
* **Usprawnienie zatwierdzeń**: Automatyzacja przypisania do przeglądu na podstawie określonych rozbieżności pomaga usprawnić proces zatwierdzania i zapewnia, że problemy są niezwłocznie rozwiązywane przez odpowiedni personel.
* **Nadzór finansowy**: Wymaganie drugiego zatwierdzenia, szczególnie na podstawie dopasowania cen, wzmacnia kontrole finansowe i odpowiedzialność w organizacji.
