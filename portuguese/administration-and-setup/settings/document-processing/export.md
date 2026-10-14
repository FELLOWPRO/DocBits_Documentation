# Exportação

## Visão Geral

A página de Exportação exibe todas as configurações de exportação configuradas, incluindo se estão ativas ou inativas. A partir daqui, os usuários podem:

* Visualizar e gerenciar configurações de exportação existentes
* Criar novas conexões de exportação (ex.: para **Infor**, **Infor & IDM**, **Webhook** ou **SFTP**)
* Editar ou excluir configurações de exportação existentes

## Onde encontrar

Você pode encontrá-lo em: **Configurações** → **Processamento de Documentos** → **Exportação**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_settings_menu_access.png)

## **Usando a página de Exportação**

Quando você abre a página de Exportação, verá uma lista de todas as configurações de exportação existentes.

Cada linha na lista mostra:

* **Indicador de status**
  * **Verde** significa que a exportação está ativa
  * **Vermelho** significa que a exportação está desativada
* **Nome** – o nome da configuração de exportação
* **Tipo de documento** – o tipo de documento para o qual a exportação está configurada
* **Sub-organização** – se a exportação está limitada a uma sub-organização específica
* **Método de exportação** – para onde o documento será enviado (ex.: Infor, IDM, SFTP)
* **Ações** – botões para **editar, excluir** ou **ativar/desativar** a configuração

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_list_view.png)

#### **Regras importantes para configuração de exportação**

Para cada **tipo de documento** **dentro de uma determinada organização ou sub-organização**, aplicam-se as seguintes regras:

* Você pode ter **apenas uma exportação Infor ativa**
* Você pode ter **apenas uma exportação não-Infor ativa** (ex.: Webhook, SFTP)

No entanto, é possível ter:

* **Uma exportação Infor ativa** _e_ **uma exportação não-Infor ativa** ao mesmo tempo para o mesmo tipo de documento
* **Diferentes configurações de exportação para diferentes sub-organizações** — por exemplo, uma exportação Infor para Sub-Org A e outra exportação Infor para Sub-Org B

## **Criando uma nova exportação**

Para criar uma nova exportação:

1. Clique no botão **"Novo"**. ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_create_new_button.png)
2. Selecione o **Tipo de Exportação** que deseja configurar (ex.: Infor, IDM, SFTP).
3. Preencha os campos obrigatórios com base no tipo de exportação.
4. Salve a configuração.

## Opções de exportação

#### Webhook

<details>

<summary>Webhook</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_webhook_configuration.png)

**Descrição dos campos**

* **Title** O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organization** _(opcional)_ Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado vazio: aplica-se à organização principal.
  * Se selecionado: a exportação será aplicada apenas à sub-organização escolhida.
* **Document Type** Menu suspenso listando todos os tipos de documentos disponíveis. Isso determina a qual tipo de documento esta configuração de exportação se aplica.
* **Export URL** A URL de destino onde o documento deve ser exportado.

</details>

#### SFTP

<details>

<summary>SFTP</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_sftp_configuration.png)

**Descrição dos campos**

* **Title** O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organization** _(opcional)_ Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado vazio: aplica-se à organização principal.
  * Se selecionado: a exportação será aplicada apenas à sub-organização escolhida.
* **Document Type** Menu suspenso listando todos os tipos de documentos disponíveis. Isso determina a qual tipo de documento esta configuração de exportação se aplica.
* **Username** O nome de usuário usado para autenticar no servidor SFTP.
* **Password** A senha correspondente para a conta SFTP. Certifique-se de que a conta tenha acesso de gravação à pasta especificada.
* **Server URL** O nome do host ou endereço IP do servidor SFTP de destino.
* **Port** A porta usada para conectar ao servidor SFTP.
* **Folder** O caminho no servidor SFTP onde os documentos devem ser carregados (ex.: `/incoming/invoices/`). Deve existir e ser gravável.
*   **XSLT File (Opcional)**

    O **arquivo XSLT** permite a transformação do formato de exportação padrão do DocBits.

    * **Quando usar:** Apenas se o sistema receptor requer uma estrutura diferente ou formatação específica que difere do padrão do DocBits.
    * **Deixe vazio** se o formato de exportação padrão atende aos requisitos.



**Configurações avançadas:**

