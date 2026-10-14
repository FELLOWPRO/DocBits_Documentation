# Set Checkbox to

<figure><img src="../../../../.gitbook/assets/image (279).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Ta karta przepływu pracy służy do ustawienia pola wyboru na określoną wartość (true lub false) na podstawie warunków zdefiniowanych w sekcjach **"Where"** i **"And"**. Zapewnia prosty, ale skuteczny sposób automatyzacji aktualizacji pól wyboru, gdy spełnione są określone kryteria, zapewniając usprawnione przetwarzanie dokumentów.

## **Komponenty karty:**

1. **Field Name:**
   * **Opis**: Określa pole, w którym zostanie ustawione pole wyboru.
   * **Szczegóły**: Pole wyboru do aktualizacji jest identyfikowane przez nazwę pola.
2. **Boolean**
   * **Opis**: Definiuje wartość, na którą zostanie ustawione pole wyboru, gdy warunki w sekcjach **Where** i **And** są oba prawdziwe.
   * **Opcje**:
     * **True**: Pole wyboru zostanie ustawione na **true**, jeśli warunki są spełnione.
     * **False**: Pole wyboru zostanie ustawione na **false**, jeśli warunki są spełnione.

## **Funkcjonalność:**

* **Ocena warunku**: System ocenia warunki zarówno w sekcji **"Where"**, jak i **"And"**&#x20;
* **Wykonanie akcji**: Jeśli zarówno **"Where"**, jak i **"And Sections"** są prawdziwe, pole wyboru zostanie zaktualizowane do określonej wartości (true lub false). Jeśli którykolwiek z warunków jest fałszywy, nie są podejmowane żadne akcje, a pole wyboru pozostaje bez zmian.

## **Konfiguracja:**

Aby skonfigurować tę kartę, użytkownicy muszą:

1. **Określić docelowe pole wyboru**, które zostanie ustawione na true lub false, gdy warunki są spełnione.
2. **Wybrać wartość (true lub false)**, na którą zostanie ustawione pole wyboru po ocenie warunku.
3. Karta wykonuje swoją akcję tylko wtedy, gdy oba warunki w sekcjach **"Where"** i **"And Sections"** są prawdziwe.

## **Podsumowanie:**

Karta przepływu pracy **"Set Checkbox"** jest prostym i skutecznym narzędziem automatyzacji do aktualizacji pól wyboru na podstawie określonych warunków. Zapewniając, że zarówno **"Where"**, jak i **"And Sections"** są spełnione, umożliwia użytkownikom automatyzację procesów i redukcję ręcznej interwencji, zapewniając płynniejsze i bardziej efektywne przetwarzanie dokumentów.
