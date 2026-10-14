# FAQ do Administrador do WatchDog e Solução de Problemas

<figure><img src="../../../.gitbook/assets/watchdog-troubleshooting-infographic.svg" alt="Referência rápida de solução de problemas do WatchDog"><figcaption></figcaption></figure>

Esta documentação ajuda os administradores a entender as mensagens de erro do WatchDog e a solucionar problemas.

**Local na interface:** Settings → Document Processing → WatchDog

---

## 1. Páginas de Configurações do WatchDog (Interface)

### 1.1 Aba General

<figure><img src="../../../.gitbook/assets/watchdog_v2_01.png" alt="Aba General do WatchDog"><figcaption></figcaption></figure>

* **Download:** Baixe o WatchDog.exe mais recente
* **API Key:** Copie o comando de configuração
* **Auto-Update Schedule:** Configure a frequência das atualizações
* **Installation Guide:** Instruções de instalação passo a passo

### 1.2 Aba Configurations

* **Import Configurations:** Defina as pastas monitoradas e os tipos de documento
* **Export Configurations:** Defina os destinos e os métodos de exportação
* **Bulk Copy:** Copie configurações entre suborganizações
* **Import/Export:** Importe/exporte configurações como JSON

> **Importante:** As configurações de exportação agora **exigem um tipo de documento** (`doc_type`). Configurações sem um tipo de documento válido serão rejeitadas.

### 1.3 Aba Status

<figure><img src="../../../.gitbook/assets/watchdog_v2_status.png" alt="Status do serviço WatchDog"><figcaption></figcaption></figure>

* Mostra o status da conexão do WatchDog em tempo real
* **Novos campos:** `last_restart`, `version_first_seen`, `latest_version_checked_at`
* **Informações do sistema:** caminho de instalação, RAM livre, espaço livre em disco

### 1.4 Aba Logs

<figure><img src="../../../.gitbook/assets/watchdog_v2_05.png" alt="Logs do WatchDog"><figcaption></figcaption></figure>

* Mostra todos os eventos do WatchDog vindos do OpenSearch
* Filtrável por tipo de evento, período etc.
* **Tipos de evento:**
  * `FILE_IMPORT_STARTED`: Importação de arquivo iniciada
  * `FILE_IMPORT_COMPLETED`: Importação concluída com sucesso
  * `FILE_IMPORT_FAILED`: Falha na importação
  * `EXPORT_STARTED`: Exportação iniciada
  * `EXPORT_COMPLETED`: Exportação concluída com sucesso
  * `EXPORT_FAILED`: Falha na exportação
  * `FOLDER_VALIDATION_FAILED`: Pasta inacessível
  * `CONFIG_LOADED`: Configuração carregada
  * `SERVICE_RESTART_INITIATED`: Reinício do serviço solicitado
  * `SERVICE_RESTART_COMPLETED`: Serviço reiniciado

### 1.5 Aba XSLT Templates

<figure><img src="../../../.gitbook/assets/watchdog_v2_06.png" alt="Lista de modelos XSLT"><figcaption></figcaption></figure>

* Envie e gerencie modelos de transformação XSLT
* Validação em tempo real com análise de campos
* Vincule modelos às configurações de exportação

---

## 2. Mensagens de Erro de Validação de Pastas

| Erro | Significado | Solução |
| :--- | :--- | :--- |
| `not_found` | A pasta não existe | Crie a pasta ou corrija o caminho |
| `no_read_access` | Sem permissão de leitura | Defina as permissões para a conta de serviço do WatchDog |
| `no_write_access` | Sem permissão de gravação | Conceda direitos de gravação à conta de serviço |
| `not_configured` | Caminho da pasta não configurado | Informe o caminho na configuração |

**Pastas afetadas:**

* **Watch Folder (Importação):** Onde o WatchDog procura novos arquivos
* **Success Folder:** Para onde os arquivos importados com sucesso são movidos
* **Export Folder:** Onde os arquivos XML/PDF exportados são gravados

---

## 3. Mensagens de Erro de Importação

| Erro | Significado | Solução |
| :--- | :--- | :--- |
| `file_not_found` | O arquivo foi excluído antes da importação | Forneça o arquivo novamente |
| `invalid_file_type` | Somente arquivos PDF são suportados | Remova os outros tipos de arquivo |
| `api_not_accessible` | API do DocBits inacessível | Verifique a rede/firewall e a URL da API |
| `api_check_failed` | Falha na verificação de integridade da API | Verifique a API Key e a conexão |
| `upload_failed` | Falha no envio para a API | Verifique a API Key, a rede e o status do servidor |

---

## 4. Mensagens de Erro de Exportação

| Erro | Significado | Solução |
| :--- | :--- | :--- |
| `transformation_error` | Falha na transformação XSLT | Verifique o modelo XSLT e valide a estrutura do XML |
| `folder_error` | Pasta de exportação inacessível | Crie a pasta e verifique as permissões |
| `file_write_error` | Não foi possível gravar o arquivo | Verifique o espaço em disco, as permissões e os bloqueios de arquivo |
| `permission_denied` | Sem permissão de gravação | Defina as permissões da conta de serviço |
| `creation_failed` | Não foi possível criar a pasta | Verifique as permissões da pasta pai |
| `no_config_match` | Nenhuma configuração de exportação correspondente | Crie uma configuração de exportação com o tipo de documento correto |

> **Nota:** As configurações de exportação exigem um `doc_type`. Se você vir `no_config_match`, verifique se existe uma configuração de exportação ativa para o tipo do documento.

