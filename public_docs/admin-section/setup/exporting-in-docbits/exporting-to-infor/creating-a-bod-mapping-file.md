# Creación de un Archivo de Mapeo BOD

Descargue un Archivo de Mapeo BOD y ábralo en su editor de archivos correspondiente para editarlo. Para este tutorial, se utiliza VSCode.

## Edición del Archivo de Mapeo

Cambie la empresa al valor correcto (SFV\_AccountingEntityID) y edite el ID de ubicación si es necesario.

![](https://lh7-us.googleusercontent.com/eJQI1CKlxEkS\_Pwp0VH2hgS220b-q8NSFG5iJKpLOL457qTN3CbUB8IHTw1lRinbB\_kP00UUNgepWNsbh3\_Ko-SExObePjqmxP7ee\_lQnADTtDmxEtRM\_S7AONMbcpjwtnHTakYd1Q06GVm2G0o-UDA)

Verifique el código del documento yendo a la configuración de campo del tipo de documento que está intentando exportar (encontrado en la URL de la configuración de campo del tipo de documento en DocBits como se muestra a continuación

![](https://lh7-us.googleusercontent.com/AhU3i27qFS7BMCgpNQnmLWAjcIWHXHOlxMKqd2Yob5RQKa8qysQQsSsacr6zao4cnAh3DISPgYu1GnjubIJpgtAdiBR\_0vy3WJZXPY-HeEfVQkWnlRI9UEJWMPQ7DbWYLQhz339BOlbd4KgxU9B\_CPE)

Por último, edite el SFV\_LogicalID que se puede encontrar en INFOR ION DESK → Conectar → Puntos de Conexión y seleccione DocBits\_Export u otro punto de conexión similar y dentro de esa página encontrará el ID Lógico que necesita.

![](https://lh7-us.googleusercontent.com/f50i7pzRuZULJ6shehba0lWIWFBTsPZyip-LQxAYJpYDXK66SlzdGOpdEG-wqLQfqXMgMMhm5SAvj57UOCvF6xf2OMCXtFiEEKr9yiQr4xtv8vbV-NGcLuJwuQ9zHMBBKfTktAp1nSfBJhdPeAu3RWc)

![](https://lh7-us.googleusercontent.com/qyEt4iYRIjOZCCrVbImeK6EdZGun2YrAy8li8u3tulcD8bwzl\_sl1TiEXKqbik-4MxnbV\_MCwltvuA2WAgzzvDpTVd7W52he9QD9IK0qijoz3ZihUYcWJlqlD5kbcsRTj3SfP1CDqcyhoFfBeiE1Xfo)

## Crear ID Lógico (Punto de Conexión)

Si este Punto de Conexión aún no existe, necesitará crear uno.

Primero, vaya a ION Desk → Conectar → Puntos de Conexión y haga clic en el botón "+ Agregar"

![](https://lh7-us.googleusercontent.com/fQPmV8KgffyWhM0i0cQlyh7fyQe37p8uR6C\_pVD5SboEx2emIJX2212GXqk\_KT71DfYMKSjkfYFFTARqgLLxoOPNQFXHxUOo9vMXH2pmDN469VgbQkV-JjRtCevZJsbvS8vbfUtasN83xN25tX6\_S5U)

Luego seleccione la opción "IMS via API Gateway"

![](https://lh7-us.googleusercontent.com/uPLiiLHp6Z3jPCzYBOzHVuI8sGY5XQuUfv66fZYH0HndSBL7yvzFHh3lJjEMxteJfXsVMhUe3U\_38xZHDRFSn0jeiMZUQBJJLzZ2oaIQAixY7wUPd6D0PJwg7wvC8XBeZxPmjNoiUvP3ImoG\_aOhFmY)

![](https://lh7-us.googleusercontent.com/VhyMDEuglPfxeX-3cATu6ZFB\_Mz2Y7C-yJ99EvBvrhD8IoVzGd4ksjrWAE0mIPub2PX5\_Zua10ZHQeWI82QbJ8ZgJKN-tVpVrYGvMdfQOj3Uco5efsPT6JYkDyPu\_lkeR9aTGhh5-q2bzZztXuTUixM)

Se le llevará a la pantalla anterior donde ahora debe completar la información necesaria, el nombre debería ser algo como "DocBits\_export" o similar.

Para "ID de Cliente de API de ION" ingrese el mismo ID de Cliente que obtuvo anteriormente para el Archivo de Mapeo de ION.

Luego seleccione la pestaña Documento del menú de creación del Punto de Conexión y agregue los siguientes documentos presionando el signo "+", esto solo será útil más adelante.

![](https://lh7-us.googleusercontent.com/GtHlTliePV-JIDLP9YNGlXELKuWIU2VSlUt4mvWO4q\_XM54MSL9zTmtxPMdeOl24VFtNC0pQ-nbXyHb9PaeMkKvgzpCOo5kLdL3A8Bw54ILniwIdTyfxFhPuzRUGKs2hRi5ioKvfkdsPMgq4x6EHOtM)

Una vez que guarde este Punto de Conexión, obtendrá el ID Lógico como se muestra a continuación

![](https://lh7-us.googleusercontent.com/P7cihsQT2Qcq\_XGL08dTV2jHMUK7YCMQyXsJudkVDXDh73GZ-hS61IoAKSHptPyX4C5e\_xPKP0yZGzpQOwCFw6BppPlzZuFWZ\_VGIrOUmJH2egxaCEXMoVBHBM6lkZeb3gPYWYdMYpuNqFFPC-4Qol0)

Luego inserte este ID Lógico en la sección correspondiente del Archivo de Mapeo BOD y guarde el archivo.

## Subir Archivo a DocBits

Arrastre y suelte el archivo en su configuración de exportación en DocBits. Esto está disponible en Configuración → Exportar.

![](https://lh7-us.googleusercontent.com/AqCo7QgC-kaAxbaIJD8MYeKGLBXbwGVJPGx9\_2yfUp3R2MYxJPowVAjnO80uxQ9qMDxNoXy1eY3WH-mEpaeWwatwi91edm\_0lS9Hg93FSAjQGtDAR5y7Ptce-ARfetSiXIBJKiGwujSggVXXHUhG77U)
