# Configurações

![Settings Overview](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_overview.png)

A área de Configurações (**Settings**) é o ponto central para configurar o DocBits. Ela está organizada em cinco seções principais:

## 1. Organização e acesso

Gerencie o perfil da sua empresa e controle quem pode acessar o quê.

* **Company Information**: Informe o nome da empresa, endereço, número de identificação fiscal e outros identificadores legais.
* **Users**: Adicione, edite ou desative contas de usuário e atribua funções (Admin, System Admin).
* **Sub-Organizations**: Crie e gerencie suborganizações para estruturas com várias entidades.
* **Groups and Permissions**: Defina grupos de usuários e configure permissões detalhadas para cada grupo.

## 2. Processamento de documentos

Configure como os documentos são importados, processados e exportados.

* **Documents Expiry**: Defina regras de exclusão automática de documentos (por exemplo, excluir após 48 horas, 1 semana etc.).
* **Document Types**: Defina e configure os tipos de documento que o DocBits processa (faturas, pedidos, notas de entrega etc.), incluindo campos, colunas de tabela, scripts e muito mais.
* **Import**: Configure como os documentos entram no DocBits — por e-mail (IMAP/Office 365), FTP ou upload de arquivos. Configure tipos de arquivo e limites de páginas.
* **Rule Management**: Defina regras de resolução de conflitos para a conciliação entre faturas e pedidos de compra (PO), incluindo configurações de tolerância e fluxos de aprovação.
* **OCR Settings**: Configure os limites de qualidade do reconhecimento óptico de caracteres (OCR), o uso de E-Text, a versão do AI OCR e o comportamento da extração de tabelas.
* **Classification and Extraction**: Configure a divisão de documentos, a formatação de valores, os métodos de extração de tabelas, as regras de classificação e os modelos de IA.
* **Lookup Master Data**: Configure como os dados extraídos são validados com os dados mestres do seu sistema ERP (por exemplo, contas de fornecedores, pedidos de compra).
* **List of Values**: Crie e gerencie listas de valores predefinidos usadas em menus suspensos e na validação de dados.
* **Export**: Configure como e para onde os documentos processados são enviados — via Webhook, SFTP, SMB ou integrações Infor (IDM, ION, M3, LN).
* **Module**: Ative ou desative funcionalidades opcionais, como PO Dashboard, Auto Accounting, Supplier Portal, Workflow Builder, QR-Code Extraction e outras.
* **Decision Trees**: Crie lógica de decisão baseada em regras com um designer visual. Suporta várias políticas (Unique, First, Priority, Collect etc.).
* **Agent Setup**: Crie e gerencie agentes de automação e canais de comunicação para fluxos automatizados de processamento de documentos.

## 3. Comunicação e notificações

Controle como o DocBits se comunica com os usuários e processa os e-mails recebidos.

* **Email Notification**: Configure alertas por e-mail para eventos de processamento de documentos e mudanças de status.
* **Email Templates**: Crie e gerencie modelos de e-mail reutilizáveis para notificações, organizados por tipo de documento.
* **Email Ingestion**: Configure como os e-mails recebidos são classificados automaticamente e convertidos em documentos. Inclui regras de classificação, extração de campos, processamento, gestão de remetentes e treinamento — organizadas por tipo de documento (Orders, Invoices, Quotes, Delivery Notes, COA, PO Confirm).

## 4. Sistema e administração

Monitore a integridade do sistema, gerencie integrações e mantenha a segurança.

* **Integration & SSO**: Configure chaves de API para integrações externas e o Single Sign-On (SSO) com provedores de identidade.
* **Watchdog**: Configure o serviço Watchdog para a importação automática de documentos a partir de diretórios locais.
* **Dashboard**: Personalize o comportamento do dashboard — filtros, configurações de exportação, permissões de ações e opções de exibição de status.
* **Activity Logging**: Visualize em tempo real os logs de eventos do sistema, filtrados por gravidade (Debug, Info, Warning, Error), intervalo de tempo e serviço.
* **Analytics**: Acesse dashboards analíticos detalhados, incluindo Logs Analytics, monitoramento de Auth Security e API Metrics com Real User Monitoring (RUM).
* **Access Audit**: Ative e revise trilhas de auditoria que registram todas as ações de criação, atualização e exclusão (Create, Update, Delete) na sua organização, para fins de conformidade e segurança.
* **System Licenses**: Visualize e gerencie as informações e o uso das licenças de API.
* **Cache Management**: Configure os intervalos de limpeza automática do cache (TTL) para os caches Received Delivery, Purchase Order e Task/Notification.
* **Fulltext Search Settings**: Configure a pesquisa de texto completo nos seus documentos e dados (requer que o módulo Fulltext Search esteja ativado).

## 5. Configurações de fornecedores

Configure o Supplier Portal e gerencie os fluxos de trabalho relacionados a fornecedores.

* **Supplier General Settings**: Configure os campos de convite do portal de fornecedores, os status do fluxo de trabalho (Not Invited, Open, Pending Registration, Approved, Rejected) e as configurações de aprovação.
* **Email Templates**: Crie e gerencie modelos de e-mail específicos para a comunicação com fornecedores.
* **Supplier Layout**: Personalize o layout e a aparência do Supplier Portal.
* **Export Configuration**: Configure como os dados de fornecedores são exportados para sistemas externos.
* **Supplier Group**: Crie e gerencie grupos de fornecedores para categorizar e organizar seus fornecedores.
* **User and Supplier Group Mapping**: Vincule usuários internos a grupos de fornecedores específicos para controlar a visibilidade e o acesso.
