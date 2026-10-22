# Testes de importação e tratamento de e-mails

## Finalidade

Estes testes verificam o tratamento da importação de e-mails: envio, receção, movimentação para pastas específicas, verificação do estado lido ou não lido, importação para o sistema e limpeza posterior.

## Passos do teste

1. **Preparação:**
   * **Obter as configurações do ambiente:** carregar os dados necessários, como a informação do servidor de e-mail e as credenciais, a partir de variáveis de ambiente.
   * **Cifrar a palavra-passe do e-mail:** cifrar a palavra-passe de forma segura para a sua utilização.
2. **Envio e gestão de e-mails:**
   * **Enviar um e-mail:** utilizar uma função SMTP para enviar um e-mail com assunto e anexo específicos.
   * **Mover o e-mail:** utilizar funções IMAP para o mover para uma pasta de destino.
   * **Listar pastas:** confirmar que a pasta de destino existe.
   * **Eliminar o e-mail:** limpar os dados, eliminando o e-mail da pasta.
   * **Verificar o estado do e-mail:** confirmar se está marcado como lido ou não lido.
3.  **Sequência de teste**

    **Preparação inicial:**

    * **Verificar a ligação:** confirmar a ligação ao servidor de e-mail e obter o identificador da ligação.
    * **Testar o início de sessão:** confirmar que é possível iniciar sessão com as credenciais guardadas.
    * **Verificar a pasta:** confirmar que a pasta de destino existe no servidor de e-mail.

    **Operações de e-mail:**

    * **Enviar um e-mail de teste:** enviar um e-mail com um assunto específico.
    * **Obter o identificador do e-mail:** obter o identificador do e-mail enviado a partir da caixa de entrada.
    * **Mover o e-mail:** mover o e-mail da caixa de entrada para a pasta de destino.
    * **Verificar o estado do e-mail:** confirmar que o e-mail na pasta de destino está marcado como não lido.

    **Importação de e-mails:**

    * **Obter o e-mail:** importar o e-mail da pasta de destino para o sistema.
    * **Verificar o e-mail importado:** confirmar que foi obtido e registado corretamente.

    **Verificação dos registos:**

    * **Verificar o registo de importação:** confirmar que contém o assunto do e-mail enviado.

    **Limpeza:**

    * **Eliminar o documento importado:** remover o documento importado do e-mail.
    * **Eliminar o e-mail:** eliminar das pastas o e-mail enviado e movido para limpar os dados.

## Explicação detalhada de cada teste

* **Preparação e inicialização:**
  * **Inicializar os dados partilhados:** preparar os dados partilhados dos testes.
* **Testes de ligação ao e-mail:**
  * **Obter o identificador da ligação:** verificar se é possível ligar ao servidor de e-mail e obter um identificador para a ligação.
  * **Verificar o início de sessão:** confirmar que o início de sessão no servidor de e-mail funciona corretamente.
* **Testes de verificação de pastas:**
  * **Verificar a pasta de destino:** confirmar que existe no servidor de e-mail.
  * **Verificar a listagem de pastas:** confirmar que a lista devolvida pelo servidor corresponde ao esperado.
* **Envio de e-mails e obtenção de identificadores:**
  * **Enviar um e-mail:** enviar um e-mail de teste com assunto e anexo específicos.
  * **Obter o identificador do e-mail:** obter o identificador único do e-mail enviado a partir da caixa de entrada.
* **Movimentação de e-mails e verificação do estado:**
  * **Mover o e-mail para a pasta:** mover o e-mail de teste da caixa de entrada para a pasta de destino.
  * **Verificar o estado não lido:** confirmar que o e-mail fica marcado como não lido depois de ser movido.
* **Obtenção de e-mails e validação da resposta:**
  * **Obter o e-mail da pasta:** importar o e-mail da pasta de destino para o sistema.
  * **Validar o e-mail obtido:** confirmar que o e-mail está presente na resposta.
* **Verificação do registo de importação:**
  * **Obter o registo de importação:** consultar o registo dos e-mails importados.
  * **Verificar o assunto no registo:** confirmar que o assunto do e-mail de teste consta do registo de importação.
* **Limpeza:**
  * **Eliminar o documento importado:** remover o documento importado do e-mail.
  * **Eliminar o e-mail:** eliminar o e-mail de teste da caixa de entrada e da pasta de destino para limpar os dados.

\


