# Configuração do Identity Service Provider

Configurar o Identity Service Provider (IdP) para integrar com o DocBits requer algumas etapas específicas. Aqui está um guia para fazer isso:

<figure><img src="../../../../.gitbook/assets/image (83).png" alt=""><figcaption></figcaption></figure>

**Acessando a interface de configuração do IdP**

* Faça login no seu Identity Service Provider (IdP) como administrador.
* Navegue até as configurações ou a interface de configuração dedicada ao gerenciamento de integrações SAML.

**Inserindo o Tenant ID:**

* Procure a seção que permite a configuração de novas integrações SAML.
* Insira o tenant ID do DocBits. Este ID identifica a sua conta do DocBits para o IdP e permite a comunicação segura entre os dois sistemas.

**Importando os arquivos necessários:**

* O DocBits geralmente requer o download de metadados ou a adição de detalhes de configuração específicos. Consulte a documentação do seu IdP para ver quais etapas são necessárias.
* Baixe o arquivo de metadados do DocBits ou importe-o no menu de configuração do seu IdP. Como alternativa, você pode inserir manualmente os detalhes de configuração necessários, dependendo do que o seu IdP suporta.

**Configurar as definições de integração:**

* Certifique-se de que as definições de integração, como a SSO URL, o Entity ID e o certificado SAML, estejam corretas.
* Verifique se a URL de Single Log-Out (SLO) e os demais parâmetros necessários estão configurados corretamente. Eles são essenciais para uma autenticação e um logout tranquilos via SAML.

**Verificar a configuração:**

* Reserve um tempo para garantir que todas as informações inseridas estejam corretas e que não haja erros de digitação ou configurações incorretas.
* Execute testes para garantir que os usuários consigam fazer login no DocBits via SAML com sucesso e que o Single Log-Out esteja funcionando corretamente.

**Considerações de segurança:**

* Certifique-se de que todos os arquivos transferidos e os detalhes de configuração sejam tratados de forma segura para evitar vazamentos de dados ou acessos não autorizados.
* Proteja informações sensíveis, como certificados SAML e credenciais, contra acesso não autorizado e armazene-as em um local seguro.