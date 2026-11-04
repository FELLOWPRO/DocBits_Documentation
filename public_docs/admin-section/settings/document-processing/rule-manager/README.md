# Menedżer Reguł

\


Dokument ten zawiera szczegółowe wyjaśnienie zasad rozwiązywania konfliktów stosowanych w systemie fakturowania DocBits. Zasady te mają na celu automatyczne zarządzanie rozbieżnościami między szczegółami faktury a danymi zamówienia (PO), zapewniając dokładne uzgadnianie finansowe. System stosuje te zasady do przetwarzania pozycji faktury, opłat i podatków oraz generuje odpowiednie korekty lub notatki w razie potrzeby.

## Struktura Reguł

### &#x20;1. Metadane

• wersja: Identyfikuje wersję pliku mapowania.

• rewizja: Numer rewizji do śledzenia zmian.

• autor: Wskazuje twórcę pliku mapowania.

• opis: Krótkie streszczenie celu pliku.

• created\_at & updated\_at: Znaczniki czasu, kiedy plik został utworzony i ostatnio zaktualizowany.

### &#x20;2. Konfiguracja Eksportu

Sekcja konfiguracji eksportu definiuje mapowanie między polami danych w systemie a odpowiadającymi polami w plikach eksportowych.

• Nagłówek: Definiuje pola nagłówka dla eksportowanych danych faktury.

• Pozycje Podatkowe: Określa pola dla pozycji podatkowych w eksporcie.

• Opłaty Nagłówka Zamówienia: Mapuje pola związane z dodatkowymi opłatami na poziomie nagłówka zamówienia.

• Pozycje Paragonu: Mapuje pola dla poszczególnych pozycji w paragonie.

• Opłaty Pozycji Zamówienia: Definiuje pola dla opłat związanych z konkretnymi pozycjami zamówienia.

• Pozycje Kosztów: Określa pola dla linii alokacji kosztów.

• Nota Debetowa & Nota Kredytowa: Definiuje pola do generowania not debetowych i kredytowych w przypadku rozbieżności.

### 3. Zasady Rozwiązywania Konfliktów

Zasady te zajmują się rozbieżnościami między danymi faktury a odpowiadającymi danymi PO. Każda zasada składa się z kilku komponentów:

• Nazwa: Opisowa nazwa zasady, wskazująca typ rozbieżności, którą się zajmuje.

• Sekcja: Wskazuje, która część faktury (np. receipt\_lines, line\_charges) dotyczy zasady.

• Aktywna: Wartość logiczna (prawda lub fałsz) wskazująca, czy zasada jest obecnie aktywna.

• Kryteria Dopasowania: Warunki, które uruchamiają zasadę na podstawie porównań między rzeczywistymi danymi faktury a oczekiwanymi danymi PO.

• Działania: Definiuje, co system powinien zrobić, gdy zasada zostanie uruchomiona, w tym dostosowanie wartości, zastosowanie opłat lub generowanie not kredytowych/debetowych.

## Wspólne Elementy w Regułach

### Operatory Porównania

Operatory te definiują, jak rzeczywiste wartości faktury są porównywane z oczekiwanymi wartościami PO:

• równe

• większe niż

• większe lub równe

• mniejsze niż

• mniejsze lub równe

• w tolerancji

• poza tolerancją

\


### Status Zatwierdzenia

Wskazuje, czy rozbieżność jest zatwierdzona, czy nie:

• zatwierdzona

• odrzucona

• dowolna

\


### Typy Działań

Definiuje konkretne działania do podjęcia, gdy wykryta zostanie rozbieżność:

\
• linia paragonu

• linia kosztów

• opłata nagłówka

• opłata linii

• linia podatkowa

• linia paragonu noty debetowej

• linia kosztów noty debetowej

• opłata nagłówka noty debetowej

• opłata linii noty debetowej

• linia paragonu noty kredytowej

• linia kosztów noty kredytowej

• opłata nagłówka noty kredytowej

• opłata linii noty kredytowej

• linia podatkowa noty kredytowej

\


### Przykłady Reguł

#### [Przypadek 1, 2, 3: Ilość i Cena Jednostkowa w Tolerancji](transactionconfig-pro-template/case-1-2-3-quantity-and-unit-price-within-tolerance.md)

