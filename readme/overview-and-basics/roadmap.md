# Roadmap do DocBits

_Estado do planeamento a 18 de setembro de 2026. Cada versão indica a data de
sandbox planeada (quando os clientes a podem testar) e a data de produção
planeada. Os temas descrevem o que está planeado para a versão, não o que já
foi entregue; o âmbito e as datas podem mudar. Os hotfixes entre versões estão
documentados nas [Notas de versão](release-notes/README.md)._

| Versão | Sandbox | Produção |
|---|---|---|
| R1.1 | 5 de outubro de 2026 | 14 de outubro de 2026 |
| R1.2 | 23 de novembro de 2026 | 2 de dezembro de 2026 |
| R1.3 | 8 de fevereiro de 2027 | 17 de fevereiro de 2027 |
| R1.4 | 7 de abril de 2027 | 15 de abril de 2027 |
| R1.5 | 18 de maio de 2027 | 27 de maio de 2027 |
| R1.6 | 6 de julho de 2027 | 15 de julho de 2027 |
| R1.7 | 21 de setembro de 2027 | 30 de setembro de 2027 |
| R2.0 | a anunciar | a anunciar |

---

## R1.1 — Sandbox 5 de outubro de 2026 · Produção 14 de outubro de 2026

**Regras de transformação e layouts**

- Um motor de regras para os valores extraídos de campos e colunas: definir,
  substituir ou derivar valores com grupos de condições aninhados, com um ecrã
  de definições para gerir as regras. As regras de seleção de layout recebem
  as mesmas condições aninhadas.
- A seleção de layout funciona independentemente da origem do documento.
- Regras de precedência claras para as etiquetas de campo nos campos de
  cabeçalho e nas colunas de tabela.
- Uma coluna de tabela pode voltar a ser atribuída depois de ter sido
  eliminada, e a tabela de preços de artigos de fornecedor mostra todas as
  suas colunas.

**Ecrãs de aprovação e validação**

- As três tabelas de linhas de artigos do ecrã de aprovação (linhas da fatura,
  linhas de comparação, correspondência de PO) partilham um único estilo, e a
  vista de comparação mostra o número de artigo que pertence à linha.
- O último painel lateral aberto (fluxo de atividade ou histórico de
  aprovação) é memorizado por utilizador.
- Fundir documentos a partir do ecrã de aprovação com o carregador de
  documentos.
- As regras de validação personalizadas tratam os custos de envio de forma
  genérica, e as regras que reportavam um falso negativo foram corrigidas.
- Uma barra de carregamento substitui o simples ícone de carregamento; URLs de
  página mais amigáveis.

**Deteção de duplicados**

- Os campos personalizados aparecem no resultado da deteção de duplicados, e
  as definições de duplicados podem ser pesquisadas.

**Fluxos de trabalho e tarefas**

- Um botão "New workflow", registos para fluxos de trabalho avançados, um ecrã
  de registo do watchdog mais claro, e os passos de fluxo de trabalho que
  alteram um campo ou uma caixa de seleção são aplicados de forma fiável.
- Adicionar uma linha numa árvore de decisão mantém os nomes dos utilizadores
  em vez de mostrar IDs.
- Todas as mudanças de estado de um documento são registadas.
- A criação de um novo modelo de e-mail volta a funcionar.

**Importação**

- A importação de e-mail só move uma mensagem para fora da caixa de entrada
  depois de o carregamento ser confirmado, trata um reencaminhamento
  reentregue como uma única entrega, regista quem guardou pela última vez e
  aceita mensagens assinadas com S/MIME.
- A importação FTP recebe uma verdadeira opção de eliminar após a importação,
  ao lado de mover e arquivar.
- O carregamento a partir da aplicação de scanner volta a funcionar.
- Os ficheiros BOD de ordens de compra carregados na região dos EUA
  permanecem na região dos EUA.

**Processamento de documentos e extração**

- Quando o serviço de códigos de barras bloqueia, o documento mostra o erro em
  vez de ficar em "Processing" indefinidamente.
- Um novo nível de modelo de IA mais económico ("Eco") para a extração.
- Com a extração estruturada por IA, os números de artigo de fornecedor
  treinados mantêm-se treinados, e o número de artigo e o número de artigo de
  fornecedor deixam de ser trocados.
