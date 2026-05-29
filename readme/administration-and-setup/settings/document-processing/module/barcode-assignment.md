# Atribuição por código de barras

### Visão geral

A configuração **Atribuição por código de barras** (Barcode Assignment) permite que o DocBits use os **códigos de barras dentro de um arquivo para separá-lo em documentos individuais**. Isso é útil quando vários documentos são digitalizados juntos em um único PDF grande e um código de barras marca onde um documento termina e o próximo começa.

Esta configuração está **desativada por padrão**.

### O que faz?

Quando esta configuração está ativada, o DocBits procura códigos de barras em um arquivo recebido com várias páginas e o divide em documentos separados nas posições marcadas. Cada documento resultante é então processado individualmente.

* **Ativada** — O DocBits detecta os códigos de barras e separa automaticamente um arquivo combinado em documentos individuais com base neles.
* **Desativada** — O arquivo é processado como um único documento; os códigos de barras não são usados para dividi-lo.

{% hint style="info" %}
Aqui trata-se de **dividir e atribuir** páginas com base em códigos de barras. A leitura dos dados codificados em um código de barras (por exemplo, para códigos QR de pagamento) é tratada separadamente em **Bar-Code / QR Code Extraction**.
{% endhint %}

### Benefícios

* **Digitalização em lote mais rápida**: Digitalize uma pilha inteira de documentos de uma só vez, separados por folhas com código de barras, em vez de digitalizar cada documento individualmente.
* **Menos triagem manual**: O DocBits cria os documentos individuais para você, então ninguém precisa dividir o PDF manualmente.
* **Menos erros**: Os documentos são separados exatamente nas posições marcadas todas as vezes.

### Como usar

1. Vá para **Configurações**.
2. Selecione **Processamento de Documentos**.
3. Selecione **Módulo**.
4. Abra a seção **Tipo de Documento**.
5. Encontre **Atribuição por código de barras** e ligue o botão.

### Quando usar este recurso

* **Digitalização de alto volume**: Quando você digitaliza muitos documentos juntos e usa folhas separadoras com código de barras entre eles.
* **Lotes mistos**: Quando um único arquivo recebido contém vários documentos diferentes que precisam ser processados separadamente.
* **Deixe desativado** se os seus documentos sempre chegam como arquivos separados — a divisão não é necessária nesse caso.
