# Automatyczne Dopasowywanie Danych Zamówień Zakupu

Docbits to zaawansowany system zaprojektowany do automatycznego dopasowywania danych zamówień zakupu (PO) z nadchodzącymi dokumentami faktur. To narzędzie jest specjalnie zaprojektowane do efektywnego zarządzania i przetwarzania danych faktur w systemach ERP. Niniejsza dokumentacja wyjaśnia podstawy automatycznego dopasowywania za pomocą Docbits i definiuje specyficzne zasady wymagane do pomyślnego dopasowania.

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_invoice_3.svg" alt="DocBits Zakup Zamówienie Faktura 3"><figcaption></figcaption></figure>

### **Podstawowe Zasady Automatycznego Dopasowywania w Docbits**

**Ekstrakcja Danych:** Docbits rozpoczyna proces od ekstrakcji istotnych danych z cyfrowych dokumentów faktur. Zazwyczaj dane te obejmują numery pozycji, ilości i ceny jednostkowe każdej linii faktury. Precyzja tej ekstrakcji jest kluczowa, ponieważ stanowi podstawę do dalszego procesu dopasowywania.

**Porównanie z Danymi PO:** Wyekstrahowane dane są porównywane z odpowiadającymi im informacjami w przechowywanych zamówieniach zakupu. Docbits sprawdza, czy numery pozycji, ilości i ceny odpowiadają tym w PO. Aby dopasowanie było pomyślne, dane w fakturach muszą odpowiadać danym w zamówieniach zakupu, z uwzględnieniem zdefiniowanych progów tolerancji.

**Automatyczne Dopasowywanie:** Na podstawie wyników porównania, Docbits wykonuje dopasowywanie. System weryfikuje, czy kryteria dopasowania mieszczą się w ustalonych granicach tolerancji. Jeśli te kryteria są spełnione, dopasowanie uznaje się za pomyślne.

**Raportowanie:** Po zakończeniu procesu dopasowywania, Docbits generuje raporty pokazujące status dopasowań. Raporty te informują o pomyślnie dopasowanych fakturach i identyfikują te z rozbieżnościami.

### **Definicja Zasad Dopasowywania**

**Numer Pozycji:** Numer pozycji na fakturze musi dokładnie odpowiadać numerowi pozycji w zamówieniu zakupu. Nie ma tolerancji dla odchyleń w numerach pozycji.

**Ilości:** Ilość dostarczonych towarów na fakturze może się różnić w ramach zdefiniowanego zakresu tolerancji. Zazwyczaj tolerancja ±5% może być akceptowalna, aby uwzględnić drobne różnice w ilościach dostaw.

**Ceny:** Odchylenia cenowe są tolerowane do ustalonego progu. Powszechna tolerancja może wynosić ±2% ceny, aby zaakceptować niewielkie różnice w oświadczeniach cenowych wynikające z różnic zaokrągleń lub wahań kursów walut.

### **Status Dopasowania:**

* **Pełne Dopasowanie:** Wszystkie punkty danych (numer pozycji, ilość i cena) mieszczą się w ustalonych granicach tolerancji.
* **Częściowe Dopasowanie:** Jeden lub więcej punktów danych odbiega poza granice tolerancji, ale odchylenia są minimalne i wymagają ręcznej weryfikacji.
* **Brak Dopasowania:** Znaczące odchylenia w jednym lub więcej punktach danych, które wymagają natychmiastowej korekty lub dalszego dochodzenia.

Dokładna definicja tych zasad i ustalenie granic tolerancji są kluczowe dla efektywności automatycznego dopasowywania i redukcji ręcznych interwencji. Docbits pozwala na elastyczną konfigurację tych parametrów, aby sprostać potrzebom różnych firm i branż.
