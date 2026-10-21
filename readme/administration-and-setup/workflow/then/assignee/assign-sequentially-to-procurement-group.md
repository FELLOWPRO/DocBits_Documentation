# Przypisz sekwencyjnie do grupy zaopatrzenia

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-3b31b4f42710-pl.png" alt="Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs." width="563"><figcaption><p>Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs.</p></figcaption></figure>

## **Cel**

Karta przepływu pracy "**Przypisz dokument sekwencyjnie do grupy zaopatrzenia**" umożliwia sekwencyjne przypisywanie dokumentów do określonej grupy zakupowej. Wartość priorytetu określa kolejność przypisywania, przy czym niższe liczby reprezentują wyższy priorytet.

## **Komponenty karty**

1. **Grupa**
   * **Opis**: Pole wprowadzania tekstu, w którym można wprowadzić nazwę grupy zakupowej.
   * **Szczegóły**: Określa grupę zakupową, do której zostanie przypisany dokument.
2. **Priorytet (wartość)**
   * **Opis**: Numeryczne pole wprowadzania, w którym można ustawić poziom priorytetu dla grupy.
   * **Szczegóły**: Niższe liczby oznaczają wyższy priorytet, zapewniając przypisywanie dokumentów do grup w rosnącej kolejności priorytetu.

## **Funkcjonalność**

* **Przypisanie dokumentu**:\
  Karta przypisuje dokumenty do określonej grupy zakupowej w sposób sekwencyjny.\
  Wartości priorytetu dyktują kolejność przypisywania, przy czym niższe liczby są przetwarzane jako pierwsze.

## **Konfiguracja**

1. Dodaj kartę **Przypisz dokument sekwencyjnie** do swojego przepływu pracy.
2. Skonfiguruj pole **Grupa**:
   * Wprowadź nazwę grupy zakupowej w polu tekstowym.
3. Skonfiguruj pole **Priorytet (wartość)**:
   * Wprowadź wartość liczbową, aby ustawić priorytet przypisania.
4. Zapisz i aktywuj przepływ pracy, aby zastosować konfigurację.

## **Podsumowanie**

Karta przepływu pracy "Assign the Document Sequentially to the Procurement Group" zapewnia efektywną alokację dokumentów do grup zakupowych na podstawie priorytetu. Zwiększa to efektywność organizacyjną i zarządzanie zadaniami.

<!-- workflow-card-practical-example-20261021 -->

## Praktyczny przykład

**Kiedy używać:** Nadaj priorytet grupie zaopatrzeniowej w ramach przeglądu dokumentów.

**Konfiguracja:** Wybierz `Demo Procurement` i priorytet `10`.

**Oczekiwany wynik i kontrprzykład:** Dokument otrzymuje przypisanie grupy zaopatrzeniowej z priorytetem `10`. Sprawdź, czy w późniejszych przypisaniach używane są zamierzone wyższe priorytety liczbowe.

To jest ilustracyjna konfiguracja i oczekiwany wynik. Korzystaj z pól, użytkowników i grup skonfigurowanych w Twojej organizacji testowej; nie jest to twierdzenie, że ten przykład został wykonany.
