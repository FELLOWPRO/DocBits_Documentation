# Settings

<figure><img src="../../.gitbook/assets/settings_overview.png" alt="Settings Overview"><figcaption><p>Página Settings Overview</p></figcaption></figure>

El área Settings es su centro de control para configurar DocBits. Está organizada en cinco secciones principales:

## 1. Organization & Access

Gestione el perfil de su empresa y controle quién puede acceder a qué.

* **Company Information**: introduzca el nombre de su empresa, la dirección, el número de identificación fiscal y otros identificadores legales.
* **Users**: añada, edite o desactive cuentas de usuario y asigne roles (Admin, System Admin).
* **Sub-Organizations**: cree y gestione suborganizaciones para configuraciones con varias entidades.
* **Groups and Permissions**: defina grupos de usuarios y configure permisos detallados para cada grupo.

## 2. Document Processing

Configure cómo se importan, procesan y exportan los documentos.

* **Documents Expiry**: establezca reglas de eliminación automática de documentos (por ejemplo, eliminar tras 48 horas, 1 semana, etc.).
* **Document Types**: defina y configure los tipos de documento que procesa DocBits (facturas, pedidos, albaranes, etc.), incluidos campos, columnas de tabla, scripts y más.
* **Import**: configure cómo llegan los documentos a DocBits: por correo electrónico (IMAP/Office 365), FTP o carga de archivos. Configure los tipos de archivo y los límites de páginas.
* **Rule Management**: defina reglas de resolución de conflictos para la conciliación de facturas con pedidos de compra, incluidos los ajustes de tolerancia y los flujos de aprobación.
* **OCR Settings**: configure los umbrales de calidad del reconocimiento óptico de caracteres, el uso de E-Text, la versión de OCR con IA y el comportamiento de la extracción de tablas.
* **Classification and Extraction**: configure la división de documentos, el formato de importes, los métodos de extracción de tablas, las reglas de clasificación y los modelos de IA.
* **Lookup Master Data**: configure cómo se validan los datos extraídos con los datos maestros de su sistema ERP (por ejemplo, cuentas de proveedores, pedidos de compra).
* **List of Values**: cree y gestione listas de valores predefinidas que se utilizan en listas desplegables y en la validación de datos.
* **Export**: configure cómo y adónde se envían los documentos procesados: mediante Webhook, SFTP, SMB o integraciones de Infor (IDM, ION, M3, LN).
* **Module**: active o desactive funciones opcionales como PO Dashboard, Auto Accounting, Supplier Portal, Workflow Builder, QR-Code Extraction y más.
* **Decision Trees**: cree lógica de decisión basada en reglas con un diseñador visual. Admite varias políticas (Unique, First, Priority, Collect, etc.).
* **Agent Setup**: cree y gestione agentes de automatización y canales de comunicación para flujos de trabajo de procesamiento automático de documentos.

## 3. Communication & Notifications

Controle cómo se comunica DocBits con los usuarios y cómo procesa los correos electrónicos entrantes.

* **Email Notification**: configure alertas por correo electrónico para eventos de procesamiento de documentos y cambios de estado.
* **Email Templates**: cree y gestione plantillas de correo electrónico reutilizables para notificaciones, organizadas por tipo de documento.
* **Email Ingestion**: configure cómo se clasifican automáticamente los correos electrónicos entrantes y se convierten en documentos. Incluye reglas de clasificación, extracción de campos, procesamiento, gestión de remitentes y entrenamiento, organizadas por tipo de documento (Orders, Invoices, Quotes, Delivery Notes, COA, PO Confirm).

## 4. System & Administration

Supervise el estado del sistema, gestione las integraciones y mantenga la seguridad.

* **Integration & SSO**: configure claves de API para integraciones externas y establezca el inicio de sesión único (SSO) con proveedores de identidad.
* **Watchdog**: configure el servicio Watchdog para la importación automática de documentos desde directorios locales.
* **Dashboard**: personalice el comportamiento del panel: filtros, ajustes de exportación, permisos de acciones y opciones de visualización de estados.
* **Activity Logging**: consulte en tiempo real los registros de eventos del sistema filtrados por gravedad (Debug, Info, Warning, Error), intervalo de tiempo y servicio.
* **Analytics**: acceda a paneles de análisis detallados, como Logs Analytics, la supervisión de seguridad de autenticación (Auth Security) y API Metrics con Real User Monitoring (RUM).
* **Access Audit**: active y revise los registros de auditoría que rastrean todas las acciones de creación, actualización y eliminación en su organización con fines de cumplimiento normativo y seguridad.
* **System Licenses**: consulte y gestione la información y el uso de las licencias de API.
* **Cache Management**: configure los intervalos de limpieza automática de caché (TTL) para las cachés de Received Delivery, Purchase Order y Task/Notification.
* **Fulltext Search Settings**: configure las capacidades de búsqueda de texto completo en sus documentos y datos (requiere que el módulo Fulltext Search esté activado).

## 5. Supplier Settings

Configure el Supplier Portal y gestione los flujos de trabajo relacionados con proveedores.

* **Supplier General Settings**: configure los campos de invitación del portal de proveedores, los estados del flujo de trabajo (Not Invited, Open, Pending Registration, Approved, Rejected) y los ajustes de aprobación.
* **Email Templates**: cree y gestione plantillas de correo electrónico específicas para la comunicación con proveedores.
* **Supplier Layout**: personalice el diseño y la apariencia del Supplier Portal.
* **Export Configuration**: configure cómo se exportan los datos de proveedores a sistemas externos.
* **Supplier Group**: cree y gestione grupos de proveedores para categorizar y organizar a sus proveedores.
* **User and Supplier Group Mapping**: vincule usuarios internos con grupos de proveedores específicos para controlar la visibilidad y el acceso.
