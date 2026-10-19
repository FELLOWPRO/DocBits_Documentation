# NOVA – Versão Menor 4 de novembro de 2026

**Disponibilidade da NOVA R1.1:** Disponível no ambiente de testes desde **16 de outubro de 2026**. A entrada em produção está prevista para **4 de novembro de 2026**.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/nova-release/v2/pt.mp4" %}

**DocBits é o produto. NOVA designa o ciclo de lançamentos.** [Ver o vídeo sobre o novo lançamento do DocBits](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/nova-release/v2/pt.mp4) · [Legendas](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/nova-release/v2/pt.vtt).

**Versões dos serviços no ambiente de testes: 16 de outubro de 2026**

A NOVA inclui todas as funcionalidades anteriormente disponíveis como beta na VESTA como funcionalidades regulares, juntamente com validação de documentos orientada, mais formas de melhorar a automação, verificações mais claras de faturas eletrónicas e melhor controlo sobre importações e processamento de documentos. Estas notas descrevem as adições voltadas para o cliente nas versões de serviço listadas abaixo, em comparação com o último [hotfix da VESTA publicado, R1.0.15 de 14 de outubro de 2026](incremental-updates-14-october-2026.md), incluindo hotfixes anteriores da VESTA.

O instantâneo identifica as compilações cobertas por estas notas. Para disponibilidade no seu ambiente de sandbox ou de produção e para alternar entre canais, consulte o [ciclo de vida de lançamento da DocBits](../docbits-release-lifecycle-strategy.md). As funcionalidades que têm uma opção de organização ou de tipo de documento ainda precisam de ser ativadas por um administrador.

## Funcionalidades beta anteriores da VESTA: incluídas na NOVA <a href="#former-vesta-beta-features-included-in-nova" id="former-vesta-beta-features-included-in-nova"></a>

**Todas as antigas funcionalidades beta da VESTA estão incluídas como funcionalidades regulares no ambiente de testes da NOVA.** Para clientes que não utilizaram a beta da VESTA, isto expande as funcionalidades disponíveis para a sua equipa, incluindo **Gerir Layouts**, [**Regras de validação personalizadas**](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) e [**Regras de transformação**](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md). As definições da organização, as opções de tipo de documento e as permissões de acesso continuam a aplicar-se.

As mesmas funcionalidades beta anteriores tornar-se-ão funcionalidades regulares da VESTA com o **próximo hotfix da VESTA, planeado para [11 de novembro de 2026](vesta-hotfix-11-november-2026.md)**. Este anúncio abrange as funcionalidades beta anteriores da VESTA; as secções abaixo também descrevem adições e melhorias adicionais da NOVA.

## O que a NOVA acrescenta para os clientes <a href="#what-nova-adds-for-customers" id="what-nova-adds-for-customers"></a>

A comparação abaixo abrange funcionalidades beta anteriores agora disponíveis, novas capacidades e extensões de funcionalidades existentes. A linha de base da VESTA inclui funcionalidade que estava apenas disponível em beta; a sua inclusão no conjunto de funcionalidades regulares da NOVA é uma alteração de lançamento voltada para o cliente.

