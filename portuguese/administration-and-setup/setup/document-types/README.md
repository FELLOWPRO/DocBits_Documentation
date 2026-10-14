# Tipos de Documento

Os tipos de documento informam ao DocBits com quais tipos de documentos a sua organização trabalha. Um administrador os encontra em **Settings → Document Types**, na seção **Document Processing** do menu de configurações.

A página mostra os **Default Document Types**, que o DocBits fornece e que você não pode excluir, seguidos dos **Custom Document Types** criados para a sua organização. Cada tipo tem o seu próprio cartão.

<figure><img src="../../../.gitbook/assets/document-types-overview-en-20260928.png" alt="Página Document Types com o cartão Invoice e outros cartões de tipos de documento padrão, interruptores de ativação e extração, engrenagem de configurações e links de configuração"><figcaption><p>Escolha o cartão de um tipo de documento para configurar esse tipo.</p></figcaption></figure>

## O que você pode fazer em um cartão

| Controle | O que faz |
| --- | --- |
| **Activate** | Torna este tipo de documento disponível ou indisponível na sua organização. Um interruptor azul está ligado; um interruptor cinza está desligado. |
| **Extraction** | Escolhe o modo de extração: **Flex** quando ligado ou **Fix** quando desligado. Ele não simplesmente liga ou desliga a extração. Passe o mouse sobre o interruptor para ver o modo atual. |
| **Settings** (engrenagem) | Abre **More Settings** para este tipo. Expanda uma categoria ali para ver suas opções. As categorias dependem do tipo de documento. |
| **Layouts** | Abre a configuração de layouts. Consulte [Layout Builder](layout-builder.md) para os próximos passos. |
| **Fields** | Abre as configurações de campos e de reconhecimento deste tipo. Consulte [Fields](../../settings/global-settings/document-types/fields/README.md) para saber como configurá-los. |
| **Tables** | Abre a configuração das colunas de tabela deste tipo. |
| **Scripts** | Abre os scripts de processamento quando este recurso está disponível. |
| **Model Training** | Abre o treinamento de modelo para este tipo. |
| **E-Doc** | Abre as configurações de documentos eletrônicos quando o tipo as suporta. |
| **Document Sub Types** | Abre os subtipos deste tipo de documento. |

Você pode ver mais links, como regras de validação ou de transformação, dependendo dos recursos da sua organização. Escolha o link no cartão do tipo que você deseja alterar.

## Edite os campos e as configurações de reconhecimento

Clique em **Fields** em um cartão para ver seus grupos de campos. Na parte superior dessa página, **OCR** e **Match Score** definem os limites de reconhecimento, **Restore Defaults** redefine esses limites e **Search by Name** encontra um campo. Use **Create new group** para organizar os campos e **Create field** dentro de um grupo para adicionar um. **Master Data Settings** abre a configuração de dados mestres relacionada.

Cada linha de campo tem controles como **Required**, **Read Only**, **Hidden**, **Force Validation**, **Use AI**, OCR, Match Score e Formula. Revise o [guia de Fields](../../settings/global-settings/document-types/fields/README.md) antes de alterar valores individuais. Clique em **Save Settings** na página Fields para manter suas alterações.

<figure><img src="../../../.gitbook/assets/document-types-invoice-fields-en-20260928.png" alt="Página Invoice Fields com configurações de reconhecimento, grupos de campos, controles por campo e Save Settings"><figcaption><p>A página Fields tem o seu próprio botão Save Settings.</p></figcaption></figure>

## Crie um tipo de documento personalizado

Role até **Custom Document Types** e clique em **+ New**. Siga [Adicionando/Editando Tipos de Documento](../../settings/global-settings/document-types/adding-editing-document-types.md) para configurar o novo tipo.

<figure><img src="../../../.gitbook/assets/document-types-custom-new-en-20260928.png" alt="Parte inferior da página Document Types mostrando a seção Custom Document Types e o botão New"><figcaption><p>Use New em Custom Document Types para começar a criar um tipo.</p></figcaption></figure>
