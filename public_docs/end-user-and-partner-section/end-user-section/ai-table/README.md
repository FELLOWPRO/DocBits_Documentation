# AI Table

AI Table służy do sprawdzania wyodrębnionych pozycji, poprawiania kolumn i zapisywania instrukcji dla układu dostawcy. Wybierz odpowiednią instrukcję. Structured Output ma własny przewodnik z opcjami Domyślne/Tak/Nie, nadpisaniami, podglądem i pełnym przykładem.

* [Ustawienia i nadpisania](configuration.md)
* [Structured Output dla tabel](structured-output.md)
* [Kolumny i poprawki](columns-and-corrections.md)
* [Instrukcje AI](ai-instructions.md)
* [Tagowanie tabeli AI](ai-table-tags.md)
* [Wyjaśnianie ekstrakcji i diagnostyka](explain-extraction.md)
* [Asystent i uprawnienia](assistant-and-permissions.md)

<figure><img src="../../../.gitbook/assets/anatomy-ai-table.svg" alt="Izometryczna ilustracja czytnika tabel: głowica czytająca z kasetą instrukcji skanuje tabelę dokumentu, panel krosowy podłącza każdą zwróconą kolumnę do skonfigurowanej kolumny, a skonfigurowane kolumny stoją jako pojemniki, każdy z trzypozycyjnym pokrętłem Use AI."><figcaption><p>AI czyta tabelę i zwraca kolumny. Każda zwrócona kolumna jest mapowana na skonfigurowaną kolumnę tabeli (zwrócona kolumna bez mapowania pozostaje ukryta), każda skonfigurowana kolumna ma własne ustawienie Use AI (Domyślne, Tak lub Nie), a instrukcje AI oraz <strong>Zapisz jako szkolenie</strong> kształtują sposób odczytu kolejnych dokumentów o układzie tego dostawcy.</p></figcaption></figure>

## Kiedy otrzymujesz tabelę AI

* Administrator włączył opcję **Ekstrakcja tabeli AI** (Ustawienia → Przetwarzanie dokumentów → Klasyfikacja i ekstrakcja, patrz [Ustawienia dla administratorów](#ustawienia-dla-administratorow)). Jeśli jest wyłączona, w obszarze tabeli wyświetla się komunikat *Tutaj wyświetli się tabela AI. Włącz w …*.
* Sprawdź czytelny tekst lub wejście Vision. Zapisane klasyczne reguły mogą nadal określać faktyczną ścieżkę; sprawdź [użytą ścieżkę ekstrakcji](../../../overview-and-basics/faq/document-processing/which-extraction-path-was-used.md).
* Każda kolumna ma wybór Use AI o trzech stanach. Sprawdź też rzeczywiste źródło i reguły dostawcy; Structured Output nie zastępuje każdej tabeli opartej na regułach.

Poziom AI odczytujący tabelę (Fast, Full, Nexus) jest ustawiany dla organizacji i można go nadpisać dla dostawcy, patrz Model AI specyficzny dla dostawcy.

## Tabela AI w skrócie

<figure><img src="../../../.gitbook/assets/ai-table-overview-pl.png" alt="Wyodrębniona tabela AI z nagłówkami kolumn i czterema wierszami"><figcaption><p>Dwie zakładki, tabela Wyodrębniona tabela AI i nagłówki jej kolumn.</p></figcaption></figure>

* **Zakładki.** *Wyodrębniona tabela AI* to to, co odczytała AI. *Wyodrębniona tabela* to klasyczna tabela z wytrenowanych reguł. Zakładka AI otwiera się domyślnie, gdy dokument ma tabelę AI.
* **Nagłówek kolumny.** Każda kolumna pokazuje swoją nazwę, mały symbol **pochodzenia** (najedź na niego kursorem: *AI · mapowanie*, *AI · synonim* itd. informują, jak AI dopasowała kolumnę), menu **trzech kropek** oraz, dla kolumny zmapowanej, **przycisk z nazwą**, którym możesz zmienić, jaką kolumną ma być.
* **Przyciski wierszy.** **x** na początku wiersza usuwa ten wiersz. Kliknij wiersz prawym przyciskiem myszy, aby wybrać *Wybierz jako koszt dodatkowy* / *Usuń jako dodatkowy koszt*.
* **Pasek narzędzi w stopce.** Ikony na dole ekranu dodają lub ukrywają kolumny i wiersze, patrz [Pasek narzędzi w stopce](#pasek-narzedzi-w-stopce).
* **Karta Instrukcje dla sztucznej inteligencji** pod tabelą: prompt, dodatkowe kolumny, **Zmiana testu**, **Stosować**, **Zapisz jako szkolenie**, **Usuwać**, **Eksport**, patrz [Podaj instrukcje dla AI](#podaj-instrukcje-dla-ai).

{% hint style="info" %}
Elementy sterowania kolumnami działają tylko wtedy, gdy możesz edytować dokument. Jeśli są wyszarzone, dokument jest tylko do odczytu lub zablokowany w innej sesji. Gdy czerwony baner informuje, że dokument jest zablokowany przez Twojego użytkownika w innej sesji, przycisk **Odblokować** przejmuje blokadę.
{% endhint %}


## Ustawienia dla administratorów

Czytaj dalej: [Ustawienia i nadpisania](configuration.md).

### Użyj AI dla pojedynczych kolumn

Czytaj dalej: [Structured Output dla tabel](structured-output.md).

<a id="wybierz-właściwą-kolumnę-ponowne-mapowanie"></a>
<a id="wybierz-własciwa-kolumne-ponowne-mapowanie"></a>
<a id="menu-trzech-kropek"></a>
<a id="pasek-narzędzi-w-stopce"></a>
<a id="pasek-narzedzi-w-stopce"></a>

## Zmiana kolumny

Czytaj dalej: [Kolumny i poprawki](columns-and-corrections.md).

<a id="zasugeruj-za-pomocą-nexus"></a>
<a id="zasugeruj-za-pomoca-nexus"></a>
<a id="test-zastosowanie-zapis-co-robi-każdy-przycisk"></a>
<a id="test-zastosowanie-zapis-co-robi-kazdy-przycisk"></a>

## Podaj instrukcje dla AI

Czytaj dalej: [Instrukcje AI](ai-instructions.md).


## Sprawdź, co zrobiła AI

Czytaj dalej: [Wyjaśnianie ekstrakcji i diagnostyka](explain-extraction.md).


## Praktyczne przykłady

Czytaj dalej: [Wyjaśnianie ekstrakcji i diagnostyka](explain-extraction.md).

<a id="zaproponuj-regułę-administratorowi"></a>
<a id="zaproponuj-regułe-administratorowi"></a>

## Asystent a tabela AI

Czytaj dalej: [Asystent i uprawnienia](assistant-and-permissions.md).


## Kto co może

Czytaj dalej: [Asystent i uprawnienia](assistant-and-permissions.md).

## Powiązane strony

* [Tagowanie tabeli AI](ai-table-tags.md)
* [Szkolenie Pól Linii/Szkolenie Tabeli](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md)
* [Touchless Intelligence](../../../administration-and-setup/touchless-intelligence.md)
