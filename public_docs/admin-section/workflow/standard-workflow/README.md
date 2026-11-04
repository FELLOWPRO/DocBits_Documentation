# Fluxo de Trabalho Padrão

<figure><img src="../../../.gitbook/assets/docbits_workflow_purchase_order_4.svg" alt="DocBits Fluxo de trabalho Compra Pedido 4"><figcaption></figcaption></figure>

#### Visão Geral dos Componentes do Fluxo de Trabalho:

* **E-mail de Fatura AP**: O processo provavelmente começa com uma fatura recebida por e-mail.
* **DocBits**: Esta ferramenta pode ser usada para tarefas iniciais de gerenciamento de documentos, como captura e digitalização de faturas.
* **Revisão Financeira**: As faturas passam por uma revisão financeira onde decisões são tomadas sobre sua validade e precisão.

#### Etapas no Fluxo de Trabalho:

1. **Revisão Inicial**:
* As faturas são recebidas e processadas inicialmente usando o DocBits.
* Em seguida, são revisadas pela equipe financeira para garantir que sejam removidas do fluxo de trabalho se estiverem completas, ou encaminhadas para processamento adicional.
2. **Faturas de PO vs. Não-PO**:
* O fluxo de trabalho distingue entre faturas relacionadas a PO e não relacionadas a PO.
* Faturas não relacionadas a PO são encaminhadas para aprovação ou rejeição com base em critérios predefinidos como ID do fornecedor, quantidade, preço unitário e número do item.
3. **Conferência e Não Conformidade**:
* As faturas são verificadas em relação aos recibos de mercadorias para garantir que os detalhes correspondam (como ID do fornecedor e quantidade).
* Se ocorrerem não conformidades, a fatura está sujeita a uma revisão adicional e possivelmente rejeição.
4. **Revisão Financeira e do Comprador**:
* Para faturas relacionadas a PO, um processo de correspondência detalhado é conduzido envolvendo uma revisão do comprador.
* Ajustes nos pedidos de compra ou nos recibos de mercadorias podem ser necessários.
5. **Decisões Finais**:
* Faturas que passam em todas as verificações são aprovadas e integradas aos sistemas financeiros para registro.
* Faturas rejeitadas acionam notificações, e uma nova fatura pode ser solicitada pelo comprador.
6. **Integração com Infor IDM & LN+M3**:
* Faturas aprovadas provavelmente são enviadas para o Infor's IDM para gerenciamento de documentos e para o LN para anotação contábil.
* Essa integração garante que todos os registros financeiros estejam atualizados e que o fluxo de trabalho se integre perfeitamente ao sistema ERP mais amplo.

#### Pontos de Decisão:

* Ao longo do fluxo de trabalho, existem vários pontos de decisão onde uma fatura pode ser aprovada, rejeitada ou devolvida para informações adicionais. Notificações são enviadas após atrasos, garantindo processamento oportuno.

Esses Fluxos de Trabalho serão incluídos no Fluxo de Trabalho Padrão
