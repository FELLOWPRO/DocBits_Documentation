# Kolumny tabeli

Kolumny tabeli określają, jakie kolumny ma tabela pozycji dokumentu danego typu: co DocBits wyodrębnia do każdej kolumny, co użytkownik widzi na ekranie walidacji oraz co jest wysyłane do systemu ERP podczas eksportu.

**Gdzie:** Ustawienia → Ustawienia globalne → Typy dokumentów → Kolumny tabeli

<figure><img src="../../../../../.gitbook/assets/structured-output-column-choice-pl-20261104.png" alt="Aktualna lista Use AI z opcjami Domyślne, Tak i Nie. Nie zmieniono żadnej opcji. Komórki tytułów ukryto w celu ochrony danych."><figcaption><p>Aktualna lista Use AI z opcjami Domyślne, Tak i Nie. Nie zmieniono żadnej opcji. Komórki tytułów ukryto w celu ochrony danych.</p></figcaption></figure>

## Co widzisz

Każdy wiersz to jedna kolumna jednej tabeli. Lista pokazuje:

| Kolumna | Znaczenie |
|---|---|
| **Column name** | Nazwa techniczna, generowana z tytułu (wielkie litery, podkreślenia). Używana w skryptach, mapowaniach eksportu i API. Nie można jej później zmienić. |
| **Title** | Etykieta wyświetlana na ekranie walidacji. Zmienisz ją ikoną tłumaczenia w kolumnie *Actions* (*Update translation key*). |
| **Column Type** | `AMOUNT`, `STRING`, `DATE`, `NUMBER`, `BOOLEAN` lub `CURRENCY`. Określa walidację i formatowanie. |
| **Table name** | Tabela, do której należy kolumna, na przykład `INVOICE_TABLE`. |
| **Is Required** | Dokumentu nie można zatwierdzić, dopóki ta kolumna jest pusta w którymkolwiek wierszu. |
| **Read Only** | Użytkownicy widzą wartość, ale nie mogą jej edytować. |
| **Hidden** | Kolumna nie jest ani wyświetlana, ani eksportowana. Służy do wyłączania domyślnych kolumn, których nie potrzebujesz. |
| **Use AI** | Wybór trzech stanów: Domyślne przejmuje wybór AI typu dokumentu, Tak jawnie żąda kolumny, a Nie wyklucza ją ze schematu bazowego. To niezależne od Wymagana, Tylko do odczytu i Ukryta. |
| **Actions** | Ikona tłumaczenia: zmiana tytułu. Ikona informacji: skąd pochodzi wyświetlana etykieta (Twoje tłumaczenie, wartość domyślna, klucz). Menu z trzema kropkami: *Delete*, tylko dla kolumn utworzonych przez Twoją organizację; kolumny domyślne można jedynie ukryć. |

Dwa przyciski nad listą:

* **Create new table**: druga tabela pozycji dla danego typu dokumentu (na przykład tabela opłat obok tabeli pozycji towarowych).
* **Add new table column**: otwiera okno opisane w [Dodawanie nowej kolumny](adding-a-new-column.md).

## Kolumny domyślne i własne kolumny

Każdy typ dokumentu jest dostarczany z zestawem kolumn domyślnych (dla faktur: numer pozycji, opis, ilość, cena jednostkowa, kwota całkowita, podatek, …). Należą one do DocBits, a nie do Twojej organizacji, więc nie można ich usunąć, można je jedynie ukryć. Kolumny dodane przez Ciebie należą do Twojej organizacji i można je usunąć.

{% hint style="info" %}
**Zmiany dotyczą tylko nowych dokumentów.** Kolumna, którą dodasz, ukryjesz lub usuniesz, pojawi się w dokumentach przesłanych lub zrestartowanych po zmianie. Dokumenty znajdujące się już na pulpicie zachowują tabelę w takiej postaci, w jakiej została wyodrębniona. Zrestartuj dokument, aby zastosować nową konfigurację.
{% endhint %}

## Powiązane strony

* [Cel i zastosowanie](purpose-and-use.md): gdzie widoczne są kolumny tabeli
* [Dodawanie nowej kolumny](adding-a-new-column.md)
* [Edytowanie i usuwanie kolumn](editing-and-deleting-columns.md)
* [Najlepsze praktyki](best-practices-2.md)
* [Rozwiązywanie problemów](troubleshooting-1.md)
* [Training Line Fields / Table Training](../../../../setup/document-training/training-line-fields-table-training/README.md): naucz DocBits, gdzie znajduje się tabela dostawcy
* [AI Table](../../../../../end-user-and-partner-section/end-user-section/ai-table/README.md): co użytkownik widzi na ekranie walidacji

## Use AI: Domyślne, Tak lub Nie

Otwórz [Kolumny tabeli](README.md) dla właściwego typu dokumentu i tabeli. **Użyj sztucznej inteligencji (Use AI)** jest listą trzech stanów, a nie polem wyboru. Zmiana zapisuje się natychmiast.

| Aktualna opcja | Wpływ na schemat bazowy |
| --- | --- |
| **Domyślne · żądane** lub **Domyślne · nie zażądano** | Przyjmuje ustawienie DocBits dla tego typu i nazwy kolumny. Domyślne nie oznacza zawsze włączone ani zawsze wyłączone. |
| **Tak · poproszono** | Jawnie żąda skonfigurowanej kolumny od AI. |
| **Nie · nie poproszono** | Wyklucza ją ze schematu bazowego, nawet jeśli normalnie jest żądana. |

Powrót do **Domyślne** usuwa jawny wybór. Nowa własna kolumna zwykle nie należy do domyślnego zestawu AI: wybierz **Tak**, aby AI ją zwracała. Domyślny zestaw AI nie oznacza wszystkich kolumn dostarczonych z DocBits. Sprawdź wskazany efekt i podgląd.

**Wymagana**, **Tylko do odczytu** i **Ukryta** sterują kompletnością, edycją i widocznością; nie zastępują wyboru AI. **Nie** nie usuwa kolumny ani jej wartości i nie blokuje reguł, skryptów lub innych źródeł danych. Trening dostawcy i dodatkowe tagi AI mogą rozszerzyć faktyczne żądanie: rozwiąż sprzeczności także tam. Przełącznik nie zastępuje automatycznie wyniku pochodzącego wyłącznie z reguł.

[Structured Output dla tabel](../../../../../end-user-and-partner-section/end-user-section/ai-table/structured-output.md).
