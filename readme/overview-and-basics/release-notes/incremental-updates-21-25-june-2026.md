# Notas de versão DocBits — 21–25 de junho de 2026

_O que esta atualização de produção trouxe, em linguagem simples. Cada serviço
mostra a versão agora em produção. Os serviços não listados não tiveram alterações
visíveis para o cliente nesta janela._

---

## Destaques

- **Pesquisa mais inteligente no dashboard.** Pesquise documentos de forma fiável
  por montantes e números — encontre faturas acima de um valor, ou pesquise por
  **número de requisição** — com intervalos de montantes que comparam números
  reais, não texto. Os subtipos de fatura podem ser pesquisados pelos seus nomes
  traduzidos.
- **Notificações por e-mail fiáveis.** Os alertas de mudança de estado são agora
  enviados para todos os estados (sem mais e-mails descartados silenciosamente), e
  os recibos de importação recebida e os avisos de falha estão agora devidamente
  identificados com a marca DocBits, com controlos por destinatário.
- **Início de sessão mais fluido entre regiões (EU/US).** A troca de região é agora
  um pequeno banner em vez de uma interrupção em ecrã inteiro, o single sign-on
  aterra na região correta, e manter a sessão iniciada em vários separadores do
  navegador é mais fiável.
- **Correções de permissões.** Os utilizadores obtêm o acesso que o seu grupo lhes
  concede — abrir, editar, aprovar e reiniciar documentos funciona agora
  corretamente mesmo quando grupos e permissões estão configurados de formas menos
  comuns.
- **Processamento de documentos mais estável.** Os documentos que anteriormente
  ficavam presos após o carregamento são automaticamente retomados, e um pico de um
  cliente já não abranda os outros.

---

## Web App — em produção: `10.32.4`

- **Salto de pesquisa rápida (Cmd/Ctrl + K)** diretamente para a definição
  **E-Invoice Validation**.
- **Região e início de sessão:** troca de região apresentada como um banner
  persistente em vez de um ecrã bloqueante; o single sign-on redireciona agora para
  a região correta (EU/US); manter a sessão iniciada em vários separadores é mais
  fiável.
- **Permissões:** corrigidos casos em que os utilizadores não conseguiam
  **aprovar**, **editar**, **abrir** ou **reiniciar** documentos apesar de terem as
  permissões de grupo corretas.
- **Definições de e-mail de entrada:** novas opções "Notify sender" e "Reply to
  sender on receipt".
- **Usabilidade:** o aviso de documento duplicado tem agora de ser descartado antes
  de continuar; o banner "backend unavailable" só aparece durante interrupções
  reais; os contadores de tarefas atualizam imediatamente quando as tarefas são
  concluídas; correção do modo escuro no ecrã de validação de tabelas por IA.
- **Desempenho:** corrigido um congelamento no ecrã de e-document durante a
  validação de campos e o PO matching.
- **Pesquise subtipos de fatura pelos seus nomes traduzidos.**

## API Service — em produção: `12.41.9`

- **Revisão da pesquisa no dashboard:** o número de requisição e o requisitante são
  agora pesquisáveis; as pesquisas por montante e número devolvem resultados
  corretos (comparação numérica verdadeira); o montante líquido total e as colunas
  calculadas apresentam-se corretamente.
- **E-mails de alerta de estado fiáveis** para qualquer estado do documento, com as
  falhas de envio já não ocultadas.
- **Permissões:** os utilizadores sem grupo podem abrir e aprovar os seus próprios
  documentos; a visibilidade de documentos para utilizadores sem grupo foi
  restaurada.
- **Fiabilidade do processamento de documentos:** os documentos presos em "new" são
  automaticamente recolocados na fila; processamento com partilha justa para que um
  grande pico de uma organização não prive as outras de recursos; auto-recuperação
  para problemas raros de sequência da base de dados.
- **Os PDFs digitalizados com uma camada de texto danificada são encaminhados para
  OCR** em vez de produzirem texto pouco fiável.
- **Precisão da extração e do PO:** o nome do fornecedor é preenchido a partir da
  ordem de compra associada; colunas de número de artigo duplicadas removidas;
  melhor tratamento de espaços especiais (não separáveis).
- **Exportação Infor ERP / SAP:** corrigida a autenticação da exportação SFTP.
- **Faturação eletrónica:** refinamentos no percurso de extração de ZUGFeRD /
  e-document.

## Auth Service — em produção: `1.66.0`

- **Corrigida a atribuição de organização em falta** para alguns utilizadores (org
  id vazio).

## Docflow Service — em produção: `2.3.4`

- **O período de arrefecimento (cooldown) do gatilho de workflow** é agora
  configurável por ambiente.

## Email Service — em produção: `1.35.9`

- **E-mails com a marca:** os recibos de importação recebida e os avisos de falha
  usam agora o logótipo e as cores reais do DocBits.
- **Controlos por organização:** e-mail de confirmação na receção, "notify sender"
  em caso de falha e opções de reply-to-sender.
- **Importação de entrada mais fiável:** os resultados da importação são registados
  corretamente, as falhas parciais são reportadas como falhas (e não como sucessos
  silenciosos), e os caracteres problemáticos no corpo dos e-mails já não quebram a
  importação.
- **Encaminhamento EU/US:** encaminhamento por organização para a API regional
  correta.

## Fulltext Service — em produção: `1.34.5`

- **A pesquisa por montantes e números** funciona agora de forma fiável, incluindo
  separadores de milhares e intervalos de montantes (o motor por trás da revisão da
  pesquisa no dashboard).
- **Infraestrutura de pesquisa mais estável:** as filas de segundo plano órfãs são
  limpas para que já não retenham recursos partilhados.

## PO Match Service — em produção: `1.54.7`

- **Correspondência de ordens de compra mais robusta:** os códigos de
  embalagem/unidade de embalagem baseados em texto já não bloqueiam uma
  correspondência, e a correspondência manual de linhas trata os resultados vazios
  de forma segura.

---

## Sem alterações visíveis para o cliente nesta janela

Estáveis, sem alterações de produto notáveis entre 21–25 de junho: Auto Accounting
(`1.18.5`), Barcode (`1.15.6`), Docnet (`1.54.6`), Extraction (`1.48.6`), FTP
(`1.30.0`), OCR (`1.6.8`), Operator (`1.39.5`).

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-21 → 2026-06-25. -->
