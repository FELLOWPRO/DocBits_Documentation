# Above Max Amount

<figure><img src="../../../../.gitbook/assets/docbits_invoice_2.png" alt="DocBits Faktura 2"><figcaption></figcaption></figure>

Ten tytuł wskazuje, że reguła została zaprojektowana do obsługi przypadków, w których suma faktury jest większa niż maksymalna kwota, do której obsługi upoważniony jest osoba zatwierdzająca.

#### Konfiguracja reguły:

1. **When…**
   * **Document Type is Invoice**: Ten warunek zapewnia, że reguła ma zastosowanie tylko do faktur, co jest niezbędne do prawidłowego kierowania przepływem pracy.
2. **And…**
   * **Document Status is Pending Approval**: Faktura musi mieć status "Pending Approval". Ten status jest kluczowy, aby zapewnić, że reguła jest stosowana do faktur, które są nadal przetwarzane i nie zostały jeszcze sfinalizowane.
   * **Compare two fields: Total Amount Greater Than Approver Max Amount**: Ten warunek sprawdza, czy łączna kwota faktury przekracza maksymalną kwotę, którą osoba zatwierdzająca może obsłużyć. To porównanie może również obejmować ustawienie tolerancji, dopuszczając niewielkie różnice w oparciu o wstępnie zdefiniowane kryteria.

#### Action (Then…):

* **Assign user from field Next Level Approver, use user User as fallback**: Jeśli faktura przekracza określoną maksymalną kwotę, jest automatycznie przypisywana do osoby zatwierdzającej wyższego szczebla, wskazanej w polu 'Next Level Approver'. Jeśli to pole nie jest wypełnione lub określony użytkownik jest niedostępny, używany jest domyślny użytkownik (prawdopodobnie administrator lub inny wyznaczony pracownik) jako rozwiązanie zapasowe, aby zapewnić, że faktura zostanie przejrzana bez opóźnień.

#### Elementy interfejsu:

* **Add Card**: Ta opcja umożliwia dodawanie dodatkowych warunków lub akcji do reguły, zapewniając elastyczność w obsłudze złożonych scenariuszy.
* **Save**: Ten przycisk zapisuje konfigurację reguły w systemie.

#### Cel tej reguły:

Celem tej reguły jest zapewnienie, że faktury przekraczające określone progi finansowe są przeglądane przez osoby zatwierdzające z odpowiednimi poziomami uprawnień. Pomaga to w utrzymaniu kontroli i nadzoru finansowego, zapewniając, że wydatki są przeglądane przez personel z wymaganymi limitami zatwierdzania, chroniąc tym samym organizację przed nieautoryzowanymi lub niewłaściwymi wydatkami.

Ta reguła, podobnie jak poprzednia, pomaga zautomatyzować przepływ pracy, redukując wysiłek ręczny i zwiększając zgodność z politykami finansowymi organizacji. Jest to przykład, jak automatyzacja przepływu pracy może być skutecznie wykorzystywana do zarządzania złożonymi procesami finansowymi w firmie.
