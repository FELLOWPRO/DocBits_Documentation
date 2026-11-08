# Reglas de selección de diseño

## Descripción general

Un **layout** decide qué campos y grupos ve un usuario —y en qué orden— en las pantallas de **validation**, **approval**, **reject** y **review** de un documento. Los layouts se diseñan en el [Layout Manager](./).

Clásicamente, DocBits elegía el layout según el **origen** del documento: el país o la región tomados de los ajustes de idioma del documento, como `DE` o `US`. Cada origen tenía su propia copia del layout y nada más podía influir en la elección.

Con las **reglas de selección de layout**, los layouts se convierten en bloques reutilizables independientes del origen, y las **reglas** deciden qué layout recibe un documento:

> *Cuando* el documento cumple una condición, *entonces* recibe este layout. Las reglas se comprueban de arriba abajo; **gana la primera regla que coincide**. Si ninguna regla coincide, se utiliza el **layout predeterminado**.

El origen sigue estando disponible, como una condición más entre muchas. Una regla puede mirar igualmente al proveedor, al importe, al estado del documento, al método de extracción o a cualquier campo de cabecera.

### Problemas que resuelven

| Requisito | Layouts clásicos basados en el origen | Con reglas de selección |
| --- | --- | --- |
| Las facturas de un proveedor necesitan campos adicionales (proyecto, número de aduanas) | imposible sin un origen nuevo | regla _Supplier ID is 20723_ → layout "Invoice with project fields" |
| Los documentos DE, AT y CH deben tener el mismo aspecto | tres copias del mismo layout que mantener | un layout, una regla por origen (o un grupo ANY) que apunta a él |
| Las facturas electrónicas necesitan una pantalla más sencilla que los PDF escaneados | no es posible | regla _Extraction Method is ELECTRONIC\_DOCUMENT_ → layout "E-invoice" |
| Las facturas de gran importe necesitan más campos en la pantalla de aprobación | no es posible | regla de Approval _Total Amount greater than 10000_ → layout "High value approval" |
| El segundo aprobador debe ver una pantalla distinta de la del primero | un tipo de layout "second approval" aparte | regla de Approval _Document Status is Pending second approval_ → layout "Second approval" |

## Activar los layouts basados en reglas

Los layouts basados en reglas los activa **por tipo de documento** un **administrador de la organización**.

1. Vaya a **Settings → Document Processing → Document Types**.
2. Haga clic en el icono de **settings** (engranaje) de la tarjeta del tipo de documento.
3. Abra **Manage Layouts** y active el interruptor.

<figure><img src="../../../../../.gitbook/assets/lsr-manage-layouts-toggle-en-20261102.png" alt="La sección Manage Layouts en los ajustes adicionales de un tipo de documento, con el subtítulo Enable Layout Management y el interruptor Manage Layouts activado."><figcaption><p>El interruptor Manage Layouts en los ajustes adicionales de un tipo de documento</p></figcaption></figure>

El enlace **Layouts** de la tarjeta del tipo de documento abre ahora **Layouts & Selection Rules**.

### Qué ocurre al activarlo

DocBits convierte sus layouts existentes basados en el origen en reglas, una sola vez, para este tipo de documento y para cada pantalla:

* El layout del origen **DEFAULT** pasa a ser el **layout predeterminado** (el de reserva).
* Cada layout de un origen concreto pasa a ser una regla **"Layout for XX"** con la condición _Document Origin is XX_, que apunta a ese layout. Estas reglas reciben prioridades en pasos de 10 (por ejemplo 2000, 2010, 2020 …), de modo que puede colocar sus propias reglas antes, entre o después de ellas.

<figure><img src="../../../../../.gitbook/assets/lsr-default-layout-row-en-20261102.png" alt="La parte inferior de la lista de reglas de selección: las últimas reglas de origen Layout for UY y Layout for VN, seguidas de la fila FALLBACK Default layout marcada como is_default, que se usa cuando ninguna regla anterior coincide."><figcaption><p>Las reglas de origen creadas al activar, seguidas del layout predeterminado (FALLBACK)</p></figcaption></figure>

No se elimina ni se modifica nada en los propios layouts. Por tanto, justo después de la activación cada documento recibe exactamente el layout que recibía antes. El comportamiento solo cambia cuando usted añade o modifica reglas.

**Al desactivarlo**, el tipo de documento vuelve de inmediato a la selección basada en el origen. Las reglas se conservan pero no se utilizan, y vuelven a surtir efecto cuando vuelve a activar el interruptor.

## La pantalla Layouts & Selection Rules

