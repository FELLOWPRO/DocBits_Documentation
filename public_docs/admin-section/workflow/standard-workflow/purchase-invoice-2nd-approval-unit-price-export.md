# Faktura zakupu - 2. zatwierdzenie ceny jednostkowej eksport

<figure><img src="../../../.gitbook/assets/docbits_rule_purchase_invoice_unit_price_export.png" alt="DocBits Reguła Zakup Faktura Unit Price Eksport"><figcaption></figcaption></figure>

Ten tytuł wskazuje, że reguła jest skonfigurowana do zarządzania drugą fazą zatwierdzania faktur zakupowych z naciskiem na cenę jednostkową, zapewniając jej zgodność z uzgodnionymi warunkami.

#### Konfiguracja reguły:

1. **Gdy…**
   * **Typ dokumentu to Faktura**: Ten warunek zapewnia, że reguła jest aktywowana tylko dla dokumentów zidentyfikowanych jako faktury, co jest kluczowe dla dokładnego kierowania przepływem pracy.
2. **Oraz…**
   * **Status dokumentu to Oczekuje na drugie zatwierdzenie**: Określa to, że faktura oczekuje na drugie zatwierdzenie. Ten etap często zapewnia dodatkowy nadzór w celu zapewnienia dokładności przed sfinalizowaniem transakcji.
   * **Pole dokumentu Podtyp faktury to Faktura zakupu**: Ten warunek dodatkowo określa, że reguła dotyczy tylko faktur skategoryzowanych jako „Faktury zakupu”, odróżniając je od innych rodzajów faktur.
   * **Logika: Cena jednostkowa w potwierdzeniu zamówienia równa się zamówieniu zakupu**: Ten warunek sprawdza, czy cena jednostkowa wymieniona w potwierdzeniu zamówienia zgadza się z ceną jednostkową w zamówieniu zakupu. Zapewnia to, że przetwarzanie faktury posuwa się naprzód tylko wtedy, gdy ceny są spójne, co ma kluczowe znaczenie dla budżetowania i raportowania finansowego.

#### Akcja (Wtedy…):

* **Rozpocznij eksport**: Gdy faktura spełni określone warunki (tj. ceny jednostkowe zgadzają się między potwierdzeniem zamówienia a zamówieniem zakupu), uruchamiana jest akcja „Rozpocznij eksport”. Prawdopodobnie wiąże się to z eksportem danych faktury do dalszego przetwarzania, być może do innego systemu finansowego lub w celach raportowych.

#### Cel tej reguły:

* **Zapewnienie dokładności i spójności**: Weryfikując zgodność cen jednostkowych między potwierdzeniem zamówienia a zamówieniem zakupu, system pomaga utrzymać dokładność finansową i zapobiega nadpłatom lub niedopłatom.
* **Usprawnienie przetwarzania finansowego**: Automatyzacja eksportu danych po potwierdzeniu cen ogranicza ręczną obsługę i przyspiesza cykl przetwarzania finansowego.
* **Zwiększenie zgodności i nadzoru**: Wymaganie drugiego zatwierdzenia w celu weryfikacji ceny dodaje dodatkową warstwę nadzoru, kluczową dla zgodności z polityką finansową i kontrolami.

Reguła ta jest przykładem tego, jak automatyzacja przepływu pracy może być skutecznie wykorzystywana do zapewnienia precyzyjnej i wydajnej obsługi dokumentów finansowych w organizacji, szczególnie w kontekście dużej liczby transakcji wymagających skrupulatnej walidacji.