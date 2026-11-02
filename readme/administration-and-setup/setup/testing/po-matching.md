# Correspondência de pedidos de compra

{% embed url="https://youtu.be/qR-lrSaj4Ug" %}
Tutorial de correspondência de pedidos de compra do DocBits: correspondência automática e manual de linhas, tolerâncias e indicadores de divergência
{% endembed %}

Para testar a correspondência de pedidos de compra, crie um pedido de compra no LN/M3 e verifique se foi sincronizado com o DocBits.&#x20;

## Criar um pedido de compra na Infor

{% embed url="https://youtu.be/hn_bkeUMxJg" %}
{% endembed %}


* LN: https://docs.infor.com/ln/10.4/en-us/lnolh/docs/ln\_10.4\_procpoug\_\_en-us.pdf&#x20;
* M3: https://docs.infor.com/m3udi/16.x/en-us/m3beud/default.html?helpcontent=ois610.html&#x20;

Depois de criar o pedido, abra Configurações → Pesquisa de dados mestre e procure o respetivo número. O pedido deverá aparecer nos dados mestre de pedidos de compra do DocBits.

![](https://lh7-us.googleusercontent.com/JKGJdww6uF6U5mc1s1X\_uCcEMPYeqcikfrFOFjxpxpuaNjw-XmzNmIV2G2x6R-ZpwN2KlZACQe5Hs\_UB26klGU5XZyu6srVVLPVkS9AgEDZ1SO75YF-4ZTIt-aAuxoyyoW5sNPLsl0UxXwk193QNrFs)

O número do pedido deve aparecer aqui. Isto confirma a sincronização desse pedido entre o DocBits e a Infor.

Carregue uma fatura cuja quantidade e preços unitários correspondam ao pedido criado. Valide o documento e selecione a correspondência de pedidos de compra no ecrã de validação.

Os itens da fatura e do pedido devem corresponder automaticamente. Selecione a exportação e confirme que o documento é exportado sem erros. Se ocorrer um erro, crie um pedido de suporte para a equipa DocBits. Consulte a documentação de visão geral do DocBits para saber como criar o pedido.

\
