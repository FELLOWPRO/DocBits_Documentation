# Poniżej kwoty maksymalnej

<figure><img src="../../../.gitbook/assets/docbits_invoice_less_than_max.png" alt="DocBits Faktura Less Than Max"><figcaption></figcaption></figure>

Ten tytuł sugeruje, że konfigurowana reguła lub warunek jest przeznaczony do obsługi faktur, których całkowita kwota jest mniejsza lub równa określonej kwocie maksymalnej.

#### Konfiguracja reguły:

1. **Gdy…**
   * **Typ dokumentu to Faktura**: Ten warunek sprawdza, czy przetwarzany dokument jest fakturą. Jest to kluczowe dla zapewnienia, że reguła ma zastosowanie tylko do faktur, a nie do innych rodzajów dokumentów.
2. **Oraz…**
   * **Status dokumentu to Oczekuje na zatwierdzenie**: Określa to, że faktura musi znajdować się w statusie „Oczekiwanie na zatwierdzenie”. To sprawdzenie statusu gwarantuje, że reguła ma zastosowanie tylko do faktur oczekujących na zatwierdzenie.
   * **Porównaj dwa pola: Suma całkowita mniejsza lub równa Maksymalna kwota zatwierdzającego**: Ten warunek porównuje całkowitą kwotę faktury z maksymalną upoważnioną kwotą zatwierdzającego. Jeśli całkowita kwota faktury jest mniejsza lub równa tej kwocie maksymalnej, reguła przechodzi do następnego kroku. Prawdopodobnie obejmuje to poziom tolerancji, który pozwala na niewielkie odchylenia w określonych granicach.

#### Akcja (Wtedy…):

* **Przypisz użytkownika z pola Nazwisko zatwierdzającego, użyj użytkownika Użytkownik jako rezerwowego**: Jeśli określone warunki zostaną spełnione, faktura jest automatycznie przypisywana do zatwierdzającego, którego nazwisko jest określone w polu. Jeśli to pole jest puste lub niedostępne, do obsługi zatwierdzenia przypisywany jest użytkownik domyślny (prawdopodobnie administrator lub inny wyznaczony pracownik).

#### Elementy interfejsu:

* **Dodaj kartę**: Ten przycisk prawdopodobnie pozwala użytkownikom dodać więcej warunków lub działań do reguły, zwiększając elastyczność i specyfikę przepływu pracy.
* **Zapisz**: Zapisuje skonfigurowaną regułę w systemie.

#### Cel tej reguły:

Ta konfiguracja ma na celu usprawnienie procesu zatwierdzania faktur poprzez automatyczne kierowanie ich do odpowiedniego zatwierdzającego na podstawie kwoty i zapewnienie, że tylko te mieszczące się w określonym progu są obsługiwane w ten zautomatyzowany sposób. Pomaga to w zarządzaniu kontrolami finansowymi i przyspiesza przepływ pracy poprzez ograniczenie ręcznych kontroli każdej faktury.