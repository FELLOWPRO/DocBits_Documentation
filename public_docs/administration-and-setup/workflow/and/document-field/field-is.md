# Verificar a presença e o conteúdo de um campo

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_docfield_status_v1-pt-pt.png" alt="Verificar a presença e o conteúdo de um campo, Versão 1" width="634"><figcaption><p>Versão 1</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_docfield_status_v2-pt-pt.png" alt="Verificar a presença e o conteúdo de um campo, Versão 2" width="634"><figcaption><p>Versão 2</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-docfield-status/v1/pt.mp4" %}

**Vídeo:** Cartão: Campo vazio ou não · 0:45 · [Legendas (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-docfield-status/v1/pt.vtt)

<details>

<summary>Transcrição</summary>

**Campo vazio ou não** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-docfield-status/v1/pt.mp4#t=0.25)

O cartão O campo é verifica se um campo do documento está vazio. Escolha o campo, por exemplo Ordem de compra, e o estado: vazio ou não está no documento, ou está no documento e não vazio.

**Em falta conta como vazio** · [0:18](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-docfield-status/v1/pt.mp4#t=18.716)

Um campo conta como vazio quando não tem valor, só espaços, uma caixa não marcada ou uma lista vazia. Um campo que não está no documento também conta como vazio. Se o estado corresponder, o cartão é verdadeiro. Caso contrário, é falso.

**Exemplo: sem ordem de compra** · [0:34](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-docfield-status/v1/pt.mp4#t=34.516)

Por exemplo, uma fatura sem ordem de compra vai para o aprovador das faturas sem ordem. As faturas com ordem de compra seguem o outro caminho, por exemplo a correspondência com a ordem.

</details>

## Quando utilizar

Utilize esta carta para verificar se um campo do documento está vazio ou em falta, por exemplo quando uma fatura sem número necessita de uma verificação adicional. Trata-se de uma condição; configure a ação seguinte separadamente.

**Localização:** Workflow padrão → condições adicionais (AND) → Campo do documento.

## Configuração — versão 2

| Definição | Valor do exemplo |
| --- | --- |
| Campo | `invoice_id` — número da fatura |
| Estado do campo | Vazio ou em falta (`field_empty`) |

Selecione um campo realmente configurado na sua organização. A opção `field_not_empty` verifica se o campo contém um valor.

<!-- workflow-card-practical-example-20261021 -->

## Exemplo prático

| Valor do exemplo | Resultado esperado para `field_empty` |
| --- | --- |
| Campo vazio ou em falta | Condição satisfeita |
| `DEMO-001` | Condição não satisfeita |
| Número presente mas incorreto | Condição não satisfeita — o campo continua a conter um valor |

Estes exemplos mostram os resultados esperados. Para validar o próprio número, adicione uma condição adequada ao conteúdo; esta carta verifica o estado do campo. Na versão 2, os espaços no início e no fim do texto são removidos antes de verificar se o campo está vazio.

## Vídeo de exemplo com um administrador

Quando uso esta carta, onde a encontro e como deteto números de fatura em falta. Os exemplos mostram os resultados esperados.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-field-status-admin/v1/pt.mp4" %}

[Abrir vídeo com legendas em português](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-field-status-admin/v1/pt-theme-v4.html)

[Ler transcrição](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-field-status-admin/v1/pt.txt)
