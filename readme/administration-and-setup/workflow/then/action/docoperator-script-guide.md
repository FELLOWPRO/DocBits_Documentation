# Ejecute el mensaje DocOperator (script de automatización)

***

Agregue esta tarjeta al grupo **Entonces** del Generador de flujo de trabajo: las acciones que se ejecutan una vez que coinciden las condiciones Cuándo/Y:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-es.png" alt="Ejemplo sin guardar con tarjetas Cuando, Y y Entonces. Configure todos los campos antes de ejecutarlo. Algunas etiquetas de esta versión de la tarjeta todavía tienen una traducción incompleta o incorrecta en la interfaz. Las explicaciones de esta página utilizan los términos correctos."><figcaption><p>Ejemplo sin guardar con tarjetas Cuando, Y y Entonces. Configure todos los campos antes de ejecutarlo. Algunas etiquetas de esta versión de la tarjeta todavía tienen una traducción incompleta o incorrecta en la interfaz. Las explicaciones de esta página utilizan los términos correctos.</p></figcaption></figure>

***

## 📌 Información de versión

**Versión actual:** v3 (más reciente y recomendada) **Estado:** ✅ Activo

**Historial de versiones:**

* v2 → Implementación original de DocOperator
* **v3 → CURRENT** (parámetro de control de ejecución agregado)
* v4 → En desuso (funciones revertidas)

**Qué cambió:** v3 agregó el parámetro opcional "Ejecutar el mensaje" para tener más control. v4 intentó revertir esto pero quedó obsoleto.

📖 [Historial de versiones y cambios](../../release.md) | [Base de datos de tarjetas completa](../../cards-overview/export-cards-guide.md)

***

## Propósito

Esta tarjeta ejecuta una acción o secuencia de comandos automatizada del navegador mediante DocOperator. Piense en ello como un robot que puede interactuar con sitios web o sistemas exactamente como lo haría un humano: haciendo clic en botones, completando formularios, extrayendo datos, etc.

**Ejemplo del mundo real:** Su empresa utiliza un sistema de compras basado en web. Esta tarjeta puede iniciar sesión automáticamente, buscar un producto, verificar la disponibilidad y obtener el precio actual, todo sin que nadie lo haga manualmente.

***

## Cuándo utilizar esta tarjeta

Utilice esta tarjeta cuando necesite:

* Automatiza tareas en sitios web que no tienen API
* Extraer datos de páginas web
* Rellenar formularios automáticamente
* Inicie sesión en los sistemas y recupere información
* Automatiza tareas manuales repetitivas
* Interactuar con sistemas heredados que no están integrados

**Escenarios comunes:**

* Inicie sesión en los sitios web de los proveedores y obtenga un inventario en tiempo real
* Completar formularios automáticamente en sistemas externos
* Extraiga datos de páginas web que no ofrecen API
* Verifique el estado de la entrega en los sitios web de mensajería
* Obtenga precios de sistemas sin acceso API

***

## Cómo funciona

1. **Tarjeta activada**: el flujo de trabajo llega a esta tarjeta y se cumplen las condiciones
2. **Se inicia el script**: el bot DocOperator comienza a ejecutar su script de automatización
3. **Acciones del bot**: el bot realiza acciones como hacer clic, escribir, desplazarse y extraer.
4. **Extracción de datos**: Bot recopila información de páginas web
5. **Devolver datos**: Los datos regresan a DocFlow para su uso en las siguientes tarjetas
6. **Manejo de tiempo de espera**: si el script tarda demasiado, se detiene y devuelve lo que tiene

***

## Parámetros explicados

### Mensaje/script del DocOperator

El script de automatización que le dice a DocOperator exactamente qué hacer

**Ejemplo (inglés sencillo):**

```
1. Go to https://supplier.com/login
2. Enter username: myuser
3. Enter password: mypass
4. Click Login button
5. Search for product "ABC123"
6. Extract the price
7. Return the price
```

### variables

Datos que desea pasar AL script

**Ejemplo:**

```
product_id: "ABC123"
supplier_code: "SUPP-001"
```

Estas variables se pueden utilizar en el script como:

```
Search for product "{product_id}"
Find supplier "{supplier_code}"
```

### Pasos máximos

¿Cuántas acciones puede realizar el bot?

**Valores típicos:**

* Tarea simple (como obtener un precio): 10-20 pasos
* Complejidad media (rellenar formulario + extracto): 20-50 pasos
* Flujo de trabajo complejo (iniciar sesión + buscar + validar): 50-100 pasos

**Por qué es importante:** Evita bucles infinitos y scripts de ejecución muy largos

