# Any / All Charges

<figure><img src="../../../../.gitbook/assets/workflow_cards_and_po_compare_any_all_charges.png" alt="O cartão na biblioteca de cartões, versão 2 e versão 3"><figcaption><p>O cartão na biblioteca de cartões. Versão 2 acima, versão 3 abaixo.</p></figcaption></figure>

## **Objetivo:**

Este cartão de fluxo de trabalho compara os encargos adicionais de um documento com os encargos adicionais da ordem de compra correspondente, dentro de uma tolerância definida. Responde a uma única pergunta: o documento e a ordem de compra concordam quanto aos encargos adicionais? É comparado cada encargo que a correspondência da ordem de compra emparelhou, pelo que não é necessário indicar qualquer nome de campo no cartão.

Este cartão distingue-se de **Compare Total Charges**, que compara um único campo do documento com um só encargo identificado por um Charge ID. Utilize este cartão quando todos os encargos emparelhados do documento devam ser verificados de uma só vez.

A correspondência da ordem de compra tem de ser executada antes deste cartão. Se o documento não tiver uma ordem de compra correspondente, o cartão interrompe o fluxo de trabalho e comunica dados ausentes.

## **Componentes do cartão:**

1. **Qualquer/Todos:**
   * **Descrição**: Como as comparações de encargos individuais são reunidas no único resultado do cartão.
   * **Opções**:
     * **Qualquer**: pelo menos um encargo tem de satisfazer a comparação.
     * **Todos**: cada encargo tem de satisfazer a comparação.
2. **Operador:**
   * **Descrição**: Como o montante do encargo do documento é comparado com o montante da ordem de compra para o mesmo encargo.
   * **Opções**:
     * **dentro de**: os dois montantes têm de concordar, admitindo a tolerância.
     * **Fora**: os dois montantes têm de diferir em mais do que a tolerância.
3. **Quantidade de Tolerância:**
   * **Descrição**: O desvio admitido entre o encargo do documento e o encargo da ordem de compra.
4. **Tipo de tolerância:**
   * **Descrição**: Como a quantidade de tolerância é interpretada.
   * **Opções**:
     * **Por cento**: uma percentagem do encargo da ordem de compra.
     * **Valor**: um montante fixo.
5. **Comportamento de dados ausentes (apenas versão 3):**
   * **Descrição**: O que fazer quando um encargo existe apenas de um lado, no documento ou na ordem de compra, de modo que não há contraparte com que o comparar. A opção situa-se no fim da frase da versão 3.
   * **Opções**:
     * **tratar como uma incompatibilidade**: o fluxo de trabalho para. É a predefinição.
     * **ignore e trate como uma correspondência.**: o fluxo de trabalho continua como se o encargo tivesse concordado.

## **Funcionalidade:**

O cartão percorre os passos seguintes.

1. **Exige uma ordem de compra correspondente.** Sem ordem de compra correspondente, o cartão para imediatamente e comunica dados ausentes.
2. **Lê a tolerância** de **Quantidade de Tolerância** e **Tipo de tolerância** no cartão.
3. **A versão 3 classifica cada linha de ordem de compra emparelhada** numa de quatro situações, perguntando apenas se cada lado tem algum encargo: encargos em ambos os lados, nenhum encargo em qualquer dos lados, encargos apenas no documento, ou encargos apenas na ordem de compra. Uma linha que não possa ser associada aos dados da ordem de compra do documento é um erro de dados e o cartão para.
4. **Um encargo presente apenas de um lado decide todo o cartão.** Assim que uma linha emparelhada tem encargos de um lado e nenhum do outro, **Comportamento de dados ausentes** decide o resultado e nenhum encargo é comparado, nem mesmo os encargos das linhas corretamente emparelhadas. O operador e a tolerância não são consultados.
5. **Se nenhuma linha tiver encargos em qualquer dos dois lados**, ambos os lados concordam que não existem encargos adicionais. O operador **Fora** não fica assim satisfeito, porque nada difere além da tolerância, e o fluxo de trabalho para. Qualquer outro operador considera a concordância satisfeita e o fluxo de trabalho continua. **Comportamento de dados ausentes** não tem efeito aqui.
6. **Caso contrário cada encargo é comparado**, montante do documento contra montante da ordem de compra, com o operador e a tolerância. Um montante de encargo que não seja um número para o cartão com dados ausentes.
7. **As comparações são reunidas e combinadas uma só vez.** Cada encargo de cada linha emparelhada contribui para um único conjunto de resultados, que a definição **Qualquer/Todos** reduz ao único resultado do cartão. A reunião é à escala do documento, não por linha, pelo que **Qualquer** significa qualquer encargo em qualquer ponto do documento. Se o resultado combinado for verdadeiro o fluxo de trabalho continua, caso contrário para com uma condição não satisfeita.

