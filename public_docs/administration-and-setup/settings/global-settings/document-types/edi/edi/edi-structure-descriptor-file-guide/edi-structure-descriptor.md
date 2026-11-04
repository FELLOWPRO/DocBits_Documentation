# Descritor da Estrutura EDI

O objetivo principal do descritor da estrutura é delinear os elementos de uma mensagem EDI de maneira lógica e organizada, tornando mais fácil gerenciar e analisar os dados. Refletindo com precisão a hierarquia da mensagem.

### Elementos do descritor da estrutura

**N1** - Contém os seguintes campos:

* **N1** - Nome ou Identificador da entidade (por exemplo, parte, organização).
* **N2** - Informação de nome adicional (geralmente um nome secundário para a entidade).
* **N3** - Informação de endereço (tipicamente o endereço da rua).
* **N4** - Localização geográfica (cidade, estado, código postal, país).

**N9** - Contém o seguinte campo:

* **N9** - Identificador de referência (por exemplo, número do pedido de compra ou número de controle).
* **Loops:**
  * **MSG01** - Contém o seguinte campo:
    * **MSG01** - Texto de mensagem livre (geralmente uma observação ou instrução especial relacionada à transação).

**IT1** - Contém os seguintes campos:

* **IT1** - Identificador do item de linha (por exemplo, número do item ou código do produto).
* **QTY** - Quantidade do item na transação (por exemplo, unidades encomendadas ou enviadas).
* **TXI** - Informações fiscais (por exemplo, taxas, valores ou classificações fiscais para o item).
* **REF** - Informação de referência (por exemplo, número de lote, número de série ou outros identificadores relacionados ao item).
* **Loops:**
  * **SAC** - Pode se repetir e contém os seguintes campos:
    * **SAC** - Informações de serviço, promoção, desconto ou cobrança (por exemplo, custos adicionais ou descontos relacionados ao item).
    * **TXI** - Informações fiscais relacionadas ao SAC (por exemplo, impostos sobre cobranças ou descontos).

**SAC** - Contém os seguintes campos:

* **SAC** - Informações de serviço, promoção, desconto ou cobrança (pode ser usado independentemente ou dentro do loop IT1 para representar cobranças/descontos adicionais).
* **TXI** - Informações fiscais relacionadas ao SAC (por exemplo, impostos sobre cobranças ou descontos).

### Aqui está o exemplo completo de um descritor de estrutura em formato JSON:

```
{
    "N1": {
        "fields": [
            "N1",  
            "N2",   
            "N3",   
            "N4"    
        ]
    },
    "N9": {
        "fields": [
            "N9"    
        ],
        "loops": {
            "MSG01": {
                "fields": [
                    "MSG01"   
            }
        }
    },
    "IT1": {
        "fields": [
            "IT1",   
            "QTY",   
            "TXI",   
            "REF"    
        "loops": {
            "SAC": {
                "fields": [
                    "SAC",   
                    "TXI"    
        }
    },
    "SAC": {
        "fields": [
            "SAC",   
            "TXI"    
        ]
    }
}
```
