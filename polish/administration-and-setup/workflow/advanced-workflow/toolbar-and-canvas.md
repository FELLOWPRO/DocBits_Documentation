# Pasek narzędzi i Kanwa

## Film: Edytor i płótno

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/pl.mp4" %}

[Napisy (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/pl.vtt) · 1:44

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

[Zobacz wszystkie pięć rozdziałów](../advanced-workflow-videos.md)

Pasek narzędzi Zaawansowanego Workflow biegnie wzdłuż dolnej krawędzi kanwy i daje wszystko, czego potrzebujesz do budowania, nawigowania i zarządzania przepływem.

## Elementy sterujące paska narzędzi

- **+ Add** — otwiera menu węzłów, aby dodać węzeł (zobacz [Węzły](nodes.md)).
- **Undo / Redo** — cofa lub przywraca Twoje zmiany.
- **Zoom in / Zoom out** — zmienia poziom powiększenia kanwy.
- **Workflow name** — nadaje nazwę workflow w miejscu.
- **Edit description** — dodaje opis workflow.
- **Variables** — otwiera panel [Zmiennych](variables.md).
- **Help** — otwiera okno skrótów klawiszowych i pomocy.
- **Validate / Test** — sprawdza i uruchamia przepływ (zobacz [Walidacja i Testowanie](validation-and-testing.md)).
- **Snap to grid** — włącza lub wyłącza przyciąganie węzłów do siatki dla schludnych układów.
- **Mini-map** — włącza lub wyłącza małą mapę poglądową do nawigowania po dużych grafach.
- **Save** — zapisuje workflow. Wskaźnik **auto-save** pokazuje, kiedy przepływ został ostatnio zapisany automatycznie.

## Skróty klawiszowe

Naciśnij <kbd>?</kbd> na kanwie, aby w dowolnym momencie otworzyć okno skrótów i pomocy.

<figure><img src="../../../.gitbook/assets/workflow_advanced_shortcuts.png" alt="Okno skrótów klawiszowych i pomocy"><figcaption><p>Okno skrótów klawiszowych i pomocy — skróty, podświetlanie ścieżki wykonania i kolory połączeń.</p></figcaption></figure>

| Skrót | Działanie |
|---|---|
| <kbd>Cmd/Ctrl</kbd> + <kbd>S</kbd> | Zapisz workflow |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd> | Zwaliduj workflow |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd> | Przetestuj workflow |
| <kbd>Cmd/Ctrl</kbd> + <kbd>Z</kbd> / <kbd>Shift</kbd> + <kbd>Z</kbd> | Cofnij / Przywróć |
| <kbd>Cmd/Ctrl</kbd> + <kbd>C</kbd> / <kbd>V</kbd> / <kbd>D</kbd> | Kopiuj / Wklej / Duplikuj zaznaczone węzły |
| <kbd>Cmd/Ctrl</kbd> + <kbd>A</kbd> | Zaznacz wszystkie węzły |
| <kbd>Shift</kbd> + Przeciągnięcie | Zaznacz węzły (przeciągnięciem) |
| <kbd>Cmd/Ctrl</kbd> + Lewy przycisk myszy | Dodaj/usuń węzeł z zaznaczenia |
| Prawy przycisk myszy | Menu dodawania węzła |
| <kbd>Del</kbd> | Usuń zaznaczony węzeł |
| <kbd>?</kbd> | Pokaż tę pomoc |

## Następne kroki

- Buduj przepływ za pomocą [Węzłów](nodes.md) i [Zmiennych](variables.md).
