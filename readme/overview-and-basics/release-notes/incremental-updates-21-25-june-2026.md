# Notas de Versão do DocBits — 21–25 de junho de 2026

_O que esta atualização de produção trouxe, em linguagem simples. Cada serviço mostra
a versão agora ativa em produção. Os serviços não listados não tiveram alterações
visíveis para o cliente nesta janela._

---

## Destaques

- **Pesquisa no painel mais inteligente.** Pesquise documentos de forma confiável por
  valores e números — encontre faturas acima de um valor, ou pesquise por **número de
  requisição** — com intervalos de valores que comparam números reais, e não texto. Os
  subtipos de fatura podem ser pesquisados pelos seus nomes traduzidos.
- **Notificações por e-mail confiáveis.** Os alertas de mudança de status agora são
  enviados para todos os status (nada mais de e-mails descartados silenciosamente), e os
  comprovantes de importação recebida e os avisos de falha agora exibem corretamente a
  identidade visual do DocBits, com controles por destinatário.
- **Login mais fluido entre regiões (EU/US).** A troca de região agora é um pequeno
  banner em vez de uma interrupção em tela cheia, o single sign-on chega à região
  correta, e manter a sessão iniciada em várias abas do navegador é mais confiável.
- **Correções de permissões.** Os usuários obtêm o acesso que o seu grupo lhes concede —
  abrir, editar, aprovar e reiniciar documentos agora funciona corretamente mesmo quando
  os grupos e as permissões estão configurados de maneiras menos comuns.
- **Processamento de documentos mais estável.** Os documentos que antes ficavam presos
  após o upload são retomados automaticamente, e um pico de volume de um cliente já não
  deixa os demais mais lentos.

---

## Web App — ativo: `10.32.4`

- **Salto da pesquisa rápida (Cmd/Ctrl + K)** direto para a configuração de **Validação
  de E-Fatura**.
- **Região e login:** a troca de região é exibida como um banner persistente em vez de
  uma tela bloqueante; o single sign-on agora redireciona para a região correta (EU/US);
  manter a sessão iniciada em várias abas é mais confiável.
- **Permissões:** corrigidos os casos em que os usuários não conseguiam **aprovar**,
  **editar**, **abrir** ou **reiniciar** documentos apesar de terem as permissões de
  grupo corretas.
- **Configurações de e-mail recebido:** novas opções “Notificar remetente” e “Responder
  ao remetente no recebimento”.
- **Usabilidade:** o aviso de documento duplicado agora precisa ser dispensado antes de
  continuar; o banner de “backend indisponível” só aparece durante interrupções reais;
  os contadores de tarefas são atualizados imediatamente quando as tarefas são
  concluídas; correção do modo escuro na tela de validação de tabelas de IA.
- **Desempenho:** corrigido um travamento na tela de e-documentos durante a validação de
  campos e o PO matching.
- **Pesquise subtipos de fatura pelos seus nomes traduzidos.**

## API Service — ativo: `12.41.9`

- **Reformulação da pesquisa no painel:** o número de requisição e o requisitante agora
  podem ser pesquisados; as pesquisas por valores e números retornam resultados corretos
  (comparação numérica real); o valor líquido total e as colunas calculadas são exibidos
  corretamente.
- **E-mails de alerta de status confiáveis** para qualquer status de documento, sem que
  as falhas de envio fiquem mais ocultas.
- **Permissões:** os usuários sem grupo podem abrir e aprovar os seus próprios
  documentos; a visibilidade de documentos para usuários sem grupo foi restaurada.
- **Confiabilidade do processamento de documentos:** os documentos presos em “novo” são
  recolocados automaticamente na fila; processamento com partilha justa para que um
  grande pico de uma organização não prejudique as demais; auto-recuperação para
  problemas raros de sequência de banco de dados.
- **PDFs digitalizados com uma camada de texto corrompida são encaminhados para o OCR**
  em vez de produzir texto pouco confiável.
- **Precisão de extração e PO:** o nome do fornecedor é preenchido a partir do pedido de
  compra vinculado; colunas duplicadas de número de item removidas; melhor tratamento de
  espaços especiais (não separáveis).
- **Exportação Infor ERP / SAP:** corrigida a autenticação da exportação por SFTP.
- **Faturamento eletrônico:** refinamentos no caminho de extração ZUGFeRD / e-documentos.

## Auth Service — ativo: `1.66.0`

- **Corrigida a atribuição de organização ausente** para alguns usuários (id de
  organização vazio).

## Docflow Service — ativo: `2.3.4`

- **O tempo de espera do gatilho de fluxo de trabalho** agora é configurável por
  ambiente.

## Email Service — ativo: `1.35.9`

- **E-mails com identidade visual:** os comprovantes de importação recebida e os avisos
  de falha agora usam o logotipo e as cores reais do DocBits.
- **Controles por organização:** e-mail de confirmação no recebimento, “notificar
  remetente” em caso de falha, e opções de responder ao remetente.
- **Importação recebida mais confiável:** os resultados da importação são registrados
  corretamente, as falhas parciais são reportadas como falhas (e não como sucessos
  silenciosos), e os caracteres problemáticos no corpo dos e-mails já não quebram a
  importação.
- **Roteamento EU/US:** roteamento por organização para a API regional correta.

## Fulltext Service — ativo: `1.34.5`

- **Pesquisa por valores e números** agora funciona de forma confiável, incluindo
  separadores de milhares e intervalos de valores (o mecanismo por trás da reformulação
  da pesquisa no painel).
- **Infraestrutura de pesquisa mais estável:** as filas de processamento em segundo plano
  órfãs são limpas para que já não retenham recursos compartilhados.

## PO Match Service — ativo: `1.54.7`

- **Correspondência de pedidos de compra mais robusta:** os códigos de embalagem/unidade
  de embalagem baseados em texto já não bloqueiam uma correspondência, e a correspondência
  manual de linhas trata resultados vazios com segurança.

---

## Sem alterações visíveis para o cliente nesta janela

Estável, sem alterações de produto notáveis entre 21 e 25 de junho: Auto Accounting
(`1.18.5`), Barcode (`1.15.6`), Docnet (`1.54.6`), Extraction (`1.48.6`), FTP (`1.30.0`),
OCR (`1.6.8`), Operator (`1.39.5`).

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-21 → 2026-06-25. -->
