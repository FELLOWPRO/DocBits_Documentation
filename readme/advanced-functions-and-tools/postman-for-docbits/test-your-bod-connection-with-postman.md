# Teste sua conexão BOD com Postman

## Visão Geral

Esta página explica como verificar o processamento bem-sucedido do seu BOD (Business Object Document) usando Postman. Você testará o endpoint da API relevante enviando uma solicitação com seu arquivo de mapeamento BOD. Siga os passos abaixo para completar o processo.

## Acessando sua Chave de API e Arquivo de Mapeamento BOD

### Recuperando sua Chave de API

1.  Vá para **Configurações → Configurações globais → Integração e SSO**.

    ![Página de definições no DocBits com a navegação Global Settings aberta e Integrations & SSO destacado entre Document Types e Email Templates](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_integration.png)
2.  Você pode copiar manualmente sua **Chave de API** ou clicar no botão de copiar para copiá-la para a área de transferência.

    ![Página Integration & SSO no DocBits que mostra o campo API Key com o respetivo botão de copiar acima da secção SSO Service Provider Settings](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_1.png)

### **Baixando o Arquivo de Mapeamento BOD**

1.  Vá para **Configurações → Processamento de documentos → Exportar**.

    ![Página de definições no DocBits com a navegação Document Processing aberta, listando Import, OCR Settings, Classification and Extraction e Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
2.  Na coluna **Ações** da entrada de exportação relevante, clique no menu de três pontos e selecione **Editar**.

    ![Página Export settings no DocBits com as linhas google Invoice webhook e Infor LN Test Invoice e o menu Actions aberto](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_2.png)
3.  Localize o **Arquivo de mapeamento BOD** e clique no botão **Download** para salvá-lo.

    ![Diálogo do Infor ION com o campo Title Test e os botões de descarregamento ION-Mapping File, IDM Mapping File e BOD-Mapping File](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_3.png)

## Teste o Endpoint no Postman

1.  **Cole o Comando cURL no Postman**

    Abra o Postman e cole o seguinte comando cURL na seção **Import**. O Postman configurará automaticamente a solicitação.

    ```bash
    curl -X 'POST' \
      'https://api.docbits.com/prod-api/import/purchase_order_bod' \
      -H 'accept: application/json' \
      -H 'X-API-KEY:' \
      -H 'Content-Type: multipart/form-data' \
      -F 'org_id=' \
      -F 'sub_org_id=' \
      -F 'file=@file.xml;type=text/xml' \
      -F 'custom_fields_mapping='
    ```

    ![Espaço de trabalho do Postman com o ecrã de boas-vindas, o separador History e a opção Create a new request](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_4.png)

    ![Diálogo Import do Postman com o campo de colagem de cURL aberto para importar o pedido BOD](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_5.png)
2.  **Defina a Chave de API**\
    Vá para a aba **Headers**, localize o cabeçalho `X-API-KEY` e cole sua chave de API na coluna **Value**.

    ![Pedido do Postman para https://api.docbits.com/prod-api/import/purchase_order_bod com o separador Headers e a linha X-API-KEY](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_6.png)
3.  **Faça o Upload do Arquivo BOD**\
    Vá para a aba **Body**, localize a chave `file`, clique em **Select Files** na coluna **Value** e faça o upload do seu arquivo BOD XML.

    ![Separador Body do pedido do Postman com as chaves form-data org_id, sub_org_id, file com Select Files e custom_fields_mapping](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_7.png)
4.  **Envie a Solicitação**\
    Clique em **Send** para fazer a chamada da API.

    ![Pedido do Postman com o separador Authorization aberto e No Auth selecionado](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_8.png)
5.  **Verifique a Resposta**\
    Verifique a resposta para confirmar que seu BOD foi processado com sucesso.

    ![Painel de resposta do Postman com estado 200 OK e a mensagem do corpo BOD processed successfully](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/test_bod_connection_postman_9.png)
