# Lista de Condições de Status do Documento

<figure><img src="../../../.gitbook/assets/userlmn_e9d6da331deceed4f330358635d6b605.png" alt=""><figcaption></figcaption></figure>

**Propósito**

Este cartão é projetado para controlar ações de fluxo de trabalho com base no status atual de um documento, usando lógica condicional para acionar ou restringir certos processos. Garante que os documentos avancem apenas nos fluxos de trabalho quando atenderem aos critérios de status predefinidos.

**Componentes do Cartão**

1. **Operador**
* **Descrição**: Determina como o status do documento será avaliado em relação a uma condição especificada.
* **Opções**:
* **é**: Aciona as ações associadas se o status atual do documento corresponder a um dos status especificados.
* **não é**: Aciona as ações se o status do documento não corresponder a nenhum dos status especificados.
2. **Status (Lista)**
* **Descrição**: Lista os status específicos em relação aos quais o status atual do documento será comparado.
* **Exemplos**: "Erro", "Erro de Exportação", "Pronto para Validação", "Pronto para Revisão", "Aguardando Aprovação", "Aguardando Segunda Aprovação". Representam diferentes estágios ou condições em que um documento pode estar dentro de um processo de fluxo de trabalho.

**Funcionalidade**

* **Identificação de Status**: Identifica automaticamente o status atual de um documento à medida que ele se move pelo fluxo de trabalho do sistema ERP.
* **Avaliação de Condição**: Aplica o operador escolhido (é ou não é) ao status do documento em comparação com os status listados:
* Se **é**, verifica se o status do documento corresponde a algum status na lista.
* Se **não é**, verifica se o status do documento não aparece na lista.
* **Execução de Ação**: Dependendo do resultado da avaliação da condição:
* **Verdadeiro**: Executa ações ou fluxos de trabalho predefinidos se a condição for atendida.
* **Falso**: Pula ou aciona fluxos de trabalho alternativos se a condição não for atendida.
* **Integração de Fluxo de Trabalho**: Integra-se perfeitamente com outros componentes de fluxo de trabalho, garantindo que o manuseio de documentos seja coordenado em todo o sistema.

**Interações do Usuário**

* **Configuração e Configuração**: Os usuários configuram o cartão selecionando o operador e especificando os status relevantes. Essa configuração pode envolver menus suspensos simples ou caixas de seleção para selecionar status e operadores.
* **Monitoramento e Gerenciamento**: Os usuários podem acompanhar a atividade do cartão por meio de um painel, que fornece insights sobre as condições de status monitoradas e as ações tomadas com base nessas condições.
* **Tratamento de Erros e Alertas**: Suporta a configuração de alertas para falhas de processo ou divergências nos status esperados dos documentos, permitindo respostas rápidas a problemas operacionais.

#### Conclusão

O cartão de fluxo de trabalho "Condição de Status do Documento" é vital para garantir que os documentos sejam processados corretamente de acordo com seu status atual, aprimorando o controle e a eficiência dentro do sistema ERP. Documentar claramente este cartão no manual do sistema ajudará os usuários a implementá-lo e gerenciá-lo de forma eficaz, aproveitando sua funcionalidade para manter fluxos de trabalho de documentos suaves e em conformidade. Este cartão é particularmente útil na gestão dos ciclos de vida dos documentos e garantindo que apenas documentos que atendam a critérios específicos avancem para estágios subsequentes dos processos de negócios.
