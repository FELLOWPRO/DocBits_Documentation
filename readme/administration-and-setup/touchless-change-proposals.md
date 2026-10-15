# Touchless Intelligence: propostas de alteração e relatórios


Uma recomendação pode vir com uma **proposta de alteração** (change proposal), uma única mudança de configuração que deve ajudar. Os administradores trabalham com ela em quatro passos:

1. **Preview** (pré-visualização): mostra a alteração (valor atual → valor proposto) e o que o DocBits espera. Nada é salvo. **Apply** (aplicar) só é possível depois que você viu uma pré-visualização.
2. **Apply**: salva exatamente a alteração pré-visualizada. Ela é registrada no log.
3. **Measure** (medir): o DocBits compara a taxa touchless do mesmo tipo de documento **antes e depois**, em períodos de igual duração. São necessários pelo menos **20 documentos** em cada período, caso contrário ele diz *not measurable*.
4. **Undo** (desfazer): desfaz a alteração.

{% hint style="warning" %}
Uma diferença entre antes e depois é uma **observação**, não a prova de uma causa. Outras coisas podem mudar ao mesmo tempo (um novo fornecedor, um pico sazonal).
{% endhint %}

**Exemplo.** Você aplica *Switch on automatic PO match and export* para faturas. Duas semanas depois, o **Change history** diz: taxa pure antes 52 % (210 documentos), depois 61 % (198 documentos). São +9 pp, com documentos suficientes para ser mensurável.


Os administradores também veem duas seções entre os indicadores principais e os gráficos:

* **Improvement requests** (solicitações de melhoria): sugestões que os usuários enviaram pelo assistente de validação, em duas abas, **Open** e **History**.
* **Learned rule proposals** (propostas de regras aprendidas): regras que o DocBits aprendeu com as correções da sua equipe, por exemplo "para o fornecedor X, substituir o valor no campo Y". Antes de criar uma, verifique os documentos nos quais ela substituiria um valor que a sua equipe tinha aceitado. A seção **After activation** mostra as correções manuais do campo de destino antes e depois de uma regra entrar em vigor.


<figure><img src="../.gitbook/assets/touchless-consulting-report.png" alt="O Consulting report com as três principais propostas, uma tabela de classificação e os problemas por domínio"><figcaption><p>O Consulting report: principais propostas, uma classificação de todos os bloqueios com documentos e impacto estimado por mês, e os problemas por domínio. Organização de exemplo com dados de demonstração; os nomes dos fornecedores são fictícios.</p></figcaption></figure>

Os administradores encontram o **Consulting report** na parte inferior da aba. Clique em **Create report** (criar relatório) para carregá-lo. Ele combina, para a sua organização:

* as **alterações com o maior efeito**, classificadas, cada uma com o domínio, o problema, a ação recomendada, o número de documentos e o efeito **estimado** por mês,
* **o domínio de cada problema** (extração, dados mestres, PO Matching, contabilização automática, configurações, processo),
* **verificações da configuração de tabelas**, por exemplo *structured table output not used* ou *table column type mismatch* por tipo de documento e coluna.

Os valores de efeito são **estimativas**. Se o relatório responder *forbidden*, a sua função não o permite.

## Páginas relacionadas

* [Touchless Intelligence](touchless-intelligence.md)
* [Diagnóstico de fornecedores e clusters de problemas](touchless-supplier-diagnosis.md)
* [Diagnóstico de PO Matching](touchless-po-matching-diagnosis.md)
