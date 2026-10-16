---
hidden: true
---

# Configuración de Plantillas EDI

## Aquí hay instrucciones paso a paso para configurar plantillas EDI:

<figure><img src="../../../../../../.gitbook/assets/docbits_sso_cert_metadata.png" alt="Docbits Sso Cert Metadata"><figcaption></figcaption></figure>

**Definir el descriptor de estructura:**

* Identifique el tipo de mensaje EDI con el que está trabajando, por ejemplo, ANSI X12, EDIFACT o un formato personalizado.
* Determine los segmentos, elementos y subelementos dentro de la estructura EDI.
* Cree un descriptor de estructura que refleje con precisión la jerarquía y organización del mensaje EDI. Esto se puede hacer utilizando una sintaxis especial como XML o JSON.

<figure><img src="../../../../../../.gitbook/assets/docbits_sso_access_settings.png" alt="Docbits Sso Access Settings" width="273"><figcaption></figcaption></figure>

**Configurar transformaciones:**

* Utilice una herramienta o software adecuado que admita transformaciones EDI, como un traductor EDI.
* Defina las reglas para convertir el mensaje EDI al formato interno de su sistema y viceversa.
* Configure las transformaciones para interpretar y procesar segmentos, elementos y subelementos de acuerdo con los requisitos de su sistema. Pruebe las transformaciones a fondo para asegurarse de que los datos se interpreten y formateen correctamente.

<figure><img src="../../../../../../.gitbook/assets/docbits_sso_idp_config.png" alt="Docbits Sso Idp Config" width="268"><figcaption></figcaption></figure>

**Configurar rutas de extracción para una extracción y formato de datos óptimos:**

* Identifique los campos de datos que se extraerán y transferirán a su sistema interno.
* Defina rutas o reglas de extracción para extraer los campos de datos relevantes de los mensajes EDI.
* Tenga en cuenta las diferentes variaciones y formatos que pueden ocurrir en los mensajes EDI entrantes y asegúrese de que las rutas de extracción sean lo suficientemente flexibles para acomodarlos.
* Valide los resultados de la extracción para asegurarse de que se extraigan los campos de datos correctos y se formateen correctamente.

<figure><img src="../../../../../../.gitbook/assets/docbits_edi_validate_extraction.png" alt="Docbits Edi Validate Extraction" width="92"><figcaption></figcaption></figure>

Al definir cuidadosamente el descriptor de estructura, configurar las transformaciones y configurar las rutas de extracción, puede asegurarse de que la extracción y el formato de los datos se realicen de manera óptima en sus plantillas EDI. Esto ayudará a mejorar la eficiencia y precisión de sus comunicaciones comerciales electrónicas.
