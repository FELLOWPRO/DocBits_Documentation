---
description: Usar DocBits con tu inicio de sesión de Microsoft sin utilizar una contraseña (independiente)
---

# SSO de Azure

### Crear SAML SSO en Azure AD

Realiza los siguientes pasos para añadir SAML SSO en Azure AD:

*   En Azure, ve a tu consola de \`Azure Active Directory\`

    ![Página de inicio del portal de Azure con Azure Active Directory en los favoritos de la navegación izquierda](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* En el panel izquierdo, haz clic en \`Enterprise applications\`

![Navegación izquierda de Azure Active Directory con el grupo Administrar y la entrada Aplicaciones empresariales](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Haz clic en \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (213).png" alt="Página Aplicaciones empresariales de Azure Active Directory con la lista Todas las aplicaciones y el botón Nueva aplicación"><figcaption></figcaption></figure>

* Haz clic en \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (215).png" alt="Diálogo Explorar la galería de Azure AD con los botones Crear su propia aplicación y Solicitar nueva aplicación de la galería y el campo de búsqueda Buscar aplicación"><figcaption></figcaption></figure></div>

* Introduce un nombre para tu aplicación. Mantén el resto de las selecciones predeterminadas.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt="Diálogo Crear su propia aplicación con el nombre MyApplication y la opción seleccionada Integrar cualquier otra aplicación que no encuentre en la galería"><figcaption></figcaption></figure>

* Haz clic en \`Create\`

### Asignar usuarios a la configuración de SSO

A continuación, asigna usuarios o grupos a la configuración de SSO.

**Importante**: Ya deberías haber creado usuarios y grupos en Azure AD. Si no tienes ningún usuario o grupo, créalos ahora antes de continuar.

* En \`Getting Started\`, haz clic en \`Assign Users and Groups\`.
* Haz clic en \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="Página Usuarios y grupos de la aplicación MyApplication con los botones Agregar usuario, Editar, Quitar y Actualizar y el mensaje No se encontraron asignaciones de aplicaciones" width="563"><figcaption></figcaption></figure>

* Selecciona los usuarios y grupos que deseas asignar a esta configuración de SSO. Estos usuarios podrán autenticarse en DocBits (mediante SSO).

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt="Panel de selección de usuarios con varios usuarios listados y la sección Seleccionados"><figcaption></figcaption></figure>

* Haz clic en \`Select\`
* Cuando estés satisfecho con tu selección, haz clic en \`Assign\`

![Diálogo Agregar asignación del inquilino chimdustries con el mensaje 2 usuarios seleccionados y 2 grupos seleccionados](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (216) (1).png" alt="Botón Asignar resaltado con un borde verde en el diálogo de asignación de Azure Active Directory"><figcaption></figcaption></figure></div>

* Ve a la lista de la vista \`Groups\` y busca los grupos asignados.

### Configurar SSO en Azure

A continuación, debes finalizar la configuración del inicio de sesión único en Azure.\\

* En el panel izquierdo, haz clic en \`Single sign-on\`

![Navegación izquierda de la aplicación empresarial MyApplication con la entrada Inicio de sesión único](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Haz clic en \`SAML\`

![Página Inicio de sesión único con el icono SAML y el texto Autenticación segura y fiable para aplicaciones mediante el protocolo SAML](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Haz clic en \`Upload metadata file\`

![Página Inicio de sesión basado en SAML con los enlaces Cargar archivo de metadatos y Configurar el inicio de sesión único](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Carga el **metadata.xml** de DocBits, que puedes encontrar en el menú Configuración **Integración**, en **SSO Service Provider Settings** de tu cuenta de DocBits.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt="Configuración del proveedor de servicios SSO en DocBits con el Entity ID, la SLO URI y la SSO URI y los botones Descargar certificado y Descargar metadatos"><figcaption></figcaption></figure>

* Edita la \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt="Página Configurar el inicio de sesión único con SAML con la sección Configuración básica de SAML y los campos Identificador Entity ID, URL de respuesta, URL de inicio de sesión, Estado de retransmisión y URL de cierre de sesión"><figcaption></figcaption></figure>

* Comprueba si los campos \`Entity ID\`, \`ACS URL\`, \`Sign on URL\` y \`Logout URL\` están rellenados correctamente.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt="Configuración básica de SAML en Azure con los textos descriptivos, el Identificador Entity ID con la URL de metadatos SAML del inquilino y la URL de respuesta como Assertion Consumer Service URL"><figcaption></figcaption></figure>

* Descarga el **Federation Metadata XML** recién generado.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt="Sección Certificado de firma SAML con el estado Activo, la huella digital, la fecha de expiración, el correo de notificación y los enlaces de descarga Certificado sin formato y XML de metadatos de federación"><figcaption></figcaption></figure>

* Carga el FederationMetadata.xml en **Identity Service Provider Settings** de tu cuenta de DocBits, que puedes encontrar en el menú Configuración **Integración**.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt="Configuración del proveedor de servicios de identidad en DocBits con el Tenant ID, los botones Cargar archivo e Importar y la entrada del archivo existente"><figcaption></figcaption></figure>
