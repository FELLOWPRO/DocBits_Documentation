# Teste de Automação de Faturas com DocBits

## Visão Geral

Este documento descreve o plano de testes para automação de faturas usando DocBits com Infor LN ou M3. Inclui detalhes sobre casos de teste, preparação para testes, etapas de execução e processos de suporte.

## Casos de Teste

| ID | Caso de Teste                                                                       | Descrição                                                                                                                                                                                                    | Status        |
| -- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- |
| 1  | Faturas de Custo                                                                    | Faturas sem ordem de compra são processadas com sucesso no DocBits e exportadas para LN como “fatura de custo”.                                                                                              | A SER TESTADO |
| 2  | Fatura Relacionada a Ordem de Compra com Correspondência Perfeita                   | Faturas relacionadas a ordens de compra são processadas com sucesso no DocBits com uma correspondência perfeita da fatura para a OC, uma vez que o número do item, quantidade e preço unitário correspondem. | A SER TESTADO |
| 3  | Faturas Relacionadas a Ordens de Compra com Quantidade Diferente                    | Faturas relacionadas a ordens de compra são processadas no DocBits, mas no módulo de correspondência de OC, temos uma discrepância na quantidade.                                                            | A SER TESTADO |
| 4  | Faturas Relacionadas a Ordens de Compra com Preço Unitário Diferente                | Faturas relacionadas a ordens de compra são processadas no DocBits, mas no módulo de correspondência de OC, temos uma discrepância no preço unitário.                                                        | A SER TESTADO |
| 5  | Faturas Relacionadas a Ordens de Compra com Número de Item Diferente ou Inexistente | Faturas relacionadas a ordens de compra são processadas no DocBits, mas no módulo de correspondência de OC, temos uma discrepância ou um número de item inexistente.                                         | A SER TESTADO |
| 6  | Faturas Relacionadas a Ordens de Compra com Discrepância Dentro da Tolerância       | Faturas relacionadas a ordens de compra são processadas no DocBits, mas no módulo de correspondência de OC, temos uma discrepância na quantidade ou preço unitário, mas está dentro da tolerância.           | A SER TESTADO |
| 7  | Notas de Crédito                                                                    | Notas de crédito são processadas com sucesso no DocBits e exportadas para LN. Esclarecer se os valores devem ser exportados com sinal positivo ou negativo.                                                  | A SER TESTADO |

## Plano de Testes com o Cliente

### 1. Configuração

* **Reunião Inicial**: Agendar uma reunião de kickoff com o cliente para explicar o processo de teste e os objetivos.
* **Acesso e Permissões**: Garantir que o cliente tenha todo o acesso necessário ao DocBits e Infor LN ou M3 para fins de teste.

### 2. Preparação para Testes

* **Treinamento**: Fornecer treinamento abrangente para a equipe do cliente sobre como usar o DocBits para processamento de faturas.
* **Documentação**: Compartilhar documentação detalhada sobre os procedimentos de teste, incluindo resultados esperados para cada caso de teste.

### 3. Execução dos Casos de Teste

* **Ambiente de Teste**: Configurar um ambiente de teste que replique o sistema de produção do cliente o mais próximo possível.
* **Teste Passo a Passo**: Trabalhar com o cliente para executar cada caso de teste, garantindo que eles entendam cada etapa:
  * Processar faturas através do DocBits.
  * Verificar a saída no módulo de correspondência de OC.
  * Verificar os resultados da exportação no LN ou M3.

### 4. Resolução de Problemas

* **Rastreamento**: Usar um sistema de rastreamento (como Jira ou uma planilha simples) para registrar quaisquer problemas ou discrepâncias que ocorram durante os testes.
* **Suporte**: Fornecer suporte imediato para resolver problemas e esclarecer quaisquer dúvidas.

### 5. Verificação e Feedback

* **Verificação**: Após cada caso de teste, verificar os resultados com o cliente para garantir a precisão.
* **Ciclo de Feedback**: Coletar feedback do cliente sobre o processo e quaisquer melhorias necessárias.

### 6. Finalização

* **Documentação dos Resultados**: Documentar os resultados de cada caso de teste e fornecer um relatório resumido ao cliente.
* **Reunião de Revisão**: Realizar uma reunião de revisão para discutir os resultados dos testes e quaisquer etapas adicionais necessárias antes de entrar em operação.

### 7. Preparação para Go Live

* **Reforço de Treinamento**: Oferecer uma sessão de treinamento de reforço, se necessário.
* **Plano de Suporte**: Desenvolver um plano de suporte para a fase inicial de go-live para garantir uma transição suave.