| Capacidade | Linha de base da VESTA (incluindo beta) | O que os clientes ganham com a NOVA |
| --- | --- | --- |
| **Utilizar funcionalidades beta anteriores** | Funcionalidades disponíveis através da beta da VESTA | **Funcionalidades regulares da NOVA:** todas as funcionalidades beta anteriores da VESTA estão incluídas. A sua introdução regular na VESTA está planeada para o hotfix de 11 de novembro de 2026. |
| **Ajuda ao validar um documento** | Assistente de definições e Verificação de Campos de Cabeçalho | **Novo Assistente de validação:** identificar campos bloqueantes, saltar para o valor relevante, rever correções sugeridas e manter o chat numa janela separada. |
| **Melhorar a automação a partir de correções do dia a dia** | Painel Touchless Intelligence, diagnóstico de fornecedores e propostas de alteração | **Novo processo de revisão e medição:** submeter pedidos de melhoria, rever propostas de regras aprendidas, ver evidências de documentos afetados, classificar oportunidades e medir resultados após a ativação. |
| **Compreender e resolver erros de faturas eletrónicas** | Verificações de documentos eletrónicos, catálogo de regras e visualizador XML | **Validação de Faturas Eletrónicas Expandida:** relatórios agrupados por nível de validação, controlos de política e histórico de alterações, rejeição a partir do relatório e inspeção XML dentro de faturas PDF suportadas. |
| **Controlar importações FTP/SFTP** | Conexões de importação e retenção ou arquivamento de ficheiros de origem | **Nova configuração orientada e controlos:** assistente de conexão, registos passo a passo, tentativas configuráveis e notificações de falha, e eliminação de ficheiros de origem após importação bem-sucedida. |
| **Trabalhar com regras e layouts** | Motores de regras, registos de execução e transformações após pesquisa de dados mestres; painéis de gestão exigiam um link beta | **Acesso mais amplo e melhores ferramentas:** abrir painéis de gestão diretamente, pesquisar e pré-visualizar layouts de destino, abrir o editor de layout de um documento e registar a execução da seleção de layout. |
| **Agir a partir do Assistente de definições** | Chat de definições, pré-visualizar/confirmar/anular e avisos proativos de saúde da importação | **Ações adicionais:** gerir conexões com falha, ver histórico de desativação, alterar itens de configuração selecionados, criar uma regra de validação inativa a partir de um catálogo e ver explicações da página. |
| **Controlar o processamento de documentos** | Limites de páginas da organização e reinício de documento | **Novas escolhas a nível de documento:** reiniciar com uma contagem de páginas escolhida, ver páginas processadas versus totais, e escolher se campos ocultos são extraídos. |
| **Corresponder entregas complexas** | Correspondência de ordens de compra e ligação manual de linhas | **Correspondência mais flexível:** selecionar linhas em qualquer direção, opcionalmente reter cada sublinha de documento correspondida e agrupar pedidos de exportação por colunas de linha configuradas. |
| **Manter o trabalho exportado e concluído distintos** | Fluxos de trabalho de exportação e Finished existentes | **Novos controlos de estado:** utilize Exported para processamento de acompanhamento, bloqueie opcionalmente documentos Finished e localize documentos retidos pelo limite de execução do fluxo de trabalho. |

### Ativar as funcionalidades que necessitam de configuração

* **Assistente de validação:** um administrador da organização ativa-o em **Definições → Informações da Empresa → Assistentes**. É distinto do Assistente de definições e está desativado até ser ativado.
* **Relatórios de revisão de melhorias e consultoria:** requerem acesso de administrador da organização e de Analytics. As propostas aprendidas necessitam de histórico de correções; um resultado medido necessita de dados suficientes e do período de acompanhamento para ser concluído.
* **Controlos de regras e layouts:** os respetivos interruptores de ativação por tipo de documento continuam a aplicar-se. O NOVA torna os painéis de gestão acessíveis sem um link beta.
* **Comportamento de processamento opcional:** configure a limpeza e as tentativas de repetição do FTP por ligação. A expansão de sublinhas de um para muitos e o bloqueio de documentos finalizados são definições de ativação opcional.

Para disponibilidade no seu ambiente e mudança de canal de lançamento, consulte o [ciclo de vida do lançamento](../docbits-release-lifecycle-strategy.md).

## Ver os vídeos das funcionalidades <a href="#watch-the-feature-videos" id="watch-the-feature-videos"></a>

Utilize estes guias práticos em conjunto com as notas de lançamento para compreender as funcionalidades relacionadas e a sua configuração. Os vídeos disponíveis em português europeu estão ligados abaixo; os outros vídeos estão claramente identificados como em inglês.

* [Escolher a Automação Certa — incluindo onde se enquadram as Regras de correspondência de encomendas](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/choose-automation/v1/pt.mp4)
* [Regras de transformação](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/transformation-rules/v1/pt.mp4)
* [Regras de validação personalizadas (Vídeo em inglês)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/custom-validation-rules/v1/en.mp4)
* [Layouts e regras de seleção (Vídeo em inglês)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/layouts/v1/en.mp4)
* [Touchless Intelligence](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence/v1/pt.mp4)
* [Validação de Faturas Eletrónicas](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/einvoice-validation/v1/pt.mp4)
* [Utilizadores e acesso de administrador](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/users/v1/pt.mp4)
* [Suborganizações](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/sub_organizations/v1/pt.mp4)

### AI Table: seis vídeos curtos

Estes vídeos estão em inglês. Veja a série completa ou escolha o tópico que necessita.

