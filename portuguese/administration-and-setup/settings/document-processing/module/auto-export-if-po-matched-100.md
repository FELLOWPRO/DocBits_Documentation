# Exportar automaticamente com correspondência de PO a 100%

### Visão geral

A configuração **Auto Export if PO matched 100%** automatiza a exportação do documento atual quando a correspondência com o pedido de compra atinge 100%. A exportação continua sujeita às restantes condições configuradas de validação, aprovação e exportação. Esta opção reduz a intervenção manual no processamento de documentos totalmente correspondidos.

### O que faz?

Quando esta opção está ativa e a correspondência com o pedido de compra atinge 100%, o sistema pode exportar automaticamente o documento atual. A correspondência inclui os artigos, as quantidades, os preços e os restantes critérios configurados. As condições de validação, aprovação e exportação da organização continuam a aplicar-se; a opção não exporta o pedido de compra em si.

### Benefícios

* **Eficiência**: a exportação automática dos documentos totalmente correspondidos reduz o trabalho manual dos administradores e utilizadores.
* **Precisão**: a condição de correspondência a 100% reduz o risco de exportar documentos com divergências de correspondência pendentes.
* **Rapidez**: o processamento automático dos documentos correspondidos reduz os atrasos no fluxo de trabalho.

### Como utilizar

1. **Ativar a funcionalidade**:
   * Abra Configurações.
   * Selecione **Processamento de documentos**.
   * Selecione **Módulo**.
   * Abra **Pedido de compra**.
   * Ative o interruptor **Auto Export if PO matched 100%**.

<figure><img src="../../../../.gitbook/assets/100%PO.png" alt=""><figcaption></figcaption></figure>

2. **Monitorização**:
   * Os documentos com correspondência a 100% tornam-se elegíveis para exportação automática, sujeitos às restantes condições configuradas.
   * Acompanhe o estado da exportação no painel de documentos e nos respetivos registos.
3. **Considerações**:
   * Verifique se os critérios de correspondência estão corretamente definidos para evitar exportações indesejadas.
   * Reveja regularmente os documentos processados por esta opção para confirmar o funcionamento da automatização.

### Quando utilizar esta funcionalidade

* **Grandes volumes**: quando são processados muitos documentos e existe confiança nos dados de correspondência.
* **Pedidos de rotina**: quando existem poucas variações e a precisão é consistente.
* **Processamento urgente**: quando é necessário acelerar o tratamento dos documentos correspondidos.

Quando a correspondência com pedidos está ativa para o tipo de documento, a opção separada `ALLOW_AUTO_EXPORT_FOR_NON_MATCHABLE_PO_LINES` permite também o estado `NO_MATCHABLE_PO_LINES`. Não autoriza de forma geral outros estados de correspondência incompleta.
