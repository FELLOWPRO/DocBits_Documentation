# Touchless Intelligence

Touchless Intelligence distingue duas perguntas: **o DocBits extraiu corretamente a fatura?** e **o processo inteiro terminou sem intervenção de processamento?** Extração correta não exclui trabalho devido a dados Infor diferentes. AP é a equipa humana de contas a pagar.

## Vídeo: funções do relatório Touchless

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/pt.mp4" %}

Esta versão de revisão de 5:15 apresenta um relatório com dados: filtros, indicadores e cálculo, evolução, primeiros bloqueios, provas registadas, histórico do documento, execuções, regras aprendidas, melhorias e histórico, consultoria e resultados MCP reais.

[Abrir o vídeo com legendas em português e 16 capítulos](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/pt.html). A avaliação auditiva desta nova versão ainda está pendente.

Estes casos didáticos explicam funções do relatório. Uma recomendação ou pré-visualização não prova uma configuração aplicada nem uma melhoria medida. A proposta MCP apresentada ainda precisa de uma configuração de destino concreta; pré-visualização e aplicação não estão disponíveis. Alguns textos nativos do produto podem manter o idioma original. Nas regras aprendidas, «20 de 21» indica os casos a que a regra se aplica. O contraexemplo mostra um valor já aceite que seria substituído; alguns rótulos da interface traduzem este significado de forma imprecisa.

<figure><img src="../.gitbook/assets/anatomy-touchless-pt.svg" alt="Linha de triagem isométrica: uma esteira com 14 portões, um empurrador que desvia um documento para uma bandeja de revisão, um contentor de exportação com uma pilha de documentos e um mostrador com 78,9 por cento"><figcaption><p>O Touchless como linha de triagem, com os números ilustrativos do cálculo de exemplo: os 14 portões são as etapas do Caminho do oleoduto, as folhas ainda na esteira estão em andamento e não são contadas, um documento que para num portão é empurrado para a bandeja de revisão com os documentos AP Assisted (30) e de exceção de processo (10), e os documentos Pure touchless (120) e apenas aprovação (30) no contentor de exportação dão ao mostrador 150 de 190, ou 78,9 %, acima da marca da meta de 70 %.</p></figcaption></figure>

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
