# Smart Search Ranking

Smart Search Ranking umieszcza dokumenty, o które Ci chodzi, na początku wyników wyszukiwania na pulpicie. Wyszukiwanie po słowie kluczowym znajduje każdy dokument, który zawiera Twoje słowo; Smart Search Ranking dodaje jeden krok: AI czyta najlepsze trafienia i ustawia na początku dokumenty, które naprawdę dotyczą Twojego wyszukiwania. Dokładne dopasowania — numery faktur, numery zamówień, nazwy dostawców — zawsze zostają na górze.

## Co się zmienia

| | Kolejność wg słowa kluczowego | Ze Smart Search Ranking |
| --- | --- | --- |
| Które dokumenty są znajdowane | Te same | Te same |
| Kolejność wyników | Według dopasowania słowa kluczowego | Najpierw dokumenty dotyczące Twojego wyszukiwania |
| Dokładne dopasowania (numer faktury, numer zamówienia, dostawca) | Na początku | Na początku |
| Sortowanie po kolumnie, wyszukiwania `ocr:` i po polach | Bez zmian | Bez zmian — zachowują własną kolejność |

## Przykład

Dziewięć faktur testowych zawiera słowo *wkręt*: wkręty do drewna, zestaw wkrętaków, serwis wkrętarki, przegląd automatu wkrętarskiego, segregatory na wkręty, klej do zabezpieczania wkrętów, walizka z asortymentem wkrętów, zabawkowy wkrętak i profesjonalne wkrętaki.

* Wyszukaj **wkręt**. W kolejności według słowa kluczowego pierwszym wynikiem jest zestaw wkrętaków, a faktura za wkręty jest piąta. Ze Smart Search Ranking faktura za wkręty jest pierwsza, potem asortyment wkrętów; zestaw wkrętaków spada na trzecie miejsce.
* Wyszukaj **wkrętak**. W kolejności według słowa kluczowego zestaw wkrętaków jest pierwszy i ze Smart Search Ranking zostaje pierwszy — tym razem właśnie o to chodziło. Profesjonalne wkrętaki przesuwają się na drugie miejsce, a zabawka spada.

## Gdzie to działa

* W [Szybkim wyszukiwaniu](quick-search.md) na pulpicie przy zwykłym tekście (nie w chipach pól `pole:`).
* Zmieniana jest kolejność początku listy wyników; dalej długie listy zachowują kolejność według słowa kluczowego.
* Jeśli usługa rankingu nie odpowie w swoim limicie czasu, wyszukiwanie pokazuje zwykłą kolejność według słowa kluczowego. Nic nie jest ukrywane i żaden wynik nie znika.

## Jak to włączyć

Smart Search Ranking włącza DocBits dla każdej organizacji. Poproś swoją osobę kontaktową w DocBits o włączenie. Działa dla wszystkich użytkowników organizacji w ciągu minuty, bez żadnej zmiany w sposobie wyszukiwania.
