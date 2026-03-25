# Wykrywanie Podobnych Dokumentow (Wyszukiwanie Wektorowe)

{% hint style="info" %}
**Dostepne od wersji 11.48.0** — Wymaga licencji `OPENSEARCH_ENABLED`.
{% endhint %}

## Co robi ten skrypt?

Wykorzystuje wyszukiwanie podobienstwa oparte na wektorach do znajdowania dokumentow semantycznie podobnych do biezacego. Jesli zostanie znaleziony dokument z wiecej niz 95% podobienstwa, numer faktury jest oznaczany jako potencjalnie oszukancy lub zduplikowany.

## Wyzwalacz

`AFTER_FORMATTING` na typie dokumentu **INVOICE**

## Pelny Skrypt

```python
doc_id = document_json["doc_id"]
similar = vector_search(org_id, doc_id, k=5)

for doc in similar:
    if doc["similarity_percent"] > 95:
        set_field_as_invalid(
            document_data, "invoice_id",
            f"95%+ similar to: {doc['name']} (Score: {doc['similarity_percent']}%)"
        )
        break
```

## Wyjasnienie Krok po Kroku

1. **Pobierz ID biezacego dokumentu** z `document_json`
2. **Znajdz podobne dokumenty** za pomoca `vector_search()` zwracajac 5 najblizszych sasiadow
3. **Sprawdz prog podobienstwa**: Jesli jakis dokument przekracza 95% podobienstwa, jest oznaczany
4. **Oznacz jako nieprawidlowy** z nazwa podobnego dokumentu i wynikiem podobienstwa

## Jak Dziala Wyszukiwanie Wektorowe

Tekst OCR kazdego dokumentu jest konwertowany na osadzenie wektorowe 384-wymiarowe podczas indeksowania. `vector_search()` znajduje najblizszych sasiadow w tej przestrzeni wektorowej za pomoca k-NN (k-Nearest Neighbors), zwracajac dokumenty, ktorych tresc jest semantycznie podobna — nawet jesli dokladne slowa sa rozne.

**Zastosowania:**
- Wykrywanie oszustw (niemal identyczne faktury od roznych "dostawcow")
- Wykrywanie duplikatow wykraczajace poza dokladne dopasowanie tekstu
- Znajdowanie powiazanych dokumentow w roznych formatach lub jezykach

## Uzyte Funkcje

- [vector\_search()](../fulltext-search-functions.md#vector\_search) — Znajdz semantycznie podobne dokumenty
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Pokaz blad walidacji
