# Postman para o DocBits

Este guia mostra como fazer pedidos HTTP à sua organização DocBits através do Postman e destina-se sobretudo aos administradores da organização.

## Configuração

Descarregue o Postman, instale-o no seu sistema e inicie sessão ou crie uma conta.

Siga os passos seguintes para aprender a utilizar pedidos HTTP no Postman.

Autorização no Postman

Antes de criar pedidos HTTP, introduza a sua chave API do DocBits para os autorizar.

* Clique no separador \`Authorization\` e escolha \`API Key\` como tipo de autorização.

![Separadores de pedido do Postman com o separador Authorization selecionado e a lista Auth Type aberta mostrando API Key entre Bearer Token, Basic Auth e OAuth 2.0](https://lh7-us.googleusercontent.com/L3GaBZJvReeINaKbkq3VYQ9UHTBoKUA3nJkfyLqk61q5xaOJnmMLhbrEbgUgLEyYRkewHuLIAVzoYCZ6quHq0pwx\_69FEYJjzYllivB8WzdAtTFSrzl8VeFthbMsEB9sGjcGlVN38DXEXUwuNEPL6hg)

* Em \`Key\`, introduza «X-API-key». No valor, introduza a chave API obtida em Configurações → Integração do DocBits. Em Add to, selecione \`Header\`.

&#x20;

* O resultado deve ser semelhante ao seguinte:

![Separador Authorization do Postman com Type definido como API Key, o campo Key definido como X-API-key e Add to Header selecionado na lista pendente](https://lh7-us.googleusercontent.com/SmNfci4z8ECTeXzFPE9YQ8nCzCRHglc\_7RR1cN8a8F7KvYWjJcBnY5wpl7q0AV8bfNLkMk8F4F4aw8j4xMK50HJweBRBPo8EasTn-FG-fmlUJQ41aUX-dvTeWP\_xJQThi8A6EwJl3qIc-Dw1B5W9fVE)

### API DocBits

Disponível em https://api.polydocs.io

* Clique em Authorize no canto superior direito.

![Página Swagger da API DocBits com o botão Authorize destacado no canto superior direito](https://lh7-us.googleusercontent.com/kuztHpkmRWlOYSU27r97KH15SJHPF\_hn\_eX3C1DYLVYCwMHXfLjYSyFubUCvlQiBt5q3xY0XBPmkcP6AnKF2C0Mdtx3tg\_dU\_qxqAmI6axYIsXR36\_YBz6j455K3-c2SBu4YzmYIXq8VXQxzgL-0j90)

* Introduza a chave API e confirme com \`Authorize\`.

![Diálogo Available authorizations com o esquema APIKeyHeader (apiKey), Name X-API-KEY, In header e um campo Value vazio](https://lh7-us.googleusercontent.com/zLhgpdjMnxqNBdjgtDxFEKglICIZul7dgmfFFm2hSnsDQ-HsZHRKRikZ0lcanGYkkZj4waC85mEUFO951ydVnY\_\_m\_TrMrsK3vrDv9FKL-adgWL4lJqp3cSxPeClBm9IHG2cXinRsv12xTeh3psQfO4)

### Criar uma área de trabalho no Postman

* Clique em Workspaces e crie uma área de trabalho com o nome que preferir.

![Ecrã inicial do Postman com o menu Workspaces aberto listando My Workspace, More workspaces e uma ligação View all workspaces](https://lh7-us.googleusercontent.com/3rZw7jhOgVpkZuer58fPEKqDspJjK3S1lp3XpQuvE4c9212a0ALB-p7oLRwPqEbj10MpoCWsb7V9fPqiAdVvigE00x9mN5-lHFXZVVxlkeroBJd2ratgkJVJDM4LJkUJsycyl6tnFKazcFPY-vWtH2Q)

* Selecione a visibilidade, que determina quem pode aceder à área de trabalho.

![Diálogo Create workspace com os campos Name e Summary, as opções de visibilidade Personal, Private, Team, Partner e Public, mais os botões Create Workspace e Cancel](https://lh7-us.googleusercontent.com/ZajvDtMvfM5J\_Go3n\_PgzD3RXTMQAlST8\_3WnsTQ4-iw7e0QdAa3wqFk7Y0gt78IJVjNTN-5E72c1127CpXJWb8WbfDolxENLqxg5VZLPEK7-hxsNwbAyMceSHfeVy6v-b9QT0kFwnMibWndEAJ2lXA)

* Clique em \`Create Workspace\`. Depois, selecione Collections à esquerda e crie uma coleção para os pedidos HTTP no botão \`+\`.

![Barra lateral do Postman com o separador Collections ativo a mostrar New Collection e um pop-up Create new collection com um botão de mais](https://lh7-us.googleusercontent.com/mbC5t86vaB2G7FQp-40XN-SHc019LKitfUeXRzbcG4HpNai5FPapShx9swHX3mz0va8QFsUQiYn-bhjvER0XYOEDRJpI9x3wG4NgRZCd4beU1NyKJd86bSGubxVbRCtz8HkTDZd28Z7Ice3rmscFMMo)

Pode adicionar vários pedidos HTTP à coleção. Clique nos três pontos da coleção e selecione \`Add request\`.

![Menu de coleção do Postman aberto com as ações Share, Move, Run collection, Edit, Add request, Add folder e Monitor collection](https://lh7-us.googleusercontent.com/S5W75clJz7JqoIWPbKBjrJqpTAwjS51Pu4dTU160Q7i6oW-HPnb7aN8WRK2AyAb6-HEqTYMZTy9563P0sq53MAjGpVg1JivZX2ATHa6GeFbTX2UCjud7ot8Y\_ksBuUbUfyEfxIDziV8TN3zDfX9Se58)

## Exemplo do método GET

O método GET permite consultar informação sobre utilizadores, suborganizações, documentos processados e outros dados.

* Escolha o método GET no pedido HTTP.
* Configure a autorização como descrito acima.
* Abra https://api.polydocs.io e acrescente o caminho da operação ao URL do Polydocs. Por exemplo:

![Página Swagger para o endpoint GET /orgs/get_users listando a rota de utilizadores da API DocBits](https://lh7-us.googleusercontent.com/pIdgyqP7g1UwZbY5yaz1KAnKe\_ESs\_kQyiWAXXM-ukRKakS\_\_OL\_LS9J-07hZnZDf8QqtoN\_lKyuhvOIIIF-4Wp0dkofZYQwXZ0hu2RM0YogRxJah-zf8W\_cDNFf8xsec1tYIsfe0SpBuvdCG4WHMU0)

* Cole o URL no campo junto ao método GET no Postman.

Clique em \`Send\`. Deverá receber a informação dos utilizadores da sua organização.

## Exemplo do método POST

O método POST é utilizado, por exemplo, para criar utilizadores ou organizações, introduzindo informação na base de dados.

Criar um utilizador

* Selecione o método POST.
* Configure a autorização como descrito acima.
* Abra https://api.polydocs.io e acrescente o caminho da operação ao URL do Polydocs. Neste caso:

![Página Swagger para o corpo do pedido POST create user a mostrar os campos obrigatórios first_name, last_name, email, password e is_admin](https://lh7-us.googleusercontent.com/Gwabl4pN0k0NanHsFOzJj9s2H7ExS-JcWr-Y4EW0FLUYHfnaOZoMWvldJ6yDI33p\_DThVx0Rd5bi59XdOK11l1knc5rd-E5HXMw6v5E3qvHvKVWHlp21S728SVye6KU2W5ZeXtCIOzxBAcMlA2UNFfQ)

* Cole o URL no campo junto ao método POST no Postman.
* No separador \`Body\` do pedido HTTP, introduza as chaves e os valores de cada campo obrigatório, identificado por um asterisco vermelho.

Depois de preencher os campos, o resultado deve ser semelhante ao seguinte:

![Separador Body do Postman com form-data selecionado e linhas de chave-valor para firstname, lastname, email, password e is_admin](https://lh7-us.googleusercontent.com/lSExzZSbTcSRvuLDw0HNYE62yI7xs0eUewKuOcABCGYfsRBRbGz1lJxopR4QdUEoniCnZ83FKpz-AHLORP5cXGPrPhgouzE6zO920jA7A3r-Y14wY\_Gc3C98R2fcxXsWRMcle9qT981YWhCnjlUukPE)

Para criar uma conta de administrador, defina \`is\_admin\` como true.

&#x20;Clique em \`Send\` e verifique os dados na resposta abaixo para confirmar a criação do utilizador.

### Carregar um documento

Também pode utilizar POST para carregar um documento no DocBits.

* Selecione o método POST.
* Configure a autorização como descrito acima.
* Abra https://api.polydocs.io e acrescente o caminho da operação ao URL do Polydocs.&#x20;

Neste caso:

![Página Swagger para o endpoint POST /document/process listando parâmetros como source, priority e sub_org_id com caixas de verificação Send empty value](https://lh7-us.googleusercontent.com/-EwhMeH\_WXYVmMKus1-IZKLZNyTcYktcf\_YUT\_m2nfStfKXuBxKBb1MZfUIQCN4ZxNKQkNhvO\_pgnt1EUhNB34qG5AOe4wM0OxGRMQsV9a8h0XUgabqq8mLQhza\_AE7gxBetmb9bJmaWBQqEXrWT0VI)

* Cole o URL no campo junto ao método POST no Postman.
* No separador \`Body\` do pedido HTTP, selecione \`form-data\`.

![Pedido Postman ao endpoint /document/process com o separador Body aberto, form-data selecionado e uma linha de chave de ficheiro vazia](https://lh7-us.googleusercontent.com/TNrKlyorn\_5YrIu5r4vcfyYgAnfhsl-SRVqWg9RoN0X1pUjXtn6J0EI7aeQ-oc2ZtFeTj8POcMXy6CwXzI1jhv-ufb2u7d80SC-lbGXmnx\_jVDunAbRw1jqAsB4PPsEzcFIOPeH5PJZvytUW2kIDYZ4)

![Pedido Postman para https://api.polydocs.io/document/process com form-data selecionado e a chave file definida com o valor Mango-invoice.pdf](https://lh7-us.googleusercontent.com/scAJpTSCqYSKYNNGPIrEsL0zDJIa7Dhe9tpqv\_zDjdLyAydugzdGA1s93njbFOOVbVbQf7oDEtRc14Kt4p1TXX8A--WjvRgeXWsAxDNWdrCN2-QDeya6-FFEG4\_-dhYgrj4yrVYllJs8eZsUgKOPvzo)

Introduza file em \`KEY\` para apresentar a lista de tipo de ficheiro. Selecione \`File\` e, em \`VALUE\`, escolha o ficheiro através de \`Select Files\`.

Ao clicar em \`Send\`, a resposta deverá conter “success”: true.

O resultado deve ser semelhante ao seguinte:

![Resposta do Postman para o documento carregado com estado 200 OK e o corpo JSON a mostrar success true, um doc_id e o nome de ficheiro Mango_invoice.pdf](https://lh7-us.googleusercontent.com/hNtG\_uTWgxww7iOmHLhnDqdrTlHCI1rk31LozG4l2DLPqxzSn9HoKn8CQIjeBgJLV4bxrGCjWOMRykJ3qBdZLYwxrZJGq\_S3tjVwSZmGTiMgVoqM97TTQjmW8CegEL2FV309NBmV0Fv\_vciSdQRFiOI)

## Exemplo do método DELETE

O método DELETE permite eliminar recursos, por exemplo utilizadores ou organizações.

* Selecione o método DELETE.
* Configure a autorização como descrito acima.
* Abra https://api.polydocs.io e acrescente o caminho da operação ao URL do Polydocs.

&#x20;Por exemplo:

![Página Swagger para o endpoint DELETE /users/delete/{user_id} da API do DocBits](https://lh7-us.googleusercontent.com/-QqSVIELl1IkxYK\_gGDa7nIv\_B1IvO3OjT3Ge6bAXwPl6jVDETuzXwtYJdRSmqLEP2d6B0L6MuwZvgJpI968pzp1APmJmuQ\_qlqYgZZhesocYCJVMCHhIZAKmlvMybUkUGXYZtySrnEbRTwWTritvKo)

* Cole o URL no campo junto ao método DELETE no Postman.
* Substitua {user\_id} no final do URL pelo identificador do utilizador a que se destina a operação. Pode obter user\_id através do método GET.
* Se user\_id já estiver incluído no URL, não precisa de repetir a chave e o valor no corpo do pedido.
* Ao clicar em \`Send\`, a resposta deverá conter “success”: true.

&#x20;O resultado deve ser semelhante ao seguinte:

![Pedido Delete User do Postman com Status 200 OK no painel de resposta após enviar a chamada DELETE](https://lh7-us.googleusercontent.com/X8WNtsC9v7jqDIiaVhauJUgZK0yTC1GVz9rBptdiCxyLUiEEfbpIoYHpK7NvlDMTkhgiPyBb22H9GOfDdvmL-dakouTjuRDPwX4YX0Jz5IIo6eHu-wnw1S4jJd5ylHyffUXWKwX6ovDnp\_2WEAtSha4)

## Exemplo do método PUT

O método PUT é utilizado sobretudo para atualizar os dados de utilizadores ou organizações.

* Selecione o método PUT.
* Configure a autorização como descrito acima.
* Abra https://api.polydocs.io e acrescente o caminho da operação ao URL do Polydocs.

&#x20;Por exemplo:

![Página Swagger para o endpoint PUT /users/update/{user_id} com os campos do corpo do pedido Update User: first_name, last_name e email](https://lh7-us.googleusercontent.com/tC3qtPbFb1GsK6dBmB5Jrv5HqFOYLxNR1XB0PEuA8ipkHnH2ZQ6xrrkImNgbGSMoA6aAGvLr6K3cI4u\_qM96BOvR7AnQzmX17HBMBneNpLBc6RIzspfTYgrCWSj0fSE9mSWLIex3hc\_R-m-PI6zT6Rs)

* Cole o URL no campo junto ao método PUT no Postman.
* Substitua {user\_id} no final do URL pelo identificador do utilizador a que se destina a operação. Pode obter user\_id através do método GET.

## Alterar o endereço de e-mail de um utilizador

* No corpo do pedido, introduza «email» como chave e o novo endereço de e-mail como valor.
* Prima \`Send\`. A resposta deverá apresentar «success».
