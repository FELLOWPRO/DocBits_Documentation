# AI Calculation for Cost Increase Surcharges

<figure><img src="../../../../.gitbook/assets/image (309).png" alt="" width="563"><figcaption></figcaption></figure>

## Cel:

Karta przepływu pracy **"AI Calculation for Cost Increase Surcharges"** wykorzystuje AI do automatycznego obliczania kwot dopłat na podstawie wzrostu kosztów. Zapewnia spójne i dokładne obliczenia dopłat, usprawniając przepływy pracy i redukując ręczny wysiłek.

## Komponenty karty:

* **Cost Increase Factor**
  * **Opis:** Mnożnik lub procent stosowany do kosztu bazowego w celu obliczenia dopłaty.
  * **Szczegóły:** Określa kwotę dopłaty na podstawie wzrostu kosztów (np. współczynnik 1,10 dla wzrostu o 10%).
* **Base Cost Field**
  * **Opis:** Pole zawierające pierwotną wartość kosztu używaną jako podstawa obliczenia dopłaty.
  * **Szczegóły:** Wybierane automatycznie lub definiowane w przepływie pracy w celu odniesienia podczas obliczeń.
* **Surcharge Field**
  * **Opis:** Pole, w którym przechowywana jest obliczona przez AI wartość dopłaty.
  * **Szczegóły:** Pole to odzwierciedla obliczoną dopłatę, udostępniając ją do dalszego przetwarzania lub raportowania.

## Funkcjonalność:

**Ocena warunku:**

* Karta aktywuje się tylko wtedy, gdy zarówno warunki **"Where"**, jak i **"And Sections"** są prawdziwe.
* Jeśli którykolwiek z warunków jest fałszywy, obliczenie dopłaty nie jest wykonywane.

**Obliczenia napędzane AI:**

* System stosuje **Cost Increase Factor** do **Base Cost Field** w celu obliczenia dopłaty.
* Wynik jest przechowywany w **Surcharge Field**, zapewniając dostępność dla kolejnych kroków przepływu pracy.

## Podsumowanie:

Karta przepływu pracy **"AI Calculation for Cost Increase Surcharges"** automatyzuje stosowanie dopłat na podstawie wzrostu kosztów. Wykorzystując AI do precyzji i spójności, karta ta eliminuje ręczne obliczenia, zwiększa efektywność i wspiera dokładne zarządzanie kosztami w zautomatyzowanych przepływach pracy.
