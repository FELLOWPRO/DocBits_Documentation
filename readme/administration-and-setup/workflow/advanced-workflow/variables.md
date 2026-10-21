# Zmienne

## Film: Zmienne, testy i aktywacja

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/pl.mp4" %}

[Otwórz film](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/pl.mp4) · [Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_testing/v3/pl.vtt) · 1:56

<details>
<summary>Transkrypcja</summary>

**Wybierz typ zmiennej**

Otwórz zmienne ikoną nawiasów klamrowych. Wybierz tekst, liczbę, tak lub nie albo dokument. Szukaj według nazwy. Zmienna Document przechowuje odwołanie ustawiane dedykowaną akcją; formularz nie przyjmuje wartości dokumentu.

**Zmienne organizacji**

Wybierz unikalną nazwę, typ i wartość początkową. Tworzenie, edycja i usuwanie zmiennych zapisują się natychmiast dla organizacji. Inne workflow mogą je współdzielić. Zapisanie lub odrzucenie płótna nie cofa zmian zmiennych.

**Najpierw sprawdź strukturę**

Wybierz walidację. Przejrzyj błędy i ostrzeżenia nad płótnem. Kliknij komunikat, aby przejść do węzła. Sprawdź akcje, wejścia, wyjścia, cykle i połączenia gałęzi. Poprawna struktura nie gwarantuje poprawności danych wykonania.

**Wybierz kontekst testu**

Odtwarzanie na pasku otwiera wybór dokumentu. Użyj dokumentu, danych niestandardowych lub testu bez dokumentu dla niezależnych kart. Odtwarzanie na Start uruchamia bezpośrednio. Test obejmuje bieżące płótno z niezapisanymi zmianami i symuluje działania destrukcyjne.

**Przygotowanie i sprawdzanie scenariuszy testowych**

Przygotuj oddzielne testy dla kwot powyżej, poniżej i równych tysiąc oraz brakujących danych. Po uruchomieniu sprawdź komunikaty i czasy: zielony oznacza sukces, pomarańczowy fałsz, czerwony błąd, szary pominięcie. Ponownie przetestuj poprawki. Menedżer testów pozwala powtarzać scenariusze.

**Zapisz przed aktywacją**

Automatyczny zapis zachowuje lokalny szkic około trzydzieści sekund po zmianach. Zapisz jawnie na serwerze. Aktywacja wymaga pierwszego zapisu. Sprawdź stan włączenia na liście workflow, zanim oczekujesz automatycznego wykonania.

</details>

[Zobacz wszystkie pięć rozdziałów](../advanced-workflow-videos.md)

**Zmienne** pozwalają zapisać wartości raz i wykorzystać je ponownie w węzłach Zaawansowanego Workflow — na przykład próg, stałego odbiorcę lub wartość odczytaną z dokumentu i przekazaną do późniejszego węzła. Panel zmiennych otwierasz przyciskiem **Variables** (ikona `{ }`) na pasku narzędzi.

<figure><img src="../../../.gitbook/assets/workflow_advanced_variables.png" alt="Panel zmiennych pogrupowanych według typu z przyciskiem New Variable"><figcaption><p>Panel zmiennych — zmienne pogrupowane według typu, z wyszukiwaniem i przyciskiem <strong>New Variable</strong>.</p></figcaption></figure>

## Typy zmiennych

Zmienne są pogrupowane według typu:

- **Text** — wartość tekstowa (np. opis lub stała etykieta).
- **Yes/No** — flaga logiczna (Yes / No).
- **Document** — odwołanie do dokumentu lub pola dokumentu.

Użyj pola wyszukiwania, aby szybko znaleźć zmienną, gdy lista się rozrasta.

## Tworzenie zmiennej

Kliknij **New Variable**, nadaj jej nazwę i typ oraz ustaw jej wartość. Zmienna staje się wtedy dostępna do odwołania z kart na Twoich węzłach, dzięki czemu możesz przechowywać konfigurację w jednym miejscu i zmieniać ją bez edytowania każdego węzła.

## Następne kroki

- Zobacz, jak węzły korzystają z tych wartości, w sekcji [Węzły](nodes.md).
- Zwaliduj i uruchom workflow w [Walidacji i Testowaniu](validation-and-testing.md).

## Zmienne liczbowe

**Number (Liczba)** to osobny typ zmiennej, obok Text, Yes/No i Document. Wprowadź liczbę bez symbolu waluty. Zmienne organizacji są współdzielone przez przepływy pracy; tworzenie, zmiana i usunięcie zapisują się natychmiast, niezależnie od zapisania lub odrzucenia zmian na obszarze roboczym. Przed zmianą sprawdź powiązane przepływy i przetestuj wartości poniżej progu, równe progowi i powyżej progu.
