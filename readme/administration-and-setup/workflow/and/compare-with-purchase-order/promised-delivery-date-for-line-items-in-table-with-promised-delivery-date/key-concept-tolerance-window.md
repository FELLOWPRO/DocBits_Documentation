# Key Concept: Tolerance Window

Antes de examinar los operadores, es importante comprender cómo se calcula la ventana de tolerancia.

## ¿Qué es una ventana de tolerancia?

La ventana de tolerancia define un rango de fechas aceptables en torno a la fecha de entrega prometida de la orden de compra.

**Ejemplo:**

* Fecha de la orden de compra: **9 de enero**
* Tolerance Days: **3**
* Ventana de tolerancia: **6 de enero → 12 de enero**

> <mark style="color:red;">Solo los</mark> <mark style="color:red;"></mark><mark style="color:red;">**Allowed Tolerance Days**</mark> <mark style="color:red;"></mark><mark style="color:red;">seleccionados (días de la semana) se cuentan al calcular esta ventana.</mark>

### Ejemplo de línea de tiempo visual

```
← Past                           Future →
|-----|-----|-----|-----|-----|-----|-----|
     6 Jan      9 Jan      12 Jan
   (Start)    (PO Date)     (End)
```

### Comportamiento de los operadores explicado con ejemplos

* **Equals (=)**
  * **Significado:**\
    La fecha de entrega de la línea debe quedar _dentro_ de la ventana de tolerancia.
  * **Fechas válidas:**
    * Cualquier fecha entre el **6 de enero y el 12 de enero** (ambas incluidas)
  * **Fechas no válidas:**
    * Cualquier fecha **anterior al 6 de enero**
    * Cualquier fecha **posterior al 12 de enero**
* **Not Equals (≠)**
  * **Significado:**\
    La fecha de entrega de la línea debe quedar _fuera_ de la ventana de tolerancia.
  * **Fechas válidas:**
    * Cualquier fecha **anterior al 6 de enero**
    * Cualquier fecha **posterior al 12 de enero**
  * **Fechas no válidas:**
    * Fechas entre el **6 de enero y el 12 de enero**
* **Greater or Equals (≥)**
  * **Significado:**\
    La fecha de entrega de la línea debe ser igual o posterior al **inicio de la ventana de tolerancia**.
  * **Fechas válidas:**
    * **6 de enero → cualquier fecha futura**
  * **Fechas no válidas:**
    * Cualquier fecha **anterior al 6 de enero**
  * <mark style="color:red;">**Importante:**</mark>\
    Este operador permite fechas _dentro_ de la ventana de tolerancia **y más allá de ella**.
* **Lesser or Equals (≤)**
  * **Significado:**\
    La fecha de entrega de la línea debe ser igual o anterior al **final de la ventana de tolerancia**.
  * **Fechas válidas:**
    * Cualquier fecha pasada hasta el **12 de enero**
  * **Fechas no válidas:**
    * Cualquier fecha **posterior al 12 de enero**
* **Greater Than (>)**
  * **Significado:**\
    La fecha de entrega de la línea debe ser _estrictamente posterior_ a la ventana de tolerancia.
  * **Fechas válidas:**
    * **13 de enero → cualquier fecha futura**
  * **Fechas no válidas:**
    * Cualquier fecha **igual o anterior al 12 de enero**
* **Lesser Than (<)**
  * **Significado:**\
    La fecha de entrega de la línea debe ser _estrictamente anterior_ a la ventana de tolerancia.
  * **Fechas válidas:**
    * Cualquier fecha **anterior al 6 de enero**
  * **Fechas no válidas:**
    * Cualquier fecha **igual o posterior al 6 de enero**

## Cómo afectan los "Allowed Tolerance Days" a la ventana de tolerancia

Al calcular la ventana de tolerancia, **solo se cuentan los días de la semana seleccionados**.\
Los días que no están seleccionados (como los fines de semana o los días de la semana excluidos) se **omiten por completo**.

#### Ejemplo: cálculo de tolerancia basado en días de la semana

**Configuración:**

* Fecha de la orden de compra: **miércoles, 9 de enero**
* Tolerance Days: **3**
* Allowed Tolerance Days: **lunes, martes, miércoles, jueves, viernes**
* Fines de semana (sábado, domingo): **No seleccionados**

#### Cálculo paso a paso

Partiendo de la fecha de la orden de compra (**9 de enero**):

**Contando hacia atrás (3 días de tolerancia):**

* Martes, 8 de enero → **Día 1**
* Lunes, 7 de enero → **Día 2**
* Domingo, 6 de enero → _Omitido (no permitido)_
* Sábado, 5 de enero → _Omitido (no permitido)_
* Viernes, 4 de enero → **Día 3**

➡ **Fecha de inicio de la tolerancia: viernes, 4 de enero**

**Contando hacia delante (3 días de tolerancia):**

* Jueves, 10 de enero → **Día 1**
* Viernes, 11 de enero → **Día 2**
* Sábado, 12 de enero → _Omitido_
* Domingo, 13 de enero → _Omitido_
* Lunes, 14 de enero → **Día 3**

➡ **Fecha de fin de la tolerancia: lunes, 14 de enero**

#### Ventana de tolerancia resultante

```
4 January  →  14 January
```

#### Por qué es importante

Si los Allowed Tolerance Days se configuran incorrectamente:

* Las fechas de entrega pueden parecer **válidas o no válidas de forma inesperada**
* Es posible que las entregas tempranas o tardías no se detecten correctamente
