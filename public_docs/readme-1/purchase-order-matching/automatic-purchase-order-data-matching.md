# Automatyczne Dopasowywanie Danych Zamówienia Zakupu

Docbits to zaawansowany system zaprojektowany do automatyzacji dopasowywania danych zamówienia zakupu (POs) z przychodzącymi dokumentami faktury. To narzędzie jest specjalnie zaprojektowane do efektywnego zarządzania i przetwarzania danych faktur w systemach ERP. Ta dokumentacja wyjaśnia podstawy automatycznego dopasowywania za pomocą Docbits i definiuje konkretne zasady wymagane do udanego dopasowania.

## **Podstawowe Zasady Automatycznego Dopasowywania w Docbits**

**Ekstrakcja Danych:** Docbits rozpoczyna proces poprzez wyodrębnienie istotnych danych z zedytowanych dokumentów faktury. Zazwyczaj dane te obejmują numery pozycji, ilości i ceny jednostkowe każdej linii faktury. Precyzja tej ekstrakcji jest kluczowa, ponieważ stanowi podstawę dla następnego procesu dopasowywania.

**Porównanie z Danymi PO:** Wyodrębnione dane są porównywane z odpowiadającymi informacjami w przechowywanych zamówieniach zakupu. Docbits sprawdza, czy numery pozycji, ilości i ceny odpowiadają tym w PO. Dla udanego dopasowania dane na fakturach muszą odpowiadać danym w zamówieniach zakupu, biorąc pod uwagę zdefiniowane progi tolerancji.

**Automatyczne Dopasowywanie:** Na podstawie wyników porównania Docbits wykonuje dopasowanie. System weryfikuje, czy kryteria dopasowania mieszczą się w ustalonych limitach tolerancji. Jeśli te kryteria są spełnione, dopasowanie jest uważane za udane.

**Raportowanie:** Po zakończeniu procesu dopasowywania Docbits generuje raporty, które pokazują stan dopasowań. Te raporty informują o pomyślnie dopasowanych fakturach i identyfikują te z niezgodnościami.

## **Definicja Zasad Dopasowywania**

**Numer Pozycji:** Numer pozycji na fakturze musi dokładnie pasować do numeru pozycji w zamówieniu zakupu. Nie ma tolerancji dla odchyleń w numerach pozycji.

**Ilości:** Ilość dostarczonych towarów na fakturze może się różnić w określonym zakresie tolerancji. Zazwyczaj tolerancja ±5% może być akceptowalna, aby uwzględnić drobne różnice w ilościach dostaw.

**Ceny:** Odchylenia cen są dopuszczalne do określonego progu. Typowa tolerancja może wynosić ±2% ceny, aby zaakceptować niewielkie różnice w oświadczeniach cenowych wynikających z różnic w zaokrągleniach lub wahaniach walutowych.

## **Status Dopasowania:**

* **Pełne Dopasowanie:** Wszystkie punkty danych (numer pozycji, ilość i cena) mieszczą się w ustalonych limitach tolerancji.
* **Częściowe Dopasowanie:** Jeden lub więcej punktów danych odbiega poza limity tolerancji, ale odchylenia są minimalne i wymagają ręcznej weryfikacji.
* **Brak Dopasowania:** Istotne odchylenia w jednym lub więcej punktach danych, które wymagają natychmiastowej korekty lub dalszego dochodzenia.

Precyzyjna definicja tych zasad i ustawienie limitów tolerancji są kluczowe dla efektywności automatycznego dopasowywania i redukcji interwencji manualnych. Docbits pozwala na elastyczną konfigurację tych parametrów, aby sprostać potrzebom różnych firm i branż.
