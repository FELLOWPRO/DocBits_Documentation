# Quando

<figure><img src="../../../.gitbook/assets/docbits_workflow_4.png" alt="DocBits Fluxo de trabalho 4"><figcaption></figcaption></figure>

#### Compreendendo o "Quando" nas Configurações de Fluxo de Trabalho

**Propósito do "Quando"**

* A seção "Quando" em uma configuração de fluxo de trabalho define as condições de acionamento que iniciam uma ação de fluxo de trabalho específica. Essas condições são baseadas em critérios especificados relacionados aos atributos do documento ou atividades do usuário dentro do sistema ERP.

**Como Funciona**

* Na sua interface, o "Quando" parece ser um ponto de partida onde os usuários podem selecionar diferentes cartões de acionamento. Cada cartão especifica condições sob as quais ações subsequentes (definidas em outra seção da configuração do fluxo de trabalho, provavelmente rotulada como "Ação") serão executadas.

**Cartões de Condição de Tipo de Documento**

* Os cartões exibidos na captura de tela são variações das condições de "Tipo de Documento", que são usadas para acionar fluxos de trabalho com base no tipo de documento em processamento. Aqui está uma análise de cada tipo de cartão de condição mostrado:
* **Tipo de documento (Operador) um de (Tipo)**: Este cartão aciona uma ação quando o tipo de um documento corresponde a um dos tipos especificados em uma lista. O operador pode incluir opções como "é" ou "não é", permitindo condições inclusivas ou exclusivas.
* **Tipo de documento (Operador) (Tipo)**: Esta variante mais simples é acionada com base em uma única condição de tipo de documento. Normalmente, verifica se o tipo de documento "é" ou "não é" um tipo específico, sem a opção de selecionar entre vários tipos.

#### Configurando um Cartão de Acionamento "Quando"

1. **Seleção do Tipo de Condição**: Os usuários começam selecionando um tipo de condição relevante para o fluxo de trabalho que desejam automatizar. Neste caso, os tipos de documento são o foco.
2. **Definindo o Operador**: Os usuários devem decidir o operador lógico, como "é" ou "não é", que estabelece a base para comparar os tipos de documento reais em relação às condições definidas.
3. **Especificar Tipos de Documento**: Dependendo do cartão, os usuários podem selecionar um ou vários tipos de documento que acionarão o fluxo de trabalho quando documentos desses tipos forem processados.
4. **Finalizando o Acionamento**: Uma vez que a condição é configurada, ela se torna a base para acionar ações específicas definidas no fluxo de trabalho. Se um documento atender à condição definida, as ações definidas serão iniciadas automaticamente.

#### Aplicação Prática

Na prática, esses cartões de acionamento são cruciais para automatizar processos como aprovações, notificações ou qualquer procedimento que dependa do tipo de documento em questão. Por exemplo, se um tipo de documento "é" uma "Fatura" e corresponder às condições definidas no cartão "Quando", o fluxo de trabalho pode encaminhar automaticamente o documento para processamento de pagamento.

Essa configuração garante que os fluxos de trabalho sejam não apenas eficientes, mas também adaptados às necessidades operacionais específicas da organização, reduzindo a supervisão manual e acelerando os processos de manipulação de documentos.

Em resumo, a parte "Quando" da configuração do seu fluxo de trabalho trata de preparar o terreno para ações automatizadas com base em condições específicas e predefinidas. É uma ferramenta poderosa para garantir que seu sistema ERP reaja dinamicamente às necessidades do negócio, aprimorando tanto a produtividade quanto a precisão na gestão de documentos.
