# Configurações de importação por FTP

## Colunas

* `id`: interno
* `org_id`: ID da organização
* `sub_org_id`: interno
* `server_url`: interno
* `username`: interno
* `password`: interno
* `is_active`: booleano
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `deleted_on`: timestamp com fuso horário
* `port`: inteiro
* `default_directory`: interno
* `ftp_type`: interno
* `token`: interno
* `file_name_matching_patterns`: interno
* `last_mtime`: interno
* `auth_failed_count`: inteiro
* `auth_message`: texto
* `ignore_certificate`: booleano
* `move_after_import`: booleano
* `destination_directory`: interno
* `import_directory`: interno
* `include_subfolder_content`: booleano

## Análise e descrição

```markdown
# Documentação da tabela de configurações de importação por FTP

## Introdução

A tabela `public.ftp_import_configurations` foi projetada para armazenar os detalhes de configuração dos processos de importação por FTP. Essa tabela inclui as informações necessárias para se conectar a servidores FTP, gerenciar a autenticação e tratar as importações de arquivos. Ela oferece suporte aos protocolos FTP e SFTP e inclui campos para os detalhes do servidor FTP, as credenciais de autenticação e as configurações operacionais, como mover ou não os arquivos após a importação e incluir ou não o conteúdo de subpastas.

## Descrição das colunas

### id
- **Significado**: identificador único de cada registro de configuração de importação por FTP.
- **Função**: chave primária.
- **Conteúdo típico**: formato UUID, por exemplo `9862d8c6-bb61-4373-9616-d5f8c125eeb8`.

### org_id
- **Significado**: identificador da organização associada a esta configuração.
- **Função**: chave estrangeira.
- **Conteúdo típico**: formato UUID.

### sub_org_id
- **Significado**: identificador de uma suborganização, se aplicável.
- **Função**: chave estrangeira.
- **Conteúdo típico**: formato UUID ou `null` se não for aplicável.

### server_url
- **Significado**: a URL ou o endereço IP do servidor FTP.
- **Função**: campo descritivo.
- **Conteúdo típico**: nome de domínio ou endereço IP, por exemplo `sftp.it.doxee.com`.

### username
- **Significado**: nome de usuário usado para a autenticação no servidor FTP.
- **Função**: campo descritivo.
- **Conteúdo típico**: nome de usuário em texto simples.

### password
- **Significado**: senha usada para a autenticação no servidor FTP.
- **Função**: campo descritivo.
- **Conteúdo típico**: string de senha criptografada.

### is_active
- **Significado**: indica se a configuração está ativa no momento.
- **Função**: indicador de status.
- **Conteúdo típico**: `True` ou `False`.

### created_by
- **Significado**: identificador do usuário que criou a configuração.
- **Função**: chave estrangeira.
- **Conteúdo típico**: número inteiro que representa o ID do usuário.

### created_on
- **Significado**: timestamp de quando a configuração foi criada.
- **Função**: campo de auditoria.
- **Conteúdo típico**: data e hora com informações de fuso horário.

### last_modified_on
- **Significado**: timestamp da última modificação da configuração.
- **Função**: campo de auditoria.
- **Conteúdo típico**: data e hora com informações de fuso horário.

### is_deleted
- **Significado**: indica se a configuração foi marcada como excluída.
- **Função**: indicador de status.
- **Conteúdo típico**: `True` ou `False`.

### deleted_on
- **Significado**: timestamp de quando a configuração foi marcada como excluída.
- **Função**: campo de auditoria.
- **Conteúdo típico**: data e hora com informações de fuso horário ou uma data padrão para registros não excluídos.

### port
- **Significado**: número da porta usada para se conectar ao servidor FTP.
- **Função**: campo descritivo.
- **Conteúdo típico**: número inteiro, por exemplo `22` para SFTP.

### default_directory
- **Significado**: o caminho do diretório padrão no servidor FTP.
- **Função**: campo descritivo.
- **Conteúdo típico**: string com o caminho do diretório.

### ftp_type
- **Significado**: tipo de protocolo FTP usado (por exemplo, FTP, SFTP).
- **Função**: campo descritivo.
- **Conteúdo típico**: `FTP` ou `SFTP`.

### token
- **Significado**: token de segurança para autenticação ou identificação adicional.
- **Função**: campo descritivo.
- **Conteúdo típico**: string criptografada ou codificada.

### file_name_matching_patterns
- **Significado**: padrões usados para fazer a correspondência dos nomes de arquivos a serem importados.
- **Função**: campo descritivo.
- **Conteúdo típico**: strings de padrão ou `null`.

### last_mtime
- **Significado**: horário da última modificação dos arquivos, usado para filtrar as importações.
- **Função**: campo descritivo.
- **Conteúdo típico**: string que representa um timestamp ou `null`.

### auth_failed_count
- **Significado**: contador de tentativas de autenticação com falha.
- **Função**: campo descritivo.
- **Conteúdo típico**: número inteiro, por exemplo `0` ou `5`.

### auth_message
- **Significado**: mensagem que descreve o resultado da última tentativa de autenticação.
- **Função**: campo descritivo.
- **Conteúdo típico**: mensagem de texto ou `null`.

### ignore_certificate
- **Significado**: indica se a validação do certificado SSL deve ser ignorada.
- **Função**: indicador de status.
- **Conteúdo típico**: `True` ou `False`.

### move_after_import
- **Significado**: indica se os arquivos devem ser movidos após a conclusão da importação.
- **Função**: indicador de status.
- **Conteúdo típico**: `True` ou `False`.

### destination_directory
- **Significado**: caminho do diretório para onde os arquivos devem ser movidos após a importação.
- **Função**: campo descritivo.
- **Conteúdo típico**: string com o caminho do diretório ou `null`.

### import_directory
- **Significado**: caminho do diretório do qual os arquivos são importados.
- **Função**: campo descritivo.
- **Conteúdo típico**: string com o caminho do diretório ou `null`.

### include_subfolder_content
- **Significado**: indica se o conteúdo das subpastas deve ser incluído na importação.
- **Função**: indicador de status.
- **Conteúdo típico**: `True` ou `False`.
```

Esta documentação oferece uma compreensão abrangente de cada coluna da tabela `public.ftp_import_configurations`, explicando sua finalidade, sua função e seu conteúdo típico, com base nos dados fornecidos e nos nomes das colunas.
