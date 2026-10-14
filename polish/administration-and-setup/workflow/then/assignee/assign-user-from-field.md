# Assign user from field

<figure><img src="../../../../.gitbook/assets/image (299).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Karta przepływu pracy **"Assign User from Field with Fallback"** dynamicznie przypisuje użytkownika na podstawie wartości znalezionej w określonym polu dokumentu. Jeśli pole nie zawiera prawidłowego użytkownika, wybierany jest użytkownik zapasowy z predefiniowanej listy dostępnych użytkowników, aby zapewnić prawidłowe przypisanie zadania lub akcji.

## **Komponenty karty:**

1. **Field Name**
   * **Opis:** Określa **pole dokumentu** zawierające informacje o użytkowniku do przypisania.
   * **Szczegóły:** To pole jest oceniane w celu określenia, który użytkownik powinien zostać przypisany. Jeśli pole zawiera prawidłowego użytkownika, ten użytkownik zostanie przypisany do zadania. Jeśli pole jest puste lub nieprawidłowe, zostanie przypisany użytkownik zapasowy.
2. **User (Fallback)**
   * **Opis:** Określa **użytkownika zapasowego**, który ma zostać przypisany, jeśli pole dokumentu nie zawiera prawidłowego użytkownika.
   * **Szczegóły:** Do wyboru udostępniana jest lista rozwijana wszystkich dostępnych użytkowników. Ten użytkownik zostanie przypisany, jeśli pole dokumentu jest puste lub nie zawiera prawidłowego użytkownika.

## **Funkcjonalność:**

* **Ocena warunku:**\
  Karta wykonuje swoją akcję tylko wtedy, gdy zarówno **"Where"**, jak i **"And Sections"** są prawdziwe.
* **Przypisanie użytkownika na podstawie pola:**\
  Karta najpierw próbuje przypisać zadanie lub akcję do użytkownika zidentyfikowanego w **Field Name**.
* **Przypisanie użytkownika zapasowego:**\
  Jeśli pole nie zawiera prawidłowego użytkownika (lub jest puste), karta przypisuje zadanie do użytkownika zapasowego wybranego z listy rozwijanej **User (Fallback)**.

## **Konfiguracja:**

* **Select Field Name:**\
  Wybierz **pole dokumentu**, które określa użytkownika do przypisania.
* **Select Fallback User:**\
  Wybierz **użytkownika zapasowego** z listy rozwijanej. Ten użytkownik zostanie przypisany do zadania, jeśli pole dokumentu nie zawiera prawidłowego użytkownika.

## **Podsumowanie:**

Karta przepływu pracy **"Assign User from Field with Fallback"** zapewnia, że zadanie lub akcja jest zawsze przypisane do prawidłowego użytkownika. Jeśli użytkownik w polu dokumentu jest niedostępny, użytkownik zapasowy jest automatycznie przypisywany, zapewniając elastyczność i gwarantując ukończenie zadania.
