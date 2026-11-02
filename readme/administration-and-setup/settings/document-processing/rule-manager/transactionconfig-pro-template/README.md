# TransactionConfig Pro Template

## Configuración del procesamiento de documentos financieros

_TransactionConfig Pro Template_ documenta ejemplos de asignación para facturas, notas de débito y notas de crédito. El gestor de reglas puede utilizar reglas y expresiones `conflict_resolution` configuradas para determinar las acciones de procesamiento. Esta documentación no acredita que exista una plantilla predefinida desplegada en su entorno.

Las asignaciones de campos, los tipos de transacción y las decisiones del flujo deben configurarse para la integración Infor M3/LN correspondiente. Los ejemplos explican esa configuración; no garantizan resultados exactos, una integración sin ajustes ni el cumplimiento de normas financieras internacionales.

### Áreas de configuración

* **Asignación:** Defina los campos de origen y destino de cada tipo de transacción y verifique los datos resultantes.
* **Personalización:** Configure las reglas del flujo de negocio y del proceso de aprobación.
* **Automatización:** Automatice únicamente las decisiones cubiertas expresamente por las reglas y expresiones activas.
* **Integración:** Compruebe la asignación de exportación y los requisitos del sistema Infor M3/LN de destino.
* **Cumplimiento:** Revise por separado los requisitos contables y fiscales; la configuración no garantiza por sí sola el cumplimiento legal.

## Casos ilustrativos de resolución de conflictos

El siguiente escenario es un ejemplo de asignación configurada, no una plantilla predeterminada cuyo despliegue se haya verificado. La salida real, los importes, los signos y los tipos de documento dependen de las reglas y expresiones `conflict_resolution` activas, de la asignación de exportación y de las decisiones de aprobación. Cualquier nota de débito o crédito descrita está condicionada a esa configuración; el ejemplo no garantiza su emisión automática ni el cumplimiento legal.

### [Casos 1, 2 y 3: Cantidad y precio unitario dentro de tolerancia](case-1-2-3-quantity-and-unit-price-within-tolerance.md)

**Escenario:** La cantidad y el precio de la factura están dentro de las tolerancias configuradas respecto al PO.

**Acción ilustrativa:** La asignación ilustrativa acepta los valores facturados y calcula cantidad × precio unitario.

### [Casos 4 y 5: Cantidad dentro y precio fuera de tolerancia (aprobado)](case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved.md)

**Escenario:** La cantidad está dentro de tolerancia; la desviación del precio está fuera y se ha aprobado.

**Acción ilustrativa:** La asignación ilustrativa utiliza el precio del PO y asigna la diferencia aprobada como cargo de línea si así se ha configurado.

### [Caso 6: Cantidad dentro y precio por debajo de tolerancia (rechazado)](case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md)

**Escenario:** La cantidad está dentro de tolerancia; el precio está por debajo del intervalo permitido y se ha rechazado.

**Acción ilustrativa:** La asignación ilustrativa utiliza el precio del PO. La diferencia con signo no es automáticamente una nota de crédito; el tipo y el signo del ajuste dependen de la asignación.

### [Caso 7: Cantidad dentro y precio por encima de tolerancia (rechazado)](case-7-quantity-within-tolerance-unit-price-outside-tolerance-positive-rejected.md)

**Escenario:** La cantidad está dentro de tolerancia; la desviación positiva del precio se ha rechazado.

**Acción ilustrativa:** La asignación ilustrativa utiliza el precio del PO. Cualquier nota o ajuste por la diferencia depende de la asignación de exportación.

### [Casos 8a y 9a: Cantidad fuera de tolerancia (aprobada), precio dentro](case-8a-9a-quantity-outside-tolerance-approved-unit-price-within-tolerance.md)

**Escenario:** La desviación de cantidad está aprobada y el precio sigue dentro de tolerancia.

**Acción ilustrativa:** La asignación ilustrativa utiliza la cantidad facturada aprobada y el precio unitario de la factura.

### [Caso 11a: Cantidad superior a tolerancia (rechazada), precio dentro](case-11a-quantity-outside-tolerance-positive-rejected-unit-price-within-tolerance.md)

**Escenario:** La cantidad supera la tolerancia y se ha rechazado; el precio está dentro.

**Acción ilustrativa:** La asignación ilustrativa utiliza la cantidad aprobada y conserva el precio. El tratamiento del exceso depende de las reglas configuradas.