---

## 5. Configuração Desativada — Motivos

Quando uma configuração é desativada, um destes motivos é exibido:

| Motivo da desativação | Significado |
| :--- | :--- |
| `Watch folder: not_found` | A pasta de importação não existe |
| `Watch folder: no_read_access` | A pasta de importação não pode ser lida |
| `Export folder: not_found` | A pasta de exportação não existe |
| `Export folder: no_write_access` | A pasta de exportação não permite gravação |
| `Success folder: not_found` | A pasta de sucesso não existe |
| `Success folder: no_write_access` | A pasta de sucesso não permite gravação |

**Reativação automática:** O WatchDog verifica as pastas regularmente (a cada 60 segundos). Assim que a pasta volta a estar acessível, a configuração é reativada automaticamente.

---

## 6. Pasta de Erros (`_error`)

Os arquivos com falha são movidos para a pasta `_error`:

**Local:** `{import_folder}/_error/{error_type}/`

**Formato do arquivo:** `{original_name}_{YYYYMMDD_HHMMSS}.pdf`

**Arquivo auxiliar:** Cada arquivo com falha tem um arquivo `.error` associado com:

```
Error Type: transformation_error
Error Message: XSLT template not found
Timestamp: 2026-03-26 08:30:15
Original File: invoice_001.pdf
Original Path: C:\WatchDog\Import\invoice_001.pdf
```

---

## 7. Heartbeat e Status da Conexão

O WatchDog envia um heartbeat ao DocBits a cada ~10 segundos com informações do sistema:

| Dados enviados | Descrição |
| :--- | :--- |
| Timestamp | Hora atual |
| Version | Versão instalada do WatchDog |
| Last Restart | Hora do último reinício do serviço |
| Auto-Update Enabled | Se a atualização automática está ativa |
| Latest Version | Versão mais recente disponível |
| Installation Path | Onde o WatchDog está instalado |
| Free RAM / Disk | Recursos do sistema disponíveis |

### Status da Conexão

| Status | Significado |
| :--- | :--- |
| ✅ **Online** | O WatchDog está conectado e ativo |
| ⚠️ **Offline** | Nenhum heartbeat há mais de 30 segundos |
| ❌ **Not Installed** | O WatchDog nunca se conectou |

**Erros de heartbeat:**

* `Heartbeat failed - invalid API key` → A API Key é inválida
* `Heartbeat failed: 401` → Falha na autenticação
* `Heartbeat failed: 5xx` → Problema no servidor

---

## 8. Problemas Comuns e Soluções

### Problema: o WatchDog não importa arquivos

1. Verifique se o serviço está em execução: `services.msc` → WatchDog
2. Verifique os logs: Settings → WatchDog → aba Logs
3. Verifique as permissões das pastas para a conta de serviço do WatchDog
4. Teste a conexão com a API: `WatchDog.exe debug` no CMD
5. Verifique se o tipo de arquivo é PDF

### Problema: a exportação não funciona

1. Existe uma configuração de exportação com o tipo de documento correto?
2. O tipo de documento corresponde entre o documento e a configuração?
3. O modelo XSLT está vinculado (para exportação em pasta)?
4. A pasta de exportação permite gravação pela conta de serviço?
5. Para exportações Infor: as credenciais ION estão configuradas corretamente?

### Problema: a configuração está desativada

1. O caminho da pasta existe?
2. Permissões para `NT AUTHORITY\LOCAL SERVICE` ou para a conta de serviço?
3. A unidade de rede está acessível? (Verifique os caminhos UNC)
4. O WatchDog reativará automaticamente quando as pastas voltarem a estar disponíveis

### Problema: a transformação XSLT falha

1. O modelo XSLT é válido? (use a aba XSLT Templates → Validate)
2. O modelo é adequado ao tipo de documento?
3. Verifique a estrutura XML do documento
4. A exportação em pasta V3 usa transformação no lado do servidor — verifique a conectividade com a API

### Problema: a exportação via REST API falha

1. As credenciais ION OAuth estão configuradas na configuração de exportação?
2. O endpoint da API de destino está acessível a partir do servidor do WatchDog?
3. Verifique se o formato do payload corresponde ao esperado pela API de destino
4. Revise a configuração da cadeia de requisições em busca de erros de JSONPath

---

## 9. Comandos de Linha de Comando

```bash
# Configure API connection
WatchDog.exe -api YOUR_API_KEY

# Install Service
WatchDog.exe install

# Start Service
WatchDog.exe start

# Stop Service
WatchDog.exe stop

# Run in debug mode (console output)
WatchDog.exe debug

# Uninstall Service
WatchDog.exe remove

# Show version
WatchDog.exe --version

# List watch folders
WatchDog.exe --list-folders

# Add/remove watch folder
WatchDog.exe --add-folder "C:\Import\Invoices"
WatchDog.exe --remove-folder "C:\Import\Invoices"

# Check Windows service status
sc query WatchDog
```

---

## 10. Arquivos de Log

**Local:** `C:\WatchDog\logs\{module}\`

**Formato do log:**
```
INFO  - 2026-03-26 10:00:00 - module_name - Message - function=func_name - line=42
```

**Nível de log:** DEBUG, INFO, WARNING, ERROR

**Logs remotos:** O WatchDog também envia logs ao DocBits (visíveis na aba Logs) e, opcionalmente, ao serviço de log em nuvem Logtail.
