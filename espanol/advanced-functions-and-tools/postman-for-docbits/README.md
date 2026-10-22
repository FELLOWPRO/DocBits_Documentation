# Postman para DocBits

Esta guía le mostrará cómo realizar solicitudes HTTP a su organización DocBits a través de Postman. Es fácil de usar y muy útil para los administradores de organizaciones.

## Configuración

Primero, descargue Postman a su sistema e inicie sesión/regístrese.

Ahora siga esta guía paso a paso para aprender cómo funcionan las solicitudes HTTP en Postman.

Authorization in Postman

Antes de poder crear sus solicitudes HTTP, debe ingresar su clave API de DocBits para autorizarlas.

* Haga clic en la pestaña \`Authorization\` y elija \`API Key\` como tipo de autorización.

![](https://lh7-us.googleusercontent.com/L3GaBZJvReeINaKbkq3VYQ9UHTBoKUA3nJkfyLqk61q5xaOJnmMLhbrEbgUgLEyYRkewHuLIAVzoYCZ6quHq0pwx\_69FEYJjzYllivB8WzdAtTFSrzl8VeFthbMsEB9sGjcGlVN38DXEXUwuNEPL6hg)

* Complete los valores. Ingrese “X-API-key” en el campo \`Key\` y su clave API como valor (que se encuentra en el menú Configuración de DocBits en Integración). Seleccione Agregar a \`Header\`.

&#x20;

* Debería verse así:

![](https://lh7-us.googleusercontent.com/SmNfci4z8ECTeXzFPE9YQ8nCzCRHglc\_7RR1cN8a8F7KvYWjJcBnY5wpl7q0AV8bfNLkMk8F4F4aw8j4xMK50HJweBRBPo8EasTn-FG-fmlUJQ41aUX-dvTeWP\_xJQThi8A6EwJl3qIc-Dw1B5W9fVE)

### API de DocBits

Available at https://api.polydocs.io

* Haga clic en Autorizar en la esquina superior derecha

![](https://lh7-us.googleusercontent.com/kuztHpkmRWlOYSU27r97KH15SJHPF\_hn\_eX3C1DYLVYCwMHXfLjYSyFubUCvlQiBt5q3xY0XBPmkcP6AnKF2C0Mdtx3tg\_dU\_qxqAmI6axYIsXR36\_YBz6j455K3-c2SBu4YzmYIXq8VXQxzgL-0j90)

* Ingrese su clave API y confirme haciendo clic en \`Authorize\`

![](https://lh7-us.googleusercontent.com/zLhgpdjMnxqNBdjgtDxFEKglICIZul7dgmfFFm2hSnsDQ-HsZHRKRikZ0lcanGYkkZj4waC85mEUFO951ydVnY\_\_m\_TrMrsK3vrDv9FKL-adgWL4lJqp3cSxPeClBm9IHG2cXinRsv12xTeh3psQfO4)

### Crear un espacio de trabajo en Postman

* Haga clic en Espacios de trabajo y cree un nuevo espacio de trabajo (puede nombrarlo como desee)

![](https://lh7-us.googleusercontent.com/3rZw7jhOgVpkZuer58fPEKqDspJjK3S1lp3XpQuvE4c9212a0ALB-p7oLRwPqEbj10MpoCWsb7V9fPqiAdVvigE00x9mN5-lHFXZVVxlkeroBJd2ratgkJVJDM4LJkUJsycyl6tnFKazcFPY-vWtH2Q)

* Debe seleccionar la visibilidad que determina quién puede acceder a este espacio de trabajo.

![](https://lh7-us.googleusercontent.com/ZajvDtMvfM5J\_Go3n\_PgzD3RXTMQAlST8\_3WnsTQ4-iw7e0QdAa3wqFk7Y0gt78IJVjNTN-5E72c1127CpXJWb8WbfDolxENLqxg5VZLPEK7-hxsNwbAyMceSHfeVy6v-b9QT0kFwnMibWndEAJ2lXA)

* Después de hacer su selección y hacer clic en \`Create Workspace\`, seleccione Colecciones en el lado izquierdo de la aplicación y cree una nueva colección para sus solicitudes HTTP haciendo clic en \`+\`.

![](https://lh7-us.googleusercontent.com/mbC5t86vaB2G7FQp-40XN-SHc019LKitfUeXRzbcG4HpNai5FPapShx9swHX3mz0va8QFsUQiYn-bhjvER0XYOEDRJpI9x3wG4NgRZCd4beU1NyKJd86bSGubxVbRCtz8HkTDZd28Z7Ice3rmscFMMo)

En esta colección, puede agregar varias solicitudes HTTP. Para ello, haga clic en los 3 puntos de la colección y seleccione \`Add request\`.

![](https://lh7-us.googleusercontent.com/S5W75clJz7JqoIWPbKBjrJqpTAwjS51Pu4dTU160Q7i6oW-HPnb7aN8WRK2AyAb6-HEqTYMZTy9563P0sq53MAjGpVg1JivZX2ATHa6GeFbTX2UCjud7ot8Y\_ksBuUbUfyEfxIDziV8TN3zDfX9Se58)

## Ejemplo del método "GET"

El método GET es muy útil para obtener información sobre usuarios, suborganizaciones, documentos procesados y mucho más.

* Elija el método GET en su solicitud HTTP.
* Autorícese como se describe arriba.
* Abra https://api.polydocs.io y agregue la ruta de la función detrás de Polydocs URL. Por ejemplo:

![](https://lh7-us.googleusercontent.com/pIdgyqP7g1UwZbY5yaz1KAnKe\_ESs\_kQyiWAXXM-ukRKakS\_\_OL\_LS9J-07hZnZDf8QqtoN\_lKyuhvOIIIF-4Wp0dkofZYQwXZ0hu2RM0YogRxJah-zf8W\_cDNFf8xsec1tYIsfe0SpBuvdCG4WHMU0)

* Ahora pegue este enlace en el cuadro de texto junto al método GET en Postman.

Haga clic en \`Send\` y debería recibir toda la información sobre cada usuario de su organización.

## Ejemplo del método "POST"

El método POST se suele utilizar para crear usuarios u organizaciones, por ejemplo. Este método inserta información en la base de datos.

Create User

* Seleccione el método POST.
* Autorízate como se describe arriba
* Abra https://api.polydocs.io y agregue la ruta de la función detrás de Polydocs URL. En este caso:

![](https://lh7-us.googleusercontent.com/Gwabl4pN0k0NanHsFOzJj9s2H7ExS-JcWr-Y4EW0FLUYHfnaOZoMWvldJ6yDI33p\_DThVx0Rd5bi59XdOK11l1knc5rd-E5HXMw6v5E3qvHvKVWHlp21S728SVye6KU2W5ZeXtCIOzxBAcMlA2UNFfQ)

* Ahora pegue este enlace en el cuadro de texto junto al método POST en Postman.
* Seleccione la pestaña \`Body\` en su solicitud HTTP e ingrese las claves y los valores para cada credencial que tenga un asterisco rojo junto a su nombre.

Cuando haya terminado, debería verse así:

![](https://lh7-us.googleusercontent.com/lSExzZSbTcSRvuLDw0HNYE62yI7xs0eUewKuOcABCGYfsRBRbGz1lJxopR4QdUEoniCnZ83FKpz-AHLORP5cXGPrPhgouzE6zO920jA7A3r-Y14wY\_Gc3C98R2fcxXsWRMcle9qT981YWhCnjlUukPE)

Si desea crear una cuenta de administrador, establezca el valor \`is\_admin\` en verdadero.

Finalmente, haga clic en \`Send\` y podrá ver todas las credenciales que configuró en la respuesta a continuación. Esto significa que el usuario ha sido creado.

### Cargar documento

También puede utilizar el método POST para cargar un documento en DocBits.

* Seleccione el método POST.
* Autorícese como se describe arriba.
* Abra https://api.polydocs.io y agregue la ruta de la función detrás de Polydocs URL.

En este caso:

![](https://lh7-us.googleusercontent.com/-EwhMeH\_WXYVmMKus1-IZKLZNyTcYktcf\_YUT\_m2nfStfKXuBxKBb1MZfUIQCN4ZxNKQkNhvO\_pgnt1EUhNB34qG5AOe4wM0OxGRMQsV9a8h0XUgabqq8mLQhza\_AE7gxBetmb9bJmaWBQqEXrWT0VI)

* Ahora pegue este enlace en el cuadro de texto junto al método POST en Postman.
* Seleccione la pestaña \`Body\` en su solicitud HTTP y elija \`form-data\`

![](https://lh7-us.googleusercontent.com/TNrKlyorn\_5YrIu5r4vcfyYgAnfhsl-SRVqWg9RoN0X1pUjXtn6J0EI7aeQ-oc2ZtFeTj8POcMXy6CwXzI1jhv-ufb2u7d80SC-lbGXmnx\_jVDunAbRw1jqAsB4PPsEzcFIOPeH5PJZvytUW2kIDYZ4)

![](https://lh7-us.googleusercontent.com/scAJpTSCqYSKYNNGPIrEsL0zDJIa7Dhe9tpqv\_zDjdLyAydugzdGA1s93njbFOOVbVbQf7oDEtRc14Kt4p1TXX8A--WjvRgeXWsAxDNWdrCN2-QDeya6-FFEG4\_-dhYgrj4yrVYllJs8eZsUgKOPvzo)

Ingrese el archivo en el campo \`KEY\` donde encontrará el menú desplegable Archivo oculto. Seleccione \`File\` y vaya al campo \`VALUE\` donde podrá seleccionar su archivo haciendo clic en \`Select Files\`.

Cuando haces clic en \`Send\`, deberías ver “success”: verdadero en la respuesta.

Debería verse así:

![](https://lh7-us.googleusercontent.com/hNtG\_uTWgxww7iOmHLhnDqdrTlHCI1rk31LozG4l2DLPqxzSn9HoKn8CQIjeBgJLV4bxrGCjWOMRykJ3qBdZLYwxrZJGq\_S3tjVwSZmGTiMgVoqM97TTQjmW8CegEL2FV309NBmV0Fv\_vciSdQRFiOI)

## Ejemplo del método "DELETE"

El método DELETE se utiliza para eliminar, por ejemplo, usuarios, organizaciones, etc.

* Seleccione el método DELETE
* Autorícese como se describe arriba.
* Abra https://api.polydocs.io y agregue la ruta de la función detrás de Polydocs URL.

Por ejemplo:

![](https://lh7-us.googleusercontent.com/-QqSVIELl1IkxYK\_gGDa7nIv\_B1IvO3OjT3Ge6bAXwPl6jVDETuzXwtYJdRSmqLEP2d6B0L6MuwZvgJpI968pzp1APmJmuQ\_qlqYgZZhesocYCJVMCHhIZAKmlvMybUkUGXYZtySrnEbRTwWTritvKo)

* Ahora pegue este enlace en el cuadro de texto junto al método DELETE en Postman.
* Reemplace {user\_id} al final de URL con el usuario real ID que desea eliminar. (Puedes obtener el user\_id usando el método GET).
* Si incluyó el user\_id en el URL, no necesita agregarle una clave de cuerpo ni un valor.
* Cuando haces clic en \`Send\`, deberías ver “success”: verdadero en la respuesta.

Debería verse así:

![](https://lh7-us.googleusercontent.com/X8WNtsC9v7jqDIiaVhauJUgZK0yTC1GVz9rBptdiCxyLUiEEfbpIoYHpK7NvlDMTkhgiPyBb22H9GOfDdvmL-dakouTjuRDPwX4YX0Jz5IIo6eHu-wnw1S4jJd5ylHyffUXWKwX6ovDnp\_2WEAtSha4)

## Ejemplo del método "PUT"

El método PUT se utiliza principalmente para actualizar datos de usuarios u organizaciones. Es muy fácil de entender y utilizar.

* Seleccione el método PUT.
* Autorícese como se describe arriba.
* Abra https://api.polydocs.io y agregue la ruta de la función detrás de Polydocs URL.

Por ejemplo:

![](https://lh7-us.googleusercontent.com/tC3qtPbFb1GsK6dBmB5Jrv5HqFOYLxNR1XB0PEuA8ipkHnH2ZQ6xrrkImNgbGSMoA6aAGvLr6K3cI4u\_qM96BOvR7AnQzmX17HBMBneNpLBc6RIzspfTYgrCWSj0fSE9mSWLIex3hc\_R-m-PI6zT6Rs)

* Ahora pegue este enlace en el cuadro de texto junto al método PUT en Postman.
* Reemplace {user\_id} al final de URL con el usuario real ID que desea eliminar. (Puedes obtener el user\_id usando el método GET).

## Cambiar la dirección de correo de un usuario

* En el cuerpo, ingrese “email” como clave y la nueva dirección de correo electrónico como valor.
* Luego simplemente presione \`Send\` y debería ver “success” en la respuesta.
