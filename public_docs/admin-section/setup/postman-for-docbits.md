# Postman para DocBits

Esta guía te mostrará cómo hacer solicitudes HTTP a tu organización de DocBits a través de Postman. Es fácil de usar y muy útil para los administradores de la organización.

## Configuración

Primero, descarga Postman en tu sistema e inicia sesión/registrate.

Ahora sigue esta guía paso a paso para aprender cómo funcionan las solicitudes HTTP en Postman.

Autorización en Postman

Antes de poder crear tus solicitudes HTTP, necesitas ingresar tu clave API de DocBits para autorizarlas.

* Haz clic en la pestaña de \`Autorización\` y elige \`Clave API\` como tipo de autorización.

![](https://lh7-us.googleusercontent.com/L3GaBZJvReeINaKbkq3VYQ9UHTBoKUA3nJkfyLqk61q5xaOJnmMLhbrEbgUgLEyYRkewHuLIAVzoYCZ6quHq0pwx\_69FEYJjzYllivB8WzdAtTFSrzl8VeFthbMsEB9sGjcGlVN38DXEXUwuNEPL6hg)

* Completa los valores. Ingresa "X-API-key" en el campo de \`Clave\` y tu clave API como valor (encontrada en el menú de Configuración de DocBits bajo Integración). Selecciona Agregar a \`Encabezado\`.

&#x20;

* Debería lucir así:

![](https://lh7-us.googleusercontent.com/SmNfci4z8ECTeXzFPE9YQ8nCzCRHglc\_7RR1cN8a8F7KvYWjJcBnY5wpl7q0AV8bfNLkMk8F4F4aw8j4xMK50HJweBRBPo8EasTn-FG-fmlUJQ41aUX-dvTeWP\_xJQThi8A6EwJl3qIc-Dw1B5W9fVE)

### API de DocBits

Disponible en https://api.polydocs.io

* Haz clic en Autorizar en la esquina superior derecha

![](https://lh7-us.googleusercontent.com/kuztHpkmRWlOYSU27r97KH15SJHPF\_hn\_eX3C1DYLVYCwMHXfLjYSyFubUCvlQiBt5q3xY0XBPmkcP6AnKF2C0Mdtx3tg\_dU\_qxqAmI6axYIsXR36\_YBz6j455K3-c2SBu4YzmYIXq8VXQxzgL-0j90)

* Ingresa tu clave API y confirma haciendo clic en \`Autorizar\`

![](https://lh7-us.googleusercontent.com/zLhgpdjMnxqNBdjgtDxFEKglICIZul7dgmfFFm2hSnsDQ-HsZHRKRikZ0lcanGYkkZj4waC85mEUFO951ydVnY\_\_m\_TrMrsK3vrDv9FKL-adgWL4lJqp3cSxPeClBm9IHG2cXinRsv12xTeh3psQfO4)

### Crear un nuevo Espacio de trabajo en Postman

* Haz clic en Espacios de trabajo y crea un nuevo espacio de trabajo (puedes nombrarlo como desees)

![](https://lh7-us.googleusercontent.com/3rZw7jhOgVpkZuer58fPEKqDspJjK3S1lp3XpQuvE4c9212a0ALB-p7oLRwPqEbj10MpoCWsb7V9fPqiAdVvigE00x9mN5-lHFXZVVxlkeroBJd2ratgkJVJDM4LJkUJsycyl6tnFKazcFPY-vWtH2Q)

* Debes seleccionar la visibilidad que determina quién puede acceder a este espacio de trabajo.

![](https://lh7-us.googleusercontent.com/ZajvDtMvfM5J\_Go3n\_PgzD3RXTMQAlST8\_3WnsTQ4-iw7e0QdAa3wqFk7Y0gt78IJVjNTN-5E72c1127CpXJWb8WbfDolxENLqxg5VZLPEK7-hxsNwbAyMceSHfeVy6v-b9QT0kFwnMibWndEAJ2lXA)

* Después de hacer tu selección y hacer clic en \`Crear Espacio de trabajo\` selecciona Colecciones en el lado izquierdo de la aplicación y crea una nueva colección para tus solicitudes HTTP haciendo clic en \`+\`.

![](https://lh7-us.googleusercontent.com/mbC5t86vaB2G7FQp-40XN-SHc019LKitfUeXRzbcG4HpNai5FPapShx9swHX3mz0va8QFsUQiYn-bhjvER0XYOEDRJpI9x3wG4NgRZCd4beU1NyKJd86bSGubxVbRCtz8HkTDZd28Z7Ice3rmscFMMo)

En esta colección, puedes agregar múltiples solicitudes HTTP. Para hacerlo, haz clic en los 3 puntos de la colección y selecciona \`Agregar solicitud\`.

![](https://lh7-us.googleusercontent.com/S5W75clJz7JqoIWPbKBjrJqpTAwjS51Pu4dTU160Q7i6oW-HPnb7aN8WRK2AyAb6-HEqTYMZTy9563P0sq53MAjGpVg1JivZX2ATHa6GeFbTX2UCjud7ot8Y\_ksBuUbUfyEfxIDziV8TN3zDfX9Se58)

## Ejemplo de método "GET"

El método GET es muy útil para obtener información sobre usuarios, sub-organizaciones, documentos procesados y mucho más.

* Elige el método GET en tu solicitud HTTP.
* Autorízate como se describe arriba.
* Abre https://api.polydocs.io y agrega la ruta de la función detrás de la URL de Polydocs. Por ejemplo:

![](https://lh7-us.googleusercontent.com/pIdgyqP7g1UwZbY5yaz1KAnKe\_ESs\_kQyiWAXXM-ukRKakS\_\_OL\_LS9J-07hZnZDf8QqtoN\_lKyuhvOIIIF-4Wp0dkofZYQwXZ0hu2RM0YogRxJah-zf8W\_cDNFf8xsec1tYIsfe0SpBuvdCG4WHMU0)

* Ahora pega este enlace en el cuadro de texto junto al método GET en Postman.

Haz clic en \`Enviar\` y deberías recibir toda la información sobre cada usuario en tu organización.

## Ejemplo de método "POST"

El método POST se usa generalmente para crear usuarios u organizaciones, por ejemplo. Este método inserta información en la base de datos.

Crear Usuario

* Selecciona el Método POST.
* Autorízate como se describe arriba.
* Abre https://api.polydocs.io y agrega la ruta de la función detrás de la URL de Polydocs. En este caso:

![](https://lh7-us.googleusercontent.com/Gwabl4pN0k0NanHsFOzJj9s2H7ExS-JcWr-Y4EW0FLUYHfnaOZoMWvldJ6yDI33p\_DThVx0Rd5bi59XdOK11l1knc5rd-E5HXMw6v5E3qvHvKVWHlp21S728SVye6KU2W5ZeXtCIOzxBAcMlA2UNFfQ)

* Ahora pega este enlace en el cuadro de texto junto al método POST en Postman.
* Selecciona la pestaña de \`Cuerpo\` en tu solicitud HTTP e ingresa las claves y los valores para cada credencial que tenga un asterisco rojo junto a su nombre.

Cuando hayas terminado, debería lucir así:

![](https://lh7-us.googleusercontent.com/lSExzZSbTcSRvuLDw0HNYE62yI7xs0eUewKuOcABCGYfsRBRbGz1lJxopR4QdUEoniCnZ83FKpz-AHLORP5cXGPrPhgouzE6zO920jA7A3r-Y14wY\_Gc3C98R2fcxXsWRMcle9qT981YWhCnjlUukPE)

Si deseas crear una cuenta de administrador, establece el valor de \`is_admin\` en true.

&#x20;Finalmente, haz clic en \`Enviar\` y podrás ver todas las credenciales que estableciste en la respuesta a continuación. Esto significa que el usuario ha sido creado.
### Subir Documento

También puedes usar el método POST para subir un documento a DocBits.

* Selecciona el Método POST.
* Autorízate como se describe arriba.
* Abre https://api.polydocs.io y añade la ruta de la función detrás de la URL de Polydocs.&#x20;

En este caso:

![](https://lh7-us.googleusercontent.com/-EwhMeH\_WXYVmMKus1-IZKLZNyTcYktcf\_YUT\_m2nfStfKXuBxKBb1MZfUIQCN4ZxNKQkNhvO\_pgnt1EUhNB34qG5AOe4wM0OxGRMQsV9a8h0XUgabqq8mLQhza\_AE7gxBetmb9bJmaWBQqEXrWT0VI)

* Ahora pega este enlace en el cuadro de texto junto al método POST en Postman.
* Selecciona la pestaña \`Body\` en tu solicitud HTTP y elige \`form-data\`

![](https://lh7-us.googleusercontent.com/TNrKlyorn\_5YrIu5r4vcfyYgAnfhsl-SRVqWg9RoN0X1pUjXtn6J0EI7aeQ-oc2ZtFeTj8POcMXy6CwXzI1jhv-ufb2u7d80SC-lbGXmnx\_jVDunAbRw1jqAsB4PPsEzcFIOPeH5PJZvytUW2kIDYZ4)

![](https://lh7-us.googleusercontent.com/scAJpTSCqYSKYNNGPIrEsL0zDJIa7Dhe9tpqv\_zDjdLyAydugzdGA1s93njbFOOVbVbQf7oDEtRc14Kt4p1TXX8A--WjvRgeXWsAxDNWdrCN2-QDeya6-FFEG4\_-dhYgrj4yrVYllJs8eZsUgKOPvzo)

Ingresa el archivo en el campo \`KEY\` donde encontrarás el menú desplegable de Archivo oculto. Selecciona \`Archivo\` y pasa al campo \`VALUE\` donde puedes seleccionar tu archivo haciendo clic en \`Seleccionar Archivos\`.

Cuando hagas clic en \`Enviar\`, deberías ver “success”: true en la respuesta.

Debería lucir así:

![](https://lh7-us.googleusercontent.com/hNtG\_uTWgxww7iOmHLhnDqdrTlHCI1rk31LozG4l2DLPqxzSn9HoKn8CQIjeBgJLV4bxrGCjWOMRykJ3qBdZLYwxrZJGq\_S3tjVwSZmGTiMgVoqM97TTQjmW8CegEL2FV309NBmV0Fv\_vciSdQRFiOI)

## Ejemplo de Método "DELETE"

El método DELETE se utiliza para eliminar, por ejemplo, usuarios, organizaciones, etc.

* Selecciona el Método DELETE.
* Autorízate como se describe arriba.
* Abre https://api.polydocs.io y añade la ruta de la función detrás de la URL de Polydocs.

&#x20;Por ejemplo:

![](https://lh7-us.googleusercontent.com/-QqSVIELl1IkxYK\_gGDa7nIv\_B1IvO3OjT3Ge6bAXwPl6jVDETuzXwtYJdRSmqLEP2d6B0L6MuwZvgJpI968pzp1APmJmuQ\_qlqYgZZhesocYCJVMCHhIZAKmlvMybUkUGXYZtySrnEbRTwWTritvKo)

* Ahora pega este enlace en el cuadro de texto junto al método DELETE en Postman.
* Reemplaza el {user\_id} al final de la URL con el ID de usuario real que deseas eliminar. (Puedes obtener el user\_id usando el método GET).
* Si incluiste el user\_id en la URL, no necesitas añadir una clave y valor de cuerpo para ello.
* Cuando hagas clic en \`Enviar\`, deberías ver “success”: true en la respuesta.

&#x20;Debería lucir así:

![](https://lh7-us.googleusercontent.com/X8WNtsC9v7jqDIiaVhauJUgZK0yTC1GVz9rBptdiCxyLUiEEfbpIoYHpK7NvlDMTkhgiPyBb22H9GOfDdvmL-dakouTjuRDPwX4YX0Jz5IIo6eHu-wnw1S4jJd5ylHyffUXWKwX6ovDnp\_2WEAtSha4)

## Ejemplo de Método "PUT"

El método PUT se utiliza principalmente para actualizar datos de usuario u organización. Es muy fácil de entender y usar.

* Selecciona el Método PUT.
* Autorízate como se describe arriba.
* Abre https://api.polydocs.io y añade la ruta de la función detrás de la URL de Polydocs.

&#x20;Por ejemplo:

![](https://lh7-us.googleusercontent.com/tC3qtPbFb1GsK6dBmB5Jrv5HqFOYLxNR1XB0PEuA8ipkHnH2ZQ6xrrkImNgbGSMoA6aAGvLr6K3cI4u\_qM96BOvR7AnQzmX17HBMBneNpLBc6RIzspfTYgrCWSj0fSE9mSWLIex3hc\_R-m-PI6zT6Rs)

* Ahora pega este enlace en el cuadro de texto junto al método PUT en Postman.
* Reemplaza el {user\_id} al final de la URL con el ID de usuario real que deseas eliminar. (Puedes obtener el user\_id usando el método GET).

## Cambiar la Dirección de Correo Electrónico de un Usuario

* En el cuerpo, ingresa “email” como la clave y la nueva dirección de correo electrónico como el valor.
* Luego simplemente presiona \`Enviar\` y deberías ver “success” en la respuesta.
