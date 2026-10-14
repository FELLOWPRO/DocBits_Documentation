# Painel

## Visão Geral

As configurações do Painel são projetadas para ajudar os administradores a controlar a apresentação e a interação dos dados dentro do painel DocBits. Essas configurações determinam quais informações estão imediatamente disponíveis ao fazer login, garantindo que os usuários tenham acesso rápido aos dados mais relevantes para suas tarefas.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_1.png)

## Acessando as Configurações do Painel

Para acessar as configurações do painel, navegue até:\
**Configurações → Configurações globais → Painel**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_dashboard.png)

## **Em geral**

* **Redefinir filtros**: Permite a configuração de quando os filtros do painel devem ser redefinidos, como após o upload de documentos, reinício de documentos ou exportação de documentos. Isso ajuda a manter uma tela limpa para visualização de dados de acordo com estágios específicos do fluxo de trabalho.
* **Dados do painel**:
  * **Carregamento automático do painel de controle**: Controla se o painel deve carregar automaticamente os dados ao acessar o usuário, o que pode ajudar a reduzir os tempos de carregamento e melhorar a experiência do usuário, carregando dados apenas quando necessário.
  *   **Exportar dados do painel**: Este recurso adiciona um novo botão **Exportar** à barra de ferramentas do painel, permitindo que você exporte a visualização atual do painel como um arquivo **.csv** ou **.xlsx**.

      ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_3.png)

## **Histórico de Exportação**

No **Histórico de Exportação**, você verá uma tabela listando todas as exportações anteriores junto com informações-chave sobre cada solicitação.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_4.png)

Os seguintes detalhes estão incluídos:

* **E-mail**: O endereço de e-mail de onde a exportação foi solicitada.
* **Status**: O status atual da exportação (Pendente, Concluído).
* **Solicitado em**: A data e hora em que a exportação foi iniciada.
* **Concluído em**: A data e hora em que a exportação foi concluída.
* **Formato**: O formato de arquivo usado para a exportação (CSV, XLSX).
* **Filtros Usados**: Quaisquer filtros que foram aplicados ao painel no momento da exportação.

<mark style="color:red;">**Nota**</mark>: Para exportar tabelas, a opção Exportar dados do painel na seção [Em geral](./#em-geral) deve estar ativa.

## **Ação**

* **Atribuir a**: Este recurso permite que os usuários definam permissões para a atribuição de documentos.
  * **Apenas para Admin**: Apenas usuários administradores podem atribuir documentos, independentemente das permissões concedidas a usuários não administradores.
  * **Todos os Usuários**: Todos os usuários que receberam as [permissões](../groups-users-and-permissions/groups-and-permissions/activating-permissions.md) necessárias podem atribuir documentos.
* **Reiniciar**: Este recurso permite que os usuários definam permissões para reiniciar documentos.
  * **Apenas para Admin**: Apenas usuários com privilégios de Admin podem reiniciar documentos, independentemente das permissões concedidas a usuários não administradores.
  * **Apenas Admin e Atribuído**: Apenas usuários com privilégios de Admin e o usuário atribuído podem reiniciar o documento.
  * **Todos os Usuários**: Todos os usuários que receberam as [permissões](../groups-users-and-permissions/groups-and-permissions/activating-permissions.md) necessárias podem reiniciar documentos.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_2.png)

## **Filtros**

* **Estilo de filtro de status**: Determina o estilo de apresentação dos filtros de status, que podem ser definidos como padrão ou personalizados de acordo com o foco operacional dos usuários.
* **Filtro de status personalizado**: Permite a criação e aplicação de filtros personalizados que podem direcionar status de documentos específicos, como "Novo", "Validando" ou "Exportando". Isso permite que os usuários acessem rapidamente documentos em estágios específicos de processamento.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_5.png)

## Painel de Remessa Avançada

* **Visibilidade de Pedidos Entregues**: Este recurso permite que o usuário especifique a duração pela qual os pedidos entregues serão visíveis.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/dashboard_settings_6.png)

Essas configurações do painel são cruciais para garantir que a plataforma DocBits seja o mais responsiva e útil possível, fornecendo aos usuários uma ferramenta poderosa para monitorar e gerenciar atividades de processamento de documentos diretamente do painel.
