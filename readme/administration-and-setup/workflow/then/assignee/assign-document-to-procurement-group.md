# Przypisz dokument do grupy zakupowej

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-9b2624ff9d34-pl.png" alt="Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs." width="563"><figcaption><p>Pola karty w pokazanej wersji. Pola nie są jeszcze skonfigurowane. Niektóre etykiety tej wersji interfejsu nie są jeszcze przetłumaczone lub mają nieprawidłowe tłumaczenie. Objaśnienia na tej stronie używają właściwych terminów; obraz przedstawia rzeczywisty interfejs.</p></figcaption></figure>

## **Cel:**

Karta przepływu pracy **"Assign to Procurement Group"** służy do przypisywania dokumentu do określonej grupy zakupowej w systemie. Pomaga to usprawnić zarządzanie dokumentami, zapewniając, że odpowiedni zespół obsługuje dokument na podstawie przypisanej mu grupy zakupowej.

## **Komponenty karty:**

1. **Grupa Zakupowa**
   * **Opis:** Określa grupę zakupową, do której zostanie przypisany dokument.
   * **Szczegóły:** Wybrana grupa zakupowa będzie odpowiedzialna za przetwarzanie i zarządzanie dokumentem.

## **Funkcjonalność:**

* **Ocena warunku:**\
  Karta wykonuje swoją akcję tylko wtedy, gdy zarówno **„Kiedy”**, jak i **„I sekcje”** są prawdziwe.
* **Wykonanie akcji:**\
  Jeśli oba warunki są prawdziwe, dokument jest przypisywany do określonej grupy zakupowej. Jeśli którykolwiek z warunków jest fałszywy, nie są podejmowane żadne akcje, a dokument pozostaje nieprzypisany.

## **Konfiguracja:**

* **Wybierz grupę zaopatrzenia:** Wybierz grupę zakupową, do której ma zostać przypisany dokument, z listy rozwijanej.

## **Podsumowanie:**

Karta przepływu pracy **"Assign to Procurement Group"** zapewnia prosty, ale skuteczny sposób na zapewnienie, że dokumenty są automatycznie przypisywane do właściwego zespołu zakupowego w celu dalszego przetwarzania.

<!-- workflow-card-practical-example-20261021 -->

## Praktyczny przykład

**Kiedy używać:** Wyślij wyjątek dotyczący zakupów do swojej grupy zaopatrzeniowej.

**Konfiguracja:** Wybierz skonfigurowaną grupę `Demo Procurement`.

**Oczekiwany wynik i kontrprzykład:** Dokument jest przypisany do tej grupy zakupowej. Nie można zakładać, że grupa zwykła o podobnej nazwie jest tym samym skonfigurowanym celem.

To jest ilustracyjna konfiguracja i oczekiwany wynik. Korzystaj z pól, użytkowników i grup skonfigurowanych w Twojej organizacji testowej; nie jest to twierdzenie, że ten przykład został wykonany.
