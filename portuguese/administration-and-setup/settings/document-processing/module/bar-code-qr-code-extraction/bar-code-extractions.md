# Extração de códigos de barras

## Visão geral

Este recurso permite a detecção automática de códigos de barras em documentos. Quando ativado, todos os tipos de código de barras compatíveis são verificados e extraídos durante o processamento.

## Como ativar a extração de códigos de barras

Para ativar o recurso Bar-Code Extraction, siga estes passos:

1. **Acesse as configurações**:
   * No Dashboard, vá para **Settings**.
   * Selecione **Document Processing** e, em seguida, escolha **Module**.
2. **Ative o recurso**:
   * Role a página para baixo até localizar a opção **Bar-Code Extraction**.
   * Mova o controle deslizante para ativar o Bar-Code Extraction.\\

## **Configurações adicionais**

### **Barcode Assignment**

#### **Finalidade:** permite que os validadores atribuam manualmente um valor de código de barras extraído a um campo específico do documento durante a validação de campos.

#### Como ativar o **Barcode Assignment**

Para ativar o recurso **Barcode Assignment**, siga estes passos:

1. **Acesse as configurações**:
   * No Dashboard, vá para **Settings**.
   * Selecione **Document Processing** e, em seguida, escolha **Module**.
2. **Ative o recurso**:
   * Role a página para baixo até localizar a opção **Barcode Assignment**.
   * Mova o controle deslizante para ativar o **Barcode Assignment**.\\

#### **Como funciona:**

* Habilita a opção “Assign Barcode” na tela de validação de campos.\\
* Os usuários podem selecionar um valor de código de barras detectado e associá-lo a um campo do documento, como PO Number ou Invoice Number.\\

### Divisão de documentos por código de barras / QR code

**Finalidade:** divide automaticamente documentos de várias páginas em documentos separados com base na presença de determinados códigos de barras ou QR codes.

#### Como ativar a divisão de documentos por código de barras / QR code

Para ativar o recurso de **divisão de documentos por código de barras / QR code**, siga estes passos:

1. **Acesse as configurações**:
   * No Dashboard, vá para **Settings**.
   * Selecione **Document Processing** e, em seguida, escolha **Classification and Extraction**.
2. **Ative o recurso**:
   * Localize a opção **Document Splitting**.
   * Em **Split**, selecione **Split by Barcode / QR Code**.
   * Em **Barcode Type**, escolha um ou mais tipos de código de barras compatíveis na lista.
   * Em **Barcode Pattern**, defina o padrão que deve acionar uma divisão. Você pode usar uma **expressão regular** (regex) para corresponder a valores de código de barras dinâmicos.

**Como funciona:**

* Você seleciona os tipos de código de barras que devem acionar uma divisão.
* Você define um padrão com o qual o código de barras deve corresponder, que pode ser uma string fixa ou uma regex (por exemplo, `^INV\d{6}$` para corresponder a códigos de barras como `INV123456`).
* Durante o processamento do documento, sempre que uma página contém um código de barras correspondente, um **novo documento é criado** a partir dessa página.

### Tipos de código compatíveis

Consulte a [página de visão geral](./) para ver a lista completa de formatos de código de barras e QR code compatíveis.
