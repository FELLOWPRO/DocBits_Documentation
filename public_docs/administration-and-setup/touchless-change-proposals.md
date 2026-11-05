# Touchless Intelligence: propostas de alteração e relatórios

<!-- touchless-admin-video-v2-20261104:start -->
**Capítulo do vídeo (versão de revisão):** [Propostas e histórico](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/pt.html#chapter=10).
<!-- touchless-admin-video-v2-20261104:end -->


Uma recomendação pode vir com uma **proposta de alteração** (change proposal), uma única mudança de configuração que deve ajudar. Os administradores trabalham com ela em quatro passos:

1. **Preview** (pré-visualização): mostra a alteração (valor atual → valor proposto) e o que o DocBits espera. Nada é salvo. **Apply** (aplicar) só é possível depois que você viu uma pré-visualização.
2. **Apply**: salva exatamente a alteração pré-visualizada. Ela é registrada no log.
3. **Measure** (medir): o DocBits compara a taxa touchless do mesmo tipo de documento **antes e depois**, em períodos de igual duração. São necessários pelo menos **20 documentos** em cada período, caso contrário ele diz *not measurable*.
4. **Desfazer**: restaura a definição se a proposta o suportar. Verifique disponibilidade e valor restaurado.

{% hint style="warning" %}
Uma diferença entre antes e depois é uma **observação**, não a prova de uma causa. Outras coisas podem mudar ao mesmo tempo (um novo fornecedor, um pico sazonal).
{% endhint %}

**Exemplo ilustrativo.** Após uma alteração de configuração, AP passa de 52 % (210 documentos) a 61 % (198), mais 9 pontos. Inclui Pure e apenas aprovação, não precisão de extração. Cada período comparável exige pelo menos 20 documentos concluídos elegíveis. Antes/depois é observação, não causalidade. Uma correção Infor exige verificar importação e novas faturas; não presuma uma alteração DocBits registada.


Os administradores também veem duas seções entre os indicadores principais e os gráficos:

* **Improvement requests** (solicitações de melhoria): sugestões que os usuários enviaram pelo assistente de validação, em duas abas, **Open** e **History**.
* **Learned rule proposals** (propostas de regras aprendidas): regras que o DocBits aprendeu com as correções da sua equipe, por exemplo "para o fornecedor X, substituir o valor no campo Y". Antes de criar uma, verifique os documentos nos quais ela substituiria um valor que a sua equipe tinha aceitado. A seção **After activation** mostra as correções manuais do campo de destino antes e depois de uma regra entrar em vigor.


<figure><img src="../.gitbook/assets/touchless-consulting-report-pt.png" alt="O Consulting report com as três principais propostas, uma tabela de classificação e os problemas por domínio"><figcaption><p>O Consulting report: principais propostas, uma classificação de todos os bloqueios com documentos e impacto estimado por mês, e os problemas por domínio. Organização de exemplo com dados de demonstração; os nomes dos fornecedores são fictícios.</p></figcaption></figure>

Os administradores encontram o **Consulting report** na parte inferior da aba. Clique em **Create report** (criar relatório) para carregá-lo. Ele combina, para a sua organização:

* as **alterações com o maior efeito**, classificadas, cada uma com o domínio, o problema, a ação recomendada, o número de documentos e o efeito **estimado** por mês,
* **o domínio de cada problema** (extração, dados mestres, PO Matching, contabilização automática, configurações, processo),
* **verificações da configuração de tabelas**, por exemplo *structured table output not used* ou *table column type mismatch* por tipo de documento e coluna.

Os valores de efeito são **estimativas**. Se o relatório responder *forbidden*, a sua função não o permite.

Ferramentas e classificação de ações em [Touchless com MCP](touchless-mcp.md).

## Páginas relacionadas

* [Touchless Intelligence](touchless-intelligence.md)
* [Diagnóstico de fornecedores e clusters de problemas](touchless-supplier-diagnosis.md)
* [Diagnóstico de PO Matching](touchless-po-matching-diagnosis.md)

<!-- Alignment 2026-11-04: correct extraction is distinct from process Touchless; KPI numerator and denominator verified. -->

<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->
