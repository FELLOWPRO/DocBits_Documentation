# Definir tablas y columnas

Utilice esta guía para definir manualmente tablas y columnas para la extracción de líneas de artículo en DocBits. Resulta especialmente útil cuando la detección automática no captura por completo la estructura de la tabla o cuando necesita añadir campos personalizados.

### 1. Acceda a la vista de extracción de tablas

Abra su documento en DocBits y haga clic en el botón **“Table Training”** para entrar en la vista de extracción de tablas.

<figure><img src="../../../../.gitbook/assets/define_tables_and_columns_1.png" alt="" width="563"><figcaption></figcaption></figure>

### 2. Active el modo de entrenamiento

Para definir o modificar tablas y columnas manualmente, haga clic en **“TRAINING MODE”.**

<div align="center"><figure><img src="../../../../.gitbook/assets/define_tables_and_columns_2.png" alt="" width="375"><figcaption></figcaption></figure></div>

### 3. Defina el área de la tabla

Después de entrar en el modo de entrenamiento, puede definir dónde se encuentra la tabla en el documento. Tiene dos opciones:

#### Opción 1: usar la detección automática

Haga clic en el botón **“Auto-Detect Tables”** para que DocBits intente identificar por sí mismo el área de la tabla.

<figure><img src="../../../../.gitbook/assets/define_tables_and_columns_3.png" alt="" width="375"><figcaption></figcaption></figure>

Si la detección es correcta, el contorno de la tabla se mostrará automáticamente. A continuación, puede pasar a definir las columnas.

#### Opción 2: definir la tabla manualmente

Si la detección automática falla o no es precisa, puede definir la tabla manualmente:

1. Haga clic en el botón **“Edit”** para activar el modo de selección de tablas.
2. Dibuje un rectángulo alrededor del área de la tabla en la vista del documento de la izquierda.

<figure><img src="../../../../.gitbook/assets/define_tables_and_columns_4.png" alt="" width="563"><figcaption></figcaption></figure>

### 4. Añada y defina columnas

Una vez definidas las tablas, puede definir las columnas manualmente mediante el siguiente botón:\


<figure><img src="../../../../.gitbook/assets/define_tables_and_columns_5.png" alt="" width="563"><figcaption></figcaption></figure>

Defina y ordene las columnas arrastrando y soltando sobre el documento. Repita este paso también para las tablas de las demás páginas. Como alternativa, si las tablas son iguales en cada página, puede utilizar el siguiente botón para usar las mismas columnas en todas las tablas definidas en el documento. Esta función copia las columnas que ha definido también a todas las demás páginas:

<figure><img src="../../../../.gitbook/assets/define_tables_and_columns_6.png" alt="" width="563"><figcaption></figcaption></figure>

Utilice la función de **zoom** para definir mejor las columnas en documentos saturados o complejos, por ejemplo, cuando hay mucha información muy junta y resulta difícil definir las columnas:

<figure><img src="../../../../.gitbook/assets/define_tables_and_columns_7.png" alt="" width="277"><figcaption></figcaption></figure>

Si ha definido una columna por error, puede seleccionarla haciendo clic en ella y eliminarla mediante el siguiente botón:

<figure><img src="../../../../.gitbook/assets/define_tables_and_columns_9.png" alt="" width="563"><figcaption></figcaption></figure>

<mark style="color:red;">**Nota**</mark>: el botón solo es visible si la columna está seleccionada.

Cuando haya terminado de definir todas las tablas y todas las columnas de su documento, utilice el botón “Save” para activar los cambios y extraer los datos del documento:

<figure><img src="../../../../.gitbook/assets/define_tables_and_columns_8.png" alt="" width="563"><figcaption></figcaption></figure>

Los datos de todas las áreas definidas se extraerán y se mostrarán en el lado derecho:

<figure><img src="../../../../.gitbook/assets/define_tables_and_columns_10.png" alt="" width="375"><figcaption></figcaption></figure>

### 6. Guarde y extraiga

Haga clic en **“Save Rules”** una vez definidas todas las tablas y columnas.

* Esto indica a DocBits dónde encontrar los datos de la tabla para este proveedor concreto.
* La próxima vez que se cargue un documento del mismo proveedor, DocBits extraerá automáticamente la tabla con las reglas guardadas.

<mark style="color:red;">**Nota**</mark>: este entrenamiento es específico de cada proveedor. No se aplicará a documentos de otros proveedores.
