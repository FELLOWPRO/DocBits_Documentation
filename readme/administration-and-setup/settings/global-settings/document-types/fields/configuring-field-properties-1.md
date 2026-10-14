# Konfigurowanie właściwości pól

Użyj **Settings → Document Types → Fields**, aby kontrolować zachowanie pól danego typu dokumentu. Najpierw wybierz typ dokumentu; poniższy przykład pokazuje **Invoice** w angielskim interfejsie.

<figure><img src="../../../../../.gitbook/assets/dbdc155-field-properties-overview-en.png" alt="Angielskie ustawienia pól Invoice z progami rozpoznawania, wyszukiwaniem, kolumnami właściwości pól i przyciskiem Save Settings"><figcaption>Ustawienia pól Invoice w organizacji sandbox DocBits.</figcaption></figure>

## Znajdowanie pola i zmiana jego właściwości

1. W polu **Search by Name** wpisz nazwę lub etykietę pola. Filtruje to listę; nie zmienia pola.
2. Znajdź wiersz pola. Na przykład **Invoice number** ma nazwę techniczną `invoice_id`.
3. Dostosuj elementy sterujące w tym wierszu, a następnie wybierz **Save Settings**. Ten sam przycisk zapisu jest dostępny nad tabelą i pod nią.

<figure><img src="../../../../../.gitbook/assets/dbdc155-field-properties-filtered-en.png" alt="Angielskie pole Invoice number z elementami sterującymi Required, Read Only, Hidden, Force Validation, Use AI, OCR i Match Score"><figcaption>Wiersz Invoice number po wyszukaniu `invoice_id`.</figcaption></figure>

| Element sterujący | Do czego służy |
| --- | --- |
| **Required** | Oznacza informacje, które muszą być obecne do walidacji. Po zmianie tego ustawienia sprawdź wynik walidacji dokumentu. |
| **Read Only** | Wyświetla pole bez możliwości edycji jego wartości przez użytkowników. |
| **Hidden** | Ukrywa pole w zwykłym widoku dokumentu. |
| **Force Validation** | Wymaga, aby pole przeszło walidację. Szczegółowe reguły konfiguruje się osobno; to pole wyboru nie jest edytorem reguł. |
| **Use AI** | Włącza lub wyłącza żądanie ekstrakcji AI dla tego pola. Wiersz pokazuje, czy ekstrakcja jest żądana. |
| **OCR** | Wprowadź próg pewności OCR dla pola. Jest to liczba, a nie przełącznik włącz/wyłącz ani ustawienie języka. |
| **Match Score** | Wprowadź próg dopasowania dla pola. Jest to liczba, a nie przełącznik włącz/wyłącz. |

Suwaki **OCR** i **Match Score** w sekcji **Recognition Settings** stosują wartości do całej listy pól. Pola wyboru bezpośrednio pod tytułami kolumn stosują **Required**, **Read Only**, **Hidden** lub **Force Validation** do całej listy. Przed wybraniem **Save Settings** sprawdź, których wierszy dotyczą zmiany. **Restore Defaults** resetuje konfigurację pól; używaj tej opcji tylko wtedy, gdy chcesz zastąpić wprowadzone zmiany.

## Inne elementy sterujące w tym widoku

- **Create new group** i **Create field** dodają grupę lub pole. Zobacz [Adding and Editing Fields](adding-and-editing-fields.md).
- **Master Data Settings** otwiera [konfigurację danych podstawowych](master-data-settings.md).
- Skrajne lewe pola wyboru zaznaczają pola. Sąsiednie menu oferuje **Reassign Field Group** dla zaznaczonych pól.
- Przycisk plus **Formula** otwiera edytor formuł dla tego pola. Ikona **info** pokazuje informacje o polu. Ikona usuwania jest niedostępna dla pól standardowych.

Więcej informacji o walidacji i dopasowywaniu znajdziesz w [Setting Validation and Match Score](setting-validation-and-match-score.md).
