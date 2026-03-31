# Notas de versão

## **Lançamento Spring Spark 13 de maio de 2026**

Disponibilidade no Sandbox: 27–29 de abril de 2026

### Melhorias do DocBits:

*   **Advanced Workflow Designer:**\
    O DocBits apresenta um Advanced Workflow Designer completamente novo — um construtor de automação visual baseado em nós que coloca a orquestração completa de fluxos de trabalho ao alcance das suas mãos. Usando uma tela intuitiva de arrastar e soltar, os administradores podem conectar cartões de fluxo de trabalho do DocBits em pipelines de processamento complexos e de múltiplas etapas. Cada nó na tela representa uma ação ou ponto de decisão, e as conexões entre os nós definem o fluxo dos documentos através do pipeline. O designer suporta etapas de espera para introduzir atrasos temporizados, caminhos paralelos onde todos ou alguns ramos devem ser concluídos antes de continuar, e a capacidade de encadear qualquer combinação de cartões integrados ou criados por parceiros. Os fluxos de trabalho podem ser salvos como modelos reutilizáveis, importados e exportados entre ambientes, e testados diretamente a partir do designer antes de entrar em produção. O editor possui uma tela com snap-to-grid e navegação por mini-mapa para fluxos de trabalho grandes, atalhos de teclado para copiar e colar, validação em tempo real com destaque de erros durante a construção, e proteção contra edição concorrente para evitar a sobrescrita de alterações por outros utilizadores. Registos de execução detalhados fornecem monitorização por nó, permitindo aos administradores rastrear exatamente como cada etapa de um fluxo de trabalho foi executada e onde ocorreram problemas.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_advanced_workflow_designer.png)

*   **Melhorias do Workflow Designer:**\
    O designer de fluxos de trabalho existente foi melhorado com lógica de ramificação if/else, permitindo fluxos de trabalho baseados em decisões mais sofisticados. Vários novos cartões de condição foram adicionados, expandindo ainda mais a gama de lógica de automação disponível. Um novo Workflow Test Manager permite que os administradores criem e executem testes automatizados para fluxos de trabalho individualmente ou todos de uma vez, garantindo que as alterações se comportem como esperado antes da implantação. A secção de Workflow agora também inclui um painel de KPIs com métricas chave sobre o desempenho de execução dos fluxos de trabalho.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_workflow_branching.png)

*   **DocNet AI Agents:**\
    O DocBits agora inclui DocNet AI Agents — agentes inteligentes e autónomos que funcionam em segundo plano para lidar com tarefas de processamento de documentos como a correspondência de ordens de compra e a validação de faturas. Os agentes operam de forma independente, trabalhando nas tarefas atribuídas e escalando para os utilizadores apenas quando é necessário julgamento humano. Quando um agente encontra uma exceção ou requer confirmação, cria um pedido de aprovação que aparece diretamente na caixa de entrada do utilizador, garantindo que nada é perdido sem necessitar de supervisão constante. Os agentes podem coordenar-se entre si, delegar sub-tarefas e organizar o trabalho em missões e projetos para processos complexos de múltiplas etapas. Um painel dedicado de agentes fornece visibilidade completa sobre a atividade dos agentes, métricas de desempenho e registos de auditoria, para que os administradores possam monitorizar o que os agentes estão a fazer e quão eficientemente trabalham. Notificações em tempo real mantêm os utilizadores informados quando os agentes concluem tarefas ou sinalizam itens para revisão.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_docnet_ai_agents.png)

*   **Partner Card SDK:**\
    Um novo Partner Card SDK permite que desenvolvedores de terceiros e parceiros criem cartões de fluxo de trabalho personalizados para o DocBits. Os parceiros podem carregar pacotes de cartões para validação e revisão, importar cartões de repositórios GitHub e gerir submissões através de uma página dedicada de configurações do Card SDK. Um sistema de revisão alimentado por IA avalia automaticamente os cartões submetidos quanto à qualidade e conformidade. O SDK inclui downloads baseados em exemplos com diálogos de seleção de cartões, validação comportamental num ambiente sandbox e documentação abrangente para começar. O Card SDK é protegido por verificações de licença e agora é visível para todos os utilizadores, não apenas administradores.

*   **Full-Text Search / DocSearch:**\
    Uma nova capacidade de pesquisa de texto completo foi adicionada ao DocBits, alimentada por pesquisa vetorial baseada em IA. Os utilizadores podem pesquisar em todos os documentos indexados com filtragem de fornecedores em tempo real e uma funcionalidade "Find Similar" para localizar documentos semelhantes a um selecionado. Uma página de configurações dedicada permite que os administradores configurem a indexação de dados de IA, preferências de armazenamento vetorial e monitorizem o progresso da indexação em tempo real. O acesso ao DocSearch é gerido através de planos de subscrição.

*   **Expansão de formatos E-Invoice:**\
    O DocBits expandiu significativamente o seu suporte de formatos de fatura eletrónica com mais de 80 novos tipos globais de e-invoice e mais de 40 novos formatos. Os formatos recentemente suportados incluem Taiwan EGUI, Thailand E-Tax, India GST Credit Note, SPS Commerce RSX 7.7.4, XRechnung 3.0.2, ZUGFeRD 2.2 e 2.3.2, variantes Factur-X, Uruguay CFE, Ecuador SRI Retención, SVEFAKTURA 1.0, EHF 3.0, OIOUBL, Finvoice e Asia-Pacific PINT Credit Notes, entre outros. O DocBits agora atinge 100% de cobertura de classificação e extração para todos os formatos de documentos eletrónicos suportados.

