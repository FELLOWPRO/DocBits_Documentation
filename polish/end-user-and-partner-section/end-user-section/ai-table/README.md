# Tabela AI

Tabela wyodrębniona przez AI to tabela pozycji, którą DocBits odczytuje za pomocą AI, gdy dostawca nie ma wytrenowanych reguł tabeli. Pojawia się na ekranie walidacji pod polami nagłówka. Ta strona opisuje, kiedy ją otrzymujesz, jak uruchomić ją ponownie i jak wpływać na to, co wyodrębnia.

## Kiedy otrzymujesz tabelę AI

* Administrator włączył opcję **Ekstrakcja tabeli AI** (*AI Table extraction*, Ustawienia → Przetwarzanie dokumentów → Klasyfikacja i ekstrakcja). Jeśli jest wyłączona, w obszarze tabeli wyświetla się komunikat *AI Table will display here. Enable in …*.
* Dostawca **nie ma zapisanych reguł**. Gdy tylko ktoś wytrenuje tabelę dostawcy i kliknie *Save Rules*, zapisane reguły zastępują tabelę AI dla tego dostawcy; wiersze pojawiają się wtedy w zakładce *Extracted table* zamiast w zakładce *AI Extracted table*.
* Wyjątek: kolumny oznaczone **Użyj AI** (*Use AI*) w ustawieniach kolumn tabeli wypełnia AI nawet u dostawców z zapisanymi regułami, patrz [Użyj AI dla pojedynczych kolumn](#use-ai-per-column).

Poziom AI odczytujący tabelę (Fast, Full, Nexus) jest ustawiany dla organizacji i można go nadpisać dla dostawcy w *Więcej ustawień* na ekranie walidacji, patrz [Model AI specyficzny dla dostawcy](../validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

## Ponowna ekstrakcja tabeli AI

Użyj tej funkcji, gdy brakuje wierszy lub kolumna jest przesunięta i chcesz, aby AI spróbowało ponownie, na przykład po dodaniu [tagu](ai-table-tags.md):

1. Dodaj lub zmień [tagi](ai-table-tags.md) w polu pod tabelą i kliknij **Apply**. AI odbudowuje tabelę tego dokumentu z Twoimi tagami i zmianami kolumn; nic nie jest jeszcze zapisywane dla dostawcy. Jeśli dokument ma pozycje dopasowane do PO, DocBits ostrzega, że odbudowa usunie dopasowania.
2. Wynik jest dobry? Kliknij **Save** (*Save Rules*), aby następny dokument tego dostawcy został wyodrębniony w ten sam sposób.
3. Aby zacząć od nowa, kliknij **Delete** (*Delete Rules*): DocBits potwierdza *Rules has been deleted successfully* i ponownie uruchamia ekstrakcję AI bez zapisanych tagów i formatowania.

*Delete Rules* usuwa tagi i reguły formatowania zapisane dla tego dostawcy, a nie konfigurację kolumn tabeli. Aby ponownie wyodrębnić cały dokument (nagłówek i tabelę) po zmianie ustawień lub kolumn przez administratora, użyj zamiast tego opcji *Restart* (Uruchom ponownie) w menu dokumentu na pulpicie.

## Użyj AI dla pojedynczych kolumn <a href="#use-ai-per-column" id="use-ai-per-column"></a>

Każda kolumna tabeli ma flagę **Użyj AI** (*Use AI*, Ustawienia → Ustawienia globalne → Typy dokumentów → [Kolumny tabeli](../../../administration-and-setup/settings/global-settings/document-types/table-columns.md)). Przy włączonej fladze AI wypełnia tę kolumnę nawet wtedy, gdy dostawca ma zapisane reguły; pozostałe kolumny nadal pochodzą z reguł. Typowe zastosowanie: kolumna opisu tekstowego, którą wytrenowane reguły przechwytują źle, albo wartość, która zmienia położenie na stronie.

Pamiętaj, że AI zgaduje wtedy tę kolumnę na podstawie całego wiersza. Jeśli konsekwentnie wstawia tam niewłaściwą wartość (na przykład sumę pozycji do kolumny *Charges*), kontrola sumy pozycji nie przechodzi w żadnym wierszu. W takim przypadku wyłącz *Użyj AI* dla tej kolumny albo dodaj tag, który mówi AI, czym jest ta kolumna.

## Ekstrakcja strukturalna

Przy włączonej w ustawieniach organizacji opcji **Użyj ekstrakcji strukturalnej (AI)** (*Use Structured Extraction (AI)*) AI zwraca tabelę w stałej strukturze, która mapuje się bezpośrednio na skonfigurowane kolumny tabeli, zamiast kopiować nagłówki kolumn dostawcy. Nazwy kolumn zawsze odpowiadają wtedy Twojej konfiguracji; kolumna, którą dostawca drukuje, ale której nie skonfigurowano, nie jest wyodrębniana. Poproś administratora o włączenie tej opcji, gdy nagłówki dostawców mocno się różnią i tracisz czas na ponowne mapowanie.

## Praca z wyodrębnioną tabelą

Oto kluczowe możliwości i instrukcje dotyczące użytkowania:

* **Usuwanie Kolumn**: Jeśli pewne kolumny w wyodrębnionej tabeli nie są potrzebne, użytkownicy mogą łatwo je usunąć, klikając ikonę "Usuń kolumnę" (reprezentowaną przez trzy pionowe kropki) obok nagłówka kolumny. Pomaga to uporządkować tabelę i skupić się tylko na istotnych informacjach.

<figure><img src="../../../.gitbook/assets/ai-table1.png" alt=""><figcaption></figcaption></figure>

* **Zmiana Formatu Waluty**: Format waluty można zmienić, wybierając pożądany format z menu rozwijanego obok pola "Waluta". Zapewnia to, że wartości walutowe są wyświetlane w preferowanym formacie, ułatwiając interpretację i analizę danych finansowych.

<figure><img src="../../../.gitbook/assets/ai-table2.png" alt=""><figcaption></figcaption></figure>

* **Pokazywanie/Ukrywanie Kolumn Niesparowanych**: Domyślnie w tabeli widoczne są tylko sparowane kolumny (kolumny z wyodrębnionymi danymi). Użytkownicy mogą jednak wybrać pokazanie lub ukrycie kolumn niesparowanych, klikając przycisk "Ukryj kolumny niesparowane" lub "Pokaż kolumny niesparowane" na dole tabeli. Ta funkcja jest przydatna, gdy użytkownicy chcą przejrzeć wszystkie dostępne kolumny, nawet jeśli aktualnie nie zawierają danych.

<figure><img src="../../../.gitbook/assets/ai-table3.png" alt=""><figcaption></figcaption></figure>

* **Zmiana Nagłówków Tabeli**: Nagłówki tabeli (nazwy kolumn) można zmodyfikować, klikając na nagłówek i wpisując pożądaną nazwę. Ta funkcja pozwala użytkownikom dostosować nazwy kolumn, aby lepiej pasowały do ich terminologii lub preferencji, co sprawia, że dane są bardziej czytelne i zrozumiałe.

<figure><img src="../../../.gitbook/assets/ai-table4.png" alt=""><figcaption></figcaption></figure>

* **Zapisywanie zmian**: **Save** obok tagów (podpowiedź *Save Rules*) zapisuje bieżące mapowanie kolumn, ukryte kolumny i tagi dla tego dostawcy. Następny dokument tego dostawcy jest wyodrębniany z ich użyciem.

Te funkcje dają Ci kontrolę nad wyodrębnionymi danymi. Jeśli ten sam dostawca za każdym razem wymaga tych samych poprawek, wytrenuj tabelę raz, patrz [Szkolenie pól linii / Szkolenie tabeli](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md); tabela AI nie będzie wtedy już używana dla tego dostawcy.
