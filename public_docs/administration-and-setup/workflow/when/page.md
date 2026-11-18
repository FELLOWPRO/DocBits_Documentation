# Operação de Tipo de Documento

<figure><img src="../../../.gitbook/assets/workflow_card_condition_doc_type_is_isnot_v1-pt-pt.png" alt="Operação de Tipo de Documento, Versão 1" width="634"><figcaption><p>Versão 1</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/workflow_card_condition_doc_type_is_isnot_v2-pt-pt.png" alt="Operação de Tipo de Documento, Versão 2" width="634"><figcaption><p>Versão 2</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/pt.mp4" %}

**Vídeo:** Cartão: Tipo de documento é / não é · 0:31 · [Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/pt.vtt)

<details>

<summary>Transcrição</summary>

**Tipo de documento é / não é** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/pt.mp4#t=0.25)

O cartão Tipo de documento verifica o tipo de um documento. Escolha É ou Não é e depois o tipo, por exemplo Fatura. Não é corresponde a todos os tipos, exceto o escolhido.

**Exemplo: só faturas** · [0:17](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/pt.mp4#t=17.183)

Por exemplo, um Workflow só para faturas: Tipo de documento é Fatura como cartão Quando, depois um cartão de atribuição. Para notas de crédito, orçamentos ou pedidos, este Workflow não começa.

</details>

## **Propósito:**

Este cartão de fluxo de trabalho é especificamente projetado para realizar operações predefinidas em documentos categorizados por tipo. Ele simplifica o manuseio de várias formas de documentos dentro de um sistema ERP, garantindo que cada tipo seja processado de acordo com seus requisitos exclusivos e políticas organizacionais.

## **Funcionalidade:**

* **Validação de Tipo de Documento**: Este cartão verifica se um documento corresponde a um tipo específico, permitindo que os usuários confirmem sua categorização.
* **Operador**: Os usuários podem definir condições para determinar o tipo de documento. Os operadores disponíveis incluem:
  * **É**: Confirma que o documento corresponde ao tipo de documento especificado.
  * **Não É**: Garante que o documento não corresponda ao tipo de documento especificado.
* **Tipos de Documentos**: Os tipos de documentos suportados incluem:
  * **Fatura**
  * **Nota de Débito**
  * **Nota de Crédito**
  * **Ordem de Compra**
  * **Confirmação de Pedido**
  * **Aviso de Remessa Antecipada**

## **Uso**:

Este cartão é útil para gerentes de documentos e administradores que precisam garantir que os documentos sejam classificados corretamente para um processamento simplificado. A validação dos tipos de documentos aprimora a automação do fluxo de trabalho, permite ações específicas de documentos e mantém os registros organizados.

## **Cenário de Exemplo**:

* Um usuário faz upload de um documento rotulado como "Nota de Débito". Usando o operador "É", o cartão confirma que o tipo de documento é realmente "Nota de Débito", permitindo que o sistema aplique regras de processamento relevantes e o categorize adequadamente.

Ao implantar o cartão "Tipo de Documento", as organizações podem automatizar a classificação de documentos, garantir consistência no manuseio de documentos e melhorar a eficiência dos fluxos de trabalho de gerenciamento de documentos.
