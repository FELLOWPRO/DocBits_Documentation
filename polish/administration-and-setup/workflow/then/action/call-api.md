# Call Api

<figure><img src="../../../../.gitbook/assets/Then_Call_API.png" alt="" width="563"><figcaption></figcaption></figure>

## Cel:

Karta przepływu pracy **"Call API"** umożliwia użytkownikom wykonywanie żądań HTTP do określonych punktów końcowych API bezpośrednio z przepływu pracy. Ta karta obsługuje różne metody HTTP i umożliwia dynamiczną interakcję z systemami zewnętrznymi poprzez wysyłanie parametrów i danych. Usprawnia integrację z usługami zewnętrznymi i niestandardowymi interfejsami API, zapewniając bezproblemową komunikację.

## Komponenty karty:

1. **API Endpoint**
   * **Opis:** Docelowy punkt końcowy **DocBits API**, z którym ta karta będzie wchodzić w interakcję.
   * **Szczegóły:** Pole tekstowe, w którym użytkownicy określają punkt końcowy dla żądania API.
2. **HTTP Method**
   * **Opis:** Typ żądania HTTP, które ma zostać wykonane.
   * **Opcje:**
     1. **GET:** Pobiera dane z określonego punktu końcowego.
     2. **POST:** Wysyła dane do punktu końcowego.
     3. **PUT:** Aktualizuje istniejące dane w punkcie końcowym.
     4. **DELETE:** Usuwa dane w punkcie końcowym.
3. **Parameters**
   * **Opis:** Parametry zapytania, które mają zostać uwzględnione w żądaniu API.
   * **Szczegóły:** Pole tekstowe lub lista do wprowadzania par klucz-wartość dla adresu URL żądania.
4. **Data**
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

1. **Define API Endpoint:**\
   Wprowadź adres URL API, które chcesz wywołać.
2. **Select HTTP Method:**\
   Wybierz jedną z obsługiwanych metod (GET, POST, PUT, DELETE) na podstawie wymagań Twojego API.
3. **Provide Parameters:**\
   Dodaj wymagane parametry zapytania jako pary klucz-wartość.
4. **Include Data (if applicable):**\
   Dla metod POST lub PUT określ dane, które mają zostać wysłane w treści żądania.
5. **Condition Configuration:**\
   Skonfiguruj sekcje "Where" i "And Sections", aby zdefiniować, kiedy ma nastąpić wywołanie API.

## Podsumowanie:

Karta przepływu pracy **"Call API"** zwiększa automatyzację przepływu pracy, umożliwiając bezpośrednią interakcję z systemami zewnętrznymi. Zapewniając elastyczne konfiguracje punktów końcowych, metod i danych, gwarantuje, że przepływy pracy mogą bezproblemowo integrować się z zewnętrznymi interfejsami API lub niestandardowymi backendami. Możliwość warunkowego wykonywania wywołań API zapewnia precyzję i efektywność w automatyzacji komunikacji zewnętrznej.

***
