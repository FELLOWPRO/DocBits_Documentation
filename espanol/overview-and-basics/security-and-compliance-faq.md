# DocBits (FELLOWPRO AG) — Cuestionario de Seguridad y Cumplimiento

**Proveedor:** DocBits por FELLOWPRO AG | **Alojamiento:** Fráncfort, Alemania | **Certificado ISO 27001** | **Fecha:** 2026-03-04

---

## Leyenda de Estado

| Símbolo | Significado |
|---------|---------|
| ✅ Confirmado | Respuesta verificada desde documentación oficial de DocBits o fuentes públicas |
| ✅ Parcial | Respuesta parcial; se necesita detalle adicional del equipo de DocBits |
| ❓ Por Confirmar | Sin información pública disponible — debe confirmarse directamente con DocBits/FELLOWPRO |
| ⚠️ Necesita Aclaración | Información pública genera preocupaciones o ambigüedad que requiere aclaración explícita del proveedor |

---

## 🔹 Ubicación de Datos y Residencia

### 1. ¿Exactamente dónde se aloja el entorno de producción?

**Respuesta:** Se aloja en infraestructura de nube AWS en Fráncfort, Alemania. Utiliza S3 para almacenamiento e OpenSearch para indexación de registros. DocBits está certificado ISO 27001. Todas las conexiones están aseguradas mediante SSH, HTTPS y protocolos de cifrado estándar de la industria.

**Estado:** ✅ Confirmado

**Notas:** AWS Fráncfort confirmado (S3 + OpenSearch). Solicitar código de región AWS específico (eu-central-1) y si es de AZ única o múltiple.

---

### 2. ¿Dónde se aloja el entorno de Recuperación ante Desastres (DR)?

**Respuesta:** DR aprovecha ubicación de copia de seguridad secundaria en Ámsterdam, Países Bajos (UE). Combinado con sitio principal en Fráncfort, proporciona redundancia geográfica dentro de la UE.

**Estado:** ✅ Confirmado

**Notas:** Fráncfort (principal) + Ámsterdam (secundaria). Ambas ubicaciones en UE. Solicitar objetivos RTO/RPO y detalles del proceso de conmutación.

---

### 3. ¿Dónde se almacenan las copias de seguridad?

**Respuesta:** Las copias de seguridad se almacenan en dos ubicaciones de la UE:
- **Principal:** Fráncfort, Alemania
- **Secundaria:** Ámsterdam, Países Bajos

Programa de copias de seguridad: Diarias, semanales, trimestrales y anuales.

**Estado:** ✅ Confirmado

**Notas:** Programa de copias de seguridad integral (diarias/semanales/trimestrales/anuales) en dos ubicaciones de la UE. Todos los datos permanecen dentro de la UE. Confirmar cifrado de copias de seguridad y frecuencia de pruebas de restauración.

---

### 4. ¿Hay opciones de particionamiento geográfico (por ejemplo, solo Reino Unido)?

**Respuesta:** Dos regiones de centro de datos disponibles:
- **Fráncfort, Alemania** — para todos los clientes de la UE
- **Nueva York, EE. UU.** — solo para clientes de EE. UU.

Los datos de clientes de la UE se alojan exclusivamente en Fráncfort. Actualmente no hay opción solo para Reino Unido.

**Estado:** ✅ Confirmado

**Notas:** Clientes de la UE solo en Fráncfort — sin mezcla de datos entre regiones. Alojamiento solo para Reino Unido no disponible; los clientes del Reino Unido se servían desde Fráncfort. Aclarar si hay regiones adicionales en la hoja de ruta.

---

### 5. ¿Los datos están cifrados en reposo y en tránsito?

**Respuesta:** Todas las conexiones entre componentes están aseguradas usando protocolos de cifrado estándar de la industria (SSH, HTTPS). La certificación ISO 27001 exige controles de cifrado.

**Estado:** ✅ Confirmado

**Notas:** Confirmar estándares de cifrado específicos (por ejemplo, AES-256 en reposo, TLS 1.2+ en tránsito).

---

## 🔹 Manejo de Modelos de IA/ML

### 6. ¿Se envía el contenido de facturas a algún host de modelo de terceros (por ejemplo, OpenAI, Azure AI)?

**Respuesta:** Los modelos de IA NO se envían a hosts de terceros. DocBits utiliza modelos de Mistral AI ejecutándose en Fráncfort, Alemania — misma ubicación que el entorno de producción. Ningún dato sale de la región de Fráncfort para procesamiento de IA.

**Estado:** ✅ Confirmado

**Notas:** Modelos Mistral alojados en Fráncfort. Sin llamadas a API de terceros para procesamiento de documentos. Completamente autónomo.

---

### 7. ¿Se utilizan documentos extraídos para entrenar modelos más amplios entre clientes?

