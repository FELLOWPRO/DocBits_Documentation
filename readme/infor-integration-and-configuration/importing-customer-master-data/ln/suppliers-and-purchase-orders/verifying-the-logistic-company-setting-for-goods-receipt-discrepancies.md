# Verificar a Configuração da Empresa Logística em Divergências de Recebimento de Mercadorias

Ao trabalhar com processos de compras de grande escala, não é incomum encontrar situações em que determinados dados não coincidem como esperado. Por exemplo, você pode ver uma mensagem de erro como:

**“Delivery Note L1234, Order Type: Purchase, Order 100000211, Position 10, Subsequent Number 1, Logistic Company&#x20;**<mark style="color:red;">**XXXX**</mark>**, Goods Receipt WE0000293 and Entry Position 10 not found in direct debit.”**

Esse tipo de mensagem costuma indicar que há uma divergência ou falta de informações relacionadas à configuração da sua empresa logística. A empresa logística é um elemento essencial dos sistemas de planejamento de recursos empresariais (ERP), especialmente em cadeias de suprimentos complexas que abrangem várias entidades legais ou logísticas.

**Por que isso acontece?**

Em ambientes com várias entidades, cada transação (compra, recebimento de mercadorias ou início de pagamentos) deve ser atribuída corretamente à empresa logística certa. A “empresa logística” é mais do que um simples identificador: ela determina qual depósito, centro de distribuição ou nó da rede de suprimentos é responsável pelas tarefas de pedido e de atendimento. Se o número da empresa não corresponder à entidade esperada, processos subsequentes, como a verificação do recebimento de mercadorias ou as liquidações por débito direto, podem falhar.

## **Verificações principais a realizar:**

### 1. Verifique a empresa logística atribuída:

Consulte os registros de dados mestres para garantir que a empresa logística referenciada (neste caso, <mark style="color:red;">XXXX</mark>) seja a entidade correta para o pedido em questão. O <mark style="color:red;">XXXX</mark> é o código de empresa correto para tratar compras desse fornecedor ou dessa linha de produtos específica?

### 2. Revise a configuração do pedido de compra (PO):

Confirme se a empresa logística do pedido de compra está alinhada ao local de recebimento pretendido. Às vezes, um pedido é criado sob uma empresa logística, mas as mercadorias são recebidas sob outra, quando a configuração não é consistente.

### 3. Compare o recebimento de mercadorias com os registros do depósito:

Observe o recebimento de mercadorias (WE0000293) e verifique se ele foi lançado no depósito da empresa correta. Se o depósito pertencer a outra empresa logística, pode ser necessário corrigir a configuração ou processar uma transferência para a entidade correta.

### 4. Verifique a integração e a consistência dos dados mestres:

Os pontos de integração entre diferentes módulos (Compras, Armazenagem, Financeiro) dependem de códigos consistentes. Certifique-se de que a empresa logística esteja definida de maneira uniforme em todos os módulos relevantes.

### 5. Consulte a documentação e o suporte:

Se as verificações internas não resolverem o problema, consulte a documentação do seu sistema ou entre em contato com a equipe de suporte do ERP. Ela poderá ajudar a verificar se o código da empresa logística está configurado corretamente ou se são necessárias etapas de configuração adicionais.