1. [Ler a tabela AI](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part1/v1/en.mp4)
2. [Corrigir uma coluna e ensinar o DocBits](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part2/v1/en.mp4)
3. [Três problemas típicos](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part3/v1/en.mp4)
4. [Linhas de desconto, imposto e quantidade zero](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part4/v1/en.mp4)
5. [O que a IA já lê corretamente](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part5/v1/en.mp4)
6. [O Assistente e quem pode alterar o quê](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part6/v2/en.mp4)

Para capturas de ecrã e instruções detalhadas, consulte o [guia da AI Table](../../end-user-and-partner-section/end-user-section/ai-table/README.md).

## Assistente de validação: ajuda com o documento à sua frente

* **Encontrar o que bloqueia o progresso.** Pergunte por que motivo um documento não pode continuar. O assistente identifica os campos afetados, explica o problema e oferece um salto para o campo ou célula da tabela. Utiliza o documento atual e os direitos de acesso do utilizador.
* **Rever correções sugeridas em contexto.** Onde suportado, os revisores podem aplicar um valor de campo ou tabela proposto, utilizar um candidato de dados mestres, repetir uma pesquisa ou abrir o ecrã de correspondência relevante. As alterações ao formulário estão sujeitas ao processo normal de revisão e gravação do documento. Documentos só de leitura e utilizadores sem permissão de edição não recebem ações de edição.
* **Perguntar sobre correspondência e contabilidade.** O assistente pode explicar o contexto da encomenda de compra ou da contabilidade quando aberto nesses ecrãs. As alterações ao formulário de validação são efetuadas no ecrã de validação.
* **Compreender uma melhoria antes de a utilizar.** As explicações ligam uma regra ou definição proposta aos valores reais do documento. Podem incluir um diagrama e uma explicação narrada na língua do utilizador quando disponível. As sugestões mantêm-se focadas no documento atual.
* **Trabalhe com o chat numa janela separada.** Destaque a conversa enquanto revê o documento. As ações que alteram o formulário permanecem na janela do documento.
* **Veja mais detalhes por detrás dos valores extraídos.** A vista de origem do valor adiciona detalhes como OCR versus camada de texto do PDF, correspondência de regras de extração e a pesquisa que forneceu um valor. A explicação da tabela de IA adiciona conselhos de configuração mais acionáveis e contagens mais claras.

Um administrador da organização ativa o Assistente de validação separadamente do Assistente de definições em **Definições → Informações da empresa → Assistentes**.

## Transformar correções repetidas em melhorias de automação

O painel existente do [Touchless Intelligence](../../administration-and-setup/touchless-intelligence.md) ganha um processo de revisão e acompanhamento:

* **Propostas de regras aprendidas.** Correções manuais repetidas podem sugerir uma [regra de transformação](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md). Os administradores veem o que ela escreveria, os exemplos de suporte e os documentos nos quais substituiria um valor que a equipa tinha aceite. Uma proposta é revista antes de se tornar uma regra ativa.
* **Pedidos de melhoria dos revisores.** Os utilizadores podem submeter uma melhoria a partir do assistente de documentos para que um administrador a revise no Touchless Intelligence. O pedido mantém a sua explicação e decisão juntas.
* **Medir o que aconteceu após a ativação.** Para regras de transformação suportadas, o DocBits compara correções manuais antes e depois da ativação e mostra a taxa de processamento sem intervenção junto delas. A medição utiliza períodos de 14 dias e identifica dados insuficientes em vez de inventar uma melhoria. Alterar uma regra inicia uma nova medição para essa revisão.
* **Relatório de consultoria.** Os administradores podem gerar uma vista classificada de oportunidades de melhoria em extração, dados mestres, correspondência de ordens de compra, contabilidade, definições e fluxo de processamento. O impacto estimado é rotulado como uma estimativa até ter sido medido.
* **Conselhos de correspondência específicos do fornecedor.** Problemas repetidos de correspondência de fornecedores e artigos podem informar propostas para tolerâncias ou [regras de correspondência de encomendas](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md). Os conselhos distinguem uma ordem de compra em falta de um problema de regra ou tolerância.
* **Resumos de acompanhamento.** Um resumo semanal para administradores reúne pedidos de melhoria abertos, principais oportunidades e medições concluídas quando há algo para reportar. Os solicitantes podem ser notificados quando um resultado medido estiver disponível.

