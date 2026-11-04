# Pojedynczy Warunek Stanu Dokumentu

<figure><img src="../../../.gitbook/assets/userlmn_928e514bc0e2aa775894e4ec5f992bd9.png" alt=""><figcaption></figcaption></figure>

**Cel**

Ta karta przepływu pracy jest dostosowana do zarządzania operacjami na dokumentach opartych na pojedynczym, określonym stanie dokumentu. Poprzez uproszczenie warunku do jednego statusu, karta skupia się na bardzo konkretnych wyzwalaczach przepływu pracy, co czyni ją idealną do ukierunkowanych działań przetwarzania dokumentów w ramach systemu ERP.

**Składniki Karty**

1. **Operator**
* **Opis**: Określa metodę oceny stanu dokumentu względem wybranego warunku.
* **Opcje**:
* **jest**: Wywołuje operację, jeśli bieżący status dokumentu pasuje do wybranego statusu.
* **nie jest**: Wywołuje operację, jeśli bieżący status dokumentu nie pasuje do wybranego statusu.
2. **Status**
* **Opis**: Umożliwia wybór jednego statusu dokumentu do ustawienia warunku.
* **Przykładowe Statusy**: "Błąd", "Błąd Eksportu", "Gotowy do Walidacji", "Gotowy do Przejrzenia", "Oczekujący na Zatwierdzenie", "Oczekujący na Drugie Zatwierdzenie".
* **Szczegóły**: Użytkownicy wybierają jeden status z rozwijanej listy lub zestawu przycisków radio. Ten status służy jako kryterium dla działania karty.

**Funkcjonalność**

* **Identyfikacja Stanu Dokumentu**: Określa bieżący status dokumentu w trakcie przetwarzania w systemie ERP.
* **Ocena Warunku**:
* Na podstawie wybranego operatora (`jest` lub `nie jest`), karta sprawdza, czy bieżący status dokumentu zgadza się z wybranym kryterium statusu.
* **Wykonanie Działania**:
* **Prawdziwy Warunek**: Jeśli status pasuje (lub nie pasuje, w zależności od operatora), zostaje zainicjowane odpowiednie działanie. Może to być przekierowanie do dalszego przetwarzania, generowanie powiadomień lub inne zdefiniowane przepływy pracy.
* **Fałszywy Warunek**: Jeśli warunek nie jest spełniony, żadne działanie nie jest podejmowane, lub uruchamiana jest alternatywna ścieżka.
* **Integracja z Innymi Przepływami Pracy**: Pomimo że jest zaprojektowana do oceny pojedynczego statusu, ta karta może być skutecznie zintegrowana z szerszymi sekwencjami przepływu pracy, aby zapewnić precyzyjne zarządzanie dokumentami.

**Interakcje Użytkownika**

* **Konfiguracja i Ustawienia**: Użytkownicy konfigurują kartę, wybierając operatora, a następnie wybierając jeden status spośród dostępnych opcji. Proces wyboru jest prosty i zaprojektowany w taki sposób, aby zapobiec zamieszaniu.
* **Monitorowanie i Raportowanie**: Umożliwia monitorowanie poprzez raporty generowane przez system lub pulpity nawigacyjne, które śledzą przetwarzanie dokumentów na podstawie ich statusu, pomagając nadzorować skuteczność wdrożonych przepływów pracy.
* **Obsługa Błędów i Powiadomienia**: Możliwość skonfigurowania powiadomień dla użytkowników o ewentualnych anomaliiach w przetwarzaniu lub oznaczenia dokumentów, które nie spełniają ustawionych warunków, zapewniając szybką uwagę i rozwiązanie.

#### Podsumowanie

Karta przepływu pracy "Pojedynczy Warunek Stanu Dokumentu" upraszcza zarządzanie dokumentami, koncentrując się na indywidualnych warunkach statusu. Ta specyfikacja pomaga w przypadkach, gdy konieczna jest precyzyjna kontrola nad przepływami dokumentów, zwłaszcza w środowiskach o rygorystycznych kryteriach przetwarzania. Dokumentowanie tej wersji karty w sposób jasny zapewni, że użytkownicy w pełni zrozumieją jej zastosowanie i skutecznie zintegrują ją w codziennych operacjach, poprawiając zarówno zgodność, jak i efektywność przetwarzania dokumentów.