\
• Cel: Obsługuje scenariusze, w których zarówno ilość, jak i cena jednostkowa na fakturze mieszczą się w akceptowalnych granicach tolerancji w porównaniu do PO.

• Działanie: System akceptuje wartości faktury i oblicza całkową kwotę.



#### [Przypadek 4, 5: Ilość w Tolerancji, Cena Jednostkowa Poza Tolerancją (Zatwierdzona)](./#case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved)

• Cel: Stosuje się, gdy ilość jest w tolerancji, ale cena jednostkowa jest poza tolerancją i została zatwierdzona.

• Działanie: System dostosowuje cenę jednostkową, aby odpowiadała PO, i stosuje wszelkie niezbędne opłaty linii.

\


#### [Przypadek 6: Ilość w Tolerancji, Cena Jednostkowa Poza Negatywną Tolerancją (Odrzucona)](transactionconfig-pro-template/case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md)&#x20;

• Cel: Zajmuje się przypadkami, w których cena jednostkowa jest niższa niż oczekiwana i poza zakresem tolerancji, co prowadzi do odrzucenia.

• Działanie: System dostosowuje cenę jednostkową, aby odpowiadała PO, generuje notę kredytową na różnicę i stosuje opłaty nagłówka w razie potrzeby.



### Obsługa Opłat i Podatków

### Opłata na Jednostkę w Tolerancji

• Zasady w tej kategorii zajmują się rozbieżnościami w opłatach na jednostkę, z konkretnymi działaniami w zależności od tego, czy opłata mieści się w tolerancji, czy jest poza nią oraz czy jest zatwierdzona, czy odrzucona.

### Korekty Linii Podatkowych

• Te zasady zarządzają rozbieżnościami podatkowymi poprzez dostosowywanie linii podatkowych lub generowanie odpowiadających not kredytowych lub debetowych na podstawie różnic między danymi podatkowymi faktury a PO.

### Enums i Opcje

• Enums: Zdefiniowane z góry listy wartości zapewniające spójność w ramach zasad (np. operatory porównania, typy zatwierdzenia).

• Opcje: Zdefiniowane z góry wybory dotyczące obsługi ilości lub cen jednostkowych, oferujące elastyczność w definicjach zasad.

## Wyjaśnienie Zrzutów Ekranu

### Zrzut Ekranu 1: Interfejs Zarządzania Regułami

<figure><img src="../../../../.gitbook/assets/docbits_rule_manager_interface.png" alt="Docbits Rule Manager Interface"><figcaption></figcaption></figure>

Ten zrzut ekranu pokazuje interfejs Zarządzania Regułami, w którym administratorzy mogą przeglądać i zarządzać wszystkimi zasadami rozwiązywania konfliktów. Kluczowe elementy to:

• Przycisk Dodaj Regułę: Umożliwia dodawanie nowych zasad.

• Lista Reguł: Wyświetla wszystkie aktywne zasady z szczegółami, takimi jak nazwa, sekcja i status aktywności.

• Menu rozwijane Sekcji: Filtruje zasady na podstawie sekcji, do których się odnoszą (np. Pozycje Paragonu, Opłaty Linii).

### Zrzut Ekranu 2: Szczegółowa Edycja Reguły

<figure><img src="../../../../.gitbook/assets/docbits_rule_editing_detail.png" alt="Docbits Rule Editing Detail"><figcaption></figcaption></figure>

Ten zrzut ekranu ilustruje szczegółowy widok konkretnej edytowanej zasady. Kluczowe elementy to:

• Sekcja Kryteriów: Definiuje warunki, na podstawie których zasada jest uruchamiana. Na przykład kryteria mogą określać, że jeśli ilość i cena jednostkowa różnią się od PO, ale mieszczą się w tolerancji, zasada powinna być zastosowana.

• Sekcja Działań: Określa, jakie działania powinny być podjęte, gdy kryteria są spełnione. Może to obejmować dostosowanie pozycji faktury, generowanie not kredytowych lub debetowych lub stosowanie dodatkowych opłat.

• Typ Dokumentu i Elementy Kosztowe: Umożliwia administratorowi mapowanie konkretnych działań do typów dokumentów i elementów kosztowych, zapewniając elastyczność w obsłudze różnych scenariuszy.