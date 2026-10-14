# Assign document to User

<figure><img src="../../../../.gitbook/assets/image (300).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Karta przepływu pracy **"Assign Document to User"** umożliwia użytkownikom przypisanie dokumentu do określonego użytkownika, zapewniając płynne zarządzanie przepływem pracy poprzez kierowanie dokumentów do odpowiedniej osoby. Version 3 dodaje możliwość użycia drzewa decyzyjnego do dynamicznego określania przypisania użytkownika na podstawie dostępnych warunków.

## **Komponenty karty:**

1. **User**
   * **Opis:** Określa użytkownika, do którego zostanie przypisany dokument.
   * **Szczegóły:** Do wyboru udostępniana jest lista rozwijana wszystkich dostępnych użytkowników. Wybrany użytkownik otrzyma dokument do dalszego działania.

## **Dodatkowe komponenty w Version 3:**

1. **Use Decision Tree**
   * **Opis:** Jeśli włączone, karta używa drzewa decyzyjnego do dynamicznego określania przypisania użytkownika.
   * **Opcje:**
     * **True:** Używa drzewa decyzyjnego do dynamicznego przypisania użytkownika.
     * **False:** Przypisuje dokument do wybranego użytkownika bez używania drzewa decyzyjnego.

## **Funkcjonalność:**

* **Ocena warunku:**\
  Karta wykonuje swoją akcję tylko wtedy, gdy zarówno **"Where"**, jak i **"And Sections"** są prawdziwe.
* **Przypisanie dokumentu:**\
  Karta przypisuje dokument do wybranego użytkownika, zapewniając, że zadanie jest kierowane do odpowiedniej osoby do działania. Pomaga to w odpowiedzialności i efektywnym zarządzaniu dokumentami.
* **Drzewo decyzyjne (Version 3):**\
  Jeśli drzewo decyzyjne jest włączone, karta ocenia warunki zdefiniowane w drzewie, aby dynamicznie wybrać użytkownika do przypisania dokumentu.

## **Konfiguracja:**

* **Select User:**\
  Wybierz **użytkownika** z listy rozwijanej, do którego zostanie przypisany dokument.
* **Use Decision Tree (Version 3):**\
  Włącz lub wyłącz użycie drzewa decyzyjnego do dynamicznego wyboru użytkownika.

## **Podsumowanie:**

Karta przepływu pracy **"Assign Document to User"** ułatwia efektywne kierowanie dokumentów, przypisując je do wybranego użytkownika, z dodatkową elastycznością w Version 3 umożliwiającą dynamiczne określanie użytkownika za pomocą drzewa decyzyjnego. Zapewnia to bardziej adaptacyjny i efektywny proces przepływu pracy.