*   **Login Analytics:**\
    Um novo painel de Login Analytics dá aos administradores visibilidade completa sobre a atividade de login em toda a organização. O painel inclui gráficos comparativos que mostram tendências de login ao longo do tempo, vistas de agregação diária e semanal, e geolocalização baseada em GeoLite2 para ver de onde vêm os logins. Isto fornece uma forma rápida de detetar padrões de login incomuns e monitorizar a segurança das contas.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_login_analytics.png)

*   **Analytics Dashboard:**\
    Um módulo abrangente de análise de processamento de documentos foi introduzido com múltiplas vistas de painel incluindo Executive Overview, API Metrics, Quality Metrics e Processing Performance. Document Flow Analytics oferece métricas ao nível da organização sobre tempos de processamento de documentos e transições de estado. Um sistema completo de Activity Log e Event Log permite que os administradores naveguem, pesquisem, filtrem e exportem dados de eventos com visualizações de gráficos e destaque de sintaxe JSON. Uma funcionalidade de Audit Trail fornece rastreamento detalhado do histórico de alterações com detalhes em popup para cada modificação.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_analytics_dashboard.png)

*   **Melhorias no Controlo de Acesso:**\
    O controlo de acesso foi aplicado em toda a aplicação, cobrindo a tela de validação de campos, tabelas extraídas por IA e múltiplas outras vistas. Os administradores agora têm a opção de desativar o controlo de acesso globalmente quando necessário. O design do controlo de acesso foi renovado para uma experiência mais consistente e intuitiva em todas as telas.

*   **Melhorias do Layout Builder:**\
    O Layout Builder agora suporta campos ocultos e de apenas leitura com indicadores visuais, facilitando aos administradores compreender quais campos são visíveis e editáveis para os utilizadores. Um divisor redimensionável entre painéis melhora a flexibilidade do espaço de trabalho, e as configurações de comprimento de campo fornecem controlo mais preciso sobre campos de entrada de dados.

*   **Histórico de Exportação nas Ações do Dashboard:**\
    Os utilizadores podem agora aceder ao histórico de exportação de um documento diretamente a partir do menu de ações do painel, tornando mais rápido rever tentativas de exportação anteriores sem sair da vista principal.

*   **Melhorias na Exportação:**\
    As configurações de exportação agora suportam ordenação de execução, permitindo aos administradores definir a sequência em que múltiplos métodos de exportação são processados. Um novo botão de re-exportação nas telas de erro permite que os utilizadores tentem novamente a partir da etapa que falhou em vez de reiniciar todo o processo. O DocBits também agora suporta o alvo de exportação API GLS840MI, com uma interface atualizada para gerir múltiplas configurações de exportação ativas por tipo de documento.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_export_improvements.png)

*   **Script Versioning & AI Chat:**\
    Os scripts de documentos agora suportam histórico completo de versões, permitindo aos administradores rastrear alterações, comparar versões e restaurar versões anteriores de scripts. Os scripts predefinidos são protegidos contra edições acidentais, e os nomes dos scripts podem ser editados inline com navegação breadcrumb. Os campos agora podem ser definidos como apenas leitura programaticamente através da nova função set\_is\_readonly. Um novo assistente de chat alimentado por IA ajuda no desenvolvimento de scripts, fornecendo respostas em streaming em tempo real.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_script_versioning.png)

*   **API Key Management:**\
    Uma nova página de API Key Management nas configurações de integração permite que os administradores criem, visualizem e giram múltiplas chaves API com cache baseado em Redis para desempenho.

*   **Idea Board:**\
    Uma nova funcionalidade Idea Board permite que os utilizadores submetam, discutam e votem em ideias de funcionalidades e sugestões. O quadro inclui um editor de texto rico com suporte para upload de imagens, comentários e funcionalidade de votação.

*   **Estatísticas de Fornecedores:**\
    Novas vistas de estatísticas de fornecedores fornecem informações sobre métricas de processamento de documentos relacionadas com fornecedores.

*   **Expansão Linguística:**\
    O DocBits agora suporta 22 idiomas, expandido a partir da seleção anterior. O seletor de idioma foi atualizado com um layout de grelha de 4 colunas, e os utilizadores agora podem definir o seu idioma preferido diretamente nas suas configurações de utilizador.

*   **Redesign do Plano de Subscrição:**\
    O seletor de plano de subscrição foi redesenhado com uma exibição melhorada de informações de tokens e uma nova linha de utilização DocNet na tabela de subscrição.

*   **Dual Monitor Mode:**\
    O Dual Monitor Mode foi movido para uma configuração global de utilizador, tornando-o acessível e persistente entre sessões para utilizadores que trabalham com múltiplos ecrãs.

*   **Pesquisa Difusa para Caracteres Alemães:**\
    A funcionalidade de pesquisa agora suporta corretamente caracteres especiais alemães (tremas), garantindo que pesquisas por palavras como "Rechnungsnummer" também correspondam a representações alternativas de caracteres.

*   **Melhorias nas Notificações por Email:**\
    A substituição de parâmetros em modelos de email foi melhorada com melhor validação de destinatários e tratamento de preferências de utilizador.

*   **Rastreamento de Utilização de Créditos:**\
    As organizações podem agora visualizar e rastrear a sua utilização de créditos de IA ao longo do tempo com opções de filtragem, proporcionando melhor visibilidade sobre padrões de consumo.

### Melhorias Gerais:

*   A área de Settings foi redesenhada com uma barra lateral recolhível, subcategorias organizadas e navegação baseada em âncoras para acesso mais rápido. Um painel de ajuda contextual fornece orientação inline, e crachás de rastreamento de estado mostram a completude da configuração de relance.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_settings_redesign.png)