**Respuesta:** Sí — DocBits utiliza "inteligencia colectiva de IA" que entrena modelos de clasificación y extracción en todos los clientes. Sin embargo, la tecnología funciona como un mapa a través de los datos — aprende las coordenadas/posiciones estructurales de campos de datos en documentos, NO el contenido real del documento. Los datos crudos del documento no se comparten entre inquilinos.

**Estado:** ✅ Confirmado

**Notas:** La inteligencia colectiva aprende patrones de diseño estructural (coordenadas de campos/posiciones), no contenido de documentos. Esto significa que ningún dato de cliente (montos de factura, nombres de proveedores, etc.) se comparte entre inquilinos — solo conocimiento de estructura de documentos.

---

### 8. ¿Puede restringir el entrenamiento del modelo solo a su inquilino?

**Respuesta:** Sin opción de aislamiento de modelo por inquilino. Sin embargo, los modelos de IA compartidos solo aprenden coordenadas de diseño de documentos y patrones estructurales — no contenido de documento real ni datos comerciales. Los clientes pueden entrenar adicionalmente tipos de documentos personalizados limitados a su propio inquilino.

**Estado:** ✅ Confirmado

**Notas:** Bajo riesgo: Los modelos compartidos aprenden solo datos posicionales/estructurales (coordenadas), no contenido comercial. El entrenamiento de tipo de documento personalizado permanece limitado al inquilino.

---

### 9. ¿Dónde se alojan y ejecutan los modelos de IA/ML?

**Respuesta:** Los modelos de IA/ML (Mistral) se alojan y ejecutan en Fráncfort, Alemania — misma región que el entorno de producción.

**Estado:** ✅ Confirmado

**Notas:** Bien: El procesamiento de IA permanece dentro de Fráncfort. Sin transferencia de datos a infraestructura de IA externa.

---

### 10. ¿Qué tecnologías de IA/ML se utilizan (motor OCR, LLM, NLP)?

**Respuesta:** DocBits utiliza IA, OCR, aprendizaje automático para extracción. Admite 120+ idiomas. Afirma precisión del 96%+. También utiliza IA Generativa para función "AI Tags".

**Estado:** ✅ Parcial

**Notas:** Solicitar detalles de modelo específicos: OCR propio vs. de terceros, qué LLM potencia características de IA Generativa.

---

### 11. ¿Hay opción para implementación de modelo de IA local?

**Respuesta:** La documentación de arquitectura de DocBits hace referencia a ambas opciones de implementación "Cliente en la Nube de DocBits" y "DocBits Local".

**Estado:** ✅ Parcial

**Notas:** Confirmar alcance de opción local: ¿Incluye procesamiento completo de IA o solo almacenamiento de documentos?

---

## 🔹 Acceso a Datos y Registros

### 12. ¿Quién (soporte de proveedor/ingenieros) puede acceder a documentos crudos y datos de Infor LN?

**Respuesta:** FELLOWPRO AG tiene un Oficial de Protección de Datos designado (Daniel Jordan). DPAs con subprocesadores están en su lugar por GDPR. ISO 27001 exige controles de acceso.

**Estado:** ✅ Parcial

**Notas:** Solicitar a DocBits: Lista exacta de roles de personal con acceso a documentos crudos. ¿El acceso es por necesidad / bajo demanda?

---

### 13. ¿Qué controles de acceso y registro existen para personal del proveedor?

**Respuesta:** La certificación ISO 27001 requiere controles de acceso documentados, pistas de auditoría y medidas de seguridad. DocBits mantiene pista de auditoría para cumplimiento y revisión.

**Estado:** ✅ Parcial

**Notas:** Solicitar: Detalles de RBAC, requisitos de MFA, gestión de acceso privilegiado (PAM), y si el acceso se registra con pistas de auditoría inmutables.

---

### 14. ¿Cuánto tiempo se conservan los registros de acceso?

**Respuesta:** Los registros se almacenan en AWS S3 en Fráncfort e OpenSearch. Registros accesibles al cliente retenidos por 30 días. Registros internos retenidos por 3 meses.

**Estado:** ✅ Confirmado

**Notas:** S3 + OpenSearch en Fráncfort. Retención de 30 días para acceso de cliente / 3 meses para retención interna. Confirmar si los registros son inmutables/a prueba de manipulación.

---

### 15. ¿Cuánto tiempo se retienen en DocBits documentos cargados / datos extraídos?

**Respuesta:** Los clientes pueden configurar retención de datos en configuración. Opciones: 30 días o 3 meses. Después del período configurado, documentos y datos extraídos se eliminan automáticamente de servidores de DocBits.

**Estado:** ✅ Confirmado

**Notas:** Retención configurable por cliente (30 días / 3 meses). Confirmar: ¿La eliminación incluye todas las copias (S3, OpenSearch, datos de entrenamiento de IA)?

---

### 16. ¿Pueden los clientes solicitar eliminación de datos bajo demanda?

**Respuesta:** FELLOWPRO AG cumple con derechos de sujeto de datos de GDPR incluyendo solicitudes de eliminación. DPO procesa estas solicitudes por GDPR Art. 17.

