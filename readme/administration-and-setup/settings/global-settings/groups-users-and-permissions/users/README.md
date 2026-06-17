# Usuarios

<figure><img src="../../../../../.gitbook/assets/users_settings.png" alt="Gestión de usuarios"><figcaption><p>Página de gestión de usuarios</p></figcaption></figure>

La página de Usuarios permite a los administradores gestionar todas las cuentas de usuario de su organización en DocBits. Aquí puede agregar nuevos usuarios, asignar roles y controlar el acceso.

## Lista de usuarios

La tabla de usuarios muestra las siguientes columnas:

| Columna | Descripción |
|--------|-------------|
| **Nombre** | El nombre completo del usuario. |
| **Correo electrónico** | La dirección de correo electrónico del usuario, que se utiliza como identificador de inicio de sesión. |
| **Último inicio de sesión** | Fecha y hora del inicio de sesión más reciente del usuario. |
| **Admin** | Casilla que indica si el usuario tiene privilegios de administrador. Los Admin pueden acceder a todos los ajustes y gestionar a otros usuarios. |
| **System Admin** | Casilla que indica el único System Admin de la organización: la cuenta que DocBits utiliza para acciones automáticas que ocurren en segundo plano (como las importaciones y exportaciones automatizadas). Un System Admin siempre tiene también privilegios de Admin. Consulte [Privilegios de administrador](admin-privileges.md#admin-vs-system-admin) para conocer la diferencia entre Admin y System Admin. |
| **Activo** | Casilla que muestra si la cuenta de usuario está actualmente activa. Los usuarios inactivos no pueden iniciar sesión. |
| **Acciones** | Menú con opciones como editar los datos del usuario, restablecer contraseñas o desactivar la cuenta. |

Utilice la barra de **Búsqueda** en la parte superior para encontrar rápidamente usuarios por nombre o ID.

## Análisis de inicios de sesión

Haga clic en **Análisis de inicios de sesión** para ver los datos de actividad de inicio de sesión de toda su organización, incluidos la frecuencia y los patrones de inicio de sesión.

## Agregar un nuevo usuario

1. Haga clic en el botón **Agregar usuario** en la esquina superior derecha.
2. Complete la información requerida:
   * **Nombre de usuario**: Un nombre único para el usuario.
   * **Nombre** y **Apellidos**: El nombre completo del usuario.
   * **Dirección de correo electrónico**: Se utiliza para iniciar sesión y recibir notificaciones.
   * **Contraseña**: Debe cumplir con las políticas de seguridad de su organización.
   * **Rol de usuario**: Asigne el rol adecuado (Standard User, Admin o System Admin).
3. Haga clic en **Guardar** para crear la cuenta de usuario. El nuevo usuario recibirá una notificación por correo electrónico con sus datos de inicio de sesión.

> **Nota:** El rol de **System Admin** solo se puede elegir al crear un usuario; no se puede agregar ni quitar más adelante. Cada organización puede tener un único System Admin, y al elegirlo se otorgan automáticamente también los derechos de Admin. Consulte [Privilegios de administrador](admin-privileges.md#admin-vs-system-admin) para saber cuándo conviene usarlo.