* Documentos com códigos de barras agora dividem-se de forma mais fiável, com melhor tratamento de casos extremos e recuperação de erros.
* A correspondência de PO agora deteta e converte automaticamente preços unitários ao dividir linhas correspondidas, reduzindo correções manuais.
* Os documentos já não ficam presos durante a extração — um novo sistema de rastreamento de estado garante que cada documento progride através do pipeline.
* Quando ocorrem erros de extração, o DocBits agora fornece mensagens de erro mais claras com detalhes passo a passo para ajudar a resolver o problema mais rapidamente.
* O desempenho geral da aplicação foi melhorado com tempos de resposta mais rápidos em todas as telas.
* As regras de Auto Accounting agora suportam filtragem baseada em números para condições de correspondência mais precisas.

### Correções de Bugs:

* Corrigido um problema em que o nome personalizado do painel não estava alinhado com o ícone do painel.
* Corrigido um problema em que o painel exibia colunas que não estavam incluídas na configuração de colunas visíveis.
* Corrigido um problema em que o nome do separador selecionado não era exibido no painel.
* Corrigido um problema em que o popup "Nova versão disponível" aparecia em cada mudança de sub-organização.
* Corrigido um problema em que a configuração de documentos por página não era preservada após atualização da página.
* Corrigido um problema em que a contagem de documentos do painel não atualizava corretamente.
* Corrigido um problema em que os utilizadores recebiam incorretamente a mensagem de erro "O painel já existe".
* Corrigido um problema em que o popup de confirmação de eliminação em massa não era exibido.
* Corrigidos múltiplos problemas com a exibição e o comportamento de gravação de painéis partilhados.
* Corrigido um problema em que as tabelas de documentos não eram exibidas na tela de validação.
* Corrigido um problema em que uma mensagem de erro incorreta era mostrada para ficheiros PDF inválidos.
* Corrigido um problema em que o redimensionador de colunas aparecia atrás dos botões de ação da linha.
* Corrigido um problema em que valores incorretos eram extraídos para montante líquido, montante de imposto e taxa de imposto.
* Corrigido um problema em que as configurações de exportação não podiam ser criadas sem especificar um tipo de documento quando marcado como opcional.
* Corrigido um problema em que um erro de configuração duplicada ocorria ao adicionar novas configurações de exportação.
* Corrigido um problema em que erros ocorriam ao criar múltiplas configurações de exportação.
* Corrigido um problema em que o título da configuração era apagado após selecionar Watchdog como tipo de exportação.
* Corrigido um erro interno do servidor ao criar configurações de exportação Infor.
* Corrigido um problema que impedia o reinício múltiplo de documentos exportados.
* Corrigido um problema em que algumas páginas de configurações não podiam ser encontradas.
* Corrigido um problema em que o link de download do Watchdog retornava um erro.
* Corrigido um problema em que o botão de criação de List of Values não acionava nenhuma ação.
* Corrigido um problema em que as descrições de grupos não eram exibidas.
* Corrigido um problema em que o estado de validação de palavra-passe persistia após cancelar a edição de um utilizador.
* Corrigido um problema em que documentos no estado "Pending Watcher Export" não eram clicáveis.
* Corrigido um problema em que configurações de pesquisa duplicadas podiam ser criadas.
* Corrigido um problema em que a ordenação de utilizadores não funcionava corretamente.
* Corrigido um problema de exibição em que todo o texto da aplicação aparecia em azul.
* Corrigido um problema em que a exibição do formato de idioma era inconsistente.
* Corrigido um problema em que a configuração de idioma aparecia vazia quando nenhuma preferência era selecionada.
* Corrigido um problema em que o uso de maiúsculas/minúsculas do nome da empresa era ignorado.
* Corrigido um problema em que a pesquisa não funcionava para grupos e permissões.
* Corrigido um problema em que a ação de eliminar utilizador não eliminava corretamente o utilizador.
* Corrigido um problema em que os ícones de fluxo de documentos não eram visíveis.
* Corrigido um erro interno do servidor ao guardar modelos de email.
* Corrigido um problema em que variáveis duplicadas eram inseridas nos assuntos dos modelos de email.
* Corrigido um erro ao guardar os detalhes da conta de email de entrada.
* Corrigido um problema em que os documentos ficavam presos no estado "novo" após o carregamento.
* Corrigido um problema em que as colunas de tabela não estavam disponíveis após desativação e reativação.
* Corrigido um problema em que a criação de árvores de decisão falhava para tipos de documentos personalizados.
* Corrigido um problema em que a extração de tabelas não retornava resultados.
* Corrigido um problema em que o tipo de documento CREDIT\_NOTE não era reconhecido corretamente.
* Corrigido um problema em que utilizadores sem direitos de administrador podiam ver todas as tarefas criadas.
* Corrigido um problema em que o popup de sub-organização não fechava após o carregamento de ficheiros por arrastar e soltar.
* Corrigido um problema em que os filtros de período de tempo não eram aplicados corretamente.
* Corrigido um problema com a conversão de data e hora para o formato dos EUA.
* Corrigido um problema em que os fluxos de trabalho eram acionados na ordem errada — a execução de fluxos de trabalho agora usa bloqueio de documentos e prioridades de fila adequados.

## **Release HotFix 2 31 de março de 2026**

### Melhorias do DocBits:

* **Processamento híbrido de PDF — Extração XML controlada pelo utilizador:**\
  Quando um PDF contém dados XML incorporados, os utilizadores podem agora escolher se o DocBits deve usar o XML incorporado para extração ou processar o documento como um PDF padrão. Isto dá às organizações controlo total sobre como os documentos híbridos são tratados, garantindo que o método de extração mais adequado ao seu fluxo de trabalho é aplicado.

