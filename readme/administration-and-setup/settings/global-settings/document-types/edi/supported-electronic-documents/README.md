---
description: "Identifique la familia, la sintaxis, la versión y el perfil de eDocs configurados antes de probar el procesamiento de documentos."
---

# Formatos, versiones y guías por país de eDocs

Empiece por el documento de origen y la guía del país correspondiente. El nombre de un país por sí solo no identifica un formato de archivo. Una etiqueta de versión, una sintaxis XML y un perfil de negocio describen aspectos diferentes.

{% hint style="info" %}
Las tablas recogen una comprobación del catálogo de desarrollo realizada el 17 de octubre de 2026 y del código de procesamiento correspondiente. Describen las reglas y los componentes de configuración disponibles; no certifican todos los archivos, los requisitos legales ni el despliegue en producción. Su organización puede sobrescribir los valores predeterminados.
{% endhint %}

## Cómo interpretar la matriz de compatibilidad

- Familia: el formato de documento electrónico, como XRechnung, Factur-X, KSeF o CFDI.
- Sintaxis: el contenido real, como XML UBL, XML CII o un PDF con XML incrustado. Un PDF escaneado, una exportación JSON o una imagen QR no equivalen a ese contenido XML.
- Versión: la publicación o versión de esquema declarada. Una etiqueta de familia genérica no demuestra la compatibilidad con todas las versiones.
- Perfil: un subconjunto de negocio o de datos, como BASIC, EN16931, EXTENDED o la autofacturación. Un perfil no es una versión de publicación.
- Regla y componentes: la clasificación, Transformation, Preview y Extraction Paths son elementos independientes. Un perfil configurado no tiene necesariamente su propia regla de clasificación.
- Validación y transmisión: representar un archivo o extraer sus datos no verifica por sí solo todas las reglas legales, las firmas, la autorización fiscal o la entrega por red.

## Guías por país

La vista general enlaza a 39 guías de países y una guía internacional. Cada guía enumera las etiquetas exactas de formato y los componentes de configuración, junto con las capturas de DocBits, los vídeos y las pruebas de aceptación disponibles.

