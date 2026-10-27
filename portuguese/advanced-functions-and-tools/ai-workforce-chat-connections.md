# Ligar AI Workforce ao Teams e ao Discord

Precisa de uma subscrição AI Workforce ativa, permissões para gerir ligações e acesso ao tenant Teams ou servidor Discord previsto. Resolva primeiro qualquer requisito de subscrição apresentado com o administrador.

## Microsoft Teams

1. Abra **AI Workforce → Definições → Integrações**.
2. Escolha **+ → Ligar Teams**. DocBits gera um código e mostra a validade restante.
3. Siga a instrução junto do código no ambiente Teams previsto. Mantenha-o confidencial e conclua a associação antes de expirar.
4. Aguarde a confirmação. Verifique nome e modo de bot partilhado ou personalizado na lista.
5. Ative uma ligação inativa quando deva receber trabalho. Guardada e ativa são estados diferentes.
6. Envie uma solicitação de teste inofensiva a partir do contexto Teams previsto. Verifique missão, origem e organização em DocBits e complete as aprovações humanas necessárias na caixa de entrada.

Para um bot empresarial, escolha a opção personalizada e introduza nome, ID do tenant, ID e segredo da aplicação. Os segredos pertencem ao formulário de credenciais, fora de prompts e capturas.

## Discord

1. Em **Integrações → +**, escolha a ligação Discord.
2. Se disponível, adicione o bot ao servidor correto com um administrador autorizado.
3. Introduza um nome reconhecível e o **Guild ID** correto. Identifica o servidor, não o canal.
4. Crie a ligação, verifique-a e ative-a se necessário.
5. Envie um teste inofensivo e verifique missão, origem e organização resultantes.

## Diagnóstico

Se o código Teams expirar, gere outro e siga a nova instrução. Sem trabalho recebido, verifique ativação, tenant/servidor, acesso do bot e erros. Uma ligação estabelecida não comprova uma missão concluída.

Consulte [AI Workforce](ai_workforce/README.md) para missões, permissões e aprovações. Estas ligações são independentes da importação de email e do início de sessão Microsoft.