* **AP Assignment Code no ecrã de Approval:**\
  A página AP Manager Approval inclui agora um campo de AP Assignment Code, integrado com o Infor M3 CRS620. Isto permite aos aprovadores rever e confirmar os códigos de atribuição diretamente durante o processo de aprovação sem mudar para sistemas externos.

* **Correspondência do total PO com o total do documento:**\
  O DocBits agora suporta a correspondência do total da ordem de compra com o total do documento, fornecendo uma camada adicional de validação durante o PO Matching para detetar discrepâncias mais cedo no processo.

* **Atualização do número de artigo do fornecedor e VPE:**\
  O DocBits agora suporta a atualização dos campos número de artigo do fornecedor e VPE (Verpackungseinheit / unidade de embalagem) durante o processamento de documentos, com os valores sincronizados de volta para o M3 na exportação.

* **Classificação melhorada do layout do documento:**\
  O ID do layout do documento (tfidf_id) é agora gerado apenas com base no texto do cabeçalho, excluindo o texto do rodapé. Isto melhora a precisão da classificação ao impedir que o conteúdo do rodapé influencie a deteção do tipo de documento.

* **Botão Export & Next:**\
  Foi adicionado um novo botão "Export & Next", permitindo aos utilizadores exportar o documento atual e avançar imediatamente para o seguinte na fila, otimizando o fluxo de trabalho de revisão e exportação.

* **Processo de aprovação para faturas de custo:**\
  O processo de aprovação para faturas de custo foi melhorado com lógica de encaminhamento e validação otimizada.

### Correções de bugs:

* Corrigido um problema em que a exportação Infor SFTP falhava com um erro devido a um comando de biblioteca incorreto.
* Corrigido um problema em que as caixas de verificação booleanas não podiam ser exibidas no ecrã de aprovação.
* Corrigido um problema em que mensagens UNMU eram enviadas mesmo quando não havia discrepâncias na unidade de compra.
* Corrigido um problema em que o imposto sobre vendas era incorretamente classificado como encargo no ecrã de PO Matching, resultando num montante pendente negativo.
* Corrigido um problema em que a exportação falhava quando a unidade de compra não estava definida na confirmação de encomenda mas estava presente na ordem de compra.
* Corrigido um problema em que o corpo do e-mail estava em falta em vários documentos.
* Corrigido um problema em que o número de artigo do fornecedor não era visível no ecrã de aprovação e as atualizações não eram enviadas para o M3.
* Corrigido um problema em que a exportação de fornecedores para o Infor retornava um erro.
* Corrigido um problema em que o PO Matching produzia erros durante o processamento.
* Corrigido um problema em que a função `findAll` não funcionava corretamente nos scripts de documentos.
* Corrigido um problema em que a coluna "Updated By" do Watchdog mostrava incorretamente o utilizador Fellow Admin em vez do utilizador real.
* Corrigido um problema em que o BOD-Mapping não podia ser configurado na interface do Watchdog.
* Corrigido um problema em que os encargos eram incorretamente mostrados como montantes pendentes em vez de serem exibidos como encargos.
* Corrigido um problema em que a correspondência automática não funcionava para faturas multi-linha apesar de existir uma configuração de correspondência.
* Corrigido um problema em que um hífen ("-") no número de artigo era considerado durante o PO Matching para a ordem de compra mas ignorado na fatura, causando uma discrepância falsa.
* Corrigido um problema em que tanto ficheiros PDF como XML eram carregados para a pasta de exportação mesmo quando o interruptor "Export PDF" estava desativado.
* Corrigido um problema em que um estado em falta no cartão de workflow impedia os documentos de progredir através do fluxo de trabalho.
* Corrigido um problema em que a qualidade do documento estava significativamente degradada após a importação.
* Corrigido um problema em que o ecrã PO Match gerava um erro ("Cannot read properties of null").
* Corrigido um problema em que a lista de valores predefinida não podia ser editada.
* Corrigido um problema em que o workflow não conseguia ler o estado do campo corretamente, causando encaminhamento incorreto.
* Corrigido um problema em que as importações de e-mail de entrada falhavam com um erro.
* Corrigido um problema em que linhas em falta não chegavam corretamente ao M3 durante a exportação.
* Corrigido um problema em que faturas codificadas e aprovadas ocasionalmente não eram atualizadas para o estado "aprovado" no M3 através da API APS110.
* Corrigido um problema com a configuração Multi Banking que não funcionava corretamente.
* Corrigidos múltiplos problemas com a exibição e o comportamento de gravação de dashboards partilhados.
* Corrigido um problema em que o campo número de artigo do fornecedor estava limitado a 30 caracteres, impedindo o armazenamento de valores mais longos.
* Corrigido um problema em que os valores de preço unitário e preço unitário por unidade causavam um erro durante a exportação.
* Corrigido um problema em que linhas de PO com um estado excluído (por ex. "Closed") ainda podiam ser arrastadas e correspondidas no ecrã de PO Matching apesar de estarem excluídas pelas regras de correspondência.

### Alterações de configuração:

* Modelos de e-mail atualizados para remover o botão "Go to Task".
* Ajustados os scripts e as configurações de campos obrigatórios nos elementos de custo.

## **Release HotFix 1 16 de março de 2026**

### Melhorias do DocBits:

