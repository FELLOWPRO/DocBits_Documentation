# Configuração do ZUGFeRD

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
Tutorial de E-Invoice do DocBits: Processar XRechnung / ZUGFeRD (Factur-X), Validar Dados e Automatizar Fluxos de Trabalho
{% endembed %}

## **Versões suportadas do ZUGFeRD**

O DocBits suporta todas as principais versões do ZUGFeRD, incluindo:

* **1.0**
* **2.0**
* **2.1** (em conformidade com FACTUR-X 1.0.05)
* **2.2**
* **2.3** (em conformidade com FACTUR-X 1.07.2)
* **2.3.2**

#### Ativação e modificação padrão

O padrão ZUGFeRD está sempre ativo por padrão, mas você pode fazer modificações se necessário.

### **Etapas para modificar as configurações do ZUGFeRD:**

1. Navegue até **Configurações → Configurações globais → Tipos de documento → Fatura**.
2. Clique em **E-Doc**.\\
3. Uma lista de todos os e-docs disponíveis aparecerá.
4. Localize a versão do **ZUGFeRD** que deseja modificar.\\

## **Configuração de transformação e caminho XML:**

Nas **configurações de transformação**, você pode definir o caminho para localizar informações específicas dentro do arquivo XML e salvá-las em uma nova estrutura, facilitando o acesso aos dados.\
<mark style="color:red;">**Nota**</mark>: Se você usar esta funcionalidade, deverá usar os novos caminhos XML criados, e não os caminhos XML originais, na **Visualização** e no **Caminho de extração**.

### **Etapas para modificar o arquivo de transformação:**

1. Abra a **Transformação**.
2. Crie um novo rascunho clicando no **ícone do lápis**.
3. Selecione o rascunho recém-criado.
4. Crie um novo campo ou modifique um existente.
5. Defina o caminho desejado para extração de dados.
6. Clique em **Salvar**.

### Notas importantes:

* O **arquivo de visualização** é usado apenas para o **FACTUR-X** e não para o **ZUGFeRD**. O ZUGFeRD usará o **PDF** original.

## Configuração de visualização de PDF

A **Configuração de visualização de PDF** é usada para gerar uma versão do documento legível pelo usuário. Você pode personalizá-la com HTML para atender às suas necessidades.

### **Etapas para modificar o arquivo de visualização:**

1. Abra a **Visualização**.
2. Crie um novo rascunho clicando no **ícone do lápis**.
3. Selecione o rascunho recém-criado.
4. Crie um novo campo ou modifique um existente.
5. Defina o caminho desejado para extração de dados.
6. Clique em **Salvar**.

## Configuração de caminhos de extração

A **Configuração de caminhos de extração** é usada para extrair dados e preencher campos na **tela de validação**, como a tabela de faturas ou campos configurados no layout da fatura.

### **Etapas para modificar** **os caminhos de extração**:

1. Abra os **Caminhos de extração**.
2. Crie um novo rascunho clicando no **ícone do lápis**.
3. Selecione o rascunho recém-criado.
4. Crie um novo campo ou modifique um existente.
5. O lado esquerdo representa o **ID do campo DocBits**, que pode ser encontrado em **Configurações → Configurações globais → Tipos de documento → Fatura → Campos**.\\
6. O lado direito representa o **caminho para o campo** criado na Transformação.
7. Clique em **Salvar**.

Ao seguir estas etapas, você pode garantir a extração e validação precisas de dados para faturas ZUGFeRD.
