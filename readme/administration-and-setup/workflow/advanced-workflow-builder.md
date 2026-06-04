# Advanced Workflow

Kreator **Advanced Workflow** to edytor grafu węzłów dla przepływów pracy, które wymagają rozgałęzień, równoległych ścieżek i kontroli przepływu — wykraczających poza liniowy model When/And/Then z kreatora Standard. Układasz węzły na obszarze roboczym i łączysz je, aby zdefiniować przebieg wykonywania.

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
