# Reject the Document

<figure><img src="../../../../.gitbook/assets/image (282).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Karta przepływu pracy **"Reject the Document"** służy do oznaczenia dokumentu jako odrzuconego w ramach przepływu pracy. Akcja ta wstrzymuje postęp dokumentu i uniemożliwia mu przejście do następnego etapu w przepływie pracy. Zapewnia, że dokumenty, które nie spełniają niezbędnych warunków lub kryteriów, są oznaczane i blokowane przed dalszym przetwarzaniem.

## **Komponenty karty:**

1. **Rejection Status**
   * **Opis**: Ten komponent oznacza dokument jako odrzucony, sygnalizując, że nie spełnił wymaganych warunków zatwierdzenia.
   * **Szczegóły**: Po wyzwoleniu ta karta aktualizuje status dokumentu na "rejected". Decyzja ta jest podejmowana na podstawie warunków ustawionych w sekcjach **"Where"** i **"And Sections."**

## **Funkcjonalność:**

* **Ocena warunku**: System ocenia warunki ustawione w sekcjach **"Where"** i **"And Sections"**.
  * Jeśli **oba warunki są prawdziwe**, dokument zostanie odrzucony.
  * Jeśli **którykolwiek z warunków jest fałszywy**, karta nie zostanie wykonana, a status dokumentu pozostanie bez zmian.
* **Wykonanie akcji**: Gdy warunki są spełnione, dokument zostaje oznaczony jako odrzucony. Akcja ta zapewnia, że tylko dokumenty spełniające określone kryteria są kierowane dalej, podczas gdy inne są oznaczane i wstrzymywane do przeglądu lub korekty.

## **Podsumowanie:**

Karta przepływu pracy **"Reject the Document"** jest niezbędnym narzędziem do kontrolowania przepływu dokumentów w zautomatyzowanych procesach. Umożliwiając odrzucanie niezgodnych dokumentów, zapewnia, że tylko prawidłowe i dokładne dokumenty są kontynuowane w przepływie pracy, poprawiając efektywność i dokładność w zarządzaniu dokumentami.
