# Establecer signo negativo para notas de crédito

### Descripción general

La opción **Establecer signo negativo para notas de crédito** (Set Negative Sign for Credit Notes) garantiza que las **notas de crédito** se almacenen con **importes negativos**. Una nota de crédito revierte o reembolsa parte de una factura, por lo que en contabilidad sus valores deben reducir los totales, es decir, ser negativos. Cuando esta opción está activada, DocBits aplica ese signo negativo automáticamente.

Esta opción está **activada de forma predeterminada**.

### ¿Qué hace?

Cuando un documento se reconoce como **nota de crédito**, DocBits convierte automáticamente sus importes en valores negativos durante el procesamiento. Esto afecta a los campos monetarios, incluidos los importes netos, los importes de impuestos y los totales (por ejemplo, importe neto, importe de impuestos, importe total de impuestos, importe neto total e importe total).

* **Activada (predeterminado)** — Los importes de las notas de crédito se guardan como valores negativos (por ejemplo, `150,00` se convierte en `-150,00`). Las facturas normales no se ven afectadas.
* **Desactivada** — Los importes se mantienen exactamente como se leyeron del documento, sin cambio de signo.

{% hint style="info" %}
Esto solo se aplica a los documentos identificados como **notas de crédito**. Las facturas normales siempre se dejan sin cambios.
{% endhint %}

### Beneficios

* **Contabilidad correcta**: Las notas de crédito reducen los saldos, por lo que los valores negativos son lo que esperan sus sistemas contables y ERP.
* **Sin edición manual**: Su equipo no tiene que cambiar el signo a mano en cada nota de crédito.
* **Coherencia**: Cada nota de crédito se trata de la misma manera en toda su organización.

### Cómo usarla

1. Vaya a **Configuración**.
2. Seleccione **Procesamiento de documentos**.
3. Seleccione **Módulo**.
4. Abra la sección **Tipo de documento**.
5. Busque **Establecer signo negativo para notas de crédito** y active o desactive el interruptor.

### Cuándo usar esta función

* **Manténgala activada** si su sistema contable o ERP espera que las notas de crédito lleguen con importes negativos (esta es la configuración más habitual).
* **Desactívela** solo si su sistema posterior ya gestiona el signo por sí mismo o espera que los importes de las notas de crédito sigan siendo positivos.
