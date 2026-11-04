# Acima do Valor Máximo

<figure><img src="../../../.gitbook/assets/docbits_invoice_2.png" alt="DocBits Fatura 2"><figcaption></figcaption></figure>

Este título indica que a regra é projetada para gerenciar casos em que o total da fatura é maior do que o valor máximo que um aprovador está autorizado a lidar.

#### Configuração da Regra:

1. **Quando…**
* **Tipo de Documento é Fatura**: Esta condição garante que a regra se aplique apenas a faturas, o que é essencial para direcionar o fluxo de trabalho corretamente.
2. **E…**
* **Status do Documento é Aguardando Aprovação**: A fatura deve estar no status de "Aguardando Aprovação". Este status é crucial para garantir que a regra seja aplicada a faturas que ainda estão sendo processadas e ainda não foram finalizadas.
* **Comparar dois campos: Total do Valor Maior Que o Valor Máximo do Aprovador**: Esta condição verifica se o valor total da fatura excede o valor máximo que um aprovador está autorizado a lidar. Essa comparação também pode incluir uma configuração de tolerância, permitindo variações menores com base em critérios predefinidos.

#### Ação (Então…):

* **Atribuir usuário do campo Próximo Nível de Aprovador, usar usuário como alternativa**: Se a fatura exceder o valor máximo especificado, ela é automaticamente atribuída a um aprovador de nível superior, indicado pelo campo 'Próximo Nível de Aprovador'. Se este campo não estiver preenchido ou o usuário especificado não estiver disponível, um usuário padrão (provavelmente um administrador ou outro membro designado da equipe) é usado como alternativa para garantir que a fatura seja revisada sem atrasos.

#### Elementos da Interface:

* **Adicionar Cartão**: Esta opção permite adicionar condições ou ações adicionais à regra, fornecendo flexibilidade para lidar com cenários complexos.
* **Salvar**: Este botão salva a configuração da regra no sistema.

#### Propósito Dessa Regra:

O objetivo desta regra é garantir que faturas que excedam determinados limites financeiros sejam revisadas por aprovadores com os níveis de autorização apropriados. Isso ajuda a manter o controle financeiro e a supervisão, garantindo que os gastos sejam revisados por pessoal com os limites de aprovação necessários, protegendo assim a organização contra gastos não autorizados ou inadequados.

Esta regra, assim como a anterior, ajuda a automatizar o fluxo de trabalho, reduzindo o esforço manual e aprimorando a conformidade com as políticas financeiras da organização. É um exemplo de como a automação do fluxo de trabalho pode ser usada de forma eficaz para gerenciar processos financeiros complexos dentro de uma empresa.
