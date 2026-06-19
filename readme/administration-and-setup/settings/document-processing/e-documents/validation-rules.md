# Regras de validação

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_setup.png" alt="Configuração de validação e versões aceites"><figcaption><p>Configuração de validação e versões XRechnung aceites</p></figcaption></figure>

A página **Regras de validação** (**Documentos eletrónicos → Regras**) controla a forma como o DocBits valida as faturas eletrónicas recebidas. Baseia-se no conjunto de regras oficial **KoSIT XRechnung + ZUGFeRD** mais os códigos de resultado internos do validador, e permite substituir a gravidade de cada regra para a sua organização.

## Configuração da validação

O cartão **Configuração da validação** mostra o seu perfil de validação atual (por exemplo, *B2G — Public Sector Receiver*). Clique em **Editar respostas** para voltar a executar o assistente de configuração e alterar o padrão face ao qual valida.

## Versões XRechnung aceites

A barreira **Versões XRechnung aceites** lista todas as versões de XRechnung. Marque as versões que aceita — os documentos cujo CustomizationID fica fora desta lista são rejeitados com `VAL-VERSION-NOT-ALLOWED` antes de qualquer outra verificação. Uma lista vazia significa "aceitar tudo". Cada versão é marcada como **current**, **deprecated** ou **EOL** juntamente com a respetiva data de lançamento.

## Perfis aceites e modelo de gravidade

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_severity.png" alt="Perfis aceites e legenda de gravidade"><figcaption><p>Perfis aceites e o significado de cada gravidade</p></figcaption></figure>

Escolha que **perfis** aceita (BASIC WL, BASIC, EN 16931 / COMFORT, EXTENDED, XRECHNUNG (CIUS)) através de **Aceitar tudo** / **Limpar** e, em seguida, **Guardar**.

Cada regra de validação tem uma **gravidade** que decide o que acontece quando é acionada:

| Gravidade | Efeito |
|-----------|--------|
| **FATAL** | Para o processamento de imediato. Nenhuma camada seguinte é verificada; o documento passa a Erro. |
| **ERROR** | O documento é rejeitado. Os restantes resultados do mesmo documento continuam a ser apresentados; a notificação ao fornecedor (se ativada) é despoletada. |
| **WARNING** | Surge no relatório de validação, mas o documento prossegue normalmente no fluxo. |
| **INFO** | Apenas registo de auditoria. Sem efeito visível para o utilizador nem rejeição. |

## Substituir a gravidade das regras

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_table.png" alt="A tabela de regras de validação"><figcaption><p>A tabela completa de regras com substituição de gravidade por regra</p></figcaption></figure>

A tabela de regras lista todas as regras de validação (mais de 1.600 no total). Filtre por **Camada (Layer)**, **Perfil** ou **Versão**, ou pesquise por código ou campo. Para cada regra pode substituir a **Gravidade** no menu pendente para a ajustar à política da sua organização — por exemplo, baixar uma regra de `ERROR` para `WARNING` para que deixe de rejeitar o documento.
