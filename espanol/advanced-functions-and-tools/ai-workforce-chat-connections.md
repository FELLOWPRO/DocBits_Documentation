# Conectar AI Workforce con Teams y Discord

Necesita una suscripción activa a AI Workforce, permisos para administrar conexiones y acceso al tenant de Teams o servidor de Discord previsto. Resuelva primero con el administrador cualquier requisito de suscripción mostrado.

## Microsoft Teams

1. Abra **AI Workforce → Configuración → Integraciones**.
2. Elija **+ → Conectar Teams**. DocBits genera un código con su tiempo de validez restante.
3. Siga la instrucción mostrada con el código en el entorno de Teams previsto. Manténgalo privado y complete la asociación antes de que caduque.
4. Espere la confirmación y compruebe nombre y modalidad de bot compartido o personalizado en la lista.
5. Active la conexión si está inactiva y debe recibir trabajo. Guardada y activa son estados diferentes.
6. Envíe una solicitud de prueba inocua desde el contexto correcto de Teams. Compruebe misión, origen y organización en DocBits, y complete las aprobaciones humanas necesarias en la bandeja de entrada.

Para un bot gestionado por la empresa, utilice la opción de bot personalizado e introduzca nombre, ID de tenant, ID de aplicación y secreto de aplicación. Guarde los secretos en el formulario de credenciales, fuera de instrucciones y capturas.

## Discord

1. En **Integraciones → +**, elija conectar Discord.
2. Si se ofrece, añada el bot al servidor correcto con un administrador autorizado.
3. Introduzca un nombre reconocible y el **Guild ID** correcto. Es el identificador del servidor, no del canal.
4. Cree la conexión, revise el registro y actívelo si corresponde.
5. Envíe una prueba inocua y verifique la misión, origen y organización resultantes.

## Resolver problemas

Si caduca un código de Teams, genere otro y siga su instrucción actual. Si no llega trabajo, compruebe activación, identidad de tenant/servidor, acceso del bot y errores. Una conexión establecida no demuestra una misión terminada.

Consulte [AI Workforce](ai_workforce/README.md) para misiones, permisos y aprobaciones. Estas conexiones son independientes de la importación por correo y el inicio de sesión de Microsoft.
