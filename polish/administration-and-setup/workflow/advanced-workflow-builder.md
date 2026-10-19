# Advanced Workflow

Kreator **Advanced Workflow** to edytor grafu węzłów dla przepływów pracy, które wymagają rozgałęzień, równoległych ścieżek i kontroli przepływu — wykraczających poza liniowy model When/And/Then z kreatora Standard. Układasz węzły na obszarze roboczym i łączysz je, aby zdefiniować przebieg wykonywania.

## Wideo: ścieżki przetwarzania faktur w DocBits

Film przedstawia skonfigurowany workflow w rzeczywistym interfejsie DocBits: kontrolę kwoty, dwa działania, połączenia i przygotowanie przypadków testowych.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/pl.mp4" %}

[Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/pl.vtt)

Zrzuty przedstawiają niezapisany szkic demonstracyjny. `total_amount` i `approval_route` to przykładowe klucze pól. `Approval` i `Standard` oznaczają ścieżki. Skonfiguruj działania biznesowe wymagane w swoim procesie.

<details>
<summary>Transkrypcja</summary>

**Faktura z dwiema ścieżkami**

To prawdziwy zaawansowany workflow w DocBits. Sprawdzenie kwoty faktury prowadzi do dwóch działań. Połączenia określają, które działanie zostanie wykonane. Przykład wykorzystuje niezapisany szkic i pola demonstracyjne.

**Konfiguracja kontroli kwoty**

Otwórz Dodaj, wybierz And i warunek dotyczący pola dokumentu. Wskaż pole kwoty, wybierz Większe niż i wpisz tysiąc. Użyj dokładnego klucza pola z konfiguracji dokumentu.

**Konfiguracja działań**

Dodaj dwie karty Then. Obie ustawiają pole demonstracyjne approval route. Jedna wpisuje Approval, druga Standard. Wartości te oznaczają wybraną ścieżkę. W produkcyjnym workflow skonfiguruj właściwe działania biznesowe.

**Łączenie wyjść wyników**

Połącz Start z wejściem warunku. Niebieskie wyjście sukcesu połącz z Approval, a pomarańczowe wyjście fałszywego warunku ze Standard. Czerwone wyjście obsługuje osobno błędy oceny. Samo położenie kart nie tworzy ścieżki.

**Przygotowanie testów**

Otwórz Test na pasku narzędzi. Wybierz dokument testowy lub wprowadź jego pełne dane w formacie JSON. Sprawdź kwoty powyżej, poniżej i równe tysiąc oraz brakujące wartości. Po wykonaniu przejrzyj wyniki węzłów.

**Walidacja, zapis i aktywacja**

Zweryfikuj połączenia i ustawienia kart. Zapisz workflow na serwerze, a następnie osobno sprawdź aktywację. Automatyczne szkice przeglądarki nie zastępują zapisu. Wykonywanie i dostęp do dzienników wymagają odpowiedniego modułu i subskrypcji.

</details>

## Jak uzyskać dostęp

Otwórz projektant Advanced Workflow z obszaru przepływów pracy (obszar roboczy kreatora zaawansowanego). Rozpoczynasz od węzła **Start** i budujesz przepływ, dodając węzły.

<figure><img src="../../.gitbook/assets/workflow_advanced_canvas.png" alt="Advanced Workflow node-graph canvas with toolbar"><figcaption><p>Obszar roboczy Advanced Workflow — graf węzłów z elementami sterującymi powiększeniem, uruchamianiem, siatką i zapisem. Nadaj przepływowi pracy nazwę na pasku narzędzi.</p></figcaption></figure>

## Dodawanie węzłów

Kliknij **+ Add**, aby otworzyć menu węzłów. Oprócz znanych kart **When**, **And** i **Then** kreator zaawansowany dodaje węzły kontroli przepływu:

<figure><img src="../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Advanced Workflow Add menu with node types"><figcaption><p>Menu węzłów <strong>+ Add</strong>: When / And / Then oraz Wait ALL, Wait ANY, OR i Note.</p></figcaption></figure>

- **When / And / Then** — te same karty warunków i akcji co w kreatorze Standard.
- **Wait ALL** — czekaj, aż *wszystkie* przychodzące gałęzie zostaną ukończone, zanim przejdziesz dalej.
- **Wait ANY** — kontynuuj, gdy tylko *którakolwiek* przychodząca gałąź zostanie ukończona.
- **OR** — rozgałęź przepływ na alternatywne ścieżki.
- **Note** — swobodna adnotacja tekstowa na obszarze roboczym (nie wpływa na wykonywanie).

Uruchom przepływ za pomocą elementu sterującego odtwarzaniem, zweryfikuj go i zapisz przyciskiem zapisu na pasku narzędzi.

## Następne kroki

- Zobacz, co robi każda karta, w sekcji **Cards**.
- W przypadku prostych liniowych automatyzacji szybszy w konfiguracji jest kreator **Standard Workflow**.

[Zobacz wszystkie pięć rozdziałów](advanced-workflow-videos.md)
