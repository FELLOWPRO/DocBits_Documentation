# Autenticação de Dois Fatores (Admin)

## Visão geral

Como administrador de uma organização, você pode **exigir que cada membro use a autenticação de dois fatores (2FA)** ao entrar com uma senha. Quando a exigência está ativada, um membro que ainda não configurou um segundo fator é orientado pelo processo de cadastro antes de concluir o login.

Os logins com Single Sign-On (SSO) — Google, Microsoft, SAML — estão **isentos**: o provedor de identidade deles já aplica o próprio MFA, portanto a exigência afeta apenas os logins com senha.

Essa configuração fica em **Configurações → Configurações Globais → Informações da Empresa → Autenticação de dois fatores** e está disponível apenas para administradores da organização.

## Exigir MFA para a sua organização

1. Vá para **Configurações → Configurações Globais → Informações da Empresa**.
2. Abra a seção **Autenticação de dois fatores**.
3. Ative **Exigir autenticação de dois fatores para todos os membros** e clique em **Salvar**.

<figure><img src="../../../../.gitbook/assets/mfa-admin-requirement.png" alt="The organisation MFA requirement toggle and adoption report"><figcaption><p>Ative a exigência para todos os membros e acompanhe a adoção abaixo.</p></figcaption></figure>

Após salvar, a alteração entra em vigor em até um minuto. A partir de então:

* Um membro **com** um segundo fator terá esse fator solicitado após a senha, como de costume.
* Um membro **sem** um segundo fator deverá cadastrar um antes de receber uma sessão.
* Os logins com SSO / sociais não são afetados.

{% hint style="warning" %}
Ativar isso bloqueia os logins com senha para os membros que não têm um segundo fator até que concluam o cadastro. Comunique a mudança à sua equipe e considere ativá-la fora do horário de pico.
{% endhint %}

## Relatório de adoção do MFA

Abaixo do botão de alternância, o painel de **adoção do MFA** mostra o quanto a 2FA é usada na sua organização antes de você exigi-la:

* a **porcentagem de adoção** geral e uma barra de progresso,
* quantos dos seus membros têm a 2FA ativada (por exemplo, *0 de 74 membros*),
* um detalhamento por fator — **Autenticador**, **E-mail** e **Chave de acesso**.

<figure><img src="../../../../.gitbook/assets/mfa-adoption-report.png" alt="The MFA adoption report"><figcaption><p>O relatório de adoção do MFA: porcentagem geral, membros cadastrados e um detalhamento por fator.</p></figcaption></figure>

Use-o para avaliar a prontidão: aumente a adoção primeiro e, em seguida, ative a exigência com menos membros bloqueados na etapa de cadastro.

## O que os membros veem

Um membro que precisa se cadastrar é direcionado para a configuração de 2FA no próximo login e escolhe um método (aplicativo autenticador, código por e-mail ou chave de acesso). As etapas para o usuário final estão descritas em [Autenticação de Dois Fatores (2FA)](../../../../overview-and-basics/two-factor-authentication.md).

## Controles de segurança relacionados

A exigência de MFA para toda a organização complementa as proteções integradas que sempre se aplicam quando um usuário tem a 2FA ativada: códigos de login de uso único, uma proteção contra repetição de TOTP, limites de tentativas por desafio e por conta (uma conta é temporariamente bloqueada após muitas tentativas malsucedidas) e revogação automática dos dispositivos confiáveis quando um membro altera a sua senha.
