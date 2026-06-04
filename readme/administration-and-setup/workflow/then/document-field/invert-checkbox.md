# Invert Checkbox

<figure><img src="../../../../.gitbook/assets/image (280).png" alt=""><figcaption></figcaption></figure>

## **Propósito:**

Este cartão de fluxo de trabalho foi concebido para inverter o estado atual de um campo de caixa de verificação. Se a caixa de verificação estiver assinalada (true), passará a não assinalada (false), e vice-versa. A inversão ocorre com base nas condições definidas nas secções **"Where"** e **"And Sections."** Este cartão ajuda a automatizar fluxos de trabalho em que uma condição exige alternar uma caixa de verificação com base em critérios específicos.

## **Componentes do cartão:**

1. **Field Name**
   * **Descrição**: Especifica o campo de caixa de verificação a inverter.&#x20;
   * **Detalhe**: O campo de caixa de verificação selecionado terá o seu estado alternado de true para false ou de false para true com base no seu estado atual.

## **Funcionalidade:**

* **Avaliação da condição**: O sistema avalia as condições definidas nas secções **"Where"** e **"And Sections"**:
  * Se **ambas as condições forem verdadeiras**, a ação da **"Then Section"** será executada, o que neste caso significa que o campo de caixa de verificação será alternado.
  * Se **alguma das condições for falsa**, o cartão não será executado e não será feita qualquer alteração ao campo de caixa de verificação.
* **Execução da ação**: Se as condições nas secções **"Where"** e **"And Sections"** forem avaliadas como verdadeiras, o estado do campo de caixa de verificação será invertido:
  * Se a caixa de verificação estiver assinalada (true), passará a não assinalada (false).
  * Se a caixa de verificação estiver não assinalada (false), passará a assinalada (true).

## **Configuração:**

Para configurar este cartão, os utilizadores precisam de:

1. **Selecionar o campo de caixa de verificação** (Field Name) que será invertido. Os campos de caixa de verificação disponíveis no documento são listados para seleção.
2. O campo de caixa de verificação só será invertido se as condições nas secções **"Where"** e **"And Sections"** forem verdadeiras.

## **Conclusão:**

O cartão de fluxo de trabalho **"Invert checkbox \[Field Name]"** oferece uma ferramenta de automação simples mas poderosa para alternar valores de caixas de verificação com base em condições específicas. Ao reduzir a necessidade de ajustes manuais das caixas de verificação, este cartão aumenta a eficiência no processamento de documentos e assegura consistência ao longo dos fluxos de trabalho.
