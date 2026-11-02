# Facturación electrónica en Francia: plataformas autorizadas y PEPPOL

## Normas y calendario actuales

Las facturas B2B nacionales francesas incluidas en la reforma entre empresas sujetas al IVA deben intercambiarse mediante una **plataforma autorizada (plateforme agréée, PA; antes PDP)**. El **portal público de facturación (PPF)** gestiona funciones de directorio público y recopilación de datos fiscales; no es una plataforma alternativa de intercambio de estas facturas.

* **1 de septiembre de 2026:** Todas las empresas incluidas deben poder recibir facturas electrónicas. Las grandes empresas (GE) y las empresas de tamaño intermedio (ETI) también deben emitirlas y cumplir sus obligaciones de e-reporting desde esa fecha.
* **1 de septiembre de 2027:** Las obligaciones de emisión y e-reporting se aplican a las pequeñas y medianas empresas (PME) y a las microempresas.

La obligación depende del ámbito de la operación y de la categoría de empresa. Consulte la [guía oficial de plataformas autorizadas](https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees), el [calendario oficial](https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation) y la [respuesta ministerial](https://www.senat.fr/questions/base/2026/qSEQ260107185.html).

## PEPPOL e interoperabilidad

PEPPOL puede ofrecer transporte e interoperabilidad entre sistemas y plataformas conectados. Utilizarlo no sustituye la obligación de recurrir a una PA para los intercambios incluidos en la normativa francesa. Una conexión PEPPOL por sí sola no demuestra el cumplimiento de las obligaciones de intercambio y comunicación de datos.

## Contexto técnico histórico

Los seis diagramas y las descripciones de API siguientes se conservan como contexto técnico de documentación anterior sobre PPF/PDP. Utilizan la terminología y arquitectura antiguas; no describen una opción actual para intercambiar facturas B2B obligatorias mediante el PPF. Compruebe las especificaciones actuales de las PA y los servicios públicos antes de implementar una integración.

<figure><img src="../../.gitbook/assets/Picture 1.png" alt="Diagrama del ciclo de vida de una factura desde Supplier hasta los estados Submitted, Received by the platform y Made available, con los resultados Rejected, Refused, Disputed, Partially approved, In hand y Completed"><figcaption></figcaption></figure>

### Modelo histórico de servicios API

El modelo anterior describía el acceso a las funciones disponibles desde las herramientas informáticas de las organizaciones asociadas mediante dos métodos:

* **Sistemas de información (IS):** Las API se integraban en sistemas de emisores, receptores u operadores de desmaterialización (OD). Algunas estaban destinadas a sistemas PDP como alternativa a la integración EDI.
* **Software de terceros:** Los desarrolladores podían añadir una capa de comunicación al sistema del cliente. Las referencias anteriores a una conexión con el PPF pertenecen a ese modelo histórico y no constituyen una vía actual de intercambio de facturas.

<figure><img src="../../.gitbook/assets/Picture 6.png" alt="Diagrama de un Issuer OD-PDP y un Receiver OD-PDP vinculados a través de portales de servicios y software de terceros, con un paso de control y recuperación de datos entre ellos"><figcaption></figcaption></figure>

### Diagrama histórico de interconexión

Este diagrama ilustra el contexto anterior de interconexión de plataformas. Las implementaciones actuales deben seguir los requisitos de las PA; aquí no se afirma que todos los intercambios deban utilizar una única red de transporte.

<figure><img src="../../.gitbook/assets/Picture 2.png" alt="Diagrama de las tres capas de control numeradas: controles técnicos, controles de aplicación y controles funcionales y de negocio, cada una de las cuales alimenta un paso posterior del proceso"><figcaption></figcaption></figure>

### Conexión histórica de un concentrador

El modelo anterior describía una solución web o de aplicación en la que **el concentrador realizaba llamadas API en nombre de sus clientes**. Indicaba una cuenta técnica para cada socio y una aplicación en PISTE más una conexión al PPF para el concentrador. Son detalles de una arquitectura histórica, no un procedimiento de integración actual verificado.

<figure><img src="../../.gitbook/assets/Picture 5.png" alt="Diagrama del modelo de hub con un socio, una cuenta técnica, el hub, una aplicación bajo PISTE y una conexión"><figcaption></figcaption></figure>

### Referencias históricas

La documentación anterior citaba [el calendario y resumen jurídico antiguos](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform), [especificaciones de 2022](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html), [un resumen de la reforma de 2025](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html), [contexto de interconexión](https://nymus.be/fr/facturation-electronique-en-france/), [contexto de PEPPOL](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france) y [contexto de intercambio](https://nymus.be/fr/facturation-electronique-en-france/). Estos enlaces y los diagramas restantes se conservan como contexto histórico. Para las obligaciones actuales y la distinción entre intercambio mediante PA y funciones públicas del PPF, utilice las fuentes oficiales anteriores. La referencia antigua al artículo 91 de la Ley de Finanzas de 2024 no establece una opción actual de intercambio mediante PPF.

<div><figure><img src="../../.gitbook/assets/Picture 3.png" alt="Diagrama de la recepción de un flujo EDI y del flujo 2 vía API que superan controles funcionales de formato semántico, directorio y consistencia de datos antes de incorporar los datos de facturación y obtener una factura enviada"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Picture 4.png" alt="Diagrama de un flujo EDI y un flujo API que pasan controles funcionales y reglas de negocio específicas antes del rechazo o denegación de la factura o de que la factura se reciba y quede disponible"><figcaption></figcaption></figure></div>
