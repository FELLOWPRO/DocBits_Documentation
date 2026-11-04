# Correspondência Automática de Dados de Ordem de Compra

Docbits é um sistema avançado projetado para automatizar a correspondência de dados de ordens de compra (POs) com documentos de fatura recebidos. Essa ferramenta é especificamente projetada para o gerenciamento eficiente e processamento de dados de fatura dentro de sistemas ERP. Esta documentação explica o básico da correspondência automática através do Docbits e define as regras específicas necessárias para uma correspondência bem-sucedida.

## **Princípios Fundamentais da Correspondência Automática no Docbits**

**Extração de Dados:** O Docbits inicia o processo extraindo dados relevantes de documentos de fatura digitalizados. Tipicamente, esses dados incluem números de item, quantidades e preços unitários de cada linha de fatura. A precisão dessa extração é crucial, pois forma a base para o processo de correspondência subsequente.

**Comparação com Dados da Ordem de Compra:** Os dados extraídos são comparados com as informações correspondentes nas ordens de compra armazenadas. O Docbits verifica se os números de item, quantidades e preços correspondem aos das POs. Para uma correspondência bem-sucedida, os dados nas faturas devem corresponder aos dados nas ordens de compra, considerando os limites de tolerância definidos.

**Correspondência Automática:** Com base nos resultados da comparação, o Docbits realiza a correspondência. O sistema verifica se os critérios de correspondência estão dentro dos limites de tolerância definidos. Se esses critérios forem atendidos, a correspondência é considerada bem-sucedida.

**Relatórios:** Após concluir o processo de correspondência, o Docbits gera relatórios que mostram o status das correspondências. Esses relatórios informam sobre faturas correspondentes com sucesso e identificam aquelas com discrepâncias.

## **Definição de Regras de Correspondência**

**Número do Item:** O número do item na fatura deve corresponder exatamente ao número do item na ordem de compra. Não há tolerância para desvios nos números dos itens.

**Quantidades:** A quantidade de mercadorias entregadas na fatura pode variar dentro de uma faixa de tolerância predefinida. Tipicamente, uma tolerância de ±5% pode ser aceitável para considerar pequenas diferenças nas quantidades entregues.

**Preços:** Desvios de preço são toleráveis até um limite definido. Uma tolerância comum pode ser de ±2% do preço para aceitar pequenas diferenças nas declarações de preço que surgem de diferenças de arredondamento ou flutuações cambiais.

## **Status da Correspondência:**

* **Correspondência Completa:** Todos os pontos de dados (número do item, quantidade e preço) estão dentro dos limites de tolerância definidos.
* **Correspondência Parcial:** Um ou mais pontos de dados desviam fora dos limites de tolerância, mas as discrepâncias são mínimas e requerem revisão manual.
* **Sem Correspondência:** Desvios significativos em um ou mais pontos de dados que exigem correção imediata ou investigação adicional.

A definição precisa dessas regras e a configuração dos limites de tolerância são cruciais para a eficiência da correspondência automática e a redução das intervenções manuais. O Docbits permite a configuração flexível desses parâmetros para atender às necessidades de várias empresas e indústrias.
