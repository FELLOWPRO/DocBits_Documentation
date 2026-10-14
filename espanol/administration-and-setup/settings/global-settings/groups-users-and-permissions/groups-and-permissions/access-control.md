# Control de Acceso

## Resumen

El Control de Acceso define, para un único **grupo** (rol), exactamente qué pueden hacer sus miembros — tanto a **nivel de tipo de documento** (qué tipos de documento ven y qué acciones pueden realizar) como a **nivel de campo** (qué campos individuales pueden leer o editar).

Los permisos siempre se evalúan **por grupo**. Un usuario hereda los permisos de cada grupo al que pertenece.

{% hint style="info" %}
El Control de Acceso solo se aplica cuando el sistema de **Grupos y Permisos** está activado (consulte [Activar Permisos](activating-permissions.md)). **Los administradores siempre omiten el Control de Acceso** y pueden ver y hacer todo, independientemente de la configuración de esta página.
{% endhint %}

Cada grupo puede configurarse para:

* **Acceso al documento** — si el grupo puede usar un tipo de documento.
* **Permisos de acción** — qué acciones (listar, ver, editar, eliminar, actualización masiva, aprobar) puede realizar el grupo y *para qué documentos*.
* **Permisos de campo** — si cada campo individual de un tipo de documento es editable, de solo lectura u oculto.

## Activación

1. Vaya a **Configuración**.
2. Seleccione **Procesamiento de Documentos**.
3. Seleccione **Módulo.**
4. Active el **Control de Acceso** habilitando el control deslizante.

<figure><img src="../../../../../.gitbook/assets/Access-Control3_es.png" alt=""><figcaption></figcaption></figure>

## Abrir el Control de Acceso de un grupo

1. Vaya a **Configuración**.
2. Vaya a **Configuración Global**.
3. Seleccione **Grupos, Usuarios y Permisos**.
4. Seleccione **Grupos y Permisos**.
5. Para gestionar los permisos de un grupo (por ejemplo, PROCUREMENT\_DIRECTOR), haga clic en los tres puntos del lado derecho.
6. Seleccione **Gestionar Control de Acceso**.

<figure><img src="../../../../../.gitbook/assets/access_control_open_menu.png" alt="Abrir el menú de fila de un grupo y elegir Gestionar Control de Acceso"><figcaption><p>En la página «Grupos y Permisos», abra el menú <strong>⋮</strong> de un grupo y elija <strong>Gestionar Control de Acceso</strong>.</p></figcaption></figure>

## Cómo se evalúa un permiso

Cuando un usuario intenta hacer algo con un documento, DocBits comprueba, en orden:

1. **¿Está activado el sistema de Grupos y Permisos y el usuario no es administrador?** Si está desactivado, o el usuario es administrador → acceso total.
2. **¿Está el tipo de documento habilitado para uno de los grupos del usuario?** Si está deshabilitado → el usuario no puede ver ni usar ese tipo de documento.
3. **¿Qué ámbito de acceso está establecido para la acción?** (por ejemplo, *Editar = Owner*). El ámbito se compara con la relación del usuario con *este documento concreto*: ¿es el propietario, el asignado, ambos o ninguno?
4. **¿Qué permiso de campo se aplica?** Incluso cuando un usuario puede abrir un documento, ciertos campos pueden seguir ocultos o bloqueados.

## Permisos a nivel de tipo de documento

Cada fila de la matriz es un tipo de documento (Invoice, Credit Note, Purchase Order, …).

La primera columna es un interruptor **Habilitado / Deshabilitado**. Deshabilítelo y el grupo no podrá usar ese tipo de documento en absoluto — desaparece de su panel. Habilítelo y las siete columnas de acción se vuelven editables.

| Acción | Determina si el grupo puede… |
|--------|------------------------------|
| **Listar** | ver el tipo de documento en la lista del panel. |
| **Ver** | abrir un documento y ver sus detalles. |
| **Editar** | cambiar los valores de los campos de un documento. |
| **Eliminar** | eliminar un documento. |
| **Actualización Masiva** | aplicar una actualización masiva a varios documentos a la vez. |
| **Primera Aprobación** | otorgar la aprobación de primer nivel. |
| **Segunda Aprobación** | otorgar la aprobación de segundo nivel. |

### Ámbitos de acceso

Cada columna de acción es un desplegable. El valor que elija responde a la pregunta *«¿para qué documentos puede el grupo hacer esto?»*. Los nombres de los ámbitos aparecen en inglés en la interfaz:

| Ámbito | Quién está permitido | Efecto en un documento |
|--------|----------------------|------------------------|
| **No Access** | Nadie en el grupo. | La acción está bloqueada para todos en el grupo — el botón se oculta o se desactiva. |
| **Everyone** | Todos los miembros del grupo. | Cualquier miembro del grupo puede realizar la acción en **cualquier** documento de este tipo. |
| **Owner** | Solo el usuario que **creó / cargó** el documento. | La acción solo funciona en documentos que el propio usuario cargó. |
| **Assignee** | Solo el usuario (o grupo) al que está **asignado** el documento. | La acción solo funciona en documentos asignados al usuario o a un grupo al que pertenece. |
| **Owner & Assignee** | El propietario **o** el asignado. | La acción funciona si el usuario es *o bien* quien lo cargó *o bien* el asignado. |

{% hint style="info" %}
**Owner** y **Assignee** dependen de la *relación entre el usuario y cada documento individual*, por lo que dos miembros del mismo grupo pueden tener derechos diferentes sobre la misma factura — consulte el ejemplo práctico más abajo.
{% endhint %}

