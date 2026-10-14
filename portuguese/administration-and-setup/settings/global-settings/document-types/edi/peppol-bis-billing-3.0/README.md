# Peppol BIS Billing 3.0

### Visão geral

Esta seção descreve o plano de implementação para importar e mapear dados de arquivos XML usando o esquema Peppol BIS Billing 3.0. O Peppol BIS Billing 3.0 foi desenvolvido para padronizar processos de faturamento eletrônico e garantir a conformidade com os padrões europeus.

### Objetivos

* Garantir a conformidade total com as especificações do Peppol BIS Billing 3.0.
* Integração perfeita de dados de faturas eletrônicas em nosso sistema de contas a pagar usando o DocBits.
* Melhorar a qualidade dos dados e a eficiência do processamento.

### Escopo

O escopo deste projeto é mapear elementos-chave do esquema Peppol BIS Billing 3.0 para nossas estruturas de dados internas. Em particular, o mapeamento cobrirá as seguintes áreas:

* Detalhes do Fornecedor e do Comprador
* Detalhes da fatura
* Linhas de fatura
* Instruções de pagamento
* Informações fiscais e legais

### Elementos-chave e mapeamento

**Informações do fornecedor:**

* cac:AccountingSupplierParty
  * cbc:EndpointID: Endereço eletrônico do fornecedor
  * cbc:Name: Nome comercial do fornecedor
  * cbc:CompanyID: Número de registro legal do fornecedor
  * cbc:StreetName, cbc:CityName, cbc:PostalZone: Detalhes do endereço do fornecedor

**Informações do comprador:**

* cac:AccountingCustomerParty
  * cbc:EndpointID: Endereço eletrônico do comprador
  * cbc:Name: Nome comercial do comprador
  * cbc:CompanyID: Número de registro legal do comprador
  * cbc:StreetName, cbc:CityName, cbc:PostalZone: Detalhes do endereço do comprador

**Detalhes da fatura:**

* cbc:ID: Número da fatura
* cbc:IssueDate: Data de emissão da fatura
* cbc:DueDate: Data de vencimento da fatura
* cbc:InvoiceTypeCode: Tipo de fatura

**Linhas de fatura:**

* cac:InvoiceLine
  * cbc:ID: Número da linha da fatura
  * cbc:InvoicedQuantity: Quantidade faturada
  * cbc:LineExtensionAmount: Valor da extensão da linha
  * cbc:Description: Descrição da posição de faturamento
  * cac:Item
    * cbc:Name: Nome do item
    * cbc:SellerItemIdentification/cbc:ID: Número do item do fornecedor
  * cac:Price
    * cbc:PriceAmount: Preço por unidade
    * cbc:BaseQuantity: Quantidade base para o preço

**Instruções de pagamento:**

* cac:PaymentMeans
  * cbc:PaymentMeansCode: Código para identificar o método de pagamento
  * cbc:PaymentID: Identificador de pagamento

**Informações fiscais:**

* cac:TaxTotal
  * cbc:TaxAmount: Valor total do imposto
  * cac:TaxSubtotal: Detalhes para cada valor de imposto provisório

### Visualização em PDF para fatura eletrônica

Um documento PDF é gerado de acordo com um layout padrão com os campos importados para fornecer ao usuário uma visualização para fins de referência. Outras personalizações do layout de visualização em PDF são possíveis, mas exigem esforço adicional.
