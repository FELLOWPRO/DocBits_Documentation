# Opis struktury EDI

Głównym celem deskryptora struktury jest przedstawienie elementów wiadomości EDI w sposób logiczny i zorganizowany, ułatwiając zarządzanie i analizowanie danych. Poprzez dokładne odzwierciedlenie hierarchii wiadomości.

### Elementy deskryptora struktury

**N1** – Zawiera następujące pola:

* **N1** – Nazwa lub identyfikator podmiotu (np. strona, organizacja).
* **N2** – Dodatkowe informacje o nazwie (zazwyczaj druga nazwa dla podmiotu).
* **N3** – Informacje adresowe (zwykle adres ulicy).
* **N4** – Lokalizacja geograficzna (miasto, stan, kod pocztowy, kraj).

**N9** – Zawiera następujące pole:

* **N9** – Identyfikator odniesienia (np. numer zamówienia zakupu lub numer kontrolny).
* **Pętle:**
  * **MSG01** – Zawiera następujące pole:
    * **MSG01** – Tekst wiadomości w formie swobodnej (zazwyczaj notatka lub specjalna instrukcja związana z transakcją).

**IT1** – Zawiera następujące pola:

* **IT1** – Identyfikator pozycji liniowej (np. numer pozycji lub kod produktu).
* **QTY** – Ilość pozycji w transakcji (np. zamówione lub dostarczone jednostki).
* **TXI** – Informacje podatkowe (np. stawki podatkowe, kwoty lub klasyfikacje dotyczące pozycji).
* **REF** – Informacje odniesienia (np. numer partii, numer seryjny lub inne identyfikatory związane z pozycją).
* **Pętle:**
  * **SAC** – Może się powtarzać i zawiera następujące pola:
    * **SAC** – Informacje o usłudze, promocji, zniżce lub opłacie (np. dodatkowe koszty lub rabaty związane z pozycją).
    * **TXI** – Informacje podatkowe związane z SAC (np. podatki od opłat lub zniżek).

**SAC** – Zawiera następujące pola:

* **SAC** – Informacje o usłudze, promocji, zniżce lub opłacie (może być używane niezależnie lub w obrębie pętli IT1 do reprezentowania dodatkowych opłat/rabatów).
* **TXI** – Informacje podatkowe związane z SAC (np. podatki od opłat lub zniżek).

### Oto pełny przykład deskryptora struktury w formacie JSON:

```
{
    "N1": {
        "fields": [
            "N1",  
            "N2",   
            "N3",   
            "N4"    
        ]
    },
    "N9": {
        "fields": [
            "N9"    
        ],
        "loops": {
            "MSG01": {
                "fields": [
                    "MSG01"   
            }
        }
    },
    "IT1": {
        "fields": [
            "IT1",   
            "QTY",   
            "TXI",   
            "REF"    
        "loops": {
            "SAC": {
                "fields": [
                    "SAC",   
                    "TXI"    
        }
    },
    "SAC": {
        "fields": [
            "SAC",   
            "TXI"    
        ]
    }
}
```
