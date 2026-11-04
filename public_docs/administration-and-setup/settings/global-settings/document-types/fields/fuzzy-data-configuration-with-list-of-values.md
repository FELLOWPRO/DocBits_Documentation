---
hidden: true
---

# Configuración de Datos Difusos con Lista de Valores

### **Descripción general**

Cada tipo de documento tiene sus propias configuraciones de Lista de Valores (LoV), que deben configurarse por separado. A diferencia de los **Datos Difusos con Datos Maestros**, la **Lista de Valores** no viene con grupos de búsqueda predeterminados.

### Para configurar la Lista de Valores, navegue a:

Configuración → Configuración Global → Tipos de Documento → Factura → Campos → Configuración de Datos Maestros → Datos Maestros LOV

### **Crear una nueva configuración de Lista de Valores**

Hay dos formas de crear una configuración de Lista de Valores:

**1. Duplicar una búsqueda existente**

* Esto copia toda la información y los campos de un grupo existente.
* Solo necesita proporcionar un **nuevo nombre**.

**2. Crear una búsqueda desde cero**

* Haga clic en **"Crear Lista de Valores"**.
* Complete los detalles requeridos:
  * **Nombre de la configuración** → Nombre de la Lista de Valores.
  * **Tabla de búsqueda** → La tabla de la cual se recuperarán los valores.
  * **Gestor de conflictos** → Elija uno:
    * Mejor puntuación
    * No devolver ninguno
    * Devolver el primero
  * **Tipo de contexto** → Determina si la LoV se aplica al nivel de **Encabezado** o **Línea**.
  * **Coincidir todo** → _(Se necesitan más detalles)_

### **Gestión de campos dentro de un grupo de Lista de Valores**

Cada grupo LoV contiene campos que se pueden **añadir, eliminar o editar.**

**Añadir un nuevo campo**

Para añadir un nuevo campo dentro de un grupo:

* Haga clic en **"Crear"** dentro del grupo relevante.
* Proporcione los siguientes detalles:
  * **Campo de búsqueda** → El nombre de la columna de la tabla de búsqueda.
  * **Campo de validación** → El campo de DocBits correspondiente.
  * **Campo padre** → _(Se necesitan más detalles)_
  * **Operador de búsqueda** → Elija uno:
    * Inteligente
    * Contiene
    * Exacto
    * Comienza con
    * Termina con
  * **Casillas de verificación:**
    * **Disparo automático** → Cuando está habilitado, si otro campo en una configuración de búsqueda diferente comparte la misma columna, este campo se actualizará **automáticamente** cada vez que se actualice el otro campo.
    * **Buscable** → Habilita el campo como un campo de **Lista de Valores**, permitiendo búsquedas en la tabla de búsqueda.

#### **Paso final: Añadir campos al diseño**

Después de configurar los campos de la Lista de Valores, **asegúrese de añadirlos al diseño utilizando el Constructor de Diseños**. Si los campos no se añaden al diseño, no estarán disponibles para su uso.