* **Histórico de documentos na exportação SFTP:**\
  O DocBits agora suporta a inclusão do histórico completo do documento como parte do payload XML exportado ao exportar para SFTP. Esta funcionalidade é configurável através das Export Settings e fornece aos sistemas a jusante um registo de auditoria completo de cada alteração de estado e ação executada num documento no DocBits — incluindo quem fez a alteração, quando ocorreu e quais eram os estados anterior e atual. Isto é particularmente valioso para conformidade, rastreabilidade e análise operacional.
* **Atualização de encargos na confirmação de encomenda para Infor On Premise:**\
  Os clientes Infor On Premise podem agora processar confirmações de encomenda que incluem encargos diretamente no DocBits. Os encargos são completamente atualizados através da exportação, tornando o processo de confirmação de encomenda de ponta a ponta fluido e removendo a necessidade de ajustes manuais a jusante.
*   **Aplicar Layout predefinido a todos os Origins:**\
    Um novo botão **Apply Default Layout to Origins** foi introduzido no ecrã de configuração de layout. Os administradores podem agora enviar o layout predefinido para todos os origins dentro de uma organização numa única ação, eliminando o moroso processo manual de copiar e colar JSON de layout para cada origin individualmente. Isto é especialmente útil durante a integração de novos clientes onde múltiplos origins necessitam de ser configurados de forma consistente.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(5).png)
*   **Seleção de tipo de documento para importação FTP:**\
    As configurações de importação FTP agora suportam a atribuição de tipo de documento por pasta. Ao configurar uma importação FTP, os utilizadores podem especificar qual tipo de documento — como Fatura ou Confirmação de Encomenda — deve ser aplicado a todos os documentos importados dessa pasta. Os documentos são automaticamente classificados na importação, removendo a necessidade de atribuição manual do tipo de documento após a ingestão. Isto suporta organizações que gerem múltiplos tipos de documento através de diferentes suborganizações e pastas.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(4).png)
* **Exportação para GLS840 para Infor On Premise:**\
  O DocBits agora suporta a exportação de documentos para o programa GLS840 para clientes Infor On Premise, expandindo a gama de destinos de exportação suportados para ambientes on-premise.
*   **Melhorias de interface para Watchdog e configuração de exportação:**\
    Os ecrãs de configuração do Watchdog e de configuração de exportação foram atualizados com uma interface de utilizador melhorada, oferecendo um layout mais limpo e uma experiência mais intuitiva para os administradores que gerem estas configurações.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(1).png)

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(2).png)

### Correções de bugs:

* Corrigido um problema em que os utilizadores com direitos de visualização válidos não conseguiam ver documentos — a lógica de permissões foi reestruturada com uma verificação de nível de acesso substituindo a abordagem anterior de filtragem baseada em grupos.
* Melhorado o tratamento de exceções em múltiplas áreas da aplicação para maior estabilidade.
* Resolvido um problema em que colunas de tipo booleano não eram tratadas corretamente durante a extração de campos.
* Corrigido um problema de autenticação assíncrona no endpoint de carregamento de ficheiros.
* Resolvidos problemas de exibição da interface para a tabela PO no ecrã de validação.
* Atualizado o modelo de script para incluir comentários de rastreamento de alterações para melhor auditabilidade.
* Corrigido um problema com campos dropdown que não se comportavam corretamente no ecrã de validação.
* Corrigido um problema em que o campo de suborganização não estava pré-preenchido ao atualizar as atribuições de documentos a partir do dashboard.

## **Lançamento Winter Summit 10 de dezembro de 2025**

### Melhorias do DocBits:

*   **Personalização aprimorada de regras de correspondência de OC:**\
    O DocBits agora fornece controle mais granular e personalizável sobre regras de correspondência de ordens de compra. Os administradores podem configurar com precisão quais colunas devem ser avaliadas durante o processo de correspondência para cada tipo de documento, garantindo que apenas os campos mais relevantes sejam considerados. Além disso, as tolerâncias podem ser definidas no nível da coluna, permitindo maior flexibilidade ao lidar com discrepâncias menores. Cada regra também pode ser configurada para aplicar-se à correspondência manual, correspondência automática ou ambas, dando às equipes a capacidade de adaptar o fluxo de trabalho de correspondência aos seus requisitos operacionais exatos. Essas melhorias aumentam significativamente a adaptabilidade e precisão do processo de correspondência de ordens de compra.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_3.png)
*   **Suporte para múltiplas contas financeiras de fornecedores:**\
    O DocBits agora oferece suporte ao gerenciamento de múltiplas contas financeiras para fornecedores por meio do RemitToPartyMaster BOD fornecido pela Infor. Essa melhoria permite que as organizações mantenham vários registros de contas de remessa para um único fornecedor, melhorando a flexibilidade e a precisão no processamento de pagamentos. Uma nova definição de configuração foi introduzida para habilitar ou desabilitar esse recurso, permitindo que os administradores ativem a funcionalidade com base em suas necessidades operacionais.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_1.png)
*   **Adicionado acesso de usuário aos resultados de extração OCR:**\
    O botão **Visualização OCR** na tela de validação de campo agora está disponível para todos os usuários que têm acesso de validação, em vez de ser limitado aos administradores. Com esta atualização, qualquer usuário autorizado pode revisar os resultados de extração OCR diretamente, facilitando a validação da precisão dos dados e o monitoramento do desempenho geral do OCR. Essa melhoria promove maior transparência e melhora a eficiência do fluxo de trabalho de validação.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_2.png)
* **Renderização dinâmica de colunas em telas de aprovação:**\
  Visualizações de aprovação aprimoradas para exibir dinamicamente apenas as colunas configuradas para comparação nas preferências de banco de dados de cada organização. Anteriormente, algumas colunas específicas da organização apareciam vazias quando não estavam configuradas para comparação, causando confusão. Agora, as visualizações de aprovação mostram apenas campos que estão sendo ativamente comparados. Isso fornece telas de aprovação mais claras e específicas da organização sem colunas vazias ou irrelevantes.
