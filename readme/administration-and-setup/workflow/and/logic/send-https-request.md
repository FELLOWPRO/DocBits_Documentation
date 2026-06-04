# Send HTTPS Request

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Cel:**

Ta karta DocBits służy do ułatwienia interakcji z systemami zewnętrznymi poprzez wysyłanie żądań HTTPS do określonych adresów URL. Umożliwia przepływom pracy wykonywanie akcji, takich jak pobieranie, aktualizacja lub usuwanie danych, poprzez wykonywanie wywołań API, zapewniając bezproblemową integrację z usługami zewnętrznymi.

## **Funkcjonalność:**

* **Wykonanie żądania HTTPS:** Karta wysyła żądanie do określonego adresu URL przy użyciu skonfigurowanej metody HTTP (np. GET, POST, PUT, DELETE).
* **Headers and Parameters:** Użytkownicy mogą dołączyć niestandardowe nagłówki i parametry zapytania, aby zapewnić, że żądanie spełnia wymagania zewnętrznego API.
* **Request Data:** Umożliwia użytkownikom zdefiniowanie ładunku danych (jeśli dotyczy) do wysłania z żądaniem, takiego jak dane JSON lub zakodowane w formularzu.
* **Response Evaluation:** Przepływ pracy sprawdza, czy otrzymany kod statusu odpowiada oczekiwanej wartości, zapewniając pomyślną komunikację przed kontynuowaniem.
* **Obsługiwane metody HTTP:**
  * GET: Pobiera dane z określonego adresu URL.
  * POST: Przesyła dane do określonego adresu URL w celu utworzenia zasobów.
  * PUT: Aktualizuje istniejące zasoby pod określonym adresem URL.
  * DELETE: Usuwa zasoby z określonego adresu URL.

## **Zastosowanie:**

Ta karta jest szczególnie przydatna w scenariuszach, w których przepływy pracy muszą wchodzić w interakcję z zewnętrznymi interfejsami API w celu wymiany danych, takich jak wysyłanie aktualizacji do CRM, pobieranie statusów zamówień lub publikowanie nowych wpisów w bazie danych.

## **Przykładowy scenariusz:**

* Użytkownik konfiguruje kartę, aby wysłać żądanie POST do zewnętrznego systemu zarządzania zamówieniami z ładunkiem zawierającym szczegóły nowego zamówienia. Niestandardowe nagłówki są dodawane w celu uwzględnienia tokenów uwierzytelniania API. Karta jest ustawiona tak, aby kontynuować tylko wtedy, gdy kod statusu odpowiedzi to 201 (Created). Jeśli kod statusu jest inny, przepływ pracy wyzwala powiadomienie o błędzie do ręcznej interwencji.

Korzystając z karty "Send HTTPS Request", organizacje mogą zautomatyzować integracje zewnętrzne, poprawić komunikację między systemami i usprawnić złożone przepływy pracy.
