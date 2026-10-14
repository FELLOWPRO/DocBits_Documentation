# Canales PDP/PPF obligatorios – PEPPOL solo como transporte en la facturación electrónica de Francia de 2026

## Se requiere PDP o PPF para las facturas electrónicas B2B nacionales

Según el mandato de facturación electrónica de Francia de 2026, las empresas no pueden basarse únicamente en la red PEPPOL para intercambiar facturas B2B nacionales. La ley exige que todas las facturas entre empresas francesas registradas a efectos del IVA se canalicen a través de una plataforma privada certificada (PDP) o del portal público de facturación del Estado (PPF) para cumplir los [requisitos](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform) legales ￼. En otras palabras, las empresas ya no enviarán facturas directamente a sus clientes: deberán transmitirlas a través de una plataforma de facturación electrónica aprobada (una PDP) o a través del [portal](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html) del Gobierno ￼. Esto garantiza que la autoridad fiscal reciba los datos requeridos en tiempo real. El simple intercambio de facturas a través de PEPPOL sin la intervención de una PDP/PPF acreditada no cumpliría las obligaciones de notificación y transmisión exigidas.

<figure><img src="../../.gitbook/assets/Picture 1.png" alt=""><figcaption></figcaption></figure>

### Introducción a la oferta de servicio

El modo API permite a los usuarios acceder a todas las funciones que tienen a su disposición desde las herramientas informáticas ya desplegadas en las estructuras de los partners. Existen dos métodos de integración:

### ·       Integración en los sistemas de información (SI):

Las API se integran directamente en los sistemas de información o en el software de gestión de las partes que emiten y reciben facturas, o de sus operadores de desmaterialización (OD). Así, los usuarios pueden acceder directamente a las funciones de la solución y a sus mejoras desde sus herramientas informáticas habituales, internas o proporcionadas por su OD.

Las API también pueden integrarse en el SI de las PDP para darles mayor flexibilidad (en comparación con el modo EDI), con algunas API dedicadas a su uso.

### ·       Integración en software de terceros:

Los editores de software podrán ofrecer programas basados en las API. Según el modo elegido por el editor, la conexión podrá realizarla el propio editor o el cliente durante la instalación o el despliegue en su SI. Este software de terceros complementará el sistema de información del cliente añadiendo una capa de comunicación con el PPF.

<figure><img src="../../.gitbook/assets/Picture 6.png" alt=""><figcaption></figcaption></figure>

## PEPPOL utilizado únicamente como capa de interoperabilidad

Francia adopta PEPPOL como parte de su infraestructura, pero solo como capa de transporte dentro del marco de las PDP, no como vía de cumplimiento independiente.  La autoridad fiscal francesa (DGFiP) se convierte en la Peppol Authority para estandarizar la [interconexión](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html) de las PDP. Todas las PDP certificadas están obligadas a interconectarse a través de la red PEPPOL para intercambiar [facturas](https://nymus.be/fr/facturation-electronique-en-france/) .  Esto significa que PEPPOL facilitará la interoperabilidad entre las plataformas autorizadas, pero no sustituirá la necesidad de dichas plataformas.  En la práctica, una empresa solo puede utilizar PEPPOL trabajando a través de una PDP (o del PPF en su función limitada) que use PEPPOL para enviar o recibir facturas. Así lo confirma la orientación oficial: el portal público se centra en la recogida de datos, mientras que la distribución de facturas se realizará exclusivamente a través de las PDP, que aprovecharán redes como [PEPPOL](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france) para el [intercambio](https://nymus.be/fr/facturation-electronique-en-france/) .

\


<figure><img src="../../.gitbook/assets/Picture 2.png" alt=""><figcaption></figcaption></figure>

## Conexión de un hub:

El hub proporciona a sus clientes una solución web o de aplicación que les permite realizar las distintas llamadas a la API. **Es, por tanto, el hub quien realiza las llamadas a la API en nombre de todos sus clientes**. En este caso, cada partner debe disponer de una cuenta técnica, pero solo el hub necesita una aplicación en PISTE y una conexión con el PPF.

<figure><img src="../../.gitbook/assets/Picture 5.png" alt=""><figcaption></figcaption></figure>



Fuente: el artículo 91 de la Ley de Finanzas de 2024 de Francia (resumido por EY) establece que las facturas electrónicas deben enviarse a través de una PDP certificada o del portal estatal .  Las actualizaciones de la autoridad fiscal francesa aclaran además que, tras las reformas de 2024, las empresas deben utilizar una PDP registrada para la facturación electrónica B2B (el PPF dejará de servir como plataforma de intercambio gratuita) .  PEPPOL se está implantando para conectar estas PDP, no como un canal alternativo fuera del sistema . Esto confirma que utilizar únicamente la red PEPPOL no es suficiente: el cumplimiento del régimen de facturación electrónica de Francia de 2026 exige la integración con el PPF o con una PDP certificada, con PEPPOL como simple red de entrega subyacente entre dichas plataformas.

<div><figure><img src="../../.gitbook/assets/Picture 3.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Picture 4.png" alt=""><figcaption></figcaption></figure></div>
