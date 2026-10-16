---
description: Cifrado en reposo de DocBits en DigitalOcean, incluidas bases de datos, Spaces y cobertura de copias de seguridad.
---

# Cifrado en reposo

DocBits utiliza DigitalOcean Managed Databases y DigitalOcean Spaces. La revisión del **16 de octubre de 2026** confirmó servicios gestionados de PostgreSQL, OpenSearch y Valkey para producción de la UE en Fráncfort. Las [preguntas frecuentes de seguridad y cumplimiento](security-and-compliance-faq.md) documentan el uso de Spaces para almacenamiento.

Esta página describe los controles de cifrado publicados por DigitalOcean para estos servicios. Las instalaciones locales y las copias almacenadas en otros sistemas requieren su propia evaluación.

## Métodos de cifrado y alcance

| Servicio de almacenamiento | Cifrado en reposo | Cobertura |
| --- | --- | --- |
| Managed Databases: PostgreSQL, OpenSearch, Valkey | Cifrado de volúmenes completos con LUKS; `aes-xts-plain64:sha256` con 512 bits de material de clave XTS | Los volúmenes subyacentes del servicio de base de datos y los datos almacenados en ellos. Es protección del almacenamiento, no una afirmación de cifrado independiente de cada campo de la base de datos. |
| Copias de seguridad de Managed Databases | AES-256 en modo CTR, con HMAC-SHA256 para la integridad; claves por archivo protegidas mediante RSA-3072 | Copias creadas por el servicio de base de datos gestionada. Las exportaciones y copias adicionales requieren verificación por separado. |
| DigitalOcean Spaces | Cifrado de disco completo con AES-XTS de 256 bits | Datos en los discos físicos de almacenamiento. Es distinto del cifrado opcional por objeto o del lado del cliente. |
| DigitalOcean Volumes, cuando se utilizan | Cifrado LUKS del clúster de almacenamiento | Datos de estos volúmenes de almacenamiento en bloques; las instantáneas de volumen heredan el cifrado. |

XTS utiliza dos claves AES. Los 512 bits de material combinado de clave XTS del servicio de base de datos gestionada corresponden a dos claves AES de 256 bits (AES-256-XTS), no a un cifrado AES con una clave de 512 bits.

Los detalles sobre bases de datos y copias proceden del [modelo de seguridad de Managed Databases](https://www.digitalocean.com/security/shared-responsibility-model-managed-databases). El [modelo de seguridad de Spaces](https://www.digitalocean.com/security/shared-responsibility-model-spaces) confirma el cifrado en reposo; el [modelo de seguridad de App Platform](https://www.digitalocean.com/security/shared-responsibility-model-app-platform) especifica AES-XTS de 256 bits para los discos físicos de Spaces. Las [funciones de Volumes](https://docs.digitalocean.com/products/volumes/details/features/) documentan la cobertura de volúmenes e instantáneas.

## Gestión de claves y acceso autorizado

DigitalOcean gestiona el cifrado de infraestructura descrito. Para Managed Databases, documenta una clave aleatoria por instancia y volumen, descartada al destruir la instancia. Las copias de seguridad de bases de datos gestionadas utilizan una clave aleatoria por archivo, protegida mediante un par de claves RSA específico del servicio.

El cifrado del almacenamiento protege los datos en los soportes. Las aplicaciones y los usuarios autorizados de la base de datos pueden seguir leyendo los datos a través del servicio. Esto no demuestra que el personal del proveedor no pueda acceder a información de cuentas, ni que cada campo esté cifrado en la aplicación. Los hashes de contraseñas y claves API son controles separados; consulte [Almacenamiento seguro de credenciales](secure-storage-of-credentials.md).

Spaces también admite [SSE-C con claves proporcionadas por el cliente](https://docs.digitalocean.com/products/spaces/reference/s3-compatibility/). Esta capacidad opcional no demuestra que DocBits utilice SSE-C o claves de cifrado gestionadas por el cliente.

## Cifrado de las copias de seguridad

Las copias de seguridad creadas por DigitalOcean Managed Databases se cifran con AES-256-CTR y se protegen frente a cambios no detectados mediante HMAC-SHA256. Las claves de cifrado de cada archivo están protegidas con RSA-3072. Las instantáneas de volúmenes heredan el cifrado del volumen de DigitalOcean subyacente. Estos detalles describen las funciones de copia de seguridad de los servicios gestionados indicados.

## Tipos de cifrado en reposo

A continuación se resumen los principales métodos de cifrado de los servicios indicados:

> DocBits utiliza DigitalOcean Managed Databases y Spaces. Los datos de las bases de datos gestionadas se cifran en reposo a nivel de volumen completo mediante LUKS con AES-256-XTS (512 bits de material combinado de clave XTS). Sus copias de seguridad utilizan AES-256-CTR con protección de integridad HMAC-SHA256 y RSA-3072 para proteger las claves de cifrado de cada archivo. Spaces utiliza cifrado de disco completo con AES-XTS de 256 bits en su almacenamiento físico.
>
> Estos controles de almacenamiento cubren los datos en los volúmenes y discos protegidos; no implican cifrado independiente de cada campo de la base de datos. DigitalOcean gestiona las claves de cifrado de infraestructura. Esta declaración abarca los servicios gestionados indicados.
