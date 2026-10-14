# Notas de versão DocBits — 30 de junho – 3 de julho de 2026

_O que esta atualização de produção trouxe, em linguagem simples. Cada serviço
mostra a versão agora em produção. Os serviços não listados não tiveram alterações
visíveis para o cliente nesta janela._

---

## Destaques

- **Chat de IA nos Activity Logs.** Um novo painel de chat de IA na página
  Activity Logs permite-lhe colocar perguntas sobre a atividade dos registos
  diretamente, sem ter de vasculhar entradas em bruto.
- **Registo de importação de e-mails de saída.** O registo de importação passa
  agora a registar também o correio de saída, além do de entrada, com filtros
  rápidos de Erros / Entrada / Saída — as caixas de correio com falhas
  repetidas são agora desativadas automaticamente, os administradores podem
  ser notificados por e-mail quando uma importação falha, e as repetições
  chegam agora até 15 tentativas ao longo de cerca de 5 horas antes de
  desistir.
- **Erros de importação de e-mail mais claros.** As falhas de início de sessão
  mostram agora o motivo real subjacente, com mensagens dedicadas para um
  certificado inválido ou uma palavra-passe de aplicação do Gmail incorreta.
- **Ciclo de início de sessão corrigido.** Alguns utilizadores podiam ficar
  presos num ciclo repetido de início de sessão durante a renovação do token —
  resolvido.
- **Processamento de documentos mais estável.** Corrigida uma falha durante a
  extração de dados causada por valores de coordenadas não arredondados, a
  leitura de códigos de barras repete agora as falhas recuperáveis em vez de
  desistir silenciosamente, e foi corrigido um caso raro em que um documento
  podia ser exportado duas vezes em simultâneo.
- **Melhorias no ecrã de validação.** Agora pode ampliar mais os documentos, os
  campos deixam de ser limpos por scripts quando o seu valor não mudou
  realmente, e o dashboard memoriza a sua posição de página quando volta
  atrás.

---

## Web App — em produção: `10.35.7`

- **Painel de chat de IA** adicionado à página Activity Logs (#15512).
- **Registo de importação:** novos filtros rápidos Erros / Entrada / Saída;
  interruptor e campo de destinatários da notificação de falha nas definições
  de e-mail de entrada.
- **Ecrã de validação:** o zoom do documento vai agora além do tamanho
  predefinido anterior; os campos esvaziados por scripts de validação mantêm
  agora corretamente o seu valor quando o script devolve o mesmo valor.
- **Dashboard:** a posição da página é mantida ao voltar à tabela; o cursor de
  redimensionamento de colunas já não ultrapassa o cabeçalho da tabela.
- **Ecrã Auto Accounting:** corrigido um erro de validação.
- **DocBits Tasks:** corrigido um problema de permissões.
- **Registos do Watchdog:** adicionado um filtro de intervalo de datas e um
  seletor ajustável de linhas por página.
- **Correções:** um erro de gráfico ("Element not found") na página Boards;
  uma ligação de eliminação de exportação quebrada nos Activity Logs;
  correções de layout no ecrã Layout Builder; uma tradução em falta no filtro
  de intervalo de datas dos Activity Logs.
- **Atualização automática:** mais robustez no mecanismo de atualização
  automática da aplicação (limpeza de arranque mais rápida, deteção de versão
  mais fiável, limpeza de cache antes de um recarregamento de recuperação).

## API Service — em produção: `12.48.1`

- **Carregamento mais rápido dos scripts de documento:** os scripts de
  validação são agora armazenados em cache no servidor (cache de 6 horas) em
  vez de serem obtidos de cada vez.
- **Confiança de montante mais precisa:** a pontuação de confiança tem agora
  em conta documentos que usam diferentes convenções de separador decimal.
- **Fiabilidade:** a validação de documentos executa sempre a única versão de
  script ativa, e a versão executada é agora registada; foi corrigido um caso
  raro em que um documento podia ser exportado duas vezes em simultâneo; as
  regras de extração específicas do fornecedor voltam a aplicar-se
  corretamente após um novo OCR forçado.
- **Importação de e-mail:** adicionado suporte de backend para o registo de
  correio de saída e para os e-mails de notificação de falha (ver Email
  Service, abaixo).

## Auth Service — em produção: `1.68.5`

- **Corrigido um ciclo de início de sessão** que alguns utilizadores podiam
  sofrer enquanto o token de sessão estava a ser renovado.
- **Ecrãs de administração de organização mais rápidos:** os dados de
  utilizadores e de subscrição são agora carregados em lote, em vez de um
  registo de cada vez.
- **Corrigido um conflito raro na base de dados** ao associar um utilizador a
  uma organização.

## Email Service — em produção: `1.37.4`

- **O registo de importação passa agora a monitorizar também o correio de
  saída**, além do de entrada, com um filtro para mostrar apenas importações
  de entrada, de saída ou falhadas.
- **As caixas de correio com falhas são agora desativadas automaticamente**
  após falhas repetidas, e os administradores podem ser notificados por
  e-mail quando uma importação falha; as repetições chegam agora até 15
  tentativas ao longo de cerca de 5 horas antes de desistir.
- **Mensagens de falha de início de sessão mais claras:** mostra o motivo real
  subjacente, uma mensagem dedicada para um certificado inválido e uma
  mensagem específica para uma palavra-passe de aplicação do Gmail incorreta.
- **Corrigido o encaminhamento de entrada** que reescrevia incorretamente os
  endereços de servidor para contas da região UE.
- Mais resiliente a quebras breves de ligação ao Redis.

## Extraction Service — em produção: `1.49.0`

- **Corrigida uma falha durante a extração** causada por valores de
  coordenadas não arredondados.
- **Confiança de montante mais precisa** para documentos com formatos mistos
  de separador decimal; pequenas diferenças de arredondamento no total de
  impostos já não bloqueiam uma correspondência.

## Docflow Service — em produção: `2.4.2`

- **Autenticação remodelada para workflows avançados (baseados em Celery)**,
  com proteções para que uma verificação de autenticação falhada já não possa
  fazer falhar a execução de um workflow.
- **Resposta mais clara** quando um passo de workflow tenta executar-se contra
  um workflow que já não existe.

## Barcode Service — em produção: `1.15.7`

- **A leitura de códigos de barras repete agora automaticamente** as falhas
  recuperáveis em vez de desistir silenciosamente.

## OCR Service — em produção: `1.7.3`

- **Corrigida uma falha de OCR** causada por um problema de resolução do nome
  de anfitrião (hostname) do Redis.
- As desconexões do Redis durante verificações de estado (health checks)
  deixam de ser registadas como erros, reduzindo os alertas falsos.

## PO Match Service — em produção: `1.55.8`

- **Corrigidas as notas que não apareciam** nos registos do PO Match.

---

## Sem alterações visíveis para o cliente nesta janela

Estáveis, sem alterações de produto notáveis entre 30 de junho – 3 de julho:
Auto Accounting (`1.18.7`), Docnet (`1.54.6`), FTP (`1.30.2`), Fulltext
(`1.35.7`), Operator (`1.39.5`). O Auto Accounting recebeu apenas manutenção
interna de configuração de implementação (deployment). O Ideas Service não
pôde ser contactado para uma verificação de versão durante esta janela.

<!-- Generated by the docbits-changelog skill (version-boundary mode, resolved
     from the prod version table supplied by the user). Window 2026-06-30 →
     2026-07-03. -->
