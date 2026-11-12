# Ordem de compra

## Visão geral

Esta definição ativa a secção [**Purchase Order Matching**](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/), que fica acessível depois da validação do documento.

<mark style="color:red;">**Nota**</mark>: Para o tipo de documento **Invoice** têm de estar cumpridos os seguintes requisitos adicionais:

* A definição **Purchase Order** tem de estar ativa (como descrito nesta página)
* A fatura tem de ser do tipo **Purchase Invoice**
* Tem de existir uma **Extracted Table**

## Passos de ativação <a href="#activation-steps" id="activation-steps"></a>

1. Vá a **Settings → Document Types**.
2. Localize o cartão do tipo de documento e clique na roda dentada (**More Settings**).
3. Abra a secção **Purchase Order** e ative **Purchase Order**.

<figure><img src="../../../../../../.gitbook/assets/po-settings-purchase-order-pt-20261031.png" alt="More Settings do tipo de documento Invoice com a secção Purchase Order aberta"><figcaption><p>A secção <strong>Purchase Order</strong> em <strong>More Settings</strong>. O primeiro interruptor ativa a conciliação de ordens de compra para o tipo de documento; os seguintes afinam-na.</p></figcaption></figure>

## **Funcionalidade**

Uma vez ativada a definição, a secção [**Purchase Order Matching**](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/) fica disponível depois da validação do documento.

### Que quantidade é comparada

A quantidade da ordem de compra comparada pela conciliação depende de **PO match server side**:

* **PO match server side off** – junto ao interruptor **Purchase Order** aparece uma lista **Match quantity**. Escolha **Quantity**, **Received Quantity** ou **Received Delivery Open Quantity**. O DocBits compara a quantidade escolhida com o seu próprio motor de conciliação.
* **PO match server side on** – a conciliação segue o conjunto de regras do tipo de documento e **Match quantity** faz parte dessas regras. A linha de cabeçalho da secção mostra então a ligação **Configure PO matching rules**, que abre as regras. Ver [Purchase Order Matching Rules](purchase-order-matching-rules.md).

{% hint style="info" %}
A captura acima foi feita com **PO match server side** ativo, por isso a lista **Match quantity** não aparece nesse ecrã: define-se nas regras de conciliação.
{% endhint %}

### Pagamento antecipado antes da receção de mercadorias

Algumas faturas chegam antes da mercadoria. Para conciliar uma fatura destas com a quantidade encomendada em vez da recebida, ative **Allow pre-payment before goods receipt** na mesma secção.

O interruptor só aparece quando se verificam as três condições:

* o tipo de documento é **Invoice**,
* **Purchase Order** está ativo,
* e a quantidade conciliada é **Received Quantity**.

Se alterar a quantidade conciliada para outro valor, o interruptor desaparece das definições. No [PO matching screen](../../../../../../end-user-and-partner-section/end-user-section/purchase-order-matching/) aparece então **Match as pre-payment** abaixo de **Use Lines Net Amount for Matched Total**, com a indicação *Match on ordered quantity instead of received quantity*. O interruptor fica esbatido e com uma nota quando o fornecedor não pode ser faturado antes da receção de mercadorias no ERP.

Enquanto o interruptor está ativo, o ecrã lê a quantidade encomendada, e não a recebida, para as ligações manuais e para o total conciliado. A escolha é guardada no documento e o **Auto Match** é executado de novo; se essa conciliação falhar, a escolha volta ao valor anterior.
