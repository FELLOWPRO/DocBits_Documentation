---
description: Usar DocBits con tu inicio de sesión de Microsoft sin utilizar una contraseña (independiente)
---

# SSO de Azure

### Crear SAML SSO en Azure AD

Realiza los siguientes pasos para añadir SAML SSO en Azure AD:

*   En Azure, ve a tu consola de \`Azure Active Directory\`

    ![Panel de navegación del portal de Azure con favoritos como Resource groups, All resources y Azure Active Directory](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* En el panel izquierdo, haz clic en \`Enterprise applications\`

![Panel izquierdo de Azure Active Directory con las entradas de Manage: Users, Groups, Roles and administrators y Enterprise applications](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Haz clic en \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (213).png" alt="Pantalla de validación con la lista de campos extraídos a la izquierda, la vista previa del documento del proveedor a la derecha y botones de aprobación abajo"><figcaption></figcaption></figure>

* Haz clic en \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (215).png" alt="Página Configuraciones General con las casillas de verificación Quien puede subir documentos, Quien puede subir datos y Quien puede validar y exportar"><figcaption></figcaption></figure></div>

* Introduce un nombre para tu aplicación. Mantén el resto de las selecciones predeterminadas.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt="Diálogo Create your own application en Azure con el nombre de la aplicación MyApplication y las opciones de integración de aplicaciones"><figcaption></figcaption></figure>

* Haz clic en \`Create\`

### Asignar usuarios a la configuración de SSO

A continuación, asigna usuarios o grupos a la configuración de SSO.

**Importante**: Ya deberías haber creado usuarios y grupos en Azure AD. Si no tienes ningún usuario o grupo, créalos ahora antes de continuar.

* En \`Getting Started\`, haz clic en \`Assign Users and Groups\`.
* Haz clic en \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="Página Users and groups de MyApplication en Azure con los botones Add user, Edit y Remove y una lista vacía de Display Name" width="563"><figcaption></figcaption></figure>

* Selecciona los usuarios y grupos que deseas asignar a esta configuración de SSO. Estos usuarios podrán autenticarse en DocBits (mediante SSO).

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt="Panel de selección de usuarios y grupos en Azure con una lista de usuarios Daniel y un panel Selected items"><figcaption></figcaption></figure>

* Haz clic en \`Select\`
* Cuando estés satisfecho con tu selección, haz clic en \`Assign\`

![Diálogo Add Assignment en Azure con 2 users selected, 2 groups selected y Select Role establecido en User](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (216) (1).png" alt="Página de ajustes de Integration and SSO con la tabla Claves API y las columnas Nombre, Caduca, Ultimo Uso, Estado y Actions"><figcaption></figcaption></figure></div>

* Ve a la lista de la vista \`Groups\` y busca los grupos asignados.

### Configurar SSO en Azure

A continuación, debes finalizar la configuración del inicio de sesión único en Azure.\\

* En el panel izquierdo, haz clic en \`Single sign-on\`

![Menú de descripción general de Enterprise Application en Azure con las entradas de Manage: Properties, Owners, Users and groups, Single sign-on y Provisioning](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Haz clic en \`SAML\`

![Tarjeta de opción SAML en Azure que describe una autenticación completa y segura con el protocolo Security Assertion Markup Language](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Haz clic en \`Upload metadata file\`

![Panel SAML-based Sign-on en Azure con Upload metadata file y Set up Single Sign-On](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Carga el **metadata.xml** de DocBits, que puedes encontrar en el menú Configuración **Integración**, en **SSO Service Provider Settings** de tu cuenta de DocBits.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt="Página SSO Service Provider Settings con el Tenant ID, el Entity ID y los campos SSO Url, SLO Url y Metadata Url"><figcaption></figcaption></figure>

* Edita la \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt="Pantalla de configuración del inicio de sesión único con SAML que muestra Basic SAML Configuration con Identifier, Reply URL, Sign on URL y Logout Url"><figcaption></figcaption></figure>

* Comprueba si los campos \`Entity ID\`, \`ACS URL\`, \`Sign on URL\` y \`Logout URL\` están rellenados correctamente.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt="Editor de Basic SAML Configuration en Azure con los campos Identifier, Reply URL, Sign on URL, Relay State y Logout Url, además de Save"><figcaption></figcaption></figure>

* Descarga el **Federation Metadata XML** recién generado.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt="Sección SAML Signing Certificate en Azure con huella digital, fecha de expiración y enlaces de descarga para Certificate (Raw) y Federation Metadata XML"><figcaption></figcaption></figure>

* Carga el FederationMetadata.xml en **Identity Service Provider Settings** de tu cuenta de DocBits, que puedes encontrar en el menú Configuración **Integración**.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt="Diálogo Identity Service Provider Settings en DocBits con el Tenant ID FELLOWPRO_PRD y el botón Upload file"><figcaption></figcaption></figure>
