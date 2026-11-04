# Eliminar linhas com quantidade e valor vazios

#### Parte 1: Eliminar Linhas com Quantidade e Valor Vazios

Esta seção do script processa uma tabela de faturas para remover quaisquer linhas em que tanto a quantidade quanto o valor total sejam zero ou não fornecidos.

* **Verificar INVOICE\_TABLE:** Começa verificando se a chave `INVOICE_TABLE` existe no dicionário `tables_dict`.
* **Iterar sobre as Linhas:** Para cada linha na tabela, o script inicializa flags e variáveis para determinar se as colunas `TOTAL_AMOUNT` e `QUANTITY` existem e para capturar seus valores.
* **Verificar Nomes das Colunas:** Ao iterar por cada coluna em uma linha, procura por colunas com os nomes `TOTAL_AMOUNT` e `QUANTITY`.
* Se `TOTAL_AMOUNT` for encontrado, captura o valor. Se este valor for diferente de zero, converte-o para um float.
* Da mesma forma para `QUANTITY`, capturando e convertendo o valor se for diferente de zero.
* **Marcar Linha para Deleção:** Após verificar ambas as colunas em uma linha, se tanto o valor total quanto a quantidade forem efetivamente zero (seja por serem zero ou por não existirem), a linha é marcada para deleção definindo `row['is_deleted']` como `True`.

#### Parte 2: Validar Total da Linha Contra o Total da Fatura

Esta seção calcula o valor total de todas as linhas em uma fatura e compara com o total reportado na fatura para validar sua consistência.

* **Inicializar Total da Linha:** Começa definindo uma variável `lines_total` como 0.0 para acumular o valor total de todas as linhas.
* **Somar Valores das Linhas:** Itera sobre cada linha na `INVOICE_TABLE`, extraindo o `TOTAL_AMOUNT` de cada uma e adicionando a `lines_total`.
* **Recuperar e Converter Total da Fatura:** Busca o valor total da fatura usando uma função auxiliar `get_field_value` e converte para um float.
* **Comparar Totais:** Por fim, verifica se a diferença absoluta entre o total da linha calculado (`lines_total`) e o total da fatura reportado (`total_amount`) excede um limite de 0.05. Se sim, marca o campo de total da fatura como inválido usando outra função auxiliar `set_field_as_invalid`, citando uma inconsistência.
```python
##################################################
# Delete lines with empty quantity and amount
##################################################


if tables_dict.get('INVOICE_TABLE'):
for row in tables_dict['INVOICE_TABLE']['rows']:
amount_col_found = False
quantity_col_found = False
line_amount = 0.0
line_quantity = 0.0
for col in row['columns']:
if col['name'] == 'TOTAL_AMOUNT':
amount_col_found = True
line_amount = col.get('value', 0)
if line_amount:
line_amount = float(line_amount)
if col['name'] == 'QUANTITY':
quantity_col_found = True
line_quantity = col.get('value', 0)
if line_quantity:
line_quantity = float(line_quantity)
if amount_col_found and quantity_col_found:
break
if amount_col_found and quantity_col_found and (not line_amount and not line_quantity or (line_amount + line_quantity) == 0):
row['is_deleted'] = True

##################################################
# End: Delete lines with empty quantity and amount
##################################################

##################################################
# Validating Line total againg invoice total
##################################################
lines_total = 0.0
# Getting Lines Total
if tables_dict.get('INVOICE_TABLE'):
for row in tables_dict['INVOICE_TABLE']['rows']:
line_amount = 0.0
for col in row['columns']:
if col['name'] == 'TOTAL_AMOUNT':
line_amount = col.get('value', 0)
if line_amount:
line_amount = float(line_amount)
break
lines_total += line_amount

# Getting Invoice total
total_amount = get_field_value(fields_dict, "net_amount", "0.0")
if total_amount:
total_amount = float(total_amount)

# Comparing lines total with invoice total
if abs(total_amount - lines_total) > 0.05:
set_field_as_invalid(fields_dict, "net_amount", "Invoice total mismatches lines total", "AMOUNTS_MISMATCH")

##################################################
# End: Validating Line total againg invoice total
##################################################







```
#### Resumo

O script garante efetivamente a integridade dos dados ao:

1. Remover linhas de dados que não contribuem para o total financeiro da fatura devido à falta de quantidades ou valores.
2. Validar a consistência entre a soma dos valores de linha individuais e o total geral da fatura, destacando discrepâncias para ação adicional.

Essa automação ajuda a manter registros financeiros precisos e pode ser crucial para sistemas como ERP que exigem dados precisos para contabilidade e relatórios financeiros.
