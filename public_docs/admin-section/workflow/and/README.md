# I

## Zrozumienie kart „And”

### **Cel kart „And”**

* Karty **And** pełnią rolę kart warunkowych, które określają kryteria, które muszą zostać spełnione, aby workflow mógł kontynuować. Skutecznie działają jako logiczni operatorzy „AND”, co oznacza, że wszystkie warunki określone w tych kartach muszą zostać spełnione, aby następna akcja została uruchomiona.

#### Kategorie kart „And”

Z zrzutów ekranu wynika, że te karty obejmują szeroki zakres warunków, w tym:

*   **Porównaj z zamówieniem zakupu**:

* Warunki związane z walidacją i porównywaniem do zamówień zakupu, takie jak porównywanie dat dostawy, cen jednostkowych lub różnic w ilości. Są one kluczowe dla zapewnienia, że transakcje są zgodne z ustalonymi warunkami.



<figure><img src="../../../.gitbook/assets/And1.png" alt=""><figcaption></figcaption></figure>

*   **Pole dokumentu**:

* Dotyczą one warunków opartych na konkretnych polach w dokumentach, takich jak zaznaczone pola wyboru, porównanie wartości pól lub zapewnienie, że pole dokumentu spełnia określoną tolerancję. Jest to szczególnie istotne dla integralności danych i automatycznych kontroli w formularzach lub systemach zarządzania dokumentami.



<figure><img src="../../../.gitbook/assets/And2.png" alt=""><figcaption></figcaption></figure>

* **Dokument**:
* Warunki oparte na cechach dokumentu, takie jak typ lub powiązanie z określoną podorganizacją. Te warunki mogą kierować workflow na podstawie kategoryzacji dokumentów lub zaangażowania działowego.

<figure><img src="../../../.gitbook/assets/And3.png" alt=""><figcaption></figcaption></figure>

* **Logika**:
* Warunki logiczne, które mogą obejmować oceny takie jak „Kontynuuj z szansą na X%” lub wykonywanie żądań HTTPS, które są istotne dla integracji i podejmowania decyzji probabilistycznych w ramach workflowów.

<figure><img src="../../../.gitbook/assets/And4.png" alt=""><figcaption></figcaption></figure>

*   **Status**:

* Skupiając się na statusie dokumentów lub zadań, te warunki zapewniają, że tylko elementy w określonych stanach uruchamiają określone workflowy, co jest istotne dla zarządzania procesami opartymi na statusie.

<figure><img src="../../../.gitbook/assets/And5.png" alt=""><figcaption></figcaption></figure>

* **Tabela**:
* Dotyczą one warunków opartych na danych tabelarycznych, takich jak dopasowywanie wzorców regex lub porównywanie wartości w tabeli. Takie warunki są niezbędne do walidacji i manipulacji dużymi zbiorami danych.

<figure><img src="../../../.gitbook/assets/And6.png" alt=""><figcaption></figcaption></figure>

*   **Wykonawca**:

* Warunki oparte na wykonawcach zadań lub dokumentów. Zapewnia to, że działania są podejmowane tylko wtedy, gdy zaangażowani są określeni użytkownicy, zwiększając odpowiedzialność i specyficzność zadań.

<figure><img src="../../../.gitbook/assets/And7.png" alt=""><figcaption></figcaption></figure>

### Zastosowanie praktyczne

Te karty „And” są konfigurowane w ramach workflowu w celu przeprowadzania kontroli i walidacji, które zapewniają, że proces ścisłe przestrzega reguł biznesowych i standardów integralności danych. Na przykład:

* **Workflow może użyć karty „And”, aby zweryfikować, czy łączna kwota faktury odpowiada zamówieniu zakupu przed uruchomieniem płatności.**
* **Inny workflow mógłby użyć karty „And”, aby upewnić się, że dokument jest sprawdzany przez określonych członków zespołu, zanim przejdzie do następnego etapu.**

### Podsumowanie

Karty „And” są fundamentalnym elementem systemów workflow, które wymagają precyzyjnej kontroli nad wykonaniem procesu na podstawie wielu warunków. Zapewniają, że każdy krok workflowu kontynuuje się tylko wtedy, gdy wszystkie niezbędne kryteria są dokładnie spełnione, co automatyzuje złożone drzewa decyzyjne w procesach biznesowych.

Zrozumienie i poprawna konfiguracja tych kart jest kluczowe dla wykorzystania pełnych możliwości systemu zarządzania workflowem w celu zwiększenia efektywności, dokładności i zgodności w ramach procesów organizacyjnych.
