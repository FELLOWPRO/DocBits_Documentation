# Configuración Avanzada

En algunos documentos, las estructuras de tabla pueden ser complejas, abarcando múltiples líneas, conteniendo información agrupada o incluyendo filas adicionales innecesarias. Los _Ajustes Avanzados_ en modo de entrenamiento te permiten ajustar la extracción de tablas para estos casos, mejorando la precisión y consistencia.

Para acceder a estos ajustes, activa el **Modo de Entrenamiento** y haz clic en el ícono de engranaje **Configuración** en la barra de acciones superior:

![Vista de Document training con los interruptores Tables, Rules y Training Mode en la barra de acciones superior](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FW1cBx4IOjycKv6IZM9AX8Wggj1eEBgzBVJWgsyWkutX9dRRJuEjQtSCsPaNZuRndd9ewMVvfqSXr45C-2cO-pxXkYFdl_9eEGVW6-UBqqZCsuhia6alJjD1ZuZawwSbjS9Yeywe1wDK5yAcIOUH5QAw\&width=768\&dpr=4\&quality=100\&sign=4bf6ac31\&sv=2)

## Cantidad de Filas de Encabezado

**Utiliza esta configuración para definir cuántas líneas componen el encabezado de la tabla.**

Algunas tablas tienen encabezados de varias líneas. Por ejemplo, el encabezado de esta tabla abarca dos líneas:

![Encabezado de tabla de documento que abarca las columnas número de pieza, precio unitario, importe neto, porcentaje de IVA, cantidad y descripción del producto](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FJ_nYZKzUSJHcpJuNp1ykf6shnfetOuiIPhyhyTfSqh_cTsDT5obwOSIc21OsLkjF9tMBP7Q1GQ1ZQfBsEmQIrJpfX3QpdjHnLkzInsjpngeg2L7i_TAyl9MdVmgHsDpUvoURdxfqp8FOdJxuRAMCwhk\&width=768\&dpr=4\&quality=100\&sign=554fa70\&sv=2)

Ajusta la **Cantidad de filas de encabezado** para que coincida:

![Diálogo de Advanced settings con el campo header row count y la selección de description para move extra rows to](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FG8-QpKxnRin9PGPmkbtJ35r1EugXsD4_Yd5QvTkdbb7sXqRVC3a9t0cIlNILJHLr--GsykgAlMJmMYbJaUoMqHEPvAT3PlPNf-syCmPz_GVMFEMsbhcHI2DQBbT4MJXjS2Sx7M3xl4zAzcw3aa-XNms\&width=768\&dpr=4\&quality=100\&sign=a487f5a9\&sv=2)

### ¿Por qué es importante?

Si no configuras esto, DocBits puede tratar la segunda línea como datos en lugar de parte del encabezado, lo que lleva a errores de extracción:

**Antes:**

![Listas desplegables de selección de columnas para el porcentaje de descuento y total amount con la asignación de unit price en EUR](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F35BElgcq-zbs8wcGcguVSKHRpwQXqQG9dQmBaYa8BT4RNwJxd6g-jL5wlQgrnVLrMxtpncr8ayaasWVV3snGpBiDUWs4Zx7Tn2Dck-YFBpanlcN500yIWkVz9RJXQhoq6op0WbYcgklp_LsmE9LXt9k\&width=768\&dpr=4\&quality=100\&sign=7c68faf7\&sv=2)

Después:

![Desplegables de columnas con asignación a unit price y total amount con valores de price in EUR antes de corregir el encabezado](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FbPGn9eWPK3Mmbu_ab2N3tVVP8ODho4MW6r6ynSKJWiPxq-IPlP_0Q1ghfcwjN56Sp_HA0nV-fedAfzkZoAXsj5O5ata32PCXPHJQ-dizWZ1OdpdEPS5wSPNW9jjc7TSPKQiNnCGPjLtnXQDLCbwEj3U\&width=768\&dpr=4\&quality=100\&sign=b032f2da\&sv=2)

## Mover Filas Adicionales a la Papelera

**Utiliza esto para descartar entradas de varias líneas no deseadas, como descripciones que desbordan.**

En este ejemplo, la descripción se extiende a múltiples filas, pero solo la primera línea es relevante:

![Tabla de factura con la descripción que desborda en varias líneas junto a las columnas unit price, rabatt percent y total en EUR](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FAEFanKF7uUtS_78nxi5zESPW8WOESa0Do_sCQCsttC21KoFK-sB9TQgFHboJB7CMEpc_auEbeXINU4BpEh8XuNMBHDYhuwjVX40cRyygxECs3XogrurWKNdw4s4F1kxWXLGrrF4jSqd1bba0dKPVO2E\&width=768\&dpr=4\&quality=100\&sign=926d60ed\&sv=2)

Habilita **Mover Filas Adicionales a la Papelera** para eliminar el exceso:

![Menú Settings que muestra las opciones header row count y move extra rows to trash en el entrenamiento de tablas](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FQdYUZ0ANpuFRkvNxVZzYfEhTRVf2fk1jPmoNUZcNotdkgL6VDHV1BgBXU2xqFfjBJ7W6uvB8TRZcpKEk7Qk_c0mIohiS4Jl9ZPRpG7HdS_EktuCcAtJ4KjJ_vYvYok7lv0nz2MfVMG08oDFqRSyFHy4\&width=768\&dpr=4\&quality=100\&sign=135061e3\&sv=2)

**Resultado después de mapear:**

