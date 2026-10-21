# Advanced Workflow

Kreator **Zaawansowany przepływ pracy** to edytor grafu węzłów dla przepływów pracy, które wymagają rozgałęzień, równoległych ścieżek i kontroli przepływu — wykraczających poza liniowy model When/And/Then z kreatora Standard. Układasz węzły na obszarze roboczym i łączysz je, aby zdefiniować przebieg wykonywania.

## Wideo: ścieżki przetwarzania faktur w DocBits

Poznaj Piotra i śledź jego wyjaśnienia w rzeczywistym polskim interfejsie DocBits. Sprawdza pulpit, listę workflow i licencję, a następnie otwiera niezapisany szkic w projektancie. Krok po kroku nadaje nazwę workflow, konfiguruje kontrolę kwoty oraz dwie akcje, rozmieszcza karty i łączy obie ścieżki. Następnie pokazuje przygotowanie testów z dokumentem lub własnymi danymi. Konto demonstracyjne nie ma subskrypcji Advanced Workflow i blokuje walidację; szkic pozostaje niezapisany i nieaktywny.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4" %}

[Otwórz film](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4) · [Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.vtt) · [Transkrypcja (tekst)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.txt) · 3:15

| W tym filmie | Początek |
| --- | --- |
| Poznaj administratora | [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4#t=0) |
| Sprawdź dostęp | [0:04](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4#t=4) |
| Nazwij workflow | [0:29](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4#t=29) |
| Skonfiguruj kontrolę kwoty | [0:42](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4#t=42) |
| Dodaj akcję Approval | [1:08](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4#t=68) |
| Dodaj akcję Standard | [1:29](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4#t=89) |
| Rozmieść karty | [1:49](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4#t=109) |
| Połącz ścieżki | [2:04](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4#t=124) |
| Przygotuj testy | [2:28](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4#t=148) |
| Walidacja, zapis i aktywacja | [2:49](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas-admin/v7/pl.mp4#t=169) |

<details>
<summary>Transkrypcja</summary>

**Poznaj administratora**

Zarządzam DocBits. Zbudujemy kontrolę kwoty faktury.

**Sprawdź dostęp**

Zaczynam od pulpitu workflow i otwieram listę. Następnie sprawdzam licencję. Workflow i Advanced Workflow wymagają aktywnego dostępu. Po włączeniu obu uprawnień opcja Nowy workflow oferuje Advanced Workflow. To konto dokumentacyjne nie ma aktywnej licencji workflow. Dlatego pracuję dalej na niezapisanym podglądzie w projektancie.

**Nazwij workflow**

Pracuję w prawdziwym projektancie DocBits. Najpierw nadaję wersji roboczej czytelną nazwę. Sprawdzimy kwotę faktury i pokażemy dwie możliwe ścieżki za pomocą prostych akcji. Ta demonstracja pozostanie niezapisana.

**Skonfiguruj kontrolę kwoty**

Otwieram menu dodawania i wybieram kartę warunku. W kategorii Pole dokumentu wybieram warunek Docfield. Wpisuję pole total_amount. Następnie wybieram porównanie większe niż. I wpisuję tysiąc. Użyjcie klucza pola ze swojego dokumentu. Kwota równa dokładnie tysiąc nie spełnia tego porównania.

**Dodaj akcję Approval**

Teraz dodaję kartę akcji z kategorii Pole dokumentu. Akcja ustawia wartość pola dokumentu. Używam przykładowego klucza approval_route. I wpisuję wartość Approval. To oznacza ścieżkę. Rzeczywisty proces zatwierdzania wymaga odpowiednich akcji biznesowych.

**Dodaj akcję Standard**

Dodaję drugą kartę z tą samą akcją. Akcja ustawia wartość pola dokumentu. Używam przykładowego klucza approval_route. Tym razem przykładowe pole otrzymuje wartość Standard. Obie karty są skonfigurowane. Potrzebują jeszcze połączeń, które określą wykonywaną akcję.

**Rozmieść karty**

Przeciągam karty, aby układ był czytelny. Obie akcje umieszczam po prawej stronie. Warunek znajduje się pośrodku, a Start po lewej. Przeniesienie karty zmienia jej położenie. Nie tworzy połączenia.

**Połącz ścieżki**

Przeciągam od wyjścia Start do wejścia warunku. Ścieżka sukcesu prowadzi do Approval przez niebieskie połączenie. Pomarańczowa ścieżka niespełnionego warunku prowadzi do Standard. Czerwone wyjście błędu jest osobnym wyjściem dla błędów oceny. Tutaj pozostaje niepołączone. W produkcyjnym workflow ustalcie sposób obsługi takich błędów.

**Przygotuj testy**

Przycisk testu na pasku otwiera wybór dokumentu testowego. Mogę wybrać dokument demonstracyjny albo przygotować kompletne dane niestandardowe. Przetestujcie kwoty większe, mniejsze i równe tysiąc. Sprawdźcie też brakującą kwotę. To konto nie ma licencji Advanced Workflow. Pokazuję przygotowanie testu, a nie wykonany wynik.

**Walidacja, zapis i aktywacja**

Walidacja sprawdza połączenia i ustawienia kart. Tutaj brak licencji blokuje walidację. Na koncie z dostępem zapisałbym workflow bezpośrednio na serwerze. Następnie osobno sprawdziłbym aktywację. Przed pierwszym zapisem przełącznik jest wyłączony. Wskaźnik automatycznego szkicu dotyczy lokalnej kopii w przeglądarce. Nie oznacza, że workflow jest zapisany lub aktywny.

</details>

## Jak uzyskać dostęp

Otwórz projektant Advanced Workflow z obszaru przepływów pracy (obszar roboczy kreatora zaawansowanego). Rozpoczynasz od węzła **Start** i budujesz przepływ, dodając węzły.

<figure><img src="../../.gitbook/assets/workflow_advanced_canvas.png" alt="Advanced Workflow node-graph canvas with toolbar"><figcaption><p>Obszar roboczy Advanced Workflow — graf węzłów z elementami sterującymi powiększeniem, uruchamianiem, siatką i zapisem. Nadaj przepływowi pracy nazwę na pasku narzędzi.</p></figcaption></figure>

## Dodawanie węzłów

Kliknij **+ Add**, aby otworzyć menu węzłów. Oprócz znanych kart **Gdy**, **I** i **Następnie** kreator zaawansowany dodaje węzły kontroli przepływu:

<figure><img src="../../.gitbook/assets/prior-u034-pl.png" alt="Menu węzłów zaawansowanego kreatora przepływów."><figcaption><p>Menu węzłów zaawansowanego kreatora przepływów.</p></figcaption></figure>

- **When / And / Then** — te same karty warunków i akcji co w kreatorze Standard.
- **Poczekaj WSZYSCY** — czekaj, aż *wszystkie* przychodzące gałęzie zostaną ukończone, zanim przejdziesz dalej.
- **Poczekaj DOWOLNY** — kontynuuj, gdy tylko *którakolwiek* przychodząca gałąź zostanie ukończona.
- **OR** — rozgałęź przepływ na alternatywne ścieżki.
- **Notatka** — swobodna adnotacja tekstowa na obszarze roboczym (nie wpływa na wykonywanie).

Uruchom przepływ za pomocą elementu sterującego odtwarzaniem, zweryfikuj go i zapisz przyciskiem zapisu na pasku narzędzi.

## Następne kroki

- Zobacz, co robi każda karta, w sekcji **Karty**.
- W przypadku prostych liniowych automatyzacji szybszy w konfiguracji jest kreator **Standard Workflow**.

[Zobacz wszystkie pięć rozdziałów](advanced-workflow-videos.md)
