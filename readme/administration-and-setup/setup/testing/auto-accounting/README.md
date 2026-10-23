# Automatyczne księgowanie

Po skonfigurowaniu automatycznego rozliczania dla środowiska DocBits bardzo ważne jest przetestowanie wszystkich funkcjonalności w celu zapewnienia płynnego procesu przekazania.

## Jak włączyć automatyczne księgowanie

* Z Panelu przejdź do Ustawienia → Przetwarzanie dokumentów → Moduł.
* W zakładce Zamówienie zakupu / Automatyczne księgowanie znajdziesz suwak umożliwiający włączenie tej funkcji, a także rozwijane pole umożliwiające wybranie LN lub M3

&#x20;![Strona modułu Settings z przełącznikiem Auto accounting i opcją Auto Export if PO matched na karcie Purchase Order Auto Accounting](https://lh7-us.googleusercontent.com/c3aUKad-\_Wl1-wdhTGAweIe4LGsYZx5Bor8FDKAhALTm8UeO544o7w3VwDBYFSCgzzq37Jce5yKbRaQytI0nz95Ja73rLEAZHIuoTk0V7tn6q7F6Efx6pPlHll1Ek1ZItnmcnGUtgm3Y0GA8pbbshYU)

## Otwieranie automatycznego księgowania

Po przesłaniu dokumentu i wejściu na ekran weryfikacji wybierz następującą ikonę, aby przejść do automatycznego rozliczania.

