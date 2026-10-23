# Edytor układu

Edytor układu służy do rozmieszczania pól i elementów sterujących, które widzą osoby walidujące lub zatwierdzające dokument. Układ należy do jednego typu dokumentu, jednego pochodzenia i jednego typu układu, dlatego przed zapisaniem sprawdź te trzy ustawienia u góry strony.

## Otwieranie układu

1. Otwórz **Ustawienia → Typy dokumentów**.
2. Wybierz typ dokumentu, który chcesz edytować, i otwórz **edytor układu**. W przypadku podtypu dokumentu otwórz akcję edytor układu dla tego podtypu.
3. Sprawdź nagłówek. Lewy selektor to **Pochodzenie** (na przykład **Domyślny**), następnie **Typ dokumentu** (na przykład **Faktura**) i **Typ układu** (na przykład **Walidacja pól**). Każdy selektor otwiera listę; wybranie innej pozycji wczytuje dany układ. Jeśli edytor układu jest niedostępny, administrator może musieć włączyć ten moduł dla Twojej organizacji.

<figure><img src="../../../.gitbook/assets/layout-builder-overview-pl.png" alt="Edytor układu dla faktury w DocBits, z selektorami pochodzenia, typu dokumentu i typu układu, kartami Struktura, Pola i Elementy, obszarem roboczym układu oraz panelem Właściwości po prawej stronie"><figcaption><p>Edytor układu: selektory w nagłówku, listy elementów po lewej, obszar roboczy pośrodku i panel Właściwości po prawej.</p></figcaption></figure>

## Praca z nagłówkiem

* **Typ dokumentu** i **Typ układu** umożliwiają przełączanie się między układami. Strona ponownie wczytuje wybrany układ.
* Obok przycisku **Zapisz** DocBits pokazuje, czy układ ma **Niezapisane zmiany**. Po zapisaniu widoczna jest informacja o ostatnim zapisie.
* **Zapisz** zapisuje układ dla wybranego typu dokumentu, pochodzenia i typu układu.
* Menu **Więcej** (trzy kropki) zawiera pozycje **Automatyczne generowanie szablonu**, **Zastosuj domyślny układ do źródeł**, **Użyj domyślnego szablonu**, **Edytuj JSON**, **Kopiuj JSON** oraz **Ustawienia układu**. **Automatyczne generowanie szablonu** i **Użyj domyślnego szablonu** zastępują układ niestandardowy, dlatego najpierw sprawdź wybrany typ dokumentu i układ. **Edytuj JSON** służy do konfiguracji zaawansowanej i należy z niego korzystać tylko wtedy, gdy znasz format szablonu.
* Jeśli opuścisz stronę z niezapisanymi zmianami, DocBits zapyta, czy je zapisać, czy odrzucić.

## Znajdowanie elementów: Struktura, Pola, Elementy

Po lewej stronie znajdują się trzy karty:

| Karta | Do czego służy |
| --- | --- |
| **Struktura** | Pokazuje układ w formie drzewa. Grupy i ich pola są wymienione w kolejności, w jakiej pojawiają się w obszarze roboczym, wraz z liczbą pól umieszczonych i dostępnych. |
| **Pola** | Wszystkie pola skonfigurowane dla danego typu dokumentu, pogrupowane według grup pól i domyślnie zwinięte. Filtr przełącza między polami **Wszystkie**, **Nie używany** i **Ukryty**, a pod etykietą pola widoczna jest jego nazwa techniczna. |
| **Elementy** | Elementy prezentacji i interakcji, takie jak Tekst, Etykieta, Pole wyboru, separatory, tabele, przyciski i podgrupy. |

<figure><img src="../../../.gitbook/assets/layout-builder-structure-pl.png" alt="Karta Struktura w edytor układu przedstawiająca rozwinięte grupy Szczegóły faktury, Szczegóły płatności, Zamówienie zakupu i Szczegóły dostawy wraz z ich polami"><figcaption><p>Karta Struktura pokazuje zbudowany układ jako drzewo grup i pól.</p></figcaption></figure>

Wybierz pozycję, aby ją dodać, lub przeciągnij ją do obszaru roboczego. Tytuł grupy informuje osobę walidującą dokument, co należy do danej sekcji. Pola dokumentu wielokrotnego użytku utwórz lub zmień ich nazwy najpierw w sekcji [Typy dokumentów](README.md).

## Praca w obszarze roboczym

* **Główny układ** pokazuje układ samego dokumentu. **Tabela** pokazuje układ tabeli używany dla pozycji.
* **Dokument** otwiera lub zamyka przykładowy dokument obok obszaru roboczego, dzięki czemu możesz porównać układ z rzeczywistym dokumentem.
* Grupy są przedstawiane jako karty; pola w grupie można rozmieszczać w wierszach i nadawać im różne szerokości.

## Zmiana właściwości elementu

Wybierz element lub grupę w obszarze roboczym. Panel **Właściwości** po prawej stronie jest zawsze widoczny i podzielony na sekcje:

* **Wyświetlanie** – etykieta, nazwa pola, położenie etykiety i szerokość elementu.
* **Zachowanie** – tylko do odczytu, ukryty i indeks kart.
* **Wartości i listy** – wartości oferowane dla elementu.
* **Automatyzacja** – reguły, które wypełniają lub zmieniają element.
* **Obramowanie i odstępy** – wygląd elementu.

W przypadku szerokości wybierz jedną z wartości predefiniowanych (25, 33, 50, 66, 75 lub 100 procent), zamiast wpisywać wartość, i sprawdź wynik w obszarze roboczym. To, które sekcje i opcje się pojawiają, zależy od wybranego elementu. Więcej informacji znajdziesz w artykule [Konfigurowanie właściwości pól](../../settings/global-settings/document-types/layout-manager/configuring-field-properties.md).

## Sprawdzanie i zapisywanie

Rozmieść grupy i pola, sprawdź układ w obszarze roboczym i użyj przycisku **Zapisz** w nagłówku, gdy wynik będzie prawidłowy. Informacje o układach specyficznych dla pochodzenia znajdziesz w artykule [Układy według pochodzenia](origin-layouts.md).

{% hint style="info" %}
Zrzuty ekranu przedstawiają syntetyczne ustawienia w testowej organizacji DocBits, z językiem polskim wybranym w aplikacji. Podczas ich wykonywania żaden układ nie został zapisany ani zastąpiony.
{% endhint %}
