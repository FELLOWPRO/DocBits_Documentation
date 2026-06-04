# Workflow Description: Conditional Export Trigger



<figure><img src="../../../.gitbook/assets/docbits_settings_workflow.png" alt="DocBits Configurações Fluxo de trabalho"><figcaption></figcaption></figure>

Este fluxo de trabalho descreve as condições sob as quais um processo de exportação deve ser iniciado. Garante que apenas os documentos que cumprem todos os critérios especificados são processados para exportação, reforçando a integridade dos dados e o alinhamento com as regras de negócio.

### When:

* Um documento dentro do sistema é avaliado quanto à elegibilidade para exportação.

### Lógica:

1. **Document Type Check**
   * O documento tem de ser de um determinado tipo (por exemplo, "Invoice" ou "Receipt"). Especifique o tipo de documento que se qualifica para o processo de exportação.
2. **Status Verification**
   * O estado atual do documento tem de cumprir critérios predefinidos (por exemplo, "Approved" ou "Ready for Export"), indicando que está pronto para processamento adicional.
3. **Contextual Conditions**
   * São realizadas verificações adicionais para garantir que os detalhes do documento estão em conformidade com requisitos específicos. Estas verificações podem envolver a confirmação de informações em confirmações de encomenda ou ordens de compra. Especifique as condições particulares que têm de ser cumpridas. Por exemplo:
     * Todos os artigos indicados na confirmação da encomenda correspondem aos da ordem de compra.
     * O montante total na confirmação da encomenda corresponde ao montante total da ordem de compra.
     * As datas de entrega especificadas na confirmação da encomenda estão em conformidade com as da ordem de compra.

### Then:

#### Ação:

* **Initiate Export**
  * Se todas as condições acima forem cumpridas, o sistema inicia automaticamente o processo de exportação do documento.
  * Isto pode envolver a geração de um ficheiro de exportação, o envio de dados para um sistema externo ou o desencadeamento de um fluxo de trabalho noutra aplicação.

#### Exemplo de implementação:

```yaml
rules:
  - description: "Conditional Export Trigger"
    conditions:
      - type: "DocumentType"
        criteria: "<SpecifyDocumentType>"
      - type: "Status"
        criteria: "<SpecifyStatus>"
      - type: "DetailMatch"
        criteria:
          - "ItemMatch"
          - "AmountMatch"
          - "DateMatch"
    actions:
      - operation: "StartExport"
```
