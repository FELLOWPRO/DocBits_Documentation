# Se o país estiver no campo

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-70b0b5860da5-pt.png" alt="Campos do cartão na versão apresentada. Os campos ainda não estão configurados." width="563"><figcaption><p>Campos do cartão na versão apresentada. Os campos ainda não estão configurados.</p></figcaption></figure>

Use esta condição quando uma etapa adicional de processamento deva depender de um grupo de países. O exemplo verifica se o país lido de um campo do documento pertence à União Europeia.

**Localização:** Workflow padrão → condições adicionais (AND) → Campo do documento. Configure a ação seguinte separadamente em THEN.

## Configuração — versão 2

| Definição | Valor |
| --- | --- |
| Campo | Um campo de texto existente que contenha o nome do país |
| Operador | `is` |
| Região | União Europeia (UE) |
| Valor de continuação | `true` |

<!-- workflow-card-practical-example-20261021 -->

## Exemplo prático

| Valor do país no campo | Condição esperada |
| --- | --- |
| `Germany` | Satisfeita |
| `United States` | Não satisfeita |

Os nomes dos países apresentados como código são valores de entrada fixos para este exemplo.

## Limites e verificações

`false` não inverte a comparação. Com essa definição, mesmo um país correspondente não produz uma condição positiva. Para verificar a condição oposta, selecione `isnot` com `true`.

Trate separadamente campos ausentes e valores de país vazios; eles podem devolver um resultado de dados em falta em vez de uma falta de correspondência normal.

A análise do código-fonte da versão de desenvolvimento de 22 de outubro de 2026 mostra um erro de conversão para entradas ISO como `DE` e `DEU`. Por isso, estes exemplos usam nomes de países completos. Verifique separadamente o tratamento de códigos ISO na versão instalada.

Os grupos disponíveis, incluindo UE, Schengen e NAFTA, vêm da implementação do cartão. Confirme os países incluídos na sua versão antes de usar um grupo numa regra de negócio.
