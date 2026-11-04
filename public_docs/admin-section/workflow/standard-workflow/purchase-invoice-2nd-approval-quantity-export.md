# Faktura zakupu - 2. zatwierdzenie ilości eksport

<figure><img src="../../../.gitbook/assets/docbits_rule_purchase_invoice_quantity_export.png" alt="DocBits Reguła Zakup Faktura Quantity Eksport"><figcaption></figcaption></figure>

Ten tytuł wskazuje, że reguła jest skonfigurowana do zarządzania drugą fazą zatwierdzania faktur zakupowych z naciskiem na szczegóły dotyczące ilości, zapewniając, że ilości na fakturze zgadzają się z ilościami na oryginalnym zamówieniu zakupu.

#### Konfiguracja reguły:

1. **Gdy…**
   * **Typ dokumentu to Faktura**: Ten warunek zapewnia, że reguła jest aktywowana tylko dla dokumentów zidentyfikowanych jako faktury, co jest kluczowe dla dokładnego kierowania przepływem pracy.
2. **Oraz…**
   * **Status dokumentu to Oczekuje na drugie zatwierdzenie**: Określa to, że faktura oczekuje obecnie na drugie zatwierdzenie. Ten etap często zapewnia dodatkowy nadzór w celu zapewnienia dokładności przed sfinalizowaniem transakcji.
   * **Pole dokumentu Podtyp faktury to Faktura zakupu**: Ten warunek dodatkowo określa, że reguła dotyczy tylko faktur skategoryzowanych jako „Faktury zakupu”, odróżniając je od innych rodzajów faktur.
   * **Logika: Ilość w potwierdzeniu zamówienia równa się zamówieniu zakupu**: Ten warunek sprawdza, czy ilość wymieniona w potwierdzeniu zamówienia zgadza się z ilością w zamówieniu zakupu. Zapewnia to, że przetwarzanie faktury posuwa się naprzód tylko wtedy, gdy ilości są spójne, co ma kluczowe znaczenie dla zarządzania zapasami i dokładności finansowej.

#### Akcja (Wtedy…):

* **Rozpocznij eksport**: Gdy faktura spełni określone warunki (tj. ilości zgadzają się między potwierdzeniem zamówienia a zamówieniem zakupu), uruchamiana jest akcja „Rozpocznij eksport”. Prawdopodobnie wiąże się to z eksportem danych faktury do dalszego przetwarzania, być może do innego systemu finansowego lub w celach raportowych.

#### Cel tej reguły:

* **Zapewnienie dokładności i spójności**: Weryfikując zgodność ilości między potwierdzeniem zamówienia a zamówieniem zakupu, system pomaga utrzymać dokładność inwentarza i zapobiega rozbieżnościom, które mogłyby wpłynąć na raportowanie finansowe lub zarządzanie zapasami.
* **Usprawnienie przetwarzania finansowego**: Automatyzacja eksportu danych po potwierdzeniu ilości ogranicza ręczną obsługę i przyspiesza cykl przetwarzania finansowego.
* **Zwiększenie zgodności i nadzoru**: Wymaganie drugiego zatwierdzenia w celu weryfikacji ilości dodaje dodatkową warstwę nadzoru, kluczową dla zgodności z polityką finansową i kontrolami.

Reguła ta jest wyraźnym przykładem tego, jak automatyzacja przepływu pracy może być skutecznie wykorzystywana do zapewnienia precyzyjnej i wydajnej obsługi dokumentów finansowych w organizacji, szczególnie w kontekście procesów zakupowych, które obejmują duże ilości transakcji wymagających skrupulatnej walidacji.