- Os modelos de documentos eletrónicos UBL são ajustados; correções de
  extração para montantes, taxas de imposto, preços unitários e números de
  ordem de compra em layouts específicos de fornecedores.
- São reconhecidos formatos de data adicionais.

**Correspondência de ordens de compra**

- A correspondência exige uma coluna de quantidade, usa o preço por quantidade
  da unidade base, e o fallback da última linha pode ser ativado ou desativado
  por cliente.
- As linhas de guia de remessa podem ser selecionadas individualmente.
- O ecrã de documentos eletrónicos deixa de congelar em faturas com mais de
  250 linhas.

**Touchless Intelligence**

- Mais detalhe no relatório Touchless, e a caixa de seleção Touchless reflete
  a definição guardada.

**Dashboard**

- O dashboard pode conter até 10.000 documentos por pesquisa.
- A data de vencimento do desconto e a data de vencimento da fatura estão
  disponíveis como campos de layout e são preenchidas na importação.
- Os utilizadores com quem um dashboard é partilhado mantêm-se quando o
  dashboard é guardado, e "Updated by" mostra a pessoa certa.
- Os documentos arquivados podem ser retirados do estado "Archived".

**Exportação e EDI**

- Um passo de exportação Infor M3 adicional para informação de fatura extra.
- Uma lista de embalagem (packing list) com vários números de contentor é
  exportada como um registo por contentor.
- A reimportação de uma receção de entrega (receive delivery) deixa de falhar
  com uma chave duplicada, e os BOD de receção de entrega são aplicados pela
  ordem certa.
- Os mapeamentos EDI para fatura, ordem de compra e confirmação de encomenda
  são atualizados.

**Segurança**

- A proteção de organização para chaves de API é aplicada em todos os
  ambientes.

---

## R1.2 — Sandbox 23 de novembro de 2026 · Produção 2 de dezembro de 2026

**Aprovação e correspondência de ordens de compra**

- Um estado "Pending input" coloca um documento em pausa até alguém responder,
  sem quebrar o fluxo de trabalho nem o histórico de auditoria, e os
  aprovadores podem fazer perguntas sem interromper o fluxo de aprovação.
- As faturas de pré-pagamento podem ser correspondidas antes da receção de
  mercadorias enquanto "Match on received quantity" se mantém ativo.
- Uma flag de disponibilidade de receção compara as quantidades faturadas e
  recebidas.
- Confirmações de encomenda: elementos de custo mostrados enquanto a aprovação
  está pendente, posições de sobretaxa com código de cores na correspondência
  de PO, e a coluna de número de artigo nas linhas de artigos da fatura.
- As colunas que não estão mapeadas deixam de alimentar o cálculo do montante
  da tabela.
- As linhas RMA de fornecedor são tratadas.

**Importação e classificação**

- O endereço do remetente fica disponível a partir da importação de e-mail.
- O tipo de fornecedor é derivado das linhas de artigos.

**Definições e automatização**

- O script "Set sub-organisation" passa a ser uma regra de transformação.
- As colunas padrão podem ser removidas de um tipo de documento.

**Exportação**

- O histórico de exportação volta a listar os documentos exportados.
- As faturas de frete são exportadas para o Infor LN.

---

## R1.3 — Sandbox 8 de fevereiro de 2027 · Produção 17 de fevereiro de 2027

**Rule Manager do Auto Accounting**

- As regras atribuem contas e dimensões automaticamente, delimitadas por
  suborganização e tipo de documento, com um ecrã de auditoria que mostra qual
  a regra que disparou.
- Uma regra pode preencher um valor a partir de uma coluna de linha de tabela.
- Os campos e as dimensões podem ser limpos individualmente, as linhas de
  artigos podem ser eliminadas (incluindo linhas sem montante), e as regras
  continuam a funcionar em campos que passaram de texto para lista pendente.

**Correspondência de ordens de compra**

- O ícone de correspondência navega, desloca e realça entre separadores,
  incluindo correspondências um-para-muitos.
- Conversão de unidades com aliases (por exemplo, KG e TO), uma variância de
  arredondamento configurável com uma conta de arredondamento, e cálculos com
  quatro casas decimais apresentados com três.

