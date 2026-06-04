# Assign document to matching sub organization

<figure><img src="../../../../.gitbook/assets/image (303).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Karta przepływu pracy **"Assign Document to Matching Sub-Organization Based on Field"** dynamicznie przypisuje dokument do sub-organizacji na podstawie określonego pola w dokumencie. Jeśli nie zostanie znaleziona pasująca sub-organizacja, karta używa predefiniowanej zapasowej sub-organizacji.

## **Komponenty karty:**

1. **Field Name**
   * **Opis:** Określa pole dokumentu, które ma być użyte do ustalenia pasującej sub-organizacji.
   * **Szczegóły:** Karta wyszukuje wartość w określonym polu, aby dopasować ją do dostępnej sub-organizacji.
2. **Sub-Organization (Fallback)**
   * **Opis:** Definiuje zapasową sub-organizację, która ma być użyta, jeśli nie zostanie znalezione dopasowanie w określonym polu.
   * **Szczegóły:** Jeśli wartość pola nie pasuje do żadnej sub-organizacji, dokument zostanie przypisany do wybranej zapasowej sub-organizacji.

## **Funkcjonalność:**

* **Ocena warunku:**\
  Karta wykonuje swoją akcję tylko wtedy, gdy zarówno **"Where"**, jak i **"And Sections"** są prawdziwe.
* **Dynamiczne przypisanie:**\
  Karta sprawdza wartość określonego pola i przypisuje dokument do sub-organizacji, która odpowiada tej wartości.
* **Mechanizm zapasowy:**\
  Jeśli nie zostanie znaleziona pasująca sub-organizacja, dokument jest przypisywany do zapasowej sub-organizacji.

## **Konfiguracja:**

* **Select Field Name:**\
  Wybierz pole z dokumentu zawierające wartość do dopasowania do sub-organizacji.
* **Select Fallback Sub-Organization:**\
  Wybierz sub-organizację, która zostanie użyta, jeśli nie zostanie znalezione dopasowanie w polu dokumentu.

## **Podsumowanie:**

Karta przepływu pracy **"Assign Document to Matching Sub-Organization Based on Field"** oferuje elastyczność, dynamicznie kierując dokumenty do odpowiedniej sub-organizacji, z dodatkową opcją zapasową, aby zapewnić, że żaden dokument nie pozostanie nieprzypisany.
