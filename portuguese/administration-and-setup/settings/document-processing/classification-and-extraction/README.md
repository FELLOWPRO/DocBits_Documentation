# Classification And Extraction

## Overview

In the **Classification and Extraction** settings, you can:

* Enable **Document Splitting** based on QR codes
* Configure **amount formatting**
* Set up **table extraction**
* Toggle processing of unsupported **ZUGFeRD** files
* Define special classification rules
* Monitor Custom-Trained **AI Models** used in the classification process

This page provides a detailed explanation of all available settings.

## **Accessing Classification and Extraction Settings**

To access the **Classification and Extraction** settings, go to:\
**Settings → Document Processing → Classification and Extraction**

<figure><img src="../../../../.gitbook/assets/settings_classification_and_extraction.png" alt=""><figcaption></figcaption></figure>

## Document Splitting

In the **Document Splitting** section, you can configure whether an uploaded document should be split into multiple documents whenever a **barcode** appears on one of its pages.

To activate this feature:

1. Go to the **Document Splitting** section.
2.  Open the dropdown menu.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_14.png" alt=""><figcaption></figcaption></figure>
3.  Select **Split by Barcode/QR Code**.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_15.png" alt=""><figcaption></figcaption></figure>

You will then have the option to:

* Select one or more barcode types to be detected.
*   Specify a regex pattern that the barcode must match in order to trigger document splitting.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_16.png" alt=""><figcaption></figcaption></figure>

## Amount Formatting

In the **Amount Formatting** section, you have two options:

* **Allow Rounding During Amount Comparison:**\
  If enabled, a tolerance of ±0.5 is allowed during amount comparison.\
  If disabled, a default tolerance of ±0.05 applies.
* **Require Exact Match for Amount Comparison:**\
  If enabled, amounts must match exactly with zero tolerance.\
  If disabled, a tolerance of ±0.05 is allowed.

<mark style="color:red;">**Note**</mark>: Only one of these settings can be active at a time.

## Table Extraction

{% embed url="https://youtu.be/LFw-JXqYWzw" %}
DocBits Tables Explained: AI Table Extraction vs Standard Extraction (When to Use Which)
{% endembed %}

In this video, we compare two ways to process tables in DocBits: AI-based table extraction and standard (non-AI) extraction. You’ll learn what the differences are, when each method performs best, and how to choose the right approach for your document types.

**What you’ll learn:**
*   What AI table extraction does (pattern recognition, flexible layouts)
*   What standard table extraction does (structured, more controlled behavior)
*   Pros & cons: accuracy vs consistency, speed, and maintainability
*   When AI is best (varying layouts, noisy scans, supplier differences)
*   When standard extraction is best (stable templates, strict control, predictable output)
*   Practical tips to improve table results and reduce mismatches

{% hint style="info" %}
**Pré-requisitos para uma extração de tabelas funcional**

* O tipo de documento tem **colunas de tabela** (Definições → Definições Globais → Tipos de Documento → [Colunas da Tabela](../../global-settings/document-types/table-columns.md)). Sem colunas, não há para onde extrair.
* A **Extração de tabelas** ou a **Extração de tabelas por IA** está ativada abaixo, para toda a organização.
* O documento tem texto legível: o OCR foi executado, ou o E-Text é usado para PDFs nativos digitais ([Definições OCR](../ocr-settings.md)).
* O treino e os modelos de IA são **por fornecedor**. Uma tabela treinada aplica-se apenas aos documentos do fornecedor com que foi treinada.
{% endhint %}

Pode extrair tabelas de documentos ativando a **Extração de tabelas** ou a **Extração de tabelas por IA**. Uma tabela treinada (seja com IA ou manualmente) está sempre associada a um fornecedor específico.

**Extração de tabelas:** Ativa a extração de tabelas baseada em regras. As tabelas são treinadas por fornecedor no ecrã de validação (*Ir para a vista de extração de tabelas*).\
Saiba mais sobre o treino [aqui](../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).

**Extração de tabelas por IA:** Usa IA para extrair a tabela de qualquer fornecedor sem treino. Se os resultados de um fornecedor não forem suficientemente precisos, treine a tabela desse fornecedor; as regras guardadas passam então a ter precedência sobre a IA para esse fornecedor.

