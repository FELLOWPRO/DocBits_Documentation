# Modelos de E-Mail

## **Visão Geral**

Os Modelos de E-mail permitem personalizar notificações de e-mail automatizadas enviadas pelo DocBits. Os modelos podem incluir campos dinâmicos (por exemplo, `{{FieldID}}`), imagens e formatação HTML.

## **Acessando Modelos de E-mail**

1.  Navegue até: **Configurações → Configurações Globais → Modelos de E-mail**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWzjaI1Jinpw0PQHCuwM0%252Fimage.png%3Falt%3Dmedia%26token%3D21f7af41-6ebe-4e25-952f-9ae0b11cade2\&width=768\&dpr=4\&quality=100\&sign=ae789081\&sv=2)
2. O painel exibe todos os modelos com:
   * **Nome**
   * **Assunto**
   * Data de **Última Modificação**
   * **Ações** (Editar ou Excluir).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FENN4zipGg75mpi2OooPP%252Fimage.png%3Falt%3Dmedia%26token%3Ddff6d8a8-e5b3-4e52-bee1-e311daba7b64\&width=768\&dpr=4\&quality=100\&sign=4202a84f\&sv=2)

## **Criando um Novo Modelo**

### **1 Configuração Básica**

* Clique em **Novo**.
* Preencha os campos à direita:
  * **Nome**: Identificador do modelo (por exemplo, "Erro no Documento").
  * **Assunto**: Linha de assunto do e-mail (por exemplo, "Ação Necessária: Erro no Documento").
  *   **Tipo de Documento**: Selecione no menu suspenso (por exemplo, "Fatura").

      ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FXzmfZBIoyoDS7tTz1qo4%252Fimage.png%3Falt%3Dmedia%26token%3D24547984-2406-41b5-95d6-0f7f45e06258\&width=768\&dpr=4\&quality=100\&sign=f7aa9b89\&sv=2)

### **2 Editor de Modelo**

* **Menu**: Formate texto, adicione links ou insira tabelas.
* **Editor HTML**: Clique no ícone `<>` para editar HTML bruto.
* **Adicionar Imagens**: Use a função **Upload**.
*   **Campos Dinâmicos:** Insira valores de campos de documento por

    * **Opção de Campo Variável**: Selecione em um menu suspenso.
    * **Entrada Manual**: Digite `{{FieldID}}` (por exemplo, `{{NumeroFatura}}`).

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/email_templates_4.png)

### **3 Salvando**

* Clique em **Salvar** para armazenar o modelo.

## **Enviando um E-mail de Teste**

1.  Abra o modelo e clique em **Enviar Teste**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZTskZNsVfWj6IwBmwoR5%252Fimage.png%3Falt%3Dmedia%26token%3D62229942-2ee7-4d58-833c-eb863b18f2d3\&width=768\&dpr=4\&quality=100\&sign=b804f787\&sv=2)
2. Insira:
   * **E-mail do Destinatário** (obrigatório).
   * **Valores de Campo** (opcional; dados fictícios para espaços reservados). ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FO2yw8EgefTPSCIhxUFH6%252Fimage.png%3Falt%3Dmedia%26token%3D2acc0067-3698-4565-92d8-6c4ddabe497c\&width=300\&dpr=4\&quality=100\&sign=461ae8e7\&sv=2)
3. Revise o e-mail de teste e ajuste o modelo, se necessário.

## **Usando Modelos em Notificações**

Os modelos salvos podem ser vinculados aos fluxos de trabalho de [**Notificação por E-mail**](email-notification/) (por exemplo, lembretes de aprovação, atualizações de status).
