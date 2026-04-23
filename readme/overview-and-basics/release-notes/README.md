# Notas de versão

## **Release R1.0 12/13 de maio de 2026**

> **Disponibilidade no Sandbox:** 28 de abril de 2026

### Novas funcionalidades:

* **Activity Logging / Access Audit:**\
  Registo detalhado de atividade e trilha de auditoria de acessos em toda a aplicação, para conformidade e monitorização. Diferentes tipos de logging para todos os microsserviços e baseados em intervalo de tempo.

* **Pesquisa rápida global:**\
  Pressione Cmd+K / Ctrl+K a partir de qualquer parte da aplicação para pesquisar em mais de 200 rotas e em mais de 40 funcionalidades dentro das páginas. Mostra os 8 melhores resultados com correspondência difusa (fuzzy), navegação por setas e links para a App Index Page completa.

* **Sitemap (App Index Page):**\
  Página de índice pesquisável que cataloga cada página navegável e cada funcionalidade dentro de página (diálogos, barras laterais, painéis) no DocBits. Organizada em 18 categorias com filtros por tipo, pills de categoria, pesquisa sincronizada por URL e entradas com controlo de permissões apresentadas como bloqueadas para utilizadores não-administradores.

* **Analytics Dashboard:**\
  Análises abrangentes de processamento de documentos com Executive Overview, API Metrics, Quality Metrics, Processing Performance, Document Flow Analytics, Activity Log, Event Log e Audit Trail.

* **Funcionalidade de exportação do dashboard:**\
  Nova funcionalidade de exportação do dashboard que permite a exportação de listas em formato CSV ou XLSX.

* **Full-Text Search / DocSearch:**\
  Pesquisa vetorial baseada em IA em todos os documentos indexados, com filtragem de fornecedores em tempo real, funcionalidade "Find Similar" e definições de indexação configuráveis.

* **Supplier Delivery Statistics:**\
  Novas vistas que fornecem informações sobre métricas de processamento de documentos relacionadas com fornecedores.

* **Debug Collector:**\
  Pressione Ctrl+Shift+P para capturar um snapshot completo de depuração, incluindo chamadas API, estado do WebSocket, erros, logs de consola, métricas de desempenho e informação de ambiente. Os snapshots podem ser copiados para a área de transferência ou enviados diretamente como ticket de suporte com um relatório em formato HTML e um ficheiro JSON anexado.

* **AI Agents (DocNet):**\
  Agentes autónomos em segundo plano que processam automaticamente os e-mails recebidos — classificando, extraindo e encaminhando documentos sem intervenção manual. Os agentes trabalham de forma independente nas tarefas atribuídas e escalam aos utilizadores através de pedidos de aprovação sempre que é necessário julgamento humano. Inclui um dashboard dedicado para monitorizar atividade e desempenho dos agentes.

* **Novos E-Documents:**\
  Mais de 80 novos tipos globais de e-invoice e mais de 40 novos formatos, incluindo XRechnung 3.0.2, ZUGFeRD 2.2/2.3.2, variantes Factur-X e Asia-Pacific PINT Credit Notes. 100 % de cobertura de classificação e extração.

* **AI Script Chat:**\
  Assistente de chat baseado em IA para o desenvolvimento básico de scripts, com respostas em streaming em tempo real.

* **Script Versioning:**\
  Histórico completo de versões para scripts, com rastreamento de alterações, comparação e capacidades de restauração. Fornece gestão de versões para scripts semelhante à forma como as versões dos E-Docs são mantidas.

* **Histórico de exportação nas Dashboard Actions:**\
  Acesso ao histórico de exportação de um documento diretamente a partir do menu de ações do dashboard.

* **Generic API Exporter (APS450, GLS840):**\
  Destino de exportação API genérico configurável através de uma configuração Mapping-File, para integração flexível com sistemas externos. Foi implementado suporte para APS450 e GLS840.

* **Múltiplas configurações de exportação:**\
  Suporte para múltiplas configurações de exportação ativas por tipo de documento, com ordem de execução e um botão de re-exportação para reexecutar a partir do passo que falhou.

