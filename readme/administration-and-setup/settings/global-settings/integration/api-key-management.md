---
description: >-
  Cómo encontrar y crear las claves API que dan acceso a DocBits a otros sistemas
---

# API Key Management

Una API key permite que otro sistema — su ERP, un script o una aplicación de un socio — hable con DocBits sin que inicie sesión ningún usuario. Su organización puede tener tantas claves como necesite, y cada una se gestiona por separado: póngale su propio nombre, decida si caduca y revóquela individualmente si alguna vez queda expuesta.

Como cada integración puede tener su propia clave, puede desactivar una sin molestar a ninguna de las demás.

## Abrir la gestión de claves API

Vaya a **Settings** y seleccione **Integration & SSO** bajo **System & Administration**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-settings-overview.png)

La sección **API Key** de la parte superior de la página lista todas las claves que tiene su organización.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-list.png)

## Entender la lista

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-list-row.png)

| Columna | Qué le indica |
| --- | --- |
| **Key** | Los primeros caracteres de la clave, seguidos de `****`. El resto no se vuelve a mostrar nunca después de crearla — consulte [Crear una clave API](#crear-una-clave-api). |
| **Name** | El nombre que le dio a la clave, con su descripción debajo. |
| **Expires** | La fecha en la que la clave deja de funcionar, o **Never** si no puso ninguna. |
| **Last Used** | Cuándo llegó por última vez una petición con esta clave. **Never used** significa que ningún sistema la ha usado todavía — útil para detectar claves que puede quitar sin riesgo. |
| **Status** | **Active** significa que la clave funciona. Una clave revocada queda desactivada de forma permanente. |
| **Actions** | El menú de tres puntos, donde puede revocar la clave. |

Si tiene más claves de las que caben en una página, use los controles de paginación del final de la lista.

{% hint style="info" %}
**Last Used** es la forma más rápida de encontrar claves que ya no necesita nadie. Una clave que no se ha usado nunca, o que no se usa desde hace meses, es buena candidata para revocarla.
{% endhint %}

## Crear una clave API

1. Haga clic en **+ Create API Key** en la parte superior derecha de la sección API Keys.
2. Rellene el diálogo:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-create-dialog.png)

| Campo | Qué introducir |
| --- | --- |
| **Key Name** | Obligatorio. Póngale el nombre del sistema que la va a usar — `M3 Production`, `Invoice Import Script` — para que luego pueda saber a qué integración pertenece cada clave. |
| **Description** | Opcional. Espacio para una nota sobre para qué sirve la clave o quién la configuró. |
| **Expiration** | Elija una fecha de caducidad o déjelo en **Never expires**. Una fecha de caducidad es la opción más segura: la clave se retira sola si alguna vez se olvida la integración. |

3. Haga clic en **Create**. DocBits le muestra la clave nueva:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-created.png)

4. Copie la clave con el icono de copiar y péguela directamente en el sistema que la va a usar, o en su gestor de contraseñas.
5. Marque **I have copied and saved this key** y haga clic en **Done**.

{% hint style="danger" %}
**La clave completa se muestra una sola vez.** DocBits la guarda de forma cifrada que no puede revertirse al original, así que nadie — ni sus administradores ni el soporte de DocBits — puede volver a consultarla después. Si la pierde, revoque la clave y cree una nueva.
{% endhint %}

Trate la clave como una contraseña. Cualquiera que la tenga puede actuar sobre los documentos y los datos de su organización.
