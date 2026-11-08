# Métricas e cálculo

<!-- touchless-admin-video-v2-20261104:start -->
**Capítulo do vídeo (versão de revisão):** [Calcular as taxas](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/pt.html#chapter=03).
<!-- touchless-admin-video-v2-20261104:end -->

### Extração correta e um processo touchless são coisas diferentes

**O DocBits pode ler corretamente todos os valores de uma fatura e, ainda assim, a fatura precisar de atenção de AP porque os dados do sistema de origem divergem.** AP significa Accounts Payable, a equipa que processa faturas de fornecedores. Verifique estas duas perguntas separadamente:

| Pergunta | Comparar | O que o resultado lhe diz |
| --- | --- | --- |
| **O DocBits leu o documento corretamente?** | A fatura original com os campos de cabeçalho e as linhas de tabela extraídos, antes de qualquer correção manual | Qualidade da extração: o valor extraído corresponde ao que está efetivamente na fatura? |
| **O processo poderia ter terminado sem uma intervenção?** | A fatura extraída corretamente com o pedido de compra e os dados mestres fornecidos pelo Infor ERP, juntamente com o histórico de processamento registado | Automação do processo: as verificações, o matching e a exportação configurados poderiam ter terminado sem uma correção ou um reinício? |

Um valor diferente no Infor não lhe diz, por si só, qual dos lados está errado. Verifique a fatura, a encomenda acordada e os dados efetivamente importados para o DocBits. A origem pode estar incorreta, a importação pode estar desatualizada ou o fornecedor pode ter faturado outro valor.

{% hint style="info" %}
**A taxa touchless mede o processo, não a exatidão da extração.** Um documento AP assisted não prova um erro de extração do DocBits. Inversamente, uma etapa de extração aprovada ou uma pontuação de confiança elevada não prova que todos os valores estão corretos. Para isso, compare o documento original com os valores extraídos.
{% endhint %}

Cada documento termina em exatamente **um** resultado:

| Resultado             | Significado                                                                                         | Conta na taxa                                                                              |
| --------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Pure touchless**    | Processado da importação à exportação **sem qualquer envolvimento humano**                           | Sim, como sucesso                                                                          |
| **AP touchless**      | Correu automaticamente e uma pessoa deu apenas a **aprovação de negócio**. Não foi precisa correção  | Sim, como sucesso                                                                          |
| **AP assisted**       | Terminou com sucesso, mas uma pessoa teve de **corrigir um campo, reiniciar o documento** ou intervir de outra forma; isto pode ser necessário mesmo quando a extração estava correta | Sim, fora do numerador touchless; por si só não identifica a causa |
| **Process exception** | Terminou num **erro**, foi **rejeitado**, foi **recusado pelo ERP** ou **ficou parado** no pipeline | Sim, como falha                                                                             |
| **In progress**       | Ainda não terminou                                                                                  | **Não**. Ainda não tem resultado                                                           |
| **Not eligible**      | Eliminado, arquivado, um documento de teste ou um tipo de documento excluído                        | **Não**                                                                                    |

A **taxa AP touchless**, incluindo documentos que só tiveram aprovação, é:

```
rate = (Pure touchless + AP touchless)
       ÷ (Pure touchless + AP touchless + AP assisted + Process exception)
```

Aqui, **AP touchless** no numerador é o resultado do documento "apenas aprovação". A **percentagem AP touchless** do dashboard é a taxa combinada: documentos pure mais documentos só com aprovação. **Não some as duas percentagens apresentadas.** A taxa pure usa apenas documentos pure no numerador, com o mesmo denominador.

Os documentos ainda **in progress** ou **not eligible** nunca entram no cálculo. Isto protege a taxa: um documento que chegou há cinco minutos não a pode puxar para baixo.

{% hint style="info" %}
**Um toque conta para sempre.** Assim que uma pessoa toca num documento, ele continua contado como tocado, mesmo que uma execução automática posterior não tivesse precisado de ninguém. **Reiniciar um documento não o torna novamente touchless.** A taxa reflete o trabalho que aconteceu.
{% endhint %}

### Cálculo de exemplo (números ilustrativos)

Em 30 dias, chegaram 200 documentos:

| Resultado                     | Documentos |
| ----------------------------- | ---------- |
| Pure touchless                | 120        |
| AP touchless                  | 30         |
| AP assisted                   | 30         |
| Process exception             | 10         |
| In progress                   | 8          |
| Not eligible (documentos de teste) | 2      |

* Denominador: 120 + 30 + 30 + 10 = **190**. Os 8 documentos in progress e os 2 not eligible ficam de fora.
* **Pure touchless**: 120 ÷ 190 = **63,2 %**
* Parte apenas com **aprovação**: 30 ÷ 190 = **15,8 %**. Esta é a parte desse resultado, não a taxa AP touchless combinada.
* **Taxa AP touchless**: (120 + 30) ÷ 190 = **78,9 %**

O separador mostra um **objetivo** (70 % a menos que a sua organização use outro). Neste exemplo, a taxa AP combinada está acima de 70 %, enquanto a taxa pure de 63,2 % está abaixo. Compare o objetivo com a taxa identificada pelo cartão ou gráfico relevante.

Clique em **How touchless is calculated** no canto superior direito para abrir esta explicação dentro do DocBits, com os números do seu próprio período (documentos no período, ainda in progress, excluídos, medidos).

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/touchless-report-methodology-en-20261104.png" alt="População de formação atual: 201 faturas elegíveis concluídas, nenhuma ainda em processamento ou excluída. As 107 faturas totalmente automáticas dão 53,2%; somando 11 faturas só com aprovação chega-se a 118 e 58,7%. Estas taxas de processo não medem a exatidão da extração."><figcaption><p>População de formação atual: 201 faturas elegíveis concluídas, nenhuma ainda em processamento ou excluída. As 107 faturas totalmente automáticas dão 53,2%; somando 11 faturas só com aprovação chega-se a 118 e 58,7%. Estas taxas de processo não medem a exatidão da extração.</p></figcaption></figure>
<!-- English source image: touchless-report-methodology-en-20261104.png -->

### Exemplo: extração 100% correta, 80% AP touchless

Suponha que uma revisão das faturas originais e dos seus valores extraídos confirma que **todas as 100 faturas concluídas e elegíveis foram extraídas corretamente**. Os seus resultados de processamento são:

| O que aconteceu | Documentos | Resultado |
| --- | --- | --- |
| Fatura e dados de origem coincidiram; todo o processo terminou automaticamente | 70 | Pure touchless |
| Fatura e dados de origem coincidiram; só foi precisa aprovação de negócio | 10 | AP touchless (resultado de apenas aprovação) |
| Os dados da fatura foram extraídos corretamente, mas os dados do Infor importados divergiam. AP esclareceu a discrepância e reiniciou manualmente os documentos no DocBits depois de os dados de origem serem corrigidos; terminaram então com sucesso | 20 | AP assisted |

* **Documentos extraídos corretamente nesta amostra revista:** 100 ÷ 100 = **100%**.
* **Taxa pure touchless:** 70 ÷ 100 = **70%**.
* **Taxa AP touchless:** (70 + 10) ÷ 100 = **80%**.

Não há contradição: a extração estava correta em todas as faturas, enquanto 20 precisaram de uma intervenção de processamento devido aos dados de origem. **A cifra de 100% de extração é um resultado ilustrativo de uma revisão de documentos separada**, não um KPI adicional mostrado por este dashboard. Não a calcule apenas a partir dos resultados touchless.

### Exemplos: o que AP teve efetivamente de fazer?

Os casos seguintes são ilustrativos, não são os documentos individuais por trás das capturas de ecrã. Os resultados com sucesso pressupõem que o processamento terminou, incluindo a confirmação do ERP quando necessária.

| Caso | Fatura original / extração do DocBits / dados de origem | Ação de AP e resultado | Onde investigar |
| --- | --- | --- | --- |
| **Erro de extração** | Número de PO `45001234` / extraído incorretamente como `45001284` / a encomenda correta `45001234` existe no Infor | AP corrige o número extraído; a fatura termina como **AP assisted** | Extração deste fornecedor |
| **Discrepância no sistema de origem** | Preço unitário 10,00 € / extraído corretamente 10,00 € / a encomenda importada do Infor indica 9,00 €, fora da tolerância configurada | AP confirma que 10,00 € é o preço acordado, providencia a correção da encomenda e reinicia manualmente a fatura no DocBits; termina como **AP assisted** | Dados da encomenda no Infor e a sua importação |
| **Atraso na importação** | O número de PO está correto na fatura e no DocBits / a encomenda existe no Infor mas ainda não chegou ao DocBits | Se uma importação posterior e uma nova tentativa terminarem automaticamente sem intervenção humana nem aprovação registadas, o resultado pode continuar **Pure touchless**. Um reinício manual seguido de sucesso dá **AP assisted** | Momento da importação e o histórico real de execuções |
| **Rejeição do ERP** | A extração está correta, mas o ERP recusa o documento exportado | **Process exception** enquanto classificado como rejeição terminal do ERP, mesmo que alguém tenha intervindo antes | Rejeição do ERP e evidência da exportação |

**Mesmo uma pequena correção registada ou um reinício manual conta como intervenção.** AP assisted significa "uma pessoa ajudou a processar o documento"; não é o nome de um assistente de IA separado. Um problema nos dados de origem e um problema de extração podem, por isso, ter o mesmo resultado mas exigir correções diferentes.

A classificação usa os eventos que o DocBits registra. Não assuma que o trabalho feito apenas no Infor, sem um evento correspondente registado no DocBits, é automaticamente contado como intervenção de AP. Mantenha também esse trabalho no diagnóstico.

### Que ações de AP contam como intervenção?

O seguinte pressupõe uma conclusão com sucesso, incluindo a confirmação do ERP necessária. O que conta é a ação registada e o seu autor, não quanto tempo o trabalho demorou.

| Ação | Efeito no resultado do documento |
| --- | --- |
| Abrir, ler, filtrar, comparar ou pré-visualizar | Por si só não cria uma intervenção de processamento; Pure Touchless continua possível |
| Dar aprovação de negócio, incluindo uma segunda aprovação | AP Touchless, se não houve intervenção de processamento |
| Alterar e guardar um campo de cabeçalho ou uma célula de tabela | AP Assisted; mesmo uma única correção guardada conta |
| Validar e avançar manualmente um documento, mesmo sem corrigir um valor | AP Assisted; a validação manual é distinta da aprovação apenas |
| Reiniciar manualmente o processamento ou a exportação | AP Assisted; uma execução automática posterior não elimina a intervenção |
| Nova tentativa automática do sistema ou escrita automática do workflow | Por si só não cria uma intervenção humana; os toques humanos anteriores mantêm-se |
| Corrigir dados apenas no Infor | O trabalho externo não é automaticamente um evento registado no DocBits; documente-o à parte e inspecione a ação subsequente no DocBits |
| Rejeição final do ERP depois de uma correção | Process exception tem precedência; a intervenção mantém-se no histórico |

Um clique em Save sem evidência de um valor alterado não prova uma correção. Verifique se também desencadeou uma validação manual ou um reinício.

### O rótulo AP tem dois significados

| Localização | Significado |
| --- | --- |
| Percentagem AP do cabeçalho | Combinada Pure + apenas aprovação: (120 + 30) / 190 = 78,9% |
| Contagem de documentos por baixo dessa percentagem no relatório atual | Combinada Pure + apenas aprovação: 150 = 120 + 30 |
| Categoria de resultado AP Touchless, como o bucket MCP `AP_TOUCHLESS` | Categoria separada de apenas aprovação: 30 / 190 = 15,8% |
| Linha AP azul na atual [captura de ecrã da tendência do dashboard](touchless-dashboard.md) | Taxa combinada Pure + apenas aprovação em cada ponto, usando a população desse ponto |

As categorias de resultado final somam 100% da população medida. As percentagens Pure e AP combinada do cabeçalho sobrepõem-se e não devem ser somadas.

### Quão atuais são os números

Os resultados são **recalculados a cada 15 minutos**. O resultado de um documento pode ainda mudar depois de aparecer pela primeira vez: o ERP pode confirmar uma exportação horas mais tarde. A linha **Data as of …** na parte inferior do separador mostra quando os números foram calculados pela última vez.




## Páginas relacionadas

* [Touchless Intelligence](./)
* [Utilizar o dashboard](touchless-dashboard.md)
* [Exemplos resolvidos: preço e quantidade](touchless-examples.md)
* [Supplier Diagnosis e clusters de problemas](touchless-supplier-diagnosis.md)
* [Diagnóstico de PO Matching](touchless-po-matching-diagnosis.md)
* [Document Trace](touchless-document-trace.md)
* [Change Proposals e relatórios](touchless-change-proposals.md)
* [Explicar e melhorar o Touchless com MCP](touchless-mcp.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
