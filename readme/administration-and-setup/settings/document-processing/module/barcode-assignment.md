# Atribuição por código de barras

### Visão geral

A configuração **Atribuição por código de barras** (Barcode Assignment) adiciona uma ferramenta de código de barras à **tela de validação de documentos**. Ela lê os códigos de barras e códigos QR encontrados em um documento e permite que você **atribua os valores deles aos campos do documento** — por exemplo, preencher um número de referência, de pedido ou de nota de entrega a partir de um código de barras em vez de digitá-lo.

Esta configuração está **desativada por padrão**.

### O que faz?

Quando esta configuração está ativada, um pequeno **botão de código de barras** (um ícone de código QR) aparece na barra de ferramentas enquanto você valida um documento. Ao clicar nele, são exibidos os códigos de barras que o DocBits encontrou no documento, e você pode mapear cada um para um campo. O campo é então preenchido com o valor lido do código de barras.

* **Ativada** — O botão de código de barras é exibido na tela de validação. Você pode ler os códigos de barras do documento e atribuir os valores deles aos campos.
* **Desativada** — O botão fica oculto e os valores dos códigos de barras não são oferecidos para atribuição durante a validação.

{% hint style="info" %}
**Isto serve para ler um valor de código de barras/QR e atribuí-lo a um campo durante a validação.** A extração automática de dados estruturados de códigos de pagamento (como Swiss QR Bill ou GiroCode) — e a divisão de um arquivo de várias páginas nas páginas separadoras com código de barras — são tratadas por uma configuração **diferente**: [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
{% endhint %}

### Benefícios

* **Entrada mais rápida e sem erros**: Pegue os valores diretamente de um código de barras em vez de lê-los e digitá-los manualmente.
* **Menos erros de digitação**: Um valor escaneado é exatamente o que está codificado no código de barras.
* **Mantém o controle**: Você decide qual código de barras vai em qual campo durante a validação.

### Como usar

1. Vá para **Configurações**.
2. Selecione **Processamento de Documentos**.
3. Selecione **Módulo**.
4. Abra a seção **Tipo de Documento**.
5. Encontre **Atribuição por código de barras** e ligue o botão.
6. Depois, ao validar um documento, clique no **botão de código de barras** na barra de ferramentas e atribua os valores dos códigos de barras detectados aos campos correspondentes.

### Quando usar este recurso

* **Documentos com códigos de barras**: Quando os seus documentos têm códigos de barras/QR cujos valores pertencem a campos específicos (por exemplo, números de pedido ou de referência).
* **Fluxos de validação manual**: Quando uma pessoa revisa documentos e quer preencher campos rapidamente a partir dos códigos de barras.
* **Deixe desativado** se os seus documentos não tiverem códigos de barras utilizáveis, ou se você só precisar da **extração** automática de códigos de barras/QR — consulte [Bar-Code / QR Code Extraction](bar-code-qr-code-extraction/README.md).