* **Nova versão do Watchdog:**\
  Remodelação completa da página WatchDog Settings. Foram adicionadas novas funcionalidades de conforto, incluindo o WatchDog Status atual, guia e comandos para instalação, configuração de templates XSLT e uma definição para atualização automática. Foi também implementada a funcionalidade que permite ao WatchDog gerir várias configurações em simultâneo.

* **Integração com Vertex:**\
  Integração Consumer Use Tax através da Vertex para cálculo automatizado de impostos e conformidade durante o processamento de documentos.

* **Remodelação da UI e reorganização das definições:**\
  Renovação abrangente da UI em toda a aplicação. Páginas de login e autenticação remodeladas. Área de definições remodelada, com barra lateral recolhível, subcategorias organizadas, navegação baseada em âncoras, painel de ajuda contextual e badges de acompanhamento de estado. Alterações à UI dos Document scripts. Nova UI para Document flow. UI melhorada de List of Values.

* **Idea Board:**\
  Quadro de pedidos de funcionalidades onde os utilizadores podem submeter, discutir e votar em novas funcionalidades, melhorias, correções de bugs necessárias, etc., com editor de texto enriquecido e suporte para imagens.

* **API Key Management:**\
  Página de definições dedicada à criação, visualização e gestão de várias chaves API.

* **Funcionalidade de pesquisa em Master Data Lookup:**\
  Capacidade de pesquisa de Master Data melhorada, oferecendo opções de pesquisa adequadas com base nos campos selecionados.

* **User Activity Chart:**\
  Gráfico visual que mostra padrões de atividade dos utilizadores e métricas de engagement. Dashboard de atividade de login com gráficos comparativos de tendências, agregação diária/semanal e geolocalização baseada em GeoLite2.

* **User Login History:**\
  Users Detail View com histórico de login.

* **Barra lateral personalizável:**\
  Reordenação por drag-and-drop, alternância mostrar/ocultar e fixar no topo para os itens de menu da barra lateral. As preferências são guardadas por utilizador com uma opção "Reset to default". Respeita as feature flags.

* **Video Carousel:**\
  Carousel de vídeo com reprodução automática na página prepare-dashboard, apresentando vídeos animados curtos com dicas de produto (Global Search, Keyboard Shortcuts, Document Upload, Table Customization). Disposição em duas colunas, com os vídeos à esquerda e a preparação do dashboard à direita. O redirecionamento automático é pausado enquanto os utilizadores navegam pelos vídeos.

* **Advanced Workflow Designer:**\
  Construtor de automação visual baseado em nós, com canvas drag-and-drop para pipelines de processamento multietapa. Suporta wait steps, caminhos paralelos, templates reutilizáveis, Or condition cards, botão manual de test/run, execução parcial "Test from Here" e registos de execução por nó com realce visual do fluxo que mostra exatamente quais nós foram executados.

* **Workflow KPI Dashboard:**\
  Dashboard de métricas-chave para monitorizar a execução de workflows.

* **Workflow Partner Card SDK:**\
  SDK para programadores externos criarem cartões de workflow personalizados, com revisão baseada em IA, validação em sandbox e documentação de introdução.

* **Workflow Test Manager:**\
  Gestor de testes automatizados para workflows, permitindo aos administradores criar e executar testes individualmente ou em massa.

### Melhorias:

* **Base de dados (todos os módulos) — Migração de colunas ID:**\
  Todas as colunas "ID" da base de dados do DocBits foram migradas internamente de strings para um tipo ID dedicado (UUID7). A base de dados Postgres subjacente foi migrada para V18 para suportar esta melhoria.

* **Processamento de documentos — Melhorias adicionais:**\
  Alteração da lógica de exportação relacionada com o número máximo de páginas a considerar — o documento completo será agora exportado. Durante a validação do documento, o utilizador terá a opção de substituir o limite máximo de páginas predefinido para esse documento específico. O cálculo do Pending Document Counter foi melhorado.

* **Versões, estado e data de implementação dos serviços:**\
  O estado de disponibilidade dos serviços é fornecido no popup "Service Versions".

* **Expansão de idiomas:**\
  Suporte expandido para 22 idiomas, com seletor de idioma atualizado.

