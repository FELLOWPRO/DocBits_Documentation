# Postman für DocBits

Diese Anleitung zeigt, wie Sie mit Postman HTTP-Anfragen an Ihre DocBits-Organisation senden. Das ist besonders für Organisationsadministratoren hilfreich.

## Einrichtung

Laden Sie zunächst Postman herunter und melden Sie sich an oder registrieren Sie sich.

Die folgenden Schritte erläutern, wie Sie HTTP-Anfragen in Postman erstellen und ausführen.

Autorisierung in Postman

Tragen Sie vor dem Senden der HTTP-Anfragen Ihren DocBits-API-Schlüssel ein, um die Anfragen zu autorisieren.

* Öffnen Sie die Registerkarte \`Authorization\` und wählen Sie als Autorisierungstyp \`API Key\`.

![](https://lh7-us.googleusercontent.com/L3GaBZJvReeINaKbkq3VYQ9UHTBoKUA3nJkfyLqk61q5xaOJnmMLhbrEbgUgLEyYRkewHuLIAVzoYCZ6quHq0pwx_69FEYJjzYllivB8WzdAtTFSrzl8VeFthbMsEB9sGjcGlVN38DXEXUwuNEPL6hg)

* Tragen Sie im Feld \`Key\` den Wert „X-API-key“ und als Wert Ihren API-Schlüssel ein. Sie finden ihn in den DocBits-Einstellungen unter **Integration**. Wählen Sie bei **Add to** die Option \`Header\`.
* Das Ergebnis sollte so aussehen:

![](https://lh7-us.googleusercontent.com/SmNfci4z8ECTeXzFPE9YQ8nCzCRHglc_7RR1cN8a8F7KvYWjJcBnY5wpl7q0AV8bfNLkMk8F4F4aw8j4xMK50HJweBRBPo8EasTn-FG-fmlUJQ41aUX-dvTeWP_xJQThi8A6EwJl3qIc-Dw1B5W9fVE)

### DocBits API

Verfügbar unter https://api.polydocs.io

* Klicken Sie oben rechts auf **Authorize**.

![](https://lh7-us.googleusercontent.com/kuztHpkmRWlOYSU27r97KH15SJHPF_hn_eX3C1DYLVYCwMHXfLjYSyFubUCvlQiBt5q3xY0XBPmkcP6AnKF2C0Mdtx3tg_dU_qxqAmI6axYIsXR36_YBz6j455K3-c2SBu4YzmYIXq8VXQxzgL-0j90)

* Geben Sie Ihren API-Schlüssel ein und bestätigen Sie mit \`Authorize\`.

![](https://lh7-us.googleusercontent.com/zLhgpdjMnxqNBdjgtDxFEKglICIZul7dgmfFFm2hSnsDQ-HsZHRKRikZ0lcanGYkkZj4waC85mEUFO951ydVnY__m_TrMrsK3vrDv9FKL-adgWL4lJqp3cSxPeClBm9IHG2cXinRsv12xTeh3psQfO4)

### Neuen Arbeitsbereich in Postman erstellen

* Öffnen Sie **Workspaces** und erstellen Sie einen neuen Arbeitsbereich mit einem Namen Ihrer Wahl.

![](https://lh7-us.googleusercontent.com/3rZw7jhOgVpkZuer58fPEKqDspJjK3S1lp3XpQuvE4c9212a0ALB-p7oLRwPqEbj10MpoCWsb7V9fPqiAdVvigE00x9mN5-lHFXZVVxlkeroBJd2ratgkJVJDM4LJkUJsycyl6tnFKazcFPY-vWtH2Q)

* Legen Sie über die Sichtbarkeit fest, wer auf diesen Arbeitsbereich zugreifen darf.

![](https://lh7-us.googleusercontent.com/ZajvDtMvfM5J_Go3n_PgzD3RXTMQAlST8_3WnsTQ4-iw7e0QdAa3wqFk7Y0gt78IJVjNTN-5E72c1127CpXJWb8WbfDolxENLqxg5VZLPEK7-hxsNwbAyMceSHfeVy6v-b9QT0kFwnMibWndEAJ2lXA)

* Klicken Sie nach Ihrer Auswahl auf \`Create Workspace\`. Wählen Sie anschließend links **Collections** und erstellen Sie mit \`+\` eine neue Sammlung für Ihre HTTP-Anfragen.

![](https://lh7-us.googleusercontent.com/mbC5t86vaB2G7FQp-40XN-SHc019LKitfUeXRzbcG4HpNai5FPapShx9swHX3mz0va8QFsUQiYn-bhjvER0XYOEDRJpI9x3wG4NgRZCd4beU1NyKJd86bSGubxVbRCtz8HkTDZd28Z7Ice3rmscFMMo)

Sie können dieser Sammlung mehrere HTTP-Anfragen hinzufügen. Öffnen Sie dazu das Drei-Punkte-Menü der Sammlung und wählen Sie \`Add request\`.

![](https://lh7-us.googleusercontent.com/S5W75clJz7JqoIWPbKBjrJqpTAwjS51Pu4dTU160Q7i6oW-HPnb7aN8WRK2AyAb6-HEqTYMZTy9563P0sq53MAjGpVg1JivZX2ATHa6GeFbTX2UCjud7ot8Y_ksBuUbUfyEfxIDziV8TN3zDfX9Se58)

## Beispiel für die GET-Methode

Mit der GET-Methode rufen Sie Informationen ab, beispielsweise zu Benutzern, Unterorganisationen und verarbeiteten Dokumenten.

* Wählen Sie für Ihre HTTP-Anfrage die Methode **GET**.
* Richten Sie die Autorisierung wie oben beschrieben ein.
* Öffnen Sie https://api.polydocs.io und ergänzen Sie die Polydocs-URL um den Pfad der gewünschten Funktion. Beispiel:

![](https://lh7-us.googleusercontent.com/pIdgyqP7g1UwZbY5yaz1KAnKe_ESs_kQyiWAXXM-ukRKakS__OL_LS9J-07hZnZDf8QqtoN_lKyuhvOIIIF-4Wp0dkofZYQwXZ0hu2RM0YogRxJah-zf8W_cDNFf8xsec1tYIsfe0SpBuvdCG4WHMU0)

* Fügen Sie diese URL in Postman in das Textfeld neben der Methode **GET** ein.

Klicken Sie auf \`Send\`. Die Antwort sollte die Informationen zu allen Benutzern Ihrer Organisation enthalten.

## Beispiel für die POST-Methode

Mit der POST-Methode erstellen Sie beispielsweise Benutzer oder Organisationen. Dabei werden neue Daten in die Datenbank eingefügt.

Benutzer erstellen

* Wählen Sie die Methode **POST**.
* Richten Sie die Autorisierung wie oben beschrieben ein.
* Öffnen Sie https://api.polydocs.io und ergänzen Sie die Polydocs-URL um den Pfad der Funktion. In diesem Fall:

![](https://lh7-us.googleusercontent.com/Gwabl4pN0k0NanHsFOzJj9s2H7ExS-JcWr-Y4EW0FLUYHfnaOZoMWvldJ6yDI33p_DThVx0Rd5bi59XdOK11l1knc5rd-E5HXMw6v5E3qvHvKVWHlp21S728SVye6KU2W5ZeXtCIOzxBAcMlA2UNFfQ)

* Fügen Sie diese URL in Postman in das Textfeld neben der Methode **POST** ein.
* Öffnen Sie in Ihrer HTTP-Anfrage die Registerkarte \`Body\`. Tragen Sie für jedes mit einem roten Stern markierte Pflichtfeld den Schlüssel und den zugehörigen Wert ein.

Das Ergebnis sollte so aussehen:

![](https://lh7-us.googleusercontent.com/lSExzZSbTcSRvuLDw0HNYE62yI7xs0eUewKuOcABCGYfsRBRbGz1lJxopR4QdUEoniCnZ83FKpz-AHLORP5cXGPrPhgouzE6zO920jA7A3r-Y14wY_Gc3C98R2fcxXsWRMcle9qT981YWhCnjlUukPE)

Wenn Sie ein Administratorkonto erstellen möchten, setzen Sie \`is\_admin\` auf `true`.

Klicken Sie abschließend auf \`Send\`. Wenn der Benutzer erstellt wurde, zeigt die Antwort unten die von Ihnen festgelegten Kontodaten an.

### Dokument hochladen

Mit der POST-Methode können Sie auch ein Dokument in DocBits hochladen.

* Wählen Sie die Methode **POST**.
* Richten Sie die Autorisierung wie oben beschrieben ein.
* Öffnen Sie https://api.polydocs.io und ergänzen Sie die Polydocs-URL um den Pfad der gewünschten Funktion.

In diesem Fall:

![](https://lh7-us.googleusercontent.com/-EwhMeH_WXYVmMKus1-IZKLZNyTcYktcf_YUT_m2nfStfKXuBxKBb1MZfUIQCN4ZxNKQkNhvO_pgnt1EUhNB34qG5AOe4wM0OxGRMQsV9a8h0XUgabqq8mLQhza_AE7gxBetmb9bJmaWBQqEXrWT0VI)

* Fügen Sie diese URL in Postman in das Textfeld neben der Methode **POST** ein.
* Öffnen Sie in Ihrer HTTP-Anfrage die Registerkarte \`Body\` und wählen Sie \`form-data\`.

![](https://lh7-us.googleusercontent.com/TNrKlyorn_5YrIu5r4vcfyYgAnfhsl-SRVqWg9RoN0X1pUjXtn6J0EI7aeQ-oc2ZtFeTj8POcMXy6CwXzI1jhv-ufb2u7d80SC-lbGXmnx_jVDunAbRw1jqAsB4PPsEzcFIOPeH5PJZvytUW2kIDYZ4)

![](https://lh7-us.googleusercontent.com/scAJpTSCqYSKYNNGPIrEsL0zDJIa7Dhe9tpqv_zDjdLyAydugzdGA1s93njbFOOVbVbQf7oDEtRc14Kt4p1TXX8A--WjvRgeXWsAxDNWdrCN2-QDeya6-FFEG4_-dhYgrj4yrVYllJs8eZsUgKOPvzo)

Tragen Sie `file` in das Feld \`KEY\` ein. Wählen Sie im dort verfügbaren Auswahlmenü den Typ \`File\`. Wechseln Sie zum Feld \`VALUE\` und wählen Sie Ihre Datei über \`Select Files\` aus.

Nach einem Klick auf \`Send\` sollte die Antwort „success“: true enthalten.

Das Ergebnis sollte so aussehen:

![](https://lh7-us.googleusercontent.com/hNtG_uTWgxww7iOmHLhnDqdrTlHCI1rk31LozG4l2DLPqxzSn9HoKn8CQIjeBgJLV4bxrGCjWOMRykJ3qBdZLYwxrZJGq_S3tjVwSZmGTiMgVoqM97TTQjmW8CegEL2FV309NBmV0Fv_vciSdQRFiOI)

## Beispiel für die DELETE-Methode

Mit der DELETE-Methode löschen Sie beispielsweise Benutzer oder Organisationen.

* Wählen Sie die Methode **DELETE**.
* Richten Sie die Autorisierung wie oben beschrieben ein.
* Öffnen Sie https://api.polydocs.io und ergänzen Sie die Polydocs-URL um den Pfad der gewünschten Funktion.

Beispiel:

![](https://lh7-us.googleusercontent.com/-QqSVIELl1IkxYK_gGDa7nIv_B1IvO3OjT3Ge6bAXwPl6jVDETuzXwtYJdRSmqLEP2d6B0L6MuwZvgJpI968pzp1APmJmuQ_qlqYgZZhesocYCJVMCHhIZAKmlvMybUkUGXYZtySrnEbRTwWTritvKo)

* Fügen Sie diese URL in Postman in das Textfeld neben der Methode **DELETE** ein.
* Ersetzen Sie {user\_id} am Ende der URL durch die ID des Benutzers, den Sie löschen möchten. Sie können die user\_id mit der GET-Methode abrufen.
* Wenn Sie die user\_id in der URL angegeben haben, müssen Sie dafür keinen Schlüssel und Wert im Anfragetext ergänzen.
* Nach einem Klick auf \`Send\` sollte die Antwort „success“: true enthalten.

Das Ergebnis sollte so aussehen:

![](https://lh7-us.googleusercontent.com/X8WNtsC9v7jqDIiaVhauJUgZK0yTC1GVz9rBptdiCxyLUiEEfbpIoYHpK7NvlDMTkhgiPyBb22H9GOfDdvmL-dakouTjuRDPwX4YX0Jz5IIo6eHu-wnw1S4jJd5ylHyffUXWKwX6ovDnp_2WEAtSha4)

## Beispiel für die PUT-Methode

Mit der PUT-Methode aktualisieren Sie vor allem Benutzer- oder Organisationsdaten.

* Wählen Sie die Methode **PUT**.
* Richten Sie die Autorisierung wie oben beschrieben ein.
* Öffnen Sie https://api.polydocs.io und ergänzen Sie die Polydocs-URL um den Pfad der gewünschten Funktion.

Beispiel:

![](https://lh7-us.googleusercontent.com/tC3qtPbFb1GsK6dBmB5Jrv5HqFOYLxNR1XB0PEuA8ipkHnH2ZQ6xrrkImNgbGSMoA6aAGvLr6K3cI4u_qM96BOvR7AnQzmX17HBMBneNpLBc6RIzspfTYgrCWSj0fSE9mSWLIex3hc_R-m-PI6zT6Rs)

* Fügen Sie diese URL in Postman in das Textfeld neben der Methode **PUT** ein.
* Ersetzen Sie {user\_id} am Ende der URL durch die ID des Benutzers, dessen Daten Sie aktualisieren möchten. Sie können die user\_id mit der GET-Methode abrufen.

## E-Mail-Adresse eines Benutzers ändern

* Tragen Sie im Anfragetext „email“ als Schlüssel und die neue E-Mail-Adresse als Wert ein.
* Klicken Sie auf \`Send\`. Die Antwort sollte „success“ enthalten.
