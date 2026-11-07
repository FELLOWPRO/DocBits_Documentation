---
description: "Twój proces. Twoja logika. Jasne połączenia."
---

# DocBits Advanced Workflow

Buduj obiegi dokumentów z połączonych kart. Wybieraj ścieżki według warunków, łącz wyniki i kieruj błędy osobną ścieżką, zachowując widok całego procesu.

## Zobacz prezentację funkcji

{% embed url="https://docbits-videos.fra1.digitaloceanspaces.com/settings-assistant/advanced-workflow-feature/v5/pl.mp4" %}

[Odtwarzacz z napisami](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-feature/v5/pl.html) · [Napisy](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-feature/v5/pl.vtt) · [Teksty ekranowe](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced-workflow-feature/v5/pl.txt) · 1:48 · Full HD

## Od faktury do kolejnej akcji

Przykład rozpoczyna faktura przychodząca. Kwota całkowita powyżej 1 000 wybiera ścieżkę Approval; 1 000 lub mniej wybiera Standard. Następnie film pokazuje rzeczywiste testy z wartościami 1 500 i 500 w projektancie DocBits wraz z wynikami.

## Trzy sposoby sterowania przepływem

| Funkcja | W praktyce |
| --- | --- |
| **Wybór ścieżki** | Połącz Start lub When z warunkiem. Success, Failed Condition i Error mają osobne wyjścia. |
| **Łączenie połączonych wyników** | Wait ANY wymaga co najmniej jednego pasującego połączonego źródła. Wait ALL wymaga pasującego połączonego wyniku z każdego źródła. Żaden nie anuluje innych akcji. |
| **Połączenie kolejnej akcji** | Użyj ścieżek błędów, Call API i notatek, aby połączyć systemy i opisać projekt. Notatki nie wykonują akcji. |

## Zbuduj własny workflow

<a href="../administration-and-setup/workflow/advanced-workflow-builder.md" class="button primary">Otwórz instrukcję Advanced Workflow</a>

[Omów swój proces z DocBits](https://docbits.com/en/book-demo/)

{% hint style="info" %}
Film łączy animowane karty z rzeczywistymi nagraniami angielskiego interfejsu Dev. Zawiera muzykę i polskie teksty ekranowe, bez narracji. Akcje testowe ustawiają przykładowe pole `approval_route` na `Approval` lub `Standard`; pełny proces zatwierdzania przez człowieka wymaga własnych akcji biznesowych. Demonstracji nie zapisano ani nie aktywowano. Animacje łączenia pokazują wymagane wyniki, a nie czas wykonania. Przetestuj osiągalność i pełne wykonanie dla dokumentu; poprawny test częściowy nie dowodzi działania w produkcji.
{% endhint %}
