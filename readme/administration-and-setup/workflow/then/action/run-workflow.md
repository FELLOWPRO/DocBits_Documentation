# Run Workflow

<figure><img src="../../../../.gitbook/assets/image (307).png" alt="" width="563"><figcaption></figcaption></figure>

## Cel:

Karta **"Run Workflow"** umożliwia użytkownikom dynamiczne wykonanie wybranego przepływu pracy z listy dostępnych przepływów pracy. Ta karta jest przydatna do automatyzacji procesów, w których wiele przepływów pracy jest ze sobą powiązanych, umożliwiając usprawnione operacje.

## Komponenty karty:

1. **Workflow**
   * **Opis:** Określa przepływ pracy, który ma zostać wykonany, gdy warunki są prawdziwe.
   * **Szczegóły:** Do wyboru udostępniana jest lista rozwijana wszystkich dostępnych przepływów pracy.

## Funkcjonalność:

* **Ocena warunku:** Karta wykonuje wybrany przepływ pracy tylko wtedy, gdy zarówno **"Where"**, jak i **"And Sections"** są prawdziwe.
  * Jeśli którykolwiek z warunków jest fałszywy, nie jest podejmowana żadna akcja, a przepływ pracy pozostaje niewyzwolony.
* **Wykonanie przepływu pracy:**
  * Gdy warunki są spełnione, określony przepływ pracy jest wyzwalany automatycznie.
  * Jeśli warunki nie są spełnione, żaden przepływ pracy nie jest wykonywany.

## Konfiguracja:

1. **Select Workflow:** Wybierz przepływ pracy do wyzwolenia z **listy rozwijanej** dostępnych przepływów pracy.
2. **Define Conditions:** Skonfiguruj sekcje **"Where"** i **"And Sections"**, aby określić kryteria, które muszą zostać spełnione, aby przepływ pracy został wykonany.

## Podsumowanie:

Karta **"Run Workflow"** oferuje wygodny i efektywny sposób łączenia przepływów pracy, automatyzując wieloetapowe procesy z łatwością. Zapewniając, że warunki w sekcjach **"Where"** i **"And Sections"** są spełnione, użytkownicy mogą dynamicznie wykonywać przepływy pracy i redukować ręczną interwencję.