## Assistente de definições: ações adicionais e explicações de páginas

O [Assistente de definições](../../administration-and-setup/settings/global-settings/company-information/settings-assistant.md), incluindo avisos proativos de saúde de email/FTP, já foi lançado no VESTA. O NOVA adiciona ações e contexto a essa experiência existente:

* **Ações de conexão a partir de um aviso de saúde.** Abra a conexão afetada, reveja a ação disponível e confirme-a a partir do assistente. Os avisos de saúde também podem ser descartados. Os cartões básicos de aviso por canal e as suas informações de erro/repetição já existem no VESTA.
* **Histórico de desativação visível.** Onde registado, uma importação desativada mostra quando foi desligada e por quem.
* **Ações adicionais revistas.** Os administradores podem pré-visualizar e confirmar alterações suportadas, como ativar tipos de documentos, renomear um grupo, alterar o modo de pesquisa de um campo de pesquisa, apagar um campo ou criar uma regra de validação personalizada inativa a partir do catálogo.
* **Gerir conexões de importação com falha.** Os cartões suportados podem desligar ou apagar uma conexão após confirmação. As ações reversíveis oferecem uma opção de anular; a eliminação permanente é identificada como tal.
* **Explicações de páginas.** Páginas de definições selecionadas oferecem vídeos com legendas e transcrições, incluindo layouts, utilizadores, sub-organizações, regras de transformação e validação de faturas eletrónicas onde uma versão linguística estiver disponível.

## Regras e layouts: acesso direto e melhores diagnósticos

* **Controlos beta anteriores tornam-se funcionalidades regulares.** Gerir Layouts, [Regras de validação personalizadas](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) e [Regras de transformação](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md) estão visíveis nas definições avançadas do tipo de documento do NOVA sem um link beta. Os seus interruptores de ativação permanecem sob controlo do administrador. Estes controlos estão incluídos no hotfix VESTA planeado para 11 de novembro de 2026, juntamente com todas as outras funcionalidades beta anteriores do VESTA.
* **Diagnósticos de regras mais úteis.** As regras de seleção de layout ganham uma opção **Registar execução**. A pesquisa de regras aceita identificadores de regras e abrir um editor carrega a regra guardada atual. O registo de execução de regras existente permanece o local para rever o que foi executado.
* **Escolher e abrir layouts com mais contexto.** Pesquise layouts de destino, pré-visualize o seu conteúdo e abra o destino diretamente a partir de uma regra de seleção. As regras de seleção de aprovação aceitam corretamente os tipos de layout de aprovação suportados. Os administradores também recebem um atalho da validação de documentos para o editor de layouts desse tipo de documento.
* **Selecionar vários valores de condição.** Condições como **é um de** suportam múltiplos valores selecionados.
* **Encontrar campos de deteção de duplicados mais rapidamente.** O seletor de campos nas definições de duplicados do tipo de documento é pesquisável.

As transformações após a pesquisa de dados mestres, o registo básico de execução de regras, editores de regras mais amplos e as correções de clonagem de regras padrão já têm implementações na base VESTA. O NOVA mantém essa funcionalidade e disponibiliza os antigos controlos de gestão beta como funcionalidades regulares.

Para passos de configuração, exemplos e testes, consulte [Regras de validação personalizadas](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) e [Regras de transformação](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md). Para escolher que layout um documento utiliza, consulte [Regras de seleção de layout](../../administration-and-setup/settings/global-settings/document-types/layout-manager/layout-selection-rules.md).

## Validação de faturas eletrónicas: conclusões mais claras e controlos de política

