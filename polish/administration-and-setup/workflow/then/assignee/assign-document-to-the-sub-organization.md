# Przypisz dokument do organizacji podrzędnej

<figure><img src="../../../../.gitbook/assets/workflow_card_action_change_doc_suborg_v2-pl-pl.png" alt="Przypisz dokument do organizacji podrzędnej, Wersja 2" width="634"><figcaption><p>Wersja 2</p></figcaption></figure>

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
