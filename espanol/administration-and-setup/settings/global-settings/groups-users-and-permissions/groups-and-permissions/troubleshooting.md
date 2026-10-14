# Solución de Problemas de Control de Acceso y Problemas de Permisos

Si los usuarios experimentan restricciones de acceso inesperadas, como documentos faltantes, incapacidad para editar campos o acciones denegadas, utilice la siguiente lista de verificación para identificar y resolver el problema según cómo estén configurados los permisos en DocBits.

### 1. Verificar si el Control de Acceso está Habilitado

La configuración de Control de Acceso solo se aplica si la función está **habilitada**.

* Navegar a: `Configuración` > `Procesamiento de Documentos` > `Módulo`.
* Asegurarse de que el interruptor de **Control de Acceso** esté activado.
* Si está desactivado, todos los usuarios suelen tener acceso irrestricto independientemente de los permisos de grupo o campo.

### 2. Verificar Asignaciones de Grupo

Asegurarse de que el usuario esté asignado correctamente al grupo apropiado(s):

* Navegar a: `Configuración` > `Configuración Global` > `Grupos, Usuarios y Permisos`.
* Seleccionar **Grupos y Permisos**.
* Confirmar que el usuario esté listado bajo el grupo esperado.
* Si el grupo utiliza control de acceso específico, la falta de asignación de grupo bloqueará el acceso a documentos y acciones.

### 3. Revisar Permisos de Acceso de Grupo

El acceso se otorga por tipo de documento y por acción:

* En la pantalla de **Control de Acceso** para el grupo, verificar el tipo de documento (por ejemplo, Factura, Orden de Compra).
* Validar permisos como:
  * **Listar**, **Ver**, **Editar**, **Eliminar**, **Actualización Masiva**
  * **Niveles de Aprobación** (1º, 2º), **Desbloquear Documento**
* Asegurarse de que el nivel de acceso no esté limitado a **Propietario** o **Administrador** a menos que sea apropiado.

### 4. Confirmar Permisos a Nivel de Campo

El acceso también puede estar restringido a nivel de **campo**, lo que puede bloquear la edición o visibilidad:

* En la configuración de Control de Acceso del grupo, navegar al tipo de documento y verificar la configuración a nivel de campo.
* Confirmar si los campos están configurados como:
  * **Leer/Escribir**, **Solo Lectura**, **Escritura de Propietario**, **Ninguno**
* Ajustar si es necesario según el rol del usuario.

### 5. Verificar la Configuración de "Solo Documentos Asignados"

Esta configuración global limita la visibilidad de documentos:

* Navegar a: `Configuración` > `Configuración Global` > `Grupos, Usuarios y Permisos`.
* Si **Solo Documentos Asignados** está **habilitado**, los usuarios solo pueden ver documentos asignados explícitamente a ellos o a su grupo.
* Si los usuarios no pueden ver los documentos esperados:
  * Verificar las asignaciones de documentos.
  * Deshabilitar temporalmente la configuración para probar si es la causa raíz.

### 6. Probar con un Usuario o Grupo con Funcionamiento Conocido

Para aislar el problema:

* Iniciar sesión con un usuario de un grupo que tenga acceso confirmado.
* Comparar la visibilidad de documentos y las acciones disponibles.
* Esto ayuda a determinar si el problema es específico del usuario, del grupo o de todo el sistema.

### 7. Revisar Asignaciones de Documentos

Si "Solo Documentos Asignados" está **habilitado**, asegurarse de que:

* El documento esté **asignado** al usuario o a uno de sus grupos.
* Utilizar los controles de asignación en la vista detallada del documento para hacer o revisar asignaciones.

### 8. Restablecer o Reconfigurar Permisos

Si los permisos se cambiaron recientemente o los usuarios se movieron entre grupos:

* Confirmar que la configuración de Control de Acceso refleje las nuevas configuraciones de grupo.
* Ajustar los permisos de campo y documento según sea necesario.
* Si tiene dudas, crear un grupo de prueba con permisos amplios y probar el comportamiento de acceso antes de aplicar cambios a grupos en producción.