* **Um relatório organizado por nível de validação.** As conclusões são agrupadas em sintaxe, esquema, regras de negócio, regras de verificação cruzada e regras específicas do país, com grupos adicionais para outras verificações de padrões e verificações de valores. As mensagens e resumos utilizam a língua do utilizador quando existem traduções disponíveis.
* **Verificações mais completas e resultados mais claros.** O validador e o relatório atualizados distinguem erros, avisos e a gravidade efetiva após a configuração específica da organização. A página designa-se **Validação de faturas eletrónicas**.
* **Políticas por tipo de documento.** Os administradores podem rever se a validação de faturas eletrónicas está ativa e se as falhas bloqueiam o processamento. A vista de políticas identifica substituições de subtipo, e as alterações de políticas são registadas num histórico de alterações.
* **Inspecionar o XML dentro de uma fatura PDF.** O visualizador de XML pode ler o XML incorporado em PDFs ZUGFeRD/Factur-X suportados, abrir a posição referida por uma conclusão e regressar ao documento.
* **Rejeitar com um motivo registado.** Um revisor autorizado pode rejeitar um documento elegível a partir do relatório de validação. O relatório prepara um motivo a partir dos seus erros para o revisor verificar antes de confirmar.
* **Correções de formato adicionais.** As faturas CII da utilidade EDNA são reconhecidas, e as correções ao mapeamento de IVA do XRechnung melhoram a forma como os valores relevantes da fatura chegam aos campos do DocBits.

Consulte [Regras de validação de documentos eletrónicos](../../administration-and-setup/settings/document-processing/e-documents/validation-rules.md).

## Importações FTP/SFTP e de email

* **Configuração orientada de FTP/SFTP.** O assistente de ligação separa os detalhes do servidor, as opções de importação e a configuração. As verificações de ligação e erros mais claros ajudam os administradores a identificar uma ligação incorreta ou uma pasta de origem em falta.
* **Registos de importação por passo.** Revise o progresso de um ficheiro através da importação FTP, incluindo o carregamento e a ação configurada no ficheiro de origem.
* **Comportamento configurável de nova tentativa e notificação.** Defina o intervalo entre novas tentativas posteriores, quanto tempo continuar a tentar e os destinatários das notificações. Quando a janela de nova tentativa é esgotada, a ligação pode ser desativada automaticamente e os destinatários notificados; o assistente mostra o aviso de desativação.
* **Eliminar após importação bem-sucedida.** Além de reter ou arquivar ficheiros de origem, os administradores podem escolher eliminá-los do servidor FTP/SFTP após uma importação bem-sucedida. O arquivamento e a eliminação são alternativas separadas.
* **Recuperação de importação mais fiável.** As execuções FTP sobrepostas são impedidas de carregar o mesmo ficheiro de origem duas vezes. A edição de uma ligação preserva a sua palavra-passe armazenada, a menos que seja substituída. O tratamento de email não marca uma mensagem para eliminação quando a cópia falhou.
* **Suporte para email assinado.** Mensagens S/MIME assinadas opacas que contêm faturas podem ser descompactadas em vez de ignoradas.
* **Histórico e estado da configuração de email.** As definições de importação mostram quem guardou ou ativou uma configuração pela última vez. O interruptor de email de entrada reflete o estado ativo armazenado, incluindo uma configuração recém-guardada.

Consulte [Importação FTP](../../end-user-and-partner-section/end-user-section/how-to-import-documents/ftp.md) e [Testar uma ligação de importação FTP](../../administration-and-setup/settings/document-processing/import/test-ftp-import-connection.md).

## Processamento e extração de documentos

* **Reiniciar com um número de páginas escolhido.** O painel adiciona uma ação de reinício que permite aos revisores especificar quantas páginas processar para esse documento, dentro do seu número real de páginas.
* **Ver o limite de processamento.** O painel pode mostrar as páginas processadas versus o total de páginas para um documento limitado. A definição **Páginas a processar** da organização está agrupada sob Processamento de Documentos em **Classificar & Extrair**.
* **Controlar a extração de campos ocultos.** Os administradores podem escolher se os campos ocultos participam na extração através da definição **Extrair campos ocultos**.
* **Trabalho mais rápido em lotes maiores.** Os reinícios em massa de documentos, as importações de dados mestres em CSV, o processamento de PDF e a extração de campos baseada em regras recebem melhorias de desempenho.
* **Extração de IA mais resiliente.** Os tempos limite são reportados como tempos limite, e as falhas de modelos suportados podem recorrer a outro modelo disponível. Correções adicionais lidam com chaves repetidas na saída da IA, sinónimos de campos configurados e definições de tabelas guardadas vazias.
* **Manter o valor recém-introduzido.** Guardar uma célula de tabela sem clicar primeiro noutro local preserva o valor digitado. As datas com nomes de meses confundidos pelo OCR são tratadas de forma mais fiável.

## Correspondência, aprovação e exportação de ordens de compra

