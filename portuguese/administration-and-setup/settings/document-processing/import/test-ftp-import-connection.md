# Teste de ligação de importação FTP

#### Finalidade

Estes testes verificam o funcionamento da importação FTP: adicionar uma ligação, testá-la, ativá-la ou desativá-la e limpar os dados no final.



{% embed url="https://grafana.polydocs.io/d-solo/b6ad3a9c-260c-46a3-9ade-47691e743d4d/docbits?from=1715746603760&orgId=1&panelId=84&refresh=1m&to=1715768203760" %}

## Cenários de teste

1. **Preparação:**
   * **Variáveis de ambiente:** carregar os dados necessários, como a informação do servidor FTP e as credenciais, a partir de variáveis de ambiente.
2.  **Testes de ligação FTP:**

    **Adicionar uma ligação:**

    * **Teste de adição de uma ligação de importação FTP (`test_add_new_ftp_import_connection`):**
      * Adicionar uma ligação de importação FTP com as credenciais e os dados do servidor fornecidos.
      * **Resultado esperado:** a ligação é adicionada com êxito.

    **Desativar a ligação:**

    * **Teste de desativação da ligação de importação FTP (`test_deactivate_ftp_import_connection`):**
      * Desativar a ligação de importação FTP acabada de adicionar.
      * **Resultado esperado:** a ligação é desativada com êxito.

    **Testar a ligação:**

    * **Teste da ligação FTP (`test_test_ftp_connection`):**
      * Testar se a ligação de importação consegue estabelecer uma ligação ao servidor FTP.
      * **Resultado esperado:** o teste da ligação é concluído com êxito.

    **Verificar a ligação na lista:**

    * **Teste de presença da ligação FTP na lista (`test_check_ftp_connection_in_list`):**
      * Verificar se a ligação de importação FTP adicionada está presente na lista de ligações.
      * **Resultado esperado:** a ligação é encontrada na lista.

    **Verificar a desativação da ligação:**

    * **Teste de ligação FTP desativada (`test_check_ftp_connection_deactivated`):**
      * Verificar se a ligação de importação FTP está marcada como inativa na lista.
      * **Resultado esperado:** a ligação está inativa.

    **Adicionar uma pasta de teste:**

    * **Teste de adição de pasta de teste à ligação (`test_add_test_folder_to_connection`):**
      * Adicionar um diretório padrão (pasta de teste) à ligação de importação FTP.
      * **Resultado esperado:** o diretório padrão é adicionado com êxito.

    **Reativar a ligação:**

    * **Teste de reativação da ligação de importação FTP (`test_reactivate_ftp_import_connection`):**
      * Reativar a ligação de importação FTP anteriormente desativada.
      * **Resultado esperado:** a ligação é reativada com êxito.

    **Verificar a reativação da ligação:**

    * **Teste de ligação FTP reativada (`test_check_ftp_connection_reactivated`):**
      * Verificar se a ligação de importação FTP está marcada como ativa na lista.
      * **Resultado esperado:** a ligação está ativa.

    **Limpeza:**

    * **Teste de limpeza da importação FTP (`test_cleanup_ftp_import`):**
      * Eliminar a ligação de importação FTP para limpar os dados após os testes.
      * **Resultado esperado:** a ligação é eliminada com êxito.

## Explicação detalhada de cada teste

* **Preparação e inicialização:**
  * **Inicializar os dados partilhados:** preparar os dados partilhados dos testes.
* **Testes de ligação FTP:**
  * **Adicionar uma ligação:** adicionar uma ligação de importação FTP com as credenciais e os dados do servidor fornecidos.
  * **Desativar a ligação:** desativar a ligação de importação FTP adicionada.
  * **Testar a ligação:** verificar se a ligação de importação consegue estabelecer uma ligação ao servidor FTP.
  * **Verificar a ligação na lista:** confirmar que a nova ligação de importação FTP está presente na lista de ligações.
  * **Verificar a desativação:** confirmar que a ligação de importação FTP está marcada como inativa na lista.
  * **Adicionar uma pasta de teste:** adicionar um diretório padrão (pasta de teste) à ligação de importação FTP.
  * **Reativar a ligação:** reativar a ligação de importação FTP anteriormente desativada.
  * **Verificar a reativação:** confirmar que a ligação de importação FTP está marcada como ativa na lista.
  * **Limpeza:** eliminar a ligação de importação FTP após os testes.

\