### Reintentos máximos

Si el bot falla en una acción, ¿cuántas veces debería intentarlo nuevamente?

**Ejemplos:**

* 1: Inténtalo una vez, si falla continúa
* 3: Inténtalo 3 veces antes de rendirte
* 5: Muy persistente - inténtalo 5 veces

***

## Ejemplo paso a paso

### Escenario: obtener precios de proveedores desde el sitio web

**Definición de guión:**

```
Step 1: Open website https://prices.supplier-xyz.com
Step 2: Click on "Product Lookup"
Step 3: Enter product code: ABC-123
Step 4: Click "Search"
Step 5: Wait for results to load (3 seconds)
Step 6: Extract price from the page
Step 7: Extract available quantity
Step 8: Return both values
```

**Variables pasadas:**

```
product_code = "ABC-123"
supplier_name = "Supplier XYZ"
```

**Script usando variables:**

```
Open website https://prices.{supplier_name}.com
Enter product code: {product_code}
Extract price and quantity
```

**Resultado esperado:**

```
price: 45.50
quantity_available: 500
```

***

## Tipos de acciones que DocOperator puede realizar

### Navegación

* Ir a URL
* Haga clic en enlaces
* botones de presión
* Desplazarse por la página

### Llenado de formularios

* Escriba texto en los campos
* Seleccionar opciones desplegables
* Marcar/desmarcar casillas
* Haga clic en los botones

### Extracción de datos

* Leer texto de la página
* Extraer números
* Obtener datos de la tabla
* Copiar información

### esperando

* Espere a que se cargue la página
* Espere a que aparezcan los elementos.
* Espere contenido dinámico

### Lógica condicional

* Si algo existe, haz esto.
* Si el texto coincide, entonces...
* Cuente los resultados y actúe en consecuencia

***

## Casos de uso comunes

### 1. Obtenga precios en tiempo real

**Escenario:** El proveedor no tiene API pero el sitio web muestra precios

**Guión:**

```
1. Go to supplier website
2. Search for product
3. Extract price from results
4. Return price to DocFlow
5. Use price to validate invoice
```

### 2. Verificar la disponibilidad del inventario

**Escenario:** Necesita saber si el proveedor tiene stock

**Guión:**

```
1. Log into supplier portal
2. Search for product
3. Extract availability status
4. Extract delivery time
5. Return both to DocFlow
```

### 3. Envío automático de formularios

**Escenario:** Necesita completar un formulario en un sitio externo

**Guión:**

```
1. Navigate to form page
2. Fill Company Name field
3. Fill Contact Email field
4. Select Country from dropdown
5. Upload file attachment
6. Click Submit button
7. Capture confirmation message
```

### 4. Verificación de entrada de datos

**Escenario:** Verificar coincidencias de datos en dos sistemas diferentes

**Guión:**

```
1. Go to System A
2. Search for Order #123
3. Extract order amount
4. Go to System B
5. Search for Order #123
6. Extract order amount
7. Compare amounts
8. Return true/false if they match
```

***

## Pasos de configuración

### Paso 1: crea el guión

1. Define lo que quieres lograr
2. Divídelo en pequeños pasos
3. Escribe cada paso claramente.
4. Pruebe primero manualmente (abra el sitio web, hágalo usted mismo)
5. Documente exactamente lo que hace clic, dónde escribe, qué extrae

### Paso 2: identificar variables

1. ¿Qué datos cambiarán entre documentos?
2. ¿Qué se debe pasar al guión?
3. Definir nombres de variables
4. Especificar dónde se utilizan las variables en el script

### Paso 3: establecer parámetros

* **Pasos máximos**: basado en la complejidad del script
* **Máximo de reintentos**: ¿Qué tan persistente debe ser el robot?
* **Tiempo de espera**: ¿Cuánto tiempo deben esperar las páginas?

### Paso 4: prueba

1. Prueba con datos de muestra
2. Verificar que el bot pueda acceder al sitio web
3. Verificar que la extracción sea correcta
4. Comprobar si las variables funcionan correctamente

***

## Consejos para escribir guiones

### Lenguaje claro

✅ **Hacer:**

```
1. Click the "Login" button
2. Type the username in the login field
3. Wait 2 seconds for form to process
```

❌ **No:**

```
1. Do the login thing
2. Enter stuff
3. Wait for it
```

### Selectores específicos

✅ **Hacer:**

```
Click the button labeled "Submit Order"
Type in the field with placeholder "Enter Email"
```

❌ **No:**

```
Click somewhere
Type in a field
```

### Manejo de errores

✅ **Hacer:**

