# Pole wyboru jest zaznaczone

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_checkbox_is_v2-pl-pl.png" alt="Pole wyboru jest zaznaczone, Wersja 2" width="634"><figcaption><p>Wersja 2</p></figcaption></figure>

## Cel:

Ta karta przepływu pracy sprawdza, czy pole wyboru w dokumencie jest zaznaczone, czy niezaznaczone. Może być używana do tego, aby przepływ pracy był kontynuowany dopiero po ustawieniu znacznika w dokumencie, na przykład znacznika weryfikacji.

## Film administratora:

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-checkbox-admin/v2/pl.mp4" %}

[Otwórz film z polskimi napisami](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-checkbox-admin/v2/pl-theme-v4.html)

## Komponenty karty:

1. **Nazwa pola**
   * **Opis:** Techniczna nazwa pola wyboru w dokumencie.
   * **Szczegóły:** Pole powinno być polem wyboru (logicznym) danego typu dokumentu.
2. **Wartość logiczna**
   * **Opis:** Stan, jaki powinno mieć pole wyboru.
   * **Opcje:**
     * **PRAWDA:** Pole wyboru powinno być zaznaczone.
     * **FAŁSZ:** Pole wyboru powinno być niezaznaczone.

## Funkcjonalność:

* **Ocena warunku:** Gdy przepływ pracy dociera do karty, karta odczytuje bieżącą wartość pola w dokumencie i porównuje ją z ustawieniem **Wartość logiczna**. Karta nie obserwuje pola w czasie i go nie zmienia.
  * Pusta wartość pola wyboru jest uznawana za niezaznaczoną.
  * Jeśli nie wybrano żadnej wartości w **Wartość logiczna**, karta sprawdza, czy pole wyboru jest niezaznaczone.
  * Jeśli pole nie jest polem wyboru, karta odnotowuje to w dzienniku przepływu pracy i mimo to porównuje jego wartość.
* **Wykonanie akcji:**
  * **Warunek prawdziwy:**\
    Jeśli stan pola wyboru odpowiada ustawieniu **Wartość logiczna**, przepływ pracy jest kontynuowany kolejnymi kartami.
  * **Warunek fałszywy:**\
    Jeśli nie odpowiada, przepływ pracy zatrzymuje się z niespełnionym warunkiem.
* **Brakujące dane:** Jeśli pole nie istnieje w dokumencie, karta nie ocenia warunku. Zgłasza, że pola nie znaleziono w dokumencie, co jest innym wynikiem niż niezaznaczone pole wyboru.

## Instalacja i konfiguracja:

* Kartę można dodać jako warunek And z kategorii **Pole dokumentu**. Następnie w polu **Nazwa pola** wpisuje się techniczną nazwę pola wyboru i wybiera **PRAWDA** lub **FAŁSZ**.
* Za pomocą opcji **Karta testowa** w menu karty w Workflow Builder można sprawdzić konfigurację na dokumencie z zaznaczonym polem wyboru, na dokumencie z niezaznaczonym polem wyboru i na dokumencie bez tego pola.

## Podsumowanie:

Karta przepływu pracy „Checkbox is checked” zamienia pole wyboru w dokumencie w warunek przepływu pracy. Dzięki temu przepływ pracy może poczekać na krok ręczny, taki jak zakończona weryfikacja, zanim zostaną wykonane kolejne akcje.
