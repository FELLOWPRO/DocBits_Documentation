# Gestor de Regex

Esta função do DocBits oferece uma alternativa à classificação por modelo, pois permite escrever expressões regulares pesquisáveis para um tipo de documento, para classificação e outros fins.

Tipo de documento: o Gestor de Regex permite escrever expressões regulares, que depois são procuradas no documento. Se o DocBits encontrar uma correspondência com a expressão regular de um documento definido, classifica o documento no tipo de documento correspondente. Por exemplo, se escrever uma expressão regular para encontrar “Gutschrift” e o DocBits encontrar esse termo num documento, classifica-o como nota de crédito.

Origem do documento: através de expressões regulares, o DocBits reconhece também o país de origem de um documento. Por exemplo, se uma expressão regular para um documento espanhol contiver o termo “Factura” e o DocBits o encontrar no documento, saberá que o documento é de origem espanhola e classificá-lo-á em conformidade.

## **Aceder ao Gestor de Regex**

No DocBits, aceda a Configurações → Tipos de documentos. Em “Tipos de documentos personalizados”, clique em “Novo”. Introduza um nome para o tipo de documento, adicione uma descrição opcional e marque “Mesa disponível” se o documento contiver uma tabela. Depois escolha “Expressão regular” em vez de “Auto” e clique em “Próximo”.

<figure><img src="../../../.gitbook/assets/regex-manager-create-pt-20261006.png" alt="Página de criação de um novo tipo de documento com o campo de nome, a caixa de tabela disponível, a descrição e os botões Auto e Expressão regular"><figcaption><p>Escolha “Expressão regular” para classificar o novo tipo de documento com expressões regulares.</p></figcaption></figure>

## **Adicionar e remover regex**

O passo “Expressão regular” mostra os modelos de regex existentes, cada um com origem e padrão, e um botão “Adicionar” para criar um novo modelo. Use o menu de ações no fim da linha para gerir a entrada. Clique em “Próximo” para continuar para “Campos e grupos”.

<figure><img src="../../../.gitbook/assets/regex-manager-list-pt-20261006.png" alt="Passo Expressão regular com o botão Adicionar e uma tabela com três modelos de regex, com origem, padrão e ações"><figcaption><p>Modelos de regex existentes com origem e padrão. “Adicionar” cria um novo modelo.</p></figcaption></figure>
