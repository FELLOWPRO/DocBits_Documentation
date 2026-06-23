# Documentos eletrónicos

O DocBits valida as faturas eletrónicas recebidas (e-invoices) face aos padrões oficiais — **XRechnung**, **ZUGFeRD** e **Factur-X** — e encaminha quaisquer problemas detetados para o responsável adequado. O grupo de definições **Documentos eletrónicos** (em **Processamento de documentos**) tem duas páginas:

* **[Regras de validação](validation-rules.md)** — escolha que versões e perfis de fatura eletrónica aceita e defina a gravidade de cada regra de validação para a sua organização.
* **[Encaminhamento de notificações](notification-routing.md)** — associe os resultados de validação ao agente do AI Workforce que os deve tratar.

Em conjunto, permitem decidir **o que conta como um problema** numa fatura eletrónica recebida e **quem trata disso**.

## Ativar ou desativar a validação de faturas eletrónicas

As duas páginas de Documentos eletrónicos só têm efeito depois de a **validação de faturas eletrónicas estar ativada para o tipo de documento**. O interruptor está no próprio tipo de documento, não no menu Documentos eletrónicos.

Vá a **Definições → Tipos de documento → Fatura → Definições avançadas** e abra a secção **Validação de faturas eletrónicas**.

<figure><img src="../../../../.gitbook/assets/edoc_enable_validation_toggle.png" alt="Os interruptores de validação de faturas eletrónicas no tipo de documento Fatura"><figcaption><p>Ative ou desative a validação de faturas eletrónicas por tipo de documento, com notificação opcional ao fornecedor</p></figcaption></figure>

* **Validar faturas eletrónicas recebidas** — o interruptor principal. Quando **ativado**, cada fatura carregada é verificada segundo as regras Schematron KoSIT XRechnung e as verificações semânticas L0 (PDF/A-3) e L4 (IBAN/IVA), usando as gravidades que definiu na página [Regras de validação](validation-rules.md). As faturas inválidas são bloqueadas. Quando **desativado**, as faturas ignoram totalmente a validação de faturas eletrónicas e as páginas Regras de validação e Encaminhamento de notificações não têm efeito.
* **Notificar o fornecedor em caso de rejeição** — aparece assim que a validação é ativada. Quando **ativado**, uma fatura rejeitada gera um e-mail ao fornecedor com os campos em falta ou incorretos para que possa reemiti-la. Quem recebe e trata cada resultado configura-se na página [Encaminhamento de notificações](notification-routing.md).

> A validação de faturas eletrónicas é configurada **por tipo de documento**. Atualmente aplica-se ao tipo de documento **Fatura**; ative-a em cada tipo de documento que deva ser validado.
