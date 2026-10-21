# Przypisz dokument do

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-0e17d9fb5a83-pl.png" alt="Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs." width="563"><figcaption><p>Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs.</p></figcaption></figure>

## Cel:

Karta przepływu pracy **„Przypisz dokument do \[Użytkownik/grupa] na podstawie tabeli decyzyjnej”** dynamicznie przypisuje dokumenty do użytkowników lub grup na podstawie wyniku **tabeli decyzyjnej**. Funkcja ta zapewnia, że przypisywanie dokumentów jest obsługiwane efektywnie i spójnie na podstawie predefiniowanych warunków.

## Komponenty karty:

1. **Użytkownik/Grupa**
   * **Opis:** Określa **użytkownika** lub **grupę**, do której zostanie przypisany dokument.
   * **Szczegóły:** Wybierane na podstawie wyniku **tabeli decyzyjnej**.
2. **Tabela decyzyjna**
   * **Opis:** **Tabela decyzyjna** jest używana do określenia odpowiedniego **użytkownika** lub **grupy** do przypisania dokumentu.
   * **Szczegóły:** Używa tabeli decyzyjnej zdefiniowanej w sekcji **„i”**.

## Funkcjonalność:

* **Ocena warunku:** Karta wykonuje swoją akcję tylko wtedy, gdy zarówno **„Kiedy”**, jak i **„I sekcje”** są prawdziwe.
* **Dynamiczne przypisanie dokumentu:** Dokument jest przypisywany do **użytkownika** lub **grupy** określonej przez **tabelę decyzyjną**.

## Konfiguracja:

* **Zdefiniuj tabelę decyzyjną:** Skonfiguruj **tabelę decyzyjną**, aby uwzględnić warunki określania docelowego **użytkownika** lub **grupy**.
* **Assign Document to User/Group:** Dokument zostanie dynamicznie przypisany na podstawie wyniku tabeli decyzyjnej.

## Podsumowanie:

Karta przepływu pracy **„Przypisz dokument do \[Użytkownik/grupa] na podstawie tabeli decyzyjnej”** zapewnia możliwości dynamicznego przypisywania dokumentów na podstawie logiki decyzyjnej. Zapewnia to dokładne i efektywne przetwarzanie poprzez automatyczne kierowanie dokumentów do odpowiedniego **użytkownika** lub **grupy**, zwiększając automatyzację przepływu pracy.

<!-- workflow-card-practical-example-20261021 -->

## Praktyczny przykład

**Kiedy używać:** Wybierz osobę przypisującą dokument z tabeli decyzyjnej.

**Konfiguracja:** Wybierz demonstracyjną tabelę decyzyjną, której reguła dopasowania zwraca skonfigurowanego recenzenta, i wybierz typ przypisanego oferowany przez tę wersję karty.

**Oczekiwany wynik i kontrprzykład:** Zwrócony użytkownik lub grupa staje się odbiorcą dokumentu. Pusty wynik tabeli decyzyjnej należy zdiagnozować osobno.

To jest ilustracyjna konfiguracja i oczekiwany wynik. Korzystaj z pól, użytkowników i grup skonfigurowanych w Twojej organizacji testowej; nie jest to twierdzenie, że ten przykład został wykonany.
