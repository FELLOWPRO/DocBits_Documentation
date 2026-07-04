# Notas de versão DocBits — 3–4 de julho de 2026

_O que esta atualização de produção trouxe, em linguagem simples. Cada serviço
mostra a versão agora em produção. Os serviços não listados não tiveram alterações
visíveis para o cliente nesta janela._

---

## Destaques

- **Implementações mais limpas, em toda a frota.** Vários serviços centrais
  (API, Auto Accounting, Docflow, Extraction, OCR, PO Match) encerram agora
  corretamente durante uma release, pelo que uma implementação contínua
  (rolling deploy) deixa de correr o risco de interromper um pedido que já
  estava em curso.
- **Melhorias na exportação de faturas eletrónicas.** A exportação de um
  documento para múltiplas configurações de exportação em simultâneo é agora
  mais fiável — as verificações de exportação duplicada passam a ser
  executadas uma vez por lote, em vez de uma vez por item, e um novo endpoint
  de exportação evita que o estado de exportação oscile quando várias
  exportações são acionadas em conjunto. Os documentos XRechnung/ZUGFeRD
  também passam a ter um mapeamento de campos mais consistente.
- **Processamento de documentos mais estável.** Corrigida uma falha que podia
  derrubar um documento OCR inteiro quando uma única página falhava,
  corrigida a sincronização de entregas de Ordens de Compra que só obtinha os
  primeiros 100 registos, e reforçada a resiliência de vários serviços a
  quebras breves de ligação à base de dados.
- **Anexos de e-mail recuperados.** Corrigido um caso em que os anexos de
  e-mail podiam chegar corrompidos ou com bytes em falta durante a
  importação de entrada.
- **Fiabilidade dos workflows.** Corrigidos workflows que ficavam bloqueados
  devido a um lock que não era libertado corretamente, e corrigida a lógica
  de reagendamento para que os passos de workflow ignorados sejam tratados e
  registados corretamente.
- **Novo: Ideas Service.** Um novo serviço de backend (Ideas, v0.3.0)
  juntou-se à frota de produção.

---

## API Service — em produção: `12.52.4`

- **Fiabilidade do OCR:** uma falha numa única página deixa agora de fazer
  falhar o documento inteiro.
- **Exportação:** as verificações de exportação duplicada passam a ser
  executadas uma vez por lote, em vez de uma vez por item; um novo endpoint
  de exportação evita que o estado de exportação oscile quando várias
  exportações são executadas em simultâneo; os documentos XRechnung/ZUGFeRD
  passam a ter um mapeamento de campos canónico mais consistente.
- **Ordens de Compra:** corrigida a sincronização de entregas que só obtinha
  os primeiros 100 registos por ordem.
- **Activity Logs:** corrigido o botão de página "Seguinte" que saltava para
  uma janela temporal não relacionada.
- **Master Data Lookup:** corrigido um erro de servidor (HTTP 500).
- **Indexação de pesquisa:** adicionado um marcador de confirmação de entrega
  e nova tentativa, para que os documentos sejam colocados de forma fiável na
  fila para a pesquisa full-text.
- Correções gerais de estabilidade que resolvem vários erros recorrentes em
  segundo plano.

## Auth Service — em produção: `1.68.7`

- Apenas fiabilidade e manutenção internas nesta janela.

## Auto Accounting — em produção: `1.18.8`

- **Encerramentos mais limpos** durante as implementações, evitando pedidos
  em curso interrompidos.

## Barcode Service — em produção: `1.15.8`

- Apenas uma correção interna de configuração de implementação nesta janela.

## Docflow Service — em produção: `2.5.3`

- **Nova opção de exportação** para enviar um documento para múltiplas
  configurações de exportação em simultâneo.
- **Corrigidos workflows que ficavam bloqueados** devido a um lock que não
  era libertado corretamente, independentemente do estado.
- **Corrigido o reagendamento de workflows**, para que os passos ignorados
  sejam tratados e registados corretamente, em vez de serem descartados
  silenciosamente.
- **Arranque mais rápido:** as bases de dados são agora pré-aquecidas em
  segundo plano.
- Mais resiliente a quebras breves de ligação à base de dados.
- Melhorada a interpretação de campos de data nos cartões de workflow.

## Email Service — em produção: `1.37.9`

- **Corrigidos anexos de entrada** que podiam chegar corrompidos ou com
  bytes em falta.
- **Erros mais claros** quando uma pasta de caixa de correio não pode ser
  obtida, em vez de uma falha genérica.

## Extraction Service — em produção: `1.49.6`

- **Corrigidas falhas** em documentos com um tipo de documento não
  reconhecido e em tabelas com uma estrutura invulgar/malformada.
- Mais resiliente a quebras breves de ligação à base de dados a meio de uma
  consulta.

## FTP Service — em produção: `1.30.3`

- Apenas uma atualização interna de framework nesta janela.

## Fulltext Service — em produção: `1.36.3`

- **Indexação de pesquisa:** uma verificação periódica repara agora quaisquer
  documentos que não tenham chegado ao índice de pesquisa, para qualquer
  organização.
- **Sincronização com o ERP:** corrigido um lock bloqueado que podia impedir
  a sincronização com o ERP após uma nova tentativa falhada.

## OCR Service — em produção: `1.7.8`

- **Corrigida a autenticação do OCR**, para que as chaves API da organização
  voltem a funcionar corretamente.
- Encerramentos mais limpos durante as implementações.

## Operator Service — em produção: `1.39.7`

- Apenas correções internas de fiabilidade de implementação nesta janela.

## PO Match Service — em produção: `1.56.0`

- **Corrigida uma falha** ao ordenar quantidades de PO Match que incluíam
  valores vazios.
- Encerramentos mais limpos durante as implementações.

## Web App — em produção: `10.36.9`

- **Corrigido um erro** ao regressar à Validação de Campos a partir de outro
  ecrã.
- **Corrigido o botão "Scripts"** que encaminhava para uma página 404.
- **Activity Logs:** corrigida uma apresentação incorreta "Página 2 de 1" e
  corrigido o filtro de gravidade WARN que não correspondia a nada.

---

## Sem alterações visíveis para o cliente nesta janela

Auth Service, Barcode Service, FTP Service, Operator Service e Docnet Service
(`1.54.6`, sem alterações) receberam apenas manutenção interna ou de
configuração de implementação.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact
     git ranges between the ALT and NEU version-bump commits supplied by the
     user, per service). Window ~2026-07-01 → 2026-07-04. -->
