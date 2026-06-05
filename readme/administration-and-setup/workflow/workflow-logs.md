# Dzienniki Przepływu

## **Przegląd**

**Dzienniki Przepływu** pozwalają użytkownikom analizować, które przepływy pracy zostały wykonane dla dokumentu, zrozumieć wyniki wykonania i zagłębić się w szczegóły na poziomie warunków w celu debugowania lub walidacji.

## **Dostęp do Dzienników Przepływu**

Aby uzyskać dostęp do dzienników przepływu:

1. Przejdź do **Pulpitu**.
2. Kliknij menu **Akcje** (ikona trzech kropek) obok wybranego dokumentu.
3. Wybierz **Dzienniki Przepływu** z menu.
   * <mark style="color:red;">**Uwaga**</mark>**:** Funkcja workflow musi być włączona, aby uzyskać dostęp do tej opcji.
4.  Pojawi się **panel boczny** pokazujący podsumowanie wykonanych przepływów pracy.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FAlgg3jnSVRVyuYxy4tAp%252Fimage.png%3Falt%3Dmedia%26token%3D4e8fcd63-6113-47eb-95a4-95a7821dc9b9\&width=768\&dpr=4\&quality=100\&sign=9e6ba9f5\&sv=2)

## **Składniki Panelu Dzienników Przepływu**

#### **1. Liczniki Podsumowania Przepływu**

Znajdują się na górze panelu dzienników:

* **Niebieski**: Całkowita liczba wykonanych przepływów pracy.
* **Czerwony**: Przepływy pracy zakończone **błędami**.
* **Żółty**: Przepływy pracy, które nie zostały **zakończone** z powodu niezgodności warunków.
* **Zielony**: Pomyślnie **wykonane** przepływy pracy.

#### **2. Tabela Wykonania Przepływu**

Każdy wiersz w tabeli reprezentuje jedno wykonanie przepływu pracy i zawiera:

* **Nazwę Przepływu Pracy**
* **Znacznik Czasowy** (Utworzono)
* **Czas Wykonania** (w sekundach)
* **Ikona Wyniku**:
  * Zielony znak zaznaczenia: Przepływ pracy został pomyślnie wykonany.
  * Czerwony krzyżyk: Przepływ pracy został wykonany z błędem.
  * Pomarańczowy myślnik: Wykonanie zostało zatrzymane z powodu niespełnienia warunku

Kliknięcie **strzałki** po lewej stronie każdego wiersza rozwija **widok szczegółów przepływu pracy**.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="" width="563"><figcaption></figcaption></figure></div>

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FsauGR47dbpPRomGUugst%252Fimage.png%3Falt%3Dmedia%26token%3D00d6d92f-1512-4de0-97ea-012b1d194dee\&width=768\&dpr=4\&quality=100\&sign=a6c5b7c5\&sv=2)

### **Widok Szczegółów Przepływu Pracy**

Kliknięcie konkretnego wiersza przepływu pracy otwiera jego **szczegółowy dziennik wykonania**, pokazujący:

#### **Ocena Warunków**

* Blok **Kiedy...**: Warunek początkowy.
* Blok(i) **I...**: Dodatkowe warunki.
* Blok(i) **Wtedy...**: Akcje wykonywane, gdy wszystkie warunki są spełnione.

Każda linia warunku pokazuje:

* **Zielone zaznaczenie**: Warunek został spełniony.
* **Pomarańczowy myślnik**: Warunek nie został spełniony.
* **Czerwony krzyżyk**: Warunek nie powiódł się **z powodu błędu**

### **Ważna Informacja o Zachowaniu**

Jeśli warunek w przepływie pracy **nie jest spełniony**, system **zatrzymuje ocenianie kolejnych kart przepływu pracy** w ramach tego przepływu. To zachowanie zapobiega niepotrzebnemu przetwarzaniu. Jako wskaźnik wizualny, karta, która **nie spełniła warunku**, jest pokazana na **szaro**, a wszystkie **następne karty** w tym samym przepływie również będą wyświetlane na **szaro**, co oznacza, że nie zostały **wykonane**.