* **Filename Export Mode** Especifica se o arquivo exportado mantém seu nome de arquivo original ou é renomeado usando o ID do documento DocBits.
* **Include Document History** Quando habilitado, o arquivo exportado incluirá o histórico do documento baseado nos logs disponíveis no painel.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_sftp_2.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_sftp_3.png)

</details>

#### Exportação Infor para SFTP

<details>

<summary>Exportação Infor para SFTP</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_sftp_configuration.png)

**Descrição dos campos**

* **Title** O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organization** _(opcional)_ Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado vazio: aplica-se à organização principal.
  * Se selecionado: a exportação será aplicada apenas à sub-organização escolhida.
* **Document Type** Menu suspenso listando todos os tipos de documentos disponíveis. Isso determina a qual tipo de documento esta configuração de exportação se aplica.
* **IDM Mapping File** Selecione um arquivo de mapeamento do gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Guia de Mapeamento IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **BOD Mapping File** Selecione um arquivo de mapeamento do gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Guia de Mapeamento BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Folder** O caminho no servidor SFTP onde os documentos devem ser carregados (ex.: `/incoming/invoices/`). Deve existir e ser gravável.

</details>

#### **SMB**

<details>

<summary>SMB</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_smb_configuration.png)

**Descrição dos campos**

* **Title** O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organization** _(opcional)_ Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado vazio: aplica-se à organização principal.
  * Se selecionado: a exportação será aplicada apenas à sub-organização escolhida.
* **Document Type** Menu suspenso listando todos os tipos de documentos disponíveis. Isso determina a qual tipo de documento esta configuração de exportação se aplica.
* **Username** O nome de usuário usado para conectar ao compartilhamento SMB.
* **Password** A senha correspondente para autenticação SMB.
* **Server URL** O endereço do servidor SMB.
* **Port** Número da porta usado para acessar o compartilhamento SMB.
* **Folder** O caminho da pasta dentro do compartilhamento SMB onde os documentos devem ser salvos (ex.: `/incoming/invoices/`). Deve existir e ser gravável.
*   **JPL Mapping File (Opcional)**

    O **arquivo JPL** é usado para definir uma transformação dos dados exportados antes de serem gravados no compartilhamento SMB.

    * **Quando usar:** Apenas quando os dados do documento exportado precisam ser ajustados para corresponder à formatação externa ou expectativas do sistema.
    * **Deixe vazio** se nenhuma transformação for necessária.

</details>

#### **Infor IDM**

<details>

<summary>Infor IDM</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_configuration.png)

**Descrição dos campos**

* **Title** O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organization** _(opcional)_ Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado vazio: aplica-se à organização principal.
  * Se selecionado: a exportação será aplicada apenas à sub-organização escolhida.
* **Document Type** Menu suspenso listando todos os tipos de documentos disponíveis. Isso determina a qual tipo de documento esta configuração de exportação se aplica.
* **ION Mapping File** Selecione um arquivo de mapeamento do gerenciador de arquivos.
* **IDM Mapping File** Selecione um arquivo de mapeamento do gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Guia de Mapeamento IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **Cloud / On-Prem Toggle** Um interruptor para indicar o tipo de implantação do Infor:
  * **Cloud**: Selecione isso se você for um cliente Infor CloudSuite.
  * **On-Prem**: Selecione isso se o Infor for auto-hospedado.

</details>

#### **Infor ION**

<details>

<summary>Infor ION</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_ion_configuration.png)

**Descrição dos campos**

* **Title** O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organization** _(opcional)_ Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado vazio: aplica-se à organização principal.
  * Se selecionado: a exportação será aplicada apenas à sub-organização escolhida.
* **Document Type** Menu suspenso listando todos os tipos de documentos disponíveis. Isso determina a qual tipo de documento esta configuração de exportação se aplica.
* **ION Mapping File** Selecione um arquivo de mapeamento do gerenciador de arquivos.
* **BOD Mapping File** Selecione um arquivo de mapeamento do gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Guia de Mapeamento BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Cloud / On-Prem Toggle** Um interruptor para indicar o tipo de implantação do Infor:
  * **Cloud**: Selecione isso se você for um cliente Infor CloudSuite.
  * **On-Prem**: Selecione isso se o Infor for auto-hospedado.

</details>

#### Infor IDM + ION BOD