* **Campo de tipo de pedido adicionado à pesquisa de dados mestre**:\
  A lista de cabeçalho de ordem de compra agora inclui uma coluna "Order Type" na pesquisa de dados mestre, fornecendo recursos adicionais de categorização.
* **Melhorias no painel de filtros personalizados:**\
  A funcionalidade de compartilhamento de painel foi aprimorada para fornecer maior flexibilidade aos usuários compartilhados. As pessoas que têm painéis compartilhados com elas agora podem ajustar e editar os filtros do painel, permitindo que adaptem as informações exibidas às suas necessidades específicas. Essa melhoria oferece suporte a uma experiência de visualização mais personalizada e interativa, garantindo que os usuários possam refinar facilmente os insights de dados mais relevantes para suas tarefas.
* **Prefixos personalizáveis para colunas de tela de aprovação:**\
  Uma nova opção configurável foi introduzida para exibir prefixos antes das colunas de documentos nas telas de aprovação. Esse recurso pode ser gerenciado diretamente dentro do construtor de layout, dando aos administradores controle total sobre se os prefixos são exibidos e a quais tipos de documentos se aplicam. Ao habilitar esta opção, os usuários obtêm contexto mais claro e melhor legibilidade ao revisar documentos durante o processo de aprovação.

### Melhorias gerais

* Melhorado o registro de erros para tabelas mal treinadas na extração de tabelas.
* Adicionado um limite de compartilhamento para painéis de até 10 usuários ou 5 grupos, juntamente com uma mensagem de erro clara quando o limite é atingido.
* Melhorado o tratamento de erros para painéis personalizados quando um usuário tenta criar um painel com um nome que já existe.

### Correções de Bugs:

* Corrigido um problema em que emails pareciam ser enviados com sucesso na seção Detalhes do Fornecedor, mas não eram entregues aos destinatários.
* Corrigido um problema em que campos suspensos adicionados às telas de aprovação/rejeição não eram exibidos.
* Corrigido um problema em que todos os documentos exportados eram marcados como atualizados por último pelo usuário errado.
* Corrigido um problema em que documentos mostravam o status "Fluxo de trabalho em andamento", mas nenhum fluxo de trabalho era executado e o registro permanecia vazio.
* Corrigido um problema em que usuários não relacionados eram atribuídos aos documentos no momento da exportação sem realizar nenhum trabalho neles.
* Corrigido um problema em que usuários com permissões corretas não podiam rejeitar documentos atribuídos e recebiam erros.
* Corrigido um problema em que os ícones de fluxo de documentos não eram exibidos para algumas organizações.
* Corrigido um problema em que um popup aparecia ao carregar documentos com arrastar e soltar no painel.
* Corrigido um problema em que as flags E-TEXT eram exibidas como ativadas na interface do usuário, embora a resposta da API mostrasse todos os valores como falsos.
* Corrigido um problema em que ocorria um erro ao carregar documentos contendo páginas em branco.
* Resolvido um problema em que hiperlinks de tarefas em notificações por email não redirecionavam os usuários para a tela de aprovação correta.
* Resolvido um problema em que selecionar a sub-organização cross fazia com que a Pesquisa de Dados Mestre não mostrasse nenhum fornecedor. Os usuários agora podem visualizar corretamente os dados de fornecedores entre organizações.

## Release Autumn Summit 22 de outubro de 2025

### Melhorias no DocBits:

*   #### Aperfeiçoamentos no Design do Modelo de Email:

    O editor de modelos de email foi redesenhado para fornecer uma estrutura mais clara e uma experiência mais suave. Selecionar campos de documento agora é mais intuitivo, e anexos podem ser incluídos diretamente nos modelos. Essas melhorias tornam mais rápido e fácil criar emails profissionais e personalizados.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fdv4oDlfkRyD0W9yWGAA4%252Fimage.png%3Falt%3Dmedia%26token%3D14bf7ebd-d886-4758-8184-d7b94447518a\&width=768\&dpr=4\&quality=100\&sign=88405d9c\&sv=2)
*   #### Aperfeiçoamentos no Painel de Controle:

    O painel de controle foi expandido para melhorar a navegação e a personalização. Com novas abas, os usuários podem alternar mais rapidamente entre diferentes tipos de documentos, reduzindo o tempo gasto procurando a visualização correta.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FmpO7WSIrkL0I8Rje3HQt%252Fimage.png%3Falt%3Dmedia%26token%3D77d03fe7-e626-4645-b191-e332715a25fb\&width=768\&dpr=4\&quality=100\&sign=93fa9925\&sv=2)
*   #### Painéis de Filtro Personalizados:

    Além disso, os painéis de controle agora podem ser personalizados e filtrados de acordo com as preferências individuais. Esses painéis personalizados também podem ser compartilhados com colegas, facilitando a criação de visualizações de relatórios consistentes em toda a equipe.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fn5rPvGnRltT3mTIDoJwV%252Fimage.png%3Falt%3Dmedia%26token%3D22d065e3-81eb-4f16-828c-7f9134c25b1b\&width=768\&dpr=4\&quality=100\&sign=eb11d3a3\&sv=2)
*   #### Logs de Notificações por Email:

    Um novo recurso de registro está disponível para todas as notificações por email. Os usuários agora podem revisar um histórico de notificações enviadas, facilitando a verificação de entregas e a resolução de problemas caso os emails não sejam recebidos.
