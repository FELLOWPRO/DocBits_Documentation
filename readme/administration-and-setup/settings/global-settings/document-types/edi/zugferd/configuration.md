# Configuração do ZUGFeRD

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
Tutorial de e-fatura do DocBits: processar XRechnung / ZUGFeRD (Factur-X), validar dados e automatizar workflows
{% endembed %}

## **Versões compatíveis do ZUGFeRD**

O DocBits oferece suporte a todas as principais versões do ZUGFeRD, incluindo:

* **1.0**
* **2.0**
* **2.1** (em conformidade com FACTUR-X 1.0.05)
* **2.2**
* **2.3** (em conformidade com FACTUR-X 1.07.2)
* **2.3.2**

#### Ativação e modificação do padrão

O padrão ZUGFeRD está sempre ativo por padrão, mas você pode modificá-lo se necessário.

### **Passos para modificar as configurações do ZUGFeRD:**

1. Acesse **Settings → Global Settings → Document Types → Invoice**.
2. Clique em **E-Doc**.\\
3. Uma lista de todos os e-docs disponíveis será exibida.
4. Localize a versão do **ZUGFeRD** que você deseja modificar.\\

## **Configuração de transformação e de caminhos XML:**

Nas **configurações de transformação**, você pode definir o caminho para localizar informações específicas no arquivo XML e salvá-las em uma nova estrutura, o que facilita o acesso aos dados.\
<mark style="color:red;">**Observação**</mark>: se você usar essa funcionalidade, deverá usar os caminhos XML recém-criados, e não os caminhos XML originais, em **Preview** e **Extraction Path**.

### **Passos para modificar o arquivo de transformação:**

1. Abra **Transformation**.
2. Crie um novo rascunho clicando no **ícone de lápis**.
3. Selecione o rascunho recém-criado.
4. Crie um novo campo ou modifique um existente.
5. Defina o caminho desejado para a extração de dados.
6. Clique em **Save**.

### Observações importantes:

* O **arquivo de preview** é usado somente para **FACTUR-X** e não para **ZUGFeRD**. O ZUGFeRD usará o **PDF** original.

## Configuração do Preview PDF

A **configuração do Preview PDF** é usada para gerar uma versão do documento legível pelo usuário. Você pode personalizá-la com HTML de acordo com suas necessidades.

### **Passos para modificar o arquivo de preview:**

1. Abra **Preview**.
2. Crie um novo rascunho clicando no **ícone de lápis**.
3. Selecione o rascunho recém-criado.
4. Crie um novo campo ou modifique um existente.
5. Defina o caminho desejado para a extração de dados.
6. Clique em **Save**.

## Configuração dos Extraction Paths

A **configuração dos Extraction Paths** é usada para extrair dados e preencher campos na **tela de validação**, como a tabela de itens da fatura ou os campos configurados no layout da fatura.

### **Passos para modificar os** **Extraction Paths**:

1. Abra **Extraction Paths**.
2. Crie um novo rascunho clicando no **ícone de lápis**.
3. Selecione o rascunho recém-criado.
4. Crie um novo campo ou modifique um existente.
5. O lado esquerdo representa o **ID do campo do DocBits**, que pode ser encontrado em **Settings → Global Settings → Document Types → Invoice → Fields**.\\
6. O lado direito representa o **caminho para o campo** criado na Transformation.
7. Clique em **Save**.

Seguindo esses passos, você garante a extração e a validação precisas de dados em faturas ZUGFeRD.

## Regras efetivas e ativação

As regras específicas da organização têm prioridade sobre as predefinições do formato eDoc detetado. Verifique a TRANSFORMATION ativa e verifique qual o nó que fornece invoice_type no XML transformado; o caminho depende do formato. Save guarda um rascunho; utilize a marca de verificação para o ativar após os testes. Uma Preview renderizada não comprova o tipo de documento guardado. Consulte o [guia de resolução de problemas de classificação](../credit-note-recognized-as-invoice.md) para obter informações sobre os códigos 381/261, os scripts posteriores e as precauções de reprocessamento.