**Usar Extração de tabelas Vision (IA):** A IA lê a imagem da página em vez da camada de texto. Ajuda com documentos digitalizados e tabelas sem uma estrutura de texto clara; é mais lenta.

**Usar Extração estruturada (IA):** A IA devolve a tabela numa estrutura fixa que é mapeada diretamente para as colunas de tabela configuradas. Recomendado quando os cabeçalhos das colunas nos documentos variam muito.

**Extração de tabelas para elemento de custo:** Quando ativada, o DocBits pode extrair elementos de custo das tabelas ao nível da linha e classificá-los em conformidade.\
Explicação detalhada disponível [aqui](table-extraction-for-costing-element.md).

**Extrair automaticamente o código de imposto:** Quando ativada, o sistema preenche automaticamente o campo **Código de imposto** no ecrã de validação, desde que exista um campo de código de imposto configurado.\
Mais informações sobre esta definição [aqui](auto-extract-tax-code.md).

**Guardar regras de extração (apenas administradores):** Só os administradores podem clicar em *Guardar regras* no treino de tabelas. Ative-a quando os utilizadores continuam a guardar regras que estragam a extração de um fornecedor.

**Modelo de IA:** Seleciona o nível de IA usado para a extração de tabelas: **Fast** (predefinição), **Full** (máxima precisão, mais lento) ou **Nexus** (terceiro nível, de ativação opcional). A tabela por baixo do seletor mostra:

* Quais os **fornecedores** que usam cada modelo de IA
* Se usam E-Text
* Opções para eliminar uma entrada ou repor os dados de treino

Esta definição é explicada em detalhe [aqui](ai-model.md).

### Porque é que a tabela é diferente de fornecedor para fornecedor?

Tudo o que o DocBits aprende sobre uma tabela é guardado **por fornecedor**:

* **Regras guardadas** (treino de tabelas): posição da tabela e mapeamento das suas colunas no layout desse fornecedor.
* **Tags e regras de formatação da tabela de IA**: indicações que o utilizador guardou para a tabela de IA desse fornecedor.
* **Modelo de IA específico do fornecedor**: o nível escolhido para esse fornecedor em *Mais definições* no ecrã de validação.

Assim, o fornecedor A, com regras guardadas, mostra uma tabela determinística no separador *Tabela extraída* do ecrã de validação, enquanto o fornecedor B, sem regras, recebe a *Tabela extraída por IA*. Para que o fornecedor B se comporte como o A, treine a tabela de B uma vez. Para repor um fornecedor, elimine as suas regras no ecrã de validação ou reponha os seus dados de treino na tabela do Modelo de IA.

### Chaves de preferências

Cada opção desta secção é guardada como uma preferência da organização. Use a chave quando definir o valor através da API (`/preferences/set_preference`), de um script ou do DocBits MCP (`get_preference` / `set_preference`).

| Definição (etiqueta na interface) | Chave de preferência | Valores |
|---|---|---|
| Extração de tabelas | `TABLE_EXTRACTION_SETTING` | `true` / `false` |
| Extração de tabelas por IA | `USE_AI_TABLE_EXTRACTION` | `true` / `false` |
| Usar Extração de tabelas Vision (IA) | `TABLE_EXTRACTION_USE_VISION` | `true` / `false` |
| Usar Extração estruturada (IA) | `USE_STRUCTURED_EXTRACTION` | `true` / `false` |
| Extração de tabelas para elemento de custo | `CHARGES_TABLE_EXTRACTION` | `true` / `false` |
| Extrair automaticamente o código de imposto | `AUTO_EXTRACT_TAX_CODE` | `true` / `false` |
| Guardar regras de extração (apenas administradores) | `ONLY_ADMIN_CAN_SAVE_RULES` | `true` / `false` |
| Modelo de IA | `AI_MODEL` | `gpt-5.4-mini` (Fast), `gpt-5.5` (Full), `qwen3.8-max` (Nexus) |
| Versão da extração de tabelas (caixa de diálogo de confirmação) | `TBL_EXT_VERSION` | cadeia de versão |
| Definições OCR → Usar dados de IA para tabelas, se disponíveis | `USE_AI_DATA_FOR_TABLE` | `true` / `false` |
| Definições OCR → Usar E-Text, se disponível | `USE_ETEXT_IF_AVAILABLE` | `true` / `false` |

Notas:

