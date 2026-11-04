# Powyżej kwoty maksymalnej

<figure><img src="../../../.gitbook/assets/docbits_rule_above_max.png" alt="DocBits Reguła Above Max"><figcaption></figcaption></figure>

Ten tytuł wskazuje, że reguła jest przeznaczona do obsługi przypadków, w których suma faktury jest większa niż maksymalna kwota, do której zatwierdzania upoważniony jest zatwierdzający.

#### Konfiguracja reguły:

1. **Gdy…**
   * **Typ dokumentu to Faktura**: Ten warunek zapewnia, że reguła ma zastosowanie tylko do faktur, co jest niezbędne do prawidłowego kierowania przepływem pracy.
2. **Oraz…**
   * **Status dokumentu to Oczekuje na zatwierdzenie**: Faktura musi znajdować się w statusie „Oczekiwanie na zatwierdzenie”. Ten status jest kluczowy, aby upewnić się, że reguła jest stosowana do faktur, które są nadal przetwarzane i nie zostały jeszcze sfinalizowane.
   * **Porównaj dwa pola: Suma całkowita większa niż Maksymalna kwota zatwierdzającego**: Ten warunek sprawdza, czy całkowita kwota faktury przekracza maksymalną kwotę, którą dany zatwierdzający może obsłużyć. Porównanie to może również obejmować ustawienie tolerancji, pozwalające na niewielkie odchylenia na podstawie predefiniowanych kryteriów.

#### Akcja (Wtedy…):

* **Przypisz użytkownika z pola Zatwierdzający następnego poziomu, użyj użytkownika Użytkownik jako rezerwowego**: Jeśli faktura przekracza określoną kwotę maksymalną, jest ona automatycznie przypisywana do zatwierdzającego wyższego szczebla, wskazanego w polu „Zatwierdzający następnego poziomu”. Jeśli to pole nie jest wypełnione lub wskazany użytkownik jest niedostępny, używany jest użytkownik domyślny (prawdopodobnie administrator lub inny wyznaczony pracownik), aby zapewnić przegląd faktury bez opóźnień.

#### Elementy interfejsu:

* **Dodaj kartę**: Ta opcja umożliwia dodanie dodatkowych warunków lub działań do reguły, zapewniając elastyczność w rozwiązywaniu złożonych scenariuszy.
* **Zapisz**: Ten przycisk zapisuje konfigurację reguły w systemie.

#### Cel tej reguły:

Celem tej reguły jest zapewnienie, że faktury przekraczające określone progi finansowe są przeglądane przez zatwierdzających z odpowiednimi poziomami uprawnień. Pomaga to w utrzymaniu kontroli finansowej i nadzoru, zapewniając, że wydatki są sprawdzane przez personel z wymaganymi limitami zatwierdzeń, chroniąc w ten sposób organizację przed nieautoryzowanymi lub niewłaściwymi wydatkami.

Reguła ta, podobnie jak poprzednia, pomaga zautomatyzować przepływ pracy, redukując wysiłek ręczny i zwiększając zgodność z polityką finansową organizacji. Jest to przykład tego, jak automatyzacja przepływu pracy może być skutecznie wykorzystywana do zarządzania złożonymi procesami finansowymi w firmie.