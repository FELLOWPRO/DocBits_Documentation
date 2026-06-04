# Document Operator for Sub-Organizations

<figure><img src="../../../../.gitbook/assets/userlmn_dbb4cc2e8f2f4b59ec15726545d9e502.png" alt=""><figcaption></figcaption></figure>

**Cel**

Ta karta przepływu pracy służy do wykonywania określonych operacji na dokumentach powiązanych z konkretną sub-organizacją lub działem w firmie. Zapewnia, że przetwarzanie dokumentów jest zgodne z politykami i wymaganiami specyficznymi dla różnych segmentów organizacji.

**Komponenty karty**

1. **Operator**
   * **Opis**: Definiuje akcję lub zestaw akcji, które mają być wykonane na dokumencie.
   * **Przykłady**: Może to obejmować operatory takie jak "Review", "Approve", "Archive", "Distribute" lub dowolną inną niestandardową operację istotną dla zarządzania dokumentami w organizacji.
2. **Sub-Organization**
   * **Opis**: Określa część organizacji lub dział, dla którego operacja na dokumencie jest istotna.
   * **Szczegóły**: Może to być dowolny wyznaczony obszar firmy, taki jak Human Resources, Finance, Marketing itp., lub mniejsze, wyspecjalizowane zespoły w ramach tych szerszych kategorii.

**Funkcjonalność**

* **Identyfikacja dokumentu**: Karta najpierw identyfikuje dokument(y), które wymagają przetworzenia. Identyfikacja ta może być oparta na typie dokumentu, źródle, dacie lub dowolnych innych metadanych.
* **Wykonanie operacji**: Na podstawie określonego operatora karta wykonuje wyznaczoną operację. Może to być:
  * **Review**: Wysłanie dokumentu do odpowiedniego personelu lub działu do przeglądu.
  * **Approve**: Przekierowanie dokumentu w celu uzyskania niezbędnych zatwierdzeń w ramach sub-organizacji.
  * **Archive**: Przeniesienie dokumentu do systemu archiwizacji przeznaczonego do przechowywania rekordów zgodnie z politykami organizacyjnymi.
  * **Distribute**: Rozpowszechnianie dokumentu wewnętrznie w ramach sub-organizacji lub zewnętrznie, jeśli jest to wymagane.
* **Kontrole zgodności**: Karta sprawdza, czy wszystkie operacje są zgodne z politykami wewnętrznymi i wymaganiami prawnymi mającymi zastosowanie do konkretnej sub-organizacji.
* **Informacje zwrotne i rejestrowanie**: Po operacji karta dostarcza informacji zwrotnych o podjętej akcji i rejestruje te informacje na potrzeby ścieżek audytu i śledzenia zgodności.

**Interakcje użytkownika**

* **Konfiguracja**: Użytkownicy konfigurują kartę, określając operator i sub-organizację. Mogą również zdefiniować konkretne reguły lub wyzwalacze określające, kiedy karta powinna się aktywować.
* **Monitorowanie**: Użytkownicy mogą monitorować aktywność karty za pośrednictwem pulpitu, który pokazuje trwające i ukończone operacje, zapewniając przejrzystość procesów obsługi dokumentów.
* **Ręczne nadpisanie**: W niektórych przypadkach użytkownicy mogą mieć możliwość ręcznej interwencji lub zmiany przebiegu operacji, takiej jak eskalacja problemu lub poprawienie błędów routingu dokumentów.

#### Podsumowanie

Karta "Document Operator for Sub-Organizations" jest kluczowym narzędziem do zarządzania dokumentami w sposób ustrukturyzowany i efektywny, szczególnie w większych organizacjach, w których różne działy mają unikalne potrzeby operacyjne i wymagania dotyczące zgodności. Jasne udokumentowanie tej karty w instrukcji systemu ERP pomoże użytkownikom zrozumieć jej znaczenie i skutecznie wdrożyć ją w przepływach pracy. Jeśli potrzebne są dodatkowe opisy dostosowania lub funkcjonalności, można je rozszerzyć na podstawie konkretnych potrzeb organizacyjnych i możliwości technicznych.
