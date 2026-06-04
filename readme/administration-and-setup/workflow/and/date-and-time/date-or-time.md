# Date or Time

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Ta karta DocBits sprawdza, czy określona wartość daty/godziny mieści się w zdefiniowanym zakresie. Umożliwia przepływom pracy kontynuowanie lub zatrzymanie w zależności od tego, czy warunek jest spełniony, co czyni ją odpowiednią dla operacji wrażliwych na czas lub harmonogramowania przepływów pracy.

## **Funkcjonalność:**

* **Walidacja daty/godziny:** Ta karta ocenia, czy dana data/godzina mieści się w określonym zakresie, używając następujących warunków:
  * **Is:** Sprawdza, czy data/godzina mieści się w zdefiniowanym zakresie początku i końca (włącznie).
  * **Is Not:** Zapewnia, że data/godzina znajduje się poza zdefiniowanym zakresem.

**Date/Time Range:** Użytkownicy określają wartości daty/godziny początku i końca, aby zdefiniować zakres do porównania.

## **Zastosowanie:**

Ta karta jest idealna do harmonogramowania, kontroli zgodności lub walidacji warunków opartych na czasie w przepływach pracy. Na przykład może być używana do zapewnienia, że zadania są wykonywane tylko w predefiniowanych ramach czasowych, lub do weryfikacji terminów.

## **Przykładowy scenariusz:**

* Użytkownik konfiguruje kartę, aby sprawdzić, czy **data złożenia** faktury **jest między** **"2024-11-01"** a **"2024-11-30"**. Jeśli data złożenia mieści się w tym zakresie, przepływ pracy przechodzi do przetwarzania płatności. Jeśli nie, przepływ pracy wyzwala powiadomienie do dalszego przeglądu.

Korzystając z karty "Date/Time Range Validation", organizacje mogą zapewnić dokładne harmonogramowanie, zwiększyć zgodność i usprawnić przepływy pracy, przestrzegając predefiniowanych ograniczeń czasowych.
