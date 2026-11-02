# Pola Nagłówka Szkolenia

Po przesłaniu dokumentu zostaniesz przeniesiony na ekran walidacji.\
Niektóre pola mogą być już wypełnione — jest to zasługa inteligencji zbiorowej DocBits. Jednak inne pola mogą pozostać puste. Zazwyczaj oznacza to, że typ dokumentu nie został jeszcze w pełni przeszkolony, więc DocBits nie wie jeszcze, skąd wydobyć tę informację.

Możesz pomóc w szkoleniu DocBits, aby rozpoznawał te pola, ręcznie identyfikując poprawne dane.\
**Proszę zauważyć:** jeśli pole pozostaje puste, może to po prostu oznaczać, że informacja nie znajduje się w przesłanym dokumencie.

<figure><img src="../../../.gitbook/assets/s150-header_field_training_0-pl.png" alt="Walidacja fikcyjnej faktury przed trenowaniem pól nagłówka."><figcaption><p>Walidacja fikcyjnej faktury przed trenowaniem pól nagłówka.</p></figcaption></figure>

### Aby przeszkolić pole:

1. Kliknij pole, które chcesz przeszkolić.
2. Następnie albo:
   * **Podwójnie kliknij** na odpowiednich danych w dokumencie, albo
   * **Narysuj prostokąt wyboru** wokół danych za pomocą kursora.

<figure><img src="../../../.gitbook/assets/s150-header_field_training_1-pl.png" alt="Wybór numeru faktury jako punktu początkowego treningu."><figcaption><p>Wybór numeru faktury jako punktu początkowego treningu.</p></figcaption></figure>

Powtórz ten proces dla wszystkich wymaganych pól.\
Gdy wszystkie niezbędne pola zostaną wypełnione, **kliknij "Zapisz Reguły"**, aby zapisać szkolenie. Zapewnia to, że DocBits uczy się, gdzie znaleźć każdy kawałek informacji dla podobnych dokumentów w przyszłości.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/header_field_training_2.png)

Po zapisaniu, twój dokument jest gotowy do wyeksportowania — a następnym razem DocBits automatycznie wydobyje przeszkolone pola.

Po zamierzonym zapisaniu treningu przetestuj inne dokumenty tego samego dostawcy. Eksport zależy również od walidacji i skonfigurowanego przepływu.
