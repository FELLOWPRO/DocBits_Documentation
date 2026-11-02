# Solución de problemas

## No encuentro Testing en Configuración

La página solo se muestra a los administradores de la organización. Consulte con un administrador de su organización.

## La página indica que Testing está desactivado

Un administrador de la organización debe activar **Habilitar Testing para la organización** en la parte superior de la página.
Hasta entonces no se ejecuta nada, tampoco desde un asistente de IA ni desde fuera.

## Mi ejecución ha fallado

Abra el registro en la pestaña **Registros** y consulte el primer paso fallido y su código de error:

| Lo que ve | Suele significar | Qué hacer |
|---|---|---|
| No se encontró un elemento o no es visible | La página es distinta en su organización o carga con lentitud | Abra usted mismo la página y compruébela; ajuste su plantilla propia o revise los valores de la entrada |
| Un campo o un estado no coincide | El documento tiene un valor distinto del que espera la entrada | Compruebe el documento; corrija el valor esperado en la entrada |
| No se pudo abrir la página | ID de documento incorrecto o falta de permisos | Compruebe el ID en la entrada y los permisos del usuario que inició la pestaña |
| Tiempo de espera agotado | El paso o la prueba completa tardó demasiado | Ejecute de nuevo; si se repite, revise el rendimiento de la página |
| Bloqueado por el entorno | La prueba escribe datos en un entorno de cliente | Confirme el inicio o ejecútela en un entorno de pruebas |

## Mi ejecución está «Bloqueado»

La ejecución no pudo evaluarse: se omitieron algunos pasos (por ejemplo, un paso de captura de pantalla, que el navegador no puede realizar)
o falta una confirmación. Una ejecución bloqueada nunca se cuenta como aprobada. Elimine el paso de su plantilla propia o
inícielo de nuevo con la confirmación.

## «Registre una sesión de navegador para iniciar» / ninguna pestaña acepta inicios

Los inicios desde un asistente de IA o desde fuera requieren una pestaña del navegador con **Permitir inicios desde fuera** activado. Abra
la pestaña Entradas en una pestaña que permanezca abierta, active la opción y utilice su ID de sesión. Una recarga finaliza el registro de la pestaña.

## La ejecución se detuvo o muestra Cancelado / No entregable

La pestaña que ejecutaba la prueba se recargó, se cerró o perdió la conexión, o ninguna pestaña respondió a tiempo. Mantenga la pestaña abierta
y en primer plano hasta que termine la ejecución y vuelva a iniciar. Una prueba con un paso **Recargar página** también termina así si la página no vuelve en unos dos minutos
(consulte [Recargar y reanudar](reload-and-resume.md)).

## «Las plantillas de Playwright aún no se pueden iniciar aquí»

Las plantillas cuyo **Ejecutor** es **Playwright** las ejecuta su automatización de pruebas. Puede guardar entradas para ellas, pero no
puede iniciarlas desde esta página.

## No puedo eliminar una plantilla

Solo se pueden eliminar las plantillas propias de su organización (**personalizado**). Las plantillas integradas y predeterminadas no; utilice
**Editar una copia** para obtener su propia versión.
