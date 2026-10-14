# Contabilização de Fatura de Custo e Vendas Indiretas

## Introdução

Bem-vindo ao módulo de Contabilização de Fatura de Custo e Vendas Indiretas! Este módulo foi projetado para ajudá-lo a gerenciar e reconciliar suas transações financeiras de forma eficiente dentro do seu sistema ERP. Com recursos como extração automática de dados, correspondência de documentos e rastreamento detalhado, você pode garantir que seus registros financeiros sejam precisos e atualizados.

<figure><img src="../../.gitbook/assets/acounting-for-cost-invoice-and-indirect-sales1.png" alt=""><figcaption></figcaption></figure>

## Primeiros Passos

Para começar a usar o módulo de contabilidade, certifique-se de que você possui as permissões necessárias configuradas pelo administrador do sistema. Você precisará de acesso aos módulos de contabilidade de custos e contabilidade de vendas dentro do sistema ERP.

## Requisitos do Sistema

* Acesso aos módulos de contabilidade de custos e contabilidade de vendas dentro do sistema ERP.
* Permissões de usuário apropriadas para visualizar e processar documentos financeiros.

## Principais Recursos

1. **Extração Automática de Dados**: Extrai e interpreta automaticamente dados de faturas digitais e outros documentos.
2. **Comparação de Dados**: Compara dados de faturas extraídos com dados existentes de pedidos de compra.
3. **Verificação de Correspondência**: Verifica correspondências com base em regras e tolerâncias predefinidas.
4. **Relatório de Discrepâncias**: Identifica e relata quaisquer discrepâncias entre faturas e pedidos de compra.
5. **Trilha de Auditoria**: Mantém um registro de todas as ações para conformidade e revisão.
6. **Treinamento de Documentos**: Treine o sistema para reconhecer novos documentos com esforço mínimo, geralmente apenas uma vez.
7. **Divisão de Valores**: Divida valores por departamento para rastreamento financeiro detalhado.
8. **Definição de Conta Contábil**: A equipe APS (Sistema de Contabilidade e Aquisições) pode definir a conta contábil uma vez que os dados são extraídos.

## Interface do Usuário

A interface do módulo de contabilidade geralmente inclui os seguintes componentes:

* **Painel**: Visão geral do status de faturas e vendas, e atividade recente.
* **Ferramentas de Pesquisa e Filtro**: Capacidades para pesquisar e filtrar registros de faturas e vendas.
* **Registros Correspondentes**: Seção exibindo registros correspondentes com sucesso.
* **Discrepâncias**: Seção mostrando registros com discrepâncias que precisam de revisão ou ação.
* **Relatórios**: Acesso a relatórios detalhados e opções de exportação.

## Guia Passo a Passo para Usar o Módulo de Contabilidade

### 1. Acesse o Módulo de Contabilidade

Navegue até o módulo de contabilidade no menu principal do seu sistema ERP.

### 2. Importe ou Acesse Faturas

* **Importação Automatizada**: Se o seu sistema estiver configurado para captura automática de dados, as faturas serão importadas automaticamente para o sistema.
* **Upload Manual**: Se necessário, faça o upload manual dos arquivos de fatura no sistema usando a interface fornecida.

### 3. Revise Faturas Correspondidas Automaticamente

* Revise as faturas que foram automaticamente correspondidas com pedidos de compra.
* Verifique os detalhes da correspondência, incluindo números de itens, quantidades e preços.

### 4. Lide com Discrepâncias

* Acesse a seção de Discrepâncias para revisar quaisquer faturas que não puderam ser correspondidas automaticamente.
* Ajuste manualmente quantidades ou preços conforme necessário, ou marque a fatura para revisão posterior.

### 5. Correspondência Manual

Para faturas não correspondidas automaticamente:

* Use as ferramentas de pesquisa e filtro para encontrar o pedido de compra correspondente.
* Verifique e corresponda manualmente a fatura ao pedido de compra.

### 6. Treine o Sistema

* Para novos tipos de documentos, treine o sistema para reconhecê-los fornecendo uma amostra.
* Normalmente, você só precisa treinar o sistema uma vez para que ele reconheça com precisão documentos semelhantes no futuro.

### 7. Registre Lançamentos

* Navegue até a aba "Itens de linha" para visualizar e registrar lançamentos para cada fatura.
* Alocar os valores para as contas, centros de custo e dimensões apropriadas específicas para Infor LN/M3.

**Exemplo: Registro de uma Fatura de Custo**

1. **Selecione o Item de Linha**: Escolha o item de linha para a fatura de custo.
2. **Atribuir Conta**: Atribua a conta apropriada, como "71200 - Despesa Não Operacional".
3. **Definir Dimensões**: Defina dimensões adicionais como centro de custo, grupo de produtos e projeto.
4. **Dividir Valor**: Se necessário, divida o valor por departamento para um rastreamento mais detalhado.
5. **Inserir Valor**: Insira o valor para o item de linha.

### 8. Defina Contas Contábeis

* Uma vez que os dados são extraídos, a equipe APS pode definir as contas contábeis.
* Isso garante que cada transação seja registrada na conta correta para um relatório financeiro preciso.

### 9. Gere Relatórios

* Acesse a seção "Relatórios" para gerar relatórios detalhados sobre transações financeiras.
* Use as opções de exportação para salvar relatórios para análise posterior ou arquivamento.

### Uso de Exemplo

1. **Upload de Documentos**: Os usuários podem fazer upload de vários documentos (faturas, notas de entrega, etc.) para o sistema.
2. **Correspondência Automática**: O sistema corresponde automaticamente os documentos enviados com pedidos de compra existentes.
3. **Revisão de Correspondências**: Os usuários podem revisar as correspondências, verificar detalhes e ver indicadores de status.
4. **Resolução de Discrepâncias**: Quaisquer incompatibilidades ou discrepâncias são destacadas para que o usuário revise e corrija manualmente.
5. **Exportação de Dados**: Dados correspondentes podem ser exportados para processamento posterior ou arquivamento.
