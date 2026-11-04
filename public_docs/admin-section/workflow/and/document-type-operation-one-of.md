# Operacja typu dokumentu jeden z

<figure><img src="../../../.gitbook/assets/userlmn_14ab8ac5e693d9bbe68d178795d12a9f.png" alt=""><figcaption></figcaption></figure>

**Cel**

Ta karta została zaprojektowana do zarządzania działaniami na dokumentach w zależności od ich typu, wykorzystując prostą logikę warunkową (jest/nie jest), aby wywołać lub zapobiec określonym procesom. Umożliwia to precyzyjną kontrolę nad tym, w jaki sposób różne typy dokumentów są przetwarzane w systemie ERP.

**Składniki karty**

1. **Operator**
* **Opis**: Określa logikę warunkową stosowaną do typów dokumentów.
* **Opcje**:
* **jest**: Operacja zostanie wywołana, jeśli typ dokumentu pasuje do jednego z określonych typów na liście.
* **nie jest**: Operacja zostanie wywołana, jeśli typ dokumentu nie pasuje do żadnego z wymienionych typów.
2. **Lista typów dokumentów**
* **Opis**: Określa listę typów dokumentów, do których będzie stosowany warunek.
* **Szczegóły**: Może to obejmować różne typy dokumentów, takie jak "Faktura", "Zamówienie zakupu", "Umowa", "Rekord pracownika" itp., na podstawie których zostanie oceniony warunek (jest/nie jest).

**Funkcjonalność**

* **Identyfikacja dokumentu**: System najpierw identyfikuje typ każdego przychodzącego lub istniejącego dokumentu na podstawie predefiniowanych atrybutów lub metadanych.
* **Ocena warunku**:
* Jeśli operator to **jest**, karta sprawdza, czy typ dokumentu znajduje się na podanej liście.
* Jeśli operator to **nie jest**, karta sprawdza, czy typ dokumentu nie znajduje się na liście.
* **Wywoływanie akcji**: W zależności od wyniku oceny warunku:
* **Prawda**: Inicjuje powiązane operacje lub procesy, jeśli warunek jest spełniony.
* **Fałsz**: Proces jest pomijany lub wywoływana jest alternatywna operacja, jeśli warunek nie jest spełniony.
* **Integracja i automatyzacja**: Bezproblemowo integruje się z innymi komponentami systemu, zapewniając zautomatyzowane przetwarzanie dokumentów i przestrzeganie polityk i procesów organizacyjnych.

**Interakcje użytkownika**

* **Konfiguracja**: Użytkownicy muszą określić operatora i wymienić typy dokumentów podczas konfigurowania karty. Konfiguracja ta może obejmować elementy interfejsu, takie jak rozwijane menu lub pola wyboru, do wyboru typów dokumentów i operatorów.
* **Monitorowanie i dostosowania**: Użytkownicy mogą monitorować wyniki i skuteczność tej karty za pomocą logów i raportów generowanych przez system ERP. Dostosowania mogą być dokonywane na liście lub operatorze w oparciu o zmieniające się potrzeby biznesowe.
* **Obsługa błędów i informacje zwrotne**: Zapewnia mechanizmy informowania o błędach napotkanych podczas działania. Użytkownicy mogą skonfigurować alerty dla przypadków niepowodzeń warunków, zapewniając szybką reakcję na problemy.

#### Podsumowanie

Karta workflow "Warunek typu dokumentu" odgrywa kluczową rolę w zarządzaniu operacjami opartymi na dokumentach z precyzją i elastycznością. Korzystając z prostej logiki warunkowej, pomaga zapewnić odpowiednie przetwarzanie dokumentów, zwiększając efektywność i zgodność. Dokumentowanie tej karty w sposób jasny pomoże użytkownikom zrozumieć, jak efektywnie ją wdrożyć i wykorzystać, czyniąc ją cenną częścią dokumentacji systemu ERP.