![Resultado de tabla de factura mapeada con las columnas posición, descripción, impuesto, unit price y total en EUR y valores de subtotal](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2Fzto-P_Knp1YQmCUBU6_vCg2IEwaBiBeAao8Jvu30-89x_Sj2BLDSTQu31vUNBlaQp73DPVy2F-UZawn8j4hxycD6bpfCf_KXZYvrqH5w0cwGwsjatBelIh6gdenY-NpzmQ372jtthucHpMrsXNz3DcA\&width=768\&dpr=4\&quality=100\&sign=741cbfd1\&sv=2)

## Mínimo de Filas Agrupadas

**Utiliza esto cuando las filas necesitan agruparse bajo una fila principal (por ejemplo, elementos de línea con múltiples sublíneas).**

Aquí, solo tres de seis filas son relevantes. Dos columnas clave están mapeadas (por ejemplo, Posición, Descripción), mientras que otras se tratan como campos personalizados.

Comienza configurando la **Cantidad de filas de encabezado** y el **Mínimo de filas agrupadas**:

![Diálogo de Advanced settings con las opciones header row count, move extra rows to, minimum and maximum grouped rows y split text](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2Fp0k-n1IG3_FHexG4iAlISSmN4Yaq9xUjRO2cLpV3w6a67DpULRnxj4x291DOXBVx2SHqKp6Zs-ZXxr8KHKzT9O6oCwgEOkvfMqwpDGZUrfFpozdR16sbaybtrMEqDOXO1TsNmuPFz6mOKX0pR8I5RO8\&width=768\&dpr=4\&quality=100\&sign=e19a8ef6\&sv=2)

También habilita **Mover Filas Adicionales a la Papelera** para limpiar datos irrelevantes.

Luego define la columna clave de agrupamiento, por ejemplo, _Posición_:

![Vista de Table training con filas de líneas de factura agrupadas que muestran Pos. No, número de pieza, descripción, precio unitario y totales](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F5hy2YTNQRZ6plQZnc1HwAbAUXU7LKfNpLdlfr8sPnDXMryv0KoAGgkcqAWqjvznvBa1YwW0ecTrpStpm5AIc0qiFX1zB-I_y_crIx0jKS2t6QVKdAz66Wb3XMt9sRsEUHKIuk51_AatHNCRZjOghn4A\&width=768\&dpr=4\&quality=100\&sign=6ca2a12e\&sv=2)

**Resultado:**

![Tabla de documento entrenada con columna de clave de agrupación de posiciones, leyenda de columnas mapeadas y extraíbles y totales](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FxaorEjiOEeypLMAAOXvm3VAc5BVzhIujUeLdSt0SPwrEz5x_hd8sb3Hhc7OpnUpzj6qvjWWptOsefhxjF5pIzf12RVXah1wPhlMoa3Wwx7T3s_D7Pzw8cryaAzgh8SpN-uTxpl1FWke8v33dh2VNgJ0\&width=768\&dpr=4\&quality=100\&sign=e955b28f\&sv=2)

## Agrupamiento Inverso

**Utiliza esto cuando la fila de agrupamiento aparece** _**después**_ **de las filas que debería agrupar.**

Si la fila que debería agruparse con otros datos aparece _encima_ de la clave de agrupamiento, habilita esta opción:

![Tabla con las columnas Pos. No., Qty., Cat.No., descripción del material, unit price y total que muestra las líneas agrupadas del conjunto de plátanos](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FiH7rDa637FWtr8wWtXpdqSh68xsaOFrb_vIWf-ZOpAjExmFPHVRaDGGipdwNy30gpLmEWT0UujjqlbcSlHU7ldQ5zhAy15pMxuqbDpS2xFSuL35EjbaXfFQTOSSO3QE_I37kvdL3i5k-N7F_9tedMss\&width=768\&dpr=4\&quality=100\&sign=95d583b1\&sv=2)

Habilita **Agrupamiento Inverso**, agrupa por una columna principal (por ejemplo, Monto neto) y utiliza **Mover Filas Adicionales a la Papelera** si es necesario:

![Diálogo de Advanced settings con header row count dos, minimum grouped rows y la opción reverse grouping activada](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FFJNKYXmELlMFi-Zh_0Pjgc0pcKI2-_UbDhF7b4D5p7GA4f9r-FqjruzkJw3nfJH4NA0G_BC2xQpJEzl26GbOlPt9fPyOkGowtGWgRWt5GJ62Vj-Qd04rDP0kzDFiJnRlpWF13d9YQ1e-FurQI-gHJx4\&width=768\&dpr=4\&quality=100\&sign=4b2677ae\&sv=2)

**Resultado final:**

![Resultado de Table training que muestra filas de líneas agrupadas de un conjunto de plátanos con precios unitarios, IVA y totales de descuento por pronto pago](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2Fe8x8gIUV10Y_FmPeW_X-UZw6uJ8P7alQTDy_m5OGGLZ8Ev7Ip-C-6fqtTixiSU0ZnLMIc4VR_f0xJV6beDnl7bFBIh4U2dME8KHB3qokj__SrQGp-3BXeOsN63SabFNd5miRCtK-jlf49nzcbbe8UJw\&width=768\&dpr=4\&quality=100\&sign=f7571dde\&sv=2)

## Resumen

Utiliza la _Configuración Avanzada_ para enseñar a DocBits cómo manejar con precisión estructuras de tabla más complejas o inconsistentes. Estos ajustes mejoran la precisión de la extracción al tener en cuenta:

* Encabezados de varias líneas
* Descripciones de varias filas
* Elementos de línea agrupados
* Orden inverso de datos agrupados

Habilitar estas opciones durante el entrenamiento asegura que DocBits recuerde el diseño correcto para futuros documentos del mismo proveedor.