<figure><img src="../../../../../.gitbook/assets/lsr-layouts-overview-en-20261102.png" alt="La pestaña Layouts de Layouts & Selection Rules para el tipo de documento INVOICE: las pestañas de pantalla Field Validation, Approval, Reject y Review, el filtro All, My layouts y System, el botón New layout y tarjetas de layout con Edit, Clone y Delete."><figcaption><p>La pestaña Layouts: cada layout del tipo de documento como una tarjeta</p></figcaption></figure>

* **Layouts / Selection rules** (en la cabecera de la página) alternan entre la lista de layouts y la lista de reglas. Los números indican cuántos hay.
* **Field Validation / Approval / Reject / Review** cambian la **pantalla**. Cada pantalla tiene sus propios layouts, sus propias reglas y su propio layout predeterminado: una regla de Approval nunca cambia la pantalla de validación.
* En la pestaña **Layouts** puede crear, editar, clonar y eliminar layouts. Cada tarjeta indica si una regla utiliza el layout ("Not targeted by rules" cuando ninguna lo hace). Filtre con **All / My layouts / System**; los layouts del sistema se incluyen con DocBits y se pueden ver y clonar, pero no modificar.

{% hint style="info" %}
La primera y la segunda aprobación comparten los layouts y las reglas de **Approval**. Para dar a la segunda fase de aprobación su propia pantalla, añada una regla de Approval con la condición _Document Status is Pending second approval_; véase el [ejemplo](layout-selection-rules.md#different-screens-for-first-and-second-approval).
{% endhint %}

## Cómo se elige un layout

Cada vez que se abre un documento, y de nuevo después de guardarlo, DocBits decide su layout para la pantalla actual:

1. Se comprueban las **reglas activas** de la pantalla por orden de **prioridad** (primero el número más bajo). **Gana la primera regla cuya condición es verdadera** y se utiliza su layout.
2. Si ninguna regla coincide, se utiliza el **layout predeterminado**.
3. Si tampoco hay layout predeterminado, DocBits recurre a la elección clásica basada en el origen.

Las reglas cuyo layout se ha eliminado o está vacío se omiten.

### Un ejemplo práctico

Reglas de la pantalla **Field Validation**:

| Prioridad | Regla | Condición | Layout |
| --- | --- | --- | --- |
| 5 | Behaelterbau invoices | _Supplier ID is HP0000278_ | Invoice with project fields |
| 10 | E-invoices | _Extraction Method is ELECTRONIC\_DOCUMENT_ | E-invoice |
| 2020 | Layout for DE | _Document Origin is DE_ | Field Validation Layout (DE) |
| — | Default layout | — | Field Validation Layout (Base) |

Qué layout recibe cada documento:

| Documento | Proveedor | Extracción | Origen | Layout | Porque |
| --- | --- | --- | --- | --- | --- |
| 1 | HP0000278 | e-invoice | DE | Invoice with project fields | la prioridad 5 coincide primero; las reglas posteriores no se comprueban |
| 2 | 10040 | e-invoice | DE | E-invoice | la prioridad 5 no coincide, la 10 sí |
| 3 | 10040 | scanned PDF | DE | Field Validation Layout (DE) | solo coincide la regla de origen |
| 4 | 10040 | scanned PDF | US | Field Validation Layout (Base) | ninguna regla coincide → predeterminado |

**El orden importa**: coloque las reglas específicas (un proveedor) por encima de las generales (un país).

### Cuando un usuario cambia un campo que miran las reglas

El layout se elige siempre a partir de los valores **actuales** del documento. Si un usuario corrige, por ejemplo, el proveedor en la pantalla de validación, DocBits vuelve a elegir el layout tras el guardado y la pantalla puede cambiar a otro layout. No se pierde ningún dato: un campo que no forma parte del nuevo layout conserva su valor; simplemente no se muestra hasta que vuelva a aplicarse un layout que lo contenga.

## Gestionar las reglas de selección

<figure><img src="../../../../../.gitbook/assets/lsr-rules-list-en-20261102.png" alt="La pestaña Selection rules de la pantalla Field Validation: una tabla con las columnas Priority, Rule y condiciones, Target layout, Source y Active, la primera fila marcada como FIRST, tiradores de arrastre a la izquierda y un menú de tres puntos en cada fila."><figcaption><p>La pestaña Selection rules de la pantalla Field Validation</p></figcaption></figure>

Cada fila muestra la **prioridad** (la primera fila está marcada como **FIRST**), el **nombre y la clave de la regla** con sus **condiciones**, el **layout de destino**, la insignia de **origen** y un interruptor **Active**.

| Tarea | Cómo |
| --- | --- |
| Crear una regla | **New rule** |
| Editar una regla | Haga clic en la fila |
| Cambiar el orden | Arrastre el tirador de la izquierda de una fila hacia arriba o hacia abajo. El nuevo orden se guarda de inmediato. |
| Desactivar una regla | Interruptor **Active**. Las reglas inactivas se ignoran. |
| Duplicar o eliminar | Menú **⋮** de la fila |
| Buscar una regla | **Search rules…** |

La insignia de **origen** indica de dónde procede una regla: las reglas **System** se incluyen con DocBits. Al editar una se crea una copia para su organización, que se muestra como **Customized**; el original permanece intacto y se puede restaurar. Las reglas que usted crea son **Custom**.

### El layout predeterminado

La última fila, marcada como **FALLBACK** e **is\_default**, es el layout predeterminado: se utiliza siempre que ninguna regla anterior coincide y no tiene condición. Se crea al activar la función (a partir del layout del origen DEFAULT).

{% hint style="info" %}
Para usar otro layout de reserva, cree una regla **sin ninguna condición** y asígnele el número de prioridad más alto, de modo que se compruebe en último lugar. Coincide con todos los documentos con los que no coincidió ninguna regla anterior, antes de llegar al layout predeterminado.
{% endhint %}

## Crear una regla

Haga clic en **New rule** en la pestaña Selection rules de la pantalla que desea cambiar.

<figure><img src="../../../../../.gitbook/assets/lsr-rule-editor-en-20261104.png" alt="El editor de reglas de selección de layout para una factura: la frase resumen en la parte superior, después Step 1 Scope and priority con Rule name, Rule key, Document Type, Layout Type, Priority y una casilla Log execution, Step 2 Applies when con la condición Document Origin is AR y los botones Add Condition y Add nested group, Step 3 Target layout con el Field Validation Layout (AR) seleccionado, y el panel de vista previa en vivo a la derecha con Sample document, matched_by, Resolved layout, Priority hit y watched_fields."><figcaption><p>El editor de reglas: ámbito y prioridad, las condiciones, el layout de destino y la vista previa en vivo de lo que haría la regla.</p></figcaption></figure>

La frase de la parte superior resume la regla a medida que la construye: "When doc.doc_origin = AR, an INVOICE document gets the origin-ar layout for Field validation. Checked at priority 0 — the first matching rule wins."

### Paso 1 — Scope & priority

| Ajuste | Qué hace |
| --- | --- |
| **Rule Name** | Se muestra en la lista de reglas. Describa el caso de negocio: "Behaelterbau invoices", "E-invoices", "High value approval". |
| **Rule key** | Se genera a partir del nombre; se mantiene igual cuando cambia el nombre de la regla. |
| **Document Type** / **Layout type** | El tipo de documento y la pantalla a los que se dirige la regla. Se toman del lugar donde hizo clic en **New rule**. |
| **Priority** | Los números más bajos se comprueban primero. Deje huecos (5, 10, 20 …) para poder insertar reglas más adelante. |
| **Log execution** | Registra cada evaluación de la regla para que pueda seguir después por qué un documento coincidió o no. Déjelo desactivado hasta que necesite esa traza. |

### Paso 2 — Applies when

La condición que debe cumplir un documento. Puede utilizar:

* **atributos del documento**: Document Origin, Extraction Method, Document Status, Sub Document Type,
* **campos de cabecera**: Supplier ID, Total Amount, Currency, Purchase Order y todos los demás campos del tipo de documento,
* una **ruta JSON personalizada** (Advanced).

Las columnas de tabla no están disponibles: el layout se elige una sola vez para todo el documento.

Deje el paso vacío para que coincida con todos los documentos en esta prioridad. Cómo funcionan las condiciones —ALL / ANY, grupos anidados, todos los operadores, valores vacíos, mayúsculas/minúsculas— se explica en [Rule Conditions (Applies when)](../rule-conditions-applies-when.md).

### Paso 3 — Layout de destino

Haga clic en el layout que debe recibir el documento. La lista muestra sus propios layouts y los layouts del sistema de la pantalla seleccionada. Un layout no se puede eliminar mientras una regla siga apuntando a él.

### Vista previa en vivo · /resolve

El panel de la derecha muestra lo que hace la regla para un documento de muestra que tiene los valores de sus condiciones:

| Línea | Significado |
| --- | --- |
| **Sample document** | Los valores utilizados para la vista previa, tomados de sus condiciones |
| **matched\_by** | `rule` si coincidió una regla; en caso contrario, el predeterminado |
| **Resolved layout** | El layout que recibiría el documento de muestra |
| **Priority hit** | La prioridad de la regla que coincidió |
| **watched\_fields** | Los campos de los que depende la elección del layout. Cuando un usuario cambia uno de ellos, el layout se vuelve a elegir. |

Haga clic en **Create Rule** (o **Save rule** al editar) para guardar. **Cancel** vuelve a la lista de reglas.

## Ejemplos

### Campos adicionales para un proveedor

Pantalla **Field Validation** · prioridad **5** · _Supplier ID is HP0000278_ · destino _Invoice with project fields_ (un clon de su layout estándar con los campos adicionales de proyecto y centro de coste).

### Un layout para varios países

Pantalla **Field Validation** · prioridad **100** · **ANY of**: _Document Origin is Deutsch_, _Document Origin is Austria_, _Document Origin is Switzerland_ · destino _DACH invoice_. Desactive las reglas migradas "Layout for AT" y "Layout for CH" si apuntan a copias más antiguas.

### Una pantalla más sencilla para facturas electrónicas

Pantalla **Field Validation** · prioridad **10** · _Extraction Method is ELECTRONIC\_DOCUMENT_ · destino _E-invoice_ (sin campos relacionados con el OCR).

### Una pantalla de aprobación más estricta para importes altos

Pantalla **Approval** · prioridad **10** · _Total Amount greater than 10000_ · destino _High value approval_ (que muestra centro de coste, responsable del presupuesto y número de contrato).

### Pantallas distintas para la primera y la segunda aprobación

Pantalla **Approval** · prioridad **5** · _Document Status is Pending second approval_ · destino _Second Approval Layout_. Los documentos en la primera fase de aprobación no coinciden y reciben el layout predeterminado de Approval.

<figure><img src="../../../../../.gitbook/assets/lsr-rule-editor-approval-en-20261104.png" alt="Una regla de selección de Approval en el editor: Rule name Layout for DE, prioridad 2000, las condiciones Document Status is Pending second approval y Document Origin is Deutsch, el layout de destino Second Approval Layout (DE) y la vista previa en vivo que muestra el documento de muestra, matched_by rule, el layout resuelto y priority hit 2000."><figcaption><p>Una regla de Approval para la segunda fase de aprobación: la vista previa en vivo de la derecha ya muestra que esta regla gana con la prioridad 2000.</p></figcaption></figure>

### Una pantalla de rechazo especial para algunos proveedores

Pantalla **Reject** · prioridad **10** · _Supplier ID is one of_ `10040, 10041` · destino _Reject with reason codes_.

## Buenas prácticas

* **Lo específico antes que lo general.** Las reglas de proveedor por encima de las de país, y las de país por encima del predeterminado.
* **Deje huecos en las prioridades** (5, 10, 20 …) para que las reglas nuevas encajen sin renumerar.
* **Base las condiciones en campos fiables.** El proveedor y el origen se establecen pronto y rara vez cambian. Las condiciones sobre campos que los usuarios editan con frecuencia hacen que la pantalla cambie de layout mientras trabajan.
* **Clone, no empiece desde cero.** Clone su layout estándar y ajústelo, para que todos los layouts mantengan la misma estructura básica.
* **Compruebe la vista previa en vivo** y abra un documento real de cada tipo después de cambiar reglas.
* **Mantenga un predeterminado con sentido** para cada pantalla, de modo que ningún documento se quede sin layout.

## Resolución de problemas

| Síntoma | Qué comprobar |
| --- | --- |
| Un documento recibe el layout equivocado | Coincide antes una regla anterior. Revise las reglas situadas por encima o el **Priority hit** de la vista previa. |
| Se usa el predeterminado aunque una regla debería coincidir | ¿Está la regla **Active**? ¿La condición coincide con el valor exacto (mayúsculas, espacios)? ¿Está la regla en la pestaña de **pantalla** correcta? |
| El layout cambia mientras un usuario trabaja | Se ha cambiado un campo de **watched\_fields**. Base la regla en un campo más estable. |
| Un layout no se puede eliminar | Una regla todavía apunta a él. Cambie el destino de esa regla o elimínela primero. |
| No se muestra ningún layout | Ninguna regla coincidió, no hay predeterminado y no existe un layout basado en el origen para esta pantalla. Añada una regla sin condición como comodín. |
| No cambió nada tras la activación | Es lo esperado: la activación reproduce la elección anterior basada en el origen. Añada sus propias reglas. |
| La segunda aprobación muestra el layout de la primera aprobación | Añada una regla de Approval sobre _Document Status is Pending second approval_ por encima de las demás reglas de Approval. |

## Relacionado

* [Rule Conditions (Applies when)](../rule-conditions-applies-when.md)
* [Custom Validation Rules](../custom-validation-rules.md)
* [Transformation Rules](../transformation-rules/)
* [Navigating the Layout Manager](navigating-the-layout-manager.md)