![Panel szczegółów faktury na ekranie walidacji dla FELLOWPRO AG z polem Rechnung Nr i danymi płatności](https://lh7-us.googleusercontent.com/y-GgwfK7QdmuvVLGxaLhzgA-AhUNHaWfEin8iEdOFCJQE9brJzoXdIIa6B\_E0B2fXR9ahQ7ukllz\_rmI72P4Sujv0cWjEns-u0ro2EqthuwHGN8XVVnaP9or\_c3XzTQ46ZUKf84LMxvl\_yOc5BBE3qc)

Następnie zostaniesz przeniesiony do tego ekranu. Będzie to miało miejsce tylko wtedy, gdy tabela została odpowiednio przeszkolona w celu prawidłowego rozróżnienia różnych elementów zamówienia.

![Ekran walidacji faktury FELLOWPRO pokazujący, gdzie otworzyć widok auto accounting](https://lh7-us.googleusercontent.com/1z8qvnZJoqk2bhjah6HJ7E9Z\_Dhrmi6kTZuXAKSmXT7T-pWnI176DQbliroCPvCEIIhYYnezL5ae\_Az\_O2MWTeOTC6qZvtJ5rlThPYnKnDTIHoDIi6zsahnUuvsD7YtZROXZ4U44L2aWufBsE7QqbiA)

Stąd masz dwie możliwości:

* Podziel fakturę na kwotę całkowitą
* Podziel fakturę na każdą pojedynczą pozycję

Wyboru dokonuje się poprzez kliknięcie preferowanej opcji

![Ekran podziału faktury z wybraną opcją Split by total oraz sumami Recorded bookings i Unsettled amount poniżej](https://lh7-us.googleusercontent.com/Mbusr1kisZSjyU\_YJJ-8sLfwcyBOutRPUymIuuiynvEjjD1-iY\_3kACHdf9g3VcfYtHS6\_eMSFX-3RuA2Wyhq3JDjw7VsuxOijT2q9ey6DWrLzBAK7wPFXUiyapbSEK97E2Rpbop42ZAvW4zJkD-Rz4)

## Wymagania wstępne

Aby funkcja automatycznego rozliczania mogła działać, należy skonfigurować określone dane i informacje. Aby pomóc w tym procesie lub poinformować Cię, jakiej konfiguracji brakuje, utworzyliśmy przycisk “Validate Setup”, który jest umiejscowiony jak pokazano poniżej.

![Ekran Auto accounting z sumami Recorded bookings dla faktury FELLOWPRO](https://lh7-us.googleusercontent.com/zCqiu\_\_deFqdYih9yBGQhxbgXYuBvLFhSd48k-gA9sQoxoBibeyUAEc9k9HQCnmuddIU2Bws7IfK3JCuXylCo6sCdyuUNOeUHRLGGH3Jvz5MJRJU5cmsyzrH5lTo0eH\_ygFTuXc9dI3BZ\_wW-ybzHKw)

Po naciśnięciu DocBits sprawdzi Twoje środowisko, aby sprawdzić, czy wszystko jest poprawnie skonfigurowane.

Pojawi się menu, które będzie wyglądać następująco

![Wyniki konfiguracji Validate z listą kontroli chart of accounts, dimensions i dimensions options wraz z wymaganymi kolumnami](https://lh7-us.googleusercontent.com/v2UhbvTVO7pw29xeRb1kjWlVq8xPmYQNeoXpUZpztcvuWdpFR01u46yRaS3rKeTIhr9k0wor46wwUcoOaOwoP49CGW5VlsLI6fd15DvfnykRC9lFJkY8RN\_Y6DlHP7t4ldPROsdCqIjgg7e3dIK5J9s)

Wszystkie elementy oznaczone zielonym znacznikiem wyboru przed nimi oznaczają, że są skonfigurowane i działają. Powyższy obraz powinien służyć jedynie jako przykład i nie należy go śledzić element po elemencie dla danego środowiska. Dzieje się tak dlatego, że każdy użytkownik ma własny zestaw kont, wymiarów i opcji wymiarów, jak opisano powyżej.

Splitting Amounts

Odbywa się to poprzez kliknięcie poniższej ikony obok kwoty całkowitej lub konkretnej pozycji zamówienia

![Elementy konfiguracji Auto accounting z zielonymi znacznikami wyboru, wierszami Position, Accounts i Amount oraz sumą Recorded bookings](https://lh7-us.googleusercontent.com/SzOTCQ8pox0UPXhlCeSLuqzeD\_gOfmFBkxzmae4Ms2JYLU\_GeQPgd5iITPiedpV12bNozVTFI8Z3cRtacEogkb5OU5OAiKJ4HV7li2HqDsZjYzES8WcCpPDWlYPjRrPfBo5LCGaxtd8uerJqUbmMQcg)

Po wybraniu ikony podziału pod wybranym elementem pojawi się nowe menu

![Menu Split amounts z kolumnami Position, Accounts i Amount oraz wierszami Total i Unsettled amount](https://lh7-us.googleusercontent.com/NMyfsDFrPh7NwQNXF1FHP-oHDkBTUqoniwq48Pri7ULHiZRHuYVJ\_RTiSqt12LG1Q7ut9UTmmlQC0-y2Le5cMJ-c\_OwpWJ7s09r3kHS8I2wca75EiKfa4u2uBkYudgJ-gkEC7yK8OtweSyuqOZ2hh2Y)

Accounts

Pierwszy blok nowego menu daje Ci dostęp do rozwijanej listy, gdzie możesz wybrać konto/dział ze wstępnie skonfigurowanych rachunków/działów, pomiędzy które chcesz podzielić kwotę. DocBits grupuje podobne typy kont, ułatwiając znalezienie określonych typów kont lub kont ze sobą powiązanych.

Amounts

Drugi blok umożliwia ręczne wpisanie odpowiednich kwot, na jakie zostanie podzielona kwota nadrzędna.

Percentage Split

Trzeci i ostatni blok umożliwia ręczne wprowadzenie podziału procentowego, na jaki chcesz podzielić kwotę nadrzędną. Kwota jest automatycznie ustawiana na 50% po wejściu do menu podziału, ale można ją zmienić zgodnie z własnymi preferencjami. Jeżeli w bloku wpiszesz wartość procentową, kwota zostanie automatycznie przeliczona w drugim bloku.

Nowa kwota zostanie obliczona dopiero po naciśnięciu klawisza Enter. Ta zmiana nie aktualizuje pozostałych wartości procentowych, więc suma kwot częściowych może różnić się od kwoty nadrzędnej. Licznik kwoty pozostałej do przypisania („Unsettled amount”) w tym menu pokazuje tę różnicę i został opisany poniżej.

Other Features

Add Row

Ikona plusa obok ikony podziału, można jej użyć w sytuacjach, gdy kwota wymaga podziału pomiędzy więcej niż dwa konta/działy.

![Tabela podziału kwot z pozycjami Position, Accounts i Amount oraz licznikami Recorded bookings i Unsettled amount](https://lh7-us.googleusercontent.com/AzrPkawLROoACG3XpIpXXyRgVXa8giIkgOZ8sYc4LAHwuZRqmoiFas-oYUbR04vtPWiTPAwV\_tu-idfLG57VfaC9fvQl3Zpjdm-tNxVW7YK6-Kf-UeuYpkIenmJbQhdWfg71UezLIIG5\_4bhoSRZdtk)

Delete Row

Ikona kosza używana do usuwania niechcianych lub nieprawidłowych wierszy

![Tabela podziału z dwoma dodanymi wierszami po 50 procent oraz sumami Recorded bookings i Unsettled amount](https://lh7-us.googleusercontent.com/2gAuz4KkU3xQuYZ-6w5p8T43JTJu\_aUdYfWHGBpQc\_LNPXjNu7BgN3maRgfqCzSsWyZ27j8BNn7PNzA2Tj6ZZx5T5rcJjmaFlPQZ5ioXRMoB8zSbGDawsopPoxlX2yZU\_-rh-\_D02iuzCjWDYOCJ7KE)

Unsettled Amount

Wskaźnik “Unsettled amount” na dole w przypadku jakiejkolwiek niezaliczonej wartości lub kwoty pozostającej do spłaty z kwoty nadrzędnej.

![Tabela podziału księgowań z kolumnami Position, Accounts i Amount oraz wskaźnikiem Unsettled amount poniżej](https://lh7-us.googleusercontent.com/xZ2RqteuST79CFiKJRBDLwIBBLMa2E\_vdaMmpTM3NN2qxuwCr8j208wZVHgY1Q9bg46EhRPeQpM\_K1V85yIzU88D7tGRPiP3pkpzXUBv\_vZbPrIM1S41ZeRcMMVW60nf5Whngnpbluw9M30bjDwcoQ0)
