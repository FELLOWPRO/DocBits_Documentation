# Construtor de Layouts

Utilize o Construtor de Layouts para organizar os campos e os controlos que as pessoas veem ao validar ou aprovar um documento. Um layout pertence a um tipo de documento, a uma origem e a um tipo de layout, por isso confirme estes três elementos no topo da página antes de guardar.

## Abrir o layout

1. Abra **Configurações → Tipos de documentos**.
2. Selecione o tipo de documento que pretende editar e abra o **Construtor de Layouts**. No caso de um subtipo de documento, abra a ação Construtor de Layouts desse subtipo.
3. Verifique o cabeçalho. O seletor da esquerda corresponde à **Origem** (por exemplo, **Padrão**), seguido do **Tipo de documento** (por exemplo, **Fatura**) e do **Tipo de layout** (por exemplo, **Validação de campos**). Cada seletor abre uma lista; ao escolher outra entrada, esse layout é carregado. Se o Construtor de Layouts não estiver disponível, poderá ser necessário que um administrador ative o módulo para a sua organização.

<figure><img src="../../../.gitbook/assets/layout-builder-overview-pt.png" alt="O Construtor de Layouts de uma fatura no DocBits, com os seletores de origem, tipo de documento e tipo de layout, os separadores Estrutura, Campos e Elementos, a tela do layout e o painel Propriedades à direita"><figcaption><p>O Construtor de Layouts: os seletores do cabeçalho, as listas de elementos à esquerda, a tela ao centro e o painel Propriedades à direita.</p></figcaption></figure>

## Trabalhar com o cabeçalho

* **Tipo de documento** e **Tipo de layout** permitem alternar entre layouts. A página recarrega o layout que escolher.
* Junto a **Salvar**, o DocBits indica se o layout tem **Alterações não salvas**. Depois de guardar, mostra a data em que o layout foi guardado pela última vez.
* **Salvar** guarda o layout para o tipo de documento, a origem e o tipo de layout selecionados.
* O menu **Mais** (três pontos) contém **Gerar modelo automaticamente**, **Aplicar layout padrão às origens**, **Usar modelo padrão**, **Editar JSON**, **Copiar JSON** e **Configurações de layout**. **Gerar modelo automaticamente** e **Usar modelo padrão** substituem um layout personalizado, por isso confirme primeiro o tipo de documento e o layout selecionados. **Editar JSON** destina-se a configuração avançada e só deve ser utilizado se compreender o formato do modelo.
* Se sair da página com alterações por guardar, o DocBits pergunta se pretende guardá-las ou descartá-las.

## Encontrar elementos: Estrutura, Campos, Elementos

O lado esquerdo tem três separadores:

| Separador | Para que serve |
| --- | --- |
| **Estrutura** | Ver o layout em forma de árvore. Os grupos e os respetivos campos são apresentados pela ordem em que surgem na tela, com o número de campos colocados e disponíveis. |
| **Campos** | Todos os campos configurados para o tipo de documento, agrupados por grupo de campos e recolhidos por predefinição. O filtro alterna entre os campos **Todos**, **Não utilizado** e **Escondido**, e o nome técnico do campo é apresentado por baixo do rótulo. |
| **Elementos** | Controlos de apresentação e interação, como Texto, Rótulo, Caixa de verificação, separadores, tabelas, botões e subgrupos. |

<figure><img src="../../../.gitbook/assets/layout-builder-structure-pt.png" alt="O separador Estrutura do Construtor de Layouts a mostrar os grupos Dados da fatura, Dados de pagamento, Encomenda e Dados de entrega expandidos nos respetivos campos"><figcaption><p>O separador Estrutura mostra o layout criado como uma árvore de grupos e campos.</p></figcaption></figure>

Selecione um item para o adicionar ou arraste-o para a tela. O título de um grupo indica a quem valida o documento o que pertence a essa secção. Crie ou mude o nome dos campos de documento reutilizáveis primeiro em [Tipos de documentos](README.md).

## Trabalhar na tela

* **Layout principal** mostra o layout do próprio documento. **Tabela** mostra o layout da tabela utilizado para as linhas de itens.
* **Documento** abre ou fecha o documento de exemplo junto à tela, permitindo comparar o layout com um documento real.
* Os grupos são apresentados como cartões; os campos dentro de um grupo podem ser dispostos em linhas e ter larguras diferentes.

## Alterar as propriedades de um elemento

Selecione um elemento ou um grupo na tela. O painel **Propriedades**, à direita, está sempre visível e está organizado em secções:

* **Mostrar** – rótulo, nome do campo, posição do rótulo e largura do elemento.
* **Comportamento** – somente leitura, escondido e índice de guias.
* **Valores e listas** – os valores propostos para o elemento.
* **Automação** – regras que preenchem ou alteram o elemento.
* **Bordas e espaçamento** – o aspeto do elemento.

Para a largura, escolha uma das predefinições (25, 33, 50, 66, 75 ou 100 por cento) em vez de introduzir um valor; confirme o resultado na tela. As secções e as opções apresentadas dependem do elemento selecionado. Para mais detalhes, consulte [Configurar propriedades dos campos](../../settings/global-settings/document-types/layout-manager/configuring-field-properties.md).

## Rever e guardar

Organize os grupos e os campos, verifique o layout na tela e utilize **Salvar** no cabeçalho quando o resultado estiver correto. Para layouts específicos de uma origem, consulte [Layouts de origem](origin-layouts.md).

{% hint style="info" %}
As capturas de ecrã mostram definições sintéticas na organização de teste do DocBits, com o português selecionado na aplicação. Nenhum layout foi guardado ou substituído durante a sua captura.
{% endhint %}
