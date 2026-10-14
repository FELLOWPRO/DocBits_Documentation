# Single Document Status Condition

<figure><img src="../../../../.gitbook/assets/userlmn_928e514bc0e2aa775894e4ec5f992bd9 (1).png" alt="" width="528"><figcaption></figcaption></figure>

**Cel**

Ta karta przepływu pracy jest dostosowana do zarządzania operacjami na dokumentach na podstawie pojedynczego, określonego statusu dokumentu. Upraszczając warunek do jednego statusu, karta skupia się na bardzo specyficznych wyzwalaczach przepływu pracy, co czyni ją idealną dla ukierunkowanych działań przetwarzania dokumentów w systemie ERP.

**Komponenty karty**

1. **Operator**
   * **Opis**: Określa metodę oceny statusu dokumentu względem wybranego warunku.
   * **Opcje**:
     * **is**: Wyzwala operację, jeśli bieżący status dokumentu odpowiada wybranemu statusowi.
     * **is not**: Wyzwala operację, jeśli bieżący status dokumentu nie odpowiada wybranemu statusowi.
2. **Status**
   * **Opis**: Umożliwia wybór pojedynczego statusu dokumentu w celu ustawienia warunku.
   * **Przykłady statusów**: "Error", "Export Error", "Ready in Validation", "Ready in Review", "Pending Approval", "Pending Second Approval".
   * **Szczegóły**: Użytkownicy wybierają jeden status z listy rozwijanej lub zestawu przycisków radiowych. Status ten służy następnie jako kryterium działania karty.

**Funkcjonalność**

* **Identyfikacja statusu dokumentu**: Identyfikuje bieżący status dokumentu w miarę jego przetwarzania przez system ERP.
* **Ocena warunku**:
  * Na podstawie wybranego operatora (`is` lub `is not`) karta sprawdza, czy bieżący status dokumentu jest zgodny z wybranym kryterium statusu.
* **Wykonanie akcji**:
  * **Warunek prawdziwy**: Jeśli status jest zgodny (lub niezgodny, w zależności od operatora), inicjowana jest odpowiednia akcja. Może to być routing do dalszego przetwarzania, generowanie powiadomień lub inne predefiniowane przepływy pracy.
  * **Warunek fałszywy**: Jeśli warunek nie jest spełniony, nie jest podejmowana żadna akcja lub wyzwalana jest alternatywna ścieżka.
* **Integracja z innymi przepływami pracy**: Mimo że jest zaprojektowana do oceny pojedynczego statusu, karta ta może być skutecznie zintegrowana z szerszymi sekwencjami przepływu pracy w celu zapewnienia precyzyjnej obsługi dokumentów.

**Interakcje użytkownika**

* **Konfiguracja**: Użytkownicy konfigurują kartę, wybierając operator, a następnie wybierając jeden status z dostępnych opcji. Proces wyboru jest prosty i zaprojektowany tak, aby zapobiec nieporozumieniom.
* **Monitorowanie i raportowanie**: Umożliwia monitorowanie za pośrednictwem raportów lub pulpitów generowanych przez system, które śledzą przetwarzanie dokumentów na podstawie ich statusu, pomagając nadzorować skuteczność wdrożonych przepływów pracy.
* **Obsługa błędów i powiadomienia**: Konfigurowalna w celu ostrzegania użytkowników o wszelkich anomaliach przetwarzania lub oznaczania dokumentów, które nie spełniają ustawionych warunków, zapewniając szybką uwagę i rozwiązanie.

#### Podsumowanie

Karta przepływu pracy "Single Document Status Condition" upraszcza zarządzanie dokumentami, skupiając się na pojedynczych warunkach statusu. Ta specyfikacja pomaga w przypadkach, gdy konieczna jest precyzyjna kontrola nad przepływami dokumentów, szczególnie w środowiskach o rygorystycznych kryteriach przetwarzania. Jasne udokumentowanie tej wersji karty zapewni, że użytkownicy w pełni zrozumieją jej zastosowanie i będą mogli skutecznie zintegrować ją z codziennymi operacjami, zwiększając zarówno zgodność, jak i efektywność przetwarzania dokumentów.
