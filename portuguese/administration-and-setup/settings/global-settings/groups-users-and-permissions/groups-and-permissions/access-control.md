# Controle de Acesso

## Visão geral

O Controle de Acesso define, para um único **grupo** (função), exatamente o que seus membros podem fazer — tanto no **nível do tipo de documento** (quais tipos de documento veem e quais ações podem realizar) quanto no **nível do campo** (quais campos individuais podem ler ou editar).

As permissões são sempre avaliadas **por grupo**. Um usuário herda as permissões de cada grupo ao qual pertence.

{% hint style="info" %}
O Controle de Acesso só é aplicado quando o sistema de **Grupos e Permissões** está ativado (consulte [Ativar Permissões](activating-permissions.md)). **Os administradores sempre ignoram o Controle de Acesso** e podem ver e fazer tudo, independentemente das configurações desta página.
{% endhint %}

Cada grupo pode ser configurado para:

* **Acesso ao documento** — se o grupo pode usar um tipo de documento.
* **Permissões de ação** — quais ações (listar, visualizar, editar, excluir, atualização em massa, aprovar) o grupo pode realizar e *para quais documentos*.
* **Permissões de campo** — se cada campo individual de um tipo de documento é editável, somente leitura ou oculto.

## Ativação

1. Vá para **Configurações**.
2. Selecione **Processamento de Documentos**.
3. Selecione **Módulo.**
4. Ative o **Controle de Acesso** habilitando o controle deslizante.

<figure><img src="../../../../../.gitbook/assets/Access-Control3.png" alt=""><figcaption></figcaption></figure>

## Abrir o Controle de Acesso de um grupo

1. Vá para **Configurações**.
2. Vá para **Configurações Globais**.
3. Selecione **Grupos, Usuários e Permissões**.
4. Selecione **Grupos e Permissões**.
5. Para gerenciar as permissões de um grupo (por exemplo, PROCUREMENT\_DIRECTOR), clique nos três pontos do lado direito.
6. Selecione **Gerenciar Controle de Acesso**.

<figure><img src="../../../../../.gitbook/assets/access_control_open_menu.png" alt="Abrir o menu de linha de um grupo e escolher Gerenciar Controle de Acesso"><figcaption><p>Na página «Grupos e Permissões», abra o menu <strong>⋮</strong> de um grupo e escolha <strong>Gerenciar Controle de Acesso</strong>.</p></figcaption></figure>

## Como uma permissão é avaliada

Quando um usuário tenta fazer algo com um documento, o DocBits verifica, em ordem:

1. **O sistema de Grupos e Permissões está ativado e o usuário não é administrador?** Se estiver desativado, ou o usuário for administrador → acesso total.
2. **O tipo de documento está habilitado para um dos grupos do usuário?** Se estiver desabilitado → o usuário não pode ver nem usar esse tipo de documento.
3. **Qual escopo de acesso está definido para a ação?** (por exemplo, *Editar = Owner*). O escopo é comparado com a relação do usuário com *este documento específico* — ele é o proprietário, o responsável, ambos ou nenhum?
4. **Qual permissão de campo se aplica?** Mesmo quando um usuário pode abrir um documento, campos individuais ainda podem estar ocultos ou bloqueados.

## Permissões no nível do tipo de documento

Cada linha da matriz é um tipo de documento (Invoice, Credit Note, Purchase Order, …).

A primeira coluna é um interruptor **Habilitado / Desabilitado**. Desabilite-o e o grupo não poderá usar esse tipo de documento de forma alguma — ele desaparece do painel. Habilite-o e as sete colunas de ação tornam-se editáveis.

| Ação | Determina se o grupo pode… |
|------|----------------------------|
| **Listar** | ver o tipo de documento na lista do painel. |
| **Visualizar** | abrir um documento e ver seus detalhes. |
| **Editar** | alterar os valores dos campos de um documento. |
| **Excluir** | excluir um documento. |
| **Atualização em Massa** | aplicar uma atualização em massa a vários documentos de uma vez. |
| **Primeira Aprovação** | conceder a aprovação de primeiro nível. |
| **Segunda Aprovação** | conceder a aprovação de segundo nível. |

### Escopos de acesso

Cada coluna de ação é um menu suspenso. O valor escolhido responde à pergunta *«para quais documentos o grupo pode fazer isso?»*. Os nomes dos escopos aparecem em inglês na interface:

| Escopo | Quem é permitido | Efeito em um documento |
|--------|------------------|------------------------|
| **No Access** | Ninguém no grupo. | A ação é bloqueada para todos no grupo — o botão fica oculto ou desativado. |
| **Everyone** | Todos os membros do grupo. | Qualquer membro do grupo pode realizar a ação em **qualquer** documento desse tipo. |
| **Owner** | Apenas o usuário que **criou / carregou** o documento. | A ação só funciona em documentos que o próprio usuário carregou. |
| **Assignee** | Apenas o usuário (ou grupo) ao qual o documento está **atribuído**. | A ação só funciona em documentos atribuídos ao usuário ou a um grupo ao qual ele pertence. |
| **Owner & Assignee** | O proprietário **ou** o responsável. | A ação funciona se o usuário for *ou* quem carregou *ou* o responsável. |

{% hint style="info" %}
**Owner** e **Assignee** dependem da *relação entre o usuário e cada documento individual*, portanto dois membros do mesmo grupo podem ter direitos diferentes sobre a mesma fatura — consulte o exemplo prático abaixo.
{% endhint %}

<figure><img src="../../../../../.gitbook/assets/access_control_matrix.png" alt="Matriz de Controle de Acesso de um grupo"><figcaption><p>A matriz de permissões por tipo de documento. Aqui o tipo <strong>Invoice</strong> está habilitado e suas ações têm escopos de acesso diferentes; os demais tipos estão desabilitados.</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/access_control_scope_dropdown.png" alt="Menu suspenso de escopos de acesso"><figcaption><p>Cada coluna de ação oferece os mesmos cinco escopos de acesso.</p></figcaption></figure>

