# M3 Konfiguration

## Voraussetzungen

Sie haben erstellt:

* Einen ION API-Endpunkt
* Eine ION API-Datei
* Eine BOD-Mapping-Datei
* Eine IDM-Mapping-Datei

## Importieren von Mapping-Dateien

Bevor Sie den Datenfluss einrichten, müssen Sie die Mapping-Dateien in InforOS importieren.

Im ION Desk → Verbinden und öffnen Sie Mappings

![](https://lh7-us.googleusercontent.com/EV8z6b\_W9tjTgML0j3qJAYHCTYLd4N5yLrArdIECftYpMOCRTRJ\_a7eADEzljFM4XHxMUJ6Nx9Z6EN3Hmzote5F0HrM5zd4p1BS0NYicUWDnkhQFX-\_3MGbblEYi6x2a1K25SclYYttgW3cWQbOjvfQ)

Klicken Sie auf das Import-Symbol

![](https://lh7-us.googleusercontent.com/agBHtjNitneogoZsSG1791QAARbvesv9eSriAkw0HL9Fy372Ty6SmQG1sKJjOYZCuE0SnGT3agHAFRJYjgGNxJrN1CMJj9L-fSPhNmXxN78iDKqrrdgEVYFHxsNwy9XLiUFpBCQ1wnWlwyeFH08DsWI)

Wählen Sie hier die verschiedenen Mapping-Dateien aus, die Sie benötigen, darunter: SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice und LoadSupplierInvoice\_ProcessSupplierInvoice.

Nachdem Sie alle Mapping-Dateien importiert haben, stellen Sie sicher, dass Sie jede davon genehmigen, indem Sie auf das Häkchen-Symbol innerhalb der jeweiligen Kacheln auf dem Mapping-Dashboard klicken.

## DocBits zu M3

Der nächste Schritt besteht darin, den Datenfluss in ION Desk einzurichten. Navigieren Sie zur ION Desk-Anwendung und wählen Sie Datenfluss → + HINZUFÜGEN → Dokumentenfluss wie unten gezeigt

![](https://lh7-us.googleusercontent.com/Kkro7w2LPfnwf-JPMmPI2DzrSRNEi\_F9aWW02KDtBvAZz\_R7j9DZ71Nqw3ETPSQqDuxBzJ1TU8Uuzz5jU9rOO\_tvDBf9abVF-FDSxln\_pjr-HMRdYBnGMwgcM6hg-pC2B7FgdBkXibivMB4PptvZ6fk)

Sie sehen dann diese Seite, hier bauen Sie den Informationsfluss von DocBits zu M3 auf

![](https://lh7-us.googleusercontent.com/K0B1lC\_KLO5RZqGqAltp6JnZZ1sfZG4wg-i\_nxZCnLjML33yvViRUHOInK3iHYbzbV4I0uqDY8JpsZMxssD8bbJy24A1zKr9PfQEyqVxewx\_L87RCIwzn5MDRjMqgx4X42vkKthbyz--5DDe1H0rvHQ)

Ein M3-Datenfluss sieht ähnlich aus wie unten gezeigt (es gibt 3 DocBits-Anwendungen und APIs, da sie für 3 separate Umgebungen verwendet werden).

![](https://lh7-us.googleusercontent.com/6Oy\_UBzYNml-7\_sayDEKhqYF92yDzlUNzmGLQSWZOfDT-avvfg3oNUnv\_DtXNSP0XF43D-zgIizIuTrCXl6ockLU2uQLYFJna72fzL5BP-T89xjF4oWz2eAz9w0hsoVieyTpgSw\_Prvj--89Kc4Kqoo)

Alle Teile der Kette werden aus dem oberen Abschnitt gezogen und abgelegt

In der Kette sind DocBits und M3 beide Anwendungen, während dazwischen Mappings vorhanden sind, die die Daten in eine Form umwandeln, die vom nächsten Abschnitt des Zuges verstanden werden kann, und die Informationen "abbilden", damit sie dorthin gelangen, wo sie benötigt oder gemeint sind.

![](https://lh7-us.googleusercontent.com/1kjgKNmIQ-NbM\_JukcPsj7qmyiMB9b693ixg6Dh1kOlZ6NKgBXViYwn0MNUBHt0WKKWf\_1gpRvxgqjIaqpqcy-SyXoYjhJLt3m\_bv7wbVADzqHRsx8TYXWyIQO82X-Ixfl5b7iI7nxTRkw06sX3xsBM)

### DocBits-Anwendung

Geben Sie ihr den entsprechenden Namen, z. B. "DocBits", und wählen Sie das Pluszeichen und suchen Sie nach dem Verbindungspunkt, den Sie zuvor erstellt haben, z. B. DocBits\_Export oder ähnlich, und klicken Sie darauf.

Um diesen Verbindungspunkt zu erstellen, gehen Sie zu ION Desk → Verbinden → Verbindungspunkte

![](https://lh7-us.googleusercontent.com/8qsMIUKMrgmcYqqJPL2zF4GVeHuvSHvn8Z7dfonRuvKFPcXmN4hx2PIrXko4lvW7ayD7s2VRFOMvWkQSxfAH5tTuhg0XhzYmSzlsgnowWRw8GmQC2y5BjcS9X2MjDzLSutgoHg2VN59kCYRunMSxkIY)

Klicken Sie auf "+ Hinzufügen"

![](https://lh7-us.googleusercontent.com/-3-3TzgEQppYmX64-clxjp1JBjNz9fsA2FDPqirgNF0wL8DsDJACzUBuSw5wBL2k9JanqvMzAG352CWafOdtjhMfZalJnBFVSjaWA1AszhCjKtCsTvLUUqq1WwMfF-PqL-u7LRo4TPbj4fP2\_j48240)

Wählen Sie "IMS über API Gateway" und füllen Sie die folgenden Informationen aus

![](https://lh7-us.googleusercontent.com/wImUEi9mXiQjW5O6mp7\_IrKk4CTaHFs903DJ6TXqUEcjGq45TnUWdusFTGH1jzpBPP\_TC7rokyjrkYWmh3emSKBQs05qYbO80TO87De0C5OveVURykQMCLFRRYakEMoFHpoeXzxH5QIbKJdjxujeY98)

Die ION API-Client-ID befindet sich in der ION API-Datei, die Sie bei der Erstellung einer ION API-Datei erstellt haben. Dies kann anhand des Werts "ci" gefunden werden.

Wechseln Sie zum Register Dokument und fügen Sie das Sync.CaptureDocument BOD dem DocBits-Verbindungspunkt wie unten gezeigt hinzu.

![](https://lh7-us.googleusercontent.com/ga1q0Uwdi2GNwuiz22NvDtCzGL0krSkBPLsEVxE-mtoMV7CtEU8TPO0PhF40oB9NB9iv7DCJi9niLnsKjpqarWJsgGRdc1W0pFl9rTDm7i2\_BSLj3JOrzR7iclPdqOdpztgCxWZG2Teg1gWljaMUq2E)

Speichern Sie dann den Verbindungspunkt, indem Sie auf das Diskettensymbol in der oberen linken Ecke klicken.

Navigieren Sie zurück zum Abschnitt Datenfluss von ION Desk, um auf Ihren Datenfluss zuzugreifen. Ihre DocBits-Anwendung sollte ähnlich aussehen wie unten gezeigt.

![](https://lh7-us.googleusercontent.com/fBzKL6RU0XvGpn1cKFZIyAp2amKonBWc8ilbAq5u\_r867xywWWAD7EjP-g-wjlwUsrG4Wz0lS6Ujdnu8P3vc8Q3FbtbRR4qSBmbSLoICfX-aHITMDdHp07bESefC9TuUUUQiHGb1j00HNtB\_7A3iDFs)
### Mapping 1

Der erste Zuordnungsknoten sollte wie folgt aussehen

![](https://lh7-us.googleusercontent.com/F9AcE4V-s9vs-0kRz8BcCtdHUUQoaooyK3GqOj8pAQWuvIguoUO-tJx7WBEW6\_GmzwNsJp8VUYezGCiLPXvPhEynac3FPh\_NJOvqs1SXtMIUsF5\_HjWmcvY3VC-eZsjG0ZE8HmsKsFhocadr96drSbY)

### Mapping 2

Der zweite Zuordnungsknoten sollte wie folgt aussehen

![](https://lh7-us.googleusercontent.com/8M\_V2BtkOGyqV-828ct5c2QvSs5n5\_RtLjlH717kspZwlgtfjbz6tpOJCCXDelruBenMjxsJPqncQ5hUw2bQkM3ya7\_WrVyEBz3UnaU-C9oVOWB8nNtXA20RBYgO3EBMon2TfgpefY0lSPBzF9NoTeU)

### Mapping 3

Der dritte Zuordnungsknoten sollte wie folgt aussehen

![](https://lh7-us.googleusercontent.com/x9QUHTgQrNaeKnTeMIUflkWjcBr2c3LgsYe2BZBjv01hXiEkvsLtU0GzYt5KppcE12ZqxWeBJ1kbLOC6qA3yKHhujCZt3sFpDNE5yERkHHMJJEjFl0jJE90nQ-iXeMLbR-Bk6G0NIL8AqG3U48Seiuc)

### M3 Anwendung

Es sollte bereits ein M3- oder ähnlich benannter Verbindungspunkt in INFOR erstellt worden sein, so wie bei der DocBits-Anwendung wählen Sie ihn aus, indem Sie auf das "+"-Zeichen klicken und es sollte wie folgt aussehen

![](https://lh7-us.googleusercontent.com/JTXIN5QxidvFJyjegxSw8kA7yVfHfuypxi5yX21CsSlGtOVgykc52U2r0077-cKqNhc0B4zSSZotlipFesmLo371kho3wUSRPzmwEir-stbxyZV1PwCDXkq6qJMm4PNXt\_wGarDMixGIU0tu-eAqV5Y)

### DocBits API

Sie müssen zuerst diese API als Verbindungspunkt erstellen, was wie folgt erfolgt:

ION Desk → Verbinden → Verbindungspunkte

![](https://lh7-us.googleusercontent.com/VOXW6LixmcKjHW0CTOO5L8fK6r-4k3jqk0AnoR6DEVoGgJMbx65hS3yKSgMWItypdz4Ha82T-bKCN0aMv34gif-b0Aw7zpDFPBK9G-K6x9\_csrM9xyKcpmWam15tKqO1\_rwKtMsJ2CSoWqdpLxCD5tA)

Klicken Sie auf "+ Hinzufügen" und wählen Sie API

![](https://lh7-us.googleusercontent.com/c1RAUNoA3YBhvf6FLJ\_L3ouyZwHK-3bBRU83eL3oAQXjG6SjWEO9O-gDKPItPm8AI\_YhadaCZU-GxY-qUXNuQMiRiKUhBYUtJ8kOFVg\_YYpzJDSoJ68NYSaEtHBSyyfnq0VbHUdWY1e8lBQ0j\_G5xvI)

Die Informationen, die Sie eingeben, sollten wie folgt aussehen

![](https://lh7-us.googleusercontent.com/h2KU6pKeKl9wX8oyul0KmbL\_kg-iPQJpBqbf29l64ED2e-Z4tNj8-m4hBN\_4SSiNPf2TrE92TD4H0-0AZ0eWxMFmDV22IdPlU9NO4XlQF9k0Swg0X3Sm1HMsSPvWi7Q1HUr8uy8j3aDRheFxZqZ2Gbc)

Wechseln Sie zum Register "Dokument" und fügen Sie die folgende Konfiguration hinzu

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_api\_docs1-1024x279.png)

**Acknowledge.SupplierInvoice**

Die Konfiguration für dieses BOD lautet wie folgt

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_ack\_11.png)

Stellen Sie sicher, dass Sie die Option "An API senden" im obigen Menü ausgewählt haben.

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_ack\_2-1024x338.png)

Stellen Sie schließlich sicher, dass Sie auch den Anforderungskörper entsprechend anpassen, damit er wie folgt aussieht.

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_ack\_3-1024x260.png)

Wiederholen Sie diesen Vorgang für den Rest der BODs, jede Konfiguration ist unten aufgeführt.

**Sync.PurchaseOrder**

Die Konfiguration für dieses BOD lautet wie folgt

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_po\_1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_po\_2-1024x359.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_po\_3-1024x297.png)

**Sync.RemitToPartyMaster**

Die Konfiguration für dieses BOD lautet wie folgt

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_remit\_1-1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_remit\_2-1024x351.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_remit\_3-1024x299.png)

**Sync.SupplierPartyMaster**

Die Konfiguration für dieses BOD lautet wie folgt

![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_sup\_1.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_sup\_2.png)![](https://docbits.com/wp-content/uploads/2023/09/DocBits\_Exp\_M3\_sup\_3-1024x295.png)

### BODs

![](https://lh7-us.googleusercontent.com/zaDSnm844wXqyefN58Y1DvuJOnMaoOrYQ\_12Z5ZSng8-TPy38Th2ZPdAD6hyIYCOvBKGPDSvGpTmtBPq4K5IwyGtsKyMvk-CKOuY-hzD-RL7UrsG39qLN7m3\_IDcDS66KeIQF5e70OWlHO1cbVvQUXM)

Die folgenden Konfigurationen sollten wie folgt aussehen:
#### Erste

![](https://lh7-us.googleusercontent.com/5gLpbQEYYW90dVLkSc5V60LeToMe2wcOcHHtwTdIdT0o0Gktu8T_7i7zfNikjgETM3QmzAsJAknlEGeB0W0YFLLi56g2PKPwyr2zPcHaKdu8XJWHgaC1u4--_CHNYfd1wQ__3kZpv1_PwyZty3JEyak)

#### Zweite

![](https://lh7-us.googleusercontent.com/xbWTcP8hYA72Ijt7_IV6l-9jKeSalbRPvTn7aNVcnWYMQcD2RDjM-EzKpBKjSIKF_-r8BaxmmCo9uz6-E-vC9flKb4toU3SH24EPLgbXc-VcfJeDdJKglf5P6WV6XYZg0cZVWAoyvS8qgtuR6ZqJYlI)

#### Dritte

![](https://lh7-us.googleusercontent.com/F8wVWXuHkLLW2kuu_7Dxe9LhyYdm04tl__Sp6FjeTyk_JFUzhCIUhVlKS_cq3I3FP_h2ksV4zEJHFC_KXK6sSZ5iz5yhTFZcPnH1HS_RvZb2Nr-UXYQ1H316UMoj6eRv6wMn3wHX842B5WVfPHVnJ74)

#### Vierte

![](https://lh7-us.googleusercontent.com/myhi9y2sCvS5ZFkIJa5ysLbu7p0X6CYqbiuJ3sQ5-O-2QWlfAseunjwhXK0kakmAofplm0zmh_H1Np7bA559w0-jdurQUsZwYF9CyKYSKSeGnQaIit0HQ5iN-3Xv8CIC-5nk6mMj3JTDS97SlzbsOFE)

#### Fünfte

![](https://lh7-us.googleusercontent.com/c-5iaUhhx0swH-mQfXE5Mdwe4J0skGt7mst4kJdOpjL3Uat329TZmKM5Af-lGQWmcmBht-ib_aUj4dVG7GaUAHHULjly3jxsR8MJNnLDcu5eZB268Vy-dXPxHmkVB8dMZTRhU5SUB59AREurJlW-K6o)

Das letzte Symbol sollte leer sein, da es kein Dokument oder keine Informationen enthält.

Sobald Sie alle erforderlichen Knoten im Datenfluss hinzugefügt haben, drücken Sie diese Schaltfläche, um den Datenfluss zu aktivieren (nachdem Sie den Datenfluss gespeichert haben, indem Sie auf das Festplattensymbol drücken).

![](https://lh7-us.googleusercontent.com/WIecHktG7e5dbVScLbR8hUcZUdCEWXBW4xWDEuq0IqTMmguA_Ih_oRymvpk6CzowWFG5TTSCPIH-68ICnPSOPxeZksc-n4bmpvuH8dvHuHFU1DlppGRno3PKjCSJiK12p9bNlo_9cN2t9Ps3nbqF3xE)
