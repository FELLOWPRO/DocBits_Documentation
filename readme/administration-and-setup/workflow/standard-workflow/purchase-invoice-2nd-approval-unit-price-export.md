# Purchase Invoice - 2nd Approval Unit Price Export

<figure><img src="../../../../.gitbook/assets/docbits_purchase_order_export_5.png" alt="DocBits Zakup Zamówienie Eksport 5"><figcaption></figcaption></figure>

Ten tytuł wskazuje, że reguła została skonfigurowana do zarządzania drugim etapem zatwierdzania faktur zakupowych z naciskiem na cenę jednostkową, zapewniając jej zgodność z uzgodnionymi warunkami.

#### Konfiguracja reguły:

1. **When…**
   * **Document Type is Invoice**: Ten warunek zapewnia, że reguła jest aktywowana tylko dla dokumentów zidentyfikowanych jako faktury, co jest kluczowe dla dokładnego kierowania przepływem pracy.
2. **And…**
   * **Document Status is Pending Second Approval**: To określa, że faktura oczekuje na drugie zatwierdzenie. Ten etap często zapewnia dodatkowy nadzór, aby zapewnić dokładność przed sfinalizowaniem transakcji.
   * **Document Field Invoice Sub Type is Equals Purchase Invoice**: Ten warunek dodatkowo określa, że reguła ma zastosowanie tylko do faktur sklasyfikowanych konkretnie jako "Purchase Invoices", odróżniając je od innych typów faktur.
   * **Logic Unit Price in order confirmation Equals purchase order**: Ten warunek sprawdza, czy cena jednostkowa wymieniona w potwierdzeniu zamówienia jest zgodna z ceną jednostkową w zamówieniu zakupu. Zapewnia, że przetwarzanie faktury postępuje tylko wtedy, gdy występuje spójność w cenach, co jest kluczowe dla budżetowania i raportowania finansowego.

#### Action (Then…):

* **Start Export**: Gdy faktura spełnia określone warunki (tj. ceny jednostkowe są zgodne między potwierdzeniem zamówienia a zamówieniem zakupu), wyzwalana jest akcja "Start Export". Prawdopodobnie obejmuje to eksport danych faktury do dalszego przetwarzania, ewentualnie do innego systemu finansowego lub na potrzeby raportowania.

#### Cel tej reguły:

* **Zapewnienie dokładności i spójności**: Poprzez weryfikację, że ceny jednostkowe są zgodne między potwierdzeniem zamówienia a zamówieniem zakupu, system pomaga utrzymać dokładność finansową i zapobiega zawyżaniu lub zaniżaniu opłat.
* **Usprawnienie przetwarzania finansowego**: Automatyzacja eksportu danych po potwierdzeniu cen redukuje ręczną obsługę i przyspiesza cykl przetwarzania finansowego.
* **Zwiększenie zgodności i nadzoru**: Wymaganie drugiego zatwierdzenia dla weryfikacji cen dodaje dodatkową warstwę nadzoru, co jest kluczowe dla zgodności z politykami i kontrolami finansowymi.

Ta reguła jest przykładem, jak automatyzacja przepływu pracy może być skutecznie wykorzystywana do zapewnienia precyzyjnej i wydajnej obsługi dokumentów finansowych w organizacji, szczególnie w kontekście dużych wolumenów transakcji wymagających skrupulatnej walidacji.
