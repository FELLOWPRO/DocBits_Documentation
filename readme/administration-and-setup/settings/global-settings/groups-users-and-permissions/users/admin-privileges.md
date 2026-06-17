# Privilegios de Administrador

El rol de un administrador es crucial para gestionar sistemas de TI, redes y plataformas digitales en una organización. Un administrador tiene permisos y responsabilidades avanzadas que le permiten controlar varios aspectos de la infraestructura técnica y garantizar que se opere de manera eficiente y segura. Estas son algunas de las principales responsabilidades de un administrador:

* **Gestión de usuarios:** Los administradores gestionan las cuentas de usuario, los derechos de acceso y los permisos. Crean nuevas cuentas de usuario, les asignan los permisos necesarios y gestionan el control de acceso para asegurar que solo los usuarios autorizados puedan acceder a determinados recursos.
* **Seguridad:** Los administradores son responsables de la seguridad de los sistemas de TI para protegerlos contra la pérdida de datos y el acceso no autorizado.
* **Solución de problemas y soporte:** El administrador suele ser el primer punto de contacto ante problemas técnicos. Ayuda a los usuarios a diagnosticar y resolver problemas y se asegura de que el sistema funcione sin contratiempos.

Además de estas responsabilidades, los administradores también se encargan de gestionar configuraciones sensibles y de garantizar que los sistemas cumplan los requisitos de conformidad y las mejores prácticas de seguridad de la información. Esto incluye gestionar datos sensibles, configurar controles de acceso y permisos, y supervisar y analizar los registros del sistema para identificar y abordar posibles riesgos de seguridad.

## Admin vs System Admin

DocBits tiene dos roles de administrador: **Admin** y **System Admin**. Suenan parecido, pero cumplen funciones distintas. Aquí va la versión sencilla.

### Admin — una persona que gestiona su organización

Un **Admin** es una persona real de su equipo que tiene permiso para gestionar DocBits. Los Admin pueden:

* Abrir todas las áreas de **Ajustes** y cambiar cómo funciona su organización.
* Agregar nuevos usuarios, editarlos, activarlos o desactivarlos y decidir quién más se convierte en Admin.
* Configurar grupos, permisos, integraciones y flujos de trabajo.

Puede tener **tantos Admin como necesite**, y puede otorgar o retirar el rol de Admin a cualquier usuario en cualquier momento. La mayoría de los administradores de su equipo son de este tipo.

### System Admin — la cuenta que DocBits utiliza para trabajar por su cuenta

Un **System Admin** es **una cuenta especial por organización** que DocBits utiliza para acciones que ocurren **de forma automática, sin que nadie haga clic en un botón**, por ejemplo, cuando los documentos se importan desde el correo electrónico, se exportan a otro sistema o los reenvía un servicio conectado en segundo plano.

Piense en ella como la cuenta «robot» de la organización. Cuando el sistema hace algo por su cuenta, lo hace **como el System Admin**, de modo que esa actividad automática sea fácil de reconocer y no se confunda con el trabajo de los miembros reales de su equipo.

Un System Admin es especial en tres aspectos:

* **También es siempre un Admin.** Al elegir System Admin, esa cuenta recibe automáticamente todos los derechos de Admin.
* **Solo hay uno por organización.** Una vez que existe un System Admin, no puede marcar a otro usuario como System Admin.
* **Solo se define al crear el usuario.** Esto se decide en el momento de agregar al usuario. **No se puede activar ni desactivar más adelante.**

> **Recomendación:** Cree una cuenta dedicada para este fin —por ejemplo, `system@your-company.com`— y márquela como System Admin. De esta manera, todo lo que DocBits haga de forma automática aparecerá claramente como **System Admin** en sus registros e historial de documentos, separado de sus usuarios reales.

### De un vistazo

| | Admin | System Admin |
|---|---|---|
| Acceso completo para gestionar la organización | Sí | Sí |
| Cuántos puede tener | Tantos como necesite | Solo uno |
| Se puede cambiar después de crear el usuario | Sí, en cualquier momento | No, solo se define al crearlo |
| Se usa para acciones automáticas en segundo plano | No | Sí |
| Siempre tiene derechos de Admin | — | Sí |

## Mejores prácticas de seguridad

La seguridad es un aspecto esencial de cualquier organización, especialmente cuando se trata de gestionar cuentas de usuario y derechos de acceso. Estas son algunas mejores prácticas para mantener un protocolo de gestión de usuarios seguro:

* **Actualizaciones regulares de contraseñas:** Anime a los usuarios a actualizar sus contraseñas con regularidad para mantener seguras sus cuentas. Establezca políticas de complejidad de contraseñas y exija el uso de contraseñas fuertes que incluyan una combinación de letras, números y caracteres especiales.
* **Supervisar las acciones de los administradores:** Implemente mecanismos para supervisar las actividades de los administradores y detectar actividades sospechosas o inusuales. Registre todas las acciones de los administradores, incluido el acceso a datos o configuraciones sensibles, para garantizar la rendición de cuentas e identificar posibles brechas de seguridad.
* **Limitar el número de administradores:** Reduzca el número de administradores al mínimo y otorgue privilegios administrativos solo a quienes realmente los necesiten. Al limitar el número de administradores, minimiza el riesgo de brechas de seguridad y facilita la gestión y supervisión de las cuentas de usuario.
* **Autenticación de dos factores (2FA):** Implemente la autenticación de dos factores en las cuentas de administrador para aumentar aún más la seguridad. Esto introduce un paso de seguridad adicional que garantiza que, incluso si se compromete una contraseña, un atacante no obtenga acceso no autorizado a la cuenta.
* **Revisiones de seguridad periódicas:** Realice revisiones y auditorías de seguridad periódicas para identificar y corregir posibles brechas o vulnerabilidades de seguridad. Revise los derechos de acceso y los permisos de las cuentas de usuario para asegurarse de que cumplan los requisitos actuales y las mejores prácticas.
* **Capacitación y concienciación:** Capacite con regularidad a empleados y administradores sobre las mejores prácticas de seguridad y la concienciación frente a ataques de phishing y otras amenazas cibernéticas. Hágales ver la importancia de la seguridad y anímelos a informar de cualquier actividad sospechosa.

Al implementar estas mejores prácticas, las organizaciones pueden mejorar la seguridad de su protocolo de gestión de usuarios y minimizar el riesgo de brechas de seguridad y pérdida de datos. Es importante ver la seguridad como un proceso continuo y realizar actualizaciones y ajustes periódicos para mantenerse al día con las amenazas y los requisitos de seguridad en constante cambio.
