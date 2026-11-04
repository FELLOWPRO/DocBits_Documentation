# Postman para DocBits

Este guia irá mostrar como fazer requisições HTTP para a sua organização DocBits via Postman. É fácil de usar e muito útil para administradores de organização.

## Configuração

Primeiro, baixe o Postman para o seu sistema e faça login/registro.

Agora siga este guia passo a passo para aprender como as requisições HTTP funcionam no Postman.

Autorização no Postman

Antes de criar suas requisições HTTP, você precisa inserir sua chave de API do DocBits para autorizá-las.

* Clique na aba \`Authorization\` e escolha \`API Key\` como tipo de autorização.

![](https://lh7-us.googleusercontent.com/L3GaBZJvReeINaKbkq3VYQ9UHTBoKUA3nJkfyLqk61q5xaOJnmMLhbrEbgUgLEyYRkewHuLIAVzoYCZ6quHq0pwx\_69FEYJjzYllivB8WzdAtTFSrzl8VeFthbMsEB9sGjcGlVN38DXEXUwuNEPL6hg)

* Preencha os valores. Insira “X-API-key” no campo \`Key\` e sua chave de API como valor (encontrada no menu Configurações do DocBits em Integração) Selecione Adicionar em \`Header\`.

&#x20;

* Deve ficar assim:

![](https://lh7-us.googleusercontent.com/SmNfci4z8ECTeXzFPE9YQ8nCzCRHglc\_7RR1cN8a8F7KvYWjJcBnY5wpl7q0AV8bfNLkMk8F4F4aw8j4xMK50HJweBRBPo8EasTn-FG-fmlUJQ41aUX-dvTeWP\_xJQThi8A6EwJl3qIc-Dw1B5W9fVE)

### API do DocBits

Disponível em https://api.polydocs.io

* Clique em Autorizar no canto superior direito

![](https://lh7-us.googleusercontent.com/kuztHpkmRWlOYSU27r97KH15SJHPF\_hn\_eX3C1DYLVYCwMHXfLjYSyFubUCvlQiBt5q3xY0XBPmkcP6AnKF2C0Mdtx3tg\_dU\_qxqAmI6axYIsXR36\_YBz6j455K3-c2SBu4YzmYIXq8VXQxzgL-0j90)

* Insira sua chave de API e confirme clicando em \`Autorizar\`

![](https://lh7-us.googleusercontent.com/zLhgpdjMnxqNBdjgtDxFEKglICIZul7dgmfFFm2hSnsDQ-HsZHRKRikZ0lcanGYkkZj4waC85mEUFO951ydVnY\_\_m\_TrMrsK3vrDv9FKL-adgWL4lJqp3cSxPeClBm9IHG2cXinRsv12xTeh3psQfO4)

### Criar um novo Espaço de Trabalho no Postman

* Clique em Espaços de Trabalho e crie um novo espaço de trabalho (você pode nomeá-lo como quiser)

![](https://lh7-us.googleusercontent.com/3rZw7jhOgVpkZuer58fPEKqDspJjK3S1lp3XpQuvE4c9212a0ALB-p7oLRwPqEbj10MpoCWsb7V9fPqiAdVvigE00x9mN5-lHFXZVVxlkeroBJd2ratgkJVJDM4LJkUJsycyl6tnFKazcFPY-vWtH2Q)

* Você deve selecionar a visibilidade que determina quem pode acessar este espaço de trabalho.

![](https://lh7-us.googleusercontent.com/ZajvDtMvfM5J\_Go3n\_PgzD3RXTMQAlST8\_3WnsTQ4-iw7e0QdAa3wqFk7Y0gt78IJVjNTN-5E72c1127CpXJWb8WbfDolxENLqxg5VZLPEK7-hxsNwbAyMceSHfeVy6v-b9QT0kFwnMibWndEAJ2lXA)

* Após fazer sua seleção e clicar em \`Criar Espaço de Trabalho\` selecione Coleções no lado esquerdo da aplicação e crie uma nova coleção para suas requisições HTTP clicando em \`+\`.

![](https://lh7-us.googleusercontent.com/mbC5t86vaB2G7FQp-40XN-SHc019LKitfUeXRzbcG4HpNai5FPapShx9swHX3mz0va8QFsUQiYn-bhjvER0XYOEDRJpI9x3wG4NgRZCd4beU1NyKJd86bSGubxVbRCtz8HkTDZd28Z7Ice3rmscFMMo)

Nesta coleção, você pode adicionar múltiplas requisições HTTP. Para fazer isso, clique nos 3 pontos da coleção e selecione \`Adicionar requisição\`.

![](https://lh7-us.googleusercontent.com/S5W75clJz7JqoIWPbKBjrJqpTAwjS51Pu4dTU160Q7i6oW-HPnb7aN8WRK2AyAb6-HEqTYMZTy9563P0sq53MAjGpVg1JivZX2ATHa6GeFbTX2UCjud7ot8Y\_ksBuUbUfyEfxIDziV8TN3zDfX9Se58)

## Exemplo do Método "GET"

O método GET é muito útil para obter informações sobre usuários, sub-organizações, documentos processados e muito mais.

* Escolha o método GET na sua requisição HTTP.
* Autorize-se conforme descrito acima.
* Abra https://api.polydocs.io e adicione o caminho da função atrás da URL do Polydocs. Por exemplo:

![](https://lh7-us.googleusercontent.com/pIdgyqP7g1UwZbY5yaz1KAnKe\_ESs\_kQyiWAXXM-ukRKakS\_\_OL\_LS9J-07hZnZDf8QqtoN\_lKyuhvOIIIF-4Wp0dkofZYQwXZ0hu2RM0YogRxJah-zf8W\_cDNFf8xsec1tYIsfe0SpBuvdCG4WHMU0)

* Agora cole este link na caixa de texto ao lado do método GET no Postman.

Clique em \`Enviar\` e você deverá receber todas as informações sobre cada usuário na sua organização.

## Exemplo do Método "POST"

O método POST é geralmente usado para criar usuários ou organizações, por exemplo. Este método insere informações no banco de dados.

Criar Usuário

* Selecione o Método POST.
* Autorize-se conforme descrito acima.
* Abra https://api.polydocs.io e adicione o caminho da função atrás da URL do Polydocs. Neste caso:

![](https://lh7-us.googleusercontent.com/Gwabl4pN0k0NanHsFOzJj9s2H7ExS-JcWr-Y4EW0FLUYHfnaOZoMWvldJ6yDI33p\_DThVx0Rd5bi59XdOK11l1knc5rd-E5HXMw6v5E3qvHvKVWHlp21S728SVye6KU2W5ZeXtCIOzxBAcMlA2UNFfQ)

* Agora cole este link na caixa de texto ao lado do método POST no Postman.
* Selecione a aba \`Body\` na sua requisição HTTP e insira as chaves e os valores para cada credencial que tem um asterisco vermelho ao lado do seu nome.

Quando terminar, deve ficar assim:

![](https://lh7-us.googleusercontent.com/lSExzZSbTcSRvuLDw0HNYE62yI7xs0eUewKuOcABCGYfsRBRbGz1lJxopR4QdUEoniCnZ83FKpz-AHLORP5cXGPrPhgouzE6zO920jA7A3r-Y14wY\_Gc3C98R2fcxXsWRMcle9qT981YWhCnjlUukPE)

Se deseja criar uma conta de administrador, defina o valor de \`is_admin\` como true.

&#x20;Por fim, clique em \`Enviar\` e você poderá ver todas as credenciais que definiu na resposta abaixo. Isso significa que o usuário foi criado.
### Upload Document

Você também pode usar o método POST para fazer upload de um documento para o DocBits.

* Selecione o Método POST.
* Autorize-se conforme descrito acima.
* Abra https://api.polydocs.io e adicione o caminho da função atrás da URL do Polydocs.&#x20;

Neste caso:

![](https://lh7-us.googleusercontent.com/-EwhMeH\_WXYVmMKus1-IZKLZNyTcYktcf\_YUT\_m2nfStfKXuBxKBb1MZfUIQCN4ZxNKQkNhvO\_pgnt1EUhNB34qG5AOe4wM0OxGRMQsV9a8h0XUgabqq8mLQhza\_AE7gxBetmb9bJmaWBQqEXrWT0VI)

* Agora cole este link na caixa de texto ao lado do método POST no Postman.
* Selecione a aba \`Body\` na sua solicitação HTTP e escolha \`form-data\`

![](https://lh7-us.googleusercontent.com/TNrKlyorn\_5YrIu5r4vcfyYgAnfhsl-SRVqWg9RoN0X1pUjXtn6J0EI7aeQ-oc2ZtFeTj8POcMXy6CwXzI1jhv-ufb2u7d80SC-lbGXmnx\_jVDunAbRw1jqAsB4PPsEzcFIOPeH5PJZvytUW2kIDYZ4)

![](https://lh7-us.googleusercontent.com/scAJpTSCqYSKYNNGPIrEsL0zDJIa7Dhe9tpqv\_zDjdLyAydugzdGA1s93njbFOOVbVbQf7oDEtRc14Kt4p1TXX8A--WjvRgeXWsAxDNWdrCN2-QDeya6-FFEG4\_-dhYgrj4yrVYllJs8eZsUgKOPvzo)

Digite o arquivo no campo \`KEY\` onde você encontrará o menu suspenso de Arquivo oculto. Selecione \`File\` e vá para o campo \`VALUE\` onde você pode selecionar seu arquivo clicando em \`Select Files\`.

Quando você clicar em \`Send\`, você deverá ver “success”: true na resposta.

Deve parecer com isso:

![](https://lh7-us.googleusercontent.com/hNtG\_uTWgxww7iOmHLhnDqdrTlHCI1rk31LozG4l2DLPqxzSn9HoKn8CQIjeBgJLV4bxrGCjWOMRykJ3qBdZLYwxrZJGq\_S3tjVwSZmGTiMgVoqM97TTQjmW8CegEL2FV309NBmV0Fv\_vciSdQRFiOI)

## Exemplo do Método "DELETE"

O método DELETE é usado para excluir, por exemplo, usuários, organizações e assim por diante.

* Selecione o Método DELETE
* Autorize-se conforme descrito acima.
* Abra https://api.polydocs.io e adicione o caminho da função atrás da URL do Polydocs.

&#x20;Por exemplo:

![](https://lh7-us.googleusercontent.com/-QqSVIELl1IkxYK\_gGDa7nIv\_B1IvO3OjT3Ge6bAXwPl6jVDETuzXwtYJdRSmqLEP2d6B0L6MuwZvgJpI968pzp1APmJmuQ\_qlqYgZZhesocYCJVMCHhIZAKmlvMybUkUGXYZtySrnEbRTwWTritvKo)

* Agora cole este link na caixa de texto ao lado do método DELETE no Postman.
* Substitua o {user\_id} no final da URL pelo ID de usuário real que você deseja excluir. (Você pode obter o user\_id usando o método GET).
* Se você incluiu o user\_id na URL, não precisa adicionar uma chave e valor de corpo para ele.
* Quando você clicar em \`Send\`, você deverá ver “success”: true na resposta.

&#x20;Deve parecer com isso:

![](https://lh7-us.googleusercontent.com/X8WNtsC9v7jqDIiaVhauJUgZK0yTC1GVz9rBptdiCxyLUiEEfbpIoYHpK7NvlDMTkhgiPyBb22H9GOfDdvmL-dakouTjuRDPwX4YX0Jz5IIo6eHu-wnw1S4jJd5ylHyffUXWKwX6ovDnp\_2WEAtSha4)

## Exemplo do Método "PUT"

O método PUT é principalmente usado para atualizar dados de usuário ou organização. É muito fácil de entender e usar.

* Selecione o Método PUT.
* Autorize-se conforme descrito acima.
* Abra https://api.polydocs.io e adicione o caminho da função atrás da URL do Polydocs.

&#x20;Por exemplo:

![](https://lh7-us.googleusercontent.com/tC3qtPbFb1GsK6dBmB5Jrv5HqFOYLxNR1XB0PEuA8ipkHnH2ZQ6xrrkImNgbGSMoA6aAGvLr6K3cI4u\_qM96BOvR7AnQzmX17HBMBneNpLBc6RIzspfTYgrCWSj0fSE9mSWLIex3hc\_R-m-PI6zT6Rs)

* Agora cole este link na caixa de texto ao lado do método PUT no Postman.
* Substitua o {user\_id} no final da URL pelo ID de usuário real que você deseja excluir. (Você pode obter o user\_id usando o método GET).

## Alterar Endereço de E-mail de um Usuário

* No corpo, digite “email” como a chave e o novo endereço de e-mail como o valor.
* Em seguida, basta pressionar \`Send\` e você deverá ver “success” na resposta.
