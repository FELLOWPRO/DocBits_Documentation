# Correspondência Automática de Dados de Pedido de Compra

Docbits é um sistema avançado projetado para automatizar a correspondência de dados de pedidos de compra (POs) com documentos de fatura recebidos. Esta ferramenta é especificamente projetada para a gestão eficiente e processamento de dados de faturas dentro de sistemas ERP. Esta documentação explica os fundamentos da correspondência automática através do Docbits e define as regras específicas necessárias para uma correspondência bem-sucedida.

<figure><img src="../../../.gitbook/assets/docbits_purchase_order_invoice_3.svg" alt="DocBits Compra Pedido Fatura 3"><figcaption></figcaption></figure>

## **Princípios Fundamentais da Correspondência Automática no Docbits**

**Extração de Dados:** O Docbits inicia o processo extraindo dados relevantes de documentos de fatura digitalizados. Normalmente, esses dados incluem números de itens, quantidades e preços unitários de cada linha da fatura. A precisão dessa extração é crucial, pois forma a base para o processo de correspondência subsequente.

**Comparação com Dados de PO:** Os dados extraídos são comparados com as informações correspondentes nos pedidos de compra armazenados. O Docbits verifica se os números de itens, quantidades e preços correspondem aos dos POs. Para uma correspondência bem-sucedida, os dados nas faturas devem corresponder aos dados nos pedidos de compra, considerando os limites de tolerância definidos.

**Correspondência Automática:** Com base nos resultados da comparação, o Docbits realiza a correspondência. O sistema verifica se os critérios de correspondência estão dentro dos limites de tolerância estabelecidos. Se esses critérios forem atendidos, a correspondência é considerada bem-sucedida.

**Relatórios:** Após concluir o processo de correspondência, o Docbits gera relatórios que mostram o status das correspondências. Esses relatórios informam sobre as faturas correspondidas com sucesso e identificam aquelas com discrepâncias.

## **Definição das Regras de Correspondência**

**Número do Item:** O número do item na fatura deve corresponder exatamente ao número do item no pedido de compra. Não há tolerância para desvios nos números de itens.

**Quantidades:** A quantidade de mercadorias entregues na fatura pode variar dentro de uma faixa de tolerância predefinida. Normalmente, uma tolerância de ±5% pode ser aceitável para contabilizar pequenas diferenças nas quantidades de entrega.

**Preços:** Desvios de preço são toleráveis até um limite estabelecido. Uma tolerância comum pode ser de ±2% do preço para aceitar pequenas diferenças nas declarações de preço que surgem de diferenças de arredondamento ou flutuações cambiais.

## **Status da Correspondência:**

* **Correspondência Completa:** Todos os pontos de dados (número do item, quantidade e preço) estão dentro dos limites de tolerância estabelecidos.
* **Correspondência Parcial:** Um ou mais pontos de dados desviam-se fora dos limites de tolerância, mas os desvios são mínimos e requerem revisão manual.
* **Sem Correspondência:** Desvios significativos em um ou mais pontos de dados que requerem correção imediata ou investigação adicional.

A definição precisa dessas regras e a definição dos limites de tolerância são cruciais para a eficiência da correspondência automática e a redução de intervenções manuais. O Docbits permite a configuração flexível desses parâmetros para atender às necessidades de várias empresas e indústrias.
