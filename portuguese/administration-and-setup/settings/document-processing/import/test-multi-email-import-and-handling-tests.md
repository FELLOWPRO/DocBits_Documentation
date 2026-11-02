# Testes de importação e tratamento de e-mails

## O que é testado?

Estes testes verificam se o sistema de importação de e-mails funciona corretamente. Os principais objetivos são:

1. **Enviar e-mails** com anexos.
2. **Receber e mover e-mails** para pastas específicas.
3. **Verificar se os e-mails estão lidos ou não lidos.**
4. **Importar e-mails para o sistema.**
5. **Limpar os dados**, eliminando posteriormente os e-mails e os documentos importados.

## Passos envolvidos

1. **Preparação:**
   * **Obter as configurações do ambiente:** carregar os dados do servidor de e-mail e as credenciais a partir de variáveis de ambiente.
   * **Cifrar a palavra-passe do e-mail:** cifrar a palavra-passe de forma segura.
2. **Enviar e gerir e-mails:**
   * **Enviar e-mails:** utilizar uma função SMTP para enviar e-mails com assuntos e anexos específicos.
   * **Mover e-mails:** utilizar funções IMAP para mover os e-mails para a pasta de destino.
   * **Listar pastas:** verificar se a pasta de destino existe.
   * **Eliminar e-mails:** limpar os dados, eliminando os e-mails das pastas.
   * **Verificar o estado dos e-mails:** confirmar se estão marcados como lidos ou não lidos.
3.  **Sequência de teste**

    **Preparação inicial:**

    * **Verificar a ligação:** confirmar a ligação ao servidor de e-mail e obter o identificador da ligação.
    * **Testar o início de sessão:** confirmar que é possível iniciar sessão com as credenciais guardadas.
    * **Verificar a pasta:** confirmar que a pasta de destino existe no servidor de e-mail.

    **Operações de e-mail:**

    * **Enviar e-mails de teste:** enviar três e-mails com assuntos únicos.
    * **Obter os identificadores dos e-mails:** obter os identificadores dos e-mails enviados a partir da caixa de entrada.
    * **Mover e-mails:** mover os e-mails da caixa de entrada para a pasta de destino.
    * **Verificar o estado dos e-mails:** confirmar que os e-mails na pasta de destino estão marcados como não lidos.

    **Importação de e-mails:**

    * **Obter e-mails:** importar os e-mails da pasta de destino para o sistema.
    * **Verificar os e-mails importados:** confirmar que foram obtidos e registados corretamente.

    **Verificação dos registos:**

    * **Verificar os registos de importação:** confirmar que contêm os assuntos dos e-mails enviados.

    **Limpeza:**

    * **Eliminar os documentos importados:** remover os documentos importados dos e-mails.
    * **Eliminar e-mails:** limpar os dados, eliminando das pastas os e-mails enviados e movidos.

### Explicação detalhada de cada teste

* **Preparação e inicialização:**
  * **Inicializar os dados partilhados:** preparar os dados partilhados dos testes.
* **Testes de ligação ao e-mail:**
  * **Obter o identificador da ligação:** verificar se é possível ligar ao servidor de e-mail e obter um identificador para a ligação.
  * **Verificar o início de sessão:** confirmar que o início de sessão no servidor de e-mail funciona corretamente.
* **Testes de verificação de pastas:**
  * **Verificar a pasta de destino:** confirmar que existe no servidor de e-mail.
  * **Verificar a listagem de pastas:** confirmar que a lista devolvida pelo servidor corresponde ao esperado.
* **Envio de e-mails e obtenção de identificadores:**
  * **Enviar e-mails:** enviar três e-mails de teste com assuntos e anexos específicos.
  * **Obter os identificadores dos e-mails:** obter os identificadores únicos dos e-mails enviados a partir da caixa de entrada.
* **Movimentação de e-mails e verificação do estado:**
  * **Mover e-mails para a pasta:** mover os e-mails de teste da caixa de entrada para a pasta de destino.
  * **Verificar o estado não lido:** confirmar que os e-mails ficam marcados como não lidos depois de serem movidos.
* **Obtenção de e-mails e validação da resposta:**
  * **Obter e-mails da pasta:** importar os e-mails da pasta de destino para o sistema.
  * **Validar os e-mails obtidos:** confirmar que correspondem aos e-mails enviados.
* **Verificação do registo de importação:**
  * **Obter o registo de importação:** consultar o registo dos e-mails importados.
  * **Verificar os assuntos no registo:** confirmar que os assuntos dos e-mails de teste constam do registo de importação.
* **Limpeza:**
  * **Eliminar os documentos importados:** remover os documentos importados dos e-mails.
  * **Eliminar e-mails:** eliminar os e-mails de teste da caixa de entrada e da pasta de destino para limpar os dados.

\


