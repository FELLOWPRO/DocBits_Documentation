# Jak działa wyszukiwanie w dokumentacji

Settings Assistant szuka odpowiednich informacji na publicznych stronach w [docs.docbits.com](https://docs.docbits.com). Wyniki mogą zawierać tytuł strony, krótki fragment i link do strony źródłowej. Otwórz link, gdy potrzebujesz pełnych instrukcji lub zrzutu ekranu.

## Znajdowanie właściwej strony

Wyszukiwanie łączy dopasowanie słów z dopasowaniem znaczeniowym. Pomaga to, gdy Twoje pytanie używa innych słów niż tytuł strony. Asystent może też użyć strony ustawień, którą przeglądasz, aby odpowiedź była trafniejsza.

Jeśli wyszukiwanie znaczeniowe jest chwilowo niedostępne, wyszukiwanie w dokumentacji nadal może korzystać z dopasowania słów. Najlepszym sposobem ponowienia próby jest konkretne pytanie z nazwą ustawienia.

## Języki

Wyszukiwanie w dokumentacji korzysta obecnie z indeksów stron pomocy w **języku angielskim** i **niemieckim**. Jeśli interfejs DocBits używa innego języka, asystent korzysta z wyników dokumentacji w języku angielskim. Połączona strona wyświetla własny język; sprawdź go przed wykonaniem kroków lub porównaniem zrzutów ekranu.

## Kiedy zmiany stają się wyszukiwalne

Indeks wyszukiwania jest odświeżany, gdy zmiany w dokumentacji angielskiej lub niemieckiej zostaną opublikowane z repozytorium dokumentacji. Regularne uzgadnianie usuwa też linki do stron, których nie ma już w nawigacji dokumentacji. Nowo opublikowana strona może potrzebować chwili, aby pojawić się w asystencie.

### Przegląd techniczny dla administratorów

Opublikowane strony pomocy są dzielone na sekcje i przechowywane w osobnym **OpenSearch documentation index** dla każdego obsługiwanego języka. Ten indeks jest oddzielony od indeksów używanych dla dokumentów przesłanych przez organizację. Gdy strona się zmienia, niezmienione sekcje można pominąć, a zmienione sekcje są indeksowane ponownie. Usunięte strony są usuwane z indeksu dokumentacji.

Dla pytania usługa łączy dopasowania słów kluczowych z podobieństwem wektorowym, a następnie porządkuje najbardziej odpowiednie fragmenty. Jeśli usługa embeddings jest niedostępna, wyszukiwanie po słowach kluczowych pozostaje dostępne. Settings Assistant otrzymuje linki źródłowe i krótkie fragmenty z tego wyszukiwania w dokumentacji; nie czyta indeksu dokumentów organizacji w tym celu.

Jeśli nie możesz znaleźć strony, wyszukaj bezpośrednio na [docs.docbits.com](https://docs.docbits.com), spróbuj bardziej precyzyjnego pytania lub skontaktuj się z pomocą techniczną DocBits.

{% hint style="info" %}
To wyszukiwanie obejmuje strony pomocy DocBits. Funkcja [Fulltext Search](../document-processing/module/fulltext-search.md) przeszukuje dokumenty Twojej organizacji i ma własne ustawienia.
{% endhint %}

Wróć do [korzystania z Settings Assistant](README.md).
