# Invert Checkbox

<figure><img src="../../../../.gitbook/assets/image (280).png" alt=""><figcaption></figcaption></figure>

## **Cel:**

Ta karta przepływu pracy służy do odwrócenia bieżącego stanu pola wyboru. Jeśli pole wyboru jest zaznaczone (true), zostanie odznaczone (false) i odwrotnie. Odwrócenie następuje na podstawie warunków ustawionych w sekcjach **"Where"** i **"And Sections."** Ta karta pomaga zautomatyzować przepływy pracy, w których warunek wymaga przełączania pola wyboru na podstawie określonych kryteriów.

## **Komponenty karty:**

1. **Field Name**
   * **Opis**: Określa pole wyboru, które ma zostać odwrócone.&#x20;
   * **Szczegóły**: Wybrane pole wyboru będzie miało przełączony stan z true na false lub z false na true na podstawie jego bieżącego stanu.

## **Funkcjonalność:**

* **Ocena warunku**: System ocenia warunki zdefiniowane w sekcjach **"Where"** i **"And Sections"**:
  * Jeśli **oba warunki są prawdziwe**, zostanie wykonana akcja **"Then Section"**, co w tym przypadku oznacza przełączenie pola wyboru.
  * Jeśli **którykolwiek z warunków jest fałszywy**, karta nie zostanie wykonana i nie zostanie wprowadzona żadna zmiana w polu wyboru.
* **Wykonanie akcji**: Jeśli warunki w sekcjach **"Where"** i **"And Sections"** są prawdziwe, stan pola wyboru zostanie odwrócony:
  * Jeśli pole wyboru jest zaznaczone (true), zostanie odznaczone (false).
  * Jeśli pole wyboru jest odznaczone (false), zostanie zaznaczone (true).

## **Konfiguracja:**

Aby skonfigurować tę kartę, użytkownicy muszą:

1. **Wybrać pole wyboru** (Field Name), które zostanie odwrócone. Dostępne pola wyboru w dokumencie są wymienione do wyboru.
2. Pole wyboru zostanie odwrócone tylko wtedy, gdy warunki w sekcjach **"Where"** i **"And Sections"** są prawdziwe.

## **Podsumowanie:**

Karta przepływu pracy **"Invert checkbox \[Field Name]"** oferuje proste, ale potężne narzędzie automatyzacji do przełączania wartości pól wyboru na podstawie określonych warunków. Redukując potrzebę ręcznego dostosowywania pól wyboru, karta ta zwiększa efektywność przetwarzania dokumentów i zapewnia spójność w przepływach pracy.
