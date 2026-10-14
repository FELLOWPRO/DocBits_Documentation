# Auto-Accounting

## **Voraussetzungen**

* Funktionierender Datenfluss von M3 zu DocBits
* Korrekt konfigurierte DocBits-Umgebung

## **Infor-Konfiguration**

Öffnen Sie in Infor die Anwendung ION Desk. Gehen Sie im linken Reiter zu Connect → Connection Points

&#x20;

![](https://lh7-us.googleusercontent.com/Gl49rTfnpYQjXjpUNF3SEouZiJ4pPeHVk60d7dyHizfPLT6sn4AoKVQPPvpgg2cD4ts40hDeWQRs3BqmKW-CAco7Dt0oWKF7ukQJUVDBgSUoMNHt\_gRkqLxkF5CC\_CNGpVRzrNs7rfF1msK320\_J02g)

Hier erstellen Sie den Verbindungspunkt, der zum Import Ihrer Daten aus M3 benötigt wird, die für Auto Accounting erforderlich sind.

Klicken Sie auf „+ADD", um einen neuen Verbindungspunkt zu erstellen, und wählen Sie die API-Option wie unten dargestellt

![](https://lh7-us.googleusercontent.com/ctE76pck6mGmBVxRIMhHyn0TbSKKsiGjO7rO185fjndTIo7qYyvSZS3neUdV2CWPqBSangpJ4oG\_g946\_KyOwWyJvacZe5htWiQLTZQLzfNHvsHDhmMQmjh7MrGsqKp6sm-XPcGmEwrH2ZMYCd0bUl8)

Sie müssen den API-Verbindungspunkt mit folgendem Namen konfigurieren:

* ChartOfAccounts

### **ChartOfAccounts**

Der Reiter „Connection" für Ihren ChartOfAccounts-Verbindungspunkt sollte ungefähr wie unten dargestellt aussehen. Geben Sie dem Verbindungspunkt einen passenden Namen und eine passende Beschreibung und importieren Sie das von Ihnen erstellte Service-Konto.

![](https://lh7-us.googleusercontent.com/p-jly6\_S96TsCmpFg9oOob0h7Q7NBlTxRKgNCphiy5QfbK\_lrLMAR2miVUQh-fXrCfGdZr17ongp5c9bnK6HuHCVuDArHhYcmKDlAyO52tGcxg-VXBLXZ1ka8yqZ4DWnxFFMxUKkE7jgvCgr7P-nzdU)

![](https://lh7-us.googleusercontent.com/GkX20Q23htKae7OOcGnJ5J6f0L4I69vOU9jYBpY1m9bpDPdtsD584mh\_9IaZF37Ne1OY2uOPgFxYYjwTrBOoZqahpJLlY3n3qmBn0sgzC0eVu91wE0NWBvESBFJmeVTITQoqUTEU56tHEj47-LQmI6E)

Sie müssen in diesem Abschnitt zwei BODs für diesen Verbindungspunkt hinzufügen. Diese sind Sync.ChartOfAccounts und Sync.CodeDefinition. Um diese BODs hinzuzufügen, gehen Sie wie folgt vor:

#### **Sync.ChartOfAccounts**

* Klicken Sie auf das PLUS-Symbol (+)

![](https://lh7-us.googleusercontent.com/hFWg7-4Osuy9Q0uZYqT9yfAPFYsBi7yitHj7BBxQ94vbsDVg-GuCeTBakvV2eQNjqMGwDAF90nO5h-OxFR8HtYEiYcALdBq5Fdj\_Gl-wU8QePGV4Wr3\_78OK22nUY35dfCQhUPQIp\_qkdHN0wr7V-VY)

* Wählen Sie „Send to API"

![](https://lh7-us.googleusercontent.com/jA97YupOjXJlRFRxduo\_tYO4YYDZoT0mHxWaPWfJGyU4RTNSVNRAIAsR5mzRyLh1iusHl0cBKUxhYj3hQMzacGdN2QGsvPGy1vHeq\_JNhDqxc-SI5HtZh\_Z\_zmaSjyJwmr2337tzYSWfqDl3JGkjBqY)

* Suchen Sie nach dem BOD Sync.ChartOfAccounts

![](https://lh7-us.googleusercontent.com/hzuwy-VU8xpgQ85NGHAk9u-m-\_Sw4iffT0SNtWTJw9iWHRIsIvGTEYQgJYi7CUoYC7\_Yp2KDtsohRQkNtIgr1VutFbR8mTkT\_5HmJ7ecgW8pcGuZTuwxtPDOlJpWuONq3WPIupRRBxBJPlsYQ9w-bxo)

![](https://lh7-us.googleusercontent.com/6p8nXaRAI0ucRzmyKfYYg3J8MmHXVgHs-KxcItxeZ6wbefK1YdMrYSblHwnXkSiajApB5ds\_EgpJJWYjfbKOjHdsh-H49jG45weOX9v0YBSAqdXmKgoaBcP7A4zDyINMNVt7RWgbQ51WxNTsfBllvQ4)

* Wechseln Sie zum Reiter ION API, kopieren Sie den API-Namen und suchen Sie nach dem API Call, indem Sie die Schaltfläche SELECT drücken

![](https://lh7-us.googleusercontent.com/aRXjuD3nkYsFNM2eYkfmHrshU3ycmN5G4OGSFFadbSToy3pHKYWMw6apbyMhJ9o-5xB6UDA4rbdPjZWAdP-OCH8gQFWV5vWXp0rqLxP9DozP4yMS074\_nsHzirJUgBfkBkQ8Ydp\_WjImf2bx3pDnLPE)

* Wählen Sie unter Product den API-Endpoint aus, den Sie für die Umgebung erstellt haben, mit der Sie arbeiten und den Sie in ION API erstellt haben. Suchen Sie nach dem folgenden API Call, wählen Sie den API Call aus und drücken Sie OK.

![](https://lh7-us.googleusercontent.com/LQWk7uiEPCxJcohMmIuRrg2p\_wwE\_h5GoEEP3Y2IdpKARppHoGB4Rt1KRM\_2AiXyG0-ieIV7BM51IRN5exKkhG8eLTkKCftm88j2NLc15X50VLu9t1sZZnQ7DsIIvgUsxz7oryzVIkfmifw-m3qkLDY)

* Wechseln Sie als Nächstes zum Reiter Request Body

![](https://lh7-us.googleusercontent.com/0tnYxKvtW5Fw7yJfW0QBMclidw5kKJB4oi6M932hGO8ROokbMXbyFcjPQq\_LSVe8hv3ZyVVWqjDO4vMMRgPm1L2iXV3pSoiyzrxGLvBTx4kwt5uo6XtHEt25PRVdM6aIddhHDrT7HGzx3JaZ1F02-YI)

* Hier konfigurieren Sie die Feldzuordnung für dieses BOD. Ihre Konfiguration sollte wie folgt aussehen. Die Feldzuordnungen sind hier verfügbar.

![](https://lh7-us.googleusercontent.com/3giuZYeQjdZZHAg7W-pcAHB\_69KP8Ukh\_0NhATYBxvrS\_Qy3yH58fQyrp6GKfOzi1xJms5KV-XVNnAWtX6VmIBwdxSVum9JA6-H9W3XIUYKiTEK3IWoKA560a5I2lwmYd0kitdfC4pRkQVULyWp9PpA)

Sobald Sie die oben genannten Schritte abgeschlossen haben, haben Sie das BOD Sync.ChartOfAccounts erfolgreich konfiguriert. Klicken Sie auf das PLUS-Symbol, um das nächste und letzte BOD hinzuzufügen.

#### **Sync.CodeDefinition**

Der Reiter „Connection" für Ihren CodeDefinition-Verbindungspunkt sollte ungefähr wie unten dargestellt aussehen. Geben Sie dem Verbindungspunkt einen passenden Namen und eine passende Beschreibung und importieren Sie das von Ihnen erstellte Service-Konto.

* Wählen Sie „Send to API"

![](https://lh7-us.googleusercontent.com/YLaFsc0K1Lzruo84Np3EdCTF1xsaQOLRypNpgZB7L9keTh1TwPOMnjBxJYnBOj8GrNSG\_URcRGgv\_p70-pjhBed-wvURRW08YtEWjmACMc3CleRPrHia6nihWQwVOUaZ3qHD\_zLy2W\_iMQ0I77cY\_Bs)

* Suchen Sie nach dem BOD Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/f3ikl4jh0PBhYmP3r80BrHuGGu9w9MHe-E0VmyXOCmFEkkK92cxgVimwyP8RF0kF2GruVaeDjiYRKuONX5bQ2ZBRmdKFx8Bf9cHvX5q-xYnXNH0a2xnR4eg1ynyWbRRRoY5xn28HJ\_ziRiKcTN43aHQ)

![](https://lh7-us.googleusercontent.com/nXQZ1LLZsrndggHkAmRtMlV7YzFemnjC9CnS4AdUVDits4zNfzlaqKdHnNcLyTtDkQSX3SB8R3fnZhGBPd-By8C364IIYc4vE2VXNXzoa4LfHP6irTiAg\_N\_2BHSYBLzaQyMCN1w5LdFiiqeiiwAXuk)

* Wechseln Sie zum Reiter ION API, kopieren Sie den API-Namen und suchen Sie nach dem API Call, indem Sie die Schaltfläche SELECT drücken

![](https://lh7-us.googleusercontent.com/LbHmVr1PimQkPu-t6VMvNVk9wVXeQBHOu-X4pW-9vGm-dON2buizVGbKekGL7tY1t4OkwQtzhl7uDhq908UxCfDCJaRDEukpk-07pJjLO-ezRUHgblp3REm0qrKF9wOtMkNWJlVVNVhmfzZ0TtUsqQQ)

![](https://lh7-us.googleusercontent.com/K-kDDTSaZiothC4o3JDihhVJFNt0PiBnLK7kF6RcBOX9EpzutfLHGstzvywBBqaEqm4WqOSQSxtvxRPtbVafPlhtf\_YMVkXjhTkvnGwLzwH\_p-YgRCGAu-DzA94MHjqQoAYTSBPgojcGlJs7tBRcpME)

* Wechseln Sie als Nächstes zum Reiter Request Body

![](https://lh7-us.googleusercontent.com/DfT6FtrbW7LbK4b4I6ssYDWOaPgUxkWsuTDpvQGw549tPFxgEU\_gmh3UwXTbyKHZR8SOHXPHDdobEhA91RIMB57ZAVatrZEsad2QW6QHiUkdZoyW\_yE\_iIGDgs2IrY0I6qL1JTZxksYoaLKu0Il8smU)

* Hier konfigurieren Sie die Feldzuordnung für dieses BOD. Ihre Konfiguration sollte wie folgt aussehen. Die Feldzuordnungen sind hier verfügbar.

![](https://lh7-us.googleusercontent.com/nqK7x1Km4wIP9aWnvMlSHl1\_omw22GRKONfB-zc8ikn\_rSsl60Ksml0oQacs8UNmPSLFSKPD7Eo9FsH42RjDo4oragvHZJHFW\_yv62KXDrF3SKnDN2-X6vqYJ5a-3bYkkvPDlNJSxFylvtAFr-2Kt8Y)

Sobald Sie die oben genannten Schritte abgeschlossen haben, haben Sie das BOD Sync.CodeDefinition für die Stammdatentabelle M3FlexDimensions erfolgreich konfiguriert.

## **Datenfluss**

Sie müssen den folgenden Datenfluss für Auto Accounting konfigurieren:

* ChartOfAccounts

### **ChartOfAccounts**

Ein Überblick über diesen Datenfluss sieht wie unten dargestellt aus (die Anzahl der DocBits-API-Verbindungspunkte am Ende hängt von der Anzahl der verschiedenen Umgebungen ab, die Sie konfigurieren).

![](https://lh7-us.googleusercontent.com/RfkP8xiF2vDzQhBNa66L0NQHk7TGjj52aK3hWoisEnWbdG3l-SZKKw8mYJ3b28ShXZ9omPS6WdNiXaCpYRQzwfges0SKznwQal7K2ElILbGBJNYu3VFm6gDQJMHYRItAFX0cdRZjXgCk2FQqHJ4iSjY)

### **M3-Unternehmen**

![](https://lh7-us.googleusercontent.com/tqYoI-gLUpe0c0x1T-WhP0\_FolVzPGHhFY8m52Fw38mJNzsDvjb7stRrBfWVjXLnFrJTTy2lyd9Dmva3\_EPG5eRWyf5ATA2cTWvCj3Ksa4Fu4pHF6rNFjfd3Cjei0UlibT0HAQYE0V22bdTStjY61zk)

Die Konfiguration für diesen Verbindungspunkt hängt von dem M3-Unternehmen ab, das die Stammdaten enthält, die Sie in DocBits importieren möchten. Ihre Konfiguration sollte ungefähr wie unten dargestellt aussehen.

![](https://lh7-us.googleusercontent.com/wpSluEs21T5wXG0egZPfUCYBP6X\_uUm6XAh-PyD8RrojTuIztzRJzhVYdzcNI5dQGGDsrhSKx\_K2-y0JDmK9w41fVUXWcW1N2lz5rizXcMnn5BuiaGRy-TEOBryGxvP9mBGJTZ16lMisoC\_YumwpS9Q)

### **Documents**

![](https://lh7-us.googleusercontent.com/uR6XaFI7TPQ4L8Suom25PBdtXdL4i100Juz7kRBxT5rdxhejZW7nPtVIlEGjWWnZLbo9ipx7G95NBFV8dd-g4vw\_vM-uPApJ02QdxvCmX27bwAW\_qUWUXajV6BFVmIfzTQ46Zj4DybsYKKblXjuWc6w)

Die folgenden Dokumente müssen zum Datenfluss hinzugefügt werden:

* Sync.ChartOfAccounts
* Sync.CodeDefinition

![](https://lh7-us.googleusercontent.com/6Bq-yQ9Yaf2OJwjBxyFvqAMUitcovquo\_iU4hc-pgag1iDwLcstggVjLsdY3bRl9XWNc3mKOwZrY1FSlu47IzxxUQHFkjIAl1r08Iw9UbKaaMh4WiWrqFuSObdTjEvCEI5IDvD\_Pys8jAydydJgbsK8)

### **Filter**

![](https://lh7-us.googleusercontent.com/LyKGzQUEswTD1XfpNDPSHjChgqNFfs4guXfM0KNuW2fPoiaeUo4uPrlGgwt3RepWUGQmu\_trUMiWb68cUjUAwXU9IRoWOsv9M2l5v4zFfBkEcioz5ok7Eoss7I-tBKtpD7wVUkGWi3U3ySrIQ\_fDPiY)

Für die zweite Route des Datenflusses (gemäß dem Routing im Datenfluss) wenden wir einen Filter mit der folgenden Konfiguration an.

![](https://lh7-us.googleusercontent.com/7xdqGdo9bS6\_IIzTVYF\_08woBXvhIVkA-c6-ZrDpDEzmEDFzDZSuxZ5LYHKVUhJqYq4Wlq1FXPfr5myjKFUsMbnJrefc\_L7URD7AbEq\_D90jEw7o8Yrhg5XZwLdU83OwlZVXqlYla61b0LyISXeBLWk)

![](https://lh7-us.googleusercontent.com/OdI-0FaqDaPKy2g9Mr8HUx\_oGRZkDrkeI6P1rWqOounpDauMThaqzs2wOawmw3RwcMlQHgI6wj16RXQDAP\_JNMGkxvmiEnPJ\_bvse2CvMegPwinSIJRLmXaCzfjxtB1FDqnqPOMwrMYNKJyiC2sGUe8)

![](https://lh7-us.googleusercontent.com/RMPIV6ZWsUcBA6klny6Ln-\_nhMGl1zdEHfUKK56owelabcG-6gM1S\_eqWAVLTeOHdec3D5D6xVJeC5evnJC61L8daV6IbJbCmMashkWXSK4Tv4RdE\_erjR-Mk2RihPodIG4HrqSOQ8hi7SG3xctXd-E)

### **DocBits (ChartOfAccounts)**

![](https://lh7-us.googleusercontent.com/Npm92rS\_EO5roSy3tldC88hFIyiDnZjHnnVSkkKyfmNrOcbuVj4LPNrcsWvOT8IHNQKGMqIZymG9q3VMGG6RwvuRBqZgmhHxqXn1oieajDmz8giQxSr8wOFzb8TQTJJWwj912-sDRtkrDAXCr7ne-pk)

Hier fügen Sie den zuvor erstellten ChartOfAccounts-API-Verbindungspunkt hinzu. Die Konfiguration hierfür sollte ungefähr wie folgt aussehen

![](https://lh7-us.googleusercontent.com/Dw4y6OMuMAYHZjH1etj\_FqdsaFxaRhQyk6\_PaxXrWLhrNirEn7xQc5uIpbDT6Wz85XvZgY02aNuWfbYKBzo6W9aavN\_Asu5ENfr2dszWYQqs9sy6zl4o0NxRe3IPXodLIGf9JkbK2\_UtYe4dVii0JbM)

## **Auslösen der BODs**

Sobald alle oben genannten Schritte abgeschlossen sind, müssen Sie zu Infor M3 navigieren und die BODs auslösen, damit die verschiedenen Stammdaten, die Sie für Auto Accounting benötigen, in DocBits ankommen.

Drücken Sie zunächst Command + r, um das Eingabeaufforderungsmenü zu öffnen, geben Sie „evs006" ein und drücken Sie die Eingabetaste.

![](https://lh7-us.googleusercontent.com/pzAL0cnM94AUE4KmTyBV8OPU9ft\_g9o0-KB9Ib0AjrvG7Q59GHT-2biP4n7yFyXRxQ0gjy85G6MWMWUeMIWJcTQ9TKwzCEywd7I\_6\_vV-muepobkW0O-4-CZxsmjOEQ7uM1frZpTLqlLS3aSYkEuwAw)

Das folgende Menü wird Ihnen angezeigt

![](https://lh7-us.googleusercontent.com/Wx41TNpg1zuaf1rXIBvSCVzSRf6q74rdLs91el21iErqQnDiF4cv7X0nyDaS2Gjimj7xbfAK-7mo6sXN6fkK934mHnCnivFTz9NqHi6dBoMYiRT\_vLrkVUlFd\_T4Oan3Zkq3WKLoI-kmsElHSKO7zY0)

Um die verschiedenen BODs hinzuzufügen, müssen Sie die BOD-Nouns und Tabellennamen für jedes BOD einzeln eingeben.

![](https://lh7-us.googleusercontent.com/5gVWRDm\_8CSyoQRkq-7LuI8MLU1BjRN6Z6YCcVZp7G3Be62nQBht-eUNZreTzV2rFWYK\_RcKiyzwTTlT5y5X8eGf-Z7qDavDyHML0zv6Yt6jGu2z9d-nL0K-m446nDZa2-aiFLnnzjAwk8pTT4RQK6Q)

Die BODs, die Sie hinzufügen müssen, umfassen:

* ChartOfAccounts
* CodeDefinition
* CodeDefinitionAccountingDimension

Um anschließend das nächste BOD hinzuzufügen, drücken Sie nach Eingabe des BOD-Noun und des Tabellennamens auf das unten angezeigte PLUS-Symbol

![](https://lh7-us.googleusercontent.com/66wclj8g8RAYT9-UIgRMs0qnuA9srmWv21PdqdNm\_q5icGmabL17-DpLOSs4pm6Nj3xJN-9xt7io\_5GZGfzSQ2qt\_8Y--CJFou6FaOdufiuxOdKHrUUYELNdGy9e-gnWg\_hAMSfs\_NJa6zYBMpoyTVs)

Die BOD-Nouns und Tabellennamen lauten wie folgt.

**ChartOfAccounts**

* BOD Noun: ChartOfAccounts
* Table Name: FCHACC

**CodeDefinition**

* BOD Noun: CodeDefinitionAccountingDimension
* Table Name: FCHACC

### **BODs veröffentlichen**

Klicken Sie nach dem Hinzufügen jedes BOD mit der rechten Maustaste auf das hinzugefügte BOD, wählen Sie Related und dann Run.

![](https://lh7-us.googleusercontent.com/225-ujyGzG\_RJOXgbx8NOh\_4s-Sn\_o80b\_h0DTsJqfr6OcyPUwkWLF2lfEyzFFFKddKmlWd32bb94qeYlOdVBTI8RL0r6ZfZKloVTrAYLNp-U5gL3aJhW4d72ExkkyM4AydLczsPvdE1cRDfGNKupdA)

Sie werden zu diesem Bildschirm weitergeleitet.

Ändern Sie BOD Verb auf „sync" und drücken Sie NEXT.

![](https://lh7-us.googleusercontent.com/3DyjXUSlAF7msQT1OAO3aCr1U9R68XZj0oE\_yJwsBrBj-FkiZR-oRYQYSClHG0iN0FXFdDdKQA1hOBlw3jc-lXQCWkiDFa0IweuQnoR8k-Mgyp1HeI5ImJqNogz-Q3b3P33ywb0B2o1pZ-TkZ7mAwZA)

Sobald Sie NEXT drücken, erhalten Sie eine Benachrichtigung, die anzeigt, dass der Veröffentlichungsprozess der BODs begonnen hat.

### **CostingElement**

Um die Tabelle m3costingelement in DocBits zu importieren, müssen Sie wie folgt vorgehen.

Geben Sie auf der M3-Startseite Command + r ein und suchen Sie nach der Eingabeaufforderung „PPS280".

Wählen Sie eine beliebige der Ihnen angezeigten Zeilen aus. Wählen Sie im nächsten Menü TOOLS und „Export to Excel"

![](https://lh7-us.googleusercontent.com/I8SYWm-JwpyYRHFUp2obGtXcsa7m\_blJ\_lTrnhczztRIXIN5gfxCt3eRw6ZI42fH6AwnsKyv4ux5-rhaT505PsyDFFI\_anUNvmACFyx\_ssgxaqWq25vLt\_E5s310HNoiPPLf35qJlYtstjpj5Cc4aB4)

Wählen Sie „Export all Rows" und drücken Sie dann EXPORT.

![](https://lh7-us.googleusercontent.com/wtjHI9L4YUhf-yJFjcPGu218Vis\_zELtCIfpmkIUKgasfrdfNW-dr\_J1DqXlfD-SBrnVduDrMLAIAQh6UTlzBqEP\_JPXP48elGMyGj0ByZbX7TpqlnIfRZ4ZoD0pyCo-AKigeKjlHN6cFcdpeClZ9L4)

Nach dem Download müssen Sie die Excel-Datei ändern, bevor Sie sie in eine CSV-Datei konvertieren.

Sie müssen die Excel-Datei öffnen; sie sieht ungefähr wie unten dargestellt aus.

![](https://lh7-us.googleusercontent.com/l4WbidK-5zSEQ6rwqhknudPBmmDji0f1WwTh-kHomSkgEOA7s4m72cLw8z-4nflqBvPp\_2AajIEZDZz4dRLs8jlAeYHp4ee2tDysxYy8YBjj4ktHxdUXpxO\_Z34c8\_f0cNMX-9lp0lT5wOZoH1QUCgE)

Aus dieser Excel-Tabelle benötigen Sie nur die ersten 2 Spalten. Ändern Sie die Excel-Tabelle so, dass das Endergebnis wie folgt aussieht.

![](https://lh7-us.googleusercontent.com/QaNRlKHrU6kZWFqmwYR8C\_\_nLVOeqowAxJlvooSVBIAF5ayx2xZtUppsn0jzBcJVi90vemM3tZMZOjn549N3RzMuWuE3w911WLVS5NMuiUmnfXM\_xUXbqmzBtiQZstnpEYj1dUSbs\_IkAydlhBfdmcc)

Sobald dies erledigt ist, speichern Sie die Datei als CSV.

Sobald Sie Ihre CSV-Datei haben, gehen Sie zur folgenden Webseite. Diese hängt davon ab, welche Umgebung Sie verwenden:

* Prod: http://api.docbits.com/
* Sandbox: http://sandbox.api.docbits.com/
* Stage: http://stage.api.docbits.com/
* Demo: http://demo.api.docbits.com/
* Dev: http://dev.api.docbits.com/

Hier laden Sie die CostingElement-Tabelle manuell über eine API hoch. Klicken Sie auf die Schaltfläche Authorise.

![](https://lh7-us.googleusercontent.com/tyzOq3BR2QqTguQFKicxo0dE5j5hGsP-BhfVbS81O\_mxN5bSVp40jYfgsVJcE\_rBLFMDJNvbPkPIdjPqaqoNbHBBM-9hx0i-U4VAH9ISBYhpwKgqQeUEd67VV1E4izwNyxbAwwrhCmrAo1uIKhLherY)

Hier müssen Sie den API-Key aus Ihrer DocBits-Umgebung einfügen. Dieser befindet sich in den Settings unter Integration.

![](https://lh7-us.googleusercontent.com/4ADnevq6kq\_vbxUJpyPbHNcGvRvpO-l9Gwd8ZaYf\_vO4uWhSl1jmKNpddmHGc9ZHMMbXCgLOElLDYbNwB3INmBDETecPrDnpI601IUOZQlT7tc7OLSPXwkooOJFNwML2i\_gvBPuE8CvfwRpX-ZIlb\_g)

Sobald dies abgeschlossen ist, suchen Sie nach der API mit dem Namen master\_data\_lookup/import\_data und füllen Sie die erforderlichen Informationen aus. Klicken Sie anschließend auf EXECUTE, um die API auszulösen.

![](https://lh7-us.googleusercontent.com/8UD4FhFv2dRB4cMjCDL4G9ndjH7laVMKWqdeMaJGgEo48-UVvucB1uOydzNdfFy0yPM5bb66mZB4k9uJR7TTiEREGFaV2EqW01gxJpTyuUfGNh5QmBjySkyhZ56gWV8sYs8WI5RnHcENtXgjTU0vg0Q)

Bei korrekter Durchführung sollte sich die Tabelle M3CostingElement nun in Ihrer DocBits-Umgebung befinden. Auto Accounting für M3 ist nun für Ihre Umgebung konfiguriert.
