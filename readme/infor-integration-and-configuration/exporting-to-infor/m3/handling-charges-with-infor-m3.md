# Tratamento de Encargos com o Infor M3

## Visão geral

Este documento fornece informações detalhadas sobre como o DocBits se integra ao Infor M3 para tratar os encargos associados a faturas e pedidos de compra (PO). Ele inclui cenários de encargos externos e as soluções esperadas.

## Cenários de tratamento de encargos

| ID do cenário | Descrição                                                                                      | Caso de negócio                                                                                                                                | Solução esperada                                                                                                                                                                                                                                                  |
| ------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1             | Encargos externos que não estão no PO, mas estão na fatura (aceitos)                           | Os encargos externos aparecem na fatura, mas não constam no PO. Esses encargos são aceitos.                                                    | Os encargos serão lançados na regra contábil PP20-228, com base no elemento de custo enviado pelo DocBits.                                                                                                                                                        |
| 2             | Encargos externos que não estão no PO, mas estão na fatura (não aceitos)                       | Os encargos externos aparecem na fatura, mas não constam no PO. Esses encargos não são aceitos nem aprovados.                                  | O valor total da fatura é registrado com um encargo de cabeçalho para os encargos não aprovados. Além disso, é criada uma nota de débito para esses encargos.                                                                                                     |
| 3             | Encargos externos na fatura maiores ou menores que os do PO (dentro da tolerância)             | Os encargos externos na fatura são maiores ou menores que os do PO, mas estão dentro da tolerância aceita.                                     | Os encargos adicionais são lançados na regra contábil PP20-228, com base no elemento de custo enviado pelo DocBits.                                                                                                                                               |
| 4             | Encargos externos na fatura maiores que os do PO (fora da tolerância, não aprovados)           | Os encargos externos na fatura são maiores que os do PO, estão fora da tolerância aceita e não são aprovados.                                  | A fatura é registrada com o valor total da fatura. Um encargo adicional não aprovado é incluído como encargo de cabeçalho, e uma nota de débito é criada para esse encargo adicional.                                                                              |
| 5             | Encargos externos na fatura maiores que os do PO (fora da tolerância, aprovados no DocBits)    | Os encargos externos na fatura são maiores que os do PO, estão fora da tolerância aceita e são aprovados no DocBits.                            | Os encargos adicionais são lançados em PP20-228. Duas opções consideradas:\<br>- Se a tolerância do APS900 for maior que a do DocBits, os encargos adicionais são lançados automaticamente.\<br>- Se a tolerância do APS900 for igual à do DocBits, os encargos adicionais são lançados com novos elementos de encargo que não constam no PO. |
| 6             | Encargos externos na fatura menores que os do PO (fora da tolerância, não aprovados)           | Os encargos externos na fatura são menores que os do PO, estão fora da tolerância aceita e não são aprovados.                                  | A fatura é lançada como não aprovada no APS110. A equipe de contas a pagar ajusta os encargos por meio da opção Invoice Control no APS110, que chama o APS360.                                                                                                    |
| 7             | Encargos externos no PO e nenhum encargo na fatura                                             | Os encargos externos constam no PO, mas não há encargos na fatura.                                                                             | A fatura é lançada como não aprovada no APS110. A equipe de contas a pagar ajusta os encargos por meio da opção Invoice Control no APS110, que chama o APS360.                                                                                                    |

## Exemplo para o cenário 5

| Campo          | Valor no PO | Valor na fatura do fornecedor |
| -------------- | ----------- | ----------------------------- |
| Linha 1        | $6000       | $6000                         |
| Frete (E001)   | $1000       | $3000                         |
| **Total**      | $7000       | $9000                         |

**Tolerância do frete:** $100 aprovados automaticamente no M3 (APS900) e no DocBits. Valor total da fatura de $9000 aprovado manualmente (com os encargos).

**APS451 (linha da fatura):**

* Tipo de linha 1 (linha da fatura): $9000
* Tipo de linha 5 (encargo de linha): $1000 (elemento: E001 para frete no PO de $1000)
* Tipo de linha 5 (encargo de linha): $2000 (elemento: E101 para frete no PO de $0)

### Campos e valores importantes para o tratamento de encargos no DocBits

| Campo                                  | Descrição                                                     |
| -------------------------------------- | ------------------------------------------------------------- |
| Sequence Number (número de sequência)  | Identificador único de cada cenário de encargo                |
| Costing Element ID                     | Identificador do elemento de custo                            |
| Costing Element Description            | Descrição do elemento de custo                                |
| Charge Type (tipo de encargo)          | Normalmente "External"                                        |
| Charge Invoicing                       | A relevância ainda precisa ser determinada                    |
| Distribution Method                    | Método usado para distribuir os encargos                      |
| Gross Weight (peso bruto)              | Aplicável se o peso bruto estiver disponível na fatura        |
| Volume                                 | Os casos de aplicação precisam ser definidos                  |
| Net Amount (valor líquido)             | Os casos de aplicação precisam ser definidos                  |
| 3rd Party Charge                       | Presença na fatura e requisitos de processamento              |
| Invoice Charge Quantity                | Requer esclarecimento                                         |
| Markup                                 | Considerado a diferença entre encargo e desconto              |
| Charge Category                        | A relevância precisa ser definida                             |
| Costing Operator                       | A relevância precisa ser definida                             |

\

