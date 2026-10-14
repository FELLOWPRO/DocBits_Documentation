# Compare values in table

<figure><img src="../../../../.gitbook/assets/image (48).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Ta karta DocBits wykonuje porównanie wartości w dwóch określonych kolumnach w tabeli, na podstawie wybranego warunku. Jest przydatna w scenariuszach wymagających walidacji relacji między punktami danych, takich jak kontrola jakości, kontrole spójności danych lub weryfikacja zgodności.

## **Funkcjonalność:**

* **Porównanie kolumn:** Ta karta umożliwia użytkownikom ustawienie warunków porównania wartości między dwiema kolumnami w tej samej tabeli.
* **Operators:** Dostępne są następujące operatory do zdefiniowania porównania:
  * **Equals (=):** Sprawdza, czy wartości w dwóch kolumnach są dokładnie równe.
  * **Not Equals (≠):** Zapewnia, że wartości w dwóch kolumnach nie są równe.
  * **Greater Than (>):** Potwierdza, że wartości w pierwszej kolumnie są większe niż w drugiej kolumnie.
  * **Greater or Equals (≥):** Zapewnia, że wartości w pierwszej kolumnie są większe lub równe wartościom w drugiej kolumnie.
  * **Lesser Than (<):** Sprawdza, czy wartości w pierwszej kolumnie są mniejsze niż w drugiej kolumnie.
  * **Less or Equals (≤):** Zapewnia, że wartości w pierwszej kolumnie są mniejsze lub równe wartościom w drugiej kolumnie.
* **Table and Column Selection:** Użytkownicy określają tabelę i dwie kolumny, które chcą porównać.

## **Zastosowanie:**

Ta karta jest idealna dla analityków danych, zespołów kontroli jakości lub specjalistów ds. zgodności, którzy muszą zapewnić, że wartości w jednej kolumnie odnoszą się do wartości w innej zgodnie z określonymi regułami, umożliwiając zaawansowaną walidację danych.

## **Przykładowy scenariusz:**

* Użytkownik konfiguruje kartę, aby sprawdzić, czy wartości w kolumnie "Current Stock" są **większe lub równe (≥)** wartościom w kolumnie "Minimum Stock Level" w tabeli "Inventory". Jeśli wszystkie wartości spełniają ten warunek, przepływ pracy jest kontynuowany, potwierdzając, że poziomy zapasów są wystarczające.

Korzystając z karty "Column Value Comparison", organizacje mogą zapewnić spójność danych, utrzymać standardy jakości i zweryfikować relacje danych w tabelach.
