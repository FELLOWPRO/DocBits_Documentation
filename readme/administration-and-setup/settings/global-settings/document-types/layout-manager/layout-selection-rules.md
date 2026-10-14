# Regras de Seleção de Layout

## Visão geral

Um **layout** decide quais campos e grupos um usuário vê — e em que ordem — nas telas de **validação**, **aprovação**, **rejeição** e **revisão** de um documento. Você cria os layouts no [Layout Manager](README.md).

Classicamente, o DocBits escolhia o layout pela **origem** do documento: o país ou a região obtidos das configurações de idioma do documento, como `DE` ou `US`. Cada origem tinha sua própria cópia do layout, e nada mais podia influenciar a escolha.

Com as **regras de seleção de layout**, os layouts passam a ser blocos reutilizáveis, independentes da origem, e as **regras** decidem qual layout um documento recebe:

> *Quando* o documento atende a uma condição, *então* ele recebe este layout. As regras são verificadas de cima para baixo; **a primeira regra que corresponder vence**. Se nenhuma regra corresponder, é usado o **layout padrão**.

A origem continua disponível — como uma condição entre muitas. Uma regra também pode considerar o fornecedor, o valor, o status do documento, o método de extração ou qualquer campo do cabeçalho.

### Problemas que elas resolvem

| Requisito | Layouts clássicos baseados na origem | Com regras de seleção |
| --- | --- | --- |
| As faturas de um fornecedor precisam de campos extras (projeto, número aduaneiro) | impossível sem uma nova origem | regra *Supplier ID is 20723* → layout "Invoice with project fields" |
| Os documentos de DE, AT e CH devem ter a mesma aparência | três cópias do mesmo layout para manter | um layout, uma regra por origem (ou um grupo ANY) apontando para ele |
| As faturas eletrônicas precisam de uma tela mais simples do que os PDFs digitalizados | não é possível | regra *Extraction Method is ELECTRONIC_DOCUMENT* → layout "E-invoice" |
| As faturas de alto valor precisam de mais campos na tela de aprovação | não é possível | regra de Approval *Total Amount greater than 10000* → layout "High value approval" |
| O segundo aprovador deve ver uma tela diferente da do primeiro | tipo de layout separado "segunda aprovação" | regra de Approval *Document Status is Pending second approval* → layout "Second approval" |

{% hint style="info" %}
Enquanto o recurso estiver em beta, as configurações descritas abaixo só aparecem quando a página de configurações **Document Types** é aberta com `?beta=true` anexado ao endereço.
{% endhint %}

## Ativar os layouts baseados em regras

Os layouts baseados em regras são ativados **por tipo de documento** por um **administrador da organização**.

1. Acesse **Settings → Global Settings → Document Types**.
2. Clique no ícone de **configurações** (engrenagem) no card do tipo de documento.
3. Abra **Manage Layouts** e ative o interruptor.

<figure><img src="../../../../../.gitbook/assets/doc-type-settings-rule-toggles.png" alt="O interruptor Manage Layouts"><figcaption><p>O interruptor Manage Layouts nas configurações adicionais de um tipo de documento</p></figcaption></figure>

O link **Layouts** no card do tipo de documento agora abre **Layouts & Selection Rules**.

### O que acontece quando você o ativa

O DocBits converte seus layouts existentes baseados em origem em regras — uma única vez, para este tipo de documento e para cada tela:

* O layout da origem **DEFAULT** passa a ser o **layout padrão** (o fallback).
* Cada layout de uma origem específica passa a ser uma regra **"Layout for XX"**, com a condição *Document Origin is XX*, apontando para esse layout. Essas regras recebem prioridades em intervalos de 10 (por exemplo 2000, 2010, 2020 …), para que você possa posicionar suas próprias regras antes, entre ou depois delas.

<figure><img src="../../../../../.gitbook/assets/layout-selection-default-row.png" alt="Regras de origem criadas na ativação e o layout padrão"><figcaption><p>As regras de origem criadas na ativação, seguidas do layout padrão (FALLBACK)</p></figcaption></figure>

Nada é excluído nem alterado nos próprios layouts. Logo após a ativação, portanto, cada documento recebe exatamente o layout que recebia antes. O comportamento só muda quando você adiciona ou altera regras.