* As preferências booleanas são guardadas como as cadeias `true` / `false`; uma chave que nunca foi definida conta como `false`. Se enviar `1` ou `0`, o DocBits guarda `true` / `false`.
* `AI_MODEL` não definido significa **Fast**.
* A alteração de uma chave produz efeito nos documentos processados posteriormente. Reinicie um documento para o extrair novamente com a nova definição.
* As escolhas por fornecedor (E-Text, modelo de IA, regras guardadas) não são preferências da organização; são definidas no ecrã de validação em *Mais definições* num documento desse fornecedor.

## Electronic Document

**Process Unsupported ZUGFeRD PDF:** If enabled, unsupported **ZUGFeRD** versions will be processed as standard PDFs, and the embedded XML will be ignored.

The list of supported **ZUGFeRD** versions can be found [here](../../global-settings/document-types/edi/zugferd/README.md).

## **Classification Rules**

In the **Classification Rules** section, you can define specific **regex** patterns and criteria to help the system automatically classify documents during processing.

To access this section, click the **Classification Rules** tab at the top of the page.

<figure><img src="../../../../.gitbook/assets/classification_and_extraction_1.png" alt=""><figcaption></figcaption></figure>

### **Add a New Classification Rule**

To create a new rule:

1.  Click **Add** in the top-right corner.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_2.png" alt=""><figcaption></figcaption></figure>
2. Fill in the following fields:
   * **Pattern**: The regex pattern the system should search for to trigger classification.
   * **Type**: Where the pattern should be searched (e.g., **Barcode**).
   * **Sub Organization** _(optional)_: Specify which sub organization the rule applies to.
   * **Document Type**: Define the document type to assign when the pattern is matched.
   *   **Sub Document Type** _(optional)_: Specify a sub type for more detailed classification.

       <figure><img src="../../../../.gitbook/assets/classification_and_extraction_3.png" alt=""><figcaption></figcaption></figure>
3.  Click **Save** to save your classification rule.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_4.png" alt=""><figcaption></figcaption></figure>

### **Edit a Classification Rule**

To edit an existing rule:

1.  Click the three dots in the **Actions** column.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_5.png" alt=""><figcaption></figcaption></figure>
2.  Select **Edit**.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_6.png" alt=""><figcaption></figcaption></figure>
3. Make your desired changes.
4.  Click **Save** to apply the updates.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_4.png" alt=""><figcaption></figcaption></figure>

### **Delete a Classification Rule**

To delete a rule:

1.  Click the three dots in the **Actions** column.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_5.png" alt=""><figcaption></figcaption></figure>
2.  Select **Delete**.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_7.png" alt=""><figcaption></figcaption></figure>

## AI Models

The **AI Models** section displays all custom-trained models that have been specifically fine-tuned for your needs.

### Accessing the AI Models Section

To open this section, click the **AI Models** tab located at the top of the page.

<figure><img src="../../../../.gitbook/assets/classification_and_extraction_8.png" alt=""><figcaption></figcaption></figure>

### Model Categories

Models are organized into categories. Below each category name, the number of models it contains is shown.\
Click on a category to view its details.

<figure><img src="../../../../.gitbook/assets/classification_and_extraction_9.png" alt=""><figcaption></figcaption></figure>

At the top of the selected category page, you’ll see key information about each model:

* **Type**: The type of model.
* **First Page Only**: Indicates whether the model processes only the first page of a document.
* **Version**: The version number of the model.

### Model Table

All models within a category are listed in a table, which includes the following information:

* **Name**: The name of the model.
* **Next Model**: The model that will further process the output of the current model.
* **Document Type**: The primary document type assigned by the model during classification.
* **Document Sub Types**: The sub types into which the document is further classified.
* **Priority**: The priority level that determines the model’s position in the classification queue.

<figure><img src="../../../../.gitbook/assets/classification_and_extraction_11.png" alt=""><figcaption></figcaption></figure>

### Editing a Model

To edit a model:

1.  Click the pen icon in the **Actions** column next to the model you want to edit.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_10.png" alt=""><figcaption></figcaption></figure>
2. Update the available fields:
   * **Next Model**: Select the model that should process the output from the current model.
   * **Document Type**: Choose the document type the model should classify the input as.
3.  Click **Save** to apply your changes.

    <figure><img src="../../../../.gitbook/assets/classification_and_extraction_12.png" alt=""><figcaption></figcaption></figure>
