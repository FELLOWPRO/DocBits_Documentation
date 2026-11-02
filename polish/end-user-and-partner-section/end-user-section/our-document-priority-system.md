# Nasz System Priorytetów Dokumentów

W naszym systemie przetwarzania dokumentów obsługujemy codziennie dużą liczbę dokumentów od wielu klientów. Aby zapewnić, że dokumenty każdego klienta są przetwarzane w odpowiednim czasie, wdrożyliśmy zaawansowany system priorytetów. System ten dynamicznie dostosowuje priorytety w zależności od liczby oczekujących dokumentów, które ma klient, zapewniając **sprawiedliwość** i **efektywność**. Przyjrzyjmy się, jak działa ten system priorytetów i kiedy licznik zadań jest resetowany.

**Kluczowe Koncepcje Systemu Priorytetów**

Nasz system priorytetów opiera się na kilku kluczowych koncepcjach:

1. **Oczekujące Dokumenty**: To liczba dokumentów, które klient złożył, ale które jeszcze nie zostały przetworzone.
2. **Interwał Resetowania**: System okresowo resetuje liczbę oczekujących dokumentów do zera, aby zapewnić, że żaden klient nie może monopolizować zasobów przetwarzania w nieskończoność.

**Jak Ustalany Jest Priorytet**

Oto krok po kroku wyjaśnienie, jak ustalany jest priorytet przetwarzania dokumentów:

1. **Śledzenie Oczekujących Dokumentów**: Każdy klient ma liczbę oczekujących dokumentów. Ta liczba pomaga nam wiedzieć, ile dokumentów czeka na przetworzenie dla każdego klienta.
2. **Resetowanie Licznika**: Aby zachować sprawiedliwość, resetujemy liczbę oczekujących dokumentów do zera, jeśli minął ustalony czas (interwał resetowania) od ostatniej aktualizacji. Ten interwał jest domyślnie ustawiony na 1500 sekund (lub 25 minut).
3. **Aktualizowanie Licznika**: Jeśli interwał resetowania nie minął, zmniejszamy liczbę oczekujących dokumentów o jeden za każdym razem, gdy sprawdzamy, symulując przetwarzanie dokumentu.
4. **Ustalanie Priorytetów**: Priorytet przetwarzania zadań opiera się na liczbie oczekujących dokumentów. Im mniej oczekujących dokumentów, tym wyższy priorytet, co oznacza, że te zadania będą przetwarzane wcześniej. Mamy określone progi do przypisania poziomów priorytetów od 1 (najwyższy priorytet) do 9 (najniższy priorytet).

**Poziomy Priorytetów**

Poziomy priorytetów są przypisywane na podstawie liczby oczekujących dokumentów w następujący sposób:

* **Priorytet 9**: Jeśli liczba oczekujących dokumentów jest mniejsza niż -20
* **Priorytet 8**: Jeśli liczba oczekujących dokumentów jest mniejsza niż -14
* **Priorytet 7**: Jeśli liczba oczekujących dokumentów jest mniejsza niż -12
* **Priorytet 6**: Jeśli liczba oczekujących dokumentów jest mniejsza niż -10
* **Priorytet 5**: Jeśli liczba oczekujących dokumentów jest mniejsza niż -8
* **Priorytet 4**: Jeśli liczba oczekujących dokumentów jest mniejsza niż -6
* **Priorytet 3**: Jeśli liczba oczekujących dokumentów jest mniejsza niż -4
* **Priorytet 2**: Jeśli liczba oczekujących dokumentów jest mniejsza niż -2
* **Priorytet 1**: Jeśli liczba oczekujących dokumentów jest większa lub równa -2

{% hint style="info" %}
Mówiąc prościej, w miarę wzrostu liczby oczekujących dokumentów, poziom priorytetu maleje, co oznacza, że te dokumenty są przetwarzane później w porównaniu do innych o wyższych priorytetach.
{% endhint %}

**Kiedy Licznik Jest Resetowany**

Licznik oczekujących dokumentów jest resetowany do zera, jeśli minęło więcej niż interwał resetowania (**1500** sekund) od ostatniej aktualizacji. Ten mechanizm zapewnia, że żaden klient nie może gromadzić oczekujących dokumentów w nieskończoność i wykorzystywać zasobów systemu. Poprzez okresowe resetowanie licznika gwarantujemy, że każdy klient otrzymuje sprawiedliwy udział w czasie przetwarzania.
