# Tworzenie pliku mapowania BOD

Pobierz plik mapowania BOD i otwórz go w wybranym edytorze plików, aby go edytować. W tym instruktażu jest używany VSCode.

## Edytowanie pliku mapowania

Zmień firmę na właściwą (SFV\_AccountingEntityID) i w razie potrzeby edytuj lokalizację ID.

![Plik mapowania BOD otwarty w VSCode z SFV_AccountingEntityID i innymi mapowaniami klucz-wartość SyncCaptureDocumentType](https://lh7-us.googleusercontent.com/eJQI1CKlxEkS\_Pwp0VH2hgS220b-q8NSFG5iJKpLOL457qTN3CbUB8IHTw1lRinbB\_kP00UUNgepWNsbh3\_Ko-SExObePjqmxP7ee\_lQnADTtDmxEtRM\_S7AONMbcpjwtnHTakYd1Q06GVm2G0o-UDA)

Sprawdź kod dokumentu, przechodząc do ustawień pola typu dokumentu, który próbujesz wyeksportować (znajdujących się w URL ustawień pola typu dokumentu w DocBits, jak poniżej

![Strona ustawień pól DocBits dla typu dokumentu faktury w przeglądarce z adresem URL pokazującym kod dokumentu](https://lh7-us.googleusercontent.com/AhU3i27qFS7BMCgpNQnmLWAjcIWHXHOlxMKqd2Yob5RQKa8qysQQsSsacr6zao4cnAh3DISPgYu1GnjubIJpgtAdiBR\_0vy3WJZXPY-HeEfVQkWnlRI9UEJWMPQ7DbWYLQhz339BOlbd4KgxU9B\_CPE)

Na koniec edytuj SFV\_LogicalID, który można znaleźć w INFOR ION DESK → Połącz → Punkty połączenia i wybierz DocBits\_Export lub podobny punkt połączenia, a na tej stronie znajdziesz identyfikator logiczny, którego potrzebujesz.

![Strona Connect w ION Desk z listą Connection Points i wybranym DocBits-Prod-Export](https://lh7-us.googleusercontent.com/f50i7pzRuZULJ6shehba0lWIWFBTsPZyip-LQxAYJpYDXK66SlzdGOpdEG-wqLQfqXMgMMhm5SAvj57UOCvF6xf2OMCXtFiEEKr9yiQr4xtv8vbV-NGcLuJwuQ9zHMBBKfTktAp1nSfBJhdPeAu3RWc)

![Strona Connection Point DocBits-Prod-Export w ION Desk z API Client Id i Logical ID infor.ims.docbits-prod-export](https://lh7-us.googleusercontent.com/qyEt4iYRIjOZCCrVbImeK6EdZGun2YrAy8li8u3tulcD8bwzl\_sl1TiEXKqbik-4MxnbV\_MCwltvuA2WAgzzvDpTVd7W52he9QD9IK0qijoz3ZihUYcWJlqlD5kbcsRTj3SfP1CDqcyhoFfBeiE1Xfo)

## Tworzenie identyfikatora logicznego (punkt połączenia)

Jeśli ten punkt połączenia jeszcze nie istnieje, należy go utworzyć.

Najpierw przejdź do ION Desk → Połącz → Punkty połączenia i kliknij przycisk “+ Add”

![Menu Connect w ION Desk z otwartą nawigacją Connection Points, Mappings i File Templates](https://lh7-us.googleusercontent.com/fQPmV8KgffyWhM0i0cQlyh7fyQe37p8uR6C\_pVD5SboEx2emIJX2212GXqk\_KT71DfYMKSjkfYFFTARqgLLxoOPNQFXHxUOo9vMXH2pmDN469VgbQkV-JjRtCevZJsbvS8vbfUtasN83xN25tX6\_S5U)

Następnie wybierz opcję “IMS via API Gateway”

![Lista Connection Points w ION Desk z wyróżnioną opcją IMS via API Gateway wśród dostępnych typów punktów połączenia](https://lh7-us.googleusercontent.com/uPLiiLHp6Z3jPCzYBOzHVuI8sGY5XQuUfv66fZYH0HndSBL7yvzFHh3lJjEMxteJfXsVMhUe3U\_38xZHDRFSn0jeiMZUQBJJLzZ2oaIQAixY7wUPd6D0PJwg7wvC8XBeZxPmjNoiUvP3ImoG\_aOhFmY)

![Okno dialogowe Infor Application Connection Point dla IMS przez API Gateway z sekcjami Authorization i IMS Endpoint](https://lh7-us.googleusercontent.com/VhyMDEuglPfxeX-3cATu6ZFB\_Mz2Y7C-yJ99EvBvrhD8IoVzGd4ksjrWAE0mIPub2PX5\_Zua10ZHQeWI82QbJ8ZgJKN-tVpVrYGvMdfQOj3Uco5efsPT6JYkDyPu\_lkeR9aTGhh5-q2bzZztXuTUixM)

Zostaniesz przeniesiony do powyższego ekranu, gdzie musisz teraz podać niezbędne informacje, nazwa powinna wyglądać mniej więcej tak: “DocBits\_export” lub podobna.

Dla “ION API Client ID” wpisujesz tego samego Klienta ID, którego uzyskałeś wcześniej dla pliku mapowania ION.

Następnie wybierz zakładkę Dokument w menu Tworzenie punktu połączenia i dodaj następujące dokumenty, naciskając znak “+”, przyda się to dopiero później.

![Strona Infor Application Connection Point DocBits-Sandbox-Export z identyfikatorem logicznym infor.ims.docbits-sandbox-export](https://lh7-us.googleusercontent.com/GtHlTliePV-JIDLP9YNGlXELKuWIU2VSlUt4mvWO4q\_XM54MSL9zTmtxPMdeOl24VFtNC0pQ-nbXyHb9PaeMkKvgzpCOo5kLdL3A8Bw54ILniwIdTyfxFhPuzRUGKs2hRi5ioKvfkdsPMgq4x6EHOtM)

Po zapisaniu tego punktu połączenia otrzymasz identyfikator logiczny, jak pokazano poniżej

![Strona tworzenia punktu połączenia (Connection Point) z nazwą DocBits-Sandbox i polem Logical ID Type](https://lh7-us.googleusercontent.com/P7cihsQT2Qcq\_XGL08dTV2jHMUK7YCMQyXsJudkVDXDh73GZ-hS61IoAKSHptPyX4C5e\_xPKP0yZGzpQOwCFw6BppPlzZuFWZ\_VGIrOUmJH2egxaCEXMoVBHBM6lkZeb3gPYWYdMYpuNqFFPC-4Qol0)

Następnie wstaw ten logiczny ID do odpowiedniej sekcji pliku mapowania BOD i zapisz plik.

## Przesyłanie pliku do DocBits

Przeciągnij i upuść plik do konfiguracji eksportu w DocBits. Jest to dostępne w Ustawieniach → Eksportuj.

![Strona Export Settings w DocBits z kolumnami Title, Document Type, Sub-Organizations, Export Method i Actions](https://lh7-us.googleusercontent.com/AqCo7QgC-kaAxbaIJD8MYeKGLBXbwGVJPGx9\_2yfUp3R2MYxJPowVAjnO80uxQ9qMDxNoXy1eY3WH-mEpaeWwatwi91edm\_0lS9Hg93FSAjQGtDAR5y7Ptce-ARfetSiXIBJKiGwujSggVXXHUhG77U)
