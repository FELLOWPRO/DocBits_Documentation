---
description: "Transferir fatura sintética, workflow JSON, entradas, expectativas e respostas reais de teste."
---

# Pacote de formação de workflows

Utilize este pacote com o [caso Advanced](advanced-workflow-case-study.md). Inclui fatura sintética, workflow importável, sete entradas documentais completas, expectativas independentes e respostas reais guardadas. As chaves técnicas e os nomes dos percursos permanecem iguais em todas as línguas.

{% file src="../../.gitbook/assets/workflow-training-kit-v2.zip" %}
Pacote de formação com exemplos e resultados
{% endfile %}

## Conteúdo e formatos

| Ficheiro | Utilização |
| --- | --- |
| `training-invoice.pdf` | Fatura sintética: 1500 EUR líquidos, 285 EUR de imposto, total 1785 EUR. Não pagar. |
| `advanced-workflow.json` | Importar desativado por **Import Workflow**; sem variável global, limitado a Fatura e ao número exato de formação. |
| `*-input.json` | Dados completos para **Advanced Test → Custom Data**. |
| `expectations.json` | Percursos, mensagens de estado e resultados esperados; especificação funcional, não ficheiro de carregamento do Test Manager. |
| `*-result.json` | Respostas reais Dev com resultados e mensagens; referências privadas de organização substituídas. |
| `prepare_inputs.py` | Substitui a organização sintética nas duas posições necessárias. |
| `verify_results.py` | Verifica respostas contra expectativas independentes. Requer Python 3, sem chave de acesso. |

## Utilização

1. Extraia o ZIP e leia as instruções incluídas.
2. Importe o workflow na sua organização de teste e confirme que está desativado.
3. Obtenha o ID da sua organização de teste e execute localmente:

```bash
python3 prepare_inputs.py --org-id YOUR_TEST_ORGANIZATION_UUID --out prepared
python3 verify_results.py
```

4. Utilize os ficheiros de `prepared/` na janela Advanced. Não substitua uma ID documental sintética por uma fatura real de cliente.
5. Verifique os sete casos na [tabela de resultados](advanced-workflow-case-study.md). As variações de montante são deliberadas; não alteram a fatura anexa.

Os dados incluem `id`, `org_id`, `doc_type`, `status` e `extracted_data` com `layout.groups`, `fields` e `tables`. As organizações no topo e em `extracted_data` devem corresponder à conta ligada. Um valor sem definição correspondente no layout pode não ser lido como campo documental existente.

## Âmbito do exercício

As expectativas verificam percursos escolhidos, texto de encaminhamento, mensagens de estado e nós finais, além do estado documental. Não equivalem à comparação de estado de um cenário guardado no Test Manager.

Um teste Advanced bem-sucedido confirma o processamento dos dados fornecidos. Ações simuladas não são atribuições, emails ou entregas reais. A ativação exige uma entrada de evento adequada e uma execução real verificada separadamente. Veja [Quando é executado o meu workflow?](workflow-execution-model.md).

## WF-03: Exercício e aceitação

Extraia v2, adapte organização com prepare_inputs.py e execute verify_results.py. decision-table-setup.json orienta a configuração e acceptance-record-template.json é modelo de registo; nenhum importa workflows. Confirme estado inativo antes de importar.

[Percurso](workflow-learning-path.md)
