# Acceso SQL

<figure><img src="../../.gitbook/assets/sql_direct_access_settings.png" alt="Configuración del acceso directo SQL"><figcaption></figcaption></figure>

## Descripción general

En el módulo de configuración de DocBits, los administradores pueden acceder directamente a la base de datos de BI mediante SQL. Esta función está pensada para la gestión avanzada de datos y las necesidades de informes personalizados.

### Acceso al acceso directo SQL

Diríjase a la sección SQL Direct Access del módulo de configuración. Allí encontrará las credenciales y los detalles de acceso, incluidos el nombre de usuario, la contraseña, el nombre de la base de datos y la información del host.

* **Nombre de usuario:** user\_23f3d6
* **Contraseña:** _Cifrada_
* **Base de datos:** demo
* **Host:** consulte la captura de pantalla

## **Ejemplo de detalles de acceso:**

```sql
SELECT
    COUNT(*),
    status,
    invoice_type
FROM dashboard
GROUP BY
    status,
    invoice_type

```

#### Resultados de una consulta de ejemplo

Los siguientes resultados muestran el número de documentos por estado y tipo de factura:

* **Listo para validación:** 71 facturas, 6 sin especificar
* **Pendiente de Confirmación:** 1 sin especificar
* **Terminado:** 3 sin especificar, 1 factura
* **Error:** 2 sin especificar

#### Uso de clickhouse-client para el acceso desde la terminal

Para los desarrolladores que prefieren trabajar en la terminal, el acceso puede establecerse mediante `clickhouse-client`:

```bash
clickhouse-client --host <hostname_or_ip> --port <port> --user <username> --password <your_password> --database <database_name>

```

### Creación de vistas materializadas

Recomendamos crear vistas materializadas para precalcular datos y mejorar el rendimiento en herramientas de análisis como PowerBI:

```sql
SELECT toStartOfWeek(created_on) as week_start, sum(toFloat64OrZero(field_value)) as total_sum
FROM document_extracted_data
WHERE field_name = 'total_amount'
GROUP BY week_start

```

Este ejemplo muestra cómo agrupar los importes totales por la semana en que se crearon, lo que resulta útil para resúmenes financieros semanales o pistas de auditoría.

## Recursos adicionales

Para obtener más ayuda o configuraciones avanzadas, consulte a nuestro equipo de soporte o acceda a nuestra completa formación en vídeo disponible en la sección de ayuda.
