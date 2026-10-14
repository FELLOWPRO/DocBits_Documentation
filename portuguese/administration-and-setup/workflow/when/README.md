

Os cartões desta categoria no seletor **Add Card** do Workflow Builder:

<figure><img src="../../../.gitbook/assets/workflow_cards_when.png" alt="Workflow Builder card category"><figcaption><p>Os cartões desta categoria.</p></figcaption></figure>
---
description: Configuração do gatilho Quando nos fluxos de trabalho DocBits
---

# Quando

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FKwAT37pCkZRziNLyWMsL%252Fimage.png%3Falt%3Dmedia%26token%3Db95d040f-e9e6-496d-97cd-d2c8f1c30d60\&width=768\&dpr=4\&quality=100\&sign=c323483b\&sv=2)

#### Compreendendo o "Quando" nas Configurações de Fluxo de Trabalho

**Propósito do "Quando"**

* A seção "Quando" em uma configuração de fluxo de trabalho define as condições de acionamento que iniciam uma ação de fluxo de trabalho específica. Essas condições são baseadas em critérios especificados relacionados aos atributos do documento ou atividades do usuário dentro do sistema ERP.

**Como Funciona**

* Em sua interface, "Quando" parece ser um ponto de partida onde os usuários podem selecionar diferentes cartões de acionamento. Cada cartão especifica condições sob as quais ações subsequentes (definidas na seção "E") serão executadas.

**Cartões de Condição de Tipo de Documento**

* Os cartões com o ícone de documento exibidos na captura de tela são variações das condições de "Tipo de Documento", que são usadas para acionar fluxos de trabalho com base no tipo de documento em processamento. Aqui está uma explicação de cada tipo de cartão de condição mostrado:
  * **Tipo de documento (Operador) um de (Tipo)**: Este cartão aciona uma ação quando o tipo de um documento corresponde a um dos tipos especificados em uma lista. O operador pode incluir opções como "é" ou "não é", permitindo condições inclusivas ou exclusivas.
  * **Tipo de documento (Operador) (Tipo)**: Esta variante mais simples é acionada com base em uma única condição de tipo de documento. Normalmente, verificará se o tipo de documento "é" ou "não é" um tipo específico, sem a opção de selecionar entre vários tipos.
  *

**Celery Beat**

* O cartão com o ícone de relógio na captura de tela é uma condição de "Celery Beat", que é usada para acionar fluxos de trabalho com base em data e hora.

#### Configurando um Cartão de Acionamento "Quando"

1. **Seleção do Tipo de Condição**: Os usuários começam selecionando um tipo de condição relevante para o fluxo de trabalho que desejam automatizar. Neste caso, os tipos de documento são o foco.
2. **Definindo o Operador**: Os usuários devem decidir o operador lógico, como "é" ou "não é", que estabelece a base para comparar os tipos de documento reais em relação às condições definidas.
3. **Especificar Tipos de Documento**: Dependendo do cartão, os usuários podem selecionar um ou vários tipos de documento que acionarão o fluxo de trabalho quando documentos desses tipos forem processados.
4. **Finalizando o Acionamento**: Uma vez que a condição é configurada, ela se torna a base para acionar ações específicas definidas no fluxo de trabalho. Se um documento atender à condição definida, as ações definidas serão iniciadas automaticamente.

#### Aplicação Prática

Na prática, esses cartões de acionamento são cruciais para automatizar processos como aprovações, notificações ou qualquer procedimento que dependa do tipo de documento em questão. Por exemplo, se um tipo de documento "é" uma "Fatura" e corresponder às condições definidas no cartão "Quando", o fluxo de trabalho poderá encaminhar automaticamente o documento para processamento de pagamento.

Essa configuração garante que os fluxos de trabalho sejam não apenas eficientes, mas também adaptados às necessidades operacionais específicas da organização, reduzindo a supervisão manual e acelerando os processos de manipulação de documentos.

Em resumo, a parte "Quando" da configuração do seu fluxo de trabalho trata de preparar o terreno para ações automatizadas com base em condições específicas e predefinidas. É uma ferramenta poderosa para garantir que seu sistema ERP reaja dinamicamente às necessidades do negócio, aprimorando tanto a produtividade quanto a precisão na gestão de documentos.
