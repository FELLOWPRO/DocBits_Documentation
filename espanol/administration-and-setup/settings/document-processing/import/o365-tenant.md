# O365 Tenant

## Registrar App en Azure AD

<mark style="color:red;">**Nota**</mark>: Los permisos pueden requerir autorización de un administrador.

1. Inicie sesión en el [Portal de Azure](https://portal.azure.com/) usando sus credenciales.
2. Desde los servicios de Azure, localice y abra Azure Active Directory (también conocido como Azure AD).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_1.png)

3. En la sección **Manage**, seleccione **App registrations**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_2.png)

4. En la pantalla App registrations, haga clic en **+ New registration**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_3.png)

5. Se muestra la pantalla **Register an application**. Ingrese el nombre de visualización orientado al usuario para la App en **Name**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_4.png)

6. Seleccione uno de los siguientes tipos de cuenta según sus necesidades:

* **Accounts in any organizational directory (Any Azure AD directory Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)**
* **Accounts in any organizational directory (Any Azure AD directory Multitenant)**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_5.png)

7. Deje la opción **Redirect URI (optional)** como está.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_6.png)

8. Haga clic en **Register** para completar el registro de la App. Esto le devolverá a la pantalla de la nueva App.
9. En la pantalla de la App, localice el **Application (client) ID**. Cópielo para usarlo al configurar la importación de correo electrónico para **DocBits**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_7.png)

10. Desde el panel izquierdo, seleccione **Certificates & secrets**:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_8.png)

11. En la pantalla **Certificates & secrets**, haga clic en el botón **+ New client secret** en la sección **Client secrets**:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_9.png)

12. En el cuadro de diálogo **Add a client secret**, haga clic en el botón **Add**:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_10.png)

Se recomienda completar una descripción para identificar este secreto entre muchos (por ahora el límite es de 2 secretos por App).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_11.png)

<mark style="color:red;">**Nota**</mark>: Seleccione esta fecha de vencimiento de acuerdo con la política de su empresa. Una vez vencido, se deberá crear un nuevo client secret y especificarlo para cada configuración de correo electrónico donde se usó anteriormente.

13. El client secret recién generado será visible. Copie este client secret para usarlo al configurar la importación de correo electrónico para DocBits.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_12.png)

**Importante:** Asegúrese de haber copiado el client secret, ya que el client secret no se mostrará nuevamente una vez que se cierre.

14. Seleccione **Authentication** en el panel izquierdo. Esto presentará la pantalla **Authentication** en el lado derecho.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_13.png)

15. En la sección **Advanced settings**, haga clic en **Yes** para **Default client type**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_14.png)

16. Haga clic en **Save** para confirmar los cambios.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_15.png)

17. Seleccione **API permissions** en el panel izquierdo. Esto presentará la pantalla de permisos de API.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_16.png)

18. Por defecto, el permiso **User.Read** de **Microsoft Graph** está presente, déjelo como está.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_17.png)

<mark style="color:red;">**Nota**</mark>: Este es un permiso obligatorio. Si este permiso no está disponible, agregue el permiso con los pasos mencionados a continuación para el permiso **Mail.ReadWrite**.

19. Haga clic en **+ Add a permission**. Esto abrirá el panel **Request API permissions**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_18.png)

20. Haga clic en **Microsoft Graph**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_19.png)

21. De las dos subcategorías, seleccione **App Permissions**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_20.png)

22. Escriba **Mail.ReadWrite** en el cuadro de búsqueda. Seleccione la casilla de verificación **Mail.ReadWrite** para el permiso.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_21.png)

23. Esto habilitará el botón **Add permissions** en la parte inferior del panel. Haga clic en **Add permissions**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_22.png)

24. Esto agregará el permiso **Mail.ReadWrite** a la lista de **Configured permissions** para la App.

<mark style="color:red;">**Nota**</mark>: Es posible que se requieran permisos de administrador. El administrador tendrá que autorizar la App para usar estos permisos. Una vez autorizado, el estado otorgado se indicará de la siguiente manera:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_23.png)
