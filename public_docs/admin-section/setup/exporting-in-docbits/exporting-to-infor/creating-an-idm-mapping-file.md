# Tworzenie pliku mapowania IDM

Po uzyskaniu pliku otwórz go w wybranym edytorze plików. W tym przewodniku zostanie użyty VSCode.

## Edytuj plik mapowania

Sprawdź, czy kod typu dokumentu jest taki sam jak w DocBits (np. w przypadku pliku mapowania BOD powinien pasować do nazwy typu dokumentu w adresie URL ustawień pola) oraz sprawdź nazwę typu dokumentu, tak jak powinna być w Menedżerze Dokumentów (IDM) w Infor.

![](https://lh7-us.googleusercontent.com/WHO0vg2W36yVFBq0ay0wBMFVzMfT6pNvHklt0o8N4tqUpM03jXJm2fykuYjyZh0z4wFTO4Eaeh39-D03re3a9utegrdVdsjHBfucmALA3B7YBWd92-9bcYr543G4MWftv0RosvTgFP3J6NNmLZAz5Dc)

**FYI**: Wskazuje, że nazwa typu dokumentu w IDM to M3\_SupplierInvoice, jest to przykład z instancji M3. Może się to zmieniać w zależności od tego, czy używasz LN czy M3, a także od konfiguracji IDM.

Sprawdź identyfikator firmy oraz identyfikator jednostki (SF\_MDS\_EntityType), ta wartość powinna być taka sama jak w pliku mapowania BOD.

Upewnij się, że IndexFieldFromDocBits=IDMAttributeID (sprawdź, czy DocBits po lewej stronie w ustawieniach pola pasuje do IDM po prawej stronie w Typ Dokumentu → Atrybuty).

### Menedżer Dokumentów w Infor

Przejdź do Menedżera Dokumentów i wybierz nazwę bieżącego typu dokumentu, który chcesz wyeksportować, na przykład Faktura Dostawcy.

![](https://lh7-us.googleusercontent.com/EV3uw3R1L6\_RRANB7FRLwtUFMbv\_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk)

Kliknij powyższą ikonę, a następnie kliknij Administracja → Typ Dokumentu, a następnie znajdź potrzebny typ dokumentu na liście.

![](https://lh7-us.googleusercontent.com/ldsuINS9SCUQm3E57s8j\_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8)

Jak pokazano poniżej, zobaczysz nazwę typu dokumentu taką, jak jest w INFOR.

![](https://lh7-us.googleusercontent.com/KSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj\_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW\_dpRfw\_5BXm0WvAnw4HOALmw)

Upewnij się, że taka jest nazwa w pliku mapowania IDM.

## Prześlij plik do DocBits

Gdy plik jest przygotowany, prześlij go do konfiguracji eksportu w DocBits. Jest to dostępne w Ustawienia → Eksport.

![](https://lh7-us.googleusercontent.com/rUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F\_i5mZ42YDnjqZUYKYSJu1Cetc\_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM)