### A aprovação também requer Editar

Aprovar um documento aciona **duas ações** nos bastidores: o DocBits primeiro **salva** o documento e depois o move para o status aprovado. A etapa de salvamento precisa da permissão **Editar**, portanto as duas permissões estão vinculadas.

Um usuário a quem se concede apenas **Primeira Aprovação** ou **Segunda Aprovação** — mas *não* **Editar** — encontra um erro de permissão na etapa de salvamento e não consegue aprovar o documento.

{% hint style="warning" %}
Sempre que conceder **Primeira Aprovação** ou **Segunda Aprovação**, conceda também **Editar** (e **Visualizar**) para o mesmo tipo de documento. Uma permissão de aprovação por si só não é suficiente.
{% endhint %}

## Permissões no nível do campo

Clique em uma linha de tipo de documento para abrir o painel **Permissões de Campo** abaixo. Os campos são organizados em abas (por exemplo, *Colunas da tabela*, *Detalhes da fatura*, *Detalhes de pagamento*, *Impostos e valores*). Cada campo tem seu próprio nível de acesso:

| Nível | Efeito no campo |
|-------|-----------------|
| **Leitura/Escrita** | O campo é visível **e** editável. |
| **Somente leitura** | O campo é visível, mas **não pode ser editado** (esmaecido). |
| **Aprovação** | O campo pode ser editado, mas a alteração deve passar por um **fluxo de aprovação** antes de ser aplicada. |
| **Sem acesso** | O campo fica **totalmente oculto** — o usuário nunca o vê. |

{% hint style="info" %}
As regras de campo se aplicam igualmente a **todos** os membros do grupo — não dependem do proprietário/responsável. Use-as para ocultar ou bloquear campos sensíveis (por exemplo, um desconto ou um valor total) para um grupo inteiro.
{% endhint %}

<figure><img src="../../../../../.gitbook/assets/access_control_field_permissions.png" alt="Painel Permissões de Campo"><figcaption><p>O painel «Permissões de Campo» para o tipo Invoice. <code>CUSTOMER_DISCOUNT</code> está oculto (Sem acesso) enquanto os demais campos permanecem em Leitura/Escrita.</p></figcaption></figure>

## Exemplo prático: o que o Controle de Acesso faz em uma fatura real

Suponha que você crie um grupo **AP_CLERK** para seus auxiliares de contas a pagar e configure o tipo de documento **Invoice** assim:

**Permissões de tipo de documento para Invoice**

| Ação | Escopo |
|------|--------|
| Habilitado | ✅ Sim |
| Listar | Everyone |
| Visualizar | Everyone |
| Editar | Owner & Assignee |
| Excluir | No Access |
| Atualização em Massa | No Access |
| Primeira Aprovação | Assignee |
| Segunda Aprovação | No Access |

**Permissões de campo para Invoice**

| Campo | Nível |
|-------|-------|
| `TOTAL_AMOUNT` | Somente leitura |
| `CUSTOMER_DISCOUNT` | Sem acesso |
| *(todos os outros campos)* | Leitura/Escrita |

Agora acompanhe um documento concreto — a fatura **INV-4711**, que **Maria carregou** e que está **atribuída a Maria**. Tanto Maria quanto seu colega Tom estão no grupo **AP_CLERK**.

**Maria (proprietária *e* responsável por INV-4711):**

* ✅ Vê INV-4711 na lista do painel *(Listar = Everyone)*.
* ✅ Abre-a *(Visualizar = Everyone)*.
* ✅ Edita o nome do fornecedor e os itens *(Editar = Owner & Assignee — ela é a proprietária)*.
* 🔒 Vê `TOTAL_AMOUNT`, mas o campo está esmaecido e ela não pode alterá-lo *(Somente leitura)*.
* 🚫 Nunca vê o campo `CUSTOMER_DISCOUNT` *(Sem acesso)*.
* 🚫 O botão **Excluir** está oculto *(Excluir = No Access — ninguém no grupo pode excluir)*.
* ✅ Pode conceder a **primeira aprovação** *(Primeira Aprovação = Assignee — ela é a responsável)*.

**Tom (mesmo grupo, mas *não* carregou INV-4711 e ela *não* está atribuída a ele):**

* ✅ Vê-a na lista e ✅ abre-a *(Listar e Visualizar = Everyone)*.
* 🚫 Não pode editar nada — o documento abre em **somente leitura** *(Editar = Owner & Assignee — Tom não é nenhum dos dois)*.
* 🔒 / 🚫 Vê exatamente a mesma visibilidade de campos que Maria: `TOTAL_AMOUNT` bloqueado, `CUSTOMER_DISCOUNT` oculto *(as regras de campo se aplicam ao grupo inteiro)*.
* 🚫 Não pode conceder a primeira aprovação *(Primeira Aprovação = Assignee — não é Tom)*.
* 🚫 Não pode excluir *(No Access)*.

**O que este exemplo mostra**

* **Everyone** abre um documento para todos os membros do grupo; **Owner / Assignee** restringe uma ação às pessoas vinculadas àquele documento específico.
* **No Access** remove uma ação (Excluir) ou oculta um campo (`CUSTOMER_DISCOUNT`) para o grupo inteiro.
* **Somente leitura** mantém um campo visível para referência (`TOTAL_AMOUNT`), mas impede alterações.
* Duas pessoas no **mesmo grupo** podem ter **direitos diferentes sobre a mesma fatura**, apenas por causa de quem a carregou e a quem ela está atribuída.
