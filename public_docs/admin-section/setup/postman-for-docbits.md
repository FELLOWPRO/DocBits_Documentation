# Postman für DocBits

Dieser Leitfaden zeigt Ihnen, wie Sie HTTP-Anfragen an Ihre DocBits-Organisation über Postman senden können. Es ist einfach zu bedienen und sehr nützlich für Organisationsadministratoren.

## Einrichtung

Laden Sie zunächst Postman auf Ihr System herunter und melden Sie sich an/registrieren Sie sich.

Befolgen Sie nun diesen Schritt-für-Schritt-Leitfaden, um zu lernen, wie HTTP-Anfragen in Postman funktionieren.

Autorisierung in Postman

Bevor Sie Ihre HTTP-Anfragen erstellen können, müssen Sie Ihren API-Schlüssel von DocBits eingeben, um sie zu autorisieren.

* Klicken Sie auf den Tab \`Authorization\` und wählen Sie \`API Key\` als Autorisierungstyp.

![](https://lh7-us.googleusercontent.com/L3GaBZJvReeINaKbkq3VYQ9UHTBoKUA3nJkfyLqk61q5xaOJnmMLhbrEbgUgLEyYRkewHuLIAVzoYCZ6quHq0pwx\_69FEYJjzYllivB8WzdAtTFSrzl8VeFthbMsEB9sGjcGlVN38DXEXUwuNEPL6hg)

* Füllen Sie die Werte aus. Geben Sie "X-API-key" in das Feld \`Key\` ein und Ihren API-Schlüssel als Wert (zu finden im DocBits-Einstellungsmenü unter Integration). Wählen Sie Hinzufügen zu \`Header\`.

&#x20;

* Es sollte so aussehen:

![](https://lh7-us.googleusercontent.com/SmNfci4z8ECTeXzFPE9YQ8nCzCRHglc\_7RR1cN8a8F7KvYWjJcBnY5wpl7q0AV8bfNLkMk8F4F4aw8j4xMK50HJweBRBPo8EasTn-FG-fmlUJQ41aUX-dvTeWP\_xJQThi8A6EwJl3qIc-Dw1B5W9fVE)

### DocBits API

Verfügbar unter https://api.polydocs.io

* Klicken Sie oben rechts auf Autorisieren

![](https://lh7-us.googleusercontent.com/kuztHpkmRWlOYSU27r97KH15SJHPF\_hn\_eX3C1DYLVYCwMHXfLjYSyFubUCvlQiBt5q3xY0XBPmkcP6AnKF2C0Mdtx3tg\_dU\_qxqAmI6axYIsXR36\_YBz6j455K3-c2SBu4YzmYIXq8VXQxzgL-0j90)

* Geben Sie Ihren API-Schlüssel ein und bestätigen Sie durch Klicken auf \`Authorize\`

![](https://lh7-us.googleusercontent.com/zLhgpdjMnxqNBdjgtDxFEKglICIZul7dgmfFFm2hSnsDQ-HsZHRKRikZ0lcanGYkkZj4waC85mEUFO951ydVnY\_\_m\_TrMrsK3vrDv9FKL-adgWL4lJqp3cSxPeClBm9IHG2cXinRsv12xTeh3psQfO4)

### Erstellen eines neuen Workspace in Postman

* Klicken Sie auf Workspaces und erstellen Sie einen neuen Workspace (Sie können ihn benennen, wie Sie möchten)

![](https://lh7-us.googleusercontent.com/3rZw7jhOgVpkZuer58fPEKqDspJjK3S1lp3XpQuvE4c9212a0ALB-p7oLRwPqEbj10MpoCWsb7V9fPqiAdVvigE00x9mN5-lHFXZVVxlkeroBJd2ratgkJVJDM4LJkUJsycyl6tnFKazcFPY-vWtH2Q)

* Wählen Sie die Sichtbarkeit aus, die bestimmt, wer auf diesen Workspace zugreifen kann.

![](https://lh7-us.googleusercontent.com/ZajvDtMvfM5J\_Go3n\_PgzD3RXTMQAlST8\_3WnsTQ4-iw7e0QdAa3wqFk7Y0gt78IJVjNTN-5E72c1127CpXJWb8WbfDolxENLqxg5VZLPEK7-hxsNwbAyMceSHfeVy6v-b9QT0kFwnMibWndEAJ2lXA)

* Nachdem Sie Ihre Auswahl getroffen und auf \`Workspace erstellen\` geklickt haben, wählen Sie auf der linken Seite der Anwendung Sammlungen aus und erstellen Sie eine neue Sammlung für Ihre HTTP-Anfragen, indem Sie auf \`+\` klicken.

![](https://lh7-us.googleusercontent.com/mbC5t86vaB2G7FQp-40XN-SHc019LKitfUeXRzbcG4HpNai5FPapShx9swHX3mz0va8QFsUQiYn-bhjvER0XYOEDRJpI9x3wG4NgRZCd4beU1NyKJd86bSGubxVbRCtz8HkTDZd28Z7Ice3rmscFMMo)

In dieser Sammlung können Sie mehrere HTTP-Anfragen hinzufügen. Klicken Sie dazu auf die 3 Punkte der Sammlung und wählen Sie \`Anfrage hinzufügen\`.

![](https://lh7-us.googleusercontent.com/S5W75clJz7JqoIWPbKBjrJqpTAwjS51Pu4dTU160Q7i6oW-HPnb7aN8WRK2AyAb6-HEqTYMZTy9563P0sq53MAjGpVg1JivZX2ATHa6GeFbTX2UCjud7ot8Y\_ksBuUbUfyEfxIDziV8TN3zDfX9Se58)

## Beispiel für die Methode "GET"

Die GET-Methode ist sehr nützlich, um Informationen über Benutzer, Unterorganisationen, verarbeitete Dokumente und vieles mehr zu erhalten.

* Wählen Sie die GET-Methode in Ihrer HTTP-Anfrage.
* Autorisieren Sie sich wie oben beschrieben.
* Öffnen Sie https://api.polydocs.io und fügen Sie den Pfad der Funktion hinter die Polydocs-URL ein. Zum Beispiel:

![](https://lh7-us.googleusercontent.com/pIdgyqP7g1UwZbY5yaz1KAnKe\_ESs\_kQyiWAXXM-ukRKakS\_\_OL\_LS9J-07hZnZDf8QqtoN\_lKyuhvOIIIF-4Wp0dkofZYQwXZ0hu2RM0YogRxJah-zf8W\_cDNFf8xsec1tYIsfe0SpBuvdCG4WHMU0)

* Fügen Sie diesen Link nun in das Textfeld neben der GET-Methode in Postman ein.

Klicken Sie auf \`Send\` und Sie sollten alle Informationen über jeden Benutzer in Ihrer Organisation erhalten.

## Beispiel für die Methode "POST"

Die POST-Methode wird normalerweise verwendet, um Benutzer oder Organisationen zu erstellen, zum Beispiel. Diese Methode fügt Informationen in die Datenbank ein.

Benutzer erstellen

* Wählen Sie die POST-Methode aus.
* Autorisieren Sie sich wie oben beschrieben.
* Öffnen Sie https://api.polydocs.io und fügen Sie den Pfad der Funktion hinter die Polydocs-URL ein. In diesem Fall:

![](https://lh7-us.googleusercontent.com/Gwabl4pN0k0NanHsFOzJj9s2H7ExS-JcWr-Y4EW0FLUYHfnaOZoMWvldJ6yDI33p\_DThVx0Rd5bi59XdOK11l1knc5rd-E5HXMw6v5E3qvHvKVWHlp21S728SVye6KU2W5ZeXtCIOzxBAcMlA2UNFfQ)

* Fügen Sie diesen Link nun in das Textfeld neben der POST-Methode in Postman ein.
* Wählen Sie den Tab \`Body\` in Ihrer HTTP-Anfrage aus und geben Sie die Schlüssel und Werte für jede Anmeldeinformation ein, die einen roten Stern neben ihrem Namen hat.

Wenn Sie fertig sind, sollte es so aussehen:

![](https://lh7-us.googleusercontent.com/lSExzZSbTcSRvuLDw0HNYE62yI7xs0eUewKuOcABCGYfsRBRbGz1lJxopR4QdUEoniCnZ83FKpz-AHLORP5cXGPrPhgouzE6zO920jA7A3r-Y14wY\_Gc3C98R2fcxXsWRMcle9qT981YWhCnjlUukPE)

Wenn Sie ein Admin-Konto erstellen möchten, setzen Sie den Wert von \`is\_admin\` auf true.

&#x20;Klicken Sie abschließend auf \`Send\` und Sie können alle Anmeldeinformationen, die Sie in der Antwort festgelegt haben, unten sehen. Dies bedeutet, dass der Benutzer erstellt wurde.
### Dokument hochladen

Sie können auch die POST-Methode verwenden, um ein Dokument in DocBits hochzuladen.

* Wählen Sie die POST-Methode aus.
* Autorisieren Sie sich wie oben beschrieben.
* Öffnen Sie https://api.polydocs.io und fügen Sie den Pfad der Funktion hinter die Polydocs-URL hinzu.&#x20;

In diesem Fall:

![](https://lh7-us.googleusercontent.com/-EwhMeH\_WXYVmMKus1-IZKLZNyTcYktcf\_YUT\_m2nfStfKXuBxKBb1MZfUIQCN4ZxNKQkNhvO\_pgnt1EUhNB34qG5AOe4wM0OxGRMQsV9a8h0XUgabqq8mLQhza\_AE7gxBetmb9bJmaWBQqEXrWT0VI)

* Fügen Sie diesen Link nun in das Textfeld neben der POST-Methode in Postman ein.
* Wählen Sie den `Body`-Tab in Ihrer HTTP-Anfrage und wählen Sie `form-data`.

![](https://lh7-us.googleusercontent.com/TNrKlyorn\_5YrIu5r4vcfyYgAnfhsl-SRVqWg9RoN0X1pUjXtn6J0EI7aeQ-oc2ZtFeTj8POcMXy6CwXzI1jhv-ufb2u7d80SC-lbGXmnx\_jVDunAbRw1jqAsB4PPsEzcFIOPeH5PJZvytUW2kIDYZ4)

![](https://lh7-us.googleusercontent.com/scAJpTSCqYSKYNNGPIrEsL0zDJIa7Dhe9tpqv\_zDjdLyAydugzdGA1s93njbFOOVbVbQf7oDEtRc14Kt4p1TXX8A--WjvRgeXWsAxDNWdrCN2-QDeya6-FFEG4\_-dhYgrj4yrVYllJs8eZsUgKOPvzo)

Geben Sie die Datei in das `KEY`-Feld ein, wo Sie das versteckte Dropdown-Menü Datei finden. Wählen Sie `File` und wechseln Sie zum `VALUE`-Feld, wo Sie Ihre Datei auswählen können, indem Sie auf `Select Files` klicken.

Wenn Sie auf `Send` klicken, sollten Sie in der Antwort "success": true sehen.

Es sollte so aussehen:

![](https://lh7-us.googleusercontent.com/hNtG\_uTWgxww7iOmHLhnDqdrTlHCI1rk31LozG4l2DLPqxzSn9HoKn8CQIjeBgJLV4bxrGCjWOMRykJ3qBdZLYwxrZJGq\_S3tjVwSZmGTiMgVoqM97TTQjmW8CegEL2FV309NBmV0Fv\_vciSdQRFiOI)

## Beispiel für die "DELETE"-Methode

Die DELETE-Methode wird verwendet, um beispielsweise Benutzer, Organisationen usw. zu löschen.

* Wählen Sie die DELETE-Methode aus.
* Autorisieren Sie sich wie oben beschrieben.
* Öffnen Sie https://api.polydocs.io und fügen Sie den Pfad der Funktion hinter die Polydocs-URL hinzu.

&#x20;Zum Beispiel:

![](https://lh7-us.googleusercontent.com/-QqSVIELl1IkxYK\_gGDa7nIv\_B1IvO3OjT3Ge6bAXwPl6jVDETuzXwtYJdRSmqLEP2d6B0L6MuwZvgJpI968pzp1APmJmuQ\_qlqYgZZhesocYCJVMCHhIZAKmlvMybUkUGXYZtySrnEbRTwWTritvKo)

* Fügen Sie diesen Link nun in das Textfeld neben der DELETE-Methode in Postman ein.
* Ersetzen Sie das {user\_id} am Ende der URL durch die tatsächliche Benutzer-ID, die Sie löschen möchten. (Sie können die user\_id mit der GET-Methode erhalten).
* Wenn Sie die user\_id in der URL enthalten haben, müssen Sie keinen Body-Schlüssel und -Wert hinzufügen.
* Wenn Sie auf `Send` klicken, sollten Sie in der Antwort "success": true sehen.

&#x20;Es sollte so aussehen:

![](https://lh7-us.googleusercontent.com/X8WNtsC9v7jqDIiaVhauJUgZK0yTC1GVz9rBptdiCxyLUiEEfbpIoYHpK7NvlDMTkhgiPyBb22H9GOfDdvmL-dakouTjuRDPwX4YX0Jz5IIo6eHu-wnw1S4jJd5ylHyffUXWKwX6ovDnp\_2WEAtSha4)

## Beispiel für die "PUT"-Methode

Die PUT-Methode wird hauptsächlich verwendet, um Benutzer- oder Organisationsdaten zu aktualisieren. Sie ist sehr einfach zu verstehen und zu verwenden.

* Wählen Sie die PUT-Methode aus.
* Autorisieren Sie sich wie oben beschrieben.
* Öffnen Sie https://api.polydocs.io und fügen Sie den Pfad der Funktion hinter die Polydocs-URL hinzu.

&#x20;Zum Beispiel:

![](https://lh7-us.googleusercontent.com/tC3qtPbFb1GsK6dBmB5Jrv5HqFOYLxNR1XB0PEuA8ipkHnH2ZQ6xrrkImNgbGSMoA6aAGvLr6K3cI4u\_qM96BOvR7AnQzmX17HBMBneNpLBc6RIzspfTYgrCWSj0fSE9mSWLIex3hc\_R-m-PI6zT6Rs)

* Fügen Sie diesen Link nun in das Textfeld neben der PUT-Methode in Postman ein.
* Ersetzen Sie das {user\_id} am Ende der URL durch die tatsächliche Benutzer-ID, die Sie löschen möchten. (Sie können die user\_id mit der GET-Methode erhalten).

## Ändern der E-Mail-Adresse eines Benutzers

* Geben Sie im Body "email" als Schlüssel und die neue E-Mail-Adresse als Wert ein.
* Drücken Sie dann einfach auf `Send` und Sie sollten in der Antwort "success" sehen.