O [guia de Regras de correspondência de encomendas](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) explica como ativar a correspondência baseada em regras, configurar tipos de correspondência e tolerâncias, definir a ordem de execução e gerir versões de regras.

* **Corresponder em qualquer direção.** Selecione linhas de documentos e ligue-as a linhas de ordens de compra, ou comece pelas linhas da ordem de compra. Isto é útil quando muitas linhas de notas de entrega se relacionam com uma linha de ordem de compra.
* **Preservar o detalhe de linhas um-para-muitos.** Uma configuração de correspondência pode agora reter uma sublinha individual para cada linha de documento quando várias linhas correspondem a uma linha de ordem de compra. Esta opção está desativada por predefinição. A exportação genérica via API pode agrupar pedidos por colunas de linha configuradas, suportando entregas ou contentores que necessitam de registos de destino separados.
* **Configurar o recurso de última linha.** As organizações podem controlar se a linha restante do documento e da ordem de compra pode ser correspondida pelo recurso de linha única.
* **Correspondência e visualização mais precisas.** As correções preservam a base de preço correta para correspondências convertidas por embalagem, herdam o estado da linha da ordem de compra nas linhas de calendário e mostram as quantidades recebidas a partir das linhas de receção.
* **Prevenir aprovação prematura e trabalho duplicado.** A aprovação final é bloqueada enquanto as discrepâncias relevantes da ordem de compra permanecerem não aprovadas. A execução repetida do fluxo de trabalho não cria outra tarefa aberta para o mesmo grupo, e as verificações de exportação duplicada são executadas antes da aprovação.
* **Separar Exported de Finished.** As ações de exportação podem selecionar o estado após uma exportação bem-sucedida. **Exported** tem o seu próprio distintivo no painel. As organizações que ativam o bloqueio de documentos concluídos impedem que fluxos de trabalho comuns ou reinícios reabram documentos concluídos; as substituições autorizadas são registadas.
* **Resolução de problemas de fluxo de trabalho mais clara.** Um filtro no painel encontra documentos retidos pelo limite de execução do fluxo de trabalho. As execuções do fluxo de trabalho podem ser inspecionadas num pop-up, e uma alteração de estado recusada nomeia o estado do documento.
* **Correções adicionais de exportação.** As tentativas de validação e aprovação do M3 são ajustadas, e as configurações de exportação de fornecedores condicionais são tratadas corretamente.

## Usabilidade e acesso quotidianos

* **Navegação mais fiável.** Os endereços de documentos atualizados têm redirecionamentos para links antigos. Os links diretos do NOVA mantêm o canal pretendido através do início de sessão, e o progresso de carregamento mostra qual a parte da página que está a ser preparada.
* **Preferências de trabalho pessoais.** A ordem das colunas da ordem de compra é guardada por utilizador, e o ecrã de aprovação memoriza o painel lateral aberto do utilizador.
* **Vistas de tarefas e painéis mais fiáveis.** As tarefas sem um responsável podem ser listadas, abertas e atribuídas. O quadro de tarefas recarrega quando a organização selecionada está pronta, os intervalos de datas personalizados do painel são aplicados corretamente, e as linhas de documentos duplicadas são evitadas.
* **Etiquetas e registos melhores.** Os administradores podem editar as chaves de tradução de campos e colunas de tabelas. As colunas do registo de documentos podem ser redimensionadas, as colunas personalizadas do painel lidam com identificadores de campos com maiúsculas e minúsculas misturadas, e as etiquetas e nomes de ficheiros longos cabem de forma mais consistente.
* **Âmbito das notificações.** As regras de e-mail de estado de documentos podem ser limitadas a uma sub-organização.
* **Onboarding de fornecedores.** Os links mágicos de registo no Portal de Fornecedores mantêm-se válidos durante **21 dias em vez de 7 dias**. Os administradores também podem configurar o título do erro de carregamento para um campo de ficheiro num layout de fornecedor.
* **Fiabilidade do início de sessão.** O início de sessão SAML deixa de reutilizar sessões expiradas ou revogadas. O início de sessão de gestão suporta o passo MFA obrigatório e as adesões inativas não podem receber um novo convite de definição de palavra-passe.
* **Imagens do Quadro de Ideias.** As imagens carregadas são armazenadas e servidas separadamente da descrição da ideia, melhorando o tratamento das imagens.
* **Mudança controlada de canal.** A definição Canal de Lançamento pode ser definida como somente leitura quando a mudança não está ativada para o ambiente. Siga o anúncio de lançamento para a disponibilidade.

