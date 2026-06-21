# Auto-Accounting

## **Voraussetzungen**

* Funktionierender Datenfluss von LN zu DocBits
* Korrekt konfigurierte DocBits-Umgebung

## **Infor-Konfiguration**

### **ION Desk**

Öffnen Sie in Infor die Anwendung ION Desk. Navigieren Sie im linken Reiter zu Connect → Connection Points

![](https://lh7-us.googleusercontent.com/tOzuXMmjVxByy-GQHBnNbFgP15YKIR0GNGoqrcqz87S3\_qBeZCvk92FA4PtD6UjLtUGBBKfmMd-W087C6TnORp7qptWzpDIEp4R2BbivWjQAsmStpZ4RcMgCY7s2CIV0AHErRtQDO2ePlMbNJSoIrmg)

Hier erstellen Sie die beiden Verbindungspunkte, die zum Importieren Ihrer Daten aus LN erforderlich sind und für Auto-Accounting benötigt werden.

Klicken Sie auf „+ADD", um einen neuen Verbindungspunkt zu erstellen, und wählen Sie die API-Option wie unten dargestellt

![](https://lh7-us.googleusercontent.com/C8l4LJ2WHIoPU7E\_uFhNIo8XakbizRx874hyTdJH9oHIW-PGd5tOhsnc1uJ6TW6P9BUQqmjoMrHL5WwQJ8IUJqufsbPFIdamKR9cF0EnnPOZD-TlJEQQAmcHKzoKrumCDQAexYZOQ1CpN1p\_bAnLNzI)

Sie müssen zwei separate API-Verbindungspunkte konfigurieren, nämlich:

* ChartOfAccounts
* FinalFlexDimensions

#### **ChartOfAccounts**

Der Verbindungsreiter für Ihren ChartOfAccounts-Verbindungspunkt sollte ähnlich aussehen wie unten dargestellt. Geben Sie dem Verbindungspunkt einen passenden Namen und eine Beschreibung und importieren Sie das von Ihnen erstellte Service Account.

![](https://lh7-us.googleusercontent.com/gJ1VStvYQ8cu1HBua2iA1Axo1M\_lXTS0VGYuqqtSDx-mtu-4xQQBjasNsGyiNSgjuYYQ0yYQkJN79\_HJcFF0vTyY4wLZWYIJQHC2oCColX43Va-g-E-KeCRyRQiV6eRDm932eFu6ic7g8OttWULPNUE)

![](https://lh7-us.googleusercontent.com/6zmLNSm7pLiS8dA9VceJv5pxwGpTE8WWZ1nmOt-UJA9qvW0wytcRZXB21jW2xa1BABB1YNNS5uWlxVWgEp4bWU5Rw4li3\_qr9potqxxXTY99V0VQQrp3kz4YyFE4jmibHYAEusc1qRtb8E-x9ilbR8c)

In diesem Bereich müssen Sie für diesen Verbindungspunkt zwei BODs hinzufügen. Dies sind Sync.ChartOfAccounts und Sync.CodeDefinition. Um diese BODs hinzuzufügen, gehen Sie wie folgt vor:

**Sync.ChartOfAccounts**

* Klicken Sie auf das PLUS-Symbol (+)

![](https://lh7-us.googleusercontent.com/aWwQaVreFHJsv5jd8-ZrVt-FAMvt00aO9W3n1KZ2XmUyxtaCGkg6yS6adPOwXJrqRGdFGTDpG4QsXXJG9V6IJeCrWKsKh6SRjl7ZOacLy9-i5K3dA5mWs6Ps6a91K2TNvdUx98OPwEDWWadz3BwaPiQ)

* Wählen Sie „Send to API"

![](https://lh7-us.googleusercontent.com/uT-PjpDfv7MGB7wwvkYu0M9muSRXtAqMSjk3LKz3xWdtduWHr\_HT1m4ZoETyhP782zOaWBbnEiWxTC9PphoiqogrUNsM5e8PuYutjcwJPqQKAqAlXQMWHOpYru0b7nabzmt\_WqgxEp2Naz2hXViNWzY)

* Suchen Sie nach dem BOD Sync.ChartOfAccounts

![](https://lh7-us.googleusercontent.com/yQQ92Nn3koBsPG32cPv2Pv9sjdmScGE0WGJ062YSg9q9RDyHnIg-qbh1RA6i7yhfKBeBhgbYEi3uJmR\_z6AdnR9pL49M41hvDoqzvijuPhGm3ZltHExmRtfXdccFc7Ogb44\_Y4gA8VDBXwt5lJsYEW0)

![](https://lh7-us.googleusercontent.com/WcK\_a7Lb61R-5fKGGqzVyR3lAAyyg9jgYunJYC8VNHCsU3Qopvz\_d7EJwXo6RZsbcEos05hv\_sILd-b29Ky4QVz9lNtzvoicT6bBykPKe-WIPPS-OtZ7yXg8VK6MHa5ZzNdqXvR1CUZmnR4WCu3MpSs)

* Wechseln Sie zum Reiter ION API, kopieren Sie den API-Namen und suchen Sie nach dem API Call, indem Sie die Schaltfläche SELECT drücken

![](https://lh7-us.googleusercontent.com/364Jd0-EBMpWgpgPZukqcjdRlEoGfkgKkB\_U-Y2d87DlB13\_E-ovjnBaeRdPCi4rAMm6Ksc\_MRHAm75y1BPY21HQ12Fjdr6Q0j1YDTBI0Fo5l3LiIHSwL3ITsKbQ-VIBc5aO6O\_DAeKl1z8AUr8xhfo)

* Wählen Sie bei „product" den API-Endpunkt aus, den Sie für die von Ihnen verwendete Umgebung erstellt haben und den Sie in der ION API angelegt haben. Suchen Sie nach dem folgenden API Call, wählen Sie ihn aus und drücken Sie OK.

![](https://lh7-us.googleusercontent.com/NWfGZk5ttI0tWMli1DRZ4SdzC9xHa0LhGR1QbgaeJN1726FYoiqMg1Cb5\_x0TvYu4MlTyJqS9n6c6EfW2veKhcUdvpY-bkK\_uyfRJt6vESmRsVuIx93ipwuffd3YJr3y2sYX5fjFxjRNWEWzH9ojlr8)

* Wechseln Sie als Nächstes zum Reiter Request Body

![](https://lh7-us.googleusercontent.com/BNwExG0mPZ\_enovlnQh\_SWATS4wDEcOCXuyX98EJza80OxKvrhcFUZ\_l4v88XVBBI-iIjg6eprynpO-zjjNeNsCpgulcUCG8OpGA1SzC-1h\_OyPHTfHlF\_ZsWkpUhT5hz39ruI-TNPo4lelSsvz4jrc)

* Hier konfigurieren Sie das Feldmapping für diesen BOD; Ihre Konfiguration sollte wie folgt aussehen. Die Feldmappings sind verfügbar unter https://docbits.com/doc/field-mappings/.

![](https://lh7-us.googleusercontent.com/0O76spiOI\_ZofZiDYRtzuphCzPycktfvxzeEa9MTG3fxeI3bQPjREIyh2sVEwzyGthFzlwdHo1OPifIVpcSMS9yv2WjfIfacCdUQwgvCQu-dXf6aZutRYmrMSCoTFv4mCYtndtLL0-N8NjrlR6oIy-A)

Sobald Sie die oben genannten Schritte abgeschlossen haben, haben Sie den BOD Sync.ChartOfAccounts erfolgreich konfiguriert. Klicken Sie auf das PLUS-Symbol, um den nächsten und letzten BOD hinzuzufügen.

**Sync.CodeDefinition (TotalFlexDimensions)**

Der Verbindungsreiter für Ihren CodeDefinition-Verbindungspunkt sollte ähnlich aussehen wie unten dargestellt. Geben Sie dem Verbindungspunkt einen passenden Namen und eine Beschreibung und importieren Sie das von Ihnen erstellte Service Account.

* Wählen Sie „Send to API"

![](https://lh7-us.googleusercontent.com/h-HCsruFxSb6FVNKRRfLcbeiLnRXrQYDRmVH5cK\_N-PgIVkkA8zY1gd4T0w8Nq9f\_x7AFnR3D\_veVdI6In7DoIRebiFbXfIleXROV2AoAG\_\_C00UnvFapAFvPuGTwYxQfuZpeKk1yXsJE9\_dQ-mX2M4)

* Suchen Sie nach dem BOD Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/WrXZYGIgQMRuWXG8pWHbI-6TQj6VyC9\_Opon05kup2gfDva-JwFShHzusw5sz78cq643hBF5dEJx4ZOqFXjUQm\_oqAB00O3Z\_Xd5Bdf\_4h\_Criq5g-8OeVIz69N6vqNraz\_zCfxZQur-37VT5VzWka0)

![](https://lh7-us.googleusercontent.com/5Mn6YBvca3Ejc9EIemE3UIHZ4sLzDObOr5RF4TsOucRPkFiIX-4ot7FSMb7TsspFsH\_ysbSZ8zB3xgM1zXboK5jBqqTbVDMNbsUEQOrwfzSkHfuhB44m2j9V0LRMalHJNtujOmz4FJd8Ey69VvdJ6EM)

* Wechseln Sie zum Reiter ION API, kopieren Sie den API-Namen und suchen Sie nach dem API Call, indem Sie die Schaltfläche SELECT drücken

![](https://lh7-us.googleusercontent.com/lQNNzs9RNxvf85YGk0pq3-8vuwqXgzkfl-W4a8qcuFdThRTf4r6aJEmo3IXGp0cykwy6cml3AIRWwR3N8GZRbpL8yUynqKPeoTlmJ5CiKeJSmxm7Ea1aU3L8KXecM\_yv2mhDobYA09zaSV8kKAVs70A)

![](https://lh7-us.googleusercontent.com/1bE6Zgval5nkr9xxBGLgL0tk2f5IKN-OYng-9BzrPqX4aGq06emYHtICMgaIlAtXjP9sjQ8KHeL3Pa8gBgGMLFwmiArb9Lh9iX-mZ3X59Oblo7HRfZvD29jrifb0\_pJA4FMtHThpZq\_Vi\_nTeXB1XUQ)

* Wechseln Sie als Nächstes zum Reiter Request Body

![](https://lh7-us.googleusercontent.com/0MVLj442YbPOa83BtT8VwV9WG-Jl3DajGm4MGKwzsdD6QZLwtFhwhghCUX7ShlsbDogDmflsa4C5CmoxNqrFqNh\_ngxQ-rwoNAnWif4tYbwzTdEmAVy7kGRMs8v2VTDaAWsXk5nbRHFoszXeuCp8DGk)

* Hier konfigurieren Sie das Feldmapping für diesen BOD; Ihre Konfiguration sollte wie folgt aussehen. Die Feldmappings sind verfügbar unter https://docbits.com/doc/field-mappings/.

![](https://lh7-us.googleusercontent.com/tmDr3sAIr\_S7tRPebboyt9TPSGEBU4eC0zS04BcsDy4B4yQ3xdv8k-DlBjHXPy0P4slyLKYaRxM9s93Qx6Wf\_fI82St3XcmzsZwxKgRnXWHkzDcKj5oVYdtnW9I3dX8kM1rgxAYuRBIrWKSUhx8JZYk)

Sobald Sie die oben genannten Schritte abgeschlossen haben, haben Sie den BOD Sync.CodeDefinition für die Stammdatentabelle TotalFlexDimensions erfolgreich konfiguriert.

#### **FinalFlexDimensions**

Der Verbindungsreiter für Ihren FinalFlexDimensions-Verbindungspunkt sollte ähnlich aussehen wie unten dargestellt. Geben Sie dem Verbindungspunkt einen passenden Namen und eine Beschreibung und importieren Sie das von Ihnen erstellte Service Account.

![](https://lh7-us.googleusercontent.com/iOmkBrlLIeok6YuiHW\_qZl3jCr6HYB3-2FMiEtME1UUQFPHjjL1cBsRaHHtdpVveyQL3YHcV0FabTQWtQgS-gkB0q6ztI0QELrI5xX4fN1KfcGyjtOcmWbsFeHZ7tOw4ZjZjSJ4LXpTWGpVWZyBGji0)

![](https://lh7-us.googleusercontent.com/WOZFs6pSjqD3NFGMlv4PTu6UyZ9cHcAywiOccMn4h2TKqgF-Rz5ROXhCsFd97wPmtGtv0fvA902vcf6UUULhXAkyD22Vn3kUZwaLbCcOqjKbjeoKvPjcYemhi8qy\_pbc8hTNGhRj7oJCBBm8GOOenac)

In diesem Bereich müssen Sie für diesen Verbindungspunkt einen BOD hinzufügen. Dies ist Sync.CodeDefinition. Um diesen BOD hinzuzufügen, gehen Sie wie folgt vor:

Der Verbindungsreiter für Ihren CodeDefinition-Verbindungspunkt sollte ähnlich aussehen wie unten dargestellt. Geben Sie dem Verbindungspunkt einen passenden Namen und eine Beschreibung und importieren Sie das von Ihnen erstellte Service Account.

* Wählen Sie „Send to API"

![](https://lh7-us.googleusercontent.com/TjKLqUUaxoJSg7dUvkjKWKz7OYLfTKdFJT3pjsI5KKBcwB\_lGNQJz1hYQvM6KW9xIjryZbBUvRXLg5bKr3zNSgOPmXt9fl0BN1489jxnxXqRnS4vt9n3iCott-JOtm\_qUmMq1T5xXFD-reH8GYEDzio)

* Suchen Sie nach dem BOD Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/s22p9SJWCFQmri9p-Pw4d2UjsZyWOWjEbXUOBJZwenL9AM1b8FMYy79TD\_c5SkXCZpDTYvaJkUGji1I6FJQSvPftQp5nf77KeMAoiwCH\_5Ucbmeis8WxOFiqjbjbZhzIBA5jsaUcu68LISJHgNwnkns)

![](https://lh7-us.googleusercontent.com/RBqwvAah2I4ZhiYetNXmb7i2LkPrCuIW-yxX\_HSvITXDoidf4vnVKsGEklsUGaZRgCR857iNPrj1uNGv1wU5k2KxA0Eyxv0kh5RZmQy5dbMKUls79nNHIHva91T3uZKAw6kwzDacIs8OTH3Yi-mM4hs)

* Wechseln Sie zum Reiter ION API, kopieren Sie den API-Namen und suchen Sie nach dem API Call, indem Sie die Schaltfläche SELECT drücken

![](https://lh7-us.googleusercontent.com/s1he9mTSuxGSCO-5j9a1k6\_hCHfXkXa9k7e18mN-9c8-a9GQNmw4fYyYTlUFHJzPQRKhmTtNATxQ8qA8tI2uCazUEL1vlwG0ykgyQkONgAEKczn8UUheIsV5lpg9JN8UI93n8iq5yyAuRc0rNne0v2E)

![](https://lh7-us.googleusercontent.com/Oxair9LPtt\_3BF62GPXEy5WMCuSvm6L6oe\_C7W\_HbO\_s2IzfP2iKmDuk-gHvYifutl8JQjFMA87q5XBK3cwfYKac8UonGm7nHkHVMz8MuWsgY68bgzbJAuoE1GSLur4O0HeGb\_YQ3EyMopFl\_290NNI)

* Wechseln Sie als Nächstes zum Reiter Request Body

![](https://lh7-us.googleusercontent.com/LRDKhs2rq92Zef63nYy9NNK6bapmlPKUX10NSrRGBhvhdXIgBRte4sGunmOBUzymgnWnAv1O\_qV0AKsULSXsGT1kvorG0Pl0vQFW0exV2sqyUXhgiBMthRYTQbB10c6oI4P6Z139A8VqZVeg6c2HkZ4)

* Hier konfigurieren Sie das Feldmapping für diesen BOD; Ihre Konfiguration sollte wie folgt aussehen. Die Feldmappings sind verfügbar unter https://docbits.com/doc/field-mappings/.

![](https://lh7-us.googleusercontent.com/bjoXs4ZSra4dgpf2rC8GwA-uB\_Qp6INkdCapR7M03EV7cuqKzeVPWRCq4EHTZVeKpL92sdesL0iuHTHD1Ed5WHpr7Z15XOJMkPBlWgfbapzD4ZjfSre29Ii2SLGOvjs9-85SougBpDGzzTseAcWNVUo)

Sobald Sie die oben genannten Schritte abgeschlossen haben, haben Sie den BOD Sync.CodeDefinition für die Stammdatentabelle FinalFlexDimensions erfolgreich konfiguriert.

## **Datenflüsse**

Sie müssen zwei separate Datenflüsse für Auto-Accounting konfigurieren:

* ChartOfAccounts
* FinalFlexDimensions

### **ChartOfAccounts**

Ein Überblick über diesen Datenfluss sieht wie unten dargestellt aus (die Anzahl der DocBits-API-Verbindungspunkte am Ende hängt von der Anzahl der verschiedenen Umgebungen ab, die Sie konfigurieren).

![](https://lh7-us.googleusercontent.com/xog1wW9zE0PeVF\_SzaVS5qWxR2UuHKVR9cD4n6hxD9IAm\_jqJJHKGMCvmsF4V4bcVhd\_zaepEBrbK6wTd6kd7eqDL2Apwe799ewGo8TwMVrtRPwJcImuRjvWJxmcBiMvTjla0KgoGXhMD6oCeZFvOcM)

#### **LN Company**

![](https://lh7-us.googleusercontent.com/jaFn8KOdu907VI7vx2fkgtJZYiKw37LJ9ySqKWlgm5MLOuUcElJdOCpThwwa2NdE2eJ4iLWdfM\_Nlrkiq0BpIvrZDvyYJng94oZyaOpCIAhF5ZCTwQ0asfceY-KnIjZYrlQ5QsApnvU-hdMp8waQNeA)

Die Konfiguration für diesen Verbindungspunkt hängt vom LN-Mandanten ab, der die Stammdaten enthält, die Sie in DocBits importieren möchten; Ihre sollte ähnlich aussehen wie unten dargestellt.

![](https://lh7-us.googleusercontent.com/k28OYp8vkZZcWCKJTiSFZkDE0SlfLgE\_S3o37OhuvNsOR7Tli3xCYzqN3fRTfrlgE9fF9tYkOXCiC7kZeweCGA86wEDEMj0wKRUO7Idba1d8mY-v15uJGpYlkhZEKSlUA83yPvSlp-aRn2e-pYckXyc)

#### **Document**

![](https://lh7-us.googleusercontent.com/n9ABWRQI8k7SVDk6RsYcvI\_\_r5CWXdMDn49fKkAy3T\_0s3TTJp4aMV5K4hsiGh56YKrxcUaqmUZfj3\_QBSS2eSZ1TAPCoI5-LnJCC-JYv8K5XEOZsJLXX77EKGZCs37qtKiFHD9P9KpW2jhOEX4bu1Y)

Die folgenden Dokumente müssen dem Datenfluss hinzugefügt werden:

* Sync.ChartOfAccounts
* Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/c6Dhk5iR1fJXqjrXsbSMmkIDBl3eaRNoiijw9WMA69HSrXMKqOjMEKtRtqfXbHcy9fQH1etprR2IuZO6xpMBnY6EYuU6cyBCFjHx4yN2KxxRwTqX12TwSsUaF7wFySImLki86BUKRMW-0YKQJfQTWOw)

#### **DocBits (ChartOfAccounts)**

![](https://lh7-us.googleusercontent.com/JhBa8R1tRR\_GcoBmas\_mJ-QPT3XTNyGAdwh48N7pISM-fRNa3lfuZB7MhAScDbbCtpgGXtxx140w0bcEwgVdtMkGDh6S56uVsm039Z\_8FGA\_FwA2aSvJftr8MeHr3e9WPwRZqugKvRD\_kIVnQdexFek)

Hier fügen Sie den ChartOfAccounts-API-Verbindungspunkt hinzu, den Sie zuvor erstellt haben; die Konfiguration dafür sollte ähnlich wie diese aussehen

![](https://lh7-us.googleusercontent.com/yyq6JularNBP\_GpUbDLQ-KWu6utcEZefLXcoHboFa6rcmbN1e8QrdLkab9h2QBWuW-V-i7edmqpTWJwtqWg14GKLDnukyLGuljKXue\_XH\_bLmL2dNz5dECDI\_lkg9hO84nFIDyYWYatkzRkxAYyJe6w)

### **FinalFlexDimensions**

Ein Überblick über diesen Datenfluss sieht wie unten dargestellt aus (die Anzahl der DocBits-API-Verbindungspunkte am Ende hängt von der Anzahl der verschiedenen Umgebungen ab, die Sie konfigurieren).

![](https://lh7-us.googleusercontent.com/MQyQxEHmvG0vX4VXSnpntbXBGQBtC5uvMeNXklp-EETOIMLZNOJqwOlZp9xm\_\_Lj--o3bJETADpxgZkajW0H0xOE2Gvib9OeU3BeV-mj4lpKFqPQ8A4fymQJDjTZNI8fzrOxYqa595I0\_C3b8QkoTb0)

#### **LN Company**

Die Konfiguration für diesen Verbindungspunkt hängt vom LN-Mandanten ab, der die Stammdaten enthält, die Sie in DocBits importieren möchten; Ihre sollte ähnlich aussehen wie unten dargestellt.

![](https://lh7-us.googleusercontent.com/D25DTQRX3yecDDMmp\_UvmS9b6AWPYue8LdUueurlCTYg0qWw\_SyM0lCx1sn3VSK0m5MOilgmGWJ261YLr1MlTm9G452QyDQXbyN7DXsQpmmINEbVL5g-OIhpYKN14XQk6oEMqwoTgvpLNKS9\_MkU-sk)

![](https://lh7-us.googleusercontent.com/rGMdEdvYixTZ5wmS5ptBiGcxoOT0abpASTeSDzEFH3SSx-G97gSxIniXja2R3erYP4oIxyVezvL7VjqXKcKd5i6caNZHI-1gVIi2jrKfy\_yVFQ5T80n3ZpR1wSiPWCh\_8affNONcGAcuokvN69-Urfg)

#### **Document**

![](https://lh7-us.googleusercontent.com/WyltkYqwzyofXZpwm\_x1-SiM5MCbvDoKPQ9AVOT6nyxXnqXqQn4G-uM7BO2hNRJii91EODf5mjIwS85eOfJ\_UyATLAWqbXegd54leKsK\_zNlVWQNm79yoyTb\_Ok3605NEOM\_Hu\_ov-yaboAQ26PpmTk)

Das folgende Dokument muss dem Datenfluss hinzugefügt werden:

* Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/YIvKeqyGUDBZIoi7I6jhTIlUYtsgYEMeKA3h4Xm9KHz5pYWssDuIaq7343RQdEsxMznTNnReWEB2OCqBQGvgzi7HEOVGlX5EqPa2JEO5sC1LpUF-OXvYLO5a7LMbE2h2YY1Bk2rRnNbCjAZqIMuIxGw)

**DocBits (FlexDimensions)**

![](https://lh7-us.googleusercontent.com/zNJteyBB\_TcRKGE7GL3iPPlFaOqbij5ag37NdNW5GcZBz0xMmb9iev8EktCSJDSNkeZPOnCf-5nImxJjn6RIBTg3x8xJrLK-Z0Z48VTXXLPNIO-3NnmDEVVF-9oHteOQWIjCIMhhzKLK7iCL\_jVsfEY)

Hier fügen Sie den FinalFlexDimensions-API-Verbindungspunkt hinzu, den Sie zuvor erstellt haben; die Konfiguration dafür sollte ähnlich wie diese aussehen

![](https://lh7-us.googleusercontent.com/ymjxWkOzchUu91ovhE1eE58mSRCyrclNKsNoK48gFcSwKRVuc9Zfy7QZzJ83ATXUWJO4sgPpcNEVPyYZX8dr-sJoEfYKez-WtScX\_hnmOfH-2wBcFKrhxy5wwBUSlKP-ayxcMnCiQ6DKrgqYkfL4xQg)

## **BOD-Auslösung (M3)**

Sobald alles oben Genannte abgeschlossen ist, müssen Sie zu Infor LN navigieren und die BODs auslösen, damit die verschiedenen Stammdaten, die Sie für Auto-Accounting benötigen, in DocBits ankommen.

![](https://lh7-us.googleusercontent.com/OG5eKwuynVhgRagfTwylC2hT6lYMKIgn0ogn1RPShzv7gbE2IO4lC8YzKWDmHa6l6waMREGwVLZmhsCOhUWNrp\_7rkkdrVgo5Z8s84V475UO927BPujEwsX8SY7kRsZBt3R0GUWD13hogj0LdgqNotU)

Wählen Sie im obigen Menü im linken Menüreiter Common → BOD-Messaging → Publish BODs → Publish Financial Master Data. Im folgenden Menü finden Sie die BODs FlexDimensions und ChartOfAccounts zum Veröffentlichen.

![](https://lh7-us.googleusercontent.com/KWv\_YZ0BuoZrBvnp2MRzXKRRH1pID7V0iwjCkT4xt7NcbHYoZnFS6wnM\_itC3RzNNGJ95565KynkMFuPb-1NjY0zOGjvlINvVQIrJBcm8daOZa3UiDIB0zBPlt5BS5KavsmYcXHWBQZ9NytMg6NJezs)

Wählen Sie die folgenden BODs zum Veröffentlichen aus, indem Sie einfach jedes Kontrollkästchen aktivieren. Es sind keine weiteren Änderungen erforderlich, da wir alle diese BODs veröffentlichen möchten, damit die Stammdaten in DocBits vollständig sind.

![](https://lh7-us.googleusercontent.com/cp9CKdRYofwTrRodTNbZDfMmi\_Q23jchyt\_w7hFkGvvoBo89uhSRoKz0uD2cm2M0tLDmrkb6-8qq9z5EfX-ciEmraWqyytxH09jMK8jVVunb8zjK9EkvGhyl07Igoa4sf8hCLvyGnIlHMVjeLzMFrD8)

![](https://lh7-us.googleusercontent.com/cu8PW0WenwC5jBBFa4trAua-d8zYxi60S2syvKHoBoL2Tk9jdQAOQTvUvGZWSR3cpErwDUZ3WHkm4cDCwS1ZhSJyiQltf43\_Re05WddfxQwJ69C3E\_z\_0bMhEwbq3NasV3Q2waKJlfyBk1oIWdVDjps)

Sobald beide oben genannten BODs ausgewählt sind, navigieren Sie zum Reiter Options

![](https://lh7-us.googleusercontent.com/imBr628dcJJoNBknxVfKjoWindKT\_\_5AzmYDVXIaHF\_n0RWQUSiK07EHH1df0L2xxCOC5z36UQOfsknF4-GwUgZ9tDZcwDosjxChqFft0GGvVo1JAkPpK\_St-GB7NW1RlBgTszID4YQteYiZlFKPuz4)

Wählen Sie im Optionsmenü die folgenden Optionen aus und wählen Sie PROCESS, um die BODs zu veröffentlichen.

![](https://lh7-us.googleusercontent.com/3LH3Me8kacFfp1QH0VFMIfzQtWyFt12IgRQzcAcJByoPQtjhxDnQKE3EjNLO349WeW2WINoFwwrpQJIOoSXBBM\_tmIecJLJEyLipUHXel5yRw7H98OdfydXJdZcChaHvnnwc86wihiblnthMobZyu\_s)

Sobald dies abgeschlossen ist, sollten Sie die drei separaten Stammdatentabellen in Ihren DocBits-Umgebungen unter Master Data Lookup sehen:

* chartofaccounts
* totalflexdimensions
* finalflexdimensions
