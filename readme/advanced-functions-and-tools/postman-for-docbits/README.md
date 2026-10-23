# Postman voor DocBits

In deze handleiding ziet u hoe u HTTP-verzoeken kunt indienen bij uw DocBits-organisatie via Postman. Het is gemakkelijk te gebruiken en zeer nuttig voor organisatiebeheerders.

## Configuratie

Download eerst Postman naar uw systeem en meld u aan/registreer.

Volg nu deze stapsgewijze handleiding om te leren hoe HTTP-verzoeken werken in Postman.

Authorization in Postman

Voordat u uw HTTP-verzoeken kunt maken, moet u uw API-sleutel uit DocBits invoeren om deze te autoriseren.

* Klik op het tabblad \`Authorization\` en kies \`API Key\` als autorisatietype.

![Postman-verzoektabs met het tabblad Authorization geselecteerd en de lijst Auth Type open met API Key tussen Bearer Token, Basic Auth en OAuth 2.0](https://lh7-us.googleusercontent.com/L3GaBZJvReeINaKbkq3VYQ9UHTBoKUA3nJkfyLqk61q5xaOJnmMLhbrEbgUgLEyYRkewHuLIAVzoYCZ6quHq0pwx_69FEYJjzYllivB8WzdAtTFSrzl8VeFthbMsEB9sGjcGlVN38DXEXUwuNEPL6hg)

* Vul de waarden in. Voer “X-API-key” in het veld \`Key\` in en uw API-sleutel als waarde (te vinden in het menu DocBits Instellingen onder Integratie). Selecteer Toevoegen aan \`Header\`.
* Het zou er zo uit moeten zien:

![Postman-tabblad Authorization met Type ingesteld op API Key, het veld Key ingesteld op X-API-key en Add to Header geselecteerd in de vervolgkeuzelijst](https://lh7-us.googleusercontent.com/SmNfci4z8ECTeXzFPE9YQ8nCzCRHglc_7RR1cN8a8F7KvYWjJcBnY5wpl7q0AV8bfNLkMk8F4F4aw8j4xMK50HJweBRBPo8EasTn-FG-fmlUJQ41aUX-dvTeWP_xJQThi8A6EwJl3qIc-Dw1B5W9fVE)

### DocBits-API

Available at https://api.polydocs.io

* Klik rechtsboven op Autoriseren

![Swagger-pagina van de DocBits API met de gemarkeerde knop Authorize in de rechterbovenhoek](https://lh7-us.googleusercontent.com/kuztHpkmRWlOYSU27r97KH15SJHPF_hn_eX3C1DYLVYCwMHXfLjYSyFubUCvlQiBt5q3xY0XBPmkcP6AnKF2C0Mdtx3tg_dU_qxqAmI6axYIsXR36_YBz6j455K3-c2SBu4YzmYIXq8VXQxzgL-0j90)

* Voer uw API-sleutel in en bevestig door op \`Authorize\` te klikken

![Dialoog Available authorizations met het schema APIKeyHeader (apiKey), Name X-API-KEY, In header en een leeg veld Value](https://lh7-us.googleusercontent.com/zLhgpdjMnxqNBdjgtDxFEKglICIZul7dgmfFFm2hSnsDQ-HsZHRKRikZ0lcanGYkkZj4waC85mEUFO951ydVnY__m_TrMrsK3vrDv9FKL-adgWL4lJqp3cSxPeClBm9IHG2cXinRsv12xTeh3psQfO4)

### Een nieuwe werkruimte in Postman maken

* Klik op Werkruimten en maak een nieuwe werkruimte (je kunt deze een naam geven zoals je wilt).

![Postman-startscherm met het geopende menu Workspaces met My Workspace, More workspaces en een koppeling View all workspaces](https://lh7-us.googleusercontent.com/3rZw7jhOgVpkZuer58fPEKqDspJjK3S1lp3XpQuvE4c9212a0ALB-p7oLRwPqEbj10MpoCWsb7V9fPqiAdVvigE00x9mN5-lHFXZVVxlkeroBJd2ratgkJVJDM4LJkUJsycyl6tnFKazcFPY-vWtH2Q)

* U moet de zichtbaarheid selecteren die bepaalt wie toegang heeft tot deze werkruimte.

![Dialoogvenster Create workspace met de velden Name en Summary, de zichtbaarheidsopties Personal, Private, Team, Partner en Public, plus de knoppen Create Workspace en Cancel](https://lh7-us.googleusercontent.com/ZajvDtMvfM5J_Go3n_PgzD3RXTMQAlST8_3WnsTQ4-iw7e0QdAa3wqFk7Y0gt78IJVjNTN-5E72c1127CpXJWb8WbfDolxENLqxg5VZLPEK7-hxsNwbAyMceSHfeVy6v-b9QT0kFwnMibWndEAJ2lXA)

* Nadat u uw selectie heeft gemaakt en op \`Create Workspace\` heeft geklikt, selecteert u Collecties aan de linkerkant van de applicatie en maakt u een nieuwe collectie voor uw HTTP-aanvragen door op \`+\` te klikken.

![Postman-zijbalk met het actieve tabblad Collections dat New Collection toont en een pop-up Create new collection met een plusschakelaar](https://lh7-us.googleusercontent.com/mbC5t86vaB2G7FQp-40XN-SHc019LKitfUeXRzbcG4HpNai5FPapShx9swHX3mz0va8QFsUQiYn-bhjvER0XYOEDRJpI9x3wG4NgRZCd4beU1NyKJd86bSGubxVbRCtz8HkTDZd28Z7Ice3rmscFMMo)

In deze verzameling kunt u meerdere HTTP-verzoeken toevoegen. Om dit te doen, klikt u op de 3 punten van de verzameling en selecteert u \`Add request\`.

![Geopend Postman-collectiemenu met de acties Share, Move, Run collection, Edit, Add request, Add folder en Monitor collection](https://lh7-us.googleusercontent.com/S5W75clJz7JqoIWPbKBjrJqpTAwjS51Pu4dTU160Q7i6oW-HPnb7aN8WRK2AyAb6-HEqTYMZTy9563P0sq53MAjGpVg1JivZX2ATHa6GeFbTX2UCjud7ot8Y_ksBuUbUfyEfxIDziV8TN3zDfX9Se58)

## Voorbeeld van de methode "GET"

De GET-methode is erg handig voor het verkrijgen van informatie over gebruikers, suborganisaties, verwerkte documenten en nog veel meer.

* Kies de GET-methode in uw HTTP-verzoek.
* Autoriseer uzelf zoals hierboven beschreven.
* Open https://api.polydocs.io en voeg het functiepad toe aan de Polydocs URL. Bijvoorbeeld:

![Swagger-pagina voor het endpoint GET /orgs/get_users met de gebruikersroute van de DocBits-API](https://lh7-us.googleusercontent.com/pIdgyqP7g1UwZbY5yaz1KAnKe_ESs_kQyiWAXXM-ukRKakS__OL_LS9J-07hZnZDf8QqtoN_lKyuhvOIIIF-4Wp0dkofZYQwXZ0hu2RM0YogRxJah-zf8W_cDNFf8xsec1tYIsfe0SpBuvdCG4WHMU0)

* Plak nu deze link in het tekstvak naast de GET methode in Postman.

Klik op \`Send\` en u ontvangt alle informatie over elke gebruiker in uw organisatie.

## Voorbeeld van de methode "POST"

De methode POST wordt meestal gebruikt om bijvoorbeeld gebruikers of organisaties aan te maken. Met deze methode wordt informatie in de database ingevoegd.

Create User

* Select the POST Method.
* Autoriseer uzelf zoals hierboven beschreven
* Open https://api.polydocs.io en voeg het functiepad toe aan de Polydocs URL. In dit geval:

![Swagger-pagina voor de POST create user request body met de verplichte velden first_name, last_name, email, password en is_admin](https://lh7-us.googleusercontent.com/Gwabl4pN0k0NanHsFOzJj9s2H7ExS-JcWr-Y4EW0FLUYHfnaOZoMWvldJ6yDI33p_DThVx0Rd5bi59XdOK11l1knc5rd-E5HXMw6v5E3qvHvKVWHlp21S728SVye6KU2W5ZeXtCIOzxBAcMlA2UNFfQ)

* Plak nu deze link in het tekstvak naast de POST methode in Postman.
* Selecteer het tabblad \`Body\` in uw HTTP-verzoek en voer de sleutels en waarden in voor elke inloggegevens met een rode asterisk naast de naam.

Als je klaar bent, zou het er zo uit moeten zien:

![Postman-tabblad Body met form-data geselecteerd en sleutel-waarderegels voor firstname, lastname, email, password en is_admin](https://lh7-us.googleusercontent.com/lSExzZSbTcSRvuLDw0HNYE62yI7xs0eUewKuOcABCGYfsRBRbGz1lJxopR4QdUEoniCnZ83FKpz-AHLORP5cXGPrPhgouzE6zO920jA7A3r-Y14wY_Gc3C98R2fcxXsWRMcle9qT981YWhCnjlUukPE)

Als u een beheerdersaccount wilt maken, stelt u de waarde \`is\_admin\` in op true.

Klik ten slotte op \`Send\` en u kunt alle inloggegevens zien die u heeft ingesteld in het onderstaande antwoord. Dit betekent dat de gebruiker is aangemaakt.

### Document uploaden

U kunt ook de methode POST gebruiken om een document naar DocBits te uploaden.

* Select the POST Method.
* Autoriseer uzelf zoals hierboven beschreven.
* Open https://api.polydocs.io en voeg het functiepad toe aan de Polydocs URL.

In dit geval:

![Swagger-pagina voor het endpoint POST /document/process met parameters als source, priority en sub_org_id en selectievakjes Send empty value](https://lh7-us.googleusercontent.com/-EwhMeH_WXYVmMKus1-IZKLZNyTcYktcf_YUT_m2nfStfKXuBxKBb1MZfUIQCN4ZxNKQkNhvO_pgnt1EUhNB34qG5AOe4wM0OxGRMQsV9a8h0XUgabqq8mLQhza_AE7gxBetmb9bJmaWBQqEXrWT0VI)

* Plak nu deze link in het tekstvak naast de POST methode in Postman.
* Selecteer het tabblad \`Body\` in uw HTTP-verzoek en kies \`form-data\`

![Postman-verzoek naar het endpoint /document/process met het tabblad Body open, form-data geselecteerd en een lege bestandsleutelrij](https://lh7-us.googleusercontent.com/TNrKlyorn_5YrIu5r4vcfyYgAnfhsl-SRVqWg9RoN0X1pUjXtn6J0EI7aeQ-oc2ZtFeTj8POcMXy6CwXzI1jhv-ufb2u7d80SC-lbGXmnx_jVDunAbRw1jqAsB4PPsEzcFIOPeH5PJZvytUW2kIDYZ4)

![Postman-verzoek naar https://api.polydocs.io/document/process met form-data geselecteerd en de sleutel file ingesteld op de waarde Mango-invoice.pdf](https://lh7-us.googleusercontent.com/scAJpTSCqYSKYNNGPIrEsL0zDJIa7Dhe9tpqv_zDjdLyAydugzdGA1s93njbFOOVbVbQf7oDEtRc14Kt4p1TXX8A--WjvRgeXWsAxDNWdrCN2-QDeya6-FFEG4_-dhYgrj4yrVYllJs8eZsUgKOPvzo)

Voer het bestand in het veld \`KEY\` in, waar u de vervolgkeuzelijst met verborgen bestanden vindt. Selecteer \`File\` en ga naar het veld \`VALUE\` waar u uw bestand kunt selecteren door op \`Select Files\` te klikken.

Wanneer u op \`Send\` klikt, zou u “success”: true in het antwoord moeten zien.

Het zou er zo uit moeten zien:

![Postman-antwoord voor het geüploade document met status 200 OK en de JSON-body met success true, een doc_id en de bestandsnaam Mango_invoice.pdf](https://lh7-us.googleusercontent.com/hNtG_uTWgxww7iOmHLhnDqdrTlHCI1rk31LozG4l2DLPqxzSn9HoKn8CQIjeBgJLV4bxrGCjWOMRykJ3qBdZLYwxrZJGq_S3tjVwSZmGTiMgVoqM97TTQjmW8CegEL2FV309NBmV0Fv_vciSdQRFiOI)

## Voorbeeld van de methode "DELETE"

De methode DELETE wordt gebruikt om bijvoorbeeld gebruikers, organisaties enzovoort te verwijderen.

* Select the DELETE Method
* Autoriseer uzelf zoals hierboven beschreven.
* Open https://api.polydocs.io en voeg het functiepad toe aan de Polydocs URL.

For example:

![Swagger-pagina voor het endpoint DELETE /users/delete/{user_id} van de DocBits-API](https://lh7-us.googleusercontent.com/-QqSVIELl1IkxYK_gGDa7nIv_B1IvO3OjT3Ge6bAXwPl6jVDETuzXwtYJdRSmqLEP2d6B0L6MuwZvgJpI968pzp1APmJmuQ_qlqYgZZhesocYCJVMCHhIZAKmlvMybUkUGXYZtySrnEbRTwWTritvKo)

* Plak nu deze link in het tekstvak naast de DELETE methode in Postman.
* Vervang de {user\_id} aan het einde van URL door de daadwerkelijke gebruiker ID die u wilt verwijderen. (Je kunt de user\_id verkrijgen met behulp van de GET-methode).
* Als u de user\_id in de URL hebt opgenomen, hoeft u er geen hoofdtekst en waarde voor toe te voegen.
* Wanneer u op \`Send\` klikt, zou u “success”: true in het antwoord moeten zien.

Het zou er zo uit moeten zien:

![Postman-verzoek Delete User met Status 200 OK in het antwoordpaneel na het verzenden van de DELETE-aanroep](https://lh7-us.googleusercontent.com/X8WNtsC9v7jqDIiaVhauJUgZK0yTC1GVz9rBptdiCxyLUiEEfbpIoYHpK7NvlDMTkhgiPyBb22H9GOfDdvmL-dakouTjuRDPwX4YX0Jz5IIo6eHu-wnw1S4jJd5ylHyffUXWKwX6ovDnp_2WEAtSha4)

## Voorbeeld van de methode "PUT"

De PUT-methode wordt voornamelijk gebruikt om gebruikers- of organisatiegegevens bij te werken. Het is heel gemakkelijk te begrijpen en te gebruiken.

* Select the PUT Method.
* Autoriseer uzelf zoals hierboven beschreven.
* Open https://api.polydocs.io en voeg het functiepad toe aan de Polydocs URL.

For example:

![Swagger-pagina voor het endpoint PUT /users/update/{user_id} met de request-body-velden first_name, last_name en email van Update User](https://lh7-us.googleusercontent.com/tC3qtPbFb1GsK6dBmB5Jrv5HqFOYLxNR1XB0PEuA8ipkHnH2ZQ6xrrkImNgbGSMoA6aAGvLr6K3cI4u_qM96BOvR7AnQzmX17HBMBneNpLBc6RIzspfTYgrCWSj0fSE9mSWLIex3hc_R-m-PI6zT6Rs)

* Plak nu deze link in het tekstvak naast de PUT methode in Postman.
* Vervang de {user\_id} aan het einde van URL door de daadwerkelijke gebruiker ID die u wilt verwijderen. (Je kunt de user\_id verkrijgen met behulp van de GET-methode).

## E-mailadres van een gebruiker wijzigen

* Voer in de hoofdtekst “email” in als sleutel en het nieuwe e-mailadres als waarde.
* Druk vervolgens gewoon op \`Send\` en u zou “success” in het antwoord moeten zien.
