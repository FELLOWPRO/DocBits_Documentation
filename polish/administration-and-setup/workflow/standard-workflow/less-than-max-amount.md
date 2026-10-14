# Less than Max Amount

<figure><img src="../../../../.gitbook/assets/docbits_invoice.png" alt="DocBits Faktura"><figcaption></figcaption></figure>

Ten tytuł sugeruje, że konfigurowana reguła lub warunek został zaprojektowany do obsługi faktur, w których łączna kwota jest mniejsza lub równa określonej maksymalnej kwocie.

#### Konfiguracja reguły:

1. **When…**
   * **Document Type is Invoice**: Ten warunek sprawdza, czy przetwarzany dokument jest fakturą. Jest to kluczowe, aby zapewnić, że reguła ma zastosowanie tylko do faktur, a nie do innych typów dokumentów.
2. **And…**
   * **Document Status is Pending Approval**: To określa, że faktura musi mieć status "Pending Approval". Ta kontrola statusu zapewnia, że reguła ma zastosowanie tylko do faktur oczekujących na zatwierdzenie.
   * **Compare two fields: Total Amount Less Or Equals Approver Max Amount**: Ten warunek porównuje łączną kwotę faktury z maksymalną autoryzowaną kwotą osoby zatwierdzającej. Jeśli łączna kwota faktury jest mniejsza lub równa tej maksymalnej kwocie, reguła przechodzi do następnego kroku. Prawdopodobnie obejmuje to poziom tolerancji, który dopuszcza niewielkie odchylenia w określonych granicach.

#### Action (Then…):

* **Assign user from field Approver Name, use user User as fallback**: Jeśli określone warunki są spełnione, faktura jest automatycznie przypisywana do osoby zatwierdzającej, której nazwa jest określona w polu. Jeśli to pole jest puste lub niedostępne, przypisywany jest domyślny użytkownik (prawdopodobnie administrator lub inny wyznaczony pracownik) jako rozwiązanie zapasowe do obsługi zatwierdzenia.

#### Elementy interfejsu:

* **Add Card**: Ten przycisk prawdopodobnie umożliwia użytkownikom dodawanie kolejnych warunków lub akcji do reguły, zwiększając elastyczność i specyficzność przepływu pracy.
* **Save**: Zapisuje skonfigurowaną regułę w systemie.

#### Cel tej reguły:

Ta konfiguracja została zaprojektowana w celu usprawnienia procesu zatwierdzania faktur poprzez automatyczne kierowanie faktur do odpowiedniej osoby zatwierdzającej na podstawie kwoty oraz zapewnienie, że tylko te w określonym progu są obsługiwane w ten zautomatyzowany sposób. Pomaga to w zarządzaniu kontrolami finansowymi i przyspiesza przepływ pracy poprzez redukcję ręcznych kontroli dla każdej faktury.

\