**Desativá-lo** faz o tipo de documento voltar imediatamente à seleção baseada em origem. As regras são mantidas, mas não são usadas, e voltam a valer quando você reativa o interruptor.

## A tela Layouts & Selection Rules

<figure><img src="../../../../../.gitbook/assets/layouts-overview.png" alt="A aba Layouts"><figcaption><p>A aba Layouts: cada layout do tipo de documento como um card</p></figcaption></figure>

* **Layouts / Selection rules** (canto superior direito) alternam entre a lista de layouts e a lista de regras. Os números mostram quantos existem.
* **Field Validation / Approval / Reject / Review** alternam a **tela**. Cada tela tem seus próprios layouts, suas próprias regras e seu próprio layout padrão — uma regra de Approval nunca altera a tela de validação.
* Na aba **Layouts** você pode criar, editar, clonar e excluir layouts. Cada card mostra se uma regra usa o layout ("Not targeted by rules" quando nenhuma o usa). Filtre com **All / My layouts / System**; os layouts de sistema vêm com o DocBits e podem ser visualizados e clonados, mas não alterados.

{% hint style="info" %}
A primeira e a segunda aprovação compartilham os layouts e as regras de **Approval**. Para dar à segunda etapa de aprovação uma tela própria, adicione uma regra de Approval com a condição *Document Status is Pending second approval* — veja o [exemplo](#telas-diferentes-para-a-primeira-e-a-segunda-aprovacao).
{% endhint %}

## Como um layout é escolhido

Cada vez que um documento é aberto, e novamente depois que é salvo, o DocBits decide o layout para a tela atual:

1. As **regras ativas** da tela são verificadas em ordem de **prioridade** (o menor número primeiro). **A primeira regra cuja condição for verdadeira vence**, e seu layout é usado.
2. Se nenhuma regra corresponder, é usado o **layout padrão**.
3. Se também não houver um layout padrão, o DocBits volta à escolha clássica baseada em origem.

As regras cujo layout foi excluído ou está vazio são ignoradas.

### Um exemplo prático

Regras da tela **Field Validation**:

| Prioridade | Regra | Condição | Layout |
| --- | --- | --- | --- |
| 5 | Behaelterbau invoices | *Supplier ID is HP0000278* | Invoice with project fields |
| 10 | E-invoices | *Extraction Method is ELECTRONIC_DOCUMENT* | E-invoice |
| 2020 | Layout for DE | *Document Origin is DE* | Field Validation Layout (DE) |
| — | Layout padrão | — | Field Validation Layout (Base) |

Qual layout cada documento recebe:

| Documento | Fornecedor | Extração | Origem | Layout | Porque |
| --- | --- | --- | --- | --- | --- |
| 1 | HP0000278 | fatura eletrônica | DE | Invoice with project fields | a prioridade 5 corresponde primeiro; as regras seguintes não são verificadas |
| 2 | 10040 | fatura eletrônica | DE | E-invoice | a prioridade 5 não corresponde, a 10 sim |
| 3 | 10040 | PDF digitalizado | DE | Field Validation Layout (DE) | apenas a regra de origem corresponde |
| 4 | 10040 | PDF digitalizado | US | Field Validation Layout (Base) | nenhuma regra corresponde → padrão |

**A ordem importa**: coloque as regras específicas (um fornecedor) acima das regras gerais (um país).

### Quando um usuário altera um campo que as regras consideram

O layout é sempre escolhido a partir dos valores **atuais** do documento. Se um usuário corrigir, por exemplo, o fornecedor na tela de validação, o DocBits escolhe o layout novamente após o salvamento, e a tela pode passar para outro layout. Nenhum dado é perdido: um campo que não faz parte do novo layout mantém seu valor; ele apenas não é exibido até que volte a ser aplicado um layout que o contenha.

## Gerenciar as regras de seleção

<figure><img src="../../../../../.gitbook/assets/layout-selection-rules-list.png" alt="A aba Selection rules"><figcaption><p>A aba Selection rules da tela Field Validation</p></figcaption></figure>

Cada linha mostra a **prioridade** (a primeira linha é marcada como **FIRST**), o **nome e a chave da regra** com suas **condições**, o **layout de destino**, o selo de **origem** e um interruptor **Active**.

| Tarefa | Como |
| --- | --- |
| Criar uma regra | **New rule** |
| Editar uma regra | Clique na linha |
| Alterar a ordem | Arraste a alça à esquerda de uma linha para cima ou para baixo. A nova ordem é salva imediatamente. |
| Desativar uma regra | Interruptor **Active**. As regras inativas são ignoradas. |
| Duplicar ou excluir | Menu **⋮** da linha |
| Encontrar uma regra | **Search rules…** |

O selo de **origem** indica de onde vem uma regra: as regras **System** vêm com o DocBits. Editar uma delas cria uma cópia para a sua organização, exibida como **Customized**; o original permanece intacto e pode ser restaurado. As regras que você cria são **Custom**.

### O layout padrão

A última linha, marcada como **FALLBACK** e **is_default**, é o layout padrão: ele é usado sempre que nenhuma regra acima corresponde e não tem condição. É criado quando você ativa o recurso (a partir do layout da origem DEFAULT).

{% hint style="info" %}
Para usar outro layout de fallback, crie uma regra **sem nenhuma condição** e atribua-lhe o maior número de prioridade, para que seja verificada por último. Ela corresponde a todos os documentos que nenhuma regra anterior atendeu, antes de se chegar ao padrão.
{% endhint %}

## Criar uma regra

Clique em **New rule** na aba Selection rules da tela que você quer alterar.

<figure><img src="../../../../../.gitbook/assets/layout-rule-editor.png" alt="O editor de regras de seleção de layout"><figcaption><p>O editor de regras: frase-resumo no topo, três etapas à esquerda, pré-visualização em tempo real à direita</p></figcaption></figure>

A frase no topo resume a regra à medida que você a constrói — "When header.supplier_id = HP0000278, an INVOICE document gets the Field Validation Layout (Base) layout for Field validation. Checked at priority 5 — the first matching rule wins."

### Etapa 1 — Escopo e prioridade

| Configuração | O que faz |
| --- | --- |
| **Rule Name** | Exibido na lista de regras. Descreva o caso de negócio: "Behaelterbau invoices", "E-invoices", "High value approval". |
| **Rule key** | Gerada a partir do nome; permanece a mesma quando você renomeia a regra. |
| **Document Type** / **Layout type** | O tipo de documento e a tela para os quais a regra vale. Obtidos do local onde você clicou em **New rule**. |
| **Priority** | Os números menores são verificados primeiro. Deixe intervalos (5, 10, 20 …) para poder inserir regras depois. |

### Etapa 2 — Applies when

A condição que um documento deve atender. Você pode usar:

* **atributos do documento**: Document Origin, Extraction Method, Document Status, Sub Document Type,
* **campos do cabeçalho**: Supplier ID, Total Amount, Currency, Purchase Order e todos os demais campos do tipo de documento,
* um **caminho JSON personalizado** (Advanced).

As colunas de tabela não estão disponíveis: o layout é escolhido uma única vez para o documento inteiro.

Deixe a etapa vazia para corresponder a todos os documentos nessa prioridade. Como as condições funcionam — ALL / ANY, grupos aninhados, todos os operadores, valores vazios, maiúsculas/minúsculas — é explicado em [Condições da regra (Applies when)](../rule-conditions-applies-when.md).

### Etapa 3 — Layout de destino

Clique no layout que o documento deve receber. A lista mostra seus próprios layouts e os layouts de sistema da tela selecionada. Um layout não pode ser excluído enquanto uma regra ainda apontar para ele.

### Live preview · /resolve

O painel à direita mostra o que a regra faz com um documento de exemplo que tem os valores das suas condições:

| Linha | Significado |
| --- | --- |
| **Sample document** | Os valores usados na pré-visualização, obtidos das suas condições |
| **matched_by** | `rule` se uma regra correspondeu; caso contrário, o padrão |
| **Resolved layout** | O layout que o documento de exemplo receberia |
| **Priority hit** | A prioridade da regra que correspondeu |
| **watched_fields** | Os campos dos quais a escolha do layout depende. Quando um usuário altera um deles, o layout é escolhido novamente. |

Clique em **Create Rule** (ou **Save rule**, ao editar) para salvar. **Cancel** volta à lista de regras.

## Exemplos

### Campos extras para um fornecedor

Tela **Field Validation** · prioridade **5** · *Supplier ID is HP0000278* · destino *Invoice with project fields* (um clone do seu layout padrão com os campos adicionais de projeto e centro de custo).

### Um layout para vários países

Tela **Field Validation** · prioridade **100** · **ANY of**: *Document Origin is Deutsch*, *Document Origin is Austria*, *Document Origin is Switzerland* · destino *DACH invoice*. Desative as regras migradas "Layout for AT" e "Layout for CH" se elas apontarem para cópias mais antigas.

### Uma tela mais simples para faturas eletrônicas

Tela **Field Validation** · prioridade **10** · *Extraction Method is ELECTRONIC_DOCUMENT* · destino *E-invoice* (sem campos relacionados ao OCR).

### Uma tela de aprovação mais rigorosa para valores altos

Tela **Approval** · prioridade **10** · *Total Amount greater than 10000* · destino *High value approval* (exibindo centro de custo, responsável pelo orçamento e número do contrato).

### Telas diferentes para a primeira e a segunda aprovação

Tela **Approval** · prioridade **5** · *Document Status is Pending second approval* · destino *Second Approval Layout*. Os documentos na primeira etapa de aprovação não correspondem e recebem o layout padrão de Approval.

<figure><img src="../../../../../.gitbook/assets/layout-rule-approval-status.png" alt="Uma regra de aprovação baseada no status do documento"><figcaption><p>Uma regra de Approval para a segunda etapa de aprovação; a pré-visualização resolve o Second Approval Layout</p></figcaption></figure>

### Uma tela de rejeição especial para alguns fornecedores

Tela **Reject** · prioridade **10** · *Supplier ID is one of* `10040, 10041` · destino *Reject with reason codes*.

## Boas práticas

* **O específico antes do geral.** Regras de fornecedor acima das regras de país, regras de país acima do padrão.
* **Deixe intervalos de prioridade** (5, 10, 20 …) para que novas regras caibam sem renumeração.
* **Baseie as condições em campos confiáveis.** Fornecedor e origem são definidos cedo e raramente mudam. Condições sobre campos que os usuários editam com frequência fazem a tela trocar de layout enquanto eles trabalham.
* **Clone, não comece do zero.** Clone seu layout padrão e ajuste-o, para que todos os layouts mantenham a mesma estrutura básica.
* **Verifique a pré-visualização em tempo real** e abra um documento real de cada tipo após alterar as regras.
* **Mantenha um padrão útil** para cada tela, para que nenhum documento fique sem layout.

## Solução de problemas

| Sintoma | O que verificar |
| --- | --- |
| Um documento recebe o layout errado | Uma regra anterior corresponde primeiro. Veja as regras acima dela, ou o **Priority hit** na pré-visualização. |
| O padrão é usado embora uma regra devesse corresponder | A regra está **Active**? A condição corresponde ao valor exato (maiúsculas/minúsculas, espaços)? A regra está na aba de **tela** correta? |
| O layout muda enquanto um usuário trabalha | Um campo em **watched_fields** foi alterado. Baseie a regra em um campo mais estável. |
| Um layout não pode ser excluído | Uma regra ainda aponta para ele. Redirecione ou exclua essa regra primeiro. |
| Nenhum layout é exibido | Nenhuma regra correspondeu, não há padrão e não existe layout baseado em origem para esta tela. Adicione uma regra sem condição como coringa. |
| Nada mudou após a ativação | Esperado: a ativação reproduz a escolha anterior baseada em origem. Adicione suas próprias regras. |
| A segunda aprovação mostra o layout da primeira aprovação | Adicione uma regra de Approval com *Document Status is Pending second approval* acima das outras regras de Approval. |

## Relacionados

* [Condições da regra (Applies when)](../rule-conditions-applies-when.md)
* [Regras de Validação Personalizadas](../custom-validation-rules.md)
* [Regras de Transformação](../transformation-rules.md)
* [Navegando no Layout Manager](navigating-the-layout-manager.md)
