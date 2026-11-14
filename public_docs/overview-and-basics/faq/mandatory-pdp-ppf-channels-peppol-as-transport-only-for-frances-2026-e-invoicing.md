# Faturação eletrónica B2B em França: plataformas autorizadas e Peppol

## Regras e calendário atuais

Nas trocas de faturas B2B nacionais em França abrangidas pela reforma, entre empresas sujeitas a IVA, a fatura tem de ser transmitida através de uma **plataforma autorizada (plateforme agréée, PA; anteriormente PDP)**. O **portal público de faturação (Portail public de facturation, PPF)** assegura o diretório público e a recolha dos dados fiscais; não é uma plataforma alternativa de troca de faturas para estas operações.

* **1 de setembro de 2026:** todas as empresas abrangidas têm de estar aptas a receber faturas eletrónicas. As grandes empresas (GE) e as empresas de dimensão intermédia (ETI) têm também de emitir faturas eletrónicas e de cumprir as obrigações de comunicação de dados (*e-reporting*) a partir dessa data.
* **1 de setembro de 2027:** as obrigações de emissão e de comunicação de dados passam a aplicar-se às pequenas e médias empresas (PME) e às microempresas.

A obrigação aplicável depende do âmbito da operação e da categoria da empresa. Consulte as [orientações oficiais sobre plataformas autorizadas](https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees), o [calendário de aplicação](https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation) e a [resposta do Senado](https://www.senat.fr/questions/base/2026/qSEQ260107185.html).

## Peppol e interoperabilidade

A Peppol pode assegurar o transporte e a interoperabilidade entre sistemas e plataformas ligados. Recorrer à Peppol não substitui a exigência de utilizar uma PA nas trocas de faturas abrangidas pelo mandato francês. Não considere uma ligação Peppol, por si só, como prova de que as obrigações francesas de troca e de comunicação de dados estão cumpridas.

Para o catálogo de formatos do DocBits, consulte a [visão geral dos padrões de faturação eletrónica](../../administration-and-setup/settings/global-settings/document-types/edi/currently-supported-e-invoice-standards/README.md).

## Contexto técnico histórico

Os seis diagramas e as descrições de API abaixo foram mantidos do material anterior sobre PPF/PDP como contexto técnico histórico. Utilizam a terminologia e a arquitetura anteriores e não descrevem uma opção atual para trocar faturas B2B obrigatórias através do PPF. Verifique as especificações atuais da PA e dos serviços públicos antes de implementar uma integração.

<figure><img src="../../.gitbook/assets/Picture 1.png" alt="Diagrama histórico do ciclo de vida da faturação eletrónica francesa, com as fases de preparação, receção, validação e pagamento e os estados do fornecedor e do comprador"><figcaption><p>Diagrama histórico do ciclo de vida: preparação e emissão, receção, validação/devolução e pagamento, com as designações de estado do fornecedor e do comprador visíveis em cada fase.</p></figcaption></figure>

### Modelo histórico de serviços de API

O modelo de API anterior descrevia o acesso às funções disponíveis a partir das ferramentas informáticas implementadas pelas organizações parceiras, através de dois métodos de integração:

* **Sistemas de informação (SI):** as APIs eram descritas como integradas nos sistemas dos emitentes, dos destinatários ou dos respetivos operadores de desmaterialização (OD). Algumas APIs destinavam-se a sistemas PDP e ofereciam uma alternativa à integração EDI.
* **Software de terceiros:** os editores de software podiam acrescentar uma camada de comunicação aos sistemas dos clientes. As referências anteriores a uma ligação ao PPF pertencem a esse modelo histórico e não constituem uma via atual de troca de faturas.

<figure><img src="../../.gitbook/assets/Picture 6.png" alt="Diagrama do emitente e do destinatário a trocar faturas através de portais de serviço OD-PDP e do PPF, com controlo e recuperação de dados"><figcaption><p>Diagrama histórico de interligação: o emitente e o destinatário ligam-se através de software de terceiros, de portais de serviço e de blocos OD/PDP em torno do bloco de controlo e recuperação de dados do PPF.</p></figcaption></figure>

### Diagrama histórico de interligação

Este diagrama ilustra o contexto anterior de interligação de plataformas. A implementação atual tem de seguir os requisitos da PA; não se afirma aqui um requisito geral de que todas as trocas utilizem uma única rede de transporte.

<figure><img src="../../.gitbook/assets/Picture 2.png" alt="Diagrama dos controlos de fluxo, de fatura e de dados de faturação: as submissões do fornecedor passam por controlos técnicos, aplicacionais e funcionais, com rejeições"><figcaption><p>Diagrama histórico de controlos: os controlos técnicos, aplicacionais e funcionais/de negócio são apresentados para submissões manuais, por API e por EDI, a par dos resultados de fluxo inadmissível, fatura rejeitada e fatura recusada.</p></figcaption></figure>

### Ligação histórica ao hub

O modelo de hub anterior descrevia uma solução web ou aplicacional em que **o hub efetuava chamadas de API em nome dos seus clientes**. Referia uma conta técnica por cada parceiro, uma aplicação sob PISTE e uma ligação ao PPF para o hub. São detalhes de arquitetura históricos, não um procedimento de integração atual verificado.

<figure><img src="../../.gitbook/assets/Picture 5.png" alt="Diagrama de parceiros com contas técnicas ligados através de um único hub a uma aplicação sob PISTE e a uma única ligação"><figcaption><p>Diagrama histórico do hub: parceiros com contas técnicas ligam-se através de um único hub a uma aplicação sob PISTE e a uma única ligação.</p></figcaption></figure>

### Referências históricas

O material anterior citava [o antigo calendário e enquadramento legal](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform), [as especificações de 2022](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html), [uma visão geral da reforma de 2025](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html), [contexto sobre a interligação de plataformas](https://nymus.be/fr/facturation-electronique-en-france/), [contexto sobre a Peppol](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france) e [contexto sobre a troca de faturas](https://nymus.be/fr/facturation-electronique-en-france/). Estas ligações e os restantes diagramas são mantidos como contexto histórico. Utilize as fontes oficiais indicadas acima para as obrigações atuais, incluindo a distinção entre a troca de faturas através de uma PA e as funções públicas do PPF. A referência anterior ao artigo 91.º da Lei das Finanças de 2024 não estabelece uma opção atual de troca de faturas através do PPF.

<figure><img src="../../.gitbook/assets/Picture 3.png" alt="Fluxograma histórico do processo de emissão, desde a receção do fluxo EDI e das chamadas de API, passando pelos controlos de fluxo, aplicacionais e funcionais, até à fatura emitida"><figcaption><p>Fluxograma histórico de emissão: os fluxos EDI e as chamadas de API recebidos passam pelos controlos de fluxo, aplicacionais e funcionais antes da incorporação dos dados de faturação; são também apresentados os caminhos de rejeição, os fluxos de saída 1 e 2 e as notificações do ciclo de vida.</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/Picture 4.png" alt="Fluxograma histórico do processo de receção, desde a receção do fluxo EDI e das chamadas de API, passando pelos controlos com rejeição ou recusa, até à fatura disponibilizada"><figcaption><p>Fluxograma histórico de receção: os controlos técnicos, aplicacionais e funcionais incluem regras de negócio específicas, com caminhos de rejeição ou recusa; os dados aceites conduzem a uma fatura recebida e disponibilizada, a par do fluxo 2 do destinatário e das notificações do ciclo de vida.</p></figcaption></figure>
