# Key Concept: Tolerance Window

Antes de analisar os operadores, é importante compreender como a janela de tolerância é calculada.

## O que é uma janela de tolerância?

A janela de tolerância define um intervalo de datas aceitáveis em torno da data de entrega prometida da ordem de compra.

**Exemplo:**

* Data da Ordem de Compra: **9 de janeiro**
* Tolerance Days: **3**
* Janela de Tolerância: **6 de janeiro → 12 de janeiro**

> <mark style="color:red;">Apenas os</mark> <mark style="color:red;"></mark><mark style="color:red;">**Allowed Tolerance Days**</mark> <mark style="color:red;"></mark><mark style="color:red;">selecionados (dias da semana) são contabilizados ao calcular esta janela.</mark>

### Exemplo de cronologia visual

```
← Passado                         Futuro →
|-----|-----|-----|-----|-----|-----|-----|
     6 Jan      9 Jan      12 Jan
   (Início)   (Data PO)     (Fim)
```

### Comportamento dos operadores explicado com exemplos

* **Equals (=)**
  * **Significado:**\
    A data de entrega da linha de item tem de estar _dentro_ da janela de tolerância.
  * **Datas válidas:**
    * Qualquer data entre **6 de janeiro e 12 de janeiro** (inclusive)
  * **Datas inválidas:**
    * Qualquer data **antes de 6 de janeiro**
    * Qualquer data **depois de 12 de janeiro**
* **Not Equals (≠)**
  * **Significado:**\
    A data de entrega da linha de item tem de estar _fora_ da janela de tolerância.
  * **Datas válidas:**
    * Qualquer data **antes de 6 de janeiro**
    * Qualquer data **depois de 12 de janeiro**
  * **Datas inválidas:**
    * Datas entre **6 de janeiro e 12 de janeiro**
* **Greater or Equals (≥)**
  * **Significado:**\
    A data de entrega da linha de item tem de ser igual ou posterior ao **início da janela de tolerância**.
  * **Datas válidas:**
    * **6 de janeiro → qualquer data futura**
  * **Datas inválidas:**
    * Qualquer data **antes de 6 de janeiro**
  * <mark style="color:red;">**Importante:**</mark>\
    Este operador permite datas _dentro_ da janela de tolerância **e para além dela**.
* **Lesser or Equals (≤)**
  * **Significado:**\
    A data de entrega da linha de item tem de ser igual ou anterior ao **fim da janela de tolerância**.
  * **Datas válidas:**
    * Qualquer data passada até **12 de janeiro**
  * **Datas inválidas:**
    * Qualquer data **depois de 12 de janeiro**
* **Greater Than (>)**
  * **Significado:**\
    A data de entrega da linha de item tem de ser _estritamente posterior_ à janela de tolerância.
  * **Datas válidas:**
    * **13 de janeiro → qualquer data futura**
  * **Datas inválidas:**
    * Qualquer data **igual ou anterior a 12 de janeiro**
* **Lesser Than (<)**
  * **Significado:**\
    A data de entrega da linha de item tem de ser _estritamente anterior_ à janela de tolerância.
  * **Datas válidas:**
    * Qualquer data **antes de 6 de janeiro**
  * **Datas inválidas:**
    * Qualquer data **igual ou posterior a 6 de janeiro**

## Como os "Allowed Tolerance Days" afetam a janela de tolerância

Ao calcular a janela de tolerância, **apenas os dias da semana selecionados são contabilizados**.\
Os dias que não estão selecionados (como fins de semana ou dias da semana excluídos) são **totalmente ignorados**.

#### Exemplo: cálculo de tolerância com base nos dias da semana

**Configuração:**

* Data da Ordem de Compra: **quarta-feira, 9 de janeiro**
* Tolerance Days: **3**
* Allowed Tolerance Days: **segunda, terça, quarta, quinta, sexta**
* Fins de semana (sábado, domingo): **Não selecionados**

#### Cálculo passo a passo

A começar pela data da PO (**9 de janeiro**):

**Contando para trás (3 dias de tolerância):**

* Terça, 8 de janeiro → **Dia 1**
* Segunda, 7 de janeiro → **Dia 2**
* Domingo, 6 de janeiro → _Ignorado (não permitido)_
* Sábado, 5 de janeiro → _Ignorado (não permitido)_
* Sexta, 4 de janeiro → **Dia 3**

➡ **Data de início da tolerância: sexta-feira, 4 de janeiro**

**Contando para a frente (3 dias de tolerância):**

* Quinta, 10 de janeiro → **Dia 1**
* Sexta, 11 de janeiro → **Dia 2**
* Sábado, 12 de janeiro → _Ignorado_
* Domingo, 13 de janeiro → _Ignorado_
* Segunda, 14 de janeiro → **Dia 3**

➡ **Data de fim da tolerância: segunda-feira, 14 de janeiro**

#### Janela de tolerância resultante

```
4 de janeiro  →  14 de janeiro
```

#### Porque é que isto é importante

Se os Allowed Tolerance Days estiverem configurados incorretamente:

* As datas de entrega podem parecer **inesperadamente válidas ou inválidas**
* As entregas antecipadas ou atrasadas podem não ser detetadas corretamente