*   #### Suporte a Fatura Eletrônica: e-SLOG 1.6 & 2.0:

    Foi introduzido suporte para formatos adicionais de fatura eletrônica. O sistema agora pode processar e gerar versões e-SLOG 1.6 e 2.0, expandindo a compatibilidade com parceiros e requisitos regulatórios.
*   #### Aperfeiçoamentos na Detecção de Duplicatas:

    A detecção de duplicatas foi aprimorada com duas opções de configuração poderosas. O **Intervalo de Detecção de Duplicatas** permite que você defina um intervalo de tempo para verificar duplicatas com mais precisão, enquanto a configuração **Impedir Exportação de Duplicatas** impede automaticamente a exportação de documentos detectados como duplicatas. Juntos, esses aprimoramentos oferecem mais controle e garantem uma maior precisão dos dados.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXHRKTmuSxTlDt9lDEkE7%252Fimage.png%3Falt%3Dmedia%26token%3D96b56af6-c644-4b0f-a488-8bc16a03c11f\&width=768\&dpr=4\&quality=100\&sign=9b723b7f\&sv=2)
*   #### Aperfeiçoamentos na Árvore de Decisão:

    As árvores de decisão agora são mais versáteis, com a capacidade de retornar valores de campos de documento. Isso permite lógica de automação mais avançada, possibilitando que os fluxos de trabalho tomem decisões com base em dados reais do documento.
*   #### Novos Cartões de Fluxo de Trabalho:

    Dois novos cartões de fluxo de trabalho expandem as capacidades de automação. O primeiro permite verificar se um documento pertence a uma sub-organização específica, facilitando o manuseio de configurações multi-entidades. O segundo introduz uma verificação de tolerância de data de entrega, que compara datas de entrega com a data atual em dias úteis para ajudar a gerenciar e aplicar requisitos de entrega de forma mais eficaz.
*   #### Melhorias na Exportação CSV:

    O recurso de exportação CSV foi significativamente aprimorado. Em vez de exportar apenas os documentos exibidos na página atual, o sistema agora exporta todos os documentos em um conjunto de dados. Cada exportação cria uma entrada de log, e o CSV resultante é enviado automaticamente por email, proporcionando um processo de exportação mais completo e confiável.
*   #### Período de Exclusão de Ordem de Compra:

    Uma nova opção de configuração permite que os administradores definam um período de tempo para a exclusão de ordens de compra. Essa melhoria adiciona flexibilidade e controle sobre as políticas de retenção de dados, garantindo que as ordens de compra sejam removidas apenas quando apropriado.

### Correções de Bugs

* Corrigido um problema em que dados antigos eram incluídos ao exportar documentos.
* Corrigido o filtro para Erros de Exportação, que anteriormente mostrava outros status também.
* Resolvida uma incompatibilidade de validação de tabela em que “Preço Unitário” disparava erros, mas “Preço Unitário Por” não, apesar dos valores estarem corretos.
* Corrigido um problema em que adicionar uma nova coluna ao painel de controle falhava.
* Corrigido um problema em que as tarefas não eram visíveis na coluna de tarefas do painel de controle.
* Corrigido o comportamento de classificação aleatória para que as listas sigam agora uma ordem consistente.
* Resolvido um problema em que a alteração do tamanho da coluna não podia ser interrompida.
* Corrigido um bug que impedia a correspondência manual de linhas na tela de Correspondência de PO.
* Corrigido um problema em que a opção de anexo de email era redefinida após salvar.
* Corrigido um problema em que a contabilidade automática exibia IDs de banco de dados inicialmente.
* Corrigido o comportamento de campo difuso para que os valores não sejam mais sobrescritos incorretamente.
* Corrigido um problema em que os campos na conta automática desapareciam após excluir o conteúdo.
* Corrigido um bug em que o usuário não conseguia renomear “Nome” e “Sobrenome” na janela de configurações.
* Resolvido um problema em que os documentos podiam ficar presos em “fluxo de trabalho em andamento”.
* Corrigido um problema de cor de ícone de menu em que as cores de organização selecionadas não eram aplicadas corretamente.
* Corrigido um problema em que os códigos QR às vezes não eram reconhecidos.
* Corrigido um problema em que as contas não podiam ser removidas com a tecla de retrocesso para inserir uma diferente.
* Resolvido um problema de mistura de idiomas após o login após a atualização de produção.

## Lançamento Spring Bloom – 23 de Abril de 2025

### Melhorias no DocBits:

