---
hidden: true
---

# Configuração de Fuzzy Data com List of Values

### **Visão geral**

Cada tipo de documento tem suas próprias configurações de List of Values (LoV), que devem ser definidas separadamente. Diferentemente de **Fuzzy Data com Master Data**, a **List of Values** não vem com grupos de lookup padrão.

### Para configurar a List of Values, navegue até:

Settings → Global Settings → Document Types → Invoice → Fields → Master Data Settings → LOV Master Data

### **Criando uma Nova Configuração de List of Values**

Existem duas maneiras de criar uma configuração de List of Values:

**1. Duplicar um Lookup Existente**

* Isso copia todas as informações e campos de um grupo existente.
* Você só precisa fornecer um **novo nome**.

**2. Criar um Lookup do Zero**

* Clique em **"Create List of Values"**.
* Preencha os detalhes necessários:
  * **Configuration Name** → Nome da List of Values.
  * **Lookup Table** → A tabela da qual os valores serão obtidos.
  * **Conflict Handler** → Escolha um:
    * Best Score
    * Return None
    * Return First
  * **Context Type** → Determina se a LoV se aplica ao nível **Header** ou **Line**.
  * **Match All** → _(Mais detalhes necessários)_

### **Gerenciando Campos Dentro de um Grupo de List of Values**

Cada grupo de LoV contém campos que podem ser **adicionados, removidos ou editados.**

**Adicionando um Novo Campo**

Para adicionar um novo campo dentro de um grupo:

* Clique em **"Create"** dentro do grupo relevante.
* Forneça os seguintes detalhes:
  * **Lookup Field** → O nome da coluna da tabela de lookup.
  * **Validation Field** → O campo correspondente do DocBits.
  * **Parent Field** → _(Mais detalhes necessários)_
  * **Search Operator** → Escolha um:
    * Smart
    * Contains
    * Exact
    * Starts with
    * Ends with
  * **Caixas de seleção:**
    * **Auto Trigger** → Quando ativado, se outro campo em uma configuração de lookup diferente compartilhar a mesma coluna, este campo será atualizado **automaticamente** sempre que o outro campo for atualizado.
    * **Searchable** → Ativa o campo como um campo de **List of Values**, permitindo buscas na tabela de lookup.

#### **Etapa Final: Adicionando os Campos ao Layout**

Após configurar os campos de List of Values, **certifique-se de adicioná-los ao layout usando o Layout Builder**. Se os campos não forem adicionados ao layout, eles não estarão disponíveis para uso.
