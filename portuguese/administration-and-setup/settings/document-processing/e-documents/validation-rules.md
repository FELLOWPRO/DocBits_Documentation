# Validação de faturas eletrônicas

A página **Validação de faturas eletrônicas** (**Definições → Documentos eletrónicos → Validação de faturas eletrônicas**, caminho `/settings/einvoice-validation`; anteriormente chamada *Regras de validação*) controla a forma como o DocBits valida as faturas eletrónicas recebidas. Baseia-se no conjunto de regras oficial **KoSIT XRechnung + ZUGFeRD** mais os códigos de resultado internos do validador, e permite substituir a gravidade de cada regra para a sua organização.

> Esta página é para **faturas eletrónicas** (XRechnung, ZUGFeRD, Factur-X). Não é o mesmo que as **Regras de validação de dados**, que verificam os campos extraídos do documento.

## O que existe nesta página

<figure><img src="../../../../.gitbook/assets/einvoice-validation-settings-pt.png" alt="A página Validação de faturas eletrônicas com a tabela Validação para cada tipo de documento"><figcaption><p>A página Validação de faturas eletrônicas. O separador <strong>Regras e políticas</strong> começa com a tabela <strong>Validação para cada tipo de documento</strong>. Organização de exemplo.</p></figcaption></figure>

| Tema | O que faz | Quem |
| --- | --- | --- |
| [Configuração da validação e versões aceites](validation-setup.md) | O assistente de configuração, as versões XRechnung aceites, os perfis aceites e o significado de cada gravidade. | Administradores da organização |
| [Gravidade das regras](validation-rule-severities.md) | A tabela de regras: altere a gravidade de cada regra para a sua organização. | Administradores da organização |
| [Validação para cada tipo de documento](validation-per-document-type.md) | Ative a validação (**Habilitado**) e decida se uma verificação falhada pára o documento (**Bloqueio**). Cada alteração precisa de confirmação. | Administradores da organização |
| [Registo de alterações](validation-change-log.md) | Todas as alterações das definições: quando, quem, que regra, de → para. | Administradores da organização |
| [O ecrã de erro de uma fatura eletrónica rejeitada](validation-error-screen.md) | O que o utilizador vê no documento quando uma fatura é rejeitada: o XML com a linha errada marcada, a camada e o código da regra, os botões e o próximo passo. | Todos os que processam faturas |
| [Relatório de validação](validation-report.md) | O que o utilizador vê quando uma fatura falha: os resultados em linguagem simples. Abre-se a partir do documento, não desta página. | Todos os que processam faturas |
| [Próximo passo e rejeitar um documento](validation-next-step-and-reject.md) | O que fazer depois de ler o relatório, transferências do relatório e **Rejeitar documento**. | Todos os que processam faturas |
