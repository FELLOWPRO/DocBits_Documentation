# Almacenamiento, conservación y eliminación de datos

Sus datos están en buenas manos con DocBits. Operamos DocBits en dos regiones, **Frankfurt am Main (UE)** y **San Francisco (EE. UU.)**, y usted decide en su configuración durante cuánto tiempo permanecen los documentos con nosotros. Esta página trata sobre las ubicaciones de almacenamiento, los plazos de conservación y la eliminación.

**Documentación actualizada a: 28 de octubre de 2026.**

## De un vistazo

- **Usted elige la región:** Frankfurt para clientes de la UE, San Francisco para clientes de EE. UU.
- **Sus datos permanecen en su región.** Los datos de la UE se alojan en Frankfurt y los de EE. UU. en San Francisco. No se mezclan datos entre regiones.
- **Usted controla durante cuánto tiempo se conservan sus documentos** en **Procesamiento de documentos → Caducidad de documentos** ([ir a la configuración](../administration-and-setup/settings/document-processing/documents-expiry.md)).
- **Los archivos OCR temporales** se eliminan automáticamente después de 90 minutos.
- **Con gusto le ayudamos:** nuestro equipo responde a sus preguntas y solicitudes de eliminación en **compliance@fellowpro.com**.

## ¿Dónde se almacenan sus datos?

| Región | Para quién | Ubicación | Servicios utilizados |
| --- | --- | --- | --- |
| **UE** | Todos los clientes de la UE | **Frankfurt am Main, Alemania** | DigitalOcean Kubernetes (región `fra1`) con bases de datos gestionadas PostgreSQL, OpenSearch y Valkey (`fra1`), además de DigitalOcean Spaces para el almacenamiento de archivos |
| **EE. UU.** | Clientes de EE. UU. | **San Francisco, EE. UU.** | DigitalOcean Kubernetes (región `sfo2`) con bases de datos gestionadas PostgreSQL, OpenSearch y Valkey (`sfo2`) |

**Copias de seguridad en la UE:** Frankfurt es la ubicación principal de las copias de seguridad y Ámsterdam (Países Bajos) la secundaria, de modo que sus copias de seguridad también permanecen dentro de la UE.

**Sistemas conectados:** si exporta documentos a su ERP, a Infor IDM o a otro sistema de destino, esas copias se almacenan allí, según las normas y en la ubicación de ese sistema. Eso queda en sus manos.

## ¿Durante cuánto tiempo se conservan los datos?

| Tipo de datos | Conservación |
| --- | --- |
| **Documentos cargados y datos extraídos** | Usted lo controla mediante [Caducidad de documentos](../administration-and-setup/settings/document-processing/documents-expiry.md) (véase más abajo). |
| **Archivos OCR temporales** | Limpieza automática después de **90 minutos**. Esto se aplica únicamente al almacenamiento OCR temporal, no a su documento en DocBits. |
| **Registros accesibles para el cliente** (consultables en [Registro de actividad](../administration-and-setup/settings/log-settings/README.md)) | **30 días** |
| **Registros internos** | **3 meses** |
| **Copias de seguridad diarias de la base de datos (gestionadas)** | **7 días**; las copias más antiguas se eliminan automáticamente. |
| **Copias de seguridad diarias adicionales (SnapShooter)** | Para las bases de datos de producción y sandbox; la conservación se define por entorno. |
| **Cookies y almacenamiento del navegador** | Varía según la finalidad, véase [Cookies y almacenamiento del navegador](cookies-and-browser-storage.md). |

Además, realizamos copias de seguridad diarias, semanales, trimestrales y anuales. Con gusto le facilitamos, previa solicitud, los plazos de conservación exactos de estos tipos de copia de seguridad para su entorno.

## Cómo configurar la conservación de sus documentos

En Configuración, abra **Procesamiento de documentos → Caducidad de documentos**. Hay dos ajustes:

- **Delete document after:** durante cuánto tiempo se conservan los documentos.
- **Delete finished document after:** durante cuánto tiempo se conservan los documentos finalizados, es decir, completamente procesados y exportados.

Las opciones son **Default**, **48 Hours**, **1 Week**, **2 Weeks** y **4 Weeks**. **Default** aplica el valor predeterminado del sistema. Si desea un plazo fijo, simplemente elija una de las duraciones. Encontrará todos los detalles en la [guía de Caducidad de documentos](../administration-and-setup/settings/document-processing/documents-expiry.md).

## ¿Qué ocurre cuando se eliminan los datos?

Caducidad de documentos elimina automáticamente sus documentos una vez transcurrido el plazo que haya elegido. Esto es independiente de la limpieza de los archivos OCR temporales, de la caducidad de los registros y de la conservación de las copias de seguridad.

Conviene saber:

- **Las copias de seguridad caducan según su propio calendario.** Por ello, eliminar un documento en el sistema activo no borra de inmediato las copias de seguridad, sino cuando finaliza el período de la copia correspondiente.
- **Las copias exportadas son suyas.** Cuando DocBits elimina un documento, la copia en su ERP o archivo permanece. Planifique allí la conservación según sus propios requisitos.

## ¿Preguntas o solicitudes de eliminación? Estamos a su disposición

Para obtener información sobre su implementación o para una solicitud de eliminación, escríbanos a **compliance@fellowpro.com**. Indíquenos su organización, el entorno afectado, el tipo de datos y el alcance que necesita. Por favor, no envíe contraseñas ni claves de API.

También le confirmamos con gusto:

- Su región activa y la configuración de conservación vigente, incluido el valor predeterminado del sistema.
- Cuándo comienza el plazo de eliminación y con qué frecuencia se ejecuta la limpieza.
- El alcance de la eliminación de documentos, datos extraídos, índices de búsqueda y datos derivados.
- Las ubicaciones y los plazos de conservación de todos los tipos de copia de seguridad, también tras la finalización del contrato.

## Más información de seguridad

- [DocBits (FELLOWPRO AG) — Cuestionario de Seguridad y Cumplimiento](security-and-compliance-faq.md)
- [Cifrado en reposo](encryption-at-rest.md)
- [Almacenamiento seguro de credenciales](secure-storage-of-credentials.md)
- [Cookies y almacenamiento del navegador](cookies-and-browser-storage.md)
