# Facturación electrónica en Francia: plataformas autorizadas y PEPPOL

## Normas y calendario actuales

Las facturas B2B nacionales francesas incluidas en la reforma entre empresas sujetas al IVA deben intercambiarse mediante una **plataforma autorizada (plateforme agréée, PA; antes PDP)**. El **portal público de facturación (PPF)** gestiona funciones de directorio público y recopilación de datos fiscales; no es una plataforma alternativa de intercambio de estas facturas.

* **1 de septiembre de 2026:** Todas las empresas incluidas deben poder recibir facturas electrónicas. Las grandes empresas (GE) y las empresas de tamaño intermedio (ETI) también deben emitirlas y cumplir sus obligaciones de e-reporting desde esa fecha.
* **1 de septiembre de 2027:** Las obligaciones de emisión y e-reporting se aplican a las pequeñas y medianas empresas (PME) y a las microempresas.

La obligación depende del ámbito de la operación y de la categoría de empresa. Consulte la [guía oficial de plataformas autorizadas](https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees), el [calendario de aplicación](https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation) y la [respuesta ministerial](https://www.senat.fr/questions/base/2026/qSEQ260107185.html).

## PEPPOL e interoperabilidad

PEPPOL puede ofrecer transporte e interoperabilidad entre sistemas y plataformas conectados. Utilizarlo no sustituye la obligación de recurrir a una PA para los intercambios incluidos en la normativa francesa. Una conexión PEPPOL por sí sola no demuestra el cumplimiento de las obligaciones de intercambio y comunicación de datos.

Para el catálogo de formatos de DocBits, consulte [Resumen de estándares de factura electrónica](../../administration-and-setup/settings/global-settings/document-types/edi/currently-supported-e-invoice-standards/README.md).

## Contexto técnico histórico

Los seis diagramas y las descripciones de API siguientes se conservan como contexto técnico de documentación anterior sobre PPF/PDP. Utilizan la terminología y arquitectura antiguas; no describen una opción actual para intercambiar facturas B2B obligatorias mediante el PPF. Compruebe las especificaciones actuales de las PA y los servicios públicos antes de implementar una integración.

<figure><img src="../../.gitbook/assets/Picture 1.png" alt="Diagrama del ciclo de vida de la facturación electrónica francesa con las fases de preparación, recepción, validación y pago y los estados del proveedor y del comprador"><figcaption><p>Diagrama histórico del ciclo de vida: preparación y emisión, recepción, validación/devolución y pago, con las etiquetas de estado del proveedor y del comprador visibles en cada fase.</p></figcaption></figure>

### Modelo histórico de servicios API

El modelo anterior describía el acceso a las funciones disponibles desde las herramientas informáticas de las organizaciones asociadas mediante dos métodos de integración:

* **Sistemas de información (IS):** Las API se integraban en sistemas de emisores, receptores u operadores de desmaterialización (OD). Algunas estaban destinadas a sistemas PDP como alternativa a la integración EDI.
* **Software de terceros:** Los desarrolladores podían añadir una capa de comunicación al sistema del cliente. Las referencias anteriores a una conexión con el PPF pertenecen a ese modelo histórico y no constituyen una vía actual de intercambio de facturas.

<figure><img src="../../.gitbook/assets/Picture 6.png" alt="Diagrama del emisor y el receptor que intercambian facturas mediante portales de servicio OD-PDP y el PPF, con control y recuperación de datos"><figcaption><p>Diagrama histórico de interconexión: el emisor y el receptor se conectan mediante software de terceros, portales de servicio y bloques OD/PDP alrededor del bloque de control y recuperación de datos del PPF.</p></figcaption></figure>

### Diagrama histórico de interconexión

Este diagrama ilustra el contexto anterior de interconexión de plataformas. Las implementaciones actuales deben seguir los requisitos de las PA; aquí no se afirma que todos los intercambios deban utilizar una única red de transporte.

<figure><img src="../../.gitbook/assets/Picture 2.png" alt="Diagrama de controles del flujo, la factura y los datos de facturación: los envíos del proveedor pasan por controles técnicos, de aplicación y funcionales con rechazos"><figcaption><p>Diagrama histórico de controles: se muestran controles técnicos, de aplicación y funcionales y de negocio para envíos manuales, por API y por EDI, junto con los resultados no admisible, rechazado y denegado.</p></figcaption></figure>

### Conexión histórica de un concentrador

El modelo anterior describía una solución web o de aplicación en la que **el concentrador realizaba llamadas API en nombre de sus clientes**. Indicaba una cuenta técnica para cada socio y una aplicación en PISTE más una conexión al PPF para el concentrador. Son detalles de una arquitectura histórica, no un procedimiento de integración actual verificado.

<figure><img src="../../.gitbook/assets/Picture 5.png" alt="Diagrama de socios con cuentas técnicas que se conectan mediante un concentrador a una aplicación en PISTE y a una conexión"><figcaption><p>Diagrama histórico del concentrador: los socios con cuentas técnicas se conectan mediante un concentrador a una aplicación en PISTE y a una conexión.</p></figcaption></figure>

### Referencias históricas

La documentación anterior citaba [el calendario y resumen jurídico antiguos](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform), [especificaciones de 2022](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html), [un resumen de la reforma de 2025](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html), [contexto de interconexión](https://nymus.be/fr/facturation-electronique-en-france/), [contexto de PEPPOL](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france) y [contexto de intercambio](https://nymus.be/fr/facturation-electronique-en-france/). Estos enlaces y los diagramas restantes se conservan como contexto histórico. Para las obligaciones actuales y la distinción entre intercambio mediante PA y funciones públicas del PPF, utilice las fuentes oficiales anteriores. La referencia antigua al artículo 91 de la Ley de Finanzas de 2024 no establece una opción actual de intercambio mediante PPF.

<figure><img src="../../.gitbook/assets/Picture 3.png" alt="Diagrama de flujo del proceso de emisión, desde la recepción del flujo EDI y por API pasando por controles de flujo, de aplicación y funcionales hasta la factura emitida"><figcaption><p>Diagrama histórico del proceso de emisión: los flujos EDI y API entrantes pasan por controles de flujo, de aplicación y funcionales antes de incorporar los datos de facturación; también se muestran las rutas de rechazo, los flujos salientes 1 y 2 y las notificaciones de ciclo de vida.</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/Picture 4.png" alt="Diagrama de flujo del proceso de recepción, desde la recepción del flujo EDI y por API pasando por controles con rechazo o denegación hasta la factura puesta a disposición"><figcaption><p>Diagrama histórico del proceso de recepción: los controles técnicos, de aplicación y funcionales incluyen reglas de negocio específicas, con rutas de rechazo o denegación; los datos aceptados dan lugar a una factura recibida y puesta a disposición, junto con el flujo 2 del destinatario y las notificaciones de ciclo de vida.</p></figcaption></figure>
