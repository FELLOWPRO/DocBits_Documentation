# Assign Sequentially to User/Group

<figure><img src="../../../../.gitbook/assets/image (11) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel**

Karta przepływu pracy "**Assign the Document Sequentially to User/Group Based on Decision Table**" dynamicznie przypisuje dokumenty do użytkownika lub grupy, w zależności od oceny tabeli decyzyjnej. Zapewnia to, że dokumenty są odpowiednio kierowane na podstawie predefiniowanych reguł.

## **Komponenty karty**

1. **Priority (Value)**
   * **Opis**: Określa poziom priorytetu dla przypisań, gdzie niższe liczby reprezentują wyższy priorytet.
   * **Szczegóły**: Numeryczne pole wprowadzania, w którym można ustawić wartość priorytetu w celu kontrolowania kolejności przypisywania.

## **Funkcjonalność**

* **Ocena tabeli decyzyjnej**:\
  Tabela decyzyjna ocenia predefiniowane warunki, aby zdecydować, czy dokument jest przypisany do użytkownika, czy grupy.
* **Przypisanie dokumentu**:
  * Jeśli tabela decyzyjna zwraca użytkownika, dokument jest przypisywany bezpośrednio do tego użytkownika.
  * Jeśli tabela decyzyjna zwraca grupę, dokument jest przypisywany do grupy sekwencyjnie, z poszanowaniem określonej wartości priorytetu.

## **Konfiguracja**

1. Dodaj kartę **Assign the Document Sequentially** do swojego przepływu pracy.
2. Skonfiguruj pole **Priority (Value)**:
   * Wprowadź wartość liczbową, aby ustawić priorytet przypisania.
3. Zapisz i aktywuj przepływ pracy, aby zastosować konfigurację.

## **Podsumowanie**

Karta przepływu pracy "**Assign the Document Sequentially to User/Group Based on Decision Table**" zapewnia efektywne i dynamiczne kierowanie dokumentów. Wykorzystując logikę tabeli decyzyjnej i wartości priorytetu, karta ułatwia dokładne przypisanie do użytkownika lub grupy, usprawniając przepływy pracy dokumentów.
