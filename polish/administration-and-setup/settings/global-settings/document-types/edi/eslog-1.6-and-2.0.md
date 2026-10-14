# eSLOG 1.6 i 2.0

**eSLOG 1.6** i **eSLOG 2.0** są w DocBits osobnymi formatami faktur elektronicznych. Wybierz wersję używaną przez przychodzącą słoweńską fakturę. Poniższe zrzuty ekranu pokazują aktualny angielski interfejs Sandbox w testowej organizacji dokumentacji; nie dowodzą, że faktura w którejkolwiek z tych wersji została przetworzona pomyślnie.

## Znajdowanie konfiguracji

1. Przejdź do **Settings → Document Types → Invoice → E-Doc**.
2. Rozwiń **E-SLOG 1.6** lub **E-SLOG 2.0**. Każdy format ma własne trzy wpisy.

<figure><img src="../../../../../.gitbook/assets/dbdc-142-eslog-16-en.png" alt="Angielski format E-SLOG 1.6 w Sandbox z wierszami Transformation, Preview i Extraction Paths"><figcaption>E-SLOG 1.6 na liście E-Doc dla Invoice.</figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/dbdc-142-eslog-20-en.png" alt="Angielski format E-SLOG 2.0 w Sandbox z wierszami Transformation, Preview i Extraction Paths"><figcaption>E-SLOG 2.0 ma osobne konfiguracje dla tych samych trzech etapów.</figcaption></figure>

| Wpis | Co kontroluje | Kolejny przewodnik |
| --- | --- | --- |
| **TRANSFORMATION (XSLT)** | Konwertuje dane źródłowe formatu na ustrukturyzowany XML. | [Transformation](edi/edi-transformation-file-guide.md) |
| **PREVIEW (XSLT)** | Definiuje czytelny widok dokumentu. | [Preview](edi/edi-preview-file-guide.md) |
| **EXTRACTION PATHS (JSON)** | Mapuje wartości XML na pola DocBits i kolumny tabeli. | [Extraction Paths](edi/edi-extraction-paths-file-guide.md) |

Kliknij wiersz, aby zobaczyć jego wersje i konfigurację. **Default** oznacza dostarczony wpis. **Last Modified At** pokazuje, kiedy wpis ostatnio zmieniono. Przycisk **New** rozpoczyna dodatkowy wpis konfiguracji. Menu z trzema kropkami w wierszu domyślnym oferuje **Customize**, które tworzy kopię specyficzną dla organizacji, oraz **Delete**; przed użyciem Delete uważnie sprawdź wybrany wiersz.

W konfiguracji ołówek obok aktywnej wersji tworzy wersję roboczą. Sprawdź wersję roboczą w panelu testowym **Preview**, używając ID reprezentatywnego przesłanego dokumentu, zanim aktywujesz ją znacznikiem wyboru. Ikona kosza przy wersji roboczej usuwa tę wersję roboczą. Rzeczywiste nazwy pól i ścieżki XML zależą od Twojego pliku eSLOG; szczegóły edytora znajdziesz w odpowiednim przewodniku powyżej.
