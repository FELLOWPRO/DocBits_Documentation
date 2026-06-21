---
description: Usar DocBits con tu inicio de sesión de Microsoft sin utilizar una contraseña (independiente)
---

# Azure SSO

### Crear SAML SSO en Azure AD

Realiza los siguientes pasos para añadir SAML SSO en Azure AD:

*   En Azure, ve a tu consola de \`Azure Active Directory\`

    ![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* En el panel izquierdo, haz clic en \`Enterprise applications\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Haz clic en \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (213).png" alt=""><figcaption></figcaption></figure>

* Haz clic en \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (215).png" alt=""><figcaption></figcaption></figure></div>

* Introduce un nombre para tu aplicación. Mantén el resto de las selecciones predeterminadas.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt=""><figcaption></figcaption></figure>

* Haz clic en \`Create\`

### Asignar usuarios a la configuración de SSO

A continuación, asigna usuarios o grupos a la configuración de SSO.

**Importante**: Ya deberías haber creado usuarios y grupos en Azure AD. Si no tienes ningún usuario o grupo, créalos ahora antes de continuar.

* En \`Getting Started\`, haz clic en \`Assign Users and Groups\`.
* Haz clic en \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="" width="563"><figcaption></figcaption></figure>

* Selecciona los usuarios y grupos que deseas asignar a esta configuración de SSO. Estos usuarios podrán autenticarse en DocBits (mediante SSO).

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt=""><figcaption></figcaption></figure>

* Haz clic en \`Select\`
* Cuando estés satisfecho con tu selección, haz clic en \`Assign\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (216) (1).png" alt=""><figcaption></figcaption></figure></div>

* Ve a la lista de la vista \`Groups\` y busca los grupos asignados.

### Configurar SSO en Azure

A continuación, debes finalizar la configuración del inicio de sesión único en Azure.\\

* En el panel izquierdo, haz clic en \`Single sign-on\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Haz clic en \`SAML\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Haz clic en \`Upload metadata file\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Carga el **metadata.xml** de DocBits, que puedes encontrar en el menú Configuración **Integración**, en **SSO Service Provider Settings** de tu cuenta de DocBits.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt=""><figcaption></figcaption></figure>

* Edita la \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt=""><figcaption></figcaption></figure>

* Comprueba si los campos \`Entity ID\`, \`ACS URL\`, \`Sign on URL\` y \`Logout URL\` están rellenados correctamente.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt=""><figcaption></figcaption></figure>

* Descarga el **Federation Metadata XML** recién generado.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt=""><figcaption></figcaption></figure>

* Carga el FederationMetadata.xml en **Identity Service Provider Settings** de tu cuenta de DocBits, que puedes encontrar en el menú Configuración **Integración**.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt=""><figcaption></figcaption></figure>
