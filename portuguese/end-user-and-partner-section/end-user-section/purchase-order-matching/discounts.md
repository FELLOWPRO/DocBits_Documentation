# Descontos

## **Visão Geral**

Se sua tabela extraída contiver a coluna **Desconto** ou **Porcentagem de desconto**, **DocBits** aplicará automaticamente o desconto correspondente ao Preço unitário durante o processamento na [**tela de correspondência de ordem de compra**](./).

## Exceções

Os descontos não serão aplicados automaticamente quando o recurso de correspondências múltiplas for utilizado. Mais informações sobre o recurso de correspondências múltiplas podem ser encontradas [aqui](./#correspondencias-multiplas).

## Cálculo de Desconto

Quando um **Desconto** está presente, o preço unitário com desconto é calculado subtraindo o valor do desconto do preço unitário:

```
UNIT_PRICE_DISCOUNTED = UNIT_PRICE - DISCOUNT
```

## Cálculo de Porcentagem de Desconto

Quando uma **Porcentagem de desconto** está presente, o preço unitário com desconto é calculado usando a seguinte fórmula:

```
UNIT_PRICE_DISCOUNTED = UNIT_PRICE * (1 - DISCOUNT_PERCENT / 100)
```

## Arredondamento

Todos os resultados de preço unitário com desconto são arredondados para quatro casas decimais para consistência no processamento subsequente.
