# Pruebas de Automatización de Facturas con DocBits

## Descripción General

Este documento describe el plan de pruebas para la automatización de facturas utilizando DocBits con Infor LN o M3. Incluye detalles de los casos de prueba, preparación de pruebas, pasos de ejecución y procesos de soporte.

## Casos de Prueba

| ID | Caso de Prueba                                                                            | Descripción                                                                                                                                                                                                         | Estado     |
| -- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| 1  | Facturas de Costos                                                                        | Las facturas sin orden de compra se procesan correctamente en DocBits y se exportan a LN como “factura de costos”.                                                                                                  | POR PROBAR |
| 2  | Factura Relacionada con Orden de Compra con Coincidencia Perfecta                         | Las facturas relacionadas con órdenes de compra se procesan correctamente en DocBits con una coincidencia perfecta de la factura a la OC, ya que el número de artículo, la cantidad y el precio unitario coinciden. | POR PROBAR |
| 3  | Facturas Relacionadas con Orden de Compra con Cantidad Diferente                          | Las facturas relacionadas con órdenes de compra se procesan en DocBits, pero en el módulo de coincidencia de OC, tenemos un desajuste en la cantidad.                                                               | POR PROBAR |
| 4  | Facturas Relacionadas con Orden de Compra con Precio Unitario Diferente                   | Las facturas relacionadas con órdenes de compra se procesan en DocBits, pero en el módulo de coincidencia de OC, tenemos un desajuste en el precio unitario.                                                        | POR PROBAR |
| 5  | Facturas Relacionadas con Orden de Compra con Número de Artículo Diferente o No Existente | Las facturas relacionadas con órdenes de compra se procesan en DocBits, pero en el módulo de coincidencia de OC, tenemos un desajuste o un número de artículo no existente.                                         | POR PROBAR |
| 6  | Facturas Relacionadas con Orden de Compra con un Desajuste dentro de la Tolerancia        | Las facturas relacionadas con órdenes de compra se procesan en DocBits, pero en el módulo de coincidencia de OC, tenemos un desajuste en la cantidad o el precio unitario, pero está dentro de la tolerancia.       | POR PROBAR |
| 7  | Notas de Crédito                                                                          | Las notas de crédito se procesan correctamente en DocBits y se exportan a LN. Aclarar si los montos deben ser exportados con un signo positivo o negativo.                                                          | POR PROBAR |

## Plan de Pruebas con el Cliente

### 1. Configuración

* **Reunión Inicial**: Programar una reunión de inicio con el cliente para explicar el proceso de pruebas y los objetivos.
* **Acceso y Permisos**: Asegurarse de que el cliente tenga todo el acceso necesario a DocBits y a Infor LN o M3 para fines de prueba.

### 2. Preparación de Pruebas

* **Capacitación**: Proporcionar capacitación integral al equipo del cliente sobre cómo usar DocBits para el procesamiento de facturas.
* **Documentación**: Compartir documentación detallada sobre los procedimientos de prueba, incluidos los resultados esperados para cada caso de prueba.

### 3. Ejecución de Casos de Prueba

* **Entorno de Pruebas**: Configurar un entorno de pruebas que replique el sistema de producción del cliente lo más cerca posible.
* **Pruebas Paso a Paso**: Trabajar con el cliente para ejecutar cada caso de prueba, asegurándose de que comprendan cada paso:
  * Procesar facturas a través de DocBits.
  * Verificar la salida en el módulo de coincidencia de OC.
  * Comprobar los resultados de exportación en LN o M3.

### 4. Resolución de Problemas

* **Seguimiento**: Utilizar un sistema de seguimiento (como Jira o una hoja de cálculo simple) para registrar cualquier problema o desajuste que ocurra durante las pruebas.
* **Soporte**: Proporcionar soporte inmediato para resolver problemas y aclarar cualquier duda.

### 5. Verificación y Retroalimentación

* **Verificación**: Después de cada caso de prueba, verificar los resultados con el cliente para asegurar la precisión.
* **Ciclo de Retroalimentación**: Recoger retroalimentación del cliente sobre el proceso y cualquier mejora necesaria.

### 6. Finalización

* **Documentación de Resultados**: Documentar los resultados de cada caso de prueba y proporcionar un informe resumen al cliente.
* **Reunión de Revisión**: Realizar una reunión de revisión para discutir los resultados de las pruebas y cualquier paso adicional requerido antes de la implementación.

### 7. Preparación para el Go Live

* **Refresco de Capacitación**: Ofrecer una sesión de capacitación de repaso si es necesario.
* **Plan de Soporte**: Desarrollar un plan de soporte para la fase inicial de implementación para asegurar una transición fluida.
