# Auto Księgowość

## **Wymagania wstępne**

* Działający przepływ danych M3 do DocBits
* Poprawnie skonfigurowane środowisko DocBits

## **Konfiguracja Infor**

W Inforze otwórz aplikację ION Desk. W lewym panelu przejdź do Połącz → Punkty połączenia

&#x20;

![](https://lh7-us.googleusercontent.com/Gl49rTfnpYQjXjpUNF3SEouZiJ4pPeHVk60d7dyHizfPLT6sn4AoKVQPPvpgg2cD4ts40hDeWQRs3BqmKW-CAco7Dt0oWKF7ukQJUVDBgSUoMNHt\_gRkqLxkF5CC\_CNGpVRzrNs7rfF1msK320\_J02g)

To jest miejsce, w którym utworzysz punkt połączenia potrzebny do importu danych z M3 wymaganych do Auto Księgowości.

Kliknij na „+DODAJ”, aby utworzyć nowy punkt połączenia, wybierz opcję API jak poniżej

![](https://lh7-us.googleusercontent.com/ctE76pck6mGmBVxRIMhHyn0TbSKKsiGjO7rO185fjndTIo7qYyvSZS3neUdV2CWPqBSangpJ4oG\_g946\_KyOwWyJvacZe5htWiQLTZQLzfNHvsHDhmMQmjh7MrGsqKp6sm-XPcGmEwrH2ZMYCd0bUl8)

Będziesz musiał skonfigurować punkt połączenia API o nazwie:

* PlanKont

### **PlanKont**

Zakładka połączenia dla punktu połączenia PlanKont powinna wyglądać podobnie jak na poniższym obrazku. Nadaj punktowi połączenia odpowiednią nazwę i opis, a także zaimportuj Konto Usługi, które utworzyłeś.

![](https://lh7-us.googleusercontent.com/p-jly6\_S96TsCmpFg9oOob0h7Q7NBlTxRKgNCphiy5QfbK\_lrLMAR2miVUQh-fXrCfGdZr17ongp5c9bnK6HuHCVuDArHhYcmKDlAyO52tGcxg-VXBLXZ1ka8yqZ4DWnxFFMxUKkE7jgvCgr7P-nzdU)

![](https://lh7-us.googleusercontent.com/GkX20Q23htKae7OOcGnJ5J6f0L4I69vOU9jYBpY1m9bpDPdtsD584mh\_9IaZF37Ne1OY2uOPgFxYYjwTrBOoZqahpJLlY3n3qmBn0sgzC0eVu91wE0NWBvESBFJmeVTITQoqUTEU56tHEj47-LQmI6E)

Będziesz musiał dodać dwie BOD w tej sekcji dla tego punktu połączenia. Są to Sync.PlanKont i Sync.DefinicjaKodu, aby dodać te BOD, wykonaj następujące czynności:

#### **Sync.PlanKont**

* Kliknij na ikonę PLUS (+)

![](https://lh7-us.googleusercontent.com/hFWg7-4Osuy9Q0uZYqT9yfAPFYsBi7yitHj7BBxQ94vbsDVg-GuCeTBakvV2eQNjqMGwDAF90nO5h-OxFR8HtYEiYcALdBq5Fdj\_Gl-wU8QePGV4Wr3\_78OK22nUY35dfCQhUPQIp\_qkdHN0wr7V-VY)

* Wybierz „Wyślij do API”

![](https://lh7-us.googleusercontent.com/jA97YupOjXJlRFRxduo\_tYO4YYDZoT0mHxWaPWfJGyU4RTNSVNRAIAsR5mzRyLh1iusHl0cBKUxhYj3hQMzacGdN2QGsvPGy1vHeq\_JNhDqxc-SI5HtZh\_Z\_zmaSjyJwmr2337tzYSWfqDl3JGkjBqY)

* Wyszukaj BOD Sync.PlanKont

![](https://lh7-us.googleusercontent.com/hzuwy-VU8xpgQ85NGHAk9u-m-\_Sw4iffT0SNtWTJw9iWHRIsIvGTEYQgJYi7CUoYC7\_Yp2KDtsohRQkNtIgr1VutFbR8mTkT\_5HmJ7ecgW8pcGuZTuwxtPDOlJpWuONq3WPIupRRBxBJPlsYQ9w-bxo)

![](https://lh7-us.googleusercontent.com/6p8nXaRAI0ucRzmyKfYYg3J8MmHXVgHs-KxcItxeZ6wbefK1YdMrYSblHwnXkSiajApB5ds\_EgpJJWYjfbKOjHdsh-H49jG45weOX9v0YBSAqdXmKgoaBcP7A4zDyINMNVt7RWgbQ51WxNTsfBllvQ4)

* Przełącz się na zakładkę ION API, skopiuj nazwę API i wyszukaj Wywołanie API, naciskając przycisk WYBIERZ

![](https://lh7-us.googleusercontent.com/aRXjuD3nkYsFNM2eYkfmHrshU3ycmN5G4OGSFFadbSToy3pHKYWMw6apbyMhJ9o-5xB6UDA4rbdPjZWAdP-OCH8gQFWV5vWXp0rqLxP9DozP4yMS074\_nsHzirJUgBfkBkQ8Ydp\_WjImf2bx3pDnLPE)

* W polu Produkt wybierz Koniec punktu API, który utworzyłeś dla środowiska, z którym pracujesz, utworzony w ION API. Wyszukaj następujące wywołanie API, wybierz wywołanie API i naciśnij OK.

![](https://lh7-us.googleusercontent.com/LQWk7uiEPCxJcohMmIuRrg2p\_wwE\_h5GoEEP3Y2IdpKARppHoGB4Rt1KRM\_2AiXyG0-ieIV7BM51IRN5exKkhG8eLTkKCftm88j2NLc15X50VLu9t1sZZnQ7DsIIvgUsxz7oryzVIkfmifw-m3qkLDY)

* Następnie przełącz się na zakładkę Ciało żądania

![](https://lh7-us.googleusercontent.com/0tnYxKvtW5Fw7yJfW0QBMclidw5kKJB4oi6M932hGO8ROokbMXbyFcjPQq\_LSVe8hv3ZyVVWqjDO4vMMRgPm1L2iXV3pSoiyzrxGLvBTx4kwt5uo6XtHEt25PRVdM6aIddhHDrT7HGzx3JaZ1F02-YI)

* Tutaj skonfigurujesz mapowanie pól dla tego BOD, twoja konfiguracja powinna wyglądać jak poniżej. Mapowania pól są dostępne tutaj.

![](https://lh7-us.googleusercontent.com/3giuZYeQjdZZHAg7W-pcAHB\_69KP8Ukh\_0NhATYBxvrS\_Qy3yH58fQyrp6GKfOzi1xJms5KV-XVNnAWtX6VmIBwdxSVum9JA6-H9W3XIUYKiTEK3IWoKA560a5I2lwmYd0kitdfC4pRkQVULyWp9PpA)

Po wykonaniu powyższych kroków pomyślnie skonfigurowano BOD Sync.PlanKont. Kliknij na ikonę PLUS, aby dodać kolejny i ostatni BOD.
#### **Sync.CodeDefinition**

Karta połączeń dla punktu połączenia CodeDefinition powinna wyglądać podobnie do przedstawionej poniżej. Nadaj punktowi połączenia odpowiednią nazwę i opis, a także zaimportuj konto usługi, które utworzyłeś.

* Wybierz „Wyślij do interfejsu API”

![](https://lh7-us.googleusercontent.com/YLaFsc0K1Lzruo84Np3EdCTF1xsaQOLRypNpgZB7L9keTh1TwPOMnjBxJYnBOj8GrNSG\_URcRGgv\_p70-pjhBed-wvURRW08YtEWjmACMc3CleRPrHia6nihWQwVOUaZ3qHD\_zLy2W\_iMQ0I77cY\_Bs)

* Wyszukaj BOD Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/f3ikl4jh0PBhYmP3r80BrHuGGu9w9MHe-E0VmyXOCmFEkkK92cxgVimwyP8RF0kF2GruVaeDjiYRKuONX5bQ2ZBRmdKFx8Bf9cHvX5q-xYnXNH0a2xnR4eg1ynyWbRRRoY5xn28HJ\_ziRiKcTN43aHQ)

![](https://lh7-us.googleusercontent.com/nXQZ1LLZsrndggHkAmRtMlV7YzFemnjC9CnS4AdUVDits4zNfzlaqKdHnNcLyTtDkQSX3SB8R3fnZhGBPd-By8C364IIYc4vE2VXNXzoa4LfHP6irTiAg\_N\_2BHSYBLzaQyMCN1w5LdFiiqeiiwAXuk)

* Przełącz się na kartę ION API, skopiuj nazwę interfejsu API i wyszukaj wywołanie interfejsu API, naciskając przycisk WYBIERZ

![](https://lh7-us.googleusercontent.com/LbHmVr1PimQkPu-t6VMvNVk9wVXeQBHOu-X4pW-9vGm-dON2buizVGbKekGL7tY1t4OkwQtzhl7uDhq908UxCfDCJaRDEukpk-07pJjLO-ezRUHgblp3REm0qrKF9wOtMkNWJlVVNVhmfzZ0TtUsqQQ)

![](https://lh7-us.googleusercontent.com/K-kDDTSaZiothC4o3JDihhVJFNt0PiBnLK7kF6RcBOX9EpzutfLHGstzvywBBqaEqm4WqOSQSxtvxRPtbVafPlhtf\_YMVkXjhTkvnGwLzwH\_p-YgRCGAu-DzA94MHjqQoAYTSBPgojcGlJs7tBRcpME)

* Następnie przejdź do karty Ciało żądania

![](https://lh7-us.googleusercontent.com/DfT6FtrbW7LbK4b4I6ssYDWOaPgUxkWsuTDpvQGw549tPFxgEU\_gmh3UwXTbyKHZR8SOHXPHDdobEhA91RIMB57ZAVatrZEsad2QW6QHiUkdZoyW\_yE\_iIGDgs2IrY0I6qL1JTZxksYoaLKu0Il8smU)

* Tutaj skonfigurujesz mapowanie pól dla tego BOD, Twoja konfiguracja powinna wyglądać jak poniżej. Mapowania pól są dostępne tutaj.

![](https://lh7-us.googleusercontent.com/nqK7x1Km4wIP9aWnvMlSHl1\_omw22GRKONfB-zc8ikn\_rSsl60Ksml0oQacs8UNmPSLFSKPD7Eo9FsH42RjDo4oragvHZJHFW\_yv62KXDrF3SKnDN2-X6vqYJ5a-3bYkkvPDlNJSxFylvtAFr-2Kt8Y)

Po wykonaniu powyższych kroków pomyślnie skonfigurowano BOD Sync.CodeDefinition dla tabeli danych głównych M3FlexDimensions.

## **Przepływ danych**

Aby skonfigurować następujący przepływ danych dla Auto Accounting:

* ChartOfAccounts

### **ChartOfAccounts**

Przegląd tego przepływu danych wygląda jak pokazano poniżej (ilość punktów połączenia interfejsu API DocBits na końcu zależy od ilości różnych środowisk, które konfigurujesz).

![](https://lh7-us.googleusercontent.com/RfkP8xiF2vDzQhBNa66L0NQHk7TGjj52aK3hWoisEnWbdG3l-SZKKw8mYJ3b28ShXZ9omPS6WdNiXaCpYRQzwfges0SKznwQal7K2ElILbGBJNYu3VFm6gDQJMHYRItAFX0cdRZjXgCk2FQqHJ4iSjY)

### **M3 Company**

![](https://lh7-us.googleusercontent.com/tqYoI-gLUpe0c0x1T-WhP0\_FolVzPGHhFY8m52Fw38mJNzsDvjb7stRrBfWVjXLnFrJTTy2lyd9Dmva3\_EPG5eRWyf5ATA2cTWvCj3Ksa4Fu4pHF6rNFjfd3Cjei0UlibT0HAQYE0V22bdTStjY61zk)

Konfiguracja tego punktu połączenia zależy od firmy M3, która zawiera dane główne, które chcesz zaimportować do DocBits, Twoja konfiguracja powinna wyglądać podobnie do tego, co pokazano poniżej.

![](https://lh7-us.googleusercontent.com/wpSluEs21T5wXG0egZPfUCYBP6X\_uUm6XAh-PyD8RrojTuIztzRJzhVYdzcNI5dQGGDsrhSKx\_K2-y0JDmK9w41fVUXWcW1N2lz5rizXcMnn5BuiaGRy-TEOBryGxvP9mBGJTZ16lMisoC\_YumwpS9Q)

### **Dokumenty**

![](https://lh7-us.googleusercontent.com/uR6XaFI7TPQ4L8Suom25PBdtXdL4i100Juz7kRBxT5rdxhejZW7nPtVIlEGjWWnZLbo9ipx7G95NBFV8dd-g4vw\_vM-uPApJ02QdxvCmX27bwAW\_qUWUXajV6BFVmIfzTQ46Zj4DybsYKKblXjuWc6w)

Następujące dokumenty muszą zostać dodane do przepływu danych:

* Sync.ChartOfAccounts
* Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/6Bq-yQ9Yaf2OJwjBxyFvqAMUitcovquo\_iU4hc-pgag1iDwLcstggVjLsdY3bRl9XWNc3mKOwZrY1FSlu47IzxxUQHFkjIAl1r08Iw9UbKaaMh4WiWrqFuSObdTjEvCEI5IDvD\_Pys8jAydydJgbsK8)
### **Filtr**

![](https://lh7-us.googleusercontent.com/LyKGzQUEswTD1XfpNDPSHjChgqNFfs4guXfM0KNuW2fPoiaeUo4uPrlGgwt3RepWUGQmu\_trUMiWb68cUjUAwXU9IRoWOsv9M2l5v4zFfBkEcioz5ok7Eoss7I-tBKtpD7wVUkGWi3U3ySrIQ\_fDPiY)

Dla drugiej trasy przepływu danych (zgodnie z trasowaniem w przepływie danych) stosujemy filtr z następującą konfiguracją.

![](https://lh7-us.googleusercontent.com/7xdqGdo9bS6\_IIzTVYF\_08woBXvhIVkA-c6-ZrDpDEzmEDFzDZSuxZ5LYHKVUhJqYq4Wlq1FXPfr5myjKFUsMbnJrefc\_L7URD7AbEq\_D90jEw7o8Yrhg5XZwLdU83OwlZVXqlYla61b0LyISXeBLWk)

![](https://lh7-us.googleusercontent.com/OdI-0FaqDaPKy2g9Mr8HUx\_oGRZkDrkeI6P1rWqOounpDauMThaqzs2wOawmw3RwcMlQHgI6wj16RXQDAP\_JNMGkxvmiEnPJ\_bvse2CvMegPwinSIJRLmXaCzfjxtB1FDqnqPOMwrMYNKJyiC2sGUe8)

![](https://lh7-us.googleusercontent.com/RMPIV6ZWsUcBA6klny6Ln-\_nhMGl1zdEHfUKK56owelabcG-6gM1S\_eqWAVLTeOHdec3D5D6xVJeC5evnJC61L8daV6IbJbCmMashkWXSK4Tv4RdE\_erjR-Mk2RihPodIG4HrqSOQ8hi7SG3xctXd-E)

### **DocBits (ChartOfAccounts)**

![](https://lh7-us.googleusercontent.com/Npm92rS\_EO5roSy3tldC88hFIyiDnZjHnnVSkkKyfmNrOcbuVj4LPNrcsWvOT8IHNQKGMqIZymG9q3VMGG6RwvuRBqZgmhHxqXn1oieajDmz8giQxSr8wOFzb8TQTJJWwj912-sDRtkrDAXCr7ne-pk)

Tutaj dodajesz punkt łączenia interfejsu API ChartOfAccounts, który utworzyłeś wcześniej, konfiguracja powinna wyglądać podobnie do tej

![](https://lh7-us.googleusercontent.com/Dw4y6OMuMAYHZjH1etj\_FqdsaFxaRhQyk6\_PaxXrWLhrNirEn7xQc5uIpbDT6Wz85XvZgY02aNuWfbYKBzo6W9aavN\_Asu5ENfr2dszWYQqs9sy6zl4o0NxRe3IPXodLIGf9JkbK2\_UtYe4dVii0JbM)

## **Wywoływanie BOD**

Po zakończeniu powyższych czynności, przejdź do Infor M3 i wywołaj BOD w celu przesłania różnych danych podstawowych potrzebnych do Auto Accounting do DocBits.

Zacznij od naciśnięcia Command + r, aby otworzyć menu poleceń, wpisz "evs006" i naciśnij Enter.

![](https://lh7-us.googleusercontent.com/pzAL0cnM94AUE4KmTyBV8OPU9ft\_g9o0-KB9Ib0AjrvG7Q59GHT-2biP4n7yFyXRxQ0gjy85G6MWMWUeMIWJcTQ9TKwzCEywd7I\_6\_vV-muepobkW0O-4-CZxsmjOEQ7uM1frZpTLqlLS3aSYkEuwAw)

Zostanie wyświetlone następujące menu

![](https://lh7-us.googleusercontent.com/Wx41TNpg1zuaf1rXIBvSCVzSRf6q74rdLs91el21iErqQnDiF4cv7X0nyDaS2Gjimj7xbfAK-7mo6sXN6fkK934mHnCnivFTz9NqHi6dBoMYiRT\_vLrkVUlFd\_T4Oan3Zkq3WKLoI-kmsElHSKO7zY0)

Aby dodać różne BOD, musisz wprowadzić rzeczowniki BOD i nazwy tabel dla każdego BOD osobno.

![](https://lh7-us.googleusercontent.com/5gVWRDm\_8CSyoQRkq-7LuI8MLU1BjRN6Z6YCcVZp7G3Be62nQBht-eUNZreTzV2rFWYK\_RcKiyzwTTlT5y5X8eGf-Z7qDavDyHML0zv6Yt6jGu2z9d-nL0K-m446nDZa2-aiFLnnzjAwk8pTT4RQK6Q)

Należy dodać następujące BOD:

* ChartOfAccounts
* CodeDefinition
* CodeDefinitionAccountingDimension

Aby dodać nowy BOD, po wprowadzeniu rzeczownika BOD i nazwy tabeli, naciśnij ikonę PLUS wskazaną poniżej

![](https://lh7-us.googleusercontent.com/66wclj8g8RAYT9-UIgRMs0qnuA9srmWv21PdqdNm\_q5icGmabL17-DpLOSs4pm6Nj3xJN-9xt7io\_5GZGfzSQ2qt\_8Y--CJFou6FaOdufiuxOdKHrUUYELNdGy9e-gnWg\_hAMSfs\_NJa6zYBMpoyTVs)

Rzeczowniki BOD i nazwy tabel są następujące.

**ChartOfAccounts**

* Rzeczownik BOD: ChartOfAccounts
* Nazwa tabeli: FCHACC

**CodeDefinition**

* Rzeczownik BOD: CodeDefinitionAccountingDimension
* Nazwa tabeli: FCHACC

### **Publikowanie BOD**

Po dodaniu każdego BOD, kliknij prawym przyciskiem myszy dodany BOD, wybierz Powiązane, a następnie Uruchom.

![](https://lh7-us.googleusercontent.com/225-ujyGzG\_RJOXgbx8NOh\_4s-Sn\_o80b\_h0DTsJqfr6OcyPUwkWLF2lfEyzFFFKddKmlWd32bb94qeYlOdVBTI8RL0r6ZfZKloVTrAYLNp-U5gL3aJhW4d72ExkkyM4AydLczsPvdE1cRDfGNKupdA)

Zostaniesz przeniesiony do tego ekranu.

Zmień czasownik BOD na "sync" i naciśnij DALEJ.

![](https://lh7-us.googleusercontent.com/3DyjXUSlAF7msQT1OAO3aCr1U9R68XZj0oE\_yJwsBrBj-FkiZR-oRYQYSClHG0iN0FXFdDdKQA1hOBlw3jc-lXQCWkiDFa0IweuQnoR8k-Mgyp1HeI5ImJqNogz-Q3b3P33ywb0B2o1pZ-TkZ7mAwZA)

Po naciśnięciu DALEJ, otrzymasz powiadomienie o rozpoczęciu procesu publikowania BOD.
### **ElementKosztów**

Aby zaimportować tabelę m3costingelement do DocBits, wykonaj poniższe kroki.

Z głównego menu M3, wpisz Command + r i wyszukaj polecenie "PPS280".

Wybierz dowolną z wyświetlonych linii. W następnym menu wybierz NARZĘDZIA i "Eksport do programu Excel"

![](https://lh7-us.googleusercontent.com/I8SYWm-JwpyYRHFUp2obGtXcsa7m\_blJ\_lTrnhczztRIXIN5gfxCt3eRw6ZI42fH6AwnsKyv4ux5-rhaT505PsyDFFI\_anUNvmACFyx\_ssgxaqWq25vLt\_E5s310HNoiPPLf35qJlYtstjpj5Cc4aB4)

Wybierz "Eksportuj wszystkie wiersze" a następnie kliknij EKSPORTUJ.

![](https://lh7-us.googleusercontent.com/wtjHI9L4YUhf-yJFjcPGu218Vis\_zELtCIfpmkIUKgasfrdfNW-dr\_J1DqXlfD-SBrnVduDrMLAIAQh6UTlzBqEP\_JPXP48elGMyGj0ByZbX7TpqlnIfRZ4ZoD0pyCo-AKigeKjlHN6cFcdpeClZ9L4)

Po pobraniu pliku, będziesz musiał zmodyfikować plik Excel przed przekonwertowaniem go na plik CSV.

Musisz otworzyć plik Excel, który będzie wyglądał podobnie jak poniżej.

![](https://lh7-us.googleusercontent.com/l4WbidK-5zSEQ6rwqhknudPBmmDji0f1WwTh-kHomSkgEOA7s4m72cLw8z-4nflqBvPp\_2AajIEZDZz4dRLs8jlAeYHp4ee2tDysxYy8YBjj4ktHxdUXpxO\_Z34c8\_f0cNMX-9lp0lT5wOZoH1QUCgE)

Z tego arkusza Excel potrzebujesz tylko dwóch pierwszych kolumn, zmodyfikuj arkusz Excel, aby wynik końcowy wyglądał następująco.

![](https://lh7-us.googleusercontent.com/QaNRlKHrU6kZWFqmwYR8C\_\_nLVOeqowAxJlvooSVBIAF5ayx2xZtUppsn0jzBcJVi90vemM3tZMZOjn549N3RzMuWuE3w911WLVS5NMuiUmnfXM\_xUXbqmzBtiQZstnpEYj1dUSbs\_IkAydlhBfdmcc)

Gdy to zrobisz, zapisz plik jako plik CSV.

Po uzyskaniu pliku CSV, przejdź na następującą stronę internetową. To zależy od środowiska, w którym pracujesz:

* Prod: http://api.docbits.com/
* Sandbox: http://sandbox.api.docbits.com/
* Stage: http://stage.api.docbits.com/
* Demo: http://demo.api.docbits.com/
* Dev: http://dev.api.docbits.com/

Tutaj ręcznie załaduj tabelę ElementKosztów za pomocą interfejsu API. Kliknij przycisk Autoryzuj.

![](https://lh7-us.googleusercontent.com/tyzOq3BR2QqTguQFKicxo0dE5j5hGsP-BhfVbS81O\_mxN5bSVp40jYfgsVJcE\_rBLFMDJNvbPkPIdjPqaqoNbHBBM-9hx0i-U4VAH9ISBYhpwKgqQeUEd67VV1E4izwNyxbAwwrhCmrAo1uIKhLherY)

Musisz wstawić klucz API ze swojego środowiska DocBits. Znajdziesz go w Ustawieniach w sekcji Integracja.

![](https://lh7-us.googleusercontent.com/4ADnevq6kq\_vbxUJpyPbHNcGvRvpO-l9Gwd8ZaYf\_vO4uWhSl1jmKNpddmHGc9ZHMMbXCgLOElLDYbNwB3INmBDETecPrDnpI601IUOZQlT7tc7OLSPXwkooOJFNwML2i\_gvBPuE8CvfwRpX-ZIlb\_g)

Po zakończeniu, wyszukaj API o nazwie master\_data\_lookup/import\_data i wypełnij wymagane informacje. Po zakończeniu, kliknij WYKONAJ, aby uruchomić API.

![](https://lh7-us.googleusercontent.com/8UD4FhFv2dRB4cMjCDL4G9ndjH7laVMKWqdeMaJGgEo48-UVvucB1uOydzNdfFy0yPM5bb66mZB4k9uJR7TTiEREGFaV2EqW01gxJpTyuUfGNh5QmBjySkyhZ56gWV8sYs8WI5RnHcENtXgjTU0vg0Q)

Jeśli wszystko zostało wykonane poprawnie, tabela M3CostingElement powinna teraz znajdować się w Twoim środowisku DocBits. Automatyczne rozliczanie dla M3 zostało skonfigurowane dla Twojego środowiska.
