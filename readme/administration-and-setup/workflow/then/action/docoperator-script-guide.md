# Run DocOperator Prompt (Automation Script)

Estas tarjetas van en el grupo **Then** del Generador de flujos de trabajo: las acciones que se ejecutan cuando se cumplen las condiciones When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Las tarjetas se añaden al grupo <strong>Then</strong> mediante <strong>Add Card</strong>.</p></figcaption></figure>

---

## 📌 Información de versión

**Versión actual:** v3 (la más reciente y recomendada)
**Estado:** ✅ Activa

**Historial de versiones:**
- v1 → No documentada
- v2 → Implementación original de DocOperator
- **v3 → ACTUAL** (se añadió el parámetro de control de ejecución)
- v4 → Obsoleta (funciones revertidas)

**Qué cambió:** v3 añadió el parámetro opcional "Execute the prompt" para un mayor control. v4 intentó revertir esto pero quedó obsoleta.

📖 [Version History & Changes](../../../changelog/release.md#3-action_run_docoperator_script--) | [Complete Card Database](../../../../DocFlow/docs/card_version.md#action_run_docoperator_script)

---

## Propósito
Esta tarjeta ejecuta una acción de navegador o un script automatizado mediante DocOperator. Considérela como un robot que puede interactuar con sitios web o sistemas exactamente como lo haría una persona: hacer clic en botones, rellenar formularios, extraer datos, etc.

**Ejemplo real:** Su empresa utiliza un sistema de compras basado en web. Esta tarjeta puede iniciar sesión automáticamente, buscar un producto, comprobar la disponibilidad y obtener el precio actual, todo ello sin que nadie lo haga manualmente.

---

## Cuándo usar esta tarjeta

Use esta tarjeta cuando necesite:
- Automatizar tareas en sitios web que no tienen API
- Extraer datos de páginas web
- Rellenar formularios automáticamente
- Iniciar sesión en sistemas y recuperar información
- Automatizar tareas manuales repetitivas
- Interactuar con sistemas heredados que no están integrados

**Escenarios comunes:**
- Iniciar sesión en sitios web de proveedores y obtener el inventario en tiempo real
- Rellenar automáticamente formularios en sistemas externos
- Extraer datos de páginas web que no ofrecen API
- Comprobar el estado de la entrega en los sitios web de mensajería
- Obtener precios de sistemas sin acceso a API

---

## Cómo funciona

1. **Tarjeta activada**: El flujo de trabajo llega a esta tarjeta y se cumplen las condiciones
2. **El script comienza**: El bot de DocOperator empieza a ejecutar su script de automatización
3. **Acciones del bot**: El bot realiza acciones como hacer clic, escribir, desplazarse y extraer
4. **Extracción de datos**: El bot recopila información de las páginas web
5. **Devolver datos**: Los datos vuelven a DocFlow para usarlos en las siguientes tarjetas
6. **Gestión del tiempo de espera**: Si el script tarda demasiado, se detiene y devuelve lo que tiene

---

## Explicación de los parámetros

### DocOperator Prompt/Script
El script de automatización que indica a DocOperator exactamente qué hacer

**Ejemplo (en lenguaje sencillo):**
```
1. Go to https://supplier.com/login
2. Enter username: myuser
3. Enter password: mypass
4. Click Login button
5. Search for product "ABC123"
6. Extract the price
7. Return the price
```

### Variables
Datos que desea pasar AL script

**Ejemplo:**
```
product_id: "ABC123"
supplier_code: "SUPP-001"
```

Estas variables pueden usarse en el script de la siguiente manera:
```
Search for product "{product_id}"
Find supplier "{supplier_code}"
```

### Maximum Steps
Cuántas acciones puede realizar el bot

**Valores típicos:**
- Tarea simple (como obtener un precio): 10-20 pasos
- Complejidad media (rellenar formulario + extraer): 20-50 pasos
- Flujo de trabajo complejo (iniciar sesión + buscar + validar): 50-100 pasos

**Por qué es importante:** Evita bucles infinitos y scripts de ejecución muy larga

### Maximum Retries
Si el bot falla una acción, ¿cuántas veces debe volver a intentarlo?

**Ejemplos:**
- 1: Intentarlo una vez; si falla, continuar
- 3: Intentarlo 3 veces antes de rendirse
- 5: Muy persistente: intentarlo 5 veces

---

## Ejemplo paso a paso

### Escenario: Obtener los precios del proveedor desde el sitio web

**Definición del script:**
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

**Script que usa variables:**
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

---

## Tipos de acciones que DocOperator puede realizar

### Navegación
- Ir a una URL
- Hacer clic en enlaces
- Pulsar botones
- Desplazar la página

### Rellenado de formularios
- Escribir texto en los campos
- Seleccionar opciones desplegables
- Marcar/desmarcar casillas
- Hacer clic en botones

### Extracción de datos
- Leer texto de la página
- Extraer números
- Obtener datos de tablas
- Copiar información

### Espera
- Esperar a que se cargue la página
- Esperar a que aparezcan los elementos
- Esperar el contenido dinámico

### Lógica condicional
- Si algo existe, hacer esto
- Si el texto coincide, entonces...
- Contar resultados y actuar en consecuencia

---

## Casos de uso comunes

### 1. Obtener precios en tiempo real
**Escenario:** El proveedor no tiene API pero el sitio web muestra los precios

**Script:**
```
1. Go to supplier website
2. Search for product
3. Extract price from results
4. Return price to DocFlow
5. Use price to validate invoice
```

### 2. Comprobar la disponibilidad de inventario
**Escenario:** Necesita saber si el proveedor tiene existencias

**Script:**
```
1. Log into supplier portal
2. Search for product
3. Extract availability status
4. Extract delivery time
5. Return both to DocFlow
```

### 3. Envío automático de formularios
**Escenario:** Necesita rellenar un formulario en un sitio externo

**Script:**
```
1. Navigate to form page
2. Fill Company Name field
3. Fill Contact Email field
4. Select Country from dropdown
5. Upload file attachment
6. Click Submit button
7. Capture confirmation message
```

### 4. Verificación de la entrada de datos
**Escenario:** Verificar que los datos coinciden en dos sistemas diferentes

**Script:**
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

---

## Pasos de configuración

### Paso 1: Crear el script
1. Defina lo que desea lograr
2. Divídalo en pasos pequeños
3. Escriba cada paso con claridad
4. Pruébelo primero manualmente (abra el sitio web y hágalo usted mismo)
5. Documente exactamente qué hace clic, dónde escribe y qué extrae

### Paso 2: Identificar las variables
1. ¿Qué datos cambiarán entre documentos?
2. ¿Qué debe pasarse al script?
3. Defina los nombres de las variables
4. Especifique dónde se usan las variables en el script

### Paso 3: Establecer los parámetros
- **Maximum Steps**: Según la complejidad del script
- **Maximum Retries**: ¿Qué grado de persistencia debe tener el bot?
- **Timeout**: ¿Cuánto tiempo debe esperar a las páginas?

### Paso 4: Probar
1. Pruebe con datos de muestra
2. Verifique que el bot puede acceder al sitio web
3. Verifique que la extracción es correcta
4. Compruebe si las variables funcionan correctamente

---

## Consejos para escribir scripts

### Lenguaje claro
✅ **Haga:**
```
1. Click the "Login" button
2. Type the username in the login field
3. Wait 2 seconds for form to process
```

❌ **No haga:**
```
1. Do the login thing
2. Enter stuff
3. Wait for it
```

### Selectores específicos
✅ **Haga:**
```
Click the button labeled "Submit Order"
Type in the field with placeholder "Enter Email"
```

❌ **No haga:**
```
Click somewhere
Type in a field
```

### Gestión de errores
✅ **Haga:**
```
1. Try to click "Next" button
2. If button not found, extract data from current page
3. Return what we have
```

❌ **No haga:**
```
Click "Next" (assumes it's always there)
```

---

## Resolución de problemas

### "Script Timed Out"
**Causa:** El script tardó demasiado en completarse

**Soluciones:**
- [ ] Reduzca el número de acciones
- [ ] Aumente el valor de "Maximum Steps"
- [ ] Optimice el script para una ejecución más rápida
- [ ] Simplifique lo que intenta extraer

### "Element Not Found"
**Causa:** DocOperator no pudo encontrar el botón/campo que especificó

**Soluciones:**
- [ ] Verifique que el nombre del botón/campo es exactamente correcto
- [ ] Compruebe si el diseño del sitio web ha cambiado
- [ ] Añada tiempo de espera antes de hacer clic
- [ ] Compruebe si el botón solo aparece bajo determinadas condiciones

### "Login Failed"
**Causa:** Fallo de autenticación

**Soluciones:**
- [ ] Verifique que el usuario/contraseña son correctos
- [ ] Compruebe si la contraseña tiene caracteres especiales
- [ ] Verifique que la cuenta no está bloqueada
- [ ] Compruebe si el proceso de inicio de sesión ha cambiado

### "Data Not Extracted Correctly"
**Causa:** El script se ejecutó pero extrajo información incorrecta

**Soluciones:**
- [ ] Verifique que se seleccionó el campo correcto
- [ ] Compruebe si los datos están en la ubicación esperada
- [ ] Pruebe manualmente la lógica de extracción
- [ ] Añada pasos de depuración para verificar qué hay en la página

### "Script Runs Slowly"
**Causa:** Demasiados pasos o sitio web lento

**Soluciones:**
- [ ] Elimine los pasos innecesarios
- [ ] Optimice los tiempos de espera
- [ ] Compruebe la conexión a internet
- [ ] Considere si existe una alternativa de API

---

## Buenas prácticas

✅ **Haga:**
- Pruebe los scripts exhaustivamente antes de desplegarlos
- Mantenga los scripts simples y enfocados
- Añada comentarios que expliquen cada paso
- Use nombres de variables significativos
- Supervise el rendimiento del script
- Tenga un plan alternativo para cuando los scripts fallen

❌ **No haga:**
- Crear scripts extremadamente largos (>100 pasos)
- Poner contraseñas confidenciales en los registros
- Confiar en coordenadas exactas (los sitios web cambian)
- Crear bucles sin condiciones de salida
- Ignorar los mensajes de error

---

## Consejos de rendimiento

- **Elimine los pasos no utilizados**: Cada paso lleva tiempo
- **Combine acciones similares**: Agrupe los clics relacionados
- **Optimice las esperas**: Use solo los retrasos necesarios
- **Almacene datos en caché**: No extraiga los mismos datos dos veces
- **Procesamiento en paralelo**: Ejecute varios scripts si es posible

---

## Consideraciones de seguridad

⚠️ **Importante:**
- No almacene contraseñas en DocFlow
- Use métodos seguros para pasar las credenciales
- No registre datos confidenciales
- Supervise lo que se está extrayendo
- Asegúrese de que la actividad del bot se registre y sea auditable

---

## Ejemplo de variables

### Variables disponibles que puede usar:
```
{invoice_number} - From document field
{supplier_code} - From document field
{product_id} - From document field
{quantity} - From document field
{currency} - From document field
```

### Script que usa variables:
```
1. Go to https://supplier.com/api/lookup
2. Enter supplier code: {supplier_code}
3. Search for product: {product_id}
4. Enter quantity: {quantity}
5. Extract price in currency: {currency}
6. Return extracted price
```

---

## Comparación: cuándo usar DocOperator frente a API

| Situación | Usar DocOperator | Usar API |
|-----------|-----------------|---------|
| El sitio web tiene API | ❌ No | ✅ Sí |
| El sitio web es interactivo | ✅ Sí | ❌ No |
| Requiere inicio de sesión | ✅ Sí | Depende |
| Se necesita mucha rapidez | ❌ No | ✅ Sí |
| Flujo de trabajo complejo | ✅ Sí | ❌ Quizá no |
| Los datos cambian a diario | ✅ Sí | ✅ Sí |

---

## Tarjetas relacionadas

- **CALL_API** - Úsela cuando haya una API disponible en su lugar
- **ACTION_HTTPS_REQUEST** - Solicitudes más simples
- **ACTION_SET_FIELD_TO_TEXT** - Usar los datos extraídos
- **CONDITION_HTTPS_REQUEST_STATUS** - Comprobar el estado de la solicitud