Vale a pena conhecer três consequências antes de configurar o cartão.

* **dentro de com uma tolerância de 0 exige igualdade exata.** Os dois montantes têm de concordar ao cêntimo.
* **Um encargo presente apenas de um lado prevalece sobre tudo o resto.** Como o passo 4 é executado antes de qualquer comparação, **ignore e trate como uma correspondência.** também salta a verificação de montantes de cada encargo corretamente emparelhado do documento. Mantenha **tratar como uma incompatibilidade** se os montantes tiverem de ser verificados.
* **tratar como uma incompatibilidade para o fluxo de trabalho como erro, não como condição não satisfeita.** Apesar da formulação, o cartão comunica dados ausentes, o que o registo do fluxo de trabalho e o teste do cartão mostram em vermelho e não em laranja como uma condição não satisfeita. O fluxo de trabalho para em ambos os casos.

## **Instalação e configuração:**

Adicione o cartão como condição And após a correspondência da ordem de compra. Escolha se cada encargo ou qualquer encargo tem de satisfazer a comparação, escolha o operador **dentro de** ou **Fora** e introduza a quantidade e o tipo de tolerância. Na versão 3, escolha o que deve acontecer quando os encargos surgem apenas de um lado.

Para experimentar uma configuração sem esperar por um documento, abra o menu do cartão no Workflow Builder, escolha **Cartão de teste**, escolha um documento e depois **Teste no documento**. O registo do cartão enumera cada encargo comparado com ambos os montantes, o operador e a tolerância utilizada, e registra também qual o valor de **Comportamento de dados ausentes** que decidiu o resultado quando um encargo estava presente apenas de um lado.

## **Cenário de exemplo:**

Uma confirmação de encomenda tem um encargo de transporte de 100,00 e a linha de ordem de compra correspondente tem o mesmo encargo de transporte de 100,00. Com **Todos**, o operador **dentro de** e uma tolerância de 0 como valor, os montantes são iguais, o cartão fica satisfeito e o fluxo de trabalho continua.

Com 120,00 na confirmação de encomenda contra 100,00 na ordem de compra, a mesma configuração não fica satisfeita e o fluxo de trabalho para com uma condição não satisfeita.

Se nem a confirmação de encomenda nem a ordem de compra tiverem qualquer encargo, o operador **dentro de** considera isso concordância e o fluxo de trabalho continua, enquanto **Fora** o para.

Se a confirmação de encomenda tiver um encargo de transporte e a ordem de compra nenhum, o operador deixa de se aplicar. Com **tratar como uma incompatibilidade** o fluxo de trabalho para, para que alguém possa verificar por que razão o encargo consta apenas de um lado.

## **Diferenças entre versões:**

A versão 3 é a que os cartões novos usam. A versão 2 continua suportada nos fluxos de trabalho existentes. Ambas as versões comparam encargo por encargo e combinam os resultados à escala do documento com a definição **Qualquer/Todos**, mas a versão 2 não tem classificação por casos, o que altera o que acontece assim que os encargos não estão presentes em ambos os lados:

* A versão 2 não tem a opção **Comportamento de dados ausentes**. A sua frase termina após o tipo de tolerância.
* A versão 2 não classifica as linhas emparelhadas e por isso não reconhece um encargo que existe apenas de um lado. Compara o montante presente contra o 0,00 mantido para o lado ausente, e o operador decide: **dentro de** não fica satisfeito e o fluxo de trabalho para, **Fora** fica satisfeito e o fluxo de trabalho continua. O registo do cartão mostra a comparação contra 0,00.
* Se nenhum dos dois lados tiver encargos, a versão 2 não tem nada a comparar e comunica dados ausentes em vez de considerar a ausência em ambos os lados como concordância.

## **Conclusão:**

O cartão "Any / All Charges" automatiza a verificação de que os encargos adicionais faturados ou confirmados correspondem aos encargos adicionais encomendados. Como a ausência de encargos em ambos os lados conta como concordância na versão 3, os documentos sem encargos adicionais passam sem intervenção manual, enquanto os encargos que surgem apenas de um lado são retidos para revisão, salvo se isso for deliberadamente permitido.
