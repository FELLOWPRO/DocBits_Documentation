# Faturação eletrónica B2B em França: plataformas autorizadas e Peppol

## Utilizar uma plataforma autorizada (PA)

As operações B2B nacionais entre empresas estabelecidas em França e sujeitas a IVA, quando abrangidas pela reforma francesa da faturação eletrónica, devem ser transmitidas e recebidas através de uma **plateforme agréée (PA)**, anteriormente designada **PDP**. A obrigação aplica-se às operações e empresas sujeitas ao regime francês; não abrange automaticamente todas as faturas ou transações internacionais. O **Portail public de facturation (PPF)** não é uma plataforma alternativa para trocar estas faturas. Consulte as [orientações atuais da DGFiP sobre plataformas autorizadas](https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees).

## Calendário de aplicação

* **1 de setembro de 2026:** as empresas abrangidas devem poder receber faturas eletrónicas. As grandes empresas e as empresas de dimensão intermédia (GE/ETI) devem também cumprir as obrigações aplicáveis de emissão eletrónica e de comunicação de dados (*e-reporting*).
* **1 de setembro de 2027:** as obrigações aplicáveis de emissão eletrónica e de *e-reporting* estendem-se às pequenas e médias empresas e às microempresas (PME/micro).

Verifique o âmbito e a categoria da sua empresa no [calendário oficial da DGFiP](https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation).

## Peppol e a integração técnica

A utilização da rede **Peppol**, por si só, não substitui o recurso a uma PA para as operações abrangidas. A rede pode ser utilizada no transporte e na interoperabilidade entre plataformas. Confirme com a sua PA os formatos, os canais de troca e as interfaces que suporta; não presuma que uma ligação Peppol ou uma ligação direta ao PPF satisfaz, por si só, as obrigações de emissão e receção.

Para integrar o DocBits ou outro sistema de gestão, escolha a PA e confirme as respetivas especificações de API, autenticação, encaminhamento de faturas e comunicação de dados. Os requisitos concretos dependem do serviço e da integração contratados. A existência de uma conta técnica, de um hub ou de uma aplicação no PISTE não constitui, por si só, prova de conformidade com o regime atual.

## Referências e diagramas históricos

As referências e imagens seguintes documentam propostas e integrações anteriores da reforma. **Não constituem instruções atuais para trocar faturas através do PPF.** Em particular, os antigos desenhos de API, integração de software e ligação de hubs não demonstram que o PPF continua a ser uma alternativa à PA. Utilize as orientações atuais da DGFiP acima e as especificações atuais da sua PA antes de configurar uma integração.

Referências históricas: [requisitos da reforma](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform), [especificações do portal em 2022](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html), [interconexão entre plataformas](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html), [troca de faturas](https://nymus.be/fr/facturation-electronique-en-france/), [Peppol e a reforma](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france) e [interoperabilidade](https://nymus.be/fr/facturation-electronique-en-france/).

<figure><img src="../../.gitbook/assets/Picture 1.png" alt="Diagrama do ciclo de vida de uma fatura do fornecedor até aos estados Submitted, Received by the platform e Made available, com os resultados Rejected, Refused, Disputed, Partially approved, In hand e Completed"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/Picture 6.png" alt="Diagrama de um Issuer OD-PDP e um Receiver OD-PDP ligados através de portais de serviços e software de terceiros, com um passo de controlo e recuperação de dados entre eles"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/Picture 2.png" alt="Diagrama das três camadas de controlo numeradas, controlos técnicos, controlos de aplicação e controlos funcionais e de negócio, cada uma a alimentar um passo seguinte do processo"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/Picture 5.png" alt="Diagrama do modelo de hub com um parceiro, uma conta técnica, o hub, uma aplicação ao abrigo do PISTE e uma ligação"><figcaption></figcaption></figure>

<div><figure><img src="../../.gitbook/assets/Picture 3.png" alt="Diagrama da receção de um fluxo EDI e do fluxo 2 via API que passam controlos funcionais de formato semântico, diretório e consistência de dados antes da incorporação dos dados de faturação e de um resultado de fatura submetida"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Picture 4.png" alt="Diagrama de um fluxo EDI e um fluxo API que passam controlos funcionais e regras de negócio específicas antes da rejeição ou recusa da fatura ou de uma fatura recebida e disponibilizada"><figcaption></figcaption></figure></div>
