# Página de Relatórios

A **Página de Relatórios** resume o percurso dos documentos no DocBits durante um período: quantos foram recebidos, quanto tempo demorou o processamento, que campos foram corrigidos e qual foi o destino dos documentos. Destina-se a administradores e responsáveis de equipa que analisam globalmente o trabalho de receção e validação, e não um documento individual.

{% embed url="https://www.youtube.com/watch?v=ar9jXYJo_AM" %}

## Ativar a Página de Relatórios

A página é controlada por um interruptor de módulo. Ative-a uma vez para a organização:

1. Aceda a **Configurações → Módulo** e abra o grupo **Integração de Documentos**.
2. No cartão **Tipo de documento**, ative **Mostrar relatório**.
3. A entrada **Relatorio** passa então a aparecer na barra lateral para os utilizadores da organização.

<figure><img src="../.gitbook/assets/report-show-report-setting-pt.png" alt="O interruptor Mostrar relatório."><figcaption><p>O interruptor <strong>Mostrar relatório</strong>.</p></figcaption></figure>

## Abrir a Página de Relatórios

Selecione o ícone de gráfico **Relatorio** na barra lateral. A página abre com o filtro de período, os principais valores do período e as estatísticas dos campos.

<figure><img src="../.gitbook/assets/report-sidebar-icon-pt.png" alt="A barra lateral do DocBits com o ícone de gráfico realçado e o tooltip Relatorio"><figcaption><p>A entrada <strong>Relatorio</strong> na barra lateral.</p></figcaption></figure>

## Escolher o período

O filtro **Unidade de tempo** no topo da página define o período de todos os valores e secções abaixo. Disponibiliza **Últimos 7 dias**, **Últimos 30 dias** e **Selecione o intervalo de tempo**; esta última opção abre um calendário onde pode escolher a data de início e a data de fim.

<figure><img src="../.gitbook/assets/dbdc-19-report-time-options-native-20261103-pt.png" alt="Opções de Unidade de tempo: Últimos 7 dias, Últimos 30 dias e Selecione o intervalo de tempo. O cabeçalho e a navegação da aplicação estão fora da imagem."><figcaption><p>Opções de <strong>Unidade de tempo</strong>: <strong>Últimos 7 dias</strong>, <strong>Últimos 30 dias</strong> e <strong>Selecione o intervalo de tempo</strong>. O cabeçalho e a navegação da aplicação estão fora da imagem.</p></figcaption></figure>

## Os valores junto ao filtro

<figure><img src="../.gitbook/assets/report-time-unit-filter-pt.png" alt="A linha superior da Página de Relatórios: Unidade de tempo definida como 30, o cartão Novos Documentos, o cartão Tempo médio do sistema e o botão de transferência"><figcaption><p><strong>Unidade de tempo</strong>, <strong>Novos Documentos</strong>, <strong>Tempo médio do sistema</strong> e o botão de transferência.</p></figcaption></figure>

- **Novos Documentos** mostra quantos documentos foram importados no período selecionado.
- **Tempo médio do sistema** mostra o tempo médio, em segundos, que o DocBits demorou a processar um documento nesse período.
- O botão de transferência, à direita da linha, exporta o relatório como um ficheiro Excel (XLSX) para o período selecionado.

## Campos alterados

O gráfico **Campos alterados** conta quantas vezes cada campo foi corrigido manualmente no período selecionado, permitindo identificar facilmente os campos que a equipa mais edita. O ponto de interrogação junto ao título explica o que o gráfico conta. Quando existem correções manuais no período selecionado, o gráfico apresenta uma barra por campo; se não existirem dados, apresenta uma mensagem de período sem dados.

<figure><img src="../.gitbook/assets/report-changed-fields-pt.png" alt="A secção Campos alterados sem dados no período selecionado, com a mensagem Nenhuma entrada de dados encontrada no respectivo período de tempo."><figcaption><p>A mensagem apresentada em <strong>Campos alterados</strong> quando não existem dados no período selecionado.</p></figcaption></figure>

Utilize o menu no canto superior direito do gráfico para transferir o diagrama em **SVG**, **PNG** ou **CSV**.

## Secções adicionais do relatório

Abaixo do gráfico existem quatro cartões. Estão fechados por predefinição; selecione um cabeçalho para abrir a respetiva tabela e selecione-o novamente para a fechar.

1. **Total de documentos por tipo** lista cada tipo de documento com o respetivo **Tipo** e o número de documentos em **Contar**. Um tipo que tenha subtipos de documento apresenta um sinal **+** para desagregar esse total.
2. **Média diária por doctype** apresenta a mesma lista como uma média diária por tipo de documento.
3. **Estatística de status** desagrega os documentos por estado de processamento, com as colunas **Tipo**, **Status** e **Contar**.
4. **Estatística de exportação** lista primeiro as organizações da sua conta; expanda uma para ver os formatos de exportação utilizados, com as colunas **Usuários**, **Tipo** e **Exportado**.

<figure><img src="../.gitbook/assets/report-total-documents-per-type-pt.png" alt="O cartão Total de documentos por tipo expandido, com as colunas Tipo e Contar"><figcaption><p><strong>Total de documentos por tipo</strong>.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/report-daily-average-per-doctype-pt.png" alt="O cartão Média diária por doctype expandido, com as colunas Tipo e Contar"><figcaption><p><strong>Média diária por doctype</strong>.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/report-status-statistic-pt.png" alt="O cartão Estatística de status expandido, com as colunas Tipo, Status e Contar"><figcaption><p><strong>Estatística de status</strong>.</p></figcaption></figure>

<figure><img src="../.gitbook/assets/dbdc-19-report-export-stats-native-20261103-pt.png" alt="Estatística de exportação com uma organização existente expandida. Os nomes das organizações e os valores das linhas estão mascarados; a imagem mostra estatísticas existentes."><figcaption><p><strong>Estatística de exportação</strong> com uma organização existente expandida. Os nomes das organizações e os valores das linhas estão mascarados; a imagem mostra estatísticas existentes.</p></figcaption></figure>
