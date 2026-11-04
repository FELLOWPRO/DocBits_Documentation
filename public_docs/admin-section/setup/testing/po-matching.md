# Correspondência de PO

Quando se trata de testar a configuração de Correspondência de PO, você precisará criar um pedido de compra no LN/M3 para verificar se o INFOR está sincronizado com o DocBits.

## Criando um Pedido de Compra no INFOR

* LN: https://docs.infor.com/ln/10.4/en-us/lnolh/docs/ln\_10.4\_procpoug\_\_en-us.pdf
* M3: https://docs.infor.com/m3udi/16.x/en-us/m3beud/default.html?helpcontent=ois610.html

Depois de criar seu pedido de compra, vá para Configurações → Consulta de Dados Mestres e procure pelo número do pedido de compra do PO que você acabou de criar, pois agora ele deve aparecer nos dados mestres do pedido de compra no DocBits.

![](https://lh7-us.googleusercontent.com/JKGJdww6uF6U5mc1s1X\_uCcEMPYeqcikfrFOFjxpxpuaNjw-XmzNmIV2G2x6R-ZpwN2KlZACQe5Hs\_UB26klGU5XZyu6srVVLPVkS9AgEDZ1SO75YF-4ZTIt-aAuxoyyoW5sNPLsl0UxXwk193QNrFs)

Você deverá ver seu número de PO único aqui, o que significa que o DocBits e o INFOR estão corretamente sincronizados.

Agora, faça o upload de sua fatura que corresponda à quantidade e aos preços unitários do pedido de compra que você criou. Valide o documento e selecione a Correspondência de PO na tela de validação.

Os itens de linha do PO e da fatura devem corresponder automaticamente, então basta selecionar a opção de exportação e verificar se o documento é exportado sem erros. Se você encontrar um erro de exportação, crie um ticket para a equipe de suporte do DocBits para ajudá-lo. Se você não souber como criar um ticket dentro do DocBits, consulte nossa documentação de Visão Geral do DocBits para obter assistência.
