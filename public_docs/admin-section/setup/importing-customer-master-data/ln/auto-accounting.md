# Automatyczne księgowanie

## **Wymagania wstępne**

* Sprawny przepływ danych z LN do DocBits
* Poprawnie skonfigurowane środowisko DocBits

## **Konfiguracja Infor**

### **ION Desk**

W Inforze otwórz aplikację ION Desk. W lewym panelu przejdź do Connect → Connection Points

![](https://lh7-us.googleusercontent.com/tOzuXMmjVxByy-GQHBnNbFgP15YKIR0GNGoqrcqz87S3_qBeZCvk92FA4PtD6UjLtUGBBKfmMd-W087C6TnORp7qptWzpDIEp4R2BbivWjQAsmStpZ4RcMgCY7s2CIV0AHErRtQDO2ePlMbNJSoIrmg)

To jest miejsce, w którym utworzysz dwa punkty połączenia potrzebne do importu danych z LN wymaganych do automatycznego księgowania.

Kliknij „+DODAJ”, aby utworzyć nowy punkt połączenia, wybierz opcję API jak poniżej

![](https://lh7-us.googleusercontent.com/C8l4LJ2WHIoPU7E_uFhNIo8XakbizRx874hyTdJH9oHIW-PGd5tOhsnc1uJ6TW6P9BUQqmjoMrHL5WwQJ8IUJqufsbPFIdamKR9cF0EnnPOZD-TlJEQQAmcHKzoKrumCDQAexYZOQ1CpN1p_bAnLNzI)

Należy skonfigurować dwa oddzielne punkty połączenia API, mianowicie:

* Plan kont
* Ostateczne wymiary elastyczne

#### **Plan kont**

Zakładka połączenia dla punktu połączenia Plan kont powinna wyglądać podobnie jak na poniższym rysunku. Nadaj punktowi połączenia odpowiednią nazwę i opis, a także zaimportuj konto usługi, które utworzyłeś.

![](https://lh7-us.googleusercontent.com/gJ1VStvYQ8cu1HBua2iA1Axo1M_lXTS0VGYuqqtSDx-mtu-4xQQBjasNsGyiNSgjuYYQ0yYQkJN79_HJcFF0vTyY4wLZWYIJQHC2oCColX43Va-g-E-KeCRyRQiV6eRDm932eFu6ic7g8OttWULPNUE)

![](https://lh7-us.googleusercontent.com/6zmLNSm7pLiS8dA9VceJv5pxwGpTE8WWZ1nmOt-UJA9qvW0wytcRZXB21jW2xa1BABB1YNNS5uWlxVWgEp4bWU5Rw4li3_qr9potqxxXTY99V0VQQrp3kz4YyFE4jmibHYAEusc1qRtb8E-x9ilbR8c)

W tej sekcji należy dodać dwa BOD-y dla tego punktu połączenia. Są to Sync.ChartOfAccounts i Sync.CodeDefinition, aby dodać te BOD-y, wykonaj następujące czynności:

**Sync.ChartOfAccounts**

* Kliknij ikonę PLUS (+)

![](https://lh7-us.googleusercontent.com/aWwQaVreFHJsv5jd8-ZrVt-FAMvt00aO9W3n1KZ2XmUyxtaCGkg6yS6adPOwXJrqRGdFGTDpG4QsXXJG9V6IJeCrWKsKh6SRjl7ZOacLy9-i5K3dA5mWs6Ps6a91K2TNvdUx98OPwEDWWadz3BwaPiQ)

* Wybierz „Wyślij do API”

![](https://lh7-us.googleusercontent.com/uT-PjpDfv7MGB7wwvkYu0M9muSRXtAqMSjk3LKz3xWdtduWHr_HT1m4ZoETyhP782zOaWBbnEiWxTC9PphoiqogrUNsM5e8PuYutjcwJPqQKAqAlXQMWHOpYru0b7nabzmt_WqgxEp2Naz2hXViNWzY)

* Wyszukaj BOD Sync.ChartOfAccounts

![](https://lh7-us.googleusercontent.com/yQQ92Nn3koBsPG32cPv2Pv9sjdmScGE0WGJ062YSg9q9RDyHnIg-qbh1RA6i7yhfKBeBhgbYEi3uJmR_z6AdnR9pL49M41hvDoqzvijuPhGm3ZltHExmRtfXdccFc7Ogb44_Y4gA8VDBXwt5lJsYEW0)

![](https://lh7-us.googleusercontent.com/WcK_a7Lb61R-5fKGGqzVyR3lAAyyg9jgYunJYC8VNHCsU3Qopvz_d7EJwXo6RZsbcEos05hv_sILd-b29Ky4QVz9lNtzvoicT6bBykPKe-WIPPS-OtZ7yXg8VK6MHa5ZzNdqXvR1CUZmnR4WCu3MpSs)

* Przełącz się na zakładkę ION API, skopiuj nazwę API i wyszukaj wywołanie API, naciskając przycisk WYBIERZ

![](https://lh7-us.googleusercontent.com/364Jd0-EBMpWgpgPZukqcjdRlEoGfkgKkB_U-Y2d87DlB13_E-ovjnBaeRdPCi4rAMm6Ksc_MRHAm75y1BPY21HQ12Fjdr6Q0j1YDTBI0Fo5l3LiIHSwL3ITsKbQ-VIBc5aO6O_DAEKl1z8AUr8xhfo)

* W polu Produkt wybierz punkt końcowy API, który utworzyłeś dla środowiska, z którym pracujesz, które utworzyłeś w ION API. Wyszukaj następujące wywołanie API, wybierz wywołanie API i naciśnij OK.

![](https://lh7-us.googleusercontent.com/NWfGZk5ttI0tWMli1DRZ4SdzC9xHa0LhGR1QbgaeJN1726FYoiqMg1Cb5_x0TvYu4MlTyJqS9n6c6EfW2veKhcUdvpY-bkK_uyfRJt6vESmRsVuIx93ipwuffd3YJr3y2sYX5fjFxjRNWEWzH9ojlr8)

* Następnie przejdź do zakładki Ciało żądania

![](https://lh7-us.googleusercontent.com/BNwExG0mPZ_enovlnQh_SWATS4wDEcOCXuyX98EJza80OxKvrhcFUZ_l4v88XVBBI-iIjg6eprynpO-zjjNeNsCpgulcUCG8OpGA1SzC-1h_OyPHTfHlF_ZsWkpUhT5hz39ruI-TNPo4lelSsvz4jrc)

* Tutaj skonfigurujesz mapowanie pól dla tego BOD, Twoja konfiguracja powinna wyglądać jak poniżej. Mapowania pól są dostępne pod adresem https://docbits.com/doc/field-mappings/.

![](https://lh7-us.googleusercontent.com/0O76spiOI_ZofZiDYRtzuphCzPycktfvxzeEa9MTG3fxeI3bQPjREIyh2sVEwzyGthFzlwdHo1OPifIVpcSMS9yv2WjfIfacCdUQwgvCQu-dXf6aZutRYmrMSCoTFv4mCYtndtLL0-N8NjrlR6oIy-A)

Po wykonaniu powyższych kroków pomyślnie skonfigurowano BOD Sync.ChartOfAccounts. Kliknij ikonę PLUS, aby dodać kolejny i ostatni BOD.

**Sync.CodeDefinition (TotalFlexDimensions)**

Zakładka połączenia dla punktu połączenia CodeDefinition powinna wyglądać podobnie jak na poniższym rysunku. Nadaj punktowi połączenia odpowiednią nazwę i opis, a także zaimportuj konto usługi, które utworzyłeś.

* Wybierz „Wyślij do API”
* Wyszukaj BOD Sync.CodeDefinition

* Przełącz się na kartę ION API, skopiuj nazwę interfejsu API i wyszukaj wywołanie interfejsu API, naciskając przycisk WYBIERZ

* Następnie przełącz się na kartę Ciało żądania

* Tutaj skonfigurujesz mapowanie pól dla tego BOD, Twoja konfiguracja powinna wyglądać jak poniżej. Mapowania pól są dostępne pod adresem https://docbits.com/doc/field-mappings/.

Po wykonaniu powyższych kroków pomyślnie skonfigurowano BOD Sync.CodeDefinition dla tabeli danych głównych TotalFlexDimensions.

#### **FinalFlexDimensions**

Karta połączenia dla punktu końcowego FinalFlexDimensions powinna wyglądać podobnie jak przedstawiono poniżej. Nadaj punktowi połączenia odpowiednią nazwę i opis, a także zaimportuj konto usługi, które utworzyłeś.

Należy dodać jeden BOD w tej sekcji dla tego punktu połączenia. Jest to Sync.CodeDefinition, aby dodać ten BOD, wykonaj następujące czynności:

Karta połączenia dla punktu końcowego CodeDefinition powinna wyglądać podobnie jak przedstawiono poniżej. Nadaj punktowi połączenia odpowiednią nazwę i opis, a także zaimportuj konto usługi, które utworzyłeś.

* Wybierz „Wyślij do interfejsu API”

* Wyszukaj BOD Sync.CodeDefinition

* Przełącz się na kartę ION API, skopiuj nazwę interfejsu API i wyszukaj wywołanie interfejsu API, naciskając przycisk WYBIERZ
* Następnie przełącz się na kartę Ciało żądania

![](https://lh7-us.googleusercontent.com/LRDKhs2rq92Zef63nYy9NNK6bapmlPKUX10NSrRGBhvhdXIgBRte4sGunmOBUzymgnWnAv1O\_qV0AKsULSXsGT1kvorG0Pl0vQFW0exV2sqyUXhgiBMthRYTQbB10c6oI4P6Z139A8VqZVeg6c2HkZ4)

* Tutaj skonfigurujesz mapowanie pól dla tego BOD, Twoja konfiguracja powinna wyglądać jak poniżej. Mapowania pól są dostępne na stronie https://docbits.com/doc/field-mappings/.

![](https://lh7-us.googleusercontent.com/bjoXs4ZSra4dgpf2rC8GwA-uB\_Qp6INkdCapR7M03EV7cuqKzeVPWRCq4EHTZVeKpL92sdesL0iuHTHD1Ed5WHpr7Z15XOJMkPBlWgfbapzD4ZjfSre29Ii2SLGOvjs9-85SougBpDGzzTseAcWNVUo)

Po wykonaniu powyższych kroków pomyślnie skonfigurowano BOD Sync.CodeDefinition dla tabeli danych głównych FinalFlexDimensions.

## **Przepływy danych**

Aby skonfigurować dwa oddzielne przepływy danych dla Auto Accounting:

* ChartOfAccounts
* FinalFlexDimensions

### **ChartOfAccounts**

Przegląd tego przepływu danych wygląda jak pokazano poniżej (ilość punktów połączenia interfejsu API DocBits na końcu zależy od ilości różnych środowisk, które konfigurujesz).

![](https://lh7-us.googleusercontent.com/xog1wW9zE0PeVF\_SzaVS5qWxR2UuHKVR9cD4n6hxD9IAm\_jqJJHKGMCvmsF4V4bcVhd\_zaepEBrbK6wTd6kd7eqDL2Apwe799ewGo8TwMVrtRPwJcImuRjvWJxmcBiMvTjla0KgoGXhMD6oCeZFvOcM)

#### **Firma LN**

Konfiguracja tego punktu połączenia zależy od firmy LN, która zawiera dane główne, które chcesz zaimportować do DocBits, Twoja konfiguracja powinna wyglądać podobnie do tego, co pokazano poniżej.

![](https://lh7-us.googleusercontent.com/k28OYp8vkZZcWCKJTiSFZkDE0SlfLgE\_S3o37OhuvNsOR7Tli3xCYzqN3fRTfrlgE9fF9tYkOXCiC7kZeweCGA86wEDEMj0wKRUO7Idba1d8mY-v15uJGpYlkhZEKSlUA83yPvSlp-aRn2e-pYckXyc)

#### **Dokument**

Należy dodać następujące dokumenty do przepływu danych:

* Sync.ChartOfAccounts
* Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/c6Dhk5iR1fJXqjrXsbSMmkIDBl3eaRNoiijw9WMA69HSrXMKqOjMEKtRtqfXbHcy9fQH1etprR2IuZO6xpMBnY6EYuU6cyBCFjHx4yN2KxxRwTqX12TwSsUaF7wFySImLki86BUKRMW-0YKQJfQTWOw)

#### **DocBits (ChartOfAccounts)**

Tutaj dodajesz punkt połączenia interfejsu API ChartOfAccounts, który utworzyłeś wcześniej, konfiguracja powinna wyglądać podobnie do tej

![](https://lh7-us.googleusercontent.com/yyq6JularNBP\_GpUbDLQ-KWu6utcEZefLXcoHboFa6rcmbN1e8QrdLkab9h2QBWuW-V-i7edmqpTWJwtqWg14GKLDnukyLGuljKXue\_XH\_bLmL2dNz5dECDI\_lkg9hO84nFIDyYWYatkzRkxAYyJe6w)

### **FinalFlexDimensions**

Przegląd tego przepływu danych wygląda jak pokazano poniżej (ilość punktów połączenia interfejsu API DocBits na końcu zależy od ilości różnych środowisk, które konfigurujesz).

![](https://lh7-us.googleusercontent.com/MQyQxEHmvG0vX4VXSnpntbXBGQBtC5uvMeNXklp-EETOIMLZNOJqwOlZp9xm\_\_Lj--o3bJETADpxgZkajW0H0xOE2Gvib9OeU3BeV-mj4lpKFqPQ8A4fymQJDjTZNI8fzrOxYqa595I0\_C3b8QkoTb0)

#### **Firma LN**

Konfiguracja tego punktu połączenia zależy od firmy LN, która zawiera dane główne, które chcesz zaimportować do DocBits, Twoja konfiguracja powinna wyglądać podobnie do tego, co pokazano poniżej.

![](https://lh7-us.googleusercontent.com/D25DTQRX3yecDDMmp\_UvmS9b6AWPYue8LdUueurlCTYg0qWw\_SyM0lCx1sn3VSK0m5MOilgmGWJ261YLr1MlTm9G452QyDQXbyN7DXsQpmmINEbVL5g-OIhpYKN14XQk6oEMqwoTgvpLNKS9\_MkU-sk)

![](https://lh7-us.googleusercontent.com/rGMdEdvYixTZ5wmS5ptBiGcxoOT0abpASTeSDzEFH3SSx-G97gSxIniXja2R3erYP4oIxyVezvL7VjqXKcKd5i6caNZHI-1gVIi2jrKfy\_yVFQ5T80n3ZpR1wSiPWCh\_8affNONcGAcuokvN69-Urfg)
#### **Dokument**

![](https://lh7-us.googleusercontent.com/WyltkYqwzyofXZpwm\_x1-SiM5MCbvDoKPQ9AVOT6nyxXnqXqQn4G-uM7BO2hNRJii91EODf5mjIwS85eOfJ\_UyATLAWqbXegd54leKsK\_zNlVWQNm79yoyTb\_Ok3605NEOM\_Hu\_ov-yaboAQ26PpmTk)

Następujący dokument musi zostać dodany do przepływu danych:

* Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/YIvKeqyGUDBZIoi7I6jhTIlUYtsgYEMeKA3h4Xm9KHz5pYWssDuIaq7343RQdEsxMznTNnReWEB2OCqBQGvgzi7HEOVGlX5EqPa2JEO5sC1LpUF-OXvYLO5a7LMbE2h2YY1Bk2rRnNbCjAZqIMuIxGw)

**DocBits (FlexDimensions)**

![](https://lh7-us.googleusercontent.com/zNJteyBB\_TcRKGE7GL3iPPlFaOqbij5ag37NdNW5GcZBz0xMmb9iev8EktCSJDSNkeZPOnCf-5nImxJjn6RIBTg3x8xJrLK-Z0Z48VTXXLPNIO-3NnmDEVVF-9oHteOQWIjCIMhhzKLK7iCL\_jVsfEY)

Tutaj dodajesz punkt połączenia API FinalFlexDimensions, który wcześniej utworzyłeś, konfiguracja powinna wyglądać podobnie do tej

![](https://lh7-us.googleusercontent.com/ymjxWkOzchUu91ovhE1eE58mSRCyrclNKsNoK48gFcSwKRVuc9Zfy7QZzJ83ATXUWJO4sgPpcNEVPyYZX8dr-sJoEfYKez-WtScX\_hnmOfH-2wBcFKrhxy5wwBUSlKP-ayxcMnCiQ6DKrgqYkfL4xQg)

## **Wywoływanie BOD (M3)**

Po zakończeniu wszystkich powyższych czynności, należy przejść do Infor LN i wywołać BOD w celu dostarczenia różnych danych głównych potrzebnych do Auto Accounting w DocBits.

![](https://lh7-us.googleusercontent.com/OG5eKwuynVhgRagfTwylC2hT6lYMKIgn0ogn1RPShzv7gbE2IO4lC8YzKWDmHa6l6waMREGwVLZmhsCOhUWNrp\_7rkkdrVgo5Z8s84V475UO927BPujEwsX8SY7kRsZBt3R0GUWD13hogj0LdgqNotU)

Z powyższego menu, w zakładce menu po lewej stronie, wybierz Common → BOD-Messaging → Publish BODs → Publish Financial Master Data. Z następnego menu znajdziesz BODs FlexDimensions i ChartOfAccounts do opublikowania.

![](https://lh7-us.googleusercontent.com/KWv\_YZ0BuoZrBvnp2MRzXKRRH1pID7V0iwjCkT4xt7NcbHYoZnFS6wnM\_itC3RzNNGJ95565KynkMFuPb-1NjY0zOGjvlINvVQIrJBcm8daOZa3UiDIB0zBPlt5BS5KavsmYcXHWBQZ9NytMg6NJezs)

Wybierz następujące BODs do opublikowania, po prostu zaznaczając każde pole wyboru, nie trzeba dokonywać żadnych innych zmian, ponieważ chcemy opublikować wszystkie te BODs, aby dane główne były kompletne w DocBits.

![](https://lh7-us.googleusercontent.com/cp9CKdRYofwTrRodTNbZDfMmi\_Q23jchyt\_w7hFkGvvoBo89uhSRoKz0uD2cm2M0tLDmrkb6-8qq9z5EfX-ciEmraWqyytxH09jMK8jVVunb8zjK9EkvGhyl07Igoa4sf8hCLvyGnIlHMVjeLzMFrD8)

![](https://lh7-us.googleusercontent.com/cu8PW0WenwC5jBBFa4trAua-d8zYxi60S2syvKHoBoL2Tk9jdQAOQTvUvGZWSR3cpErwDUZ3WHkm4cDCwS1ZhSJyiQltf43\_Re05WddfxQwJ69C3E\_z\_0bMhEwbq3NasV3Q2waKJlfyBk1oIWdVDjps)

Po zaznaczeniu obu powyższych BODs, przejdź do zakładki Opcje

![](https://lh7-us.googleusercontent.com/imBr628dcJJoNBknxVfKjoWindKT\_\_5AzmYDVXIaHF\_n0RWQUSiK07EHH1df0L2xxCOC5z36UQOfsknF4-GwUgZ9tDZcwDosjxChqFft0GGvVo1JAkPpK\_St-GB7NW1RlBgTszID4YQteYiZlFKPuz4)

Po przejściu do menu Opcje, wybierz następujące opcje i wybierz PROCES, aby opublikować BODs.

![](https://lh7-us.googleusercontent.com/3LH3Me8kacFfp1QH0VFMIfzQtWyFt12IgRQzcAcJByoPQtjhxDnQKE3EjNLO349WeW2WINoFwwrpQJIOoSXBBM\_tmIecJLJEyLipUHXel5yRw7H98OdfydXJdZcChaHvnnwc86wihiblnthMobZyu\_s)

Po zakończeniu powyższych czynności, powinieneś zobaczyć trzy oddzielne tabele danych głównych w środowisku DocBits w sekcji Wyszukiwanie danych głównych:

* chartofaccounts
* totalflexdimensions
* finalflexdimensions
