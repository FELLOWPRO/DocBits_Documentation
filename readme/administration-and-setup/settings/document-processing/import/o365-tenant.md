# O365 Tenant

## Registrar App en Azure AD

<mark style="color:red;">**Nota**</mark>: Los permisos pueden requerir autorización de un administrador.

1. Inicie sesión en el [Portal de Azure](https://portal.azure.com/) usando sus credenciales.
2. Desde los servicios de Azure, localice y abra Azure Active Directory (también conocido como Azure AD).

![Página del portal de Azure con la entrada Azure Active Directory y la barra de búsqueda de servicios](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_1.png)

3. En la sección **Manage**, seleccione **App registrations**.

![Página de información general de Azure Active Directory con el menú Manage de la izquierda abierto y App registrations resaltado](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_2.png)

4. En la pantalla App registrations, haga clic en **+ New registration**.

![Pantalla App registrations en Azure con el botón New registration en la barra de herramientas y la lista de aplicaciones registradas](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_3.png)

5. Se muestra la pantalla **Register an application**. Ingrese el nombre de visualización orientado al usuario para la App en **Name**.

![Pantalla Register an application en Azure Portal con el campo Name vacío para la nueva aplicación](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_4.png)

6. Seleccione uno de los siguientes tipos de cuenta según sus necesidades:

* **Cuentas en cualquier directorio organizacional (Cualquier directorio de Azure AD Multiinquilino) y cuentas personales de Microsoft (por ejemplo, Skype, Xbox)**
* **Cuentas en cualquier directorio organizacional (Cualquier directorio Azure AD Multiinquilino)**

![Pantalla Register an application con las opciones de botón de radio del tipo de cuenta admitido para directorios organizativos y cuentas personales de Microsoft](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_5.png)

7. Deje la opción **Redirect URI (optional)** como está.

![Pantalla Register an application con la sección Redirect URI (optional) sin cambios en la parte inferior](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_6.png)

8. Haga clic en **Register** para completar el registro de la App. Esto le devolverá a la pantalla de la nueva App.
9. En la pantalla de la App, localice el **Application (client) ID**. Cópielo para usarlo al configurar la importación de correo electrónico para **DocBits**.

![Página de descripción general de la aplicación registrada que muestra el Display name Ephesoft OAuth2 App y el Application client ID](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_7.png)

10. Desde el panel izquierdo, seleccione **Certificates & secrets**:

![Página de información general de la aplicación registrada con Certificates and secrets seleccionado en la sección Manage del panel izquierdo](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_8.png)

11. En la pantalla **Certificates & secrets**, haga clic en el botón **+ New client secret** en la sección **Client secrets**:

![Pantalla de Certificates & secrets con la sección Client secrets y el botón + New client secret](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_9.png)

12. En el cuadro de diálogo **Add a client secret**, haga clic en el botón **Add**:

![Diálogo Add a client secret con los campos Description y Expires y el botón Add](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_10.png)

Se recomienda completar una descripción para identificar este secreto entre muchos (por ahora el límite es de 2 secretos por App).

![Lista de client secrets que muestra el nuevo secreto con sus columnas de descripción, Value y Expires](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_11.png)

<mark style="color:red;">**Nota**</mark>: Seleccione esta fecha de vencimiento de acuerdo con la política de su empresa. Una vez vencido, se deberá crear un nuevo client secret y especificarlo para cada configuración de correo electrónico donde se usó anteriormente.

13. El client secret recién generado será visible. Copie este client secret para usarlo al configurar la importación de correo electrónico para DocBits.

![Sección Client secrets de Certificates & secrets con el valor del secreto generado listo para copiar](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_12.png)

**Importante:** Asegúrese de haber copiado el client secret, ya que el client secret no se mostrará nuevamente una vez que se cierre.

14. Seleccione **Authentication** en el panel izquierdo. Esto presentará la pantalla **Authentication** en el lado derecho.

![Pantalla de autenticación del registro de aplicaciones abierta desde el panel izquierdo con la configuración de plataformas a la derecha](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_13.png)

15. En la sección **Advanced settings**, haga clic en **Yes** para **Default client type**.

![Sección Advanced settings de la pantalla de Authentication con la opción Default client type establecida en Yes](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_14.png)

16. Haga clic en **Save** para confirmar los cambios.

![Barra superior del registro de la aplicación con el botón Save resaltado tras habilitar el tipo de cliente predeterminado](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_15.png)

17. Seleccione **API permissions** en el panel izquierdo. Esto presentará la pantalla de permisos de API.

![Pantalla API permissions abierta desde el panel izquierdo que muestra los permisos configurados para la aplicación](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_16.png)

18. Por defecto, el permiso **User.Read** de **Microsoft Graph** está presente, déjelo como está.

![Lista de permisos configurados que muestra el permiso delegado predeterminado User.Read para Microsoft Graph](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_17.png)

<mark style="color:red;">**Nota**</mark>: Este es un permiso obligatorio. Si este permiso no está disponible, agregue el permiso con los pasos mencionados a continuación para el permiso **Mail.ReadWrite**.

19. Haga clic en **+ Add a permission**. Esto abrirá el panel **Request API permissions**.

![Panel Request API permissions con Microsoft APIs, APIs my organization uses y el flujo de + Add a permission](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_18.png)

20. Haga clic en **Microsoft Graph**.

![Panel Request API permissions con Microsoft Graph resaltado entre las API de Microsoft más utilizadas](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_19.png)

21. De las dos subcategorías, seleccione **App Permissions**.

![Panel Request API permissions para Microsoft Graph con las opciones Delegated permissions y Application permissions](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_20.png)

22. Escriba **Mail.ReadWrite** en el cuadro de búsqueda. Seleccione la casilla de verificación **Mail.ReadWrite** para el permiso.

![Cuadro de búsqueda de permisos de aplicación con Mail.ReadWrite escrito y la casilla del permiso Mail.ReadWrite seleccionada](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_21.png)

23. Esto habilitará el botón **Add permissions** en la parte inferior del panel. Haga clic en **Add permissions**.

![Panel Request API permissions con el permiso Mail.ReadWrite seleccionado y el botón Add permissions en la parte inferior](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_22.png)

24. Esto agregará el permiso **Mail.ReadWrite** a la lista de **Configured permissions** para la App.

<mark style="color:red;">**Nota**</mark>: Es posible que se requieran permisos de administrador. El administrador tendrá que autorizar la App para usar estos permisos. Una vez autorizado, el estado otorgado se indicará de la siguiente manera:

![Lista de permisos configurados con el permiso de aplicación Mail.ReadWrite añadido y su estado concedido mostrado](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_23.png)
