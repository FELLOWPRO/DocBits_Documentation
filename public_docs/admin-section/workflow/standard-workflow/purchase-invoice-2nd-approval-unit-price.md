# Faktura zakupu - 2. zatwierdzenie jednostkowej ceny

<figure><img src="../../../.gitbook/assets/docbits_approval_invoice_3.png" alt="DocBits Zatwierdzenie Faktura 3"><figcaption></figcaption></figure>

Ten tytuł wskazuje, że reguła jest ustawiona w celu zarządzania drugą fazą zatwierdzenia faktury zakupu, ze szczególnym uwzględnieniem walidacji jednostkowej ceny.

#### Konfiguracja reguły:

1. **Kiedy…**
* **Typ dokumentu to Faktura**: Ta warunek zapewnia, że reguła jest wyzwalana tylko dla dokumentów zidentyfikowanych jako faktury, wykluczając inne typy dokumentów i zachowując istotność procesu roboczego.
2. **I…**
* **Status dokumentu to Oczekuje na drugie zatwierdzenie**: Określa to, że faktura znajduje się w fazie oczekiwania na drugie zatwierdzenie. Zazwyczaj jest to krok zaprojektowany w celu zapewnienia dodatkowego nadzoru przed ostatecznym przetworzeniem.
* **Pole dokumentu Podtyp faktury to Równa się Faktura zakupu**: To dodatkowo zawęża zastosowanie tej reguły tylko do tych faktur, które są sklasyfikowane jako "Faktury zakupu", odróżniając je od innych podtypów faktur.
* **Logika Jednostkowa cena w potwierdzeniu zamówienia Nie Równa się zamówieniu zakupu**: Ta kontrola logiczna jest kluczowa, ponieważ porównuje cenę jednostkową podaną w potwierdzeniu zamówienia z ceną jednostkową w oryginalnym zamówieniu zakupu. Akcja jest wyzwalana, jeśli te wartości się nie zgadzają, co może wskazywać na rozbieżność, która wymaga rozwiązania.

#### Akcja (Wtedy…):

* **Przypisz użytkownika z pola Nazwa kupującego, użyj użytkownika Użytkownik jako awaryjnego**: Jeśli spełnione są określone warunki (czyli występuje niezgodność w cenach jednostkowych), faktura jest automatycznie przypisywana do kupującego (nazwa określona w polu 'Nazwa kupującego') w celu dalszej weryfikacji. Jeśli pole 'Nazwa kupującego' jest puste lub nieokreślone, domyślny użytkownik (prawdopodobnie administrator lub inny wyznaczony pracownik) jest przypisywany jako awaryjny do obsługi zatwierdzenia.

#### Cel tej reguły:

* **Zapewnienie dokładności i zgodności**: Ta reguła jest kluczowa dla zapewnienia, że proces fakturowania jest dokładny i zgodny z ustalonymi warunkami. Poprzez wyzwalanie przeglądu w przypadku rozbieżności w cenach jednostkowych, system pomaga zapobiegać błędom finansowym lub potencjalnym oszustwom.
* **Usprawnienie zatwierdzeń**: Automatyzacja przypisania do przeglądu na podstawie konkretnych rozbieżności pomaga usprawnić proces zatwierdzania i zapewnia, że problemy są natychmiast rozwiązywane przez odpowiedni personel.
* **Nadzór finansowy**: Wymaganie drugiego zatwierdzenia, zwłaszcza opartego na dopasowaniu cen, wzmacnia kontrole finansowe i odpowiedzialność w organizacji.
