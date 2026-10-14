# Estratégia de ciclo de vida de releases do DocBits

O DocBits utiliza dois canais de release, **VESTA** e **NOVA**, para introduzir novas releases e dar à sua organização tempo para avaliá-las antes da adoção. Durante a produção paralela, você decide se e quando mudar para a nova release. Em seguida, a FELLOWPRO gerencia a transição (rollover) que a torna a release de produção comum para todos os clientes.

Os números de versão neste guia — R1.0.x, R1.1.x e R1.2 — são ilustrativos. O mesmo ciclo de vida se repete com as releases seguintes; `x` representa atualizações dentro de uma série de releases.

## Canais de release

| Canal     | Função no ciclo de vida                                                                                                                                                                                              |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **VESTA** | Disponibiliza a release de produção atual.                                                                                                                                                                           |
| **NOVA**  | Disponibiliza a próxima release à medida que ela avança pelas etapas de desenvolvimento, testes e disponibilidade em produção. Durante a produção paralela, NOVA e VESTA oferecem ambos releases de produção ativas. |

## Visão geral do ciclo de vida

![Ciclo de vida de releases do DocBits em três fases com VESTA e NOVA](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits-release-lifecycle-strategy.png)

Cada ciclo é composto por três fases. Em seguida, um rollover gerenciado pela FELLOWPRO leva a release de produção do NOVA para o VESTA e inicia o próximo ciclo.

| Fase                            | VESTA              | NOVA                    | O que isso significa para sua organização                                                      |
| ------------------------------- | ------------------ | ----------------------- | ---------------------------------------------------------------------------------------------- |
| **1. Desenvolvimento**          | R1.0.x em produção | R1.1 em desenvolvimento | Continue utilizando o VESTA enquanto a próxima release é preparada.                            |
| **2. QA e testes de aceitação** | R1.0.x em produção | R1.1 em QA e UAT        | Avalie a próxima release no sandbox do NOVA enquanto o trabalho de produção continua no VESTA. |
| **3. Produção paralela**        | R1.0.x em produção | R1.1.x em produção      | Permaneça no VESTA ou mude de forma independente para o NOVA quando estiver pronto.            |

Após o rollover, todos os clientes utilizam o VESTA R1.1.x, e o NOVA é reaproveitado para o desenvolvimento da R1.2. A Fase 1 começa novamente com essas versões atualizadas.

### Fase 1 — Desenvolvimento

O VESTA disponibiliza a release de produção atual, R1.0.x, enquanto a próxima release, R1.1, é desenvolvida no NOVA. Sua organização continua seu trabalho diário no VESTA durante toda esta fase.

### Fase 2 — QA e testes de aceitação

A próxima release do NOVA passa por garantia de qualidade (QA) e testes de aceitação do usuário (UAT). Você pode avaliá-la no sandbox do NOVA para verificar como as alterações se adequam aos fluxos de trabalho da sua organização e preparar a adoção.

O VESTA R1.0.x continua sendo a release de produção durante esta fase. Você pode mudar para o NOVA para uso em produção assim que ele estiver disponível na Fase 3.

### Fase 3 — Produção paralela

O VESTA R1.0.x e o NOVA R1.1.x são ambos releases de produção ativas. Sua organização decide se e quando mudar para o NOVA, com base em suas necessidades e nos resultados da avaliação no sandbox.

Para adotar o NOVA durante esta fase:

1. Avalie a release no sandbox do NOVA.
2. Decida quando sua organização estará pronta para utilizá-la em produção.
3. Mude do VESTA para o NOVA utilizando a configuração **Release Channel** no aplicativo DocBits.

Essa mudança é feita em regime de autoatendimento. A FELLOWPRO não seleciona quais clientes devem migrar para o NOVA. Você pode continuar utilizando o VESTA durante toda a produção paralela e adotar a nova release por meio do rollover subsequente.

## Rollover da release e o próximo ciclo

A FELLOWPRO gerencia o rollover assim que a release do NOVA estiver pronta para se tornar a release de produção comum e a aceitação da transição planejada tiver sido obtida de todos os clientes:

**NOVA R1.1.x → VESTA R1.1.x**

### Comunicação prévia e aceitação dos clientes

A FELLOWPRO comunica antecipadamente o rollover planejado a todos os clientes por e-mail e solicita a aceitação da transição. Você está convidado a entrar em contato com a FELLOWPRO para apresentar quaisquer preocupações ou objeções, para que possam ser discutidas antes do rollover. O rollover e o reaproveitamento do NOVA só ocorrem quando a release estiver pronta e todos os clientes tiverem aceitado a transição planejada.

### O que muda no rollover

