# Przypisz dokument do organizacji podrzędnej

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-a05599461b30-pl.png" alt="Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs." width="563"><figcaption><p>Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs.</p></figcaption></figure>

## **Cel:**

Karta przepływu pracy **„Przypisz dokument do podorganizacji”** przypisuje dokument do określonej sub-organizacji w systemie, zapewniając, że jest on kierowany do odpowiedniej jednostki organizacyjnej w celu przetwarzania.

## **Komponenty karty:**

1. **Podorganizacja**
   * **Opis:** Określa sub-organizację, do której zostanie przypisany dokument.
   * **Szczegóły:** Do wyboru docelowej sub-organizacji udostępniana jest lista rozwijana dostępnych sub-organizacji.

## **Funkcjonalność:**

* **Ocena warunku:**\
  Karta wykonuje swoją akcję tylko wtedy, gdy zarówno **„Kiedy”**, jak i **„I sekcje”** są prawdziwe.
* **Przypisanie dokumentu:**\
  Karta przypisuje dokument do sub-organizacji wybranej z listy rozwijanej.

## **Konfiguracja:**

* **Wybierz podorganizację:**\
  Wybierz odpowiednią sub-organizację z listy rozwijanej, do której ma zostać przypisany dokument.

## **Podsumowanie:**

Karta przepływu pracy **„Przypisz dokument do podorganizacji”** zapewnia, że dokumenty są kierowane do właściwej sub-organizacji, usprawniając proces zarządzania dokumentami poprzez przypisywanie odpowiedzialności na podstawie struktury organizacyjnej.

<!-- workflow-card-practical-example-20261021 -->

## Praktyczny przykład

**Kiedy używać:** Prześlij dokument do znanej jednostki biznesowej.

**Konfiguracja:** Wybierz skonfigurowaną organizację podrzędną `Demo North`.

**Oczekiwany wynik i kontrprzykład:** Po akcji dokument należy do wybranej podorganizacji. Potwierdź cel przed włączeniem przepływu pracy, ponieważ reguły dostępu organizacji podrzędnej mogą się różnić.

To jest ilustracyjna konfiguracja i oczekiwany wynik. Korzystaj z pól, użytkowników i grup skonfigurowanych w Twojej organizacji testowej; nie jest to twierdzenie, że ten przykład został wykonany.
