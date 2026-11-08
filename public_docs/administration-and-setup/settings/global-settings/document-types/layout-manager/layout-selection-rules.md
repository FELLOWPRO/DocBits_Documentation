# Regras de Seleção de Layout

## Visão geral

Um **layout** decide quais campos e grupos um utilizador vê — e em que ordem — nos ecrãs de **validação**, **aprovação**, **rejeição** e **revisão** de um documento. Você cria os layouts no [Layout Manager](./).

Classicamente, o DocBits escolhia o layout pela **origem** do documento: o país ou a região obtidos das configurações de idioma do documento, como `DE` ou `US`. Cada origem tinha a sua própria cópia do layout, e nada mais podia influenciar a escolha.

Com as **regras de seleção de layout**, os layouts passam a ser blocos reutilizáveis independentes da origem, e as **regras** decidem qual layout um documento recebe:

> *Quando* o documento cumpre uma condição, *então* recebe este layout. As regras são verificadas de cima para baixo; **a primeira regra que corresponder vence**. Se nenhuma regra corresponder, é usado o **layout padrão**.

A origem continua disponível — como uma condição entre muitas. Uma regra pode igualmente considerar o fornecedor, o valor, o estado do documento, o método de extração ou qualquer campo do cabeçalho.

### Problemas que elas resolvem

| Requisito                                                          | Layouts clássicos baseados na origem        | Com regras de seleção                                                                 |
| ------------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------- |
| As faturas de um fornecedor precisam de campos extra (projeto, número aduaneiro) | impossível sem uma nova origem              | regra _Supplier ID is 20723_ → layout "Invoice with project fields"                   |
| Os documentos de DE, AT e CH devem ter o mesmo aspeto               | três cópias do mesmo layout a manter        | um layout, uma regra por origem (ou um grupo ANY) a apontar para ele                  |
| As faturas eletrónicas precisam de um ecrã mais simples do que os PDF digitalizados | não é possível                              | regra _Extraction Method is ELECTRONIC\_DOCUMENT_ → layout "E-invoice"                |
| As faturas de valor elevado precisam de mais campos no ecrã de aprovação | não é possível                              | regra de Approval _Total Amount greater than 10000_ → layout "High value approval"    |
| O segundo aprovador deve ver um ecrã diferente do primeiro          | tipo de layout separado "second approval"   | regra de Approval _Document Status is Pending second approval_ → layout "Second approval" |

## Ativar os layouts baseados em regras

Os layouts baseados em regras são ativados **por tipo de documento** por um **administrador da organização**.

1. Aceda a **Settings → Document Processing → Document Types**.
2. Clique no ícone de **settings** (engrenagem) no cartão do tipo de documento.
3. Abra **Manage Layouts** e ligue o interruptor.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/lsr-manage-layouts-toggle-en-20261102.png" alt="A secção Manage Layouts nas configurações adicionais de um tipo de documento, com o subtítulo Enable Layout Management, e o interruptor Manage Layouts ligado."><figcaption><p>O interruptor Manage Layouts nas configurações adicionais de um tipo de documento</p></figcaption></figure>
<!-- English source image: lsr-manage-layouts-toggle-en-20261102.png -->

O link **Layouts** no cartão do tipo de documento passa a abrir **Layouts & Selection Rules**.

### O que acontece quando o ativa

O DocBits converte os layouts existentes baseados na origem em regras — uma única vez, para este tipo de documento e para cada ecrã:

* O layout da origem **DEFAULT** passa a ser o **layout padrão** (o fallback).
* Cada layout de uma origem específica passa a ser uma regra **"Layout for XX"** com a condição _Document Origin is XX_, a apontar para esse layout. Estas regras recebem prioridades em passos de 10 (por exemplo 2000, 2010, 2020 …), para poder colocar as suas próprias regras antes, entre ou depois delas.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/lsr-default-layout-row-en-20261102.png" alt="O fim da lista de regras de seleção: as últimas regras de origem Layout for UY e Layout for VN, seguidas da linha FALLBACK Default layout marcada is_default, que é usada quando nenhuma regra acima corresponde."><figcaption><p>As regras de origem criadas na ativação, seguidas do layout padrão (FALLBACK)</p></figcaption></figure>
<!-- English source image: lsr-default-layout-row-en-20261102.png -->

Nada é eliminado nem alterado nos próprios layouts. Logo após a ativação, cada documento recebe portanto exatamente o layout que recebia antes. O comportamento só muda quando adiciona ou altera regras.

**Desativá-lo** devolve o tipo de documento imediatamente à seleção baseada na origem. As regras são mantidas mas não são usadas, e voltam a ter efeito quando ligar novamente o interruptor.