## Assistentes conectados e ferramentas de integração

Para organizações e parceiros que utilizam a integração DocBits MCP, o NOVA adiciona ferramentas para listar regras de validação resolvidas, testar uma regra contra um documento sem guardar alterações e explicar a evidência de execução de regras armazenada. Os assistentes conectados também podem listar pedidos de melhoria e submeter uma aprovação autorizada pelo administrador através do mesmo processo de revisão da aplicação web. Aplicam-se as permissões existentes de organização e documento.

## Funcionalidades já presentes no VESTA

O NOVA também incorpora a funcionalidade listada abaixo. Onde o acesso estava anteriormente limitado à beta do VESTA, a disponibilidade regular faz parte desta versão do NOVA e está planeada para a correção do VESTA em 11 de novembro de 2026. A lista descreve a funcionalidade anterior, juntamente com as alterações de disponibilidade e melhorias explicadas acima:

* O Assistente de definições original, a sua pesquisa de documentação, o fluxo básico de pré-visualização/confirmação/anulação e os avisos proativos de saúde da importação por email/FTP.
* Os níveis de IA Fast, Full, Nexus e Auto e a definição de modo de visão.
* A Verificação de Campos de Cabeçalho e o relatório original de origem do valor.
* A primeira versão do Touchless Intelligence, o diagnóstico de fornecedores, a análise em massa e o diagrama de decisão da ordem de compra.
* Os motores de regras subjacentes de validação, transformação e seleção de layout, as transformações após a pesquisa de dados mestres e o registo básico de execução de regras.
* Melhorias anteriores na pesquisa do painel, MFA, domínios de email de organização verificados, tolerância de encargos e o aumento do limite de execução do fluxo de trabalho para 50.

Consulte a [correção do VESTA de 14 de outubro](incremental-updates-14-october-2026.md), a [correção de 15 de setembro](incremental-updates-15-september-2026.md) e as [notas de lançamento anteriores](README.md#vesta-hotfix-releases) para o histórico de lançamentos do VESTA.

## Versões do serviço NOVA

Estas são as versões e as datas de implementação da **compilação da NOVA disponível no ambiente de testes desde 16 de outubro de 2026**. A entrada em produção está prevista para **4 de novembro de 2026**; este registo do ambiente de testes não determina as versões definitivas de produção. As datas correspondem às implementações individuais dos serviços.

| Serviço | Versão | Marca de tempo de implementação |
| --- | --- | --- |
| API Service | `13.26.5` | 16.10.2026 11:57:49 |
| Auth Bridge | `0.5.11` | 08.10.2026 10:56:15 |
| Auth Service | `1.84.3` | 16.10.2026 12:19:50 |
| Auto Accounting | `1.23.6` | 15.09.2026 09:42:57 |
| Barcode Service | `1.20.3` | 15.10.2026 14:17:18 |
| Docflow Service | `2.13.9` | 15.10.2026 16:14:37 |
| Docnet Service | `1.59.1` | 12.10.2026 00:59:12 |
| Email Service | `1.44.4` | 16.10.2026 11:44:58 |
| Extraction Service | `1.63.1` | 15.10.2026 19:34:17 |
| FTP Service | `1.37.4` | 15.10.2026 10:42:01 |
| Fulltext Service | `1.46.1` | 12.10.2026 05:16:16 |
| Ideas Service | `0.5.6` | 14.10.2026 12:06:00 |
| OCR Service | `1.11.8` | 12.10.2026 01:00:00 |
| Operator Service | `1.45.0` | 12.10.2026 09:35:25 |
| PO Match Service | `1.65.7` | 14.10.2026 16:14:20 |
| Web App | `10.72.2` | 16.10.2026 12:04:41 |

Os números de versão avançam independentemente nos dois canais. Um número maior não significa, por si só, que um serviço tenha uma nova funcionalidade para o cliente. As alterações revistas em Auto Accounting, Barcode, Docnet, Fulltext, OCR e Operator são alterações de manutenção ou de fiabilidade de processamento; não introduzem um fluxo de trabalho de cliente separado nesta comparação. As atualizações do Auth Bridge melhoram a fiabilidade da sincronização de contas entre regiões.
