# Nawigacja w Layout Builder

Użyj **Layout Builder**, aby rozmieścić pola i grupy widoczne na dokumencie. Ten przewodnik wykorzystuje angielski układ **Invoice** w organizacji sandbox.

## Otwieranie układu Invoice

1. Przejdź do **Settings → Document Types**.
2. Znajdź **Invoice** i wybierz **Layouts** na jego karcie. Layout Builder otworzy się dla tego typu dokumentu.
3. Sprawdź selektor układu w lewym górnym rogu. Poniższy przykład pokazuje **DEFAULT**.

<figure><img src="../../../../../.gitbook/assets/dbdc177-document-types-en.png" alt="Angielska strona Document Types z kartą Invoice i linkiem Layouts"><figcaption>Otwórz **Layouts** z karty Invoice.</figcaption></figure>

## Znajdowanie grup i pól

Lewy panel **Elements** ma trzy sekcje. **Groups** wyświetla sekcje dokumentu; środkowy obszar roboczy pokazuje ich aktualny układ. Zaznacz pole w obszarze roboczym i otwórz **Properties**, aby zmienić jego ustawienia wyświetlania. Dostępne opcje opisuje [Configuring Field Properties](configuring-field-properties.md).

<figure><img src="../../../../../.gitbook/assets/dbdc177-layout-elements-en.png" alt="Angielski Layout Builder dla Invoice z listą Groups w panelu Elements i pogrupowanymi polami w obszarze roboczym"><figcaption>Lista Groups i obszar roboczy układu Invoice.</figcaption></figure>

Otwórz **Fields**, aby znaleźć dostępne pola dokumentu. Gdy lista jest długa, użyj pola wyszukiwania, a następnie przeciągnij pole do wybranej grupy w obszarze roboczym. Pola już umieszczone w układzie mogą być na liście niedostępne.

<figure><img src="../../../../../.gitbook/assets/dbdc177-layout-fields-en.png" alt="Angielski panel Fields w Layout Builder z wyszukiwaniem i dostępnymi polami Invoice"><figcaption>Przed umieszczeniem pola wyszukaj je wśród dostępnych.</figcaption></figure>

Otwórz **Form Elements**, aby znaleźć elementy wizualne, takie jak Text, Label, Check Box, separator, Button i Sub Group. Przeciągnij potrzebny element do obszaru roboczego, a następnie sprawdź jego **Properties**.

<figure><img src="../../../../../.gitbook/assets/dbdc177-layout-form-elements-en.png" alt="Angielski panel Form Elements w Layout Builder z listą pól tekstowych, etykiet, pól wyboru, przycisków i podgrup"><figcaption>Aktualna paleta Form Elements.</figcaption></figure>

## Rozmieszczanie i zapisywanie

- Zaznacz tytuł grupy w obszarze roboczym, aby go zmienić. Przycisk **+** nad obszarem roboczym dodaje grupę; sąsiednia ikona nawiasów klamrowych otwiera zaawansowany formularz grupy JSON.
- Najedź kursorem na grupę, aby zobaczyć akcje: kopiuj JSON, przesuń w górę, przesuń w dół, usuń i uchwyt przeciągania. Aby zmienić kolejność pól, przeciągaj je w obrębie grup lub między nimi.
- Zaznacz pole w obszarze roboczym, aby otworzyć **Properties**. Jego ikona usuwania usuwa je z tego układu. Aby skonfigurować walidację, OCR lub dopasowywanie, użyj osobnych [ustawień Fields](../fields/configuring-field-properties-1.md).
- Po edycji wybierz **Save** na górnym pasku. Zanim użyjesz pozostałych akcji na górnym pasku, w tym generowania szablonów, szablonów domyślnych i stosowania układu do źródeł, zapoznaj się z [Save and Apply Changes](save-and-apply-changes.md).
