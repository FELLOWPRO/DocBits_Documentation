# Privilégios de Administrador

O papel de um administrador é fundamental para gerenciar sistemas de TI, redes e plataformas digitais em uma organização. Um administrador possui permissões e responsabilidades avançadas que permitem controlar diversos aspectos da infraestrutura técnica e garantir que ela funcione de forma eficiente e segura. Veja a seguir algumas das principais responsabilidades de um administrador:

* **Gerenciamento de usuários:** Os administradores gerenciam contas de usuário, direitos de acesso e permissões. Eles criam novas contas de usuário, atribuem as permissões necessárias e gerenciam o controle de acesso para garantir que apenas usuários autorizados possam acessar determinados recursos.
* **Segurança:** Os administradores são responsáveis pela segurança dos sistemas de TI, protegendo-os contra perda de dados e acesso não autorizado.
* **Solução de problemas e suporte:** O administrador é, muitas vezes, o primeiro ponto de contato para questões técnicas. Ele ajuda os usuários a identificar e resolver problemas e garante que o sistema funcione sem falhas.

Além dessas responsabilidades, os administradores também são encarregados de gerenciar configurações sensíveis e garantir que os sistemas atendam aos requisitos de conformidade e às melhores práticas de segurança da informação. Isso inclui gerenciar dados sensíveis, configurar controles de acesso e permissões, além de monitorar e analisar os registros (logs) do sistema para identificar e tratar possíveis riscos de segurança.

## Admin vs System Admin

O DocBits tem duas funções de administrador: **Admin** e **System Admin**. Os nomes parecem semelhantes, mas elas têm finalidades diferentes. Veja a versão simples.

### Admin — uma pessoa que gerencia sua organização

Um **Admin** é uma pessoa real da sua equipe que tem permissão para gerenciar o DocBits. Os Admins podem:

* Abrir todas as áreas das **Configurações** e alterar a forma como sua organização funciona.
* Adicionar novos usuários, editá-los, ativá-los ou desativá-los e decidir quem mais se torna Admin.
* Configurar grupos, permissões, integrações e fluxos de trabalho.

Você pode ter **quantos Admins precisar** e pode conceder ou retirar a função de Admin de qualquer usuário a qualquer momento. A maioria dos administradores da sua equipe é desse tipo.

### System Admin — a conta que o DocBits usa para trabalhar sozinho

Um **System Admin** é **uma conta especial, única por organização**, que o DocBits utiliza para ações que acontecem **automaticamente, sem ninguém clicar em um botão** — por exemplo, quando documentos são importados de um e-mail, exportados para outro sistema ou repassados por um serviço conectado em segundo plano.

Pense nela como a conta "robô" da organização. Quando o sistema faz algo por conta própria, ele o faz **como o System Admin**, de modo que a atividade automática seja fácil de reconhecer e não se confunda com o trabalho dos membros reais da sua equipe.

Um System Admin é especial de três maneiras:

* **Ele também é sempre um Admin.** Escolher System Admin concede automaticamente a essa conta todos os direitos de Admin.
* **Existe apenas um por organização.** Quando já há um System Admin, você não pode marcar outro usuário como System Admin.
* **Ele é definido apenas no momento da criação do usuário.** Você decide isso ao adicionar o usuário. Essa opção **não pode ser ativada ou desativada depois**.

> **Recomendação:** Crie uma conta dedicada para essa finalidade — por exemplo, `system@your-company.com` — e marque-a como o System Admin. Assim, tudo o que o DocBits fizer automaticamente aparecerá claramente como **System Admin** nos seus registros e no histórico de documentos, separado dos seus usuários reais.

### Em resumo

| | Admin | System Admin |
|---|---|---|
| Acesso total para gerenciar a organização | Sim | Sim |
| Quantos você pode ter | Quantos precisar | Apenas um |
| Pode ser alterado após a criação do usuário | Sim, a qualquer momento | Não, definido apenas na criação |
| Usado para ações automáticas, em segundo plano | Não | Sim |
| Sempre tem direitos de Admin | — | Sim |

## Melhores Práticas de Segurança

A segurança é um aspecto essencial de qualquer organização, especialmente quando se trata de gerenciar contas de usuário e direitos de acesso. Veja a seguir algumas melhores práticas para manter um protocolo de gerenciamento de usuários seguro:

* **Atualizações regulares de senha:** Incentive os usuários a atualizar suas senhas regularmente para manter suas contas seguras. Estabeleça políticas de complexidade de senha e exija o uso de senhas fortes que incluam uma combinação de letras, números e caracteres especiais.
* **Monitorar ações dos administradores:** Implemente mecanismos para monitorar as atividades dos administradores e detectar atividades suspeitas ou incomuns. Registre todas as ações dos administradores, incluindo o acesso a dados ou configurações sensíveis, para garantir a responsabilização e identificar possíveis violações de segurança.
* **Limitar o número de administradores:** Reduza ao mínimo o número de administradores e conceda privilégios administrativos apenas a quem realmente precisa deles. Ao limitar o número de administradores, você minimiza o risco de violações de segurança e facilita o gerenciamento e o monitoramento das contas de usuário.
* **Autenticação de dois fatores (2FA):** Implemente a autenticação de dois fatores para as contas de administrador, a fim de aumentar ainda mais a segurança. Isso adiciona uma etapa extra de segurança que garante que, mesmo que uma senha seja comprometida, um invasor não consiga acessar a conta de forma não autorizada.
* **Revisões de segurança regulares:** Realize revisões e auditorias de segurança periódicas para identificar e corrigir possíveis falhas ou vulnerabilidades de segurança. Revise os direitos de acesso e as permissões das contas de usuário para garantir que estejam de acordo com os requisitos atuais e as melhores práticas.
* **Treinamento e conscientização:** Treine regularmente funcionários e administradores sobre as melhores práticas de segurança e sobre a conscientização em relação a ataques de phishing e outras ameaças cibernéticas. Conscientize-os da importância da segurança e incentive-os a relatar atividades suspeitas.

Ao implementar essas melhores práticas, as organizações podem aumentar a segurança do seu protocolo de gerenciamento de usuários e minimizar o risco de violações de segurança e perda de dados. É importante encarar a segurança como um processo contínuo e fazer atualizações e ajustes regulares para acompanhar as ameaças e os requisitos de segurança em constante mudança.
