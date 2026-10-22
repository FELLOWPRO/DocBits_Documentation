---
description: "Configurar cartões através de nome, versão, entradas, âmbito, resultados e efeitos."
---

# Compreender e configurar cartões de workflow

Escolha o cartão pela operação e pelo âmbito dos dados. **Field is** verifica presença ou vazio; **Docfield is** compara um valor. Atribuição documental, tarefa e notificação têm efeitos diferentes. Uma categoria não substitui a referência de uma versão específica.

## O que uma referência completa explica

| Elemento | Pergunta necessária |
| --- | --- |
| Identidade | Nome visível, tipo técnico, versão e função When/And/Then? |
| Requisitos | Licença, permissões e dados necessários? |
| Entradas | Tipo, valor, predefinição e opções permitidas por parâmetro? |
| Âmbito | Campo, linha, todas as posições ou variável de organização? |
| Resultados | Sucesso, falso ou erro? O que utiliza o próximo cartão? |
| Efeitos | Documentos, tarefas ou sistemas externos alterados? O que simula o teste? |
| Exemplos | Que configuração e entrada completas produzem cada resultado? |
| Limites e versões | Dados ausentes, limites exatos e versões antigas? |

## Exemplo preenchido: Docfield is

**Tipo técnico:** `condition_docfield_operator_value` · **Versão:** 2 · **Função:** And. Requer documento com layout definido e o campo a verificar.

| Entrada | Configuração |
| --- | --- |
| Field Name | `total_amount`, chave técnica e não etiqueta traduzida |
| Operator | `gt` / Maior que |
| Field Value | `1000`, sem símbolo monetário |

O cartão compara o campo do documento atual com o valor configurado. Não muda estados, cria tarefas ou exporta. Em Advanced, verdadeiro segue Success, falso segue Failed Condition e erro de avaliação segue Error. Em Standard, uma condição não satisfeita interrompe a sequência linear.

Casos realmente verificados: **1785** → Success; **999** e **1000** → Failed Condition; **1000,01** → Success; número ausente ou inválido → Error. JSON usa ponto decimal. Estes resultados descrevem esta configuração numérica, não todos os tipos e operadores.

Distinga este cartão dos cartões explícitos de tolerância. Não deduza igualdade ou operadores inclusivos apenas de `gt`; teste a combinação necessária com os seus próprios limites.

## Passos seguintes

Ligue sucesso a revisão, falso ao percurso padrão e erro à correção de dados. O [caso completo](advanced-workflow-case-study.md) inclui configuração, cartões seguintes e resultados reais. O [modelo de execução](workflow-execution-model.md) explica guardar e ativar; o [diagnóstico](workflow-troubleshooting.md) ajuda a investigar resultados diferentes.

## WF-05: Exercício e aceitação

Descreva Run Workflow e um cartão PO com a mesma estrutura: parâmetros, predefinições analisadas, percursos, efeitos e versões. Verifique destino inativo, dados ausentes e base percentual.

[Percurso](workflow-learning-path.md)
