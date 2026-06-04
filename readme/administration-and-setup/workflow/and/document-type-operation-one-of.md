# Document Type Operation one of

<figure><img src="../../../../.gitbook/assets/userlmn_14ab8ac5e693d9bbe68d178795d12a9f.png" alt=""><figcaption></figcaption></figure>

**Cel**

Ta karta służy do zarządzania akcjami na dokumentach w zależności od ich typu, wykorzystując prostą logikę warunkową (is/is not) do wyzwalania lub blokowania określonych przepływów pracy. Umożliwia to precyzyjną kontrolę nad sposobem przetwarzania różnych typów dokumentów w systemie ERP.

**Komponenty karty**

1. **Operator**
   * **Opis**: Określa logikę warunkową stosowaną do typów dokumentów.
   * **Opcje**:
     * **is**: Operacja zostanie wyzwolona, jeśli typ dokumentu odpowiada jednemu z określonych typów na liście.
     * **is not**: Operacja zostanie wyzwolona, jeśli typ dokumentu nie odpowiada żadnemu z wymienionych typów.
2. **Document Types List**
   * **Opis**: Określa listę typów dokumentów, do których będzie miał zastosowanie warunek.
   * **Szczegóły**: Może obejmować różne typy dokumentów, takie jak "Invoice", "Purchase Order", "Contract", "Employee Record" itp., na podstawie których oceniany będzie warunek (is/is not).

**Funkcjonalność**

* **Identyfikacja dokumentu**: System najpierw identyfikuje typ każdego przychodzącego lub istniejącego dokumentu na podstawie predefiniowanych atrybutów lub metadanych.
* **Ocena warunku**:
  * Jeśli operator to **is**, karta sprawdza, czy typ dokumentu znajduje się na podanej liście.
  * Jeśli operator to **is not**, karta sprawdza, czy typ dokumentu nie znajduje się na liście.
* **Wyzwalanie akcji**: W zależności od wyniku oceny warunku:
  * **True**: Inicjuje powiązane operacje lub przepływy pracy, jeśli warunek jest spełniony.
  * **False**: Proces jest pomijany lub wyzwalana jest alternatywna operacja, jeśli warunek nie jest spełniony.
* **Integracja i automatyzacja**: Bezproblemowo integruje się z innymi komponentami systemu, zapewniając, że obsługa dokumentów jest zautomatyzowana i zgodna z organizacyjnymi przepływami pracy i politykami.

**Interakcje użytkownika**

* **Konfiguracja**: Użytkownicy muszą określić operator i wymienić typy dokumentów podczas konfigurowania karty. Konfiguracja ta może obejmować elementy interfejsu, takie jak listy rozwijane lub pola wyboru, do wybierania typów dokumentów i operatorów.
* **Monitorowanie i dostosowania**: Użytkownicy mogą monitorować wyniki i skuteczność tej karty za pośrednictwem dzienników i raportów generowanych przez system ERP. Dostosowania można wprowadzać do listy lub operatora na podstawie zmieniających się potrzeb biznesowych.
* **Obsługa błędów i informacje zwrotne**: Zapewnia mechanizmy informacji zwrotnych dla błędów napotkanych podczas działania. Użytkownicy mogą skonfigurować alerty na wypadek niespełnienia warunków, zapewniając szybką reakcję na problemy.

#### Podsumowanie

Karta przepływu pracy "Document Type Condition" odgrywa kluczową rolę w zarządzaniu operacjami opartymi na dokumentach z precyzją i elastycznością. Korzystając z prostej logiki warunkowej, pomaga zapewnić, że dokumenty są odpowiednio przetwarzane, zwiększając efektywność i zgodność. Jasne udokumentowanie tej karty pomoże użytkownikom zrozumieć, jak skutecznie ją wdrożyć i wykorzystać, czyniąc ją cenną częścią dokumentacji systemu ERP.
