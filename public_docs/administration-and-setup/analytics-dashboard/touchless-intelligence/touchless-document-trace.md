# Document Trace

<!-- touchless-admin-video-v2-20261104:start -->
**Capítulo do vídeo (versão de revisão):** [Comparar execuções](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/pt.html#chapter=08).
<!-- touchless-admin-video-v2-20261104:end -->

Informe um ID de documento em **Document ID**, ou abra um documento de exemplo a partir de um cluster, para ver **o que aconteceu a este documento**.

O cabeçalho mostra o arquivo, o seu status (por exemplo **In progress**), a execução que você está vendo e o seu primeiro bloqueio, e um botão **Document** com o ID do documento.

<figure><img src="../../../.gitbook/assets/touchless-nova-trace-overview-pt.png" alt="Dev NOVA: caminho de processamento e pontos registrados da primeira execução de teste"><figcaption><p>Nova captura do Dev NOVA 11.0.3, 4 de novembro de 2026. A fatura de teste fictícia para na validação de campos. Classification, supplier search, header extraction e table extraction contêm pontos registrados reais; os cartões mostram o documento e o histórico de execuções. Esta é a interface do produto em execução.</p></figcaption></figure>

O **Pipeline Path** mostra 14 etapas: Intake, Classification, E-Document Validation, Supplier Identification, Text Recognition, Header Extraction, Table Extraction, Field Validation, PO Lookup, PO Line Match, Approval, Workflow Routing, Export, ERP Acknowledgement. Cada etapa tem um estado:

| Estado | Significado |
| --- | --- |
| **Passed** (verde) | A etapa foi executada sem problemas |
| **Stopped Here** (laranja) | A etapa bloqueou o documento |
| **Not reached** | Mostrado depois do primeiro bloqueio no caminho; verifique o registro da etapa para qualquer execução adicional registrada |
| **Nothing Recorded** (tracejado) | Nenhum dado foi registrado para esta etapa |
| **Not applicable** | A etapa não se aplica a este documento |

### Stage Log (registro de etapas)

O **Stage Log** abaixo do caminho lista as mesmas etapas com o que cada uma registrou. Um ponto de status e a palavra de status ficam à esquerda e à direita de cada linha.

* Cada valor é um **point chip**: um número com a sua unidade, por exemplo **Confidence 100 %**, **Threshold 60 %**, **Failed rules 0**, **8 missing fields** ou **0 mapping gaps**. As porcentagens são mostradas como `97 %`, nunca como `0.97`.
* **Details** abre a lista completa de pontos que uma etapa registrou, incluindo as alternativas que ela considerou.
* A etapa que bloqueou o documento informa o motivo, por exemplo **Field validation failed**.
* Um ponto que nenhuma etapa registrou é mostrado como **Not recorded**, nunca como um valor inventado. Pontos são números e palavras fixas, nunca texto do documento.
* **Show Raw Diagnostics** ativa os dados brutos quando o suporte os solicita.

<figure><img src="../../../.gitbook/assets/touchless-nova-trace-stage-log-pt.png" alt="Dev NOVA: registro de etapas com confiança, pontos de extração e validação de campos bloqueada"><figcaption><p>Primeira execução real: 100% de confiança na classificação, 0 candidatos a fornecedor, 1 linha de tabela e 7 lacunas de mapeamento. Passed significa que uma etapa foi executada; não prova uma correspondência de fornecedor nem que todos os valores da fatura estejam corretos. A validação de campos relata um campo obrigatório ausente.</p></figcaption></figure>

### Execuções e alterações

Use o seletor de execução para escolher uma tentativa. O Run History lista o resultado e o primeiro bloqueio. As diferenças registradas comparam a execução selecionada com a sua predecessora, não automaticamente com a execução atual. Um selo de diferença inclui a sua unidade; pontos inalterados permanecem inalterados.

O cartão Document lista o tipo de documento, o fornecedor, o número da fatura, o pedido de compra, as páginas e o método de análise registrado. Aqui, Manual reflete o tipo de documento fornecido durante a importação de teste. O valor de 100% de classificação não é, portanto, evidência independente da precisão da classificação automática.

### Ler detalhes de fornecedor e tabela

<figure><img src="../../../.gitbook/assets/touchless-nova-trace-supplier-pt.png" alt="Dev NOVA: detalhes do fornecedor separam identificadores detetados, pesquisas de dados mestres e correspondências"><figcaption><p>Esta execução encontra o nome do fornecedor na fatura e pesquisa nos dados mestres, mas não atribui nenhum fornecedor. VAT ID, IBAN, e-mail e GLN estão ausentes nesta fatura de teste. Uma correspondência ausente nos dados mestres é um diagnóstico diferente de um valor ausente na fatura.</p></figcaption></figure>

Verifique três perguntas separadas: um identificador foi encontrado no documento, ele foi pesquisado e um fornecedor foi correspondido? Uma etapa verde por si só não responde a elas.

<figure><img src="../../../.gitbook/assets/touchless-nova-trace-table-pt.png" alt="Dev NOVA: os detalhes da tabela da primeira execução relatam sete lacunas de mapeamento"><figcaption><p>Os detalhes da tabela relatam 7 lacunas de mapeamento para 1 tabela e 1 linha. Verifique o mapeamento das colunas antes de concluir que a extração falhou. O rodapé de comparação não é uma base válida para a execução inicial selecionada, que não tem predecessora.</p></figcaption></figure>

### Reconhecer um reinício real

<figure><img src="../../../.gitbook/assets/touchless-nova-trace-runs-pt.png" alt="Dev NOVA: comparação de duas execuções de teste reais com pontos de etapa inalterados"><figcaption><p>A mesma fatura de teste após um reinício manual genuíno, sem nenhum campo da fatura corrigido. Uma nova execução prova outra tentativa, não uma melhoria. Pontos inalterados mostram No change; nenhum selo de diferença foi inventado.</p></figcaption></figure>

Um reinício manual é uma intervenção humana. Somente uma conclusão bem-sucedida posterior classificaria este caso como AP Assisted. Enquanto ele permanecer em andamento, fica excluído do denominador de documentos concluídos.

Limites das evidências. Este caso não demonstra aprovação de negócio, exportação bem-sucedida nem confirmação do ERP. O antigo matcher de PO não fornece nenhum caminho de decisão registrado aqui; isto não é evidência de uma comparação com o Infor. No NOVA 11.0.3, o registro de etapas pode registrar um PO lookup aprovado depois de uma validação de campos bloqueada, enquanto o caminho o rotula como Not reached. Verifique as duas visualizações. O resumo também mostra o número da fatura como Not recorded, embora a extração o contenha; use o original e os campos extraídos para comparar valores.

## Distinguir extração de dados do sistema de origem

1. Abra a **fatura original** e compare os seus campos de cabeçalho e linhas com o que o DocBits extraiu. Use os valores anteriores à correção de uma pessoa ao investigar uma execução mais antiga. Um valor corrigido atual não estabelece o que foi extraído originalmente.
2. Leia o primeiro bloqueio no rastreamento. Uma etapa de extração aprovada significa que a etapa foi concluída; não certifica que todos os valores correspondem à fatura.
3. Para uma divergência de PO, compare os valores da fatura com os **dados do pedido realmente disponíveis para o DocBits** e com o registro correspondente no Infor. Inclua unidades, unidades de preço, quantidades e o momento da importação.
4. Registre a diferença confirmada: **fatura vs. extração**, **extração correta vs. dados de origem importados** ou **Infor vs. a sua cópia importada**. Deixe a causa em aberto se as evidências necessárias não estiverem registradas.
5. Verifique o histórico de execuções para uma correção manual, aprovação ou reinício, e o resultado final. O resultado e a causa respondem a perguntas diferentes.

**Exemplo.** A fatura e o valor extraído dizem ambos €10.00, enquanto o pedido importado diz €9.00. Isso estabelece uma divergência com os dados do pedido, não um erro de extração. Confirme qual preço foi acordado e se o próprio Infor ou a sua cópia importada precisa de correção. Se a equipe de AP reiniciar a fatura manualmente e ela terminar com sucesso, ela é AP assisted apesar da extração correta. Veja os [exemplos práticos e o cálculo](./#example-100-correct-extraction-80-ap-touchless).

**Campos ausentes repetidos.** Vários documentos que param em Field Validation estabelecem um bloqueio repetido. As causas possíveis incluem extração, um valor genuinamente ausente na fatura, uma regra de validação ou um padrão configurado ausente. Compare as evidências antes de escolher uma correção; a repetição por si só não prova nenhuma causa específica.

## Provar a extração original antes de tirar conclusões

1. Abra **Document** a partir deste rastreamento e confirme o ID do documento e a execução selecionada. Compare o número do PO original, a moeda, as quantidades, as unidades, as unidades de preço, os preços unitários, os valores das linhas e os totais relevantes com os campos e tabelas de validação.
2. Distinga os valores atuais da extração antes de uma correção. Para uma fatura já editada, use um registro histórico de campo correspondente ou evidência de extração dessa execução. Alternar entre execuções não promete a reconstrução de todos os campos e células antigos.
3. Se o valor extraído original não estiver disponível, registre-o como **not assessable**, não como correto. Defina os campos, a cobertura de linhas, a seleção da amostra e o tamanho da amostra antes de relatar um resultado independente de qualidade de extração.
4. Compare os valores do PO importado e o carimbo de data da importação com os valores atuais no Infor. Isso separa dados de origem incorretos de uma cópia desatualizada.

Bloqueios sucessivos são possíveis: a execução 1 pode parar porque um PO ainda não chegou; depois da importação, a execução 2 pode revelar uma divergência de preço. Nenhuma das duas prova que a primeira execução chegou à verificação posterior. Um reinício manual persiste após o sucesso como AP Assisted; uma rejeição final do ERP, em vez disso, tem precedência como exceção de processo. **Not recorded** significa evidência ausente, não uma verificação aprovada.

Consulte [Touchless com MCP](touchless-mcp.md) para as chamadas de ferramenta correspondentes e a classificação das ações humanas.

## Páginas relacionadas

* [Touchless Intelligence](./)
* [Supplier Diagnosis e clusters de problemas](touchless-supplier-diagnosis.md)
* [PO Matching Diagnosis](touchless-po-matching-diagnosis.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->

<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->

As cinco novas capturas de rastreamento mostram a interface localizada do Dev NOVA 11.0.3 e a mesma fatura de teste própria. Qualquer imagem separada de original versus campo continua a ser uma ilustração limitada dessa comparação.
