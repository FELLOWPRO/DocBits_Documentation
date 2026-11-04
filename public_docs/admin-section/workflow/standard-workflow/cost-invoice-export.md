# Faktura kosztowa - Eksport

<figure><img src="../../../.gitbook/assets/docbits_rule_cost_invoice.png" alt="DocBits Reguła Cost Faktura"><figcaption></figcaption></figure>

Ten tytuł wskazuje, że reguła jest specjalnie skonfigurowana do zarządzania fakturami kosztowymi i obejmuje akcję eksportu, prawdopodobnie w celu raportowania, dalszego przetwarzania lub integracji z innymi systemami.

#### Konfiguracja reguły:

1. **Gdy…**
   * **Typ dokumentu to Faktura**: Ten warunek zapewnia, że reguła jest uruchamiana tylko dla dokumentów skategoryzowanych jako faktury, zachowując specyfikę przepływu pracy w zarządzaniu fakturami.
2. **Oraz…**
   * **Pole dokumentu Podtyp faktury to Faktura kosztowa**: Określa to, że reguła ma zastosowanie tylko do tych faktur, które są wyraźnie oznaczone jako „Faktury kosztowe” w konkretnym polu w dokumencie. Pomaga to w odróżnieniu ich od innych rodzajów faktur.
   * **Status dokumentu to Oczekuje na drugie zatwierdzenie**: Faktura musi znajdować się w statusie „Oczekiwanie na drugie zatwierdzenie”. Wskazuje to, że faktura przeszła już wstępne zatwierdzenie i oczekuje na drugą, prawdopodobnie ostateczną, recenzję.

#### Akcja (Wtedy…):

* **Rozpocznij eksport**: Gdy faktura spełni określone warunki (będąc fakturą kosztową i oczekując na drugie zatwierdzenie), wykonywana jest akcja „Rozpocznij eksport”. Może to obejmować przesłanie danych faktury do innego systemu w celu analizy finansowej, raportowania lub celów zgodności.

#### Cel tej reguły:

* **Efektywność przepływu pracy**: Ta reguła pomaga zautomatyzować obsługę faktur kosztowych, zapewniając ich przejście przez niezbędne etapy zatwierdzania bez ręcznej interwencji, zwiększając szybkość i dokładność operacji finansowych.
* **Kontrola i zgodność**: Wymagając drugiego zatwierdzenia, system wymusza mechanizm kontrolny, który zapewnia dokładny przegląd faktur kosztowych, zwiększając nadzór finansowy.
* **Integracja i raportowanie**: Akcja eksportu sugeruje, że po pełnym zatwierdzeniu faktury mogą zostać zintegrowane z innymi systemami w celu dalszego przetwarzania lub analizy, co jest krytyczne dla raportowania finansowego i audytów.

Ten rodzaj reguły jest kluczowy dla organizacji, które mają do czynienia z różnymi rodzajami faktur i muszą zapewnić, że każdy rodzaj jest obsługiwany zgodnie z określonymi protokołami. Zmniejsza ryzyko błędów i zapewnia zgodność z kontrolami wewnętrznymi oraz regulacjami zewnętrznymi.