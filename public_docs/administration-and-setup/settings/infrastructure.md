# Infraestrutura

A página **Infrastructure** dá aos administradores uma visão atual de onde cada parte da plataforma é executada (EU ou US) e se o processamento está saudável. A página é só de leitura, portanto nada aqui é configurado.

> **Access:** Infrastructure é uma página apenas para administradores. Abra **Settings → Organization & Access → Infrastructure**.

A página tem três abas. Cada aba carrega os seus dados na primeira vez que é aberta, por isso alternar entre elas não volta a pedir tudo.

| Tab | Answers |
|-----|---------|
| **Topology** | Onde é executado cada componente e como é que um documento percorre o DocBits? |
| **Processing** | As etapas do processamento de documentos estão a ser executadas e o trabalho está a acumular-se? |
| **Scheduled Tasks** | As tarefas de fundo recorrentes são acionadas dentro do prazo? |

## Topology

**Topology** abre por predefinição. Mostra a plataforma em duas vistas: **Architecture** e **Process**. Use o comutador acima do diagrama para alternar entre elas; o indicador ao lado mostra **live** enquanto a vista transmite o seu estado.

Um aviso acima do diagrama resume a verificação de regiões:

* **Green**: todos os componentes são executados na região da sua organização e o aviso indica essa região (por exemplo **EU**).
* **Red**: um componente marcado como crítico é executado fora da região da sua organização.
* **Amber**: o aviso indica componentes que estão noutra região, embora a verificação global seja bem-sucedida. Trata-se de uma diferença de região, não de uma falha.

### Vista de arquitetura

A vista de arquitetura desenha a plataforma como faixas de cartões de componentes, por exemplo Edge / Web, Core API, Import, Background Services e Modules. As setas mostram as ligações entre os cartões.

Cada cartão mostra o nome do componente, um selo de região e, nos componentes críticos, um ponto de estado que fica verde quando o componente responde e mostra a latência em milissegundos quando é comunicado um valor.

| Badge | Meaning |
|-------|---------|
| **EU ✓** / **US ✓** | O componente é executado na região da sua organização. |
| **SHARED** | Um componente global como o CDN, sem uma região única. É o esperado. |
| **EU ⓘ** / **US ⓘ** | O componente é executado noutra região e é comunicado como aviso. |
| **EU ⚠** / **US ⚠** | O componente é executado noutra região e é comunicado como erro. Comunique-o ao suporte. |
| Selo cinzento, sem marca | A região deste componente não é conhecida. |

### Vista de processo

A vista de processo anima um único documento pela pipeline: as fontes de entrada **Email**, **FTP** e **Web** convergem em **API** e depois passam por **OCR**, **Extraction**, **PO matching**, **Auto Accounting** e **Export**. Cada etapa liga-se a uma barra de armazenamento de dados com **Postgres** e armazenamento de ficheiros. Uma legenda indica a etapa que está a ser animada e o botão de reprodução pausa ou retoma a animação.

PO matching e Auto Accounting são opcionais. Quando um deles está desativado para a sua organização, a etapa correspondente fica cinzenta e a animação salta-a.

### Módulos opcionais

Os módulos opcionais (Full-Text Search, DocFlow, Auto-Accounting, DocNet e PO Matching) têm no cartão um selo **active** ou **inactive**. Um módulo desativado oferece um botão **Activate** que o leva à página onde o ativa: as definições de Modules para a maioria dos módulos, ou **Document Types** para o PO Matching, que é ativado por tipo de documento.

## Processing

A aba **Processing** lista as etapas do processamento de documentos da sua organização e indica se o trabalho está a fluir ou a acumular-se.

| Column | Description |
|--------|-------------|
| **Process** | A etapa de processamento: Document Processing, OCR, TR-OCR, Barcode Split, Barcode Extraction, Extraction e PO Match. |
| **Last run** | Há quanto tempo a etapa foi executada pela última vez. Passe o cursor por cima para ver o registo de data e hora exato. **Never run** significa que nenhum documento chegou ainda a esta etapa. |
| **Status** | Um ou mais selos (ver abaixo). |

Os selos de estado são sinais independentes:

* Selo vermelho **Errors (N)**: `N` documentos falharam recentemente nesta etapa.
* Selo âmbar com uma contagem: `N` documentos estão a ser processados por esta etapa neste momento.
* Selo verde **OK**: sem erros recentes e nada em espera.

Como os erros e o trabalho em curso são contados em separado, uma etapa pode mostrar ambos ao mesmo tempo, pelo que uma falha continua visível enquanto outros documentos estão a ser processados.

## Scheduled Tasks

A aba **Scheduled Tasks** lista as tarefas de fundo recorrentes que mantêm o DocBits a funcionar, por exemplo atualizações de cache, alertas de estado, tempos limite de documentos e sincronizações de saída. Cada linha indica se a tarefa é acionada a horas.

| Column | Description |
|--------|-------------|
| **Task** | O nome da tarefa agendada, com os separadores substituídos por espaços. |
| **Last run** | Há quanto tempo foi executada pela última vez. Passe o cursor por cima para ver o registo de data e hora exato. **Never run** significa que ainda não foi acionada. |
| **Status** | Estado do agendamento (ver abaixo). |

| Status | Meaning |
|--------|---------|
| **On schedule** (verde) | A tarefa é executada no intervalo esperado. |
| **Delayed** (vermelho) | A tarefa não foi executada quando era esperada. Investigue ou comunique ao suporte. |
| **Unknown** (cinzento) | Não foi possível determinar o estado do agendamento. |

Ambas as tabelas têm um botão **Refresh** que recarrega os valores atuais a pedido.
