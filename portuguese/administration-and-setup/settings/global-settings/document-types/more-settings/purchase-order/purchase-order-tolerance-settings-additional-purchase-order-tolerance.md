# Configurações de tolerância de pedido de compra / Tolerância adicional de pedido de compra

### **Configuração para configurar Tolerâncias de Pedido de Compra**

Vá para **Configurações → Configurações Gerais → Tipos de Documentos → Mais Configurações → Seção de Pedido de Compra → Configuração de Tolerância de PO**

#### **Como Funciona**

Quando ativada, esta configuração permite que você defina tolerâncias para **Quantidade** e/ou **Preço Unitário**. Essas tolerâncias podem ser definidas como uma porcentagem ou como um valor fixo. Isso significa que uma fatura pode desviar do pedido de compra (PO) dentro da faixa de tolerância especificada sem ser sinalizada como uma discrepância, proporcionando flexibilidade enquanto garante um processamento contínuo.

<mark style="color:red;">**NOTA**</mark>: As tolerâncias funcionam em ambas as direções; ou seja, o valor da fatura pode ser maior ou menor que o valor do PO dentro da faixa permitida.

#### **Configurando**

* **Ativar a Configuração:**
  * Ative a Configuração de Tolerância de PO usando o botão de alternância.
* **Configurar Tolerâncias:**
  * Quatro campos aparecerão:
    * Um campo para o **Valor de Tolerância de Quantidade**.
    * Um campo para o **Valor de Tolerância de Preço Unitário**.
  * Atrás de cada campo, há um menu suspenso onde você pode selecionar o tipo de tolerância:
    * **Porcentagem:** Indica uma tolerância percentual.
    * **Valor:** Indica um valor fixo pelo qual o valor pode diferir.

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FT2n2w4uDCJvv7CJ5zrdk%2Fuploads%2Fs661pgIKUsLzwhxU4kes%2Fimage.png?alt=media\&token=6d152cde-14d8-4caf-bcc8-acf1a1fe497c)

#### **Cenário de Exemplo:**

* Suponha que a **Tolerância de Preço Unitário** esteja definida como **5%**.
* O pedido de compra inclui duas linhas:
  * **Linha 1:** Preço Unitário = **$5.00**
  * **Linha 2:** Preço Unitário = **$2.00**
* Na fatura:
  * **Linha 1:** O preço unitário é ajustado para **$4.80** (**dentro** da tolerância de 5%).
  * **Linha 2:** O preço unitário é ajustado para **$2.20** (**fora** da tolerância de 5%).
* **Resultado:**
  * A Linha 1 **não é sinalizada** como uma discrepância porque $4.80 está dentro de 5% de $5.00.
  * A Linha 2 **é sinalizada** como uma discrepância porque $2.20 excede a variação permitida de 5% de $2.00. O usuário agora é obrigado a tomar medidas para resolver a discrepância antes que a fatura possa ser processada.

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FT2n2w4uDCJvv7CJ5zrdk%2Fuploads%2Fn5ki5044GfbGekHWyjhs%2Fimage.png?alt=media\&token=6e1e641b-4d6d-4236-a375-72edcfc98529)

### Configuração para configurar Configurações Adicionais de Tolerância de Pedido de Compra

Vá para **Configurações → Configurações Gerais → Tipos de Documentos → Mais Configurações → Seção de Pedido de Compra → Configuração Adicional de Tolerância de PO**

#### **Como Funciona**

Quando ativada, esta configuração permite que você defina tolerâncias para **Frete**, **Taxas**, e/ou **Imposto**. Essas tolerâncias podem ser definidas como uma porcentagem ou como um valor fixo, permitindo que as faturas variem ligeiramente dos valores do PO sem serem sinalizadas como discrepâncias. Isso proporciona flexibilidade adicional e garante que pequenas diferenças não interrompam o fluxo de trabalho.

<mark style="color:red;">**NOTA**</mark>: Assim como as configurações de tolerância padrão, essas tolerâncias se aplicam em ambas as direções—permitindo aumentos ou diminuições dentro dos limites estabelecidos.

#### **Configurando**

* **Ativar a Configuração:**
  * Ative a Configuração Adicional de Tolerância de PO usando o botão de alternância.
* **Configurar Tolerâncias:**
  * Seis campos se tornarão visíveis:
    * Um campo para cada um dos valores de tolerância para **Frete**, **Taxas**, e **Imposto**.
  * Cada campo tem um menu suspenso correspondente onde você pode escolher o tipo de tolerância:
    * **Porcentagem:** A tolerância é definida como uma porcentagem.
    * **Valor:** A tolerância é definida como um valor fixo.

<figure><img src="../../../../../../.gitbook/assets/docbits_docbits_image_5.png" alt="DocBits DocBits Imagem 5"><figcaption></figcaption></figure>
