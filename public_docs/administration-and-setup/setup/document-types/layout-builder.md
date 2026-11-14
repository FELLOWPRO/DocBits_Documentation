# Construtor de Layouts

Utilize o Construtor de Layouts para organizar os campos e os controlos que as pessoas veem ao validar ou aprovar um documento. Um layout pertence a um tipo de documento, uma origem e um tipo de layout, por isso confirme esses três no topo da página antes de guardar.

{% embed url="https://youtu.be/-m45XGiIeig" %}
DocBits Layout Builder Tutorial: Create Custom Document Layouts for Faster, Cleaner Validation
{% endembed %}

## Abrir o layout

1. Abra **Settings → Document Types**.
2. Selecione o tipo de documento que pretende editar e abra **Layout Builder**. Para um subtipo de documento, abra a ação Layout Builder desse subtipo.
3. Confirme o cabeçalho. O seletor da esquerda é a **origin** (por exemplo **Default**), seguido de **Document Type** (por exemplo **Invoice**) e de **Layout type** (por exemplo **Field Validation**). Cada seletor abre uma lista; escolher outra entrada carrega esse layout. Se o Layout Builder não estiver disponível, um administrador poderá ter de ativar o módulo para a sua organização.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/layout-builder-overview.png" alt="O Layout Builder de uma fatura no DocBits, com os seletores origin, Document Type e Layout type, os separadores Structure, Fields e Elements, a área do layout e o painel Properties à direita"><figcaption><p>O Layout Builder: os seletores do cabeçalho, as listas de elementos à esquerda, a área do layout ao centro e o painel Properties à direita.</p></figcaption></figure>

## Trabalhar com o cabeçalho

* **Document Type** e **Layout type** alternam entre layouts. A página recarrega o layout que escolher.
* Ao lado de **Save**, o DocBits mostra se o layout tem **unsaved changes**. Depois de guardar, mostra quando o layout foi guardado pela última vez.
* **Save** guarda o layout para o tipo de documento, a origem e o tipo de layout selecionados.
* O menu **More** (três pontos) contém **Auto Generate template**, **Apply Default layout to Origins**, **Use default template**, **Edit JSON**, **Copy JSON** e **Layout settings**. **Auto Generate template** e **Use default template** substituem um layout personalizado, por isso confirme primeiro o tipo de documento e o layout selecionados. **Edit JSON** destina-se a configuração avançada e só deve ser utilizado quando compreende o formato do modelo.
* Se sair da página com alterações não guardadas, o DocBits pergunta se as pretende guardar ou descartar.

## Encontrar elementos: Structure, Fields, Elements

O lado esquerdo tem três separadores:

| Separador | Utilize para |
| --- | --- |
| **Structure** | Ver o layout como uma árvore. Os grupos e os respetivos campos são listados pela ordem em que aparecem na área do layout, com o número de campos colocados e disponíveis. |
| **Fields** | Todos os campos configurados para o tipo de documento, agrupados por grupo de campos e recolhidos por predefinição. O filtro alterna entre campos **All**, **Unused** e **Hidden**, e o nome técnico do campo é apresentado por baixo do rótulo do campo. |
| **Elements** | Controlos de apresentação e interação, como Text, Label, Check Box, linhas separadoras, tabelas, botões e subgrupos. |

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/layout-builder-structure.png" alt="O separador Structure do Layout Builder, com os grupos Invoice details, Payment details, Purchase Order e Delivery Details expandidos nos respetivos campos"><figcaption><p>O separador Structure apresenta o layout construído como uma árvore de grupos e campos.</p></figcaption></figure>

Selecione um item para o adicionar ou arraste-o para a área do layout. O título de um grupo indica à pessoa que valida o documento o que pertence a essa secção. Crie ou renomeie os campos de documento reutilizáveis em [Document Types](README.md) primeiro.

## Trabalhar na área do layout

* **Main layout** apresenta o layout do próprio documento. **Table** apresenta o layout de tabela utilizado para as linhas.
* **Document** abre ou fecha o documento de exemplo ao lado da área do layout, para poder comparar o layout com um documento real.
* Os grupos são desenhados como cartões; os campos dentro de um grupo podem ser organizados em linhas e receber larguras diferentes.

## Alterar as propriedades de um elemento

Selecione um elemento ou um grupo na área do layout. **Properties**, à direita, está sempre visível e está organizado em secções:

* **Display** – rótulo, nome do campo, posição do rótulo e largura do elemento.
* **Behaviour** – apenas leitura, oculto e índice de tabulação.
* **Values & lists** – os valores oferecidos para o elemento.
* **Automation** – regras que preenchem ou alteram o elemento.
* **Borders & spacing** – a aparência do elemento.

Para a largura, escolha uma das predefinições (25, 33, 50, 66, 75 ou 100 por cento) em vez de introduzir um valor; confirme o resultado na área do layout. As secções e as opções apresentadas dependem do elemento selecionado. Para mais detalhes, consulte [Configurar propriedades dos campos](../../settings/global-settings/document-types/layout-manager/configuring-field-properties.md).

## Traduzir rótulos de botões

Botões como **Save Rules**, **Auto Accounting**, **PO Match**, **Export**, **Export Without Validation** e **Reject** obtêm o rótulo a partir de uma chave de tradução. O visualizador mostra o rótulo no idioma da pessoa que abre o layout. Se a chave não tiver texto para esse idioma, o DocBits mostra o rótulo que foi guardado no layout.

* Um botão autónomo tem um campo **Translation Key** em **Properties**.
* **Invoice Buttons** agrupa vários botões. Defina a chave para um único botão filho, ou defina uma chave por filho na lista do painel do grupo.

Os layouts criados antes desta alteração mantêm os seus rótulos: o DocBits preenche para eles a chave predefinida de cada tipo de botão. Os layouts guardados com uma chave mantêm essa chave, também depois de recarregar.

## Save and go back to Dashboard

Um botão do tipo **Save and go back to Dashboard** guarda os valores do documento como **Save** e abre em seguida o Dashboard. O tipo é adequado a layouts em que um revisor percorre uma fila de documentos, um após outro.

* Adicione um elemento de botão na área do layout e escolha o tipo em **Properties**.
* Se a gravação falhar, o botão permanece no ecrã de validação e não abre o Dashboard, para que o problema possa ser corrigido primeiro.
* O rótulo é obtido como o rótulo de qualquer outro botão; consulte *Traduzir rótulos de botões* acima.

## Rever e guardar

Organize os grupos e os campos, confirme o layout na área do layout e utilize **Save** no cabeçalho quando o resultado estiver correto. Para layouts específicos de uma origem, consulte [Layouts de origem](origin-layouts.md).

{% hint style="info" %}
As capturas de ecrã mostram definições sintéticas na organização de teste do DocBits, com o inglês selecionado na aplicação. Nenhum layout foi guardado ou substituído durante as capturas.
{% endhint %}
