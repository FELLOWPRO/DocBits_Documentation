# Métricas de desempenho

<figure><img src="../.gitbook/assets/performance-metrics-business-pt-20261111.png" alt="A página Métricas de desempenho na interface portuguesa com o filtro Unidade de tempo, os botões Filtro e Limpar, os separadores Visão de negócios e Visão de TI e os gráficos Duração média, Duração média para outras organizações e Resumo do serviço"><figcaption><p>A página Métricas de desempenho abre no separador Visão de negócios. Os valores apresentados vêm de uma organização de exemplo sintética e serão diferentes na sua organização.</p></figcaption></figure>

**Métricas de desempenho** mostra quanto tempo os documentos passam em cada etapa de processamento e com que frequência cada serviço é executado. Use a página para responder a perguntas como "Qual é a etapa mais lenta depois da validação?" ou "Como mudou o nosso volume de processamento nas últimas semanas?".

## Como aceder

A página Métricas de desempenho não tem uma entrada própria na barra lateral de Configurações. Abra-a de uma destas formas:

1. **Mapa do Site**: clique no ícone da lupa na parte inferior da barra lateral esquerda, escreva "Desempenho" no campo de pesquisa e clique na entrada **Métricas de desempenho** em **Configurações — Avançadas**. Ver [Mapa do Site](../end-user-and-partner-section/end-user-section/sitemap.md).
2. **Pesquisa Rápida Global**: prima **Ctrl+K** (ou **Cmd+K** num Mac) em qualquer ponto da aplicação, escreva "Desempenho" e abra a entrada com **Enter**. Ver [Pesquisa Rápida Global](../end-user-and-partner-section/end-user-section/global-quick-search.md).
3. Diretamente através do endereço `/settings/performance-metrics`. O endereço mais antigo `/performance_report` continua a abrir a mesma página.

A página requer direitos de administrador. Os valores apresentados vêm de uma organização de exemplo sintética e serão diferentes na sua organização.

## Filtros

Os filtros acima dos separadores definem o período e — no separador Visão de TI — os serviços cujos números quer ver.

| Filtro | Descrição |
|--------|-------------|
| **Unidade de tempo** | Escolha o período: **Últimos 7 dias**, **Últimos 30 dias** ou **Selecione o intervalo de tempo** para um período personalizado. Para um período personalizado, clique no ícone do calendário, escolha o primeiro e o último dia e confirme com **Ok**. |
| **Microsserviço** | Aparece apenas no separador **Visão de TI**. Escolha um único serviço (por exemplo OCR) para ver apenas os seus números. Deixe vazio para ver todos os serviços. |
| **Grupos de tempo (somente para frequência)** | Aparece apenas no separador **Visão de TI**. Agrupa o gráfico Frequência do Processo por hora, dia, semana ou mês. |
| **Filtro** | Aplica os filtros selecionados e redesenha os gráficos. |
| **Limpar** | Remove todos os filtros e volta a mostrar a vista predefinida. |

Os gráficos não se atualizam sozinhos quando altera um filtro — clique depois em **Filtro**.

## Visão de negócios

O separador **Visão de negócios** responde à pergunta do negócio: quanto tempo espera um documento em cada etapa de processamento? Mostra três gráficos:

| Gráfico | Descrição |
|---------|-------------|
| **Duração média** | Tempo médio por etapa na sua organização, de **Validação para Pronto** a **Pronto para Validação**, **Validado para Aprovado**, **Segunda Aprovação para Aprovado** e **Aprovado para Concluído**. |
| **Duração média para outras organizações** | As mesmas etapas para outras organizações, para comparar as suas durações com as delas. |
| **Resumo do serviço** | Tempo mais curto (**Mínimo**) e mais longo (**Máximo**) por etapa — útil para identificar valores atípicos. |

Os tempos são apresentados em horas, minutos e segundos. São valores médios — um documento individual pode ser mais rápido ou mais lento.

## Visão de TI

<figure><img src="../.gitbook/assets/performance-metrics-it-pt-20261111.png" alt="A página Métricas de desempenho, separador Visão de TI na interface portuguesa com os filtros Microsserviço e Grupos de tempo, o gráfico Duração média por serviço, o gráfico Frequência do Processo ao longo do tempo e o gráfico Resumo do serviço com Mínimo e Máximo"><figcaption><p>A Visão de TI decompõe os mesmos dados por serviço. Use o filtro Microsserviço para se concentrar num único serviço.</p></figcaption></figure>

O separador **Visão de TI** responde à pergunta técnica: que serviço usa quanto tempo e com que frequência? Mostra três gráficos:

| Gráfico | Descrição |
|---------|-------------|
| **Duração média** | Tempo médio de processamento por serviço: **OCR**, **Classificação**, **Extração** e **Exportar**. |
| **Frequência do Processo** | Quantos documentos cada serviço processou no período selecionado, agrupados pela definição **Grupos de tempo**. |
| **Resumo do serviço** | Tempo de processamento mais curto (**Mínimo**) e mais longo (**Máximo**) por serviço — útil para identificar valores atípicos. |

Cada gráfico tem um menu de transferência (Download SVG, Download PNG, Download CSV) no canto superior direito, para exportar um gráfico para um relatório ou um caso de suporte.

## Sugestões

* Comece pela **Visão de negócios** para ver onde os documentos esperam mais tempo; mude para a **Visão de TI** para ver qual serviço é a causa.
* Um tempo elevado em **Validação para Pronto** ou **Validado para Aprovado** indica normalmente trabalho manual (documentos à espera dos revisores), enquanto tempos elevados de OCR ou Extração indicam processamento do lado do sistema.
* Se um gráfico não mostrar dados, alargue o período em **Unidade de tempo** ou clique em **Limpar** e tente novamente.

## Páginas relacionadas

* [Painel de Análises](analytics-dashboard.md) — tempos de processamento detalhados por documento, fornecedor e tipo de documento.
* [Registo de atividade](settings/log-settings/README.md) — o registo de eventos subjacente, com filtros e exportação.
* [Página de Relatórios](report-page.md) — contagens de documentos, campos alterados e estatísticas de exportação.
