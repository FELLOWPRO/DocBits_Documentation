# Cost Invoice - Export

<figure><img src="../../../../.gitbook/assets/docbits_purchase_order_export_4.png" alt="DocBits Zakup Zamówienie Eksport 4"><figcaption></figcaption></figure>

Ten tytuł wskazuje, że reguła została specjalnie skonfigurowana do zarządzania fakturami kosztowymi i obejmuje akcję eksportu, prawdopodobnie na potrzeby raportowania, dalszego przetwarzania lub integracji z innymi systemami.

#### Konfiguracja reguły:

1. **When…**
   * **Document Type is Invoice**: Ten warunek zapewnia, że reguła jest wyzwalana tylko dla dokumentów sklasyfikowanych jako faktury, utrzymując specyficzność przepływu pracy w zarządzaniu fakturami.
2. **And…**
   * **Document Field Invoice Sub Type is Equals Cost Invoice**: To określa, że reguła ma zastosowanie tylko do tych faktur, które są wyraźnie oznaczone jako "Cost Invoices" w określonym polu w dokumencie. Pomaga to odróżnić je od innych typów faktur.
   * **Document Status is Pending Second Approval**: Faktura musi mieć status "Pending Second Approval". Oznacza to, że faktura przeszła już wstępne zatwierdzenie i oczekuje na drugi, prawdopodobnie ostateczny, przegląd.

#### Action (Then…):

* **Start Export**: Gdy faktura spełnia określone warunki (jest fakturą kosztową i oczekuje na drugie zatwierdzenie), wykonywana jest akcja "Start Export". Może to obejmować wysłanie danych faktury do innego systemu na potrzeby analizy finansowej, raportowania lub zgodności.

#### Cel tej reguły:

* **Wydajność przepływu pracy**: Ta reguła pomaga zautomatyzować obsługę faktur kosztowych, zapewniając ich przetwarzanie przez niezbędne etapy zatwierdzania bez ręcznej interwencji, zwiększając szybkość i dokładność operacji finansowych.
* **Kontrola i zgodność**: Wymagając drugiego zatwierdzenia, system egzekwuje mechanizm kontroli, który zapewnia dokładne przejrzenie faktur kosztowych, zwiększając nadzór finansowy.
* **Integracja i raportowanie**: Akcja eksportu sugeruje, że gdy faktury są w pełni zatwierdzone, mogą zostać zintegrowane z innymi systemami w celu dalszego przetwarzania lub analizy, co jest kluczowe dla raportowania finansowego i audytów.

Tego rodzaju reguła jest niezbędna dla organizacji, które mają do czynienia z różnymi typami faktur i muszą zapewnić, że każdy typ jest obsługiwany zgodnie z określonymi protokołami. Redukuje ryzyko błędów i zapewnia zgodność z kontrolami wewnętrznymi oraz przepisami zewnętrznymi.
