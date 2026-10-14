---
description: >-
  Como encontrar e criar as chaves API que dão a outros sistemas acesso ao
  DocBits
---

# API Key Management

Uma API key permite que outro sistema — o seu ERP, um script ou uma aplicação de um parceiro — fale com o DocBits sem que um utilizador inicie sessão. A sua organização pode ter tantas chaves quantas precisar, e cada uma é gerida em separado: dê-lhe um nome próprio, decida se expira e revogue-a isoladamente se alguma vez for exposta.

Como cada integração pode ter a sua própria chave, pode desligar uma sem perturbar nenhuma das outras.

## Abrir a gestão de chaves API

Vá a **Settings** e selecione **Integration & SSO** em **System & Administration**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-settings-overview.png)

A secção **API Key** no topo da página lista todas as chaves que a sua organização tem.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-list.png)

## Compreender a lista

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-list-row.png)

| Coluna | O que lhe diz |
| --- | --- |
| **Key** | Os primeiros caracteres da chave, seguidos de `****`. O resto nunca mais é mostrado depois de a criar — consulte [Criar uma chave API](#criar-uma-chave-api). |
| **Name** | O nome que deu à chave, com a descrição por baixo. |
| **Expires** | A data em que a chave deixa de funcionar, ou **Never** se não tiver definido nenhuma. |
| **Last Used** | Quando chegou pela última vez um pedido com esta chave. **Never used** significa que nenhum sistema a usou ainda — útil para detetar chaves que pode remover com segurança. |
| **Status** | **Active** significa que a chave funciona. Uma chave revogada fica desligada permanentemente. |
| **Actions** | O menu de três pontos, onde pode revogar a chave. |

Se tiver mais chaves do que cabem numa página, use os controlos de paginação no fundo da lista.

{% hint style="info" %}
**Last Used** é a forma mais rápida de encontrar chaves de que já ninguém precisa. Uma chave que nunca foi usada, ou que não é usada há meses, é uma boa candidata a revogação.
{% endhint %}

## Criar uma chave API

1. Clique em **+ Create API Key** no canto superior direito da secção API Keys.
2. Preencha a caixa de diálogo:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-create-dialog.png)

| Campo | O que introduzir |
| --- | --- |
| **Key Name** | Obrigatório. Dê-lhe o nome do sistema que a vai usar — `M3 Production`, `Invoice Import Script` — para conseguir perceber mais tarde a que integração pertence cada chave. |
| **Description** | Opcional. Espaço para uma nota sobre para que serve a chave ou quem a configurou. |
| **Expiration** | Escolha uma data de expiração, ou deixe em **Never expires**. Uma data de expiração é a opção mais segura: a chave reforma-se sozinha se a integração alguma vez for esquecida. |

3. Clique em **Create**. O DocBits mostra-lhe a nova chave:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/api-key-created.png)

4. Copie a chave com o ícone de cópia e cole-a diretamente no sistema que a vai usar, ou no seu gestor de palavras-passe.
5. Assinale **I have copied and saved this key** e clique em **Done**.

{% hint style="danger" %}
**A chave completa é mostrada apenas uma vez.** O DocBits guarda-a de forma cifrada que não pode ser revertida ao original, pelo que ninguém — nem os seus administradores, nem o suporte do DocBits — a consegue consultar depois. Se a perder, revogue a chave e crie uma nova.
{% endhint %}

Trate a chave como uma palavra-passe. Qualquer pessoa que a tenha pode atuar sobre os documentos e os dados da sua organização.
