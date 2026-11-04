# Edição de Modelos de Email

### Visão Geral

O recurso de Modelos de Email permite que administradores criem e personalizem comunicações por email que são enviadas automaticamente para fornecedores. Um dos elementos-chave utilizados nesses modelos é o `{{magic_link}}`, que fornece um link dinâmico adaptado a cada destinatário.

<figure><img src="../../../.gitbook/assets/docbits_email_template_magic_link.png" alt="Docbits Email Template Magic Link"><figcaption></figcaption></figure>

#### O que é `{{magic_link}}`?

O `{{magic_link}}` é um espaço reservado que é substituído dinamicamente por uma URL única quando o email é enviado. Essa URL geralmente direciona o destinatário para completar uma ação, como registro, aprovação ou acesso a uma parte específica do portal do fornecedor.

### Edição de Modelos de Email

<figure><img src="../../../.gitbook/assets/docbits_email_template_editor_access.png" alt="Docbits Email Template Editor Access"><figcaption></figcaption></figure>

#### Acessando o Editor de Modelos de Email

1. **Navegue até Modelos de Email**:
   * Vá para a seção **Modelos de Email** no menu principal.
2. **Selecione um Modelo para Editar**:
   * Escolha o modelo de email que você deseja editar clicando no nome do modelo (por exemplo, "Email de Convite para Fornecedor").
3. **Edite o Modelo**:
   * O editor permite que você modifique tanto o código HTML quanto o design visual do email.
   * Você pode alternar entre edição visual e edição de código usando as abas fornecidas.

<figure><img src="../../../.gitbook/assets/docbits_email_template_visual_code_toggle.png" alt="Docbits Email Template Visual Code Toggle"><figcaption></figcaption></figure>

#### Definindo `{{magic_link}}` como um Link

Para definir `{{magic_link}}` como um link clicável no email, você precisa garantir que ele esteja formatado corretamente no código HTML do modelo. Siga estes passos:

1. **Localize a Seção do Link no Código HTML**:
   * No editor de código, encontre a seção onde você deseja que o link mágico apareça. Isso geralmente está dentro de uma tag `<a>` (âncora).
2. **Insira o Espaço Reservado `{{magic_link}}`**:

    * Substitua o atributo `href` da tag âncora por `{{magic_link}}`.
    * Certifique-se de que o link esteja estilizado adequadamente para o modelo de email. Aqui está um exemplo:

    ```html
    <a href="{{magic_link}}" target="_blank" style="
        background-color: #B7184B;
        border-radius: 25px;
        font-family: 'Montserrat', Arial, sans-serif;
        font-size: 14px;
        font-weight: bold;
        padding: 12px 25px;
        color: #FFFFFF;
        text-decoration: none;
        display: inline-block;
        cursor: pointer;">
        Completar Registro
    </a>
    ```

### 3. Personalize o Texto do Link:

• Modifique o texto entre as tags de abertura \<a> e fechamento \</a> para refletir a ação que você deseja que o usuário tome. Por exemplo, “Completar Registro” ou “Acessar Sua Conta”.

4. Salve e Teste o Modelo:

• Após fazer as alterações, clique no botão Salvar.

• Você pode usar o botão Enviar Teste para enviar um email de teste e garantir que o link esteja funcionando conforme o esperado.

## Melhores Práticas para Usar \{{magic\_link\}}

• Colocação do Link: Coloque o \{{magic\_link\}} de forma proeminente no email para garantir que seja facilmente acessível aos destinatários.

• Chamada à Ação Clara: O texto dentro do link deve ser uma chamada à ação clara, como “Completar Registro” ou “Confirmar Seu Email.”

• Estilização: Certifique-se de que o link esteja estilizado de forma consistente com o restante do modelo de email e se destaque visualmente.

• Testes: Sempre envie um email de teste após editar o modelo para verificar se o \{{magic\_link\}} é resolvido corretamente e se a estilização está apropriada.

## Conclusão

Ao definir corretamente o \{{magic\_link\}} em seus modelos de email, você pode garantir que os destinatários recebam um email personalizado e acionável que os guie para a tarefa apropriada dentro do seu portal de fornecedores. Isso melhora a experiência do usuário e garante processos de integração e comunicação suaves.

\


Esta documentação fornece instruções passo a passo para administradores sobre como definir e usar o \{{magic\_link\}} em modelos de email, garantindo que os emails sejam funcionais e visualmente atraentes.