## O ecrã Layouts & Selection Rules

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/lsr-layouts-overview-en-20261102.png" alt="O separador Layouts de Layouts and Selection Rules para o tipo de documento INVOICE: os separadores de ecrã Field Validation, Approval, Reject e Review, o filtro All, My layouts e System, o botão New layout e cartões de layout com Edit, Clone e Delete."><figcaption><p>O separador Layouts: cada layout do tipo de documento como um cartão</p></figcaption></figure>
<!-- English source image: lsr-layouts-overview-en-20261102.png -->

* **Layouts / Selection rules** (no cabeçalho da página) alternam entre a lista de layouts e a lista de regras. Os números mostram quantos existem.
* **Field Validation / Approval / Reject / Review** alternam o **ecrã**. Cada ecrã tem os seus próprios layouts, as suas próprias regras e o seu próprio layout padrão — uma regra de Approval nunca altera o ecrã de validação.
* No separador **Layouts** pode criar, editar, clonar e eliminar layouts. Cada cartão mostra se uma regra usa o layout ("Not targeted by rules" quando nenhuma usa). Filtre com **All / My layouts / System**; os layouts de sistema vêm com o DocBits e podem ser vistos e clonados, mas não alterados.

{% hint style="info" %}
A primeira e a segunda aprovação partilham os layouts e as regras de **Approval**. Para dar à segunda etapa de aprovação um ecrã próprio, adicione uma regra de Approval com a condição _Document Status is Pending second approval_ — veja o [exemplo](layout-selection-rules.md#different-screens-for-first-and-second-approval).
{% endhint %}

## Como um layout é escolhido

Cada vez que um documento é aberto, e novamente depois de ser guardado, o DocBits decide o seu layout para o ecrã atual:

1. As **regras ativas** do ecrã são verificadas por ordem de **prioridade** (o número mais baixo primeiro). **A primeira regra cuja condição é verdadeira vence**, e o seu layout é usado.
2. Se nenhuma regra corresponder, é usado o **layout padrão**.
3. Se também não houver layout padrão, o DocBits recorre à escolha clássica baseada na origem.

As regras cujo layout foi eliminado ou está vazio são ignoradas.

### Um exemplo prático

Regras do ecrã **Field Validation**:

| Prioridade | Regra                 | Condição                                    | Layout                         |
| -------- | --------------------- | ------------------------------------------- | ------------------------------ |
| 5        | Behaelterbau invoices | _Supplier ID is HP0000278_                  | Invoice with project fields    |
| 10       | E-invoices            | _Extraction Method is ELECTRONIC\_DOCUMENT_ | E-invoice                      |
| 2020     | Layout for DE         | _Document Origin is DE_                     | Field Validation Layout (DE)   |
| —        | Default layout        | —                                           | Field Validation Layout (Base) |

Que layout cada documento recebe:

| Documento | Fornecedor  | Extração  | Origem | Layout                         | Porque                                               |
| -------- | --------- | ----------- | ------ | ------------------------------ | ----------------------------------------------------- |
| 1        | HP0000278 | e-invoice   | DE     | Invoice with project fields    | a prioridade 5 corresponde primeiro; as regras seguintes não são verificadas |
| 2        | 10040     | e-invoice   | DE     | E-invoice                      | a prioridade 5 não corresponde, a 10 corresponde      |
| 3        | 10040     | scanned PDF | DE     | Field Validation Layout (DE)   | só a regra de origem corresponde                      |
| 4        | 10040     | scanned PDF | US     | Field Validation Layout (Base) | nenhuma regra corresponde → padrão                    |

**A ordem importa**: coloque as regras específicas (um fornecedor) acima das regras gerais (um país).

### Quando um utilizador altera um campo que as regras consideram

O layout é sempre escolhido a partir dos valores **atuais** do documento. Se um utilizador corrigir, por exemplo, o fornecedor no ecrã de validação, o DocBits escolhe o layout novamente após guardar, e o ecrã pode mudar para outro layout. Nenhum dado é perdido: um campo que não faz parte do novo layout mantém o seu valor; apenas não é apresentado até voltar a aplicar-se um layout que o contenha.

## Gerir as regras de seleção

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/lsr-rules-list-en-20261102.png" alt="O separador Selection rules do ecrã Field Validation: uma tabela com as colunas Priority, Rule e condições, Target layout, Source e Active, a primeira linha marcada FIRST, pegas de arrasto à esquerda e um menu de três pontos em cada linha."><figcaption><p>O separador Selection rules do ecrã Field Validation</p></figcaption></figure>
<!-- English source image: lsr-rules-list-en-20261102.png -->

Cada linha mostra a **prioridade** (a primeira linha está marcada **FIRST**), o **nome e a chave da regra** com as suas **condições**, o **layout de destino**, o selo de **origem** e um interruptor **Active**.

| Tarefa                | Como                                                                                |
| ------------------- | ---------------------------------------------------------------------------------- |
| Criar uma regra       | **New rule**                                                                       |
| Editar uma regra      | Clique na linha                                                                     |
| Alterar a ordem       | Arraste a pega à esquerda de uma linha para cima ou para baixo. A nova ordem é guardada imediatamente. |
| Desligar uma regra    | Interruptor **Active**. As regras inativas são ignoradas.                           |
| Duplicar ou eliminar  | Menu **⋮** da linha                                                                 |
| Encontrar uma regra   | **Search rules…**                                                                   |

O selo de **origem** indica de onde vem uma regra: as regras **System** vêm com o DocBits. Editar uma cria uma cópia para a sua organização, apresentada como **Customized**; o original mantém-se intacto e pode ser reposto. As regras que cria são **Custom**.

### O layout padrão

A última linha, marcada **FALLBACK** e **is\_default**, é o layout padrão: é usado sempre que nenhuma regra acima corresponder e não tem condição. É criado quando ativa a funcionalidade (a partir do layout da origem DEFAULT).

{% hint style="info" %}
Para usar outro layout de fallback, crie uma regra **sem qualquer condição** e dê-lhe o número de prioridade mais alto, para que seja verificada em último lugar. Corresponde a todos os documentos que nenhuma regra anterior correspondeu, antes de se chegar ao padrão.
{% endhint %}

## Criar uma regra

Clique em **New rule** no separador Selection rules do ecrã que pretende alterar.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/lsr-rule-editor-en-20261104.png" alt="O editor de regras de seleção de layout para uma fatura: a frase de resumo no topo, depois Step 1 Scope and priority com Rule name, Rule key, Document Type, Layout Type, Priority e uma caixa Log execution, Step 2 Applies when com a condição Document Origin is AR e os botões Add Condition e Add nested group, Step 3 Target layout com o Field Validation Layout (AR) selecionado, e o painel de pré-visualização em tempo real à direita com Sample document, matched_by, Resolved layout, Priority hit e watched_fields."><figcaption><p>O editor de regras: âmbito e prioridade, as condições, o layout de destino e a pré-visualização em tempo real do que a regra faria.</p></figcaption></figure>
<!-- English source image: lsr-rule-editor-en-20261104.png -->

A frase no topo resume a regra à medida que a constrói — "When doc.doc_origin = AR, an INVOICE document gets the origin-ar layout for Field validation. Checked at priority 0 — the first matching rule wins."

### Step 1 — Scope & priority

| Configuração                        | O que faz                                                                                                          |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Rule Name**                       | Apresentado na lista de regras. Descreva o caso de negócio: "Behaelterbau invoices", "E-invoices", "High value approval". |
| **Rule key**                        | Gerada a partir do nome; mantém-se igual quando renomeia a regra.                                                  |
| **Document Type** / **Layout type** | O tipo de documento e o ecrã a que a regra se destina. Obtidos do local onde clicou em **New rule**.               |
| **Priority**                        | Os números mais baixos são verificados primeiro. Deixe intervalos (5, 10, 20 …) para poder inserir regras depois.   |
| **Log execution**                   | Regista cada avaliação da regra, para poder seguir mais tarde porque é que um documento correspondeu ou não. Deixe desligado até precisar desse rasto. |

### Step 2 — Applies when

A condição que um documento tem de cumprir. Pode usar:

* **document attributes**: Document Origin, Extraction Method, Document Status, Sub Document Type,
* **header fields**: Supplier ID, Total Amount, Currency, Purchase Order e todos os outros campos do tipo de documento,
* um **caminho JSON personalizado** (Advanced).

As colunas de tabela não estão disponíveis: o layout é escolhido uma única vez para o documento inteiro.

Deixe a etapa vazia para corresponder a todos os documentos nesta prioridade. Como funcionam as condições — ALL / ANY, grupos aninhados, todos os operadores, valores vazios, maiúsculas/minúsculas — está explicado em [Rule Conditions (Applies when)](../rule-conditions-applies-when.md).

### Step 3 — Target layout

Clique no layout que o documento deve receber. A lista mostra os seus próprios layouts e os layouts de sistema do ecrã selecionado. Um layout não pode ser eliminado enquanto uma regra ainda apontar para ele.

### Pré-visualização em tempo real · /resolve

O painel à direita mostra o que a regra faz para um documento de exemplo com os valores das suas condições:

| Linha               | Significado                                                                                            |
| ------------------- | ----------------------------------------------------------------------------------------------------- |
| **Sample document** | Os valores usados na pré-visualização, obtidos das suas condições                                      |
| **matched\_by**     | `rule` se uma regra correspondeu, caso contrário o padrão                                              |
| **Resolved layout** | O layout que o documento de exemplo receberia                                                          |
| **Priority hit**    | A prioridade da regra que correspondeu                                                                 |
| **watched\_fields** | Os campos de que depende a escolha do layout. Quando um utilizador altera um deles, o layout é escolhido novamente. |

Clique em **Create Rule** (ou **Save rule** ao editar) para guardar. **Cancel** volta à lista de regras.

## Exemplos

### Campos extra para um fornecedor

Ecrã **Field Validation** · prioridade **5** · _Supplier ID is HP0000278_ · destino _Invoice with project fields_ (um clone do seu layout padrão com os campos adicionais de projeto e centro de custo).

### Um layout para vários países

Ecrã **Field Validation** · prioridade **100** · **ANY of**: _Document Origin is Deutsch_, _Document Origin is Austria_, _Document Origin is Switzerland_ · destino _DACH invoice_. Desative as regras migradas "Layout for AT" e "Layout for CH" se apontarem para cópias mais antigas.

### Um ecrã mais simples para faturas eletrónicas

Ecrã **Field Validation** · prioridade **10** · _Extraction Method is ELECTRONIC\_DOCUMENT_ · destino _E-invoice_ (sem campos relacionados com OCR).

### Um ecrã de aprovação mais rigoroso para montantes elevados

Ecrã **Approval** · prioridade **10** · _Total Amount greater than 10000_ · destino _High value approval_ (a mostrar centro de custo, responsável pelo orçamento e número do contrato).

### Ecrãs diferentes para a primeira e a segunda aprovação

Ecrã **Approval** · prioridade **5** · _Document Status is Pending second approval_ · destino _Second Approval Layout_. Os documentos na primeira etapa de aprovação não correspondem e recebem o layout padrão de Approval.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/lsr-rule-editor-approval-en-20261104.png" alt="Uma regra de seleção de Approval no editor: Rule name Layout for DE, prioridade 2000, as condições Document Status is Pending second approval e Document Origin is Deutsch, o layout de destino Second Approval Layout (DE), e a pré-visualização em tempo real a mostrar o documento de exemplo, matched_by rule, o layout resolvido e priority hit 2000."><figcaption><p>Uma regra de Approval para a segunda etapa de aprovação — a pré-visualização à direita mostra já que esta regra vence com prioridade 2000.</p></figcaption></figure>
<!-- English source image: lsr-rule-editor-approval-en-20261104.png -->

### Um ecrã de rejeição especial para alguns fornecedores

Ecrã **Reject** · prioridade **10** · _Supplier ID is one of_ `10040, 10041` · destino _Reject with reason codes_.

## Boas práticas

* **O específico antes do geral.** Regras de fornecedor acima das regras de país, regras de país acima do padrão.
* **Deixe intervalos de prioridade** (5, 10, 20 …) para que novas regras caibam sem renumerar.
* **Baseie as condições em campos fiáveis.** O fornecedor e a origem são definidos cedo e raramente mudam. Condições em campos que os utilizadores editam com frequência fazem o ecrã trocar de layout enquanto trabalham.
* **Clone, não comece do zero.** Clone o seu layout padrão e ajuste-o, para que todos os layouts mantenham a mesma estrutura básica.
* **Verifique a pré-visualização em tempo real** e abra um documento real de cada tipo depois de alterar regras.
* **Mantenha um padrão útil** para cada ecrã, para que nenhum documento fique sem layout.

## Resolução de problemas

| Sintoma                                          | O que verificar                                                                                                                        |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| Um documento recebe o layout errado              | Uma regra anterior corresponde primeiro. Veja as regras acima dela, ou o **Priority hit** na pré-visualização.                        |
| O padrão é usado embora uma regra devesse corresponder | A regra está **Active**? A condição corresponde ao valor exato (maiúsculas/minúsculas, espaços)? A regra está no separador de **ecrã** correto? |
| O layout muda enquanto um utilizador trabalha       | Um campo em **watched\_fields** foi alterado. Baseie a regra num campo mais estável.                                                  |
| Um layout não pode ser eliminado                 | Uma regra ainda aponta para ele. Redirecione ou elimine essa regra primeiro.                                                          |
| Não é apresentado nenhum layout                  | Nenhuma regra correspondeu, não há padrão e não existe layout baseado na origem para este ecrã. Adicione uma regra sem condição como apanha-tudo. |
| Nada mudou após a ativação                       | É o esperado: a ativação reproduz a escolha anterior baseada na origem. Adicione as suas próprias regras.                             |
| A segunda aprovação mostra o layout da primeira  | Adicione uma regra de Approval com _Document Status is Pending second approval_ acima das outras regras de Approval.                  |

## Relacionados

* [Rule Conditions (Applies when)](../rule-conditions-applies-when.md)
* [Regras de Validação Personalizadas](../custom-validation-rules.md)
* [Regras de Transformação](../transformation-rules/)
* [Navegar no Layout Manager](navigating-the-layout-manager.md)
