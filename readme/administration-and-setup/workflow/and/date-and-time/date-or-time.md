# Date or Time

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Este cartão DocBits verifica se um valor de data/hora especificado está dentro de um intervalo definido. Permite que os fluxos de trabalho prossigam ou parem consoante a condição seja cumprida, sendo adequado para operações sensíveis ao tempo ou para agendar fluxos de trabalho.

## **Funcionalidade:**

* **Validação de data/hora:** Este cartão avalia se uma determinada data/hora está dentro de um intervalo especificado utilizando as seguintes condições:
  * **Is:** Verifica se a data/hora está dentro do intervalo de início e fim definido (inclusive).
  * **Is Not:** Garante que a data/hora está fora do intervalo definido.

**Intervalo de data/hora:** Os utilizadores especificam os valores de data/hora de início e de fim para definir o intervalo de comparação.

## **Utilização:**

Este cartão é ideal para agendamento, verificações de conformidade ou validação de condições baseadas no tempo nos fluxos de trabalho. Por exemplo, pode ser utilizado para assegurar que as tarefas são executadas apenas durante períodos predefinidos ou para verificar prazos.

## **Exemplo de cenário:**

* Um utilizador configura o cartão para verificar se a **data de submissão** de uma fatura **está entre** **"2024-11-01"** e **"2024-11-30"**. Se a data de submissão estiver dentro deste intervalo, o fluxo de trabalho prossegue para o processamento de pagamento. Caso contrário, o fluxo de trabalho aciona uma notificação para revisão adicional.

Ao utilizar o cartão "Date/Time Range Validation", as organizações podem assegurar um agendamento preciso, reforçar a conformidade e simplificar os fluxos de trabalho ao respeitar restrições de tempo predefinidas.