**Estado:** ✅ Confirmado

**Notas:** Confirmar: ¿La eliminación cubre todas las copias incluyendo copias de seguridad y datos de entrenamiento de IA derivados del inquilino?

---

### 17. ¿Qué subprocesadores tienen acceso a datos de clientes?

**Respuesta:** Cloudflare se utiliza para protección de bots/DDoS. DPAs están en su lugar con todos los subprocesadores por requisitos de GDPR.

**Estado:** ✅ Parcial

**Notas:** Solicitar lista completa de subprocesadores. Cloudflare confirmado; solicitar sobre proveedor de alojamiento en nube, proveedores de servicios de IA, etc.

---

### 18. ¿Qué certificaciones y marcos de cumplimiento tiene DocBits?

**Respuesta:** Certificado ISO 27001. Cumple con GDPR. Mantiene DPAs con todos los subprocesadores. DPO designado.

**Estado:** ✅ Confirmado

**Notas:** Solicitar: ¿SOC 2 Tipo II? ¿Reportes de prueba de penetración? ¿ISO 27701 (privacidad)? ¿Cronograma de auditoría anual?

---

## 🔹 Alcance de Integración (Infor LN)

### 19. ¿Cuál es la lista exacta de campos de datos sacados de maestros de LN para validación?

**Respuesta:** Datos maestros importados vía Infor BODs:
- **Proveedores:** Sync.SupplierPartyMaster, Sync.RemitToPartyMaster
- **Órdenes de Compra:** Sync.PurchaseOrder
- **Plan de Cuentas:** Sync.CodeDefinition (ChartOfAccounts)
- **Dimensiones Flexibles:** Sync.CodeDefinition (FlexDimensions)
- **Códigos Fiscales:** vía publicación de BOD

**Estado:** ✅ Confirmado

**Notas:** Solicitar a DocBits lista completa de BOD y documentación de mapeo de nivel de campo para configuración específica de LN.

---

### 20. ¿Qué campos de encabezado específicos se exportan de vuelta a LN?

**Respuesta:** Los campos de exportación de encabezado incluyen: SupplierCode, PurchaseType, InvoiceType, InvoiceNumberSupplier, InvoiceDate, InvoiceAmount, InvoiceCurrency, RateDeterminer, RateDate, TaxCountry, TransactionEntryDate, Reference, IDMReference, TaxBaseAmount, InvoiceDocumentType, y más.

**Estado:** ✅ Confirmado

**Notas:** Revisar archivo de mapeo de campos para entorno específico. Confirmar que todos los campos estáticos coincidan con configuración de compañía de LN.

---

### 21. ¿Las operaciones de escritura hacia atrás se limitan solo a objetos de interfaz de AP/PO?

**Respuesta:** La exportación utiliza BOD Sync.CaptureDocument que se transforma a BODs objetivo (por ejemplo, BODs de factura de AP) en ION Desk. Los datos también se exportan a Infor IDM para archivo de documentos.

**Estado:** ✅ Parcial

**Notas:** Confirmar: ¿DocBits escribe SOLO en objetos de recibos de factura de AP y PO? ¿Otros módulos de LN tocados? ¿Qué hay del alcance de escritura de IDM?

---

### 22. ¿Qué método de integración se usa (API ION, BODs, DB directo)?

**Respuesta:** Integración vía API ION de Infor, ION Desk, y BODs Estándar de Infor. Sin acceso directo a base de datos. Utiliza archivos de API ION y cuentas de servicio para autenticación.

**Estado:** ✅ Confirmado

**Notas:** Bien: Sin acceso directo a DB. Toda comunicación vía capa de integración estándar de Infor.

---

### 23. ¿Qué autenticación/autorización se usa para conectividad de LN?

**Respuesta:** Utiliza Archivos de API ION (credenciales de cliente OAuth2) con IDs de Cliente de API ION y cuentas de servicio creadas en InforOS.

**Estado:** ✅ Confirmado

**Notas:** Asegurar que cuentas de servicio sigan principio de menor privilegio. Revisar permisos otorgados al usuario de API ION de DocBits.

---

### 24. ¿La transferencia de datos entre DocBits y LN está cifrada de extremo a extremo?

**Respuesta:** Todas las conexiones entre componentes están aseguradas usando cifrado estándar de la industria (SSH, HTTPS).

**Estado:** ✅ Confirmado

**Notas:** Comunicación de API ION usa HTTPS/TLS. Confirmar versión TLS mínima (1.2+).

---

### 25. ¿Qué tipos de documento se soportan más allá de facturas de AP?

**Respuesta:** Soporta facturas, notas de entrega/recibos, presupuestos, confirmaciones de pedidos, contratos, y más. Maneja facturas con PO y sin PO.

**Estado:** ✅ Confirmado

**Notas:** Aclarar qué tipos de documento se escriben de vuelta a LN vs. solo se almacenan en IDM.