| Mudança                                           | Resultado                                                                                               |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **A release do NOVA torna-se a release do VESTA** | A R1.1.x torna-se a release de produção comum no VESTA para todos os clientes.                          |
| **A release anterior é descontinuada**            | A R1.0.x é desativada e deixa de estar disponível em qualquer um dos canais ou por qualquer outro meio. |
| **O NOVA é reaproveitado para a próxima release** | O desenvolvimento da R1.2 começa no NOVA, iniciando a Fase 1 do próximo ciclo.                          |

As mesmas três fases se repetem então com os novos números de versão.

O diagrama abaixo ilustra com mais detalhes o ciclo de releases descrito acima.

![Ciclo de releases detalhado do DocBits com VESTA e NOVA](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/docbits-release-lifecycle-strategy-details.png)

### Cadência de releases

Atualmente, a FELLOWPRO planeja um ciclo de releases de aproximadamente **3–4 meses**. Esse intervalo reflete nossa estimativa de planejamento atual; não se trata de um cronograma fixo, de uma duração máxima do ciclo nem de uma garantia de data de release ou de rollover.

O momento de cada rollover e do reaproveitamento do NOVA depende tanto da **prontidão da release quanto da aceitação da transição planejada por todos os clientes**. Se for necessário tempo adicional para alcançar a prontidão da release, tratar preocupações dos clientes ou obter a aceitação de cada cliente, o ciclo será prorrogado e poderá ultrapassar quatro meses.

A FELLOWPRO comunica cada rollover planejado com antecedência. Qualquer prazo indicativo permanece sujeito ao cumprimento dessas condições.

## Responsabilidades e escolha do cliente

| Transição                                         | Quem a gerencia | O que esperar                                                                                                                                                                                                                           |
| ------------------------------------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mudança do VESTA para o NOVA durante a Fase 3** | Sua organização | Avalie o NOVA no sandbox e escolha se e quando mudar utilizando a configuração Release Channel do aplicativo.                                                                                                                           |
| **Rollover do NOVA R1.1.x para o VESTA R1.1.x**   | FELLOWPRO       | Analise o comunicado prévio enviado por e-mail, apresente quaisquer preocupações ou objeções e confirme a aceitação da transição planejada. A FELLOWPRO prossegue quando a release estiver pronta e todos os clientes tiverem aceitado. |

## Perguntas frequentes

### Podemos permanecer no VESTA enquanto o NOVA está disponível em produção?

Sim. Durante a Fase 3, você pode permanecer no VESTA ou mudar para o NOVA quando sua organização estiver pronta. No rollover subsequente, a nova release torna-se o VESTA e a release anterior é descontinuada.

### Como mudamos para o NOVA?

Assim que o NOVA estiver disponível em produção, utilize a configuração **Release Channel** no aplicativo DocBits. Sua organização faz essa escolha de forma independente, com base em suas necessidades e na avaliação da release no sandbox do NOVA.

### Quando o NOVA fica disponível para uso em produção?

O NOVA torna-se uma release de produção ativa na Fase 3, após o desenvolvimento e o QA/UAT. Durante esta fase, VESTA e NOVA funcionam em produção em paralelo, com versões de software diferentes.

### Como seremos informados sobre o rollover e podemos apresentar objeções?

A FELLOWPRO envia um e-mail antecipadamente a todos os clientes e solicita a aceitação da transição planejada. Você está convidado a apresentar quaisquer preocupações ou objeções à FELLOWPRO. O rollover e o reaproveitamento do NOVA só ocorrem quando a release estiver pronta e a aceitação tiver sido obtida de todos os clientes.

### Podemos continuar utilizando a R1.0.x após o rollover?

Não. A R1.0.x é desativada no rollover e deixa de estar disponível em qualquer um dos canais ou por qualquer outro meio. A R1.1.x torna-se a release de produção comum do VESTA para todos os clientes.

### Qual é a diferença entre o rollover e a nossa mudança para o NOVA?

A sua mudança para o NOVA durante a Fase 3 é uma escolha em regime de autoatendimento sobre quando adotar a nova release de produção. O rollover é a transição subsequente gerenciada pela FELLOWPRO: o NOVA R1.1.x torna-se o VESTA R1.1.x, a release anterior é descontinuada e o próximo ciclo começa.

### O que acontece com o NOVA após o rollover?

O NOVA é reaproveitado para o desenvolvimento da próxima release, a R1.2 neste exemplo. O VESTA disponibiliza a R1.1.x enquanto o NOVA passa novamente pelas etapas de desenvolvimento, QA/UAT e produção paralela.

### Há garantia de uma nova release a cada três a quatro meses?

Não. A cadência aproximada de 3–4 meses é uma estimativa de planejamento atual, não um cronograma garantido nem uma duração máxima. O rollover e o reaproveitamento do NOVA exigem tanto a prontidão da release quanto a aceitação de todos os clientes. Se qualquer uma dessas condições exigir mais tempo, o ciclo será prorrogado e poderá ultrapassar quatro meses. A FELLOWPRO comunica cada rollover planejado com antecedência.