<figure><img src="../../../../../.gitbook/assets/access_control_matrix.png" alt="Matriz de Control de Acceso de un grupo"><figcaption><p>La matriz de permisos por tipo de documento. Aquí el tipo <strong>Invoice</strong> está habilitado y sus acciones tienen distintos ámbitos de acceso; los demás tipos están deshabilitados.</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/access_control_scope_dropdown.png" alt="Desplegable de ámbitos de acceso"><figcaption><p>Cada columna de acción ofrece los mismos cinco ámbitos de acceso.</p></figcaption></figure>

### La aprobación también requiere Editar

Aprobar un documento desencadena **dos acciones** internamente: DocBits primero **guarda** el documento y luego lo pasa al estado aprobado. El paso de guardado necesita el permiso **Editar**, por lo que ambos permisos están vinculados.

Un usuario al que solo se le concede **Primera Aprobación** o **Segunda Aprobación** — pero *no* **Editar** — se encuentra con un error de permisos en el paso de guardado y no puede aprobar el documento.

{% hint style="warning" %}
Siempre que conceda **Primera Aprobación** o **Segunda Aprobación**, conceda también **Editar** (y **Ver**) para el mismo tipo de documento. Un permiso de aprobación por sí solo no es suficiente.
{% endhint %}

## Permisos a nivel de campo

Haga clic en una fila de tipo de documento para abrir el panel **Permisos de Campo** debajo. Los campos están organizados en pestañas (por ejemplo, *Columnas de tabla*, *Detalles de la factura*, *Detalles de pago*, *Tasas e importes*). Cada campo tiene su propio nivel de acceso:

| Nivel | Efecto en el campo |
|-------|--------------------|
| **Lectura/Escritura** | El campo es visible **y** editable. |
| **Solo lectura** | El campo es visible pero **no se puede editar** (atenuado). |
| **Aprobación** | El campo puede editarse, pero el cambio debe pasar por un **flujo de aprobación** antes de aplicarse. |
| **Sin acceso** | El campo está **completamente oculto** — el usuario nunca lo ve. |

{% hint style="info" %}
Las reglas de campo se aplican por igual a **todos** los miembros del grupo — no dependen del propietario/asignado. Úselas para ocultar o bloquear campos sensibles (por ejemplo, un descuento o un importe total) para todo un grupo.
{% endhint %}

<figure><img src="../../../../../.gitbook/assets/access_control_field_permissions.png" alt="Panel de Permisos de Campo"><figcaption><p>El panel «Permisos de Campo» para el tipo Invoice. <code>CUSTOMER_DISCOUNT</code> está oculto (Sin acceso) mientras que los demás campos permanecen en Lectura/Escritura.</p></figcaption></figure>

## Ejemplo práctico: qué hace el Control de Acceso en una factura real

Suponga que crea un grupo **AP_CLERK** para sus administrativos de cuentas por pagar y configura el tipo de documento **Invoice** así:

**Permisos de tipo de documento para Invoice**

| Acción | Ámbito |
|--------|--------|
| Habilitado | ✅ Sí |
| Listar | Everyone |
| Ver | Everyone |
| Editar | Owner & Assignee |
| Eliminar | No Access |
| Actualización Masiva | No Access |
| Primera Aprobación | Assignee |
| Segunda Aprobación | No Access |

**Permisos de campo para Invoice**

| Campo | Nivel |
|-------|-------|
| `TOTAL_AMOUNT` | Solo lectura |
| `CUSTOMER_DISCOUNT` | Sin acceso |
| *(todos los demás campos)* | Lectura/Escritura |

Ahora siga un documento concreto — la factura **INV-4711**, que **Maria cargó** y que está **asignada a Maria**. Tanto Maria como su colega Tom están en el grupo **AP_CLERK**.

**Maria (propietaria *y* asignada de INV-4711):**

* ✅ Ve INV-4711 en la lista del panel *(Listar = Everyone)*.
* ✅ La abre *(Ver = Everyone)*.
* ✅ Edita el nombre del proveedor y las líneas *(Editar = Owner & Assignee — es la propietaria)*.
* 🔒 Ve `TOTAL_AMOUNT`, pero el campo está atenuado y no puede cambiarlo *(Solo lectura)*.
* 🚫 Nunca ve el campo `CUSTOMER_DISCOUNT` *(Sin acceso)*.
* 🚫 El botón **Eliminar** está oculto *(Eliminar = No Access — nadie en el grupo puede eliminar)*.
* ✅ Puede otorgar la **primera aprobación** *(Primera Aprobación = Assignee — es la asignada)*.

**Tom (mismo grupo, pero *no* cargó INV-4711 y *no* le está asignada):**

* ✅ La ve en la lista y ✅ la abre *(Listar y Ver = Everyone)*.
* 🚫 No puede editar nada — el documento se abre en **solo lectura** *(Editar = Owner & Assignee — Tom no es ninguno)*.
* 🔒 / 🚫 Ve exactamente la misma visibilidad de campos que Maria: `TOTAL_AMOUNT` bloqueado, `CUSTOMER_DISCOUNT` oculto *(las reglas de campo se aplican a todo el grupo)*.
* 🚫 No puede otorgar la primera aprobación *(Primera Aprobación = Assignee — no es Tom)*.
* 🚫 No puede eliminar *(No Access)*.

**Lo que muestra este ejemplo**

* **Everyone** abre un documento para todos los miembros del grupo; **Owner / Assignee** reduce una acción a las personas vinculadas a ese documento concreto.
* **No Access** elimina una acción (Eliminar) u oculta un campo (`CUSTOMER_DISCOUNT`) para todo el grupo.
* **Solo lectura** mantiene un campo visible como referencia (`TOTAL_AMOUNT`) pero impide cambios.
* Dos personas del **mismo grupo** pueden tener **derechos diferentes sobre la misma factura**, únicamente por quién la cargó y a quién está asignada.
