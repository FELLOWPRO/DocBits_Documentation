---
description: Konfiguracja warunków I w przepływach pracy DocBits
---

# And

## Zrozumienie kart "And"

### **Cel kart "And":**

* Karty **And** pełnią funkcję kart warunków, które określają kryteria, jakie muszą zostać spełnione, aby przepływ pracy mógł być kontynuowany. Działają one efektywnie jako logiczne operatory "AND", co oznacza, że wszystkie warunki określone na tych kartach muszą być spełnione, aby kolejna akcja została wyzwolona.

#### Kategorie kart "And"

Na podstawie zrzutów ekranu widać, że karty te obejmują szeroki zakres warunków, które obejmują:

* **Compare with Purchase Order**:
  * Warunki związane z walidacją i porównaniem z zamówieniami zakupu, takie jak porównywanie dat dostawy, cen jednostkowych lub różnic w ilości. Są one kluczowe dla zapewnienia zgodności transakcji z uzgodnionymi warunkami.

<figure><img src="../../../.gitbook/assets/image (14) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Document Field**:
  * Dotyczą one warunków opartych na określonych polach w dokumentach, takich jak zaznaczone pola wyboru, porównanie wartości pól lub sprawdzanie, czy pole dokumentu mieści się w określonej tolerancji. Jest to szczególnie ważne dla integralności danych oraz automatycznych kontroli w formularzach lub systemach zarządzania dokumentami.

<figure><img src="../../../.gitbook/assets/image (15) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Date & Time:**
  * Warunki oparte na datach i godzinach

<figure><img src="../../../.gitbook/assets/image (17) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Document**:
  * Warunki oparte na cechach dokumentu, takich jak typ lub powiązanie z określoną sub-organizacją. Warunki te mogą kierować przepływami pracy na podstawie kategoryzacji dokumentu lub zaangażowania działu.

<figure><img src="../../../.gitbook/assets/image (18) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Logic**:
  * Warunki logiczne, które mogą obejmować oceny typu "Continue with a chance of X%" lub wykonywanie żądań HTTPS, kluczowe dla integracji oraz podejmowania decyzji probabilistycznych w ramach przepływów pracy.

<figure><img src="../../../.gitbook/assets/image (19) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Status**:
  * Skupiając się na statusie dokumentów lub zadań, warunki te zapewniają, że tylko elementy w określonych stanach wyzwalają konkretne przepływy pracy, co jest kluczowe dla zarządzania procesami opartego na statusie.

<figure><img src="../../../.gitbook/assets/image (20) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Table**:
  * Dotyczą one warunków opartych na danych tabelarycznych, takich jak dopasowywanie wzorców regex lub porównywanie wartości w tabeli. Takie warunki są niezbędne do walidacji i manipulacji dużymi zbiorami danych.

<figure><img src="../../../.gitbook/assets/image (22) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Assignee**:
  * Warunki oparte na osobach przypisanych do zadania lub dokumentu. Zapewnia to, że akcje są podejmowane tylko wtedy, gdy zaangażowani są określeni użytkownicy, co zwiększa odpowiedzialność i precyzję zadań.

<figure><img src="../../../.gitbook/assets/image (24) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Praktyczne zastosowanie

Te karty "And" są konfigurowane w przepływie pracy w celu przeprowadzania kontroli i walidacji, które zapewniają, że proces ściśle przestrzega reguł biznesowych i standardów integralności danych. Na przykład:

* **Przepływ pracy może używać karty "And", aby zweryfikować, że całkowita kwota faktury jest zgodna z zamówieniem zakupu, zanim wyzwoli płatność.**
* **Inny przepływ pracy może używać karty "And", aby zapewnić, że dokument zostanie sprawdzony przez określonych członków zespołu, zanim przejdzie do następnego etapu.**

### Podsumowanie

Karty "And" są podstawowym elementem systemów przepływu pracy, które wymagają precyzyjnej kontroli nad wykonywaniem procesu na podstawie wielu warunków. Zapewniają one, że każdy krok przepływu pracy jest realizowany tylko wtedy, gdy wszystkie niezbędne kryteria zostaną w pełni spełnione, automatyzując w ten sposób złożone drzewa decyzyjne w procesach biznesowych.

Zrozumienie i prawidłowe skonfigurowanie tych kart jest kluczowe dla wykorzystania pełnych możliwości systemu zarządzania przepływem pracy w celu zwiększenia wydajności, dokładności i zgodności w procesach organizacyjnych.
