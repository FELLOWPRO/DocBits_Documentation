# Descuentos

## **Descripción general**

Si su tabla extraída contiene la columna **Descuento** o **Porcentaje de descuento**, **DocBits** aplicará automáticamente el descuento correspondiente al Precio unitario durante el procesamiento en la [**pantalla de coincidencia de órdenes de compra**](./).

## Excepciones

Los descuentos no se aplicarán automáticamente cuando se utilice la función de coincidencias múltiples. Más información sobre la función de coincidencias múltiples se puede encontrar [aquí](./#coincidencias-multiples).

## Cálculo del Descuento

Cuando hay un **Descuento** presente, el precio unitario descontado se calcula restando el monto del descuento del precio unitario:

```
UNIT_PRICE_DISCOUNTED = UNIT_PRICE - DISCOUNT
```

## Cálculo del Porcentaje de Descuento

Cuando hay un **Porcentaje de descuento** presente, el precio unitario descontado se calcula utilizando la siguiente fórmula:

```
UNIT_PRICE_DISCOUNTED = UNIT_PRICE * (1 - DISCOUNT_PERCENT / 100)
```

## Redondeo

Todos los resultados del precio unitario descontado se redondean a cuatro decimales para mantener la consistencia en el procesamiento posterior.
