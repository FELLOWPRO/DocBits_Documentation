# Set to

<figure><img src="../../../../.gitbook/assets/image (278).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Ta karta przepływu pracy służy do automatycznego ustawienia określonego pola w dokumencie na predefiniowaną wartość tekstową na podstawie warunków zdefiniowanych w sekcjach **"Where"** i **"And Sections."** Umożliwia użytkownikom usprawnienie wprowadzania danych poprzez zapewnienie, że pola są wypełniane spójnymi wartościami, gdy spełnione są określone kryteria.

## **Komponenty karty:**

1. **Field Name**
   * **Opis**: Określa pole, które zostanie zaktualizowane wartością tekstową.&#x20;
   * **Szczegóły**: Wybrane pole zostanie zaktualizowane określoną wartością tekstową, jeśli warunki w sekcjach **"Where"** i **"And Sections"** są spełnione.
2. **Text**
   * **Opis**: Definiuje wartość tekstową, która zostanie ustawiona w polu docelowym, gdy warunki są prawdziwe.
   * **Szczegóły**: Może to być niestandardowa wiadomość, status lub predefiniowana wartość, którą użytkownik chce wpisać do pola. Tekst powinien być zgodny z oczekiwanym formatem wejściowym pola (np. alfanumeryczny, data lub inne typy informacji tekstowych).

## **Funkcjonalność:**

* **Ocena warunku**: System ocenia warunki w sekcjach **"Where"** i **"And Sections"**:
  * Jeśli **oba warunki są prawdziwe**, zostaną wykonane akcje zdefiniowane w **"Then Section"**. W szczególności pole docelowe (Field Name) zostanie wypełnione określonym tekstem.
  * Jeśli **sekcja "Where" lub "And" jest fałszywa**, nie jest podejmowana żadna akcja, a pole pozostaje bez zmian. Akcje **Then Section** są całkowicie pomijane, jeśli którykolwiek z warunków jest fałszywy.
* **Wykonanie akcji**: Jeśli oba warunki w sekcjach **"Where"** i **"And Sections"** są spełnione, system automatycznie wypełnia określone pole wybraną wartością tekstową. Jeśli warunki nie są spełnione, nie są wprowadzane żadne zmiany w polu.

## **Konfiguracja:**

Aby skonfigurować tę kartę:

1. **Wybierz pole** (Field Name), które zostanie zaktualizowane wartością tekstową. Dostępne pola w dokumencie są wymienione do wyboru.
2. **Określ wartość tekstową**, która zostanie wpisana do pola docelowego, gdy warunki są prawdziwe.
3. Akcja zostanie wykonana tylko wtedy, gdy warunki w sekcjach **"Where"** i **"And Sections"** są prawdziwe.

## **Podsumowanie:**

Karta przepływu pracy **"Set Field to Text"** oferuje prosty sposób automatyzacji wypełniania wartości tekstowych w określonych polach dokumentu na podstawie predefiniowanych warunków. Redukuje to ręczne wprowadzanie danych i zapewnia spójność w przetwarzaniu dokumentów, czyniąc ją przydatnym narzędziem do automatyzacji przepływów pracy i zwiększania efektywności.