* **Design do Access Control ao nível do campo:**\
  Controlo de acesso redesenhado/melhorado, com estado de ativação mais claro, acesso ao nível do campo, gestão consistente de regras e permissões simplificadas baseadas em grupos. Corrige conflitos de regras entre Access Control e View Permissions, mostra o proprietário da importação na UI e aplica o controlo de acesso de forma consistente à validação de campos, às tabelas extraídas por IA e a todas as vistas.

* **Activity Stream para todos os ecrãs:**\
  O Activity Stream está agora disponível em todos os ecrãs de processamento de documentos (Ready for Validation, PO Matching, Accounting, Quote Details, Reject) — não apenas em Pending Approval. Movido para uma posição consistente no painel direito em todos os ecrãs.

* **Página Document Flow:**\
  Página dedicada à visualização e acompanhamento do fluxo de processamento de documentos, mostrando transições de estado e progresso através da pipeline.

* **Dual Monitor Mode (definição global do utilizador):**\
  Dual Monitor Mode movido para uma definição global do utilizador, persistente entre sessões.

* **Melhorias no Layout Builder:**\
  Suporte para campos ocultos e apenas de leitura com indicadores visuais, divisor de painel redimensionável e definições de comprimento de campo. Aplique o Default Layout a múltiplos Origins sem ter de visitar cada um individualmente.

## **Release HotFix 3 16 de abril de 2026**

### Melhorias do DocBits:

* **Extração de códigos QR para faturas polacas:**\
  O DocBits suporta agora a extração de códigos QR especificamente para faturas polacas, melhorando a captura automatizada de dados para documentos originários da Polónia.

### Correções de bugs:

* Corrigido um problema em que a exportação automática falhava quando o PO Matching já tinha ocorrido, mas a ordem de compra não estava associada ao documento.
* Corrigido um problema em que os preços unitários eram arredondados incorretamente para faturas com unidades de embalagem (Verpackungseinheiten / VPE).
* Corrigido um problema em que as mensagens de erro de exportação do ION/MEC (por ex., falhas do Acknowledge.PurchaseOrder) não eram apresentadas no DocBits, exibindo o estado "Exported" apesar de a exportação ter falhado.
* Corrigido um problema em que o preço unitário no ecrã de aprovação estava incorreto quando se utilizava a extração de tabelas por IA.
* Corrigido um problema em que o script Total Matching gerava um erro no ecrã de validação.
* Corrigido um problema em que o processamento de documentos falhava com um erro ("UserAuthentication object has no setter for 'org_id'").
* Corrigido um problema em que o treino de tabelas não funcionava para fornecedores específicos — as colunas iam parar a colunas ocultas em vez dos campos mapeados.
* Corrigido um problema em que o PO Matching falhava em faturas grandes (mais de 10 páginas) devido a se ter excedido o limite de tamanho do pedido multipart.
* Corrigido um problema em que os valores de colunas preenchidos por scripts não eram mantidos após um reinício do documento.
* Corrigido um problema em que o toggle "Ignore Table Validation" aparecia como ativo (verde) na UI, mas estava, na realidade, desativado em segundo plano.
* Corrigido um problema em que a qualidade do documento era significativamente degradada após a importação.
* Corrigido um problema em que as versões dos microsserviços e as datas de implementação apresentadas na aplicação eram inconsistentes entre ambientes após uma implementação completa.
* Corrigido um problema em que a extração de código de barras falhava devido a um erro na construção do objeto de autenticação do utilizador a partir dos dados da tarefa.
* Corrigido um problema em que os dados de contacto do fornecedor eram esvaziados ao guardar no Supplier Portal.
* Corrigido um problema em que os documentos sofriam um erro NoneType durante a exportação.
* Corrigido um problema em que o corpo do e-mail não era incluído quando o primeiro ficheiro anexado era uma imagem PNG ou JPEG.
* Corrigido um problema em que o corpo do e-mail estava em falta em vários documentos.
* Corrigido um problema em que o DocBits Operator "ai-exporting" não produzia resultados de exportação nos sistemas de destino (LN/D3).

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
