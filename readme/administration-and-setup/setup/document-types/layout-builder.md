# Editor de diseños

{% embed url="https://youtu.be/-m45XGiIeig" %}
DocBits Tutorial de Layout Builder: cree diseños de documentos personalizados para una validación más rápida y limpia
{% endembed %}

## **Acceso al editor de diseños**

En primer lugar, asegúrese de que la función Layout Builder esté activada. Esto se puede hacer navegando a Configuración → Procesamiento de documentos → Módulo → Tipo de documento y asegúrese de que el control deslizante del editor de diseños esté activado como se muestra a continuación.

![Ajustes del tipo de documento con las secciones Layout Builder, Models &amp; Labels, Doc Script y Doc Scan, la sección Layout Builder abierta y su control deslizante](https://lh7-us.googleusercontent.com/I0VvFiFftKLoCB47jCAoosfTyqIQgXBoggMFp1QAeIj9xW4yiiIzyk5eIEHZ7duA251Yc4\_ArUKA8e-LjDht13bckAnkAOHOvl1p5k1-Qj\_UkEp2cSZwxHz\_PXe8IQ4\_jglzCtjAJg5pd9m\_hNZEhXA)

Una vez hecho esto, puede acceder al editor de diseños a través de Configuración → Tipos de documentos. Una vez en esta página, puede seleccionar entre los diversos tipos de documentos que ha creado y seleccionar “Edit Layout” como se muestra a continuación.

![Barra de pestañas de un tipo de documento con las entradas Labels, Edit layout, Document Sub Types, Table columns, Fields, Model Training, Regex y Scripts](https://lh7-us.googleusercontent.com/WMD8M0qugnc64ZuyLuEYH5P63qk-Vo86useg32-QyOsP63FJA\_Xh7UzwlwmUR3K9oTd19aXexSitZqQLVEKo26-i8hYWUS9CChzwAS8TgbWoqweFucJcNIgKBruzSd0mxn8zrh9i46lPxKMNDh-YEJ8)

o si tiene tipos de subdocumentos dentro de un tipo de documento creado, puede seleccionar “Document Sub Types” y seleccionar “Edit Layout” para el diseño del tipo de subdocumento que desea editar como se muestra a continuación.

![Lista de tipos de documento con las columnas NAME y ACTION y las filas WARENRECHNUNG, KOSTENRECHNUNG, FRACHTRECHNUNG y Test, cada fila con Fields, Edit layout, Scripts y Copy](https://lh7-us.googleusercontent.com/KfmM8wMGnn5tzXRxF1yT0Efm7X6v0kYeGzgNG3RihERh\_P71tjEVkJh4POMwgqnsCBoE736xI7oHkmpYNUbtAShhE-wAHsnLuxljDtmhGQUyljF\_PmOF2y6c0gIdIk\_jUD3sVNsq5viT2sb236OBYSA)

## **Conceptos básicos del gestor de diseños**

Después de seguir los pasos anteriores llegarás a una página como la que se muestra a continuación.

### **Cargar un documento de ejemplo**

Para cargar un documento en el creador de diseños, simplemente navegue hacia la derecha en la pantalla.

![Página Layout Builder con el panel ELEMENTS a la izquierda, los grupos de documento Invoice Details, Payment Details, PO number, VAT &amp; Amounts y Vendor Details y el área de diseño vacía a la derecha](https://lh7-us.googleusercontent.com/I99BkFDTOloyKwwc0P8O3wf8FbKL3B5Zn5i3GfeRKSSkBdelQ\_HNfI2oJzaXQUi\_UU6R5Vr7jrgcAxIrDmmTKWgTZx90J7izOX0oczWt\_\_qt9VmD1HqafZvqH8vb7xnZMR1m5pjwzsbcnalErYo6dIc)

Haga clic en el botón “Upload Documents” o arrastre y suelte el documento que desee en el área proporcionada

![Página Layout Builder con el árbol de elementos a la izquierda y el área de diseño a la derecha que acepta un documento mediante arrastrar y soltar](https://lh7-us.googleusercontent.com/GHqGYqvwFvN3z2ojFz\_i7ZLlZhy-A3vsKUmmzOC0NMkPd2-f6\_t\_0USF66W-N3XRqHlmx06QNSQ7U-VTPQPKWdzOhoNcN7LlMk45sKVC6bWN1O92G0r4dKyHQLlgmGZiINYjZ9vZnt89\_BjgzbON2MI)

### **Grupos**

Los grupos se pueden crear seleccionando el siguiente icono.

![Página Layout Builder con el árbol de elementos a la izquierda y el botón Upload Documents en el área de diseño](https://lh7-us.googleusercontent.com/eb4jnCmezPFKPwgUisJKvicBqMWuGHW69WIFdtpmQiY-\_78VWmMyMD4TqKMJXwjH1XDnS5RXX0DsJ2\_ur\_GG62L4F7OEzkLrpgwUkiuQjZQPJqQoHIBj6WM33zY0AkYXhI3mKLjZetbEQ2AlhPJ8KV8)

Los grupos le permiten crear diferentes secciones en un diseño, lo que facilita separar diferentes grupos de datos o información para que el diseño sea más fácil de seguir. Puedes crear un título para cada grupo para que un usuario pueda saber qué información encontrará en ese grupo.

![Página Layout Builder con el panel ELEMENTS y la sección Groups del árbol de elementos](https://lh7-us.googleusercontent.com/lWqIEC-TCOp4rKytTbhn2fYWY618\_Yra2mjWHA9oMyWPqHXA5JKCLoZoEtM8xQHAkn4HFNTPYpbMePUYnQhQGL0KmgBfTEDWPDAMy7PjZinZl2s\_kHQlsLAGjYbzSINWTme3qRO9tHLcpVaDVvS\_8F4)

### **Elementos del formulario**

![Panel Elements con las secciones Groups y Fields y los elementos de formulario Text, Label, Check Box, Multi Check Box, Horizontal Separator, Table Of Checkboxes, Button y Extracted Tables](https://lh7-us.googleusercontent.com/OFBRSGdol7loocu5uGVe4Q8URMDojvXTN0xj3TCgL-jb-wUgt1fjEqfXCyMPz\_HNh94LVVmg6ifQDhxvlQsgbbChRfrw2Ohx4ICOUwHix3iiAFY9hI3BPGBfcNABiHLhgXQJVZmGvEO\_niVWkIXz\_6g)

Se trata de un conjunto de campos predeterminados que se pueden arrastrar y soltar en el editor de diseños y que están disponibles para que usted cree el diseño que desee. Estos incluyen:

* Texto: este es un cuadro de texto que crea un campo en el diseño en el que se puede ingresar texto una vez en la pantalla de validación.
* Etiqueta: este es un campo que se puede usar para crear texto no editable, esto podría usarse para crear subtítulos o cualquier otro texto no editable que se desee cuando esté en la pantalla de validación.
* Casilla de verificación: esto crea un campo de tipo booleano que se puede marcar o desmarcar.
* Casilla de verificación múltiple: funciona de la misma manera que “Checkbox”, pero se puede usar cuando el usuario sabe que agregará varias casillas de verificación en una sección.
* Separador horizontal: esto crea una línea horizontal en el diseño que se puede usar para dividir secciones dentro de un grupo en el diseño.
* Tabla de casillas de verificación: esto permite al usuario crear una tabla de casillas de verificación que consta de valores personalizados de los ejes x e y, por ejemplo.

![Tabla de casillas con el encabezado Please mark with a cross sobre las columnas A a H y las filas Test 1 y Test 2](https://lh7-us.googleusercontent.com/lMZU68H4i8ELjgenpcNXeNhJ9iwzTWGRkjNMEdV3rqdGwnaRZ\_tvG9mbx2ogXQ2hMciGSp-9m1c5KS9VwGJWzuxcRiaioVDSLTLvh-csHUho4aX25LXrtjhGSfK6yTukufwrjQvZR-JliuhiaPCCxpw)

* Botón: crea un botón en la pantalla de validación del diseño. Puede configurarlo para **Export**, **Export mit Sonderwunsch** (exportación con una solicitud especial) o **Reject**.
* Tablas extraídas: esto le permite colocar un área en el diseño del documento que ilustra la tabla que se extrae del documento. Para obtener información haga clic aquí.
* Botones de factura: este elemento le permite arrastrar y soltar un conjunto de botones optimizados para facturas. Cuando esté en la pantalla de validación, cuando seleccione el tipo de factura (ya sea costo o compra), la conciliación con la orden de compra o Contabilidad automática desaparecerá en consecuencia.

![Fila de botones de factura en la vista de validación con las entradas SAVE RULES, AUTO ACCOUNTING, PO MATCH y EXPORT](https://lh7-us.googleusercontent.com/-w5iTr9b\_pcc6Y39osFmuzKQGRa\_e4tAXvQOn1zN8T4HwcuTs\_FP9mFPAJJeABvYKTyiQr3xZALsRgueIDksbswhnY-E9ioT1AIaf8xwAblBckX1f8xzi5v9mLxBRRUZoViDntKK6Nd5fy5sd5Bq5LU)

* QR Campos de código: este elemento le permite arrastrar y soltar un bloque que mostrará toda la información extraída de un documento cuando esté presente un código QR.

### **Crear campos específicos del documento**

El usuario puede crear sus propios grupos y campos personalizados para un tipo de documento; esto se puede hacer al crear originalmente un tipo de documento, pero también seleccionando “Fields” en la página Tipos de documento en Configuración.

![Barra de pestañas de un tipo de documento con las entradas Labels, Edit layout, Document Sub Types, Table columns, Fields, Model Training, Regex y Scripts](https://lh7-us.googleusercontent.com/N9i3KnGyXATf5jLVbPQGiPEG9rlz6WqHJ5c8FZnpw3EwmaMnl2cQhMwhug3d-A82caOS6Nxc7LgAVLMtBL404hKR7i39u2RfwzCnohqn1\_mbkMtjzNKThnjGu2ivaFNqKDuobzA6kUdD8gGiQ\_zs3z8)

### **Espacios en blanco**

#### **La regla del 100 por ciento**

![Grupo de diseño con el título Group Title, el botón DELETE GROUP y los dos campos Test 1 y Test 2 uno al lado del otro](https://lh7-us.googleusercontent.com/TwNA3gZrgzhSvZrZOGywGYz92fRkUtjIsr6sDCxEzYgWcfJ9kXuzJKkqNiFyp3H5XXoqUz76TzZ72r86YY\_O3Vw\_rvDKczD\_hdMOIQOFWORr2bo8pGunrAtUklJ1ye7KEQJEjRNqNUNCnXM0boIICUA)

Para crear el espacio anterior en el diseño, se debe utilizar un “Label” de los Elementos del formulario de forma especial. La razón de esto es que el gestor de diseños opera de acuerdo con un sistema de 100 espacios por línea en el que 1 espacio representa el 1 por ciento de una línea, esto significa que los campos solo pueden ocupar 100 espacios por línea como se muestra a continuación.

![Diseño con un elemento Label seleccionado, el grupo de diseño con el título Test 1 y el panel de propiedades con la entrada Element Width in Percentage](https://lh7-us.googleusercontent.com/YTqddzVQPWRuP5ylV6NnMc-KnEgCY0ZxZ8zn0In5d5dOxaWnwGDi4N2qohbobLNphLfVD61sMUE5QlmXJZ3e0tP7Y8no\_wVRy9WTF0nWIN5Tg3t-zLJhs9M-kVYPFV3CyerRZZoK-iMXLmKGcuSY\_Nw)

Esto significa que el usuario debe construir el diseño línea por línea de acuerdo con esta regla. Por ejemplo, digamos que desea agregar los campos “Name” y “Date” en la misma línea pero desea que el campo “Name” sea más grande. Esto se puede hacer arrastrando y soltando el campo “Text” desde el menú desplegable Elementos de campo y nombrando cada campo “Name” y “Date” como se muestra.

![Panel de propiedades de un campo de texto con el campo Name, el identificador interno y el valor 30 en Element Width in Percentage](https://lh7-us.googleusercontent.com/2ru3pj0iD3V6ADqYBjeQPqDT3uvTH\_Al2MV0gpUUQ9MpX0TSFtnjYL6JN0YOkBk9afx2q2YcMo4gWE2jItUAGSEfX79O\_6sFgKwP5FGa98SwzgjGgee1G-2aO6NyqZusf27SbJoWoHmzu51Hx25kVmM)

Ahora existe el problema de que ambos tienen el mismo tamaño de 33 (este es el tamaño predeterminado de todos los campos arrastrados y soltados), pero le gustaría que el campo “Name” fuera más grande que el campo “Date” y ambos campos deberían ocupar toda la línea en el diseño. Por lo tanto, siguiendo la regla del 100 por ciento, puede configurar los campos “Name” y “Date” en cualquier combinación de 100 que desee. Por supuesto, esto depende del tamaño que desee para cada campo individual, pero para este ejemplo estableceremos el campo “Name” en 70 y el campo “Date” en 30, los resultados son:

![Diseño con los dos campos Name y Date en una línea junto al panel de propiedades del campo seleccionado](https://lh7-us.googleusercontent.com/m411QblkCfsQWllhX74QpANjuVEv3fgM1Nhg8cJjbkNQGcjym6v0JFHIrKyMOAu-MasQ4KH9ZPaxmqNWfhWmAuL6SOZE030NXebb7ERzYxF99hLJC6oGbM-YXp7bNdZuoTaPmsDt7EjpV5BOiflwA4g)

Esta misma regla se aplica a todos los campos del editor de diseños.

#### **Crear espacios en blanco**

Ahora que se ha explicado esta regla, crear espacios en blanco tendrá más sentido. Como se mencionó anteriormente, para crear un espacio en blanco debe usar un “Label” de los Elementos del formulario.

Por ejemplo, digamos que le gustaría crear un espacio en blanco entre estos dos campos.

![Grupo de diseño con el título Test, el botón DELETE GROUP y los dos campos con un espacio entre ellos](https://lh7-us.googleusercontent.com/jOms6aTB3wCmX3L-MiUTrOb\_-q3AiFC3Y75TsHJe8QFLru10H9aZKzbE5MfHPZ0v9fqycQeddNPJp7pnRjv17crkrYUymNA8u9bF-3u9IfR6ru\_duavqrLCQocommljzLA00RXs\_lQA4gDH6l\_QvyTs)

El primer paso es arrastrar y soltar un “Label” entre estos dos campos, una vez agregado, puede hacer clic en el campo “Label” que acaba de agregar y a la izquierda se le presentarán las propiedades del campo. Ahora, de la misma manera que crearía o cambiaría el nombre de un campo como se mostró anteriormente, eliminará cualquier nombre de la propiedad “Label” así

![Panel de propiedades de un Label con el nombre mostrado vacío, el identificador interno input_8b7cc2b8 y el valor 30 en Element Width in Percentage](https://lh7-us.googleusercontent.com/0Mma4wYIIfAkOyRIFLZtjug7pbWltfaiPm3r\_WgbP5fCgKe2BGD6Qf5YJ5Ns7fBBTRfJ68NlOtmOQrvcOvjyWGxk9v\_XmDj-8moEQhcDUugh\_VO5DdrJLYYV08ftr8YdhuhEM0otWs\_ljew18j7XJFQ)

El resultado de hacer esto será entonces

![Grupo de diseño con el título Test, el botón DELETE GROUP y el espacio mayor entre los dos campos](https://lh7-us.googleusercontent.com/-HqoJUAbcHRCletgSg6gcKXpn6zto1Do8I5EmcEmPWL4qUrMREh-wZdhy7ZKtnbuGjypd7p2mjcIu6LbbfdjA3c1liT2reCQXWiP1VAji08eWc\_bbF\_a0Dd82rJRgCuD5yjdlXL\_DNheMcw-fm6pQnA)

Ahora existe una brecha entre los dos campos. Este espacio se puede ampliar o acortar según la regla del 100 por ciento comentada anteriormente, y con estas funciones puedes crear cualquier diseño que desees.
