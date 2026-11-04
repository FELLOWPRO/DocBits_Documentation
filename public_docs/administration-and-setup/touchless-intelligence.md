# Touchless Intelligence

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence/v1/pt.mp4" %}

Touchless Intelligence distingue duas perguntas: **o DocBits extraiu corretamente a fatura?** e **o processo inteiro terminou sem intervenção de processamento?** Extração correta não exclui trabalho devido a dados Infor diferentes. AP é a equipa humana de contas a pagar.

## Encontrar o guia certo

| Guia | Conteúdo |
| --- | --- |
| [Métricas e cálculo](touchless-metrics.md) | Categorias, numerador/denominador, ações e cálculos |
| [Usar o painel](touchless-dashboard.md) | Filtros, indicadores, tendências e primeiros bloqueios |
| [Exemplos: preço e quantidade](touchless-examples.md) | Faturas fictícias e vistas Dev reais de diferenças de preço e quantidade |
| [Touchless Intelligence: diagnóstico de fornecedores e clusters de problemas](touchless-supplier-diagnosis.md) | Priorizar fornecedores e causas recorrentes |
| [Touchless Intelligence: diagnóstico de PO Matching](touchless-po-matching-diagnosis.md) | Regras ativas, tolerâncias e decisões |
| [Touchless Intelligence: Rastreamento do documento](touchless-document-trace.md) | Originais, execuções, bloqueios e intervenções |
| [Touchless Intelligence: propostas de alteração e relatórios](touchless-change-proposals.md) | Distinguir pré-visualização, aplicação, medição e reversão |
| [Explicar e melhorar Touchless com MCP](touchless-mcp.md) | Explicar, diagnosticar e melhorar de forma controlada com MCP |

<figure><img src="../.gitbook/assets/touchless-overview-pt.png" alt="A aba Touchless Intelligence com cinco indicadores principais, sugestões de melhoria e o gráfico da taxa touchless"><figcaption><p>A aba Touchless Intelligence: indicadores principais, melhorias, a taxa ao longo do tempo e o gráfico de onde o touchless se perde primeiro. Organização de exemplo com dados de demonstração; os nomes dos fornecedores são fictícios.</p></figcaption></figure>

## Acesso

Parte do [painel de análise](analytics-dashboard.md). Administradores têm acesso; outros utilizadores precisam da permissão de função correspondente. Análise IA, alterações e relatórios podem exigir administrador.

<!-- Source notes (not shown): screenshots come from the dev test organisation with synthetic demo data (seed script) and fictional supplier names; the PO matching decision flow has no screenshot yet. facts read from the doc2app code (TouchlessIntelligence pages and components) and the dev UI on 14 Oct 2026; NOVA gates the tab with its own organisation flag, VESTA with the Analytics module. Consulting report export format not verified, so no export is described.

<!-- Alignment 2026-11-04: correct extraction is distinct from process Touchless; KPI numerator and denominator verified. -->
<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->