```
1. Try to click "Next" button
2. If button not found, extract data from current page
3. Return what we have
```

❌ **No:**

```
Click "Next" (assumes it's always there)
```

***

## Solución de problemas

### "Se agotó el tiempo de espera del guión"

**Causa:** El script tardó demasiado en completarse

**Soluciones:**

* [ ] Reducir el número de acciones
* [] Aumentar el valor de "Pasos máximos"
* [] Optimice el script para una ejecución más rápida
* [] Simplifica lo que estás intentando extraer

### "Elemento no encontrado"

**Causa:** DocOperator no pudo encontrar el botón/campo que especificó

**Soluciones:**

* [] Verificar que el nombre del botón/campo sea exactamente correcto
* [] Compruebe si el diseño del sitio web cambió
* [] Agregar tiempo de espera antes de hacer clic
* [] Compruebe si el botón solo aparece bajo ciertas condiciones

### "Error de inicio de sesión"

**Causa:** Error de autenticación

**Soluciones:**

* [] Verifique que el nombre de usuario y la contraseña sean correctos
* [] Compruebe si la contraseña tiene caracteres especiales
* [] Verificar que la cuenta no esté bloqueada
* [] Compruebe si el proceso de inicio de sesión cambió

### "Datos no extraídos correctamente"

**Causa:** El script se ejecutó pero extrajo información incorrecta

**Soluciones:**

* [] Verifique que se seleccionó el campo correcto
* [] Compruebe si los datos están en la ubicación esperada
* [] Pruebe la lógica de extracción manualmente
* [] Agregue pasos de depuración para verificar lo que hay en la página

### "El guión se ejecuta lentamente"

**Causa:** Demasiados pasos o sitio web lento

**Soluciones:**

* [] Eliminar pasos innecesarios
* [ ] Optimizar los tiempos de espera
* [] Verifique la conexión a Internet
* [] Considere si existe una alternativa API

***

## Mejores prácticas

✅ **Hacer:**

* Pruebe los scripts minuciosamente antes de implementarlos
* Mantenga los guiones simples y enfocados
* Añade comentarios explicando cada paso.
* Utilice nombres de variables significativos
* Supervisar el rendimiento del script
* Tener un respaldo para cuando los scripts fallan

❌ **No:**

* Cree guiones extremadamente largos (>100 pasos)
* Ponga contraseñas confidenciales en los registros
* Confíe en coordenadas exactas (los sitios web cambian)
* Crear bucles sin condiciones de salida.
* Ignorar mensajes de error

***

## Consejos de rendimiento

* **Eliminar pasos no utilizados**: cada paso lleva tiempo
* **Combinar acciones similares**: clics relacionados con el grupo
* **Optimizar esperas** - Utilice solo los retrasos necesarios
* **Datos de caché**: no extraiga los mismos datos dos veces
* **Procesamiento paralelo**: ejecute varios scripts si es posible

***

## Consideraciones de seguridad

⚠️ **Importante:**

* No almacene contraseñas en DocFlow
* Utilice métodos seguros para pasar credenciales
* No registres datos confidenciales
* Monitorear lo que se extrae
* Asegúrese de que la actividad del bot esté registrada y sea auditable

***

## Ejemplo de variables

### Variables disponibles que puede utilizar:

```
{invoice_number} - From document field
{supplier_code} - From document field
{product_id} - From document field
{quantity} - From document field
{currency} - From document field
```

### Script usando variables:

```
1. Go to https://supplier.com/api/lookup
2. Enter supplier code: {supplier_code}
3. Search for product: {product_id}
4. Enter quantity: {quantity}
5. Extract price in currency: {currency}
6. Return extracted price
```

***

## Comparación: cuándo utilizar DocOperator frente a API

| Situación              | Utilice DocOperador | Usar API     |
| ---------------------- | --------------- | ----------- |
| El sitio web tiene API        | ❌No            | ✅ Sí       |
| El sitio web es interactivo. | ✅ Sí           | ❌No        |
| Requiere iniciar sesión         | ✅ Sí           | depende     |
| Se necesita muy rapido       | ❌No            | ✅ Sí       |
| Flujo de trabajo complejo       | ✅ Sí           | ❌ Quizás no |
| Los datos cambian diariamente     | ✅ Sí           | ✅ Sí       |

***

## Tarjetas relacionadas

* **CALL\_API**: utilizar cuando la API esté disponible en su lugar
* **ACTION\_HTTPS\_REQUEST** - Solicitudes más simples
* **ACTION\_SET\_FIELD\_TO\_TEXT** - Usar datos extraídos
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - Verificar el estado de la solicitud
