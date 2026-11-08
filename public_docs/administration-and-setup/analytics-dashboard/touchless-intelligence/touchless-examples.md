# Exemplos práticos: preço e quantidade

<!-- touchless-admin-video-v2-20261104:start -->
**Capítulo do vídeo (versão de revisão):** [Acompanhar um documento](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/pt.html#chapter=07).
<!-- touchless-admin-video-v2-20261104:end -->

## Exemplo prático: extração correta, dados do Infor diferentes

Este é um caso ilustrativo, separado das capturas de tela. A fatura mostra **10 unidades a €10.00 cada**, total **€100.00**. O DocBits extrai os três valores corretamente. O pedido importado do Infor mostra **10 unidades a €9.00 cada**, total **€90.00**. Suponha que as verificações de correspondência configuradas bloqueiem essa diferença de preço.

1. **Verifique a extração:** compare a fatura original com a quantidade, o preço unitário e o valor da linha extraídos. Eles coincidem, portanto não há erro de extração demonstrado para esses valores.
2. **Verifique a origem:** compare o pedido importado com o pedido atual do Infor, incluindo a unidade de preço e o momento da importação. Uma importação desatualizada e um pedido incorreto no Infor exigem correções diferentes.
3. **Esclareça o valor do negócio:** neste exemplo, o setor de compras confirma que €10.00 foi acordado e corrige o pedido no Infor. Se €9.00 fosse o preço acordado, seria a fatura do fornecedor que precisaria de esclarecimento.
4. **Verifique a importação corrigida:** confirme que os valores corretos do pedido chegaram realmente ao DocBits antes de tentar novamente.
5. **Registre a ação de AP:** a equipe de AP reinicia esta fatura manualmente no DocBits; após a conclusão bem-sucedida, ela é **AP assisted**. Uma extração correta e um processo não touchless podem ser verdadeiros ao mesmo tempo.
6. **Verifique as faturas posteriores:** confirme que a correspondência e a exportação agora terminam sem outra correção ou reinício. A fatura tratada anteriormente continua tratada; as faturas posteriores fornecem evidências de melhoria.

{% hint style="warning" %}
Não altere um €10.00 extraído corretamente para €9.00 apenas para corresponder a um pedido incorreto, nem amplie uma tolerância somente para esconder a divergência. Confirme o valor acordado e corrija os dados ou a configuração responsáveis. Um bloqueio de correspondência identifica onde o processo parou, não quem o causou.
{% endhint %}

Consulte o [Touchless Intelligence](./) para o exemplo separado de qualidade de extração e para o cálculo do AP touchless, e o [Document Trace](touchless-document-trace.md) para as evidências a comparar.

## Três PO de demonstração próprios: valores correspondentes, preço e quantidade

Estes PO foram criados especificamente no **Dev**. O fornecedor, o item e as faturas são fictícios. Cada fatura contém **10 unidades × €10 = €100 líquidos**. Os cartões contêm recortes genuínos da interface em inglês e detalhes numéricos ampliados. Eles não mostram uma conexão Infor real de cliente, uma extração comprovada nem um processo automático de fatura concluído com sucesso.

| Caso | Fatura | PO importado | O que a comparação estabelece |
| --- | --- | --- | --- |
| PO01 / RE01: valores correspondentes | 10 × €10 = €100 | 10 × €10 = €100 | Os valores de origem coincidem; o Pure Touchless ainda precisa de extração correta e de conclusão confirmada sem intervenção nem aprovação |
| PO02 / RE02: divergência de preço | 10 × €10 = €100 | 10 × €9 = €90 | Diferença de €10 na linha; o preço unitário difere em cerca de 11.11% em relação ao preço do PO. As regras ativas reais decidem se isso bloqueia |
| PO03 / RE03: divergência de quantidade | 10 × €10 = €100 | 8 × €10 = €80 | 2 unidades adicionais, 25% em relação à quantidade encomendada. Verifique a quantidade aberta/recebida e a quantidade de comparação configurada |

<figure><img src="../../../.gitbook/assets/touchless-owned-po-match-pt.png" alt="Cartão de explicação FELLOW com o pedido de compra real PO01 em Dev mostrando quantidade dez, preço unitário dez e valor cem"><figcaption><p>Valores correspondentes no PO01 fictício. A linha nativa ampliada mostra quantidade, preço unitário e valor. A coincidência por si só não prova uma extração correta nem Pure Touchless.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/touchless-owned-po-price-pt.png" alt="Cartão de explicação FELLOW com o pedido de compra real PO02 em Dev mostrando dez unidades a nove e um valor de noventa contra um valor de fatura de cem"><figcaption><p>Exemplo de preço PO02: o pedido importado mostra realmente 10 × 9 = 90, em comparação com 10 × 10 = 100 na fatura fictícia. Verifique o preço acordado, a unidade de preço e a importação. Uma intervenção humana registrada seguida de conclusão bem-sucedida é AP Assisted.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/touchless-owned-po-quantity-pt.png" alt="Cartão de explicação FELLOW com o pedido de compra real PO03 em Dev mostrando oito unidades a dez, valor oitenta, contra dez unidades faturadas"><figcaption><p>Exemplo de quantidade PO03: o PO importado contém 8 unidades, a fatura 10. A quantidade recebida está vazia neste teste e não comprova nenhuma entrega. Esses cartões explicam a comparação; eles não comprovam uma correspondência bem-sucedida.</p></figcaption></figure>

## Páginas relacionadas

* [Touchless Intelligence](./)
* [Métricas e cálculo](../../touchless-metrics.md)
* [Usar o painel](touchless-dashboard.md)
* [Supplier Diagnosis e clusters de problemas](../../touchless-supplier-diagnosis.md)
* [PO Matching Diagnosis](../../touchless-po-matching-diagnosis.md)
* [Document Trace](touchless-document-trace.md)
* [Change Proposals e relatórios](touchless-change-proposals.md)
* [Explicar e melhorar o Touchless com MCP](touchless-mcp.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
