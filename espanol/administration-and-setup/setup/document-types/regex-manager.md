# Gestor de Regex

Esta función de DocBits le ofrece una alternativa a la clasificación por modelo, ya que permite escribir expresiones regulares de búsqueda para un tipo de documento, con fines de clasificación y otros usos.

Tipo de documento: el Gestor de Regex le permite escribir expresiones regulares que luego se buscan en el documento. Si DocBits encuentra una coincidencia con la expresión regular de un documento definido, clasifica el documento en el tipo de documento correspondiente. Por ejemplo, si escribe una expresión regular para encontrar “Gutschrift” y DocBits encuentra ese término en un documento, lo clasificará como nota de crédito.

Origen del documento: mediante expresiones regulares, DocBits también reconoce el país de origen de un documento. Por ejemplo, si una expresión regular para un documento español contiene el término “Factura” y DocBits lo encuentra en el documento, sabrá que es de origen español y lo clasificará como tal.

## **Acceder al Gestor de Regex**

En DocBits, vaya a Ajustes → Tipos de documento. En “Tipos de documento personalizados”, haga clic en “Nuevo”. Introduzca un nombre para el tipo de documento, añada una descripción opcional y marque “Tabla disponible” si el documento contiene una tabla. Después elija “Regular” en lugar de “Auto” y haga clic en “Próximo”.

<figure><img src="../../../.gitbook/assets/regex-manager-create-es-20261006.png" alt="Página para crear un nuevo tipo de documento con el campo de nombre, la casilla Tabla disponible, la descripción y los botones Auto y Regular"><figcaption><p>Elija “Regular” para clasificar el nuevo tipo de documento con expresiones regulares.</p></figcaption></figure>

## **Agregar y eliminar regex**

El paso “Regular” muestra los modelos de regex existentes, cada uno con su origen y su patrón, y un botón “Agregar” para crear un nuevo modelo. Use el menú de acciones al final de la fila para gestionar esa entrada. Haga clic en “Próximo” para continuar con “Campos y grupos”.

<figure><img src="../../../.gitbook/assets/regex-manager-list-es-20261006.png" alt="Paso Regular con el botón Agregar y una tabla con tres modelos de regex, con origen, patrón y acciones"><figcaption><p>Modelos de regex existentes con origen y patrón. “Agregar” crea uno nuevo.</p></figcaption></figure>
