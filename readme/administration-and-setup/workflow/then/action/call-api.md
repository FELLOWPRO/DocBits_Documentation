# Zadzwoń do API

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-6a1c780ee588-pl.png" alt="Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane." width="563"><figcaption><p>Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane.</p></figcaption></figure>

## Cel:

Karta przepływu pracy **"Call API"** umożliwia użytkownikom wykonywanie żądań HTTP do określonych punktów końcowych API bezpośrednio z przepływu pracy. Ta karta obsługuje różne metody HTTP i umożliwia dynamiczną interakcję z systemami zewnętrznymi poprzez wysyłanie parametrów i danych. Usprawnia integrację z usługami zewnętrznymi i niestandardowymi interfejsami API, zapewniając bezproblemową komunikację.

## Komponenty karty:

1. **Punkt końcowy API**
   * **Opis:** Docelowy punkt końcowy **DocBits API**, z którym ta karta będzie wchodzić w interakcję.
   * **Szczegóły:** Pole tekstowe, w którym użytkownicy określają punkt końcowy dla żądania API.
2. **Metoda HTTP**
   * **Opis:** Typ żądania HTTP, które ma zostać wykonane.
   * **Opcje:**
     1. **GET:** Pobiera dane z określonego punktu końcowego.
     2. **POST:** Wysyła dane do punktu końcowego.
     3. **PUT:** Aktualizuje istniejące dane w punkcie końcowym.
     4. **DELETE:** Usuwa dane w punkcie końcowym.
3. **Parametry**
   * **Opis:** Parametry zapytania, które mają zostać uwzględnione w żądaniu API.
   * **Szczegóły:** Pole tekstowe lub lista do wprowadzania par klucz-wartość dla adresu URL żądania.
4. **Dane**
   1. **Opis:** Ładunek, który ma zostać wysłany w treści żądania API (dotyczy metod POST i PUT).
   2. **Szczegóły:** Pole do wprowadzania danych w formacie JSON.

## Funkcjonalność:

**Ocena warunku:** System ocenia warunki zdefiniowane w sekcjach "Where" i "And Sections":

* Jeśli oba warunki są **prawdziwe**, żądanie API jest wykonywane zgodnie z konfiguracją.
* Jeśli którykolwiek z warunków jest **fałszywy**, karta nie jest wykonywana i nie jest wykonywane żadne wywołanie API.

**Wykonanie żądania API:**

* Karta wysyła żądanie HTTP do określonego punktu końcowego przy użyciu wybranej metody.
* Wszelkie podane parametry są dołączane do adresu URL, a dane są uwzględniane w treści żądania (jeśli dotyczy).

## Konfiguracja:

1. **Zdefiniuj punkt końcowy API:**\
   Wprowadź adres URL API, które chcesz wywołać.
2. **Wybierz metodę HTTP:**\
   Wybierz jedną z obsługiwanych metod (GET, POST, PUT, DELETE) na podstawie wymagań Twojego API.
3. **Podaj parametry:**\
   Dodaj wymagane parametry zapytania jako pary klucz-wartość.
4. **Dołącz dane (jeśli dotyczy):**\
   Dla metod POST lub PUT określ dane, które mają zostać wysłane w treści żądania.
5. **Konfiguracja warunku:**\
   Skonfiguruj sekcje "Where" i "And Sections", aby zdefiniować, kiedy ma nastąpić wywołanie API.

## Podsumowanie:

Karta przepływu pracy **"Call API"** zwiększa automatyzację przepływu pracy, umożliwiając bezpośrednią interakcję z systemami zewnętrznymi. Zapewniając elastyczne konfiguracje punktów końcowych, metod i danych, gwarantuje, że przepływy pracy mogą bezproblemowo integrować się z zewnętrznymi interfejsami API lub niestandardowymi backendami. Możliwość warunkowego wykonywania wywołań API zapewnia precyzję i efektywność w automatyzacji komunikacji zewnętrznej.

***

<!-- workflow-card-practical-example-20261021 -->

## Praktyczny przykład

**Kiedy używać:** Poproś skonfigurowaną usługę zewnętrzną o dodatkową weryfikację.

**Konfiguracja:** Wybierz skonfigurowany punkt końcowy API demonstracyjnego i metodę HTTP. Podaj parametry i treść JSON wymagane przez ten punkt końcowy.

**Oczekiwany wynik i kontrprzykład:** Aby uzyskać próbną odpowiedź `200`, sprawdź sposób obsługi odpowiedzi oczekiwany przez następujące karty. Przetestuj także `500`; rozpoczęcie połączenia nie oznacza, że ​​sprawdzenie biznesowe powiodło się.

To jest ilustracyjna konfiguracja i oczekiwany wynik. Korzystaj z pól, użytkowników i grup skonfigurowanych w Twojej organizacji testowej; nie jest to twierdzenie, że ten przykład został wykonany.
