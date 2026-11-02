# Ajuste de tolerancias de órdenes de compra / Tolerancia adicional de órdenes de compra

## Configurar reglas de conciliación y tolerancias

El recorrido abre el tipo de documento factura, comprueba la versión publicada y crea un borrador inactivo. Explica los tipos de regla, la prioridad dentro de la etapa de coincidencia, las columnas comparadas, la base de cantidad, los modos y los cálculos de tolerancia. Solo se guarda el borrador del tutorial; la versión activa y las tolerancias globales se conservan. El cálculo del cinco por ciento es ilustrativo y no cambia la tolerancia activa.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/po-matching-rules-admin/v3/es.mp4" %}

[Ver el vídeo con subtítulos](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/po-matching-rules-admin/v3/es.html)

## **Ajuste para configurar las tolerancias de órdenes de compra**&#x20;

Vaya a **Configuración → Configuración general → Tipos de documento → More Settings → Sección Purchase Order → PO Tolerance Setting**

### **Cómo funciona**

Cuando está habilitado, este ajuste permite definir tolerancias para la **Cantidad** y/o el **Precio unitario**. Estas tolerancias pueden establecerse como un porcentaje o como un valor fijo. Esto significa que una factura puede desviarse de la orden de compra (OC) dentro del rango de tolerancia especificado sin ser marcada como una discrepancia, lo que proporciona flexibilidad y garantiza un procesamiento fluido.

<mark style="color:red;">**NOTA**</mark>**:** Las tolerancias funcionan en ambas direcciones; es decir, el valor de la factura puede ser mayor o menor que el valor de la OC dentro del rango permitido.

### **Configuración**

1. **Habilite el ajuste:**
   * Active PO Tolerance Setting con el botón de alternancia.
2. **Configure las tolerancias:**
   * Aparecerán cuatro campos:
     * Un campo para el **importe de tolerancia de cantidad**.
     * Un campo para el **importe de tolerancia de precio unitario**.
   * Detrás de cada campo hay un menú desplegable donde puede seleccionar el tipo de tolerancia:
     * **Percent:** Indica una tolerancia porcentual.
     * **Value:** Indica un importe fijo en el que puede diferir el valor.

<figure><img src="../../../../../../.gitbook/assets/image (394).png" alt=""><figcaption></figcaption></figure>

### **Escenario de ejemplo:**

* Supongamos que la **tolerancia de precio unitario** está establecida en **5 %**.
* La orden de compra incluye dos líneas:
  * **Línea 1:** Precio unitario = **$5.00**
  * **Línea 2:** Precio unitario = **$2.00**
* En la factura:
  * **Línea 1:** El precio unitario se ajusta a **$4.80** (**dentro** de la tolerancia del 5 %).
  * **Línea 2:** El precio unitario se ajusta a **$2.20** (**fuera** de la tolerancia del 5 %).
* **Resultado:**
  * La línea 1 **no se marca** como discrepancia porque $4.80 está dentro del 5 % de $5.00.
  * La línea 2 **se marca** como discrepancia porque $2.20 supera la desviación permitida del 5 % respecto a $2.00. Ahora el usuario debe actuar para resolver la discrepancia antes de que la factura pueda seguir procesándose.

<figure><img src="../../../../../../.gitbook/assets/image (395).png" alt=""><figcaption></figcaption></figure>

## Ajuste para configurar la tolerancia adicional de órdenes de compra

Vaya a **Configuración → Configuración general → Tipos de documento → More Settings → Sección Purchase Order → Additional PO Tolerance Setting**

### **Cómo funciona**

Cuando está habilitado, este ajuste permite definir tolerancias para el **Flete**, los **Cargos** y/o el **Impuesto**. Estas tolerancias pueden establecerse como un porcentaje o como un valor fijo, lo que permite que las facturas varíen ligeramente respecto a los valores de la OC sin ser marcadas como discrepancias. Esto proporciona flexibilidad adicional y garantiza que las diferencias menores no interrumpan el flujo de trabajo.

<mark style="color:red;">**NOTA**</mark>**:** Al igual que los ajustes de tolerancia estándar, estas tolerancias se aplican en ambas direcciones, permitiendo aumentos o disminuciones dentro de los límites establecidos.

### **Configuración**

1. **Habilite el ajuste:**
   * Active Additional PO Tolerance Setting con el botón de alternancia.
2. **Configure las tolerancias:**
   * Se mostrarán seis campos:
     * Un campo para cada uno de los importes de tolerancia de **Flete**, **Cargos** e **Impuesto**.
   * Cada campo tiene un menú desplegable donde puede elegir el tipo de tolerancia:
     * **Percent:** La tolerancia se define como un porcentaje.
     * **Value:** La tolerancia se define como un importe fijo.

<figure><img src="../../../../../../.gitbook/assets/image (396).png" alt=""><figcaption></figcaption></figure>
