# Purchase Invoice - 2nd Approval Quantity Export

<figure><img src="../../../../.gitbook/assets/docbits_purchase_order_export_6.png" alt="DocBits Zakup Zamówienie Eksport 6"><figcaption></figcaption></figure>

Ten tytuł wskazuje, że reguła została skonfigurowana do zarządzania drugim etapem zatwierdzania faktur zakupowych z naciskiem na szczegóły ilości, zapewniając, że ilości na fakturze są zgodne z tymi w oryginalnym zamówieniu zakupu.

#### Konfiguracja reguły:

1. **When…**
   * **Document Type is Invoice**: Ten warunek zapewnia, że reguła jest aktywowana tylko dla dokumentów zidentyfikowanych jako faktury, co jest kluczowe dla dokładnego kierowania przepływem pracy.
2. **And…**
   * **Document Status is Pending Second Approval**: To określa, że faktura aktualnie oczekuje na drugie zatwierdzenie. Ten etap często zapewnia dodatkowy nadzór, aby zapewnić dokładność przed sfinalizowaniem transakcji.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Ten warunek dodatkowo określa, że reguła ma zastosowanie tylko do faktur sklasyfikowanych konkretnie jako "Purchase Invoices", odróżniając je od innych typów faktur.
   * **Logic Quantity in order confirmation Equals purchase order**: Ten warunek sprawdza, czy ilość wymieniona w potwierdzeniu zamówienia jest zgodna z ilością w zamówieniu zakupu. Zapewnia, że przetwarzanie faktury postępuje tylko wtedy, gdy ilości są spójne, co jest kluczowe dla zarządzania stanami magazynowymi i dokładności finansowej.

#### Action (Then…):

* **Start Export**: Gdy faktura spełnia określone warunki (tj. ilości są zgodne między potwierdzeniem zamówienia a zamówieniem zakupu), wyzwalana jest akcja "Start Export". Prawdopodobnie obejmuje to eksport danych faktury do dalszego przetwarzania, ewentualnie do innego systemu finansowego lub na potrzeby raportowania.

#### Cel tej reguły:

* **Zapewnienie dokładności i spójności**: Poprzez weryfikację, że ilości są zgodne między potwierdzeniem zamówienia a zamówieniem zakupu, system pomaga utrzymać dokładność stanów magazynowych i zapobiega rozbieżnościom, które mogłyby wpłynąć na raportowanie finansowe lub zarządzanie zapasami.
* **Usprawnienie przetwarzania finansowego**: Automatyzacja eksportu danych po potwierdzeniu ilości redukuje ręczną obsługę i przyspiesza cykl przetwarzania finansowego.
* **Zwiększenie zgodności i nadzoru**: Wymaganie drugiego zatwierdzenia dla weryfikacji ilości dodaje dodatkową warstwę nadzoru, kluczową dla zgodności z politykami i kontrolami finansowymi.

Ta reguła jest wyraźnym przykładem, jak automatyzacja przepływu pracy może być skutecznie wykorzystywana do zapewnienia precyzyjnej i wydajnej obsługi dokumentów finansowych w organizacji, szczególnie w kontekście procesów zakupowych obejmujących duże wolumeny transakcji wymagających skrupulatnej walidacji.
