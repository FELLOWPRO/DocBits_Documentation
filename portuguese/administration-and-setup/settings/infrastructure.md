# Infraestrutura

A página **Infraestrutura** oferece aos administradores uma visão ao vivo de onde cada parte do DocBits é executada (UE ou EUA), de como um documento percorre o sistema e se o processamento em segundo plano está saudável. É somente leitura — nada é configurado aqui; ela responde à pergunta: *«está tudo funcionando e os meus dados permanecem na minha região?»*

> **Acesso:** Infraestrutura é uma página exclusiva para administradores. Abra **Configurações → Organização e Acesso → Infraestrutura**.

<figure><img src="../../.gitbook/assets/infrastructure_overview.png" alt="Página de Infraestrutura com a aba Topologia aberta"><figcaption><p>A página de Infraestrutura, aba Topologia</p></figcaption></figure>

A página é dividida em três abas:

| Aba | Responde |
|-----|----------|
| **Topologia** | Onde cada componente é executado e está tudo na minha região? |
| **Processamento** | As etapas de processamento (OCR, extração, correspondência de PO …) estão em execução e atualizadas? |
| **Tarefas agendadas** | Os trabalhos recorrentes em segundo plano são executados conforme o previsto? |

## Topologia

A aba Topologia desenha toda a plataforma DocBits como um diagrama, agrupado em camadas — **Edge / Web**, **Core API**, **Importação**, **Serviços em segundo plano**, **Armazenamentos de dados** e **Autenticação**. Cada caixa é um componente (o App Web/CDN, o gateway de API, o worker de OCR, o banco de dados e assim por diante).

<figure><img src="../../.gitbook/assets/infrastructure_topology.png" alt="Diagrama de topologia com selos de região"><figcaption><p>Cada componente é rotulado com a região em que é executado</p></figcaption></figure>

### Transparência de região

Cada componente exibe um selo de região para que você confirme a residência dos seus dados num relance:

| Selo | Significado |
|------|-------------|
| **UE ✓** / **US ✓** | O componente é executado na região da sua organização. |
| **SHARED** | Um componente global (por ex. o CDN) sem uma região única — isso é esperado e não representa um problema. |
| **Divergência de região** | O componente é executado numa região *diferente* da sua organização. Ele é destacado para que você possa relatar ao suporte. |

O banner no topo resume o resultado: **«Todos os componentes são executados na sua região (UE)»** quando tudo corresponde, ou um aviso se algum componente crítico estiver em outra região.

### Arquitetura vs. Reproduzir processo

Use o seletor acima do diagrama para alternar a visualização:

- **Arquitetura** — o mapa estático de todos os componentes e como eles se conectam.
- **Reproduzir processo** — anima a jornada de um documento pelo sistema, passo a passo, para que você veja a ordem em que os componentes são envolvidos.

O indicador **● live** mostra que as informações de integridade no diagrama refletem o estado atual do sistema.

### Módulos opcionais

Componentes que pertencem a um módulo opcional (Pesquisa de texto completo, DocFlow, Auto-Accounting, DocNet, Correspondência de PO) exibem um selo **ativado** ou **desativado**. Clicar num módulo desativado leva você diretamente à página onde pode ativá-lo — **Configurações → Módulo** para a maioria dos módulos, ou **Tipos de documento** para a Correspondência de PO (que é ativada por tipo de documento).

## Processamento

A aba Processamento mostra o pipeline de processamento de documentos da **sua organização** — quando cada etapa foi executada pela última vez e se o trabalho flui ou se acumula.

<figure><img src="../../.gitbook/assets/infrastructure_processing.png" alt="Tabela de processamento com selos de status"><figcaption><p>Status de processamento por etapa para a sua organização</p></figcaption></figure>

| Coluna | Descrição |
|--------|-----------|
| **Processo** | A etapa de processamento — Processamento de documentos, OCR, TR-OCR, Divisão por código de barras, Extração de código de barras, Extração, Correspondência de PO. |
| **Última execução** | Há quanto tempo a etapa foi executada. Passe o mouse para ver o carimbo de data/hora exato. *«Nunca executado»* significa que nenhum documento chegou ainda a esta etapa. |
| **Status** | Um selo tipo semáforo (veja abaixo). |

Selos de status:

| Selo | Significado |
|------|-------------|
| **OK** (verde) | Sem erros recentes e nada aguardando — a etapa está saudável. |
| **Em andamento (N)** (âmbar) | `N` documentos estão sendo processados nesta etapa no momento. |
| **Erro (N)** (vermelho) | `N` documentos falharam recentemente nesta etapa. |

Erros e *em andamento* são sinais independentes, portanto uma etapa pode exibir os dois selos ao mesmo tempo — assim você vê uma falha mesmo enquanto outro trabalho ainda está em execução. Use **Atualizar** (canto superior direito) para obter os números mais recentes.

## Tarefas agendadas

A aba Tarefas agendadas lista os trabalhos recorrentes em segundo plano que mantêm o DocBits em funcionamento (atualizações de cache, alertas de status, tempos limite de documentos, sincronizações de saída e mais) e confirma que cada um é disparado no horário.

<figure><img src="../../.gitbook/assets/infrastructure_scheduled.png" alt="Tabela de tarefas agendadas"><figcaption><p>Trabalhos recorrentes em segundo plano e seu status de agendamento</p></figcaption></figure>

| Coluna | Descrição |
|--------|-----------|
| **Tarefa** | O nome do trabalho agendado. |
| **Última execução** | Há quanto tempo foi executado. Passe o mouse para ver o carimbo de data/hora exato; *«Nunca executado»* significa que ainda não foi disparado. |
| **Status** | Status de agendamento (veja abaixo). |

Valores de status:

| Selo | Significado |
|------|-------------|
| **No horário** (verde) | A tarefa é executada no intervalo esperado. |
| **Atrasada** (vermelho) | A tarefa não foi executada quando esperado — vale investigar ou relatar ao suporte. |
| **Desconhecido** (cinza) | Não foi possível determinar o status de agendamento. |

Use **Atualizar** para verificar novamente o status de agendamento sob demanda.
