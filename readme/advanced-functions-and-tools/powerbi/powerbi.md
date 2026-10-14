---
description: Cómo configurar PowerBI
---

# Conectar a través de ClickHouse

Esta guía le explica cómo conectar **ClickHouse** a **Power BI Desktop** mediante el **controlador ODBC**. Abarca la instalación del controlador, la configuración de ODBC, la integración con Power BI y la configuración de la actualización de datos.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}

#### 1. Instalar el controlador ODBC de ClickHouse

* Descargue la última versión del **controlador ODBC de ClickHouse** desde:
  * [ClickHouse GitHub - clickhouse-odbc](https://github.com/ClickHouse/clickhouse-odbc)
* Ejecute el instalador y siga el asistente de configuración.

#### 2. Configurar el origen de datos ODBC

* Abra el **Administrador de orígenes de datos ODBC (64 bits)** desde el Panel de control o la búsqueda de Windows.
* Vaya a la pestaña **DSN de sistema** y haga clic en **Agregar**.
* Seleccione **ClickHouse ODBC Driver** en la lista y haga clic en **Finalizar**.
*   Rellene los campos obligatorios. Encontrará la información necesaria en:

    **DocBits**
