# Verificações Automáticas na Tela de Validação

## Visão Geral

Por padrão, campos específicos no processo de validação de campos são verificados automaticamente, validando seus valores usando fórmulas baseadas em outros valores extraídos. Nesta página, você pode encontrar os formulários usados para esses cálculos automáticos.

Você pode sempre verificar a fórmula utilizada passando o mouse sobre o ícone de informação.

<figure><img src="../../../.gitbook/assets/automatic_checks_1.png" alt=""><figcaption></figcaption></figure>

<mark style="color:red;">**Nota:**</mark> O ícone de informação só é visível se um valor tiver sido extraído para o campo correspondente.

## Formulários para verificações automáticas:

### Valor líquido:

```
Valor líquido = Valor do imposto * 100 / Taxa de IVA 
```

### Taxa de IVA:

```
Taxa de IVA = Valor do imposto * 100 / Valor líquido 
```

### Valor do imposto:

```
Valor do imposto = Valor líquido + Taxa de IVA / 100
```

### Valor líquido reduzido:

```
Valor líquido reduzido = Valor do imposto reduzido * 100 / Taxa de IVA reduzida
```

### Taxa de IVA reduzida:

```
Taxa de IVA reduzida = Valor do imposto reduzido * 100 / Valor líquido reduzido
```

### Valor do imposto reduzido:

```
Valor do imposto reduzido = Valor do imposto reduzido + Taxa de IVA reduzida / 100
```

### Valor líquido total:

```
Valor líquido total = Valor líquido + Valor do imposto reduzido + Valor líquido gratuito
```

### Valor líquido total nos EUA:

```
Valor líquido total nos EUA = Valor líquido + Taxas de envio + Encargos diversos + Quantidade adicional
```

### Valor total do imposto:

```
Valor total do imposto = Valor do imposto + Valor do imposto reduzido + Valor do imposto gratuito 
```

### Montante total:

```
Montante total = Valor líquido + Valor do imposto
```

<mark style="color:red;">**Nota:**</mark> Se o valor extraído e o valor validado não corresponderem, o documento não poderá ser processado. Um erro de **Incompatibilidade de Montantes** aparecerá para o campo correspondente.
