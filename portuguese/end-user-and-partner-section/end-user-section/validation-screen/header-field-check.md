---
description: >-
  De onde vem o valor de um campo de cabeçalho e como ele é criado — a
  explicação por trás da Verificação de campos de cabeçalho na tela de
  validação.
---

# Verificação de campos de cabeçalho: de onde vêm os dados

O botão **Verificação de campos de cabeçalho** fica ao lado de **Salvar** na tela de validação. Ele abre o relatório *De onde vem cada valor?*: para cada campo de cabeçalho, mostra o que estava no documento, o que alterou o valor pelo caminho, o que o DocBits mostra agora e por quê.

Esta página explica como um valor é criado e o que cada fonte significa. Não é necessário conhecimento técnico.

{% hint style="info" %}
A Verificação de campos de cabeçalho faz parte do módulo **Analytics**. Se o botão estiver acinzentado, um administrador pode concedê-lo ao seu perfil em **Configurações › Funções**.
{% endhint %}

## Um valor é sempre criado nesta ordem

| Etapa | O que acontece |
| --- | --- |
| **1. Ler** | O valor é lido do documento — por uma regra treinada, pela IA ou diretamente de uma fatura eletrônica. |
| **2. Transformar** | Os scripts e as regras de transformação do cliente alteram o valor lido: encurtar, complementar, ajustar o formato. |
| **3. Pesquisar** | O valor é procurado nos dados mestres. Se algo for encontrado, o registro de dados mestres substitui o valor lido. |
| **4. Exibir** | O usuário vê apenas o resultado. O que aconteceu pelo caminho é mostrado pela Verificação de campos de cabeçalho. |

As etapas 2 e 3 nem sempre são executadas — mas, quando são, alteram o valor. É exatamente daí que vem a maioria dos casos relatados.

## As fontes — o que cada uma significa

Os ícones são os mesmos que o relatório mostra na coluna **Ação** e na barra de filtros no topo.

### Regra treinada

O DocBits lembra onde um campo fica neste tipo de documento, porque alguém o marcou ali uma vez.

* **Exemplo:** fornecedor “Bornemann” — sempre no mesmo lugar, no canto superior esquerdo.
* **Se estiver errado:** marque o local correto no documento e salve — a regra aprende com isso.

### IA

Sem padrão fixo. A IA lê o documento como uma pessoa e decide por conta própria qual texto pertence a qual campo.

* **Exemplo:** data da fatura, valores, condições de pagamento.
* **Se estiver errado:** corrija. Ela pode ser ativada e desativada em **Configurações › Campos de cabeçalho OCR**.

### Fatura eletrônica

Com XRechnung ou ZUGFeRD nada é reconhecido: o valor já é um campo de dados no documento e é assumido diretamente.

* **Exemplo:** número da fatura a partir do campo XML do remetente.
* **Se estiver errado:** o erro está no remetente. O DocBits mostra exatamente de qual campo XML o valor veio.

### Script / regra de transformação

Após a leitura, a lógica do cliente entra em ação e remodela o valor. O documento continua o mesmo — o valor não.

* **Exemplo:** `1001 / LS 206776` se torna `1001`.
* **Se estiver errado:** não procure no documento. Verifique **Configurações › Scripts** ou **Regras de Transformação**.

### Dados mestres

O valor lido é procurado nos seus próprios dados — pedidos, fornecedores. Uma correspondência substitui o valor e arrasta outros campos junto.

* **Exemplo:** `1001` encontra o pedido `06O051001` — e o fornecedor e o comprador passam a vir de lá também.
* **Se estiver errado:** verifique **Configurações › Configuração de Lookup**. Ali consta se a busca é exata ou se aceita também correspondências parciais.

### Calculado

Não lido, mas calculado a partir de outros campos.

* **Exemplo:** data de vencimento a partir da data da fatura mais as condições de pagamento.
* **Se estiver errado:** geralmente um dos campos a partir dos quais é calculado está errado.

### Código de barras

Lido de um código de barras ou código QR no documento.

* **Exemplo:** o número da fatura está codificado no código QR.
* **Se estiver errado:** verifique as configurações de código de barras do tipo de documento.

## O que mais se entende mal

{% hint style="warning" %}
Quando um campo de repente contém um valor que não aparece assim no documento, quase nunca foi a IA — foi a etapa 2 ou a etapa 3. Na maioria das vezes, a correspondência nos dados mestres, que também aceita correspondências parciais: `1001` corresponde a `06O051001`, e com o pedido encontrado o fornecedor também muda.
{% endhint %}

No relatório, esse campo é marcado em vermelho. A coluna **Ação** mostra o registro de dados mestres junto com um chip vermelho *apenas correspondência parcial*, e a parte correspondente do valor aparece destacada.

## Como ler o relatório

* **Chips de status** no topo contam os campos que vieram inalterados do documento, os que mudaram pelo caminho e os que não estão no documento como exibidos. Clique em um chip para mostrar apenas esses campos; clique novamente para mostrar todos.
* **Filtro de fonte:** a fileira de ícones mostra cada método de extração. Clique em um para mostrar apenas os campos que passaram por ele.
* **Ação:** cada etapa pela qual o valor passou, com o ícone da sua fonte. A etapa da qual vem o valor atual aparece destacada. Passe o mouse para ver o que cada etapa fez, de qual valor para qual.
* **Motivo:** o status do campo. O ícone (i) explica por que o valor é o que é. Se constar *O campo não existia*, o campo não estava presente no documento.
* Valores longos são encurtados com … — passe o mouse para ver o valor completo.
