# Menos que a Quantidade Máxima

<figure><img src="../../../.gitbook/assets/docbits_invoice.png" alt="DocBits Fatura"><figcaption></figcaption></figure>

Este título sugere que a regra ou condição sendo configurada é projetada para lidar com faturas onde o valor total é menor ou igual a um valor máximo especificado.

#### Configuração da Regra:

1. **Quando…**
* **Tipo de Documento é Fatura**: Esta condição verifica se o documento sendo processado é uma fatura. Isso é crucial para garantir que a regra se aplique apenas a faturas e não a outros tipos de documentos.
2. **E…**
* **Status do Documento é Pendente de Aprovação**: Isso especifica que a fatura deve estar em status de "Pendente de Aprovação". Esta verificação de status garante que a regra se aplique apenas a faturas aguardando aprovação.
* **Comparar dois campos: Valor Total Menor ou Igual ao Valor Máximo do Aprovador**: Esta condição compara o valor total da fatura com o valor máximo autorizado de um aprovador. Se o valor total da fatura for menor ou igual a este valor máximo, a regra avança para o próximo passo. Isso provavelmente inclui um nível de tolerância que permite pequenas variações dentro de limites especificados.

#### Ação (Então…):

* **Atribuir usuário do campo Nome do Aprovador, usar usuário User como alternativa**: Se as condições especificadas forem atendidas, a fatura é automaticamente atribuída a um aprovador cujo nome é especificado em um campo. Se este campo estiver vazio ou indisponível, um usuário padrão (provavelmente um administrador ou outro membro designado da equipe) é atribuído como alternativa para lidar com a aprovação.

#### Elementos da Interface:

* **Adicionar Cartão**: Este botão provavelmente permite aos usuários adicionar mais condições ou ações à regra, aumentando a flexibilidade e especificidade do fluxo de trabalho.
* **Salvar**: Salva a regra configurada no sistema.

#### Propósito Dessa Regra:

Esta configuração é projetada para otimizar o processo de aprovação de faturas, direcionando automaticamente as faturas para o aprovador apropriado com base no valor e garantindo que apenas aquelas dentro de um determinado limite sejam tratadas dessa maneira automatizada. Isso ajuda a gerenciar controles financeiros e acelera o fluxo de trabalho, reduzindo as verificações manuais para cada fatura.