**Exportação**

- Nomes de ficheiros de exportação configuráveis.
- Um documento incompleto no Infor LN é eliminado após uma exportação falhada.
- O conector de base de dados inclui todas as tabelas relevantes.

---

## R1.4 — Sandbox 7 de abril de 2027 · Produção 15 de abril de 2027

**Importação**

- Um mecanismo de novas tentativas para a importação FTP, de e-mail e de
  e-mail de entrada, com reprocessamento automático e manual.

**DocNet Agents**

- Entrada de encomendas: uma encomenda de cliente torna-se uma ordem de venda
  no Infor M3 ou no Infor LN (primeira versão, documentos de texto).

**Aprovação**

- Um fluxo de aprovação melhorado, delegação noutro utilizador durante a
  aprovação, e um botão "Export & Next".

**Correspondência de ordens de compra**

- Só as linhas de PO viáveis são oferecidas no ecrã de correspondência.
- As faturas com correspondência em excesso, em que a quantidade faturada
  excede a quantidade recebida, são reconhecidas no ecrã de correspondência, e
  as unidades de medida são convertidas durante a correspondência da fatura.

**Outros**

- Ronda de feedback sobre o Rule Manager.
- O formulário de pedido de suporte aceita anexos e associa a organização
  automaticamente.
- Integração fiscal Vertex alargada.

---

## R1.5 — Sandbox 18 de maio de 2027 · Produção 27 de maio de 2027

**Auto Accounting**

- Ação de pesquisa (lookup) do Rule Manager: fazer corresponder dados mestre e
  atribuir vários campos de uma só vez.
- As previsões suportam vários códigos de imposto e dimensões, vouchers e
  referências de lançamento.
- Ecrãs de Auto Accounting em vários idiomas.

**Aprovação e correspondência de ordens de compra**

- Reatribuir um documento a outro utilizador.
- A ordem das colunas no ecrã de correspondência de PO é guardada por
  utilizador.
- Os códigos de encargos (portagem, transporte, energia) são reconhecidos e o
  seu custo é distribuído.

**Proteções de exportação**

- A exportação é bloqueada com um aviso quando a quantidade correspondida
  excede ou difere demasiado da quantidade recebida, ou quando a data de
  lançamento é anterior à data de entrada em armazém.

**Usabilidade**

- A ordem de execução dos scripts de documento é visível no frontend.
- As teclas Enter e Tab percorrem os campos no teclado.

---

## R1.6 — Sandbox 6 de julho de 2027 · Produção 15 de julho de 2027

**Definições**

- As definições podem ser pesquisadas em todos os botões de alternância e
  subpáginas.
- A configuração do servidor de e-mail permite substituir um segredo OAuth ou
  de cliente expirado sem voltar a configurar a caixa de correio.
- O mapa de números de artigo de fornecedor (tabela de conversão de números
  de artigo) pode ser preenchido a partir de uma importação CSV.

**Auto Accounting**

- As dimensões são guardadas numa nova estrutura para que grandes conjuntos
  de dimensões carreguem mais depressa.

---

## R1.7 — Sandbox 21 de setembro de 2027 · Produção 30 de setembro de 2027

**Auto Accounting no ecrã de aprovação**

- Os aprovadores podem trabalhar com o Auto Accounting diretamente no ecrã de
  aprovação.
- A aprovação pode ficar condicionada a campos contabilísticos, como o código
  nominal ou o país, com uma correção de contas a pagar (AP) quando um
  documento é devolvido.
- Uma lista pendente de código de imposto no Auto Accounting sem configurar
  várias linhas de imposto.

---

## R2.0 — Sandbox a anunciar · Produção a anunciar

**Auto Accounting**

- Os campos suportados por uma lista também aceitam texto livre.
- Os campos obrigatórios são validados.
- As previsões do modelo preenchem os campos contabilísticos automaticamente
  (modo híbrido com o modelo de previsão treinado), com um registo de
  auditoria do que o modelo preencheu.

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-09-18 by the
     docbits-roadmap skill. Themes only; ticket keys, customer names and
     internal work are deliberately left out. Rerun the skill to refresh. -->
