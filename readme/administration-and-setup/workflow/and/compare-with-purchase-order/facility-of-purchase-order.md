# Obiekt zamówienia zakupu

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_check_facility_in_po_v2-pl-pl.png" alt="Obiekt zamówienia zakupu, Wersja 2" width="634"><figcaption><p>Wersja 2</p></figcaption></figure>

## Cel:

Ta karta przepływu pracy sprawdza obiekt zamówień zakupu dopasowanych do dokumentu względem listy kodów obiektów. Można jej używać, aby różnie obsługiwać dokumenty w zależności od obiektu (lokalizacji), dla którego złożono zamówienie, na przykład aby kierować je do zespołu odpowiedzialnego za ten obiekt.

Dopasowanie zamówienia zakupu powinno zostać wykonane przed tą kartą. Bez dopasowanego zamówienia zakupu karta zgłasza brakujące dane.

## Komponenty karty:

1. **Dowolny/Wszystkie**
   * **Opis:** Jak kody obiektów dopasowanych zamówień zakupu są oceniane względem listy.
   * **Opcje:**
     * **Każdy:** Co najmniej jeden wpis z listy występuje w kodach obiektów dopasowanych zamówień zakupu.
     * **Wszystko:** Każdy kod obiektu dopasowanych zamówień zakupu znajduje się na liście. Jeśli nie ustawiono żadnej wartości, karta używa **Wszystko**.
2. **Operator**
   * **Opis:** Czy obiekt powinien znajdować się na liście, czy nie.
   * **Opcje:**
     * **Jest**
     * **Nie jest**
3. **Kody nazw obiektów**
   * **Opis:** Kody obiektów, z którymi porównywany jest obiekt zamówienia zakupu.
   * **Szczegóły:** Można wprowadzić kilka kodów oddzielonych przecinkami.

## Funkcjonalność:

* **Ocena warunku:** Karta odczytuje numery zamówień zakupu dopasowanych do dokumentu, wczytuje te zamówienia zakupu i zbiera obiekt (lokalizację) każdego z nich. Zamówienia zakupu bez obiektu są pomijane. Zebrane kody obiektów są następnie porównywane z wartościami **Kody nazw obiektów** na karcie.
  * Przy **Każdy** i **Jest** porównanie nie uwzględnia wielkości liter, a wpis z listy jest uznawany również wtedy, gdy stanowi część dłuższego kodu obiektu (na przykład wpis `WH` zostaje znaleziony w `WH01`).
  * Przy **Wszystko** i **Jest** każdy kod obiektu z zamówień zakupu powinien występować na liście w dokładnie takiej samej pisowni, z uwzględnieniem wielkości liter.
  * Jeśli żadne z dopasowanych zamówień zakupu nie ma obiektu, **Wszystko** jest spełnione, a **Każdy** nie.
  * Przy **Nie jest** wynik nie jest po prostu odwrotnością **Jest**. Dziennik karty pokazuje, które kody zostały znalezione, a które nie zostały dopasowane, co pomaga sprawdzić działanie dla danej konfiguracji.
* **Wykonanie akcji:**
  * **Warunek prawdziwy:**\
    Jeśli warunek jest spełniony, przepływ pracy jest kontynuowany, na przykład krokiem przeznaczonym dla wymienionych obiektów.
  * **Warunek fałszywy:**\
    Jeśli warunek nie jest spełniony, przepływ pracy zatrzymuje się na niespełnionym warunku.
* **Brakujące dane:** Jeśli na karcie nie wprowadzono kodów obiektów lub dokument nie ma dopasowanego zamówienia zakupu, karta nie ocenia warunku i zgłasza brakujące dane w dzienniku przepływu pracy.

## Instalacja i konfiguracja:

* Kartę można dodać jako warunek And po dopasowaniu zamówienia zakupu, z kategorii **Porównaj z zamówieniem zakupu**. Następnie można ustawić **Każdy** lub **Wszystko**, operator oraz kody obiektów oddzielone przecinkami. Wprowadzenie kodów w takiej samej pisowni jak w zamówieniu zakupu jest najbezpieczniejszym wyborem, ponieważ **Wszystko** porównuje je dokładnie.
* Aby wypróbować konfigurację na istniejącym dokumencie, można użyć opcji **Karta testowa** w menu karty w Workflow Builder. Dziennik karty wymienia dopasowane zamówienia zakupu, znalezione w nich kody obiektów oraz kody, które nie zostały dopasowane.

## Podsumowanie:

Karta przepływu pracy „Facility of Purchase Order” udostępnia obiekt zamówionych towarów jako warunek przepływu pracy. Dzięki temu jeden przepływ pracy może różnie traktować dokumenty dla różnych obiektów na podstawie danych zamówienia zakupu, a nie tego, co jest wydrukowane na dokumencie.