* **Opção de Filtro para o Log de Importação de Email:** Os usuários agora têm a capacidade de filtrar os logs de importação e classificar a tabela para uma visão mais clara e eficiente. Essa melhoria agiliza o processo de identificação e gerenciamento de entradas de email, melhorando a solução de problemas e o gerenciamento geral de logs.
* **Suporte Multilíngue para Lista de Valores:** Expandimos as capacidades multilíngues para o recurso Lista de Valores. Os administradores agora podem definir rótulos em vários idiomas, garantindo que o rótulo correto seja exibido automaticamente com base nas configurações de idioma do sistema do usuário. Essa melhoria promove maior acessibilidade e localização, facilitando a interação dos usuários em todo o mundo com a plataforma em seu idioma nativo.
* **Melhorias nos Detalhes do Usuário nas Configurações:** A interface de configurações agora exibe informações abrangentes do usuário. Os administradores podem facilmente visualizar afiliações a grupos, detalhes de sub-organizações e dados adicionais importantes, permitindo uma melhor gestão dos papéis dos usuários e uma compreensão mais clara das estruturas da equipe.
* **Informações de Contabilidade Automática na Tela de Aprovação:** A tela de aprovação agora apresenta detalhes de contabilidade automática juntamente com as informações da fatura. Essa melhoria fornece uma visão mais profunda dos dados da transação, facilitando processos de revisão mais suaves e uma tomada de decisão mais informada em relação às faturas.
* **Contador de Tarefas para Documentos na Visualização do Painel:** Documentos no painel agora podem indicar tarefas abertas associadas a eles e exibir o número total de tarefas pendentes. Este recurso fornece aos usuários uma visão rápida das ações pendentes, melhorando a gestão de tarefas e a eficiência do fluxo de trabalho.
* **Seleção de Modelo de IA Baseada em Fornecedor:** Os usuários agora podem selecionar o modelo de IA usado para extração de dados com base em cada fornecedor. Esta melhoria permite uma otimização mais precisa, garantindo melhor precisão na extração para diferentes fornecedores e melhorando os resultados gerais do processamento de dados.
* **Registros de Fluxo de Trabalho Aprimorados para Cartões de Árvore de Decisão:** Os registros agora exibem a saída da árvore de decisão, facilitando o acompanhamento e a compreensão de como as decisões foram tomadas dentro dos fluxos de trabalho.
*   **Introdução de um Novo Setup de Testes Automáticos para Melhorar a Funcionalidade e Estabilidade do Sistema:**

    Estamos empolgados em anunciar a implementação de um novo sistema de testes automatizados projetado para melhorar a funcionalidade e a confiabilidade geral de nossa plataforma. Esse novo setup realizará verificações consistentes e abrangentes em nosso sistema para identificar quaisquer problemas antes que eles impactem sua experiência. Ao automatizar esses testes, podemos garantir respostas mais rápidas a problemas potenciais e manter os mais altos padrões de qualidade para nosso sistema.

    ​

### Correções de Bugs

* Resolvido um problema onde as tarefas não apareciam na tela de validação/aprovação.
* Corrigida a posição do botão Próximo/Anterior para que permaneça estático.
* Corrigidos problemas de rolagem nas visualizações de script e árvore de decisão, garantindo que os botões de ação permaneçam estacionários durante a rolagem.
* Removido o campo de país de origem das faturas eletrônicas.
* Corrigido um problema com o contador de tarefas exibindo um número impreciso de tarefas.
* Adicionadas traduções ausentes.
* Corrigidos campos personalizados para exibir nomes descritivos em vez de IDs.
* Atualizada a lista de atalhos para a tela de correspondência de PO.
* Resolvido um problema onde documentos eram baixados com um nome de arquivo incorreto.
* Corrigidas inconsistências de ordenação na tabela de linhas de fatura dentro da correspondência de PO.
* Corrigido um problema que afetava a funcionalidade de criação de tarefas.
* Corrigido um problema na correspondência de PO onde a ordenação da tabela de faturas seria redefinida ao corresponder uma linha.
* Resolvidos problemas de contabilidade automática garantindo que referências de booking sejam divididas corretamente quando um valor é dividido.
* Atualizadas as informações do host ClickHouse.
* Resolvido um problema onde documentos duplicados não eram reconhecidos como duplicados.
* Corrigidos problemas de exportação causados por referências de booking que eram muito longas.
* Resolvido um problema onde checkboxes somente leitura não eram somente leitura.
* Corrigido um problema onde os usuários podiam ser adicionados a uma sub-organização duas vezes.
* Corrigido um problema onde mudar a sub-organização de um documento fazia com que o usuário ou grupo atribuído fosse redefinido.

​

## Correção Rápida de Lançamento Inverno Frost 10 de Abril de 2025

### Melhorias no DocBits:

* **Função de Script `set_column_date_value` Aprimorada:** A função `set_column_date_value` agora inclui suporte para a opção `skip_weekend`, permitindo que os valores de data pulem automaticamente os finais de semana quando aplicados.
* **Suporte Aprimorado para Upload de Arquivos:** Arquivos PNG e JPEG agora podem ser carregados diretamente e são automaticamente convertidos para o formato PDF para um manuseio de documentos mais eficiente.
* **Atualizações na Funcionalidade de Watchdog:**
  * Agora suporta exportação para **Enaio** para melhor integração do sistema.
  * Capacidades de análise aprimoradas para extrair informações de estruturas XML `Sync.ContentDocument`, permitindo um processamento de dados mais eficiente.

### Correções de Bugs

* Corrigido um problema em uma função de script.
* Resolvido um problema onde os pedidos de compra tinham um status incorreto após serem atualizados.

## Lançamento Hot Fix Winter Frost 11 de Março de 2025

### Melhorias no DocBits:

* **Extração de Dados Aprimorada:** Adicionada uma opção para extrair o **Número do Pedido de Compra** ou **Número do Item** de uma linha acima ou abaixo.
* **Acesso Expandido a Sub-Organizações Cruzadas:** Usuários não administradores agora também podem acessar o recurso **Sub-Organizações Cruzadas**.

### **Correções de Bugs:**

* Corrigido um problema onde usuários não podiam ser adicionados a um grupo.
* Corrigido um problema com falhas na importação de e-mails.
* Resolvido um problema com o treinamento de campo em documentos com mais de uma página.
* Corrigido um problema onde scripts não funcionavam corretamente.
* Resolvido um problema onde os dados do documento não eram exibidos corretamente.
* Corrigido um problema com a configuração de atualização automática do pedido de compra.
* Corrigido um problema onde os tokens de assinatura eram exibidos incorretamente.
* Resolvido um problema onde a tela de tarefas exibia uma versão desatualizada do documento.
* Corrigido um problema que fazia com que os documentos não mudassem seu status.
