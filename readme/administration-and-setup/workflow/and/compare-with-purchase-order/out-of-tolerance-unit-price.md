# Out of Tolerance Unit Price

<figure><img src="../../../../.gitbook/assets/image (272).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Ta karta przepływu pracy służy do oceny, czy łączna wartość cen jednostkowych i określonego pola przekracza zdefiniowany próg lub jest od niego niższa. Pomaga zidentyfikować wszelkie rozbieżności, w których ceny jednostkowe w połączeniu z innymi polami są poza tolerancją, zapewniając, że warunki cenowe spełniają oczekiwania, oraz oznaczając wszelkie problemy do przeglądu lub dalszego działania.

## **Komponenty karty:**

1. **Field Name:**
   * **Opis**: Określa pole dokumentu zawierające wartość do połączenia z ceną jednostkową.
   * **Szczegóły**: Wartość w tym polu zostanie połączona z ceną jednostkową, tworząc łączną wartość do porównania.
2. **Operator:**
   * **Opis**: Definiuje warunek porównania łącznej wartości ceny jednostkowej i wartości pola z określoną wartością.
   * **Opcje**:
     * **Equals (=)**: Weryfikuje, czy łączna wartość ceny jednostkowej i pola odpowiada określonej wartości.
     * **Not Equals (≠)**: Zapewnia, że łączna wartość ceny jednostkowej i pola różni się od określonej wartości.
     * **Greater Than (>)**: Weryfikuje, czy łączna wartość ceny jednostkowej i pola przekracza określoną wartość.
     * **Greater or Equals (≥)**: Weryfikuje, czy łączna wartość ceny jednostkowej i pola jest większa lub równa określonej wartości.
     * **Lesser Than (<)**: Weryfikuje, czy łączna wartość ceny jednostkowej i pola jest mniejsza niż określona wartość.
     * **Lesser or Equals (≤)**: Weryfikuje, czy łączna wartość ceny jednostkowej i pola jest mniejsza lub równa określonej wartości.
3. **Value:**
   * **Opis**: Określa wartość, z którą porównywana będzie łączna wartość ceny jednostkowej i pola.
   * **Szczegóły**: Ta wartość liczbowa reprezentuje próg porównania. Jeśli łączna wartość ceny jednostkowej i pola przekracza tę wartość lub jest od niej niższa (na podstawie wybranego operatora), warunek wyzwoli określone akcje.

## **Funkcjonalność:**

* &#x20;**Ocena warunku:** System oblicza łączną wartość, mnożąc lub dodając cenę jednostkową do wartości pola, w zależności od konfiguracji. Wynik jest następnie porównywany z określoną wartością za pomocą wybranego operatora. Jeśli warunek jest spełniony (tj. łączna wartość jest poza tolerancją), przepływ pracy przechodzi do kolejnego kroku, czy to zatwierdzenia, odrzucenia, czy dalszego przeglądu.
* **Wykonanie akcji:**
  * **Warunek prawdziwy**: Jeśli porównanie daje wynik prawdziwy (tj. łączna wartość spełnia warunek), przepływ pracy wyzwala akcję powiązaną z warunkiem prawdziwym (np. zatwierdzenie lub powiadomienie).
  * **Warunek fałszywy**: Jeśli porównanie daje wynik fałszywy (tj. łączna wartość nie spełnia warunku), przepływ pracy nie będzie kontynuowany.

## **Konfiguracja:**

* Użytkownicy wybierają pole zawierające wartość do połączenia z ceną jednostkową. Następnie wybierają odpowiedni operator, aby określić sposób porównania łącznej wartości z określoną wartością. Na koniec użytkownik ustawia wartość, z którą porównywana będzie łączna cena.

## **Przykładowy scenariusz:**

* Faktura wymienia 50 jednostek produktu po 30 USD każda, co daje łącznie 1500 USD. Powiązany dokument ma pole ilości o wartości 10. Łączna cena jest obliczana przez pomnożenie ceny jednostkowej (30 USD) i ilości (10), co daje 300 USD. Karta porównuje następnie tę łączną wartość z progiem 250 USD. Przy użyciu operatora "Greater Than" karta identyfikuje, że 300 USD jest większe niż 250 USD, wyzwalając proces zatwierdzania dokumentu.

## **Podsumowanie:**

Karta przepływu pracy "Out of Tolerance Unit Prices Combined with Fields" pomaga zapewnić, że wartości cenowe i wartości pól są zgodne z regułami biznesowymi. Automatyzując tę kontrolę, organizacje mogą wcześnie zidentyfikować rozbieżności w procesie, zapewniając, że wszelkie ceny jednostkowe poza tolerancją są oznaczane do przeglądu lub niezbędnego działania.