| País / región | Familias y alcance de versiones | Resultado del catálogo |
| --- | --- | --- |
| [Austria](countries/austria.md) | ebInterface 4.3, 5.0, 6.0 y 6.1 tienen entradas independientes. | Entradas encontradas |
| [Dinamarca](countries/denmark.md) | OIOUBL 2.1 es la entrada danesa identificada por nombre. | Entradas encontradas |
| [Finlandia](countries/finland.md) | Finvoice 1.3, 2.0, 2.01 y 3.0 tienen entradas independientes. TEAPPSXML es otra familia. | Entradas encontradas |
| [Francia](countries/france.md) | Factur-X tiene entradas genéricas y específicas de publicación, incluidas 1.0.05, 1.08 y 1.09. VRBL FR CIUS 1.0 es independiente. | Entradas encontradas |
| [Alemania](countries/germany.md) | XRechnung tiene trece etiquetas de versión de 1.0 a 3.0.2, cada una en CII y UBL. ZUGFeRD incluye perfiles antiguos y entradas 2.5 en CII y UBL. | Entradas encontradas |
| [Italia](countries/italy.md) | FatturaPA es la familia italiana configurada. | Entradas encontradas |
| [Países Bajos](countries/netherlands.md) | SI-UBL 2.0 tiene una entrada dedicada. | Entradas encontradas |
| [Noruega](countries/norway.md) | EHF Factura 3.0 figura junto a EHF Pedido, Respuesta de pedido y Aviso de despacho. | Entradas encontradas |
| [Polonia](countries/poland.md) | KSeF tiene entradas genéricas, FA2 y FA3. | Entradas encontradas |
| [Eslovenia](countries/slovenia.md) | e-SLOG 1.6 y 2.0 tienen entradas independientes. | Entradas encontradas |
| [España](countries/spain.md) | Facturae tiene entradas genéricas, 3.2, 3.2.1 y 3.2.2. | Entradas encontradas |
| [Suecia](countries/sweden.md) | Svefaktura 1.0 es la entrada sueca identificada por nombre. | Entradas encontradas |
| [Australia](countries/australia.md) | PINT A-NZ tiene entradas de reglas para facturas y notas de crédito compartidas con Nueva Zelanda. | Entradas encontradas |
| [Nueva Zelanda](countries/new-zealand.md) | PINT A-NZ tiene entradas de reglas para facturas y notas de crédito compartidas con Australia. | Entradas encontradas |
| [India](countries/india.md) | India GST E-Invoice y GST CreditNote tienen entradas independientes. | Entradas encontradas |
| [Indonesia](countries/indonesia.md) | Indonesia E-Faktur es la familia configurada. | Entradas encontradas |
| [China](countries/china.md) | El catálogo incluye Fapiao, E-Fapiao, General VAT Invoice y Special VAT Invoice. | Entradas encontradas |
| [Japón](countries/japan.md) | JP PINT y JP PINT Self-Billing son entradas independientes. | Entradas encontradas |
| [Corea del Sur](countries/korea.md) | Korea E-Tax Invoice y Korea NTS son familias configuradas. | Entradas encontradas |
| [Malasia](countries/malaysia.md) | MyInvois tiene entradas de reglas para facturas y notas de crédito. | Entradas encontradas |
| [Filipinas](countries/philippines.md) | Philippines EIS es la familia configurada. | Entradas encontradas |
| [Singapur](countries/singapore.md) | InvoiceNow tiene entradas para facturas y notas de crédito. InvoiceNow SG es otra etiqueta configurada. | Entradas encontradas |
| [Taiwán](countries/taiwan.md) | Taiwan eGUI es la familia configurada. | Entradas encontradas |
| [Tailandia](countries/thailand.md) | Thailand E-Tax Invoice es la familia configurada. | Entradas encontradas |
| [Vietnam](countries/vietnam.md) | Vietnam E-Invoice es la familia configurada. | Entradas encontradas |
| [Argentina](countries/argentina.md) | Argentina AFIP y Factura Electronica son etiquetas configuradas. | Entradas encontradas |
| [Brasil](countries/brazil.md) | Brasil tiene entradas NF-e, NFC-e, CT-e, NFS-e y SPED NFS-e. NFS-e incluye las versiones 1.00 y de 2.00 a 2.04; SPED incluye 1.00.02 y 1.01. | Entradas encontradas |
| [Chile](countries/chile.md) | Chile DTE tiene entradas de facturas, notas de crédito y guías de despacho. | Entradas encontradas |
| [Colombia](countries/colombia.md) | Colombia Factura Electronica y Documento Soporte tienen entradas independientes. | Entradas encontradas |
| [Costa Rica](countries/costa-rica.md) | La documentación anterior menciona Costa Rica, pero no se encontró ninguna entrada de clasificación o configuración coincidente en el catálogo de desarrollo inspeccionado. | Sin confirmar |
| [Ecuador](countries/ecuador.md) | Ecuador SRI tiene entradas genéricas, 1.0.0, 1.1.0, 2.0.0 y 2.1.0. La retención es un tipo de documento independiente. | Entradas encontradas |
| [México](countries/mexico.md) | Mexico CFDI 3.3 y 4.0 tienen entradas independientes. | Entradas encontradas |
| [Paraguay](countries/paraguay.md) | Paraguay DTE, SIFEN y SIFEN 150 son etiquetas configuradas. | Entradas encontradas |
| [Perú](countries/peru.md) | Peru CPE tiene entradas genéricas, UBL 2.0 y UBL 2.1. Factura Electronica es otra etiqueta. | Entradas encontradas |
| [Uruguay](countries/uruguay.md) | Uruguay CFE tiene entradas genéricas, 24 y 25. También figuran E-Factura y E-Nota Credito. | Entradas encontradas |
| [Kazajistán](countries/kazakhstan.md) | Kazakhstan ESF es la familia configurada. | Entradas encontradas |
| [Arabia Saudí](countries/saudi-arabia.md) | ZATCA Fatoorah, Reporting, Simplified y Tax Invoice tienen entradas independientes. | Entradas encontradas |
| [Turquía](countries/turkey.md) | Turkey E-Fatura y E-Arsiv son familias configuradas independientes. | Entradas encontradas |
| [Emiratos Árabes Unidos](countries/united-arab-emirates.md) | UAE VAT Invoice es la etiqueta configurada. | Entradas encontradas |
| [Internacional](countries/international.md) | Las entradas internacionales incluyen Peppol BIS 3.0, UBL 2.1, CII puro, EDI, INVOIC02, cXML, OCI, BOD y SPS Commerce RSX 7.7.4. | Entradas encontradas |

## Factur-X / ZUGFeRD: no deduzca una versión de publicación sin pruebas

Un CII Guideline ID armonizado puede identificar una familia y un perfil aunque varias publicaciones compartan el mismo marcador 1p0. Factur-X XMP Version 1.0 es un marcador de esquema, no una publicación como 1.08 o 1.09. El XMP de ZUGFeRD puede declarar su versión. Si no se dispone de metadatos de una fuente autorizada, mantenga el resultado de familia genérica y confirme el archivo original con el remitente.

MINIMUM y BASIC WL pueden omitir información de líneas de detalle necesaria en procesos posteriores. BASIC, EN16931/COMFORT y EXTENDED ofrecen distintas coberturas de datos. Un perfil más amplio puede incluir campos que su asignación de extracción no utiliza. Compruebe los campos necesarios con ejemplos reales.

## Compruebe un formato en su organización

1. Conserve el XML original o el PDF con su XML incrustado. Consulte el espacio de nombres, el identificador de esquema o de personalización y la versión y el perfil declarados.

2. Abra Configuración → Tipos de documento → E-Doc para el documento de negocio correspondiente. Busque el formato de documento electrónico exacto que aparece en la guía.

3. Compruebe el origen Default o Custom que se está utilizando y su versión de configuración activa. Revise Transformation, Preview y Extraction Paths. Guardar un borrador no lo activa.

4. Pruebe archivos de origen representativos de cada sintaxis, versión y documento de negocio que necesite. Verifique los campos clave, los importes, los impuestos, la clasificación como factura o nota de crédito y la exportación al ERP.

5. Confirme por separado la política de validación y el transporte. Conserve las asignaciones personalizadas y compruebe las aprobaciones y el historial de exportación antes de reiniciar documentos existentes.

[Pruebas de aceptación](../credit-note-recognized-as-invoice.md)

[Configurar DocBits con Claude o Codex](../../../../../../advanced-functions-and-tools/docbits-mcp/configuration-with-claude-or-codex.md): conexión, prompts, vistas previas, cambios con versiones, comprobaciones y reversión.