<details>

<summary>Infor IDM + ION BOD</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_ion_bod_configuration.png)

**Descrição dos campos**

* **Title** O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organization** _(opcional)_ Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado vazio: aplica-se à organização principal.
  * Se selecionado: a exportação será aplicada apenas à sub-organização escolhida.
* **Document Type** Menu suspenso listando todos os tipos de documentos disponíveis. Isso determina a qual tipo de documento esta configuração de exportação se aplica.
* **ION Mapping File** Selecione um arquivo de mapeamento do gerenciador de arquivos.
* **IDM Mapping File** Selecione um arquivo de mapeamento do gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Guia de Mapeamento IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **BOD Mapping File** Selecione um arquivo de mapeamento do gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Guia de Mapeamento BOD](../../../infor-integration-and-configuration/exporting-to-infor/creating-a-bod-mapping-file.md)
* **Cloud / On-Prem Toggle** Um interruptor para indicar o tipo de implantação do Infor:
  * **Cloud**: Selecione isso se você for um cliente Infor CloudSuite.
  * **On-Prem**: Selecione isso se o Infor for auto-hospedado.

</details>

### Para clientes Infor CloudSuite

#### Infor IDM + LN

<details>

<summary>Infor IDM + LN</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_ln_configuration.png)

**Descrição dos campos**

* **Title** O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organization** _(opcional)_ Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado vazio: aplica-se à organização principal.
  * Se selecionado: a exportação será aplicada apenas à sub-organização escolhida.
* **Document Type** Menu suspenso listando todos os tipos de documentos disponíveis. Isso determina a qual tipo de documento esta configuração de exportação se aplica.
* **ION Mapping File** Selecione um arquivo de mapeamento do gerenciador de arquivos.
* **IDM Mapping File** Selecione um arquivo de mapeamento do gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Guia de Mapeamento IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **LN Mapping File** Selecione um arquivo de mapeamento do gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Exemplo de Mapeamento LN](../../../infor-integration-and-configuration/exporting-to-infor/ln/example-export-ln/)

</details>

#### Infor IDM + M3

<details>

<summary>Infor IDM + M3</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_m3_configuration.png)

**Descrição dos campos**

* **Title** O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organization** _(opcional)_ Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado vazio: aplica-se à organização principal.
  * Se selecionado: a exportação será aplicada apenas à sub-organização escolhida.
* **Document Type** Menu suspenso listando todos os tipos de documentos disponíveis. Isso determina a qual tipo de documento esta configuração de exportação se aplica.
* **ION Mapping File** Selecione um arquivo de mapeamento do gerenciador de arquivos.
* **IDM Mapping File** Selecione um arquivo de mapeamento do gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Guia de Mapeamento IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **M3 Mapping File** Selecione um arquivo de mapeamento do gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Exemplo de Mapeamento M3](../../../infor-integration-and-configuration/exporting-to-infor/m3/example-export-m3.md)

</details>

#### Infor IDM + M3 (toml)

<details>

<summary>Infor IDM + M3 (toml)</summary>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_infor_idm_m3_toml_configuration.png)

**Descrição dos campos**

* **Title** O nome da configuração de exportação. Isso aparecerá na lista de exportações.
* **Sub-Organization** _(opcional)_ Um menu suspenso com todas as sub-organizações disponíveis.
  * Se deixado vazio: aplica-se à organização principal.
  * Se selecionado: a exportação será aplicada apenas à sub-organização escolhida.
* **Document Type** Menu suspenso listando todos os tipos de documentos disponíveis. Isso determina a qual tipo de documento esta configuração de exportação se aplica.
* **ION Mapping File** Selecione um arquivo de mapeamento do gerenciador de arquivos.
* **IDM Mapping File** Selecione um arquivo de mapeamento do gerenciador de arquivos. [Precisa de ajuda para criar um? Veja o Guia de Mapeamento IDM](../../../infor-integration-and-configuration/exporting-to-infor/creating-an-idm-mapping-file.md)
* **M3 toml Mapping File** Selecione um arquivo de mapeamento do gerenciador de arquivos ou use a opção selecionar Toml para usar um toml criado com o gerenciador de regras. [Precisa de ajuda para criar um? Veja o Guia do Gerenciador de Regras](rule-manager/)

</details>
