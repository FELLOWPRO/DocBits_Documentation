# Przypisz użytkownika z pola

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-a30b121432e4-pl.png" alt="Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs." width="563"><figcaption><p>Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs.</p></figcaption></figure>

## **Cel:**

Karta przepływu pracy **„Przypisz użytkownika z pola z opcją powrotu”** dynamicznie przypisuje użytkownika na podstawie wartości znalezionej w określonym polu dokumentu. Jeśli pole nie zawiera prawidłowego użytkownika, wybierany jest użytkownik zapasowy z predefiniowanej listy dostępnych użytkowników, aby zapewnić prawidłowe przypisanie zadania lub akcji.

## **Komponenty karty:**

1. **Nazwa pola**
   * **Opis:** Określa **pole dokumentu** zawierające informacje o użytkowniku do przypisania.
   * **Szczegóły:** To pole jest oceniane w celu określenia, który użytkownik powinien zostać przypisany. Jeśli pole zawiera prawidłowego użytkownika, ten użytkownik zostanie przypisany do zadania. Jeśli pole jest puste lub nieprawidłowe, zostanie przypisany użytkownik zapasowy.
2. **Użytkownik (awaryjny)**
   * **Opis:** Określa **użytkownika zapasowego**, który ma zostać przypisany, jeśli pole dokumentu nie zawiera prawidłowego użytkownika.
   * **Szczegóły:** Do wyboru udostępniana jest lista rozwijana wszystkich dostępnych użytkowników. Ten użytkownik zostanie przypisany, jeśli pole dokumentu jest puste lub nie zawiera prawidłowego użytkownika.

## **Funkcjonalność:**

* **Ocena warunku:**\
  Karta wykonuje swoją akcję tylko wtedy, gdy zarówno **„Kiedy”**, jak i **„I sekcje”** są prawdziwe.
* **Przypisanie użytkownika na podstawie pola:**\
  Karta najpierw próbuje przypisać zadanie lub akcję do użytkownika zidentyfikowanego w **Nazwa pola**.
* **Przypisanie użytkownika zapasowego:**\
  Jeśli pole nie zawiera prawidłowego użytkownika (lub jest puste), karta przypisuje zadanie do użytkownika zapasowego wybranego z listy rozwijanej **Użytkownik (awaryjny)**.

## **Konfiguracja:**

* **Wybierz nazwę pola:**\
  Wybierz **pole dokumentu**, które określa użytkownika do przypisania.
* **Wybierz użytkownika zastępczego:**\
  Wybierz **użytkownika zapasowego** z listy rozwijanej. Ten użytkownik zostanie przypisany do zadania, jeśli pole dokumentu nie zawiera prawidłowego użytkownika.

## **Podsumowanie:**

Karta przepływu pracy **„Przypisz użytkownika z pola z opcją powrotu”** zapewnia, że zadanie lub akcja jest zawsze przypisane do prawidłowego użytkownika. Jeśli użytkownik w polu dokumentu jest niedostępny, użytkownik zapasowy jest automatycznie przypisywany, zapewniając elastyczność i gwarantując ukończenie zadania.

<!-- workflow-card-practical-example-20261021 -->

## Praktyczny przykład

**Kiedy używać:** Przypisz recenzenta wskazanego na podstawie danych dokumentu.

**Konfiguracja:** Wybierz pole `reviewer_name` i użytkownika rezerwowego `Demo Reviewer A`. W pierwszym teście podaj rozpoznawalną nazwę użytkownika demonstracyjnego.

**Oczekiwany wynik i kontrprzykład:** Prawidłowa wartość pola wybiera tego użytkownika. Pusta lub niemożliwa do rozwiązania wartość wykorzystuje skonfigurowaną rezerwę; sprawdź oba przypadki.

To jest ilustracyjna konfiguracja i oczekiwany wynik. Korzystaj z pól, użytkowników i grup skonfigurowanych w Twojej organizacji testowej; nie jest to twierdzenie, że ten przykład został wykonany.
