# AI Calculation for Cost Increase Surcharges

<figure><img src="../../../../.gitbook/assets/image (309).png" alt="" width="563"><figcaption></figcaption></figure>

## Propósito:

O cartão de fluxo de trabalho **"AI Calculation for Cost Increase Surcharges"** utiliza IA para calcular automaticamente os valores de sobretaxa com base em aumentos de custos. Assegura cálculos de sobretaxa consistentes e precisos, simplificando os fluxos de trabalho e reduzindo o esforço manual.

## Componentes do cartão:

* **Cost Increase Factor**
  * **Descrição:** O multiplicador ou percentagem aplicado ao custo base para calcular a sobretaxa.
  * **Detalhe:** Determina o valor da sobretaxa com base no aumento de custo (por exemplo, um fator de 1,10 para um aumento de 10%).
* **Base Cost Field**
  * **Descrição:** O campo que contém o valor de custo original utilizado como base para o cálculo da sobretaxa.
  * **Detalhe:** Selecionado automaticamente ou definido dentro do fluxo de trabalho para referência durante o cálculo.
* **Surcharge Field**
  * **Descrição:** O campo onde é armazenado o valor de sobretaxa calculado pela IA.
  * **Detalhe:** Este campo reflete a sobretaxa calculada, tornando-a disponível para processamento ou relatórios adicionais.

## Funcionalidade:

**Avaliação da condição:**

* O cartão é ativado apenas se tanto as condições da secção **"Where"** como das **"And Sections"** forem avaliadas como verdadeiras.
* Se alguma das condições for avaliada como falsa, não é realizado qualquer cálculo de sobretaxa.

**Cálculo orientado por IA:**

* O sistema aplica o **Cost Increase Factor** ao **Base Cost Field** para calcular a sobretaxa.
* O resultado é armazenado no **Surcharge Field**, assegurando a acessibilidade para os passos subsequentes do fluxo de trabalho.

## Conclusão:

O cartão de fluxo de trabalho **"AI Calculation for Cost Increase Surcharges"** automatiza a aplicação de sobretaxas com base em aumentos de custos. Ao recorrer à IA para precisão e consistência, este cartão elimina cálculos manuais, aumenta a eficiência e apoia uma gestão de custos rigorosa em fluxos de trabalho automatizados.
