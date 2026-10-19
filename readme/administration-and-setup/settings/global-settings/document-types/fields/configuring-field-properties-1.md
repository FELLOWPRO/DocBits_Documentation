# Configurando propriedades de campo

Use **Settings → Document Types → Fields** para controlar como os campos se comportam em um tipo de documento. Selecione primeiro o tipo de documento; o exemplo abaixo mostra **Invoice** na interface em inglês.

<figure><img src="../../../../../.gitbook/assets/dbdc155-field-properties-overview-en.png" alt="Configurações de campos de Invoice em inglês, com limites de reconhecimento, pesquisa, colunas de propriedades dos campos e Save Settings"><figcaption>Configurações de campos de Invoice em uma organização sandbox do DocBits.</figcaption></figure>

## Encontrar um campo e alterar suas propriedades

1. Em **Search by Name**, digite o nome ou o rótulo do campo. Isso filtra a lista; não altera o campo.
2. Localize a linha do campo. Por exemplo, **Invoice number** tem o nome técnico `invoice_id`.
3. Ajuste os controles dessa linha e depois selecione **Save Settings**. O mesmo botão de salvar está disponível acima e abaixo da tabela.

<figure><img src="../../../../../.gitbook/assets/dbdc155-field-properties-filtered-en.png" alt="Campo Invoice number em inglês mostrando os controles Required, Read Only, Hidden, Force Validation, Use AI, OCR e Match Score"><figcaption>A linha de Invoice number após a pesquisa por `invoice_id`.</figcaption></figure>

| Controle | Para que serve |
| --- | --- |
| **Required** | Marque as informações que precisam estar presentes para a validação. Verifique o resultado da validação do documento depois de alterar esta configuração. |
| **Read Only** | Exibe um campo sem permitir que os usuários editem o valor dele. |
| **Hidden** | Mantém o campo fora da visualização normal do documento. |
| **Force Validation** | Exige que o campo passe na validação. Configure as regras detalhadas separadamente; esta caixa de seleção não é um editor de regras. |
| **Use AI** | Solicita ou interrompe a extração por IA para este campo. A linha mostra se a extração está solicitada. |
| **OCR** | Informe o limite de confiança do OCR do campo. É um número, não um interruptor de ligar/desligar nem uma configuração de idioma. |
| **Match Score** | Informe o limite de correspondência do campo. É um número, não um interruptor de ligar/desligar. |

Os controles deslizantes **OCR** e **Match Score** em **Recognition Settings** aplicam valores a toda a lista de campos. As caixas de seleção logo abaixo dos títulos das colunas aplicam **Required**, **Read Only**, **Hidden** ou **Force Validation** a toda a lista. Revise as linhas afetadas antes de selecionar **Save Settings**. **Restore Defaults** redefine a configuração dos campos; use somente quando quiser substituir as suas alterações.

## Outros controles nesta visualização

- **Create new group** e **Create field** adicionam um grupo ou um campo. Consulte [Adicionando e editando campos](adding-and-editing-fields.md).
- **Master Data Settings** abre a [configuração de dados mestres](master-data-settings.md).
- As caixas de seleção mais à esquerda selecionam campos. O menu ao lado oferece **Reassign Field Group** para os campos selecionados.
- O botão de mais de **Formula** abre o editor de fórmulas desse campo. O ícone de **informações** mostra as informações do campo. O ícone de exclusão não está disponível para campos padrão.

Para saber mais sobre validação e correspondência, consulte [Definindo validação e Match Score](setting-validation-and-match-score.md).