### [Caso 10a: Cantidad inferior a tolerancia (rechazada), precio dentro](case-10a-quantity-outside-tolerance-negative-rejected-unit-price-within-tolerance.md)

**Escenario:** La cantidad está por debajo de tolerancia y se ha rechazado; el precio está dentro.

**Acción ilustrativa:** La asignación ilustrativa utiliza la cantidad aprobada y conserva el precio unitario.

### [Casos 8b y 9b: Cantidad y precio fuera de tolerancia (aprobados)](case-8b-9b-quantity-outside-tolerance-approved-unit-price-outside-tolerance-approved.md)

**Escenario:** Las desviaciones de cantidad y precio están aprobadas.

**Acción ilustrativa:** La asignación ilustrativa utiliza los valores facturados aprobados y los cargos o ajustes de línea expresamente configurados.

### [Caso 10b: Cantidad inferior y precio fuera de tolerancia (rechazados)](case-10b-quantity-outside-tolerance-negative-rejected-unit-price-outside-tolerance-rejected.md)

**Escenario:** No se ha aprobado ni la desviación negativa de cantidad ni la del precio.

**Acción ilustrativa:** La asignación ilustrativa utiliza los valores del PO o los aprobados. Las notas de débito o crédito requieren la asignación y la aprobación correspondientes.

### [Caso 11b: Cantidad superior y precio fuera de tolerancia (rechazados)](case-11b-quantity-outside-tolerance-positive-rejected-unit-price-outside-tolerance-rejected.md)

**Escenario:** Se han rechazado la desviación positiva de cantidad y la del precio.

**Acción ilustrativa:** La asignación ilustrativa utiliza los valores aprobados del PO; el tratamiento de excesos depende de la configuración activa.

### [Casos 12 y 13: Cargo de línea por unidad dentro de tolerancia](charge-per-unit-within-tolerance.md)

**Escenario:** El cargo de línea por unidad está dentro de la tolerancia configurada respecto al PO.

**Acción ilustrativa:** La asignación ilustrativa acepta el cargo de línea facturado sin ajuste.

### [Caso 14: Cargo de línea por unidad fuera de tolerancia (aprobado)](charge-per-unit-outside-tolerance-approved-1.md)

**Escenario:** El cargo de línea por unidad está fuera de tolerancia y se ha aprobado.

**Acción ilustrativa:** La asignación ilustrativa aplica el cargo de línea aprobado.

### [Caso 15: Cargo de línea por unidad fuera de tolerancia (rechazado)](charge-per-unit-outside-tolerance-rejected.md)

**Escenario:** El cargo de línea por unidad está fuera de tolerancia y se ha rechazado.

**Acción ilustrativa:** La asignación ilustrativa utiliza el cargo de línea del PO o el aprobado. Cualquier nota por la diferencia depende de la asignación de exportación.

### [Casos 12 y 13: Cargo de cabecera por unidad dentro de tolerancia](case-12-13-header-charge-charge-per-unit-within-tolerance.md)

**Escenario:** El cargo de cabecera por unidad está dentro de la tolerancia configurada respecto al PO.

**Acción ilustrativa:** La asignación ilustrativa aplica el cargo de cabecera facturado sin ajuste.

### [Caso 14: Cargo de cabecera por unidad fuera de tolerancia (aprobado)](charge-per-unit-outside-tolerance-approved.md)

**Escenario:** El cargo de cabecera por unidad está fuera de tolerancia y se ha aprobado.

**Acción ilustrativa:** La asignación ilustrativa aplica el cargo de cabecera aprobado.

### [Caso 15: Cargo de cabecera por unidad fuera de tolerancia (rechazado)](case-15-header-charge-charge-per-unit-outside-tolerance-rejected.md)

**Escenario:** El cargo de cabecera por unidad está fuera de tolerancia y se ha rechazado.

**Acción ilustrativa:** La asignación ilustrativa utiliza el cargo de cabecera del PO o el aprobado. Cualquier nota separada depende del tratamiento configurado.

### [Líneas de impuestos](tax-lines.md "mention")

**Escenario:** Los importes de impuestos de la factura y del PO difieren.

**Acción ilustrativa:** La asignación ilustrativa utiliza tipos e importes impositivos aprobados. Debe comprobarse frente a los requisitos fiscales aplicables; el ejemplo no garantiza el cumplimiento legal